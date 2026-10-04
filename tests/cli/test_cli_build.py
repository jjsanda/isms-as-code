from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

from isms_as_code.cli import app
from isms_as_code.render import PDF_AVAILABLE
from isms_as_code.signing import SIGNING_AVAILABLE
from tests.conftest import RepoBuilder

pytestmark = [
    pytest.mark.cli,
    pytest.mark.skipif(not (PDF_AVAILABLE and SIGNING_AVAILABLE), reason="pdf extra missing"),
]

runner = CliRunner()


def test_render_sign_verify_and_build(
    builder: RepoBuilder, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.delenv("ISMS_SIGNING_P12", raising=False)
    out = tmp_path / "dist"
    result = runner.invoke(
        app,
        [
            "render",
            "--root",
            str(builder.root),
            "--out",
            str(out),
            "--only",
            "POL-TEST",
            "--no-guides",
        ],
    )
    assert result.exit_code == 0, result.output
    assert (out / "pdf" / "POL-TEST-test-policy-v1.0.0.pdf").is_file()
    result = runner.invoke(app, ["verify", "--out", str(out)])
    assert result.exit_code == 1 and "NOT SIGNED" in result.output
    result = runner.invoke(app, ["sign", "--root", str(builder.root), "--out", str(out)])
    assert result.exit_code == 0, result.output
    assert "EPHEMERAL" in result.output and (out / "signing-trust-anchor.pem").is_file()
    result = runner.invoke(app, ["sign", "--root", str(builder.root), "--out", str(out)])
    assert result.exit_code == 0  # already signed PDFs are left alone
    result = runner.invoke(app, ["verify", "--out", str(out)])
    assert result.exit_code == 1 and "SHA256SUMS is missing" in result.output
    result = runner.invoke(
        app, ["build", "--root", str(builder.root), "--out", str(tmp_path / "build"), "--no-guides"]
    )
    assert result.exit_code == 0, result.output
    assert "build OK" in result.output and (tmp_path / "build" / "SHA256SUMS").is_file()
    result = runner.invoke(app, ["verify", "--out", str(tmp_path / "build")])
    assert result.exit_code == 0 and "manifest intact" in result.output


def test_keygen(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("ISMS_SIGNING_PASSPHRASE", raising=False)
    assert runner.invoke(app, ["keygen", "--out", str(tmp_path)]).exit_code == 2
    result = runner.invoke(
        app,
        ["keygen", "--out", str(tmp_path), "--passphrase", "pw", "--common-name", "Test Control"],
    )
    assert result.exit_code == 0, result.output
    assert (tmp_path / "isms-signing.p12").is_file() and (
        tmp_path / "isms-signing-trust-anchor.pem"
    ).is_file()
