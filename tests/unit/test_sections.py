from __future__ import annotations

import pytest

from isms_as_code.sections import REQUIRED_SECTIONS, outline

pytestmark = pytest.mark.unit


def test_outline_collects_h1_and_h2_and_skips_fences() -> None:
    text = "# POL-X — Title\n\n## Purpose\n\n```yaml\n## not: a heading\n```\n\n### H3 ignored\n\n## Scope ##\n"
    result = outline(text)
    assert result.title == "POL-X — Title"
    assert result.h2 == ("Purpose", "Scope")


def test_missing_sections() -> None:
    result = outline("# T\n\n## Purpose\n\n## Scope\n")
    assert result.missing(REQUIRED_SECTIONS["policy"]) == (
        "Policy statements",
        "Roles and responsibilities",
        "Compliance and exceptions",
        "Related documents",
    )


def test_required_sections_cover_every_document_type() -> None:
    assert set(REQUIRED_SECTIONS) == {"policy", "standard", "procedure", "control-guide"}
