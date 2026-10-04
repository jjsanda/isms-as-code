"""Derived artefacts — generated from the sources, committed, and drift-checked in CI.

Every generator is a pure function ``(Repository, digest) -> str``. The orchestrator stamps each
output with the *source digest* (a SHA-256 over the inputs, never a timestamp), so re-running on an
unchanged tree is byte-identical and ``isms generate --check`` can diff the committed files against
a fresh run.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from isms_as_code import layout
from isms_as_code.generate.badges import render_badges
from isms_as_code.generate.codeowners import render_codeowners
from isms_as_code.generate.coverage import render_coverage
from isms_as_code.generate.register import render_register
from isms_as_code.generate.risk_view import render_risk_view
from isms_as_code.generate.scope import render_scope
from isms_as_code.generate.soa import render_soa, render_soa_csv
from isms_as_code.integrity import source_digest
from isms_as_code.loader import Repository

__all__ = ["Artefact", "build_artefacts", "write_artefacts", "check_artefacts", "compute_digest"]


@dataclass(frozen=True)
class Artefact:
    """One generated file: path relative to the repository root and its full content."""

    relpath: Path
    content: str


def compute_digest(repo: Repository) -> str:
    return source_digest(repo.source_paths(), repo.root)


def build_artefacts(repo: Repository) -> list[Artefact]:
    """Render every derived artefact in a fixed order."""
    digest = compute_digest(repo)
    generated = layout.GENERATED_DIR
    artefacts = [
        Artefact(generated / "statement-of-applicability.md", render_soa(repo, digest)),
        Artefact(generated / "statement-of-applicability.csv", render_soa_csv(repo)),
        Artefact(generated / "isms-scope-statement.md", render_scope(repo, digest)),
        Artefact(generated / "document-register.md", render_register(repo, digest)),
        Artefact(generated / "risk-register.md", render_risk_view(repo, digest)),
    ]
    for entity in repo.organisation.in_scope_entities():
        artefacts.append(
            Artefact(generated / "soa" / f"{entity.id}.md", render_soa(repo, digest, entity.id))
        )
    for mapping in repo.mappings:
        artefacts.append(
            Artefact(
                generated / f"coverage-{mapping.name}.md", render_coverage(repo, mapping, digest)
            )
        )
    artefacts.append(Artefact(layout.CODEOWNERS, render_codeowners(repo, digest)))
    for name, content in render_badges(repo).items():
        artefacts.append(Artefact(generated / "badges" / f"{name}.json", content))
    return artefacts


def write_artefacts(root: Path, artefacts: list[Artefact]) -> list[Path]:
    written: list[Path] = []
    for artefact in artefacts:
        path = root / artefact.relpath
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(artefact.content, encoding="utf-8")
        written.append(path)
    return written


def check_artefacts(root: Path, artefacts: list[Artefact]) -> list[str]:
    """Return the relative paths whose committed content differs from a fresh render."""
    stale: list[str] = []
    for artefact in artefacts:
        path = root / artefact.relpath
        if not path.is_file() or path.read_text(encoding="utf-8") != artefact.content:
            stale.append(artefact.relpath.as_posix())
    return stale
