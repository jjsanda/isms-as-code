from __future__ import annotations

from datetime import date

import pytest

from isms_as_code.durations import Duration

pytestmark = pytest.mark.unit


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("P1Y", Duration(years=1)),
        ("P6M", Duration(months=6)),
        ("P2Y6M", Duration(years=2, months=6)),
        ("P2W", Duration(weeks=2)),
        ("P10D", Duration(days=10)),
    ],
)
def test_parse(text: str, expected: Duration) -> None:
    assert Duration.parse(text) == expected
    assert str(Duration.parse(text)) == text


@pytest.mark.parametrize("text", ["P", "P0D", "1Y", "PT1H", "P1Y2X", ""])
def test_parse_rejects_unsupported(text: str) -> None:
    with pytest.raises(ValueError):
        Duration.parse(text)


def test_add_to_clamps_to_month_end() -> None:
    assert Duration.parse("P1Y").add_to(date(2024, 2, 29)) == date(2025, 2, 28)
    assert Duration.parse("P1M").add_to(date(2026, 1, 31)) == date(2026, 2, 28)


def test_add_to_rolls_over_years_and_adds_days() -> None:
    assert Duration.parse("P6M").add_to(date(2026, 10, 15)) == date(2027, 4, 15)
    assert Duration.parse("P1Y2W1D").add_to(date(2026, 8, 20)) == date(2027, 9, 4)


@pytest.mark.parametrize(
    ("text", "human"),
    [
        ("P1Y", "1 year"),
        ("P2Y", "2 years"),
        ("P6M", "6 months"),
        ("P18M", "18 months"),
        ("P1W3D", "1 week 3 days"),
    ],
)
def test_humanize(text: str, human: str) -> None:
    assert Duration.parse(text).humanize() == human
