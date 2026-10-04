"""Shields-compatible endpoint JSON so the README badges reflect the repository's own data."""

from __future__ import annotations

from isms_as_code.generate.soa import soa_rows
from isms_as_code.integrity import canonical_json
from isms_as_code.loader import Repository
from isms_as_code.models import DocumentStatus, ImplementationStatus

__all__ = ["render_badges"]


def _badge(label: str, message: str, color: str) -> str:
    return canonical_json({"schemaVersion": 1, "label": label, "message": message, "color": color})


def render_badges(repo: Repository) -> dict[str, str]:
    rows = soa_rows(repo)
    applicable = [r for r in rows if r.applicable]
    implemented = sum(1 for r in applicable if r.status is ImplementationStatus.IMPLEMENTED)
    share = round(100 * implemented / len(applicable)) if applicable else 0
    approved = sum(1 for d in repo.documents if d.meta.status is DocumentStatus.APPROVED)
    badges = {
        "documents": _badge("documents", f"{len(repo.documents)} ({approved} approved)", "blue"),
        "annex-a": _badge(
            "Annex A 2022", f"{len(applicable)}/{len(rows)} applicable", "informational"
        ),
        "implemented": _badge(
            "controls implemented",
            f"{share} %",
            "brightgreen" if share >= 90 else "green" if share >= 75 else "yellow",
        ),
        "risks": _badge("risks", f"{len(repo.risks.risks)} in register", "blue"),
    }
    for mapping in repo.mappings:
        from isms_as_code.generate.coverage import FULL, requirement_verdict

        covered = sum(1 for r in mapping.requirements if requirement_verdict(repo, r) == FULL)
        total = len(mapping.requirements)
        badges[mapping.name] = _badge(
            mapping.name,
            f"{covered}/{total} covered",
            "brightgreen" if covered == total else "yellow",
        )
    return badges
