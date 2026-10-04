"""Render every document and generated artefact to HTML and PDF under an output directory."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from functools import partial
from pathlib import Path

from isms_as_code.generate import compute_digest
from isms_as_code.generate.coverage import render_coverage
from isms_as_code.generate.register import render_register
from isms_as_code.generate.risk_view import render_risk_view
from isms_as_code.generate.scope import render_scope
from isms_as_code.generate.soa import render_soa
from isms_as_code.loader import Repository
from isms_as_code.render.html import (
    RenderedPage,
    page_for_artefact,
    page_for_document,
    page_for_guides,
)
from isms_as_code.render.pdf import html_to_pdf

__all__ = ["RenderResult", "render_all", "pages_for"]


@dataclass(frozen=True)
class RenderResult:
    stem: str
    title: str
    html_path: Path
    pdf_path: Path | None


def pages_for(
    repo: Repository, only: set[str] | None = None, include_guides: bool = True
) -> list[RenderedPage]:
    """Build the HTML pages: one per document, one per generated artefact, one guide compendium."""
    digest = compute_digest(repo)
    pages: list[RenderedPage] = []
    for document in sorted(repo.documents, key=lambda d: d.meta.id):
        if only and document.meta.id not in only:
            continue
        pages.append(page_for_document(repo, document, digest))
    artefacts: list[tuple[str, str, str, Callable[[], str]]] = [
        (
            "statement-of-applicability",
            "SOA",
            "Statement of Applicability",
            lambda: render_soa(repo, digest),
        ),
        (
            "isms-scope-statement",
            "SCOPE",
            "ISMS Scope Statement",
            lambda: render_scope(repo, digest),
        ),
        (
            "document-register",
            "REGISTER",
            "Document register",
            lambda: render_register(repo, digest),
        ),
        ("risk-register", "RISKS", "Risk register", lambda: render_risk_view(repo, digest)),
    ]
    for entity in repo.organisation.in_scope_entities():
        artefacts.append(
            (
                f"soa-{entity.id}",
                f"SOA-{entity.id}",
                f"Statement of Applicability — {entity.legal_name}",
                partial(render_soa, repo, digest, entity.id),
            )
        )
    for mapping in repo.mappings:
        artefacts.append(
            (
                f"coverage-{mapping.name}",
                f"COVERAGE-{mapping.name.upper()}",
                f"Coverage — {mapping.title}",
                partial(render_coverage, repo, mapping, digest),
            )
        )
    for stem, artefact_id, title, producer in artefacts:
        if only and artefact_id not in only and stem not in only:
            continue
        pages.append(
            page_for_artefact(
                repo,
                stem=stem,
                artefact_id=artefact_id,
                title=title,
                markdown_text=producer(),
                digest=digest,
            )
        )
    if include_guides and (not only or "GUIDES" in only):
        pages.append(page_for_guides(repo, list(repo.controls), digest))
    return pages


def render_all(
    repo: Repository,
    out_dir: Path,
    only: set[str] | None = None,
    pdf: bool = True,
    include_guides: bool = True,
) -> list[RenderResult]:
    results: list[RenderResult] = []
    html_dir = out_dir / "html"
    pdf_dir = out_dir / "pdf"
    html_dir.mkdir(parents=True, exist_ok=True)
    for page in pages_for(repo, only, include_guides):
        html_path = html_dir / f"{page.stem}.html"
        html_path.write_text(page.html, encoding="utf-8")
        pdf_path: Path | None = None
        if pdf:
            pdf_path = pdf_dir / f"{page.stem}.pdf"
            html_to_pdf(page.html, pdf_path, base_url=str(repo.root), moment=page.modified)
        results.append(RenderResult(page.stem, page.title, html_path, pdf_path))
    return results
