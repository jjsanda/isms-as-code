"""The release build: validate -> generate -> render -> sign -> manifest -> verify."""

from __future__ import annotations

import shutil
from dataclasses import dataclass, field
from pathlib import Path

from isms_as_code.generate import build_artefacts, write_artefacts
from isms_as_code.loader import Repository
from isms_as_code.manifest import verify_manifest, write_manifest
from isms_as_code.render import RenderResult, render_all
from isms_as_code.signing import KeyMaterial, SignatureReport, sign_pdf, verify_pdf

__all__ = [
    "BuildReport",
    "CERT_NAME",
    "clean_outputs",
    "run_build",
    "sign_outputs",
    "verify_outputs",
]

CERT_NAME = "signing-trust-anchor.pem"


@dataclass
class BuildReport:
    rendered: list[RenderResult] = field(default_factory=list)
    signatures: list[SignatureReport] = field(default_factory=list)
    manifest_problems: list[str] = field(default_factory=list)
    generated: list[Path] = field(default_factory=list)
    ephemeral_key: bool = False

    @property
    def ok(self) -> bool:
        return all(r.ok for r in self.signatures) and not self.manifest_problems


def clean_outputs(out: Path) -> None:
    """Remove the outputs of a previous build so stale files (old versions, old keys) cannot linger."""
    for sub in ("pdf", "html"):
        shutil.rmtree(out / sub, ignore_errors=True)
    for name in ("SHA256SUMS", CERT_NAME):
        (out / name).unlink(missing_ok=True)


def _reason_for(repo: Repository, stem: str, material: KeyMaterial) -> str:
    prefix = "DEVELOPMENT BUILD (untrusted key): " if material.ephemeral else ""
    for document in repo.documents:
        if stem.startswith(document.folder.name + "-v"):
            return (
                f"{prefix}{document.meta.id} version {document.meta.version} "
                f"({document.meta.status.value}) rendered from the repository sources"
            )
    return f"{prefix}generated artefact '{stem}' rendered from the repository sources"


def sign_outputs(repo: Repository, out: Path, material: KeyMaterial) -> list[SignatureReport]:
    """Sign every unsigned PDF under ``out/pdf`` and write the public certificate next to them."""
    reports: list[SignatureReport] = []
    (out / CERT_NAME).write_bytes(material.trust_anchor_pem)
    location = f"{repo.organisation.group_name} — ISMS release pipeline"
    contact = repo.roles.get(repo.organisation.isms_owner).email
    for pdf in sorted((out / "pdf").glob("*.pdf")):
        existing = verify_pdf(pdf)
        if existing.signed:
            # Already signed (possibly by an earlier key): keep it, report integrity only.
            reports.append(existing)
            continue
        sign_pdf(
            pdf,
            pdf,
            material,
            reason=_reason_for(repo, pdf.stem, material),
            location=location,
            contact=contact,
        )
        reports.append(verify_pdf(pdf, material.certificate_pem))
    return reports


def verify_outputs(
    out: Path, trust_pem: bytes | None = None
) -> tuple[list[SignatureReport], list[str]]:
    anchor = trust_pem
    if anchor is None and (out / CERT_NAME).is_file():
        anchor = (out / CERT_NAME).read_bytes()
    pdf_dir = out / "pdf" if (out / "pdf").is_dir() else out
    reports = [verify_pdf(pdf, anchor) for pdf in sorted(pdf_dir.glob("*.pdf"))]
    return reports, verify_manifest(out)


def run_build(
    repo: Repository, out: Path, material: KeyMaterial, *, include_guides: bool = True
) -> BuildReport:
    report = BuildReport(ephemeral_key=material.ephemeral)
    clean_outputs(out)
    report.generated = write_artefacts(repo.root, build_artefacts(repo))
    report.rendered = render_all(repo, out, include_guides=include_guides)
    report.signatures = sign_outputs(repo, out, material)
    write_manifest(out)
    report.signatures, report.manifest_problems = verify_outputs(out, material.trust_anchor_pem)
    return report
