"""A single, injectable source of "now".

Every date-relative feature (review-due reports, "overdue" warnings, PDF metadata fallbacks)
reads the date through a :class:`Clock` instead of calling ``datetime.now()`` directly. Pin
``ISMS_NOW`` (an ISO date) or ``SOURCE_DATE_EPOCH`` (unix seconds) and the whole toolchain agrees
on one "today", which is what makes the tests and the CI checks reproducible.

>>> clock = FrozenClock.at("2026-08-20")
>>> clock.today().isoformat()
'2026-08-20'
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import UTC, date, datetime
from typing import Protocol, runtime_checkable

__all__ = [
    "Clock",
    "FrozenClock",
    "SystemClock",
    "default_clock",
    "ISMS_NOW_ENV",
    "SOURCE_DATE_EPOCH_ENV",
]

ISMS_NOW_ENV = "ISMS_NOW"
SOURCE_DATE_EPOCH_ENV = "SOURCE_DATE_EPOCH"


@runtime_checkable
class Clock(Protocol):
    """Anything that can report today's date and the current instant (UTC)."""

    def today(self) -> date: ...

    def now(self) -> datetime: ...


def _parse(text: str) -> datetime:
    """Parse an ISO date/datetime or a unix-epoch string into an aware UTC datetime."""
    raw = text.strip()
    if raw.isdigit():
        return datetime.fromtimestamp(int(raw), tz=UTC)
    iso = raw.replace("Z", "+00:00")
    if "T" not in iso:
        iso += "T00:00:00"
    parsed = datetime.fromisoformat(iso)
    return parsed if parsed.tzinfo is not None else parsed.replace(tzinfo=UTC)


@dataclass(frozen=True)
class FrozenClock:
    """A clock pinned to a fixed instant -- the backbone of deterministic output.

    >>> FrozenClock.at("2026-08-20").now().isoformat()
    '2026-08-20T00:00:00+00:00'
    >>> FrozenClock.at("1787184000").today().isoformat()
    '2026-08-20'
    """

    instant: datetime

    def today(self) -> date:
        return self.instant.date()

    def now(self) -> datetime:
        return self.instant

    @classmethod
    def at(cls, value: str | date | datetime) -> FrozenClock:
        if isinstance(value, datetime):
            instant = value if value.tzinfo is not None else value.replace(tzinfo=UTC)
        elif isinstance(value, date):
            instant = datetime(value.year, value.month, value.day, tzinfo=UTC)
        else:
            instant = _parse(value)
        return cls(instant)


@dataclass(frozen=True)
class SystemClock:
    """The real wall clock, in UTC."""

    def today(self) -> date:
        return self.now().date()

    def now(self) -> datetime:
        return datetime.now(tz=UTC)


def default_clock() -> Clock:
    """Return the clock the CLI should use.

    Resolution order (first hit wins): ``ISMS_NOW`` -> ``SOURCE_DATE_EPOCH`` -> system clock.
    """
    pinned = os.environ.get(ISMS_NOW_ENV)
    if pinned:
        return FrozenClock.at(pinned)
    epoch = os.environ.get(SOURCE_DATE_EPOCH_ENV)
    if epoch:
        return FrozenClock.at(epoch)
    return SystemClock()
