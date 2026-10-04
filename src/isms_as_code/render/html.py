"""Build the HTML page (cover, body, revision history, approval block) for anything we render."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

from isms_as_code.generate.common import role_with_holder
from isms_as_code.loader import ControlGuide, Document, Repository
from isms_as_code.models import DocumentStatus

__all__ = ["RenderedPage", "page_for_document", "page_for_artefact", "page_for_guides"]

ASSETS = Path(__file__).parent / "assets"
MARKDOWN_EXTENSIONS = [
    "tables",
    "toc",
    "attr_list",
    "def_list",
    "footnotes",
    "admonition",
    "sane_lists",
    "md_in_html",
    "fenced_code",
]
_H1_RE = re.compile(r"^# .+\n", re.MULTILINE)
_LOCAL_LINK_RE = re.compile(r"\[([^\]]+)\]\((?:\.\./|\./|/)[^)\s]+?\.md(?:#[^)]*)?\)")
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->\s*", re.DOTALL)
_WATERMARKS = {
    DocumentStatus.DRAFT: "DRAFT",
    DocumentStatus.IN_REVIEW: "IN REVIEW",
    DocumentStatus.RETIRED: "RETIRED",
}
_KIND_LABELS = {"policy": "Policy", "standard": "Standard", "procedure": "Procedure"}


@dataclass(frozen=True)
class RenderedPage:
    stem: str
    title: str
    html: str
    modified: date | None = None


def _environment() -> Environment:
    return Environment(
        loader=FileSystemLoader(str(ASSETS)),
        autoescape=select_autoescape(enabled_extensions=("j2",), default_for_string=True),
        trim_blocks=True,
        lstrip_blocks=True,
    )


def markdown_to_html(text: str) -> str:
    """Convert Markdown to HTML, dropping local `.md` links (they do not resolve inside a PDF)."""
    cleaned = _HTML_COMMENT_RE.sub("", text)
    cleaned = _LOCAL_LINK_RE.sub(r"\1", cleaned)
    return markdown.markdown(cleaned, extensions=MARKDOWN_EXTENSIONS, output_format="html")


def _render(
    repo: Repository,
    *,
    doc_id: str,
    title: str,
    kind_label: str,
    version: str,
    status: str,
    classification: str,
    metadata: list[tuple[str, str]],
    body_markdown: str,
    revisions: list[dict[str, str]],
    approval_text: str,
    watermark: str | None,
    created: date | None,
    modified: date | None,
    digest: str,
    language: str = "en",
) -> str:
    template = _environment().get_template("document.html.j2")
    return template.render(
        organisation=repo.organisation.group_name,
        doc_id=doc_id,
        title=title,
        kind_label=kind_label,
        version=version,
        status=status,
        classification=classification,
        metadata=metadata,
        body_html=markdown_to_html(body_markdown),
        revisions=revisions,
        approval_text=approval_text,
        watermark=watermark,
        created=f"{created.isoformat()}T00:00:00Z" if created else None,
        modified=f"{modified.isoformat()}T00:00:00Z" if modified else None,
        digest=digest,
        css=(ASSETS / "print.css").read_text(encoding="utf-8"),
        language=language,
    )


def page_for_document(repo: Repository, document: Document, digest: str) -> RenderedPage:
    meta = document.meta
    body = _H1_RE.sub("", document.body, count=1)
    metadata = [
        ("Document id", meta.id),
        ("Type", _KIND_LABELS[meta.type.value]),
        ("Status", meta.status.value),
        ("Version", meta.version),
        ("Classification", meta.classification.value),
        ("Owner", role_with_holder(repo, meta.owner)),
        ("Approver", role_with_holder(repo, meta.approver) if meta.approver else "—"),
        ("Effective date", meta.effective_date.isoformat() if meta.effective_date else "—"),
        ("Last reviewed", meta.last_reviewed.isoformat() if meta.last_reviewed else "—"),
        ("Review cycle", meta.cycle.humanize()),
        ("Next review", meta.next_review.isoformat() if meta.next_review else "—"),
        (
            "Applies to",
            "all entities in scope" if meta.applies_to_all else ", ".join(meta.applies_to),
        ),
        ("Annex A controls", ", ".join(meta.controls) or "—"),
        ("ISO/IEC 27001 clauses", ", ".join(meta.clauses) or "—"),
        ("Related documents", ", ".join(meta.related) or "—"),
    ]
    if meta.status is DocumentStatus.RETIRED:
        metadata.append(("Retired", f"{meta.retired_date} — superseded by {meta.superseded_by}"))
    revisions = [
        {"version": e.version, "date": e.date.isoformat(), "summary": "; ".join(e.bullets)}
        for e in document.changelog.entries
    ]
    if meta.status is DocumentStatus.APPROVED:
        approval = (
            f"Approved by the {role_with_holder(repo, meta.approver or '')} on "
            f"{document.changelog.latest.date.isoformat() if document.changelog.entries else '—'}; "
            f"owned by the {role_with_holder(repo, meta.owner)}. The approval is recorded in version "
            "control as the reviewed and merged pull request of this version (PROC-DOC, stage 3)."
        )
    else:
        approval = (
            f"This version is {meta.status.value} and is not an applicable rule. Owner: "
            f"{role_with_holder(repo, meta.owner)}."
        )
    created = document.changelog.earliest.date if document.changelog.entries else None
    modified = document.changelog.latest.date if document.changelog.entries else None
    html = _render(
        repo,
        doc_id=meta.id,
        title=meta.title,
        kind_label=_KIND_LABELS[meta.type.value],
        version=meta.version,
        status=meta.status.value,
        classification=meta.classification.value,
        metadata=metadata,
        body_markdown=body,
        revisions=revisions,
        approval_text=approval,
        watermark=_WATERMARKS.get(meta.status),
        created=created,
        modified=modified,
        digest=digest,
        language=meta.language,
    )
    stem = f"{document.folder.name}-v{meta.version}"
    return RenderedPage(stem=stem, title=f"{meta.id} — {meta.title}", html=html, modified=modified)


def page_for_artefact(
    repo: Repository, *, stem: str, artefact_id: str, title: str, markdown_text: str, digest: str
) -> RenderedPage:
    body = _H1_RE.sub("", markdown_text, count=1)
    metadata = [
        ("Artefact", artefact_id),
        ("Generated from", "the ISMS sources (front matter, registers, catalogue)"),
        ("Source digest", f"sha256:{digest[:16]}…"),
        ("Maintained by", role_with_holder(repo, repo.organisation.isms_owner)),
        ("Approved by", role_with_holder(repo, repo.organisation.management_representative)),
    ]
    approval = (
        "Generated artefact. It is derived deterministically from the repository sources and "
        "regenerated by CI on every change; the approval record is the version-control history of "
        "the sources it is generated from."
    )
    html = _render(
        repo,
        doc_id=artefact_id,
        title=title,
        kind_label="Generated artefact",
        version=digest[:12],
        status="generated",
        classification="internal",
        metadata=metadata,
        body_markdown=body,
        revisions=[],
        approval_text=approval,
        watermark=None,
        created=None,
        modified=None,
        digest=digest,
    )
    return RenderedPage(stem=stem, title=title, html=html)


def page_for_guides(repo: Repository, guides: list[ControlGuide], digest: str) -> RenderedPage:
    """One compendium page with every control implementation guide, grouped by theme."""
    catalogue = repo.catalogue.by_id()
    parts: list[str] = []
    current_theme = None
    for guide in sorted(
        guides, key=lambda g: (catalogue[g.meta.control].theme.value, repo.relpath(g.path))
    ):
        entry = catalogue[guide.meta.control]
        if entry.theme is not current_theme:
            current_theme = entry.theme
            parts.append(f"# {entry.theme.value.capitalize()} controls\n")
        meta = guide.meta
        parts.append(
            f"\n## {meta.control} — {entry.title}\n\n"
            f"*Applicability:* {meta.applicability.value} · *Status:* "
            f"{meta.implementation_status.value if meta.implementation_status else '—'} · "
            f"*Owner:* {role_with_holder(repo, meta.owner)} · *Implemented by:* "
            f"{', '.join(meta.implemented_by) or '—'} · *Risks:* {', '.join(meta.risks) or '—'}\n\n"
            f"*Justification:* {meta.justification}\n\n"
        )
        body = _H1_RE.sub("", guide.body, count=1)
        parts.append(re.sub(r"^## ", "### ", body, flags=re.MULTILINE))
    markdown_text = "".join(parts)
    return page_for_artefact(
        repo,
        stem="control-implementation-guides",
        artefact_id="GUIDES",
        title="Annex A control implementation guides",
        markdown_text="# Annex A control implementation guides\n\n" + markdown_text,
        digest=digest,
    )
