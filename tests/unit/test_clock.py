from __future__ import annotations

from datetime import UTC, date, datetime

import pytest

from isms_as_code.clock import FrozenClock, SystemClock, default_clock

pytestmark = pytest.mark.unit


def test_frozen_from_iso_date() -> None:
    assert FrozenClock.at("2026-08-20").today() == date(2026, 8, 20)


def test_frozen_from_epoch_string() -> None:
    assert FrozenClock.at("1787184000").today() == date(2026, 8, 20)


def test_frozen_from_iso_datetime_with_z() -> None:
    assert FrozenClock.at("2026-08-20T09:30:00Z").now() == datetime(2026, 8, 20, 9, 30, tzinfo=UTC)


def test_frozen_from_date_and_naive_datetime_objects() -> None:
    assert FrozenClock.at(date(2026, 1, 2)).today() == date(2026, 1, 2)
    assert FrozenClock.at(datetime(2026, 1, 2, 3, 4)).now().tzinfo is UTC


def test_default_clock_prefers_isms_now(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ISMS_NOW", "2026-08-20")
    monkeypatch.setenv("SOURCE_DATE_EPOCH", "0")
    assert default_clock().today() == date(2026, 8, 20)


def test_default_clock_falls_back_to_epoch_then_system(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("ISMS_NOW", raising=False)
    monkeypatch.setenv("SOURCE_DATE_EPOCH", "1787184000")
    assert default_clock().today() == date(2026, 8, 20)
    monkeypatch.delenv("SOURCE_DATE_EPOCH")
    assert isinstance(default_clock(), SystemClock)
    assert default_clock().today() == datetime.now(tz=UTC).date()
