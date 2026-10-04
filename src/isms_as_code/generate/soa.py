"""The Statement of Applicability (clause 6.1.3 d), for the group and per entity."""

from __future__ import annotations

import csv
import io
from collections import Counter

from isms_as_code.generate.common import (
    document_link,
    guide_link,
    md_header,
    role_title,
    status_label,
    table,
)
from isms_as_code.loader import Repository
from isms_as_code.models import Applicability, DocumentStatus, ImplementationStatus, Theme

__all__ = ["render_soa", "render_soa_csv", "soa_rows", "SoaRow"]

THEME_TITLES = {
    Theme.ORGANIZATIONAL: "Organizational controls (A.5)",
    Theme.PEOPLE: "People controls (A.6)",
    Theme.PHYSICAL: "Physical controls (A.7)",
    Theme.TECHNOLOGICAL: "Technological controls (A.8)",
}


class SoaRow:
    """One control as it appears in the SoA for a given scope (group or entity)."""

    def __init__(
        self,
        control: str,
        title: str,
        theme: Theme,
        applicability: Applicability,
        justification: str,
        status: ImplementationStatus | None,
        implemented_by: list[str],
        risks: list[str],
        owner: str,
        evidence_count: int,
        new_in_2022: bool,
    ) -> None:
        self.control = control
        self.title = title
        self.theme = theme
        self.applicability = applicability
        self.justification = justification
        self.status = status
        self.implemented_by = implemented_by
        self.risks = risks
        self.owner = owner
        self.evidence_count = evidence_count
        self.new_in_2022 = new_in_2022

    @property
    def applicable(self) -> bool:
        return self.applicability is Applicability.APPLICABLE


def soa_rows(repo: Repository, entity_id: str | None = None) -> list[SoaRow]:
    guides = repo.controls_by_id()
    documents = repo.documents_by_id()
    rows: list[SoaRow] = []
    for entry in repo.catalogue.sorted():
        guide = guides[entry.id]
        meta = guide.meta
        if entity_id is None:
            applicability, justification = meta.applicability, meta.justification
            status = meta.implementation_status
        else:
            applicability, justification = meta.applicability_for(entity_id)
            status = meta.status_for(entity_id)
        implemented_by = [
            doc_id
            for doc_id in meta.implemented_by
            if documents[doc_id].meta.status is DocumentStatus.APPROVED
            and (entity_id is None or _applies(documents[doc_id].meta.applies_to, entity_id))
        ]
        if applicability is Applicability.NOT_APPLICABLE:
            implemented_by = []
            status = None
        rows.append(
            SoaRow(
                control=entry.id,
                title=entry.title,
                theme=entry.theme,
                applicability=applicability,
                justification=justification,
                status=status,
                implemented_by=implemented_by,
                risks=list(meta.risks),
                owner=meta.owner,
                evidence_count=len(meta.evidence),
                new_in_2022=entry.new_in_2022,
            )
        )
    return rows


def _applies(applies_to: list[str], entity_id: str) -> bool:
    return applies_to == ["all"] or entity_id in applies_to


def _summary(rows: list[SoaRow]) -> str:
    headers = [
        "Theme",
        "Controls",
        "Applicable",
        "Implemented",
        "Partially implemented",
        "Planned",
        "Not implemented",
        "Not applicable",
    ]
    body: list[list[object]] = []
    for theme, title in THEME_TITLES.items():
        subset = [row for row in rows if row.theme is theme]
        body.append(_summary_row(title, subset))
    body.append(_summary_row("**All themes**", rows))
    return table(headers, body)


def _summary_row(label: str, subset: list[SoaRow]) -> list[object]:
    counts = Counter(row.status for row in subset if row.applicable)
    return [
        label,
        len(subset),
        sum(1 for row in subset if row.applicable),
        counts.get(ImplementationStatus.IMPLEMENTED, 0),
        counts.get(ImplementationStatus.PARTIALLY_IMPLEMENTED, 0),
        counts.get(ImplementationStatus.PLANNED, 0),
        counts.get(ImplementationStatus.NOT_IMPLEMENTED, 0),
        sum(1 for row in subset if not row.applicable),
    ]


