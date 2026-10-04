from __future__ import annotations

from pathlib import Path

import pytest

from isms_as_code.generate import compute_digest
from isms_as_code.loader import load_repository
from isms_as_code.render import PDF_AVAILABLE, page_for_document, pages_for, render_all
from isms_as_code.render.html import markdown_to_html
from tests.conftest import RepoBuilder

pytestmark = pytest.mark.render


def test_markdown_to_html_strips_comments_and_local_links() -> None:
    html = markdown_to_html(
        "<!-- hidden -->\n\nSee [POL-X](../isms/policies/POL-X/README.md) and [web](https://example.test).\n"
    )
    assert "hidden" not in html
    assert "POL-X" in html and "../isms" not in html
    assert 'href="https://example.test"' in html


def test_document_page_has_cover_revisions_and_watermark(builder: RepoBuilder) -> None:
    repo = load_repository(builder.root)
    page = page_for_document(repo, repo.document("POL-TEST"), compute_digest(repo))
    assert page.stem == "POL-TEST-test-policy-v1.0.0"
    assert '<span class="doc-id">POL-TEST</span>' in page.html
    assert "ISMS Manager (Test Manager)" in page.html
    assert 'name="dcterms.created" content="2026-01-10T00:00:00Z"' in page.html
    assert 'font-family: "DejaVu Sans"' in page.html  # the stylesheet must not be HTML-escaped
    assert "Revision history" in page.html and "Initial approved version." in page.html
    assert '<h2 id="purpose">Purpose</h2>' in page.html and "&lt;h2" not in page.html
    assert "Controlled document" in page.html and '<div class="watermark">' not in page.html
    builder.add_document(
        status="draft",
        version="0.1.0",
        approver=None,
        effective_date=None,
        last_reviewed=None,
        next_review=None,
        changelog="# Changelog\n\n## [0.1.0] - 2026-08-01\n\n### Added\n\n- First draft.\n",
    )
    repo = load_repository(builder.root)
    page = page_for_document(repo, repo.document("POL-TEST"), compute_digest(repo))
    assert '<div class="watermark">DRAFT</div>' in page.html
    assert "not an applicable rule" in page.html


def test_pages_for_covers_documents_artefacts_and_guides(builder: RepoBuilder) -> None:
    repo = load_repository(builder.root)
    stems = {p.stem for p in pages_for(repo)}
    assert {
        "POL-TEST-test-policy-v1.0.0",
        "statement-of-applicability",
        "isms-scope-statement",
        "document-register",
        "risk-register",
        "soa-ENT-AA",
        "soa-ENT-BB",
        "coverage-test-mapping",
        "control-implementation-guides",
    } <= stems
    only = {p.stem for p in pages_for(repo, only={"POL-TEST", "SOA"}, include_guides=False)}
    assert only == {"POL-TEST-test-policy-v1.0.0", "statement-of-applicability"}
    guides = next(p for p in pages_for(repo, only={"GUIDES"}))
    assert "A.5.15 — Synthetic control 5.15" in guides.html


def test_render_all_html_only(builder: RepoBuilder, tmp_path: Path) -> None:
    repo = load_repository(builder.root)
    results = render_all(
        repo, tmp_path / "dist", only={"POL-TEST"}, pdf=False, include_guides=False
    )
    assert len(results) == 1 and results[0].html_path.is_file() and results[0].pdf_path is None


@pytest.mark.skipif(not PDF_AVAILABLE, reason="WeasyPrint (pdf extra) not installed")
def test_render_pdf_is_reproducible(builder: RepoBuilder, tmp_path: Path) -> None:
    repo = load_repository(builder.root)
    import time

    first = render_all(repo, tmp_path / "one", only={"POL-TEST"}, include_guides=False)[0]
    time.sleep(1.1)  # cross a second boundary: fonts must not carry the wall-clock time
    second = render_all(repo, tmp_path / "two", only={"POL-TEST"}, include_guides=False)[0]
    assert first.pdf_path is not None and second.pdf_path is not None
    data = first.pdf_path.read_bytes()
    assert data.startswith(b"%PDF") and len(data) > 5000
    assert data == second.pdf_path.read_bytes()
    from pyhanko.pdf_utils.reader import PdfFileReader

    with first.pdf_path.open("rb") as handle:
        info = PdfFileReader(handle).trailer_view["/Info"]
        assert str(info["/CreationDate"]).startswith(
            "D:20260110"
        )  # from the CHANGELOG, not the clock
