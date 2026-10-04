"""A tiny Markdown outline parser used to enforce document structure.

Only ATX headings are considered and fenced code blocks are skipped, which is all the structure
rules need: one H1 (``# <id> — <title>``) and a fixed set of H2 sections per document type.

>>> outline("# T\\n\\n## A\\n```\\n## not a heading\\n```\\n## B\\n").h2
('A', 'B')
"""

from __future__ import annotations

import re
from dataclasses import dataclass

__all__ = ["Outline", "outline", "REQUIRED_SECTIONS"]

_FENCE_RE = re.compile(r"^(```|~~~)")
_HEADING_RE = re.compile(r"^(?P<hashes>#{1,6})\s+(?P<text>.+?)\s*#*\s*$")

# Required H2 sections per document type (in this order); extra sections are allowed.
REQUIRED_SECTIONS: dict[str, tuple[str, ...]] = {
    "policy": (
        "Purpose",
        "Scope",
        "Policy statements",
        "Roles and responsibilities",
        "Compliance and exceptions",
        "Related documents",
    ),
    "standard": (
        "Purpose",
        "Scope",
        "Requirements",
        "Compliance and exceptions",
        "Related documents",
    ),
    "procedure": (
        "Purpose",
        "Scope",
        "Procedure",
        "Records",
        "Related documents",
    ),
    "control-guide": (
        "Objective",
        "Implementation",
        "Evidence",
        "Metrics",
        "Common pitfalls",
    ),
}


@dataclass(frozen=True)
class Outline:
    h1: tuple[str, ...]
    h2: tuple[str, ...]

    @property
    def title(self) -> str | None:
        return self.h1[0] if self.h1 else None

    def missing(self, required: tuple[str, ...]) -> tuple[str, ...]:
        present = set(self.h2)
        return tuple(section for section in required if section not in present)


def outline(markdown_text: str) -> Outline:
    """Collect H1 and H2 headings, ignoring anything inside fenced code blocks."""
    h1: list[str] = []
    h2: list[str] = []
    in_fence = False
    for line in markdown_text.splitlines():
        if _FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = _HEADING_RE.match(line)
        if match is None:
            continue
        level = len(match.group("hashes"))
        if level == 1:
            h1.append(match.group("text"))
        elif level == 2:
            h2.append(match.group("text"))
    return Outline(tuple(h1), tuple(h2))