def render_soa(repo: Repository, digest: str, entity_id: str | None = None) -> str:
    rows = soa_rows(repo, entity_id)
    guides = repo.controls_by_id()
    documents = repo.documents_by_id()
    org = repo.organisation
    if entity_id is None:
        scope_name = org.group_name
        scope_note = (
            "Group-level statement covering all in-scope entities ("
            + ", ".join(e.short_name for e in org.in_scope_entities())
            + "). Entity-specific statements with local applicability decisions are generated "
            "alongside this file under `soa/`."
        )
    else:
        entity = org.entity(entity_id)
        scope_name = entity.legal_name
        scope_note = (
            f"Entity-level statement for {entity.legal_name} ({entity.short_name}, "
            f"{entity.country}). Controls marked *not applicable* here carry an entity-specific "
            "justification; everything else inherits the group decision."
        )

    out = md_header(digest)
    out += f"# Statement of Applicability — {scope_name}\n\n"
    out += (
        "The Statement of Applicability lists every control of ISO/IEC 27001:2022 Annex A, whether "
        "it is applicable, why it is included or excluded, how far it is implemented, which approved "
        "documents implement it, which risks of the risk register it treats and who owns it "
        "(clause 6.1.3 d). It is generated from the control implementation guides under "
        "`isms/controls/`, the document set and the risk register; change those sources, not this "
        "file.\n\n"
    )
    out += f"**Scope.** {scope_note}\n\n"
    out += f"**Standard.** {repo.catalogue.standard}. "
    out += (
        "Control titles only; descriptive text is original. Controls introduced with the 2022 "
        "revision are marked with *(new)*.\n\n"
    )
    out += "## Summary\n\n" + _summary(rows) + "\n"
    approved_docs = sorted({d for row in rows for d in row.implemented_by})
    out += (
        f"{len(approved_docs)} approved documents implement the applicable controls; "
        f"{len({r for row in rows for r in row.risks})} of the {len(repo.risks.risks)} risks in the "
        "register are referenced as justification.\n\n"
    )
    headers = [
        "Control",
        "Title",
        "Applicable",
        "Justification",
        "Implementation status",
        "Implemented by",
        "Risks",
        "Owner",
        "Evidence",
    ]
    for theme, title in THEME_TITLES.items():
        out += f"## {title}\n\n"
        body: list[list[object]] = []
        for row in (r for r in rows if r.theme is theme):
            guide = guides[row.control]
            body.append(
                [
                    guide_link(repo, guide),
                    row.title + (" *(new)*" if row.new_in_2022 else ""),
                    "Yes" if row.applicable else "**No**",
                    row.justification,
                    status_label(row.status) if row.status else "—",
                    ", ".join(document_link(repo, documents[d]) for d in row.implemented_by) or "—",
                    ", ".join(row.risks) or "—",
                    role_title(repo, row.owner),
                    f"{row.evidence_count} item(s)" if row.applicable else "—",
                ]
            )
        out += table(headers, body) + "\n"
    out += "## Approval\n\n"
    out += (
        f"Maintained by the {role_title(repo, org.isms_owner)}; approved by the "
        f"{role_title(repo, org.management_representative)} as part of the risk treatment plan "
        "(PROC-RISK). Approval and every subsequent change are recorded in version control through "
        "the pull-request history of the control guides.\n"
    )
    return out


def render_soa_csv(repo: Repository) -> str:
    rows = soa_rows(repo)
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(
        [
            "control",
            "title",
            "theme",
            "new_in_2022",
            "applicable",
            "justification",
            "implementation_status",
            "implemented_by",
            "risks",
            "owner",
            "evidence_items",
        ]
    )
    for row in rows:
        writer.writerow(
            [
                row.control,
                row.title,
                row.theme.value,
                "yes" if row.new_in_2022 else "no",
                "yes" if row.applicable else "no",
                row.justification,
                row.status.value if row.status else "",
                ";".join(row.implemented_by),
                ";".join(row.risks),
                role_title(repo, row.owner),
                row.evidence_count,
            ]
        )
    return buffer.getvalue()
