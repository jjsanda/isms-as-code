"""ISO 8601 durations for review cycles (``P1Y``, ``P6M``, ``P2Y``, ``P18M`` ...).

Only the calendar components that make sense for document review cycles are supported --
years, months, weeks and days -- and month arithmetic clamps to the end of the month, so a
review on 29 February + ``P1Y`` lands on 28 February, never on 1 March.

>>> Duration.parse("P1Y").add_to(date(2024, 2, 29)).isoformat()
'2025-02-28'
>>> Duration.parse("P18M").humanize()
'18 months'
"""

from __future__ import annotations

import calendar
import re
from dataclasses import dataclass
from datetime import date, timedelta

__all__ = ["Duration"]

_PATTERN = re.compile(
    r"^P(?=\d)(?:(?P<years>\d+)Y)?(?:(?P<months>\d+)M)?(?:(?P<weeks>\d+)W)?(?:(?P<days>\d+)D)?$"
)


@dataclass(frozen=True)
class Duration:
    years: int = 0
    months: int = 0
    weeks: int = 0
    days: int = 0

    @classmethod
    def parse(cls, text: str) -> Duration:
        match = _PATTERN.match(text.strip())
        if match is None:
            raise ValueError(f"not a supported ISO 8601 duration: {text!r}")
        parts = {key: int(value) for key, value in match.groupdict(default="0").items()}
        duration = cls(**parts)
        if duration.is_zero:
            raise ValueError(f"duration must be positive: {text!r}")
        return duration

    @property
    def is_zero(self) -> bool:
        return not (self.years or self.months or self.weeks or self.days)

    @property
    def total_months(self) -> int:
        return self.years * 12 + self.months

    def add_to(self, start: date) -> date:
        """Return ``start`` advanced by this duration (months clamp to month end)."""
        month_index = start.year * 12 + (start.month - 1) + self.total_months
        year, month0 = divmod(month_index, 12)
        month = month0 + 1
        day = min(start.day, calendar.monthrange(year, month)[1])
        return date(year, month, day) + timedelta(weeks=self.weeks, days=self.days)

    def humanize(self) -> str:
        """Human-readable form: ``'1 year'``, ``'6 months'``, ``'2 weeks'``."""
        chunks: list[str] = []
        if self.total_months and self.total_months % 12 == 0 and not (self.weeks or self.days):
            years = self.total_months // 12
            return f"{years} year" + ("s" if years != 1 else "")
        if self.total_months:
            chunks.append(f"{self.total_months} month" + ("s" if self.total_months != 1 else ""))
        if self.weeks:
            chunks.append(f"{self.weeks} week" + ("s" if self.weeks != 1 else ""))
        if self.days:
            chunks.append(f"{self.days} day" + ("s" if self.days != 1 else ""))
        return " ".join(chunks)

    def __str__(self) -> str:
        text = "P"
        if self.years:
            text += f"{self.years}Y"
        if self.months:
            text += f"{self.months}M"
        if self.weeks:
            text += f"{self.weeks}W"
        if self.days:
            text += f"{self.days}D"
        return text
