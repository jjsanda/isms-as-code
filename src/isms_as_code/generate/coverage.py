"""Coverage reports: how far an external requirement set is met by controls and documents."""

from __future__ import annotations

from collections import Counter

from isms_as_code.generate.common import document_link, guide_link, md_header, status_label, table
from isms_as_code.loader import Repository
from isms_as_code.models import (
    Applicability,
    DocumentStatus,
    ImplementationStatus,
    Mapping,
    MappingRequirement,
)

__all__ = ["render_coverage", "requirement_verdict"]

FULL, PARTIAL, GAP = "covered", "partial", "gap"


def _control_verdict(repo: Repository, control_id: str) -> str:
    guide = repo.controls_by_id().get(control_id)
    if guide is None or guide.meta.applicability is Applicability.NOT_APPLICABLE:
        return GAP
    if guide.meta.implementation_status is ImplementationStatus.IMPLEMENTED:
        return FULL
    if guide.meta.implementation_status is ImplementationStatus.NOT_IMPLEMENTED:
        return GAP
    return PARTIAL


def _document_verdict(repo: Repository, document_id: str) -> str:
    document = repo.documents_by_id().get(document_id)
    if document is None or document.meta.status is DocumentStatus.RETIRED:
        return GAP
    if document.meta.status is DocumentStatus.APPROVED:
        return FULL
    return PARTIAL


def requirement_verdict(repo: Repository, requirement: MappingRequirement) -> str:
    verdicts = [_control_verdict(repo, c) for c in requirement.controls]
    verdicts += [_document_verdict(repo, d) for d in requirement.documents]
    if not verdicts or GAP in verdicts:
        return GAP
    if PARTIAL in verdicts:
        return PARTIAL
    return FULL


def render_coverage(repo: Repository, mapping: Mapping, digest: str) -> str:
    guides = repo.controls_by_id()
    documents = repo.documents_by_id()
    verdicts = {req.id: requirement_verdict(repo, req) for req in mapping.requirements}
    counts = Counter(verdicts.values())
    out = md_header(digest)
    out += f"# Coverage — {mapping.title}\n\n"
    out += f"**Source.** {mapping.source}\n\n{mapping.description.strip()}\n\n"
    out += "## Summary\n\n"
    out += table(
        ["Requirements", "Covered", "Partial", "Gap"],
        [
            [
                len(mapping.requirements),
                counts.get(FULL, 0),
                counts.get(PARTIAL, 0),
                counts.get(GAP, 0),
            ]
        ],
    )
    out += (
        "\n*Covered* = every mapped control is applicable and implemented and every mapped document is "
        "approved; *partial* = at least one mapped control is partially implemented or planned, or a "
        "mapped document is still a draft or in review; *gap* = a mapped control is not applicable or "
        "not implemented, or a document is missing or retired.\n\n"
    )
    out += "## Requirements\n\n"
    rows: list[list[object]] = []
    for req in mapping.requirements:
        controls = ", ".join(
            f"{guide_link(repo, guides[c])} ({status_label(guides[c].meta.implementation_status) if guides[c].meta.is_applicable else 'not applicable'})"
            for c in req.controls
            if c in guides
        )
        docs = ", ".join(
            f"{document_link(repo, documents[d])} ({documents[d].meta.status.value})"
            for d in req.documents
            if d in documents
        )
        verdict = verdicts[req.id]
        rows.append(
            [
                f"**{req.id}**",
                req.title,
                controls or "—",
                docs or "—",
                {FULL: "✅ covered", PARTIAL: "🟡 partial", GAP: "❌ gap"}[verdict],
                req.notes or "",
            ]
        )
    out += table(["Requirement", "Title", "Controls", "Documents", "Coverage", "Notes"], rows)
    return out
