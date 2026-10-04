"""HTML -> PDF through WeasyPrint (the `pdf` extra)."""

from __future__ import annotations

import os
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import UTC, date, datetime
from pathlib import Path

try:  # pragma: no cover - import guard exercised by environments without the pdf extra
    import weasyprint as _weasyprint

    PDF_AVAILABLE = True
except ImportError:  # pragma: no cover
    PDF_AVAILABLE = False

__all__ = ["PDF_AVAILABLE", "html_to_pdf", "DEFAULT_EPOCH", "pinned_epoch"]

# 2026-08-20T00:00:00Z — used when neither the environment nor the document provides a date.
DEFAULT_EPOCH = 1787184000


@contextmanager
def pinned_epoch(moment: date | None) -> Iterator[None]:
    """Pin ``SOURCE_DATE_EPOCH`` for the duration of a render unless the caller already set it.

    WeasyPrint embeds subsetted fonts through fontTools, which stamps the font's modification time
    with the wall clock unless ``SOURCE_DATE_EPOCH`` is set; without this, two renders of the same
    document differ by a few bytes inside a compressed stream. The document's own approval date is
    the natural value.
    """
    previous = os.environ.get("SOURCE_DATE_EPOCH")
    if previous is None:
        if moment is not None:
            epoch = int(datetime(moment.year, moment.month, moment.day, tzinfo=UTC).timestamp())
        else:
            epoch = DEFAULT_EPOCH
        os.environ["SOURCE_DATE_EPOCH"] = str(epoch)
    try:
        yield
    finally:
        if previous is None:
            os.environ.pop("SOURCE_DATE_EPOCH", None)


def html_to_pdf(
    html: str, out_path: Path, base_url: str | None = None, moment: date | None = None
) -> None:
    """Write ``html`` as a PDF to ``out_path`` (parent directories are created), reproducibly."""
    if not PDF_AVAILABLE:  # pragma: no cover - guarded by callers
        raise RuntimeError("PDF rendering needs the 'pdf' extra: uv sync --extra pdf")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with pinned_epoch(moment):
        _weasyprint.HTML(string=html, base_url=base_url).write_pdf(str(out_path))
