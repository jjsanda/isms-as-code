"""Keep-a-Changelog parsing and the per-document version/date invariants.

Every controlled document owns a ``CHANGELOG.md`` whose newest entry **is** the document's
current version: ``## [1.3.0] - 2025-10-15`` must match ``version: 1.3.0`` and
``last_reviewed: 2025-10-15`` in the front matter. Entries are newest-first, strictly descending
in version and non-increasing in date. ``## [Unreleased]`` is deliberately not allowed -- every
merged change to a controlled document is a new, approved version.

>>> log = parse_changelog("# Changelog\\n\\n## [1.1.0] - 2026-01-10\\n\\n### Changed\\n\\n- Foo.\\n")
>>> log.latest.version, log.problems
('1.1.0', ())
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass, field
from datetime import date
from itertools import pairwise

from isms_as_code.ids import semver_key

__all__ = ["ChangelogEntry", "Changelog", "parse_changelog", "bump_kind", "SECTION_NAMES"]

SECTION_NAMES = ("Added", "Changed", "Deprecated", "Removed", "Fixed", "Security")

_HEADING_RE = re.compile(r"^## \[(?P<version>\d+\.\d+\.\d+)\] - (?P<date>\d{4}-\d{2}-\d{2})\s*$")
_ANY_H2_RE = re.compile(r"^## ")
_SECTION_RE = re.compile(r"^### (?P<name>\S.*?)\s*$")
_BULLET_RE = re.compile(r"^[-*] (?P<text>.+)$")


@dataclass(frozen=True)
class ChangelogEntry:
    version: str
    date: date
    sections: Mapping[str, tuple[str, ...]] = field(default_factory=dict)

    @property
    def bullets(self) -> tuple[str, ...]:
        return tuple(item for items in self.sections.values() for item in items)

    @property
    def summary(self) -> str:
        return self.bullets[0] if self.bullets else ""


@dataclass(frozen=True)
class Changelog:
    entries: tuple[ChangelogEntry, ...]
    problems: tuple[str, ...] = ()

    @property
    def latest(self) -> ChangelogEntry:
        if not self.entries:
            raise ValueError("changelog has no entries")
        return self.entries[0]

    @property
    def earliest(self) -> ChangelogEntry:
        if not self.entries:
            raise ValueError("changelog has no entries")
        return self.entries[-1]


def parse_changelog(text: str) -> Changelog:
    """Parse a document CHANGELOG; structural problems are collected, not raised."""
    entries: list[ChangelogEntry] = []
    problems: list[str] = []
    current: tuple[str, date] | None = None
    sections: dict[str, list[str]] = {}
    section: str | None = None

    def flush() -> None:
        if current is not None:
            frozen = {name: tuple(items) for name, items in sections.items()}
            if not any(frozen.values()):
                problems.append(f"entry {current[0]} has no change bullets")
            entries.append(ChangelogEntry(current[0], current[1], frozen))

    for number, line in enumerate(text.splitlines(), start=1):
        heading = _HEADING_RE.match(line)
        if heading:
            flush()
            try:
                current = (heading.group("version"), date.fromisoformat(heading.group("date")))
            except ValueError:
                problems.append(f"line {number}: invalid date in heading {line.strip()!r}")
                current = None
            sections, section = {}, None
            continue
        if _ANY_H2_RE.match(line):
            flush()
            current, sections, section = None, {}, None
            problems.append(
                f"line {number}: heading {line.strip()!r} is not of the form "
                "'## [MAJOR.MINOR.PATCH] - YYYY-MM-DD'"
            )
            continue
        section_match = _SECTION_RE.match(line)
        if section_match and current is not None:
            section = section_match.group("name")
            if section not in SECTION_NAMES:
                problems.append(
                    f"line {number}: unknown section '### {section}' "
                    f"(use one of {', '.join(SECTION_NAMES)})"
                )
            sections.setdefault(section, [])
            continue
        bullet = _BULLET_RE.match(line)
        if bullet and current is not None:
            if section is None:
                problems.append(
                    f"line {number}: bullet outside a '### Added/Changed/...' section "
                    f"in entry {current[0]}"
                )
                continue
            sections[section].append(bullet.group("text").strip())
    flush()

    if not entries and not problems:
        problems.append("no version entries found")
    for newer, older in pairwise(entries):
        if semver_key(newer.version) <= semver_key(older.version):
            problems.append(
                f"versions must be strictly descending: {newer.version} follows {older.version}"
            )
        if newer.date < older.date:
            problems.append(
                f"dates must not increase downwards: {newer.version} ({newer.date}) is older "
                f"than {older.version} ({older.date})"
            )
    return Changelog(tuple(entries), tuple(problems))


def bump_kind(old: str, new: str) -> str | None:
    """Classify a version change as ``'major'``, ``'minor'``, ``'patch'`` or ``None`` (not a bump)."""
    o, n = semver_key(old), semver_key(new)
    if n <= o:
        return None
    if n[0] > o[0]:
        return "major"
    if n[1] > o[1]:
        return "minor"
    return "patch"
