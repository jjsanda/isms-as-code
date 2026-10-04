from __future__ import annotations

import base64
from pathlib import Path

import pytest

from isms_as_code.loader import load_repository
from isms_as_code.manifest import verify_manifest, write_manifest
from isms_as_code.signing import (
    DEV_COMMON_NAME,
    SIGNING_AVAILABLE,
    from_pkcs12,
    generate_key_material,
    load_key_material,
    sign_pdf,
    to_pkcs12,
    verify_pdf,
)
from tests.conftest import RepoBuilder

pytestmark = [
    pytest.mark.signing,
    pytest.mark.skipif(not SIGNING_AVAILABLE, reason="pdf extra missing"),
]


def test_key_material_round_trips_through_pkcs12(tmp_path: Path) -> None:
    material = generate_key_material("Test Signer", "Test Org", days=30)
    assert "CN=Test Signer" in material.subject and not material.ephemeral
    data = to_pkcs12(material, "secret")
    restored = from_pkcs12(data, "secret")
    assert restored.certificate_pem == material.certificate_pem
    assert restored.trust_anchor_pem == material.trust_anchor_pem
    with pytest.raises(ValueError):
        from_pkcs12(data, "wrong")
    p12 = tmp_path / "k.p12"
    p12.write_bytes(data)
    assert load_key_material(p12, "secret").subject == material.subject
    env = {"ISMS_SIGNING_P12": base64.b64encode(data).decode(), "ISMS_SIGNING_PASSPHRASE": "secret"}
    assert load_key_material(env=env).subject == material.subject
    ephemeral = load_key_material(env={})
    assert ephemeral.ephemeral and DEV_COMMON_NAME in ephemeral.subject


def test_sign_and_verify_pdf(builder: RepoBuilder, tmp_path: Path) -> None:
    from isms_as_code.render import PDF_AVAILABLE, render_all

    if not PDF_AVAILABLE:
        pytest.skip("WeasyPrint not available")
    repo = load_repository(builder.root)
    result = render_all(repo, tmp_path / "dist", only={"POL-TEST"}, include_guides=False)[0]
    assert result.pdf_path is not None
    unsigned = verify_pdf(result.pdf_path)
    assert not unsigned.signed and "NOT SIGNED" in unsigned.summary()
    material = generate_key_material("Unit Test Signer", "Test Org", days=30)
    sign_pdf(
        result.pdf_path,
        result.pdf_path,
        material,
        reason="unit test",
        location="here",
        contact="a@b.test",
    )
    anchored = verify_pdf(result.pdf_path, material.trust_anchor_pem)
    assert (
        anchored.ok
        and anchored.trusted
        and anchored.anchored
        and anchored.coverage == "ENTIRE_FILE"
    )
    assert anchored.reason == "unit test" and "Unit Test Signer" in anchored.signer
    assert anchored.signing_time is not None
    assert "valid, trusted, entire_file" in anchored.summary()
    unanchored = verify_pdf(result.pdf_path)
    assert unanchored.ok and not unanchored.anchored
    other = generate_key_material("Someone Else", "Other Org", days=30)
    assert not verify_pdf(result.pdf_path, other.trust_anchor_pem).ok
    tampered = result.pdf_path.read_bytes() + b"\n%tamper\n"
    result.pdf_path.write_bytes(tampered)
    assert not verify_pdf(result.pdf_path, material.trust_anchor_pem).ok


def test_manifest_round_trip_and_tamper_detection(tmp_path: Path) -> None:
    dist = tmp_path / "dist"
    (dist / "pdf").mkdir(parents=True)
    (dist / "pdf" / "a.pdf").write_bytes(b"%PDF-1.7 a")
    (dist / "b.txt").write_text("b", encoding="utf-8")
    manifest = write_manifest(dist)
    text = manifest.read_text(encoding="utf-8")
    assert text.endswith("pdf/a.pdf\n") and "b.txt" in text
    assert verify_manifest(dist) == []
    (dist / "b.txt").write_text("changed", encoding="utf-8")
    (dist / "c.txt").write_text("new", encoding="utf-8")
    (dist / "pdf" / "a.pdf").unlink()
    problems = verify_manifest(dist)
    assert any("hash mismatch" in p for p in problems)
    assert any("not listed" in p for p in problems)
    assert any("missing" in p for p in problems)
    manifest.unlink()
    assert verify_manifest(dist) == ["SHA256SUMS is missing"]
