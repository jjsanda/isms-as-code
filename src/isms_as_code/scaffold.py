"""`isms new`: create a document folder from the templates with valid draft front matter."""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path

import yaml

from isms_as_code import layout
from isms_as_code.ids import DOCUMENT_ID_RE, slugify
from isms_as_code.models import DocumentMeta

__all__ = ["scaffold_document"]

_PREFIX = {"policy": "POL", "standard": "STD", "procedure": "PROC"}


def scaffold_document(
    root: Path,
    doc_type: str,
    doc_id: str,
    title: str,
    owner: str,
    approver: str,
    controls: list[str],
    today: date,
) -> Path:
    """Create ``<type dir>/<id>-<slug>/{README.md,CHANGELOG.md}`` as a 0.1.0 draft; return the folder."""
    if doc_type not in layout.DOCUMENT_DIRS:
        raise ValueError(f"unknown document type {doc_type!r}")
    if not re.match(DOCUMENT_ID_RE, doc_id) or not doc_id.startswith(_PREFIX[doc_type] + "-"):
        raise ValueError(f"id {doc_id!r} must look like {_PREFIX[doc_type]}-XXXX for a {doc_type}")
    folder = root / layout.DOCUMENT_DIRS[doc_type] / f"{doc_id}-{slugify(title)}"
    if folder.exists():
        raise FileExistsError(f"{folder} already exists")
    template_path = root / layout.TEMPLATES_DIR / f"{doc_type}.md"
    template = template_path.read_text(encoding="utf-8")
    body = template[template.index("\n---\n", 4) + len("\n---\n") :]
    mnemonic = doc_id.split("-", 1)[1]
    body = (
        body.replace(f"{_PREFIX[doc_type]}-XXXX", doc_id)
        .replace(f"Example {doc_type.capitalize()}", title)
        .replace("XXXX-", f"{mnemonic}-")
    )
    meta = DocumentMeta(
        id=doc_id,
        title=title,
        type=doc_type,
        status="draft",
        version="0.1.0",
        owner=owner,
        approver=approver,
        review_cycle="P1Y",
        controls=controls or ["A.5.1"],
    )
    front = yaml.safe_dump(
        meta.model_dump(mode="json", exclude_none=True), sort_keys=False, allow_unicode=True
    )
    folder.mkdir(parents=True)
    (folder / layout.DOCUMENT_FILENAME).write_text(
        "---\n" + front + "---\n" + body, encoding="utf-8"
    )
    changelog = (root / layout.TEMPLATES_DIR / "CHANGELOG.md").read_text(encoding="utf-8")
    changelog = changelog.replace("## [0.1.0] - 2026-01-01", f"## [0.1.0] - {today.isoformat()}")
    (folder / layout.CHANGELOG_FILENAME).write_text(changelog, encoding="utf-8")
    return folder
