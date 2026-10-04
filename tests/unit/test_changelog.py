from __future__ import annotations

from datetime import date

import pytest

from isms_as_code.changelog import bump_kind, parse_changelog

pytestmark = pytest.mark.unit

VALID = """# Changelog

## [1.3.0] - 2025-10-15

### Changed

- Require MFA for privileged access.
- Clarify quarterly access reviews.

### Added

- Break-glass account procedure.

## [1.2.0] - 2025-03-01

### Changed

- Periodic review; wording aligned with ISO/IEC 27001:2022.

## [1.0.0] - 2024-01-10

### Added

- Initial approved version.
"""


def test_parse_valid_changelog() -> None:
    log = parse_changelog(VALID)
    assert log.problems == ()
    assert [entry.version for entry in log.entries] == ["1.3.0", "1.2.0", "1.0.0"]
    assert log.latest.date == date(2025, 10, 15)
    assert log.earliest.version == "1.0.0"
    assert log.latest.sections["Changed"] == (
        "Require MFA for privileged access.",
        "Clarify quarterly access reviews.",
    )
    assert log.latest.summary == "Require MFA for privileged access."
    assert len(log.latest.bullets) == 3


def test_unreleased_heading_is_rejected() -> None:
    log = parse_changelog("# Changelog\n\n## [Unreleased]\n\n### Added\n\n- Something.\n")
    assert any("not of the form" in problem for problem in log.problems)


def test_ordering_problems_are_reported() -> None:
    text = "## [1.0.0] - 2025-01-01\n\n### Added\n\n- A.\n\n## [1.1.0] - 2024-01-01\n\n### Added\n\n- B.\n"
    log = parse_changelog(text)
    assert any("strictly descending" in problem for problem in log.problems)


def test_date_regression_is_reported() -> None:
    text = "## [1.1.0] - 2024-01-01\n\n### Added\n\n- A.\n\n## [1.0.0] - 2025-01-01\n\n### Added\n\n- B.\n"
    log = parse_changelog(text)
    assert any("dates must not increase" in problem for problem in log.problems)


def test_entry_without_bullets_unknown_section_and_loose_bullet() -> None:
    text = "## [1.0.0] - 2025-01-01\n\n- loose bullet\n\n### Tweaked\n\n## [0.9.0] - 2024-12-01\n"
    log = parse_changelog(text)
    joined = "\n".join(log.problems)
    assert "outside a '### Added" in joined
    assert "unknown section" in joined
    assert "has no change bullets" in joined


def test_empty_and_invalid_date() -> None:
    assert parse_changelog("").problems == ("no version entries found",)
    assert any("invalid date" in p for p in parse_changelog("## [1.0.0] - 2025-13-45\n").problems)


@pytest.mark.parametrize(
    ("old", "new", "kind"),
    [
        ("1.0.0", "2.0.0", "major"),
        ("1.0.0", "1.1.0", "minor"),
        ("1.0.0", "1.0.1", "patch"),
        ("1.1.0", "1.1.0", None),
        ("1.1.0", "1.0.9", None),
    ],
)
def test_bump_kind(old: str, new: str, kind: str | None) -> None:
    assert bump_kind(old, new) == kind
