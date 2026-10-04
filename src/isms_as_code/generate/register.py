"""The document register (clause 7.5.3): every controlled document, its state and its review clock."""

from __future__ import annotations

from collections import Counter

from isms_as_code.durations import Duration
from isms_as_code.generate.common import document_link, md_header, role_title, table
from isms_as_code.loader import Document, Repository
from isms_as_code.models import DocumentStatus, DocumentType, Theme

__all__ = ["render_register"]

_TYPE_ORDER = {DocumentType.POLICY: 0, DocumentType.STANDARD: 1, DocumentType.PROCEDURE: 2}
_PLURAL = {
    DocumentType.POLICY: "Policies",
    DocumentType.STANDARD: "Standards",
    DocumentType.PROCEDURE: "Procedures",
}


def _sorted(documents: tuple[Document, ...]) -> list[Document]:
    return sorted(documents, key=lambda d: (_TYPE_ORDER[d.meta.type], d.meta.id))


def render_register(repo: Repository, digest: str) -> str:
    documents = _sorted(repo.documents)
    out = md_header(digest)
    out += f"# Document register — {repo.organisation.group_name}\n\n"
    out += (
        "The register of documented information of the ISMS (ISO/IEC 27001:2022 clause 7.5.3): "
        "every policy, standard and procedure with its status, version, ownership and review clock, "
        "generated from the front matter of the documents. The authoritative version of each document "
        "is the one on the `main` branch; signed PDFs are published with every release.\n\n"
    )
    out += "## Summary\n\n"
    rows: list[list[object]] = []
    for doc_type in (DocumentType.POLICY, DocumentType.STANDARD, DocumentType.PROCEDURE):
        subset = [d for d in documents if d.meta.type is doc_type]
        counts = Counter(d.meta.status for d in subset)
        rows.append(
            [
                _PLURAL[doc_type],
                len(subset),
                counts.get(DocumentStatus.APPROVED, 0),
                counts.get(DocumentStatus.IN_REVIEW, 0),
                counts.get(DocumentStatus.DRAFT, 0),
                counts.get(DocumentStatus.RETIRED, 0),
            ]
        )
    out += table(["Type", "Total", "Approved", "In review", "Draft", "Retired"], rows) + "\n"

    out += "## Controlled documents\n\n"
    out += table(
        [
            "Id",
            "Title",
            "Type",
            "Status",
            "Version",
            "Classification",
            "Owner",
            "Approver",
            "Effective",
            "Last reviewed",
            "Cycle",
            "Next review",
        ],
        [
            [
                document_link(repo, d),
                d.meta.title,
                d.meta.type.value,
                d.meta.status.value,
                d.meta.version,
                d.meta.classification.value,
                role_title(repo, d.meta.owner),
                role_title(repo, d.meta.approver) if d.meta.approver else "—",
                d.meta.effective_date or "—",
                d.meta.last_reviewed or "—",
                Duration.parse(d.meta.review_cycle).humanize(),
                d.meta.next_review or "—",
            ]
            for d in documents
        ],
    )

    out += "\n## Review calendar\n\n"
    out += (
        "Approved documents in the order their next review falls due. The weekly review job opens an "
        "issue sixty days ahead; `isms review-due` lists what is due or overdue on a given day.\n\n"
    )
    calendar = sorted(
        repo.approved_documents(),
        key=lambda d: (d.meta.next_review or d.meta.effective_date, d.meta.id),
    )
    out += table(
        ["Next review", "Id", "Title", "Owner", "Cycle"],
        [
            [
                d.meta.next_review,
                document_link(repo, d),
                d.meta.title,
                role_title(repo, d.meta.owner),
                Duration.parse(d.meta.review_cycle).humanize(),
            ]
            for d in calendar
        ],
    )

    retired = [d for d in documents if d.meta.status is DocumentStatus.RETIRED]
    out += "\n## Retired documents\n\n"
    if retired:
        out += table(
            ["Id", "Title", "Retired on", "Superseded by"],
            [
                [document_link(repo, d), d.meta.title, d.meta.retired_date, d.meta.superseded_by]
                for d in retired
            ],
        )
    else:
        out += "None.\n"

    out += "\n## Control implementation guides\n\n"
    rows = []
    for theme in Theme:
        guides = [g for g in repo.controls if repo.catalogue.by_id()[g.meta.control].theme is theme]
        assessed = sorted(g.meta.last_assessed for g in guides if g.meta.last_assessed)
        rows.append(
            [
                theme.value,
                len(guides),
                assessed[0] if assessed else "—",
                assessed[-1] if assessed else "—",
                sum(1 for g in guides if g.meta.last_assessed is None),
            ]
        )
    out += table(
        ["Theme", "Guides", "Oldest assessment", "Newest assessment", "Never assessed"], rows
    )
    return out
