"""Identifier shapes and small text helpers shared by the models, the loader and the generators.

The id aliases are ``Annotated[str, Field(pattern=...)]``: the *shape* of every identifier is part
of the schema (so ``POL-ACC``, ``A.8.16`` or ``R-004`` are validated on load), while the
*existence* of a referenced id is checked separately by the cross-reference validator.

>>> control_sort_key("A.5.15")
(5, 15)
>>> slugify("Supplier & Cloud Security Policy")
'supplier-cloud-security-policy'
"""

from __future__ import annotations

import re
import unicodedata
from typing import Annotated

from pydantic import Field

__all__ = [
    "DocumentId",
    "ControlId",
    "RiskId",
    "EntityId",
    "SiteId",
    "ServiceId",
    "RoleKey",
    "InterestedPartyId",
    "LegalId",
    "SemVer",
    "IsoDuration",
    "ClauseRef",
    "LanguageCode",
    "CountryCode",
    "DOCUMENT_ID_RE",
    "CONTROL_ID_RE",
    "control_sort_key",
    "slugify",
    "semver_key",
]

DOCUMENT_ID_RE = r"^(POL|STD|PROC)-[A-Z]{2,6}$"
CONTROL_ID_RE = r"^A\.[5-8]\.\d{1,2}$"

DocumentId = Annotated[str, Field(pattern=DOCUMENT_ID_RE)]
ControlId = Annotated[str, Field(pattern=CONTROL_ID_RE)]
RiskId = Annotated[str, Field(pattern=r"^R-\d{3}$")]
EntityId = Annotated[str, Field(pattern=r"^ENT-[A-Z]{2,4}$")]
SiteId = Annotated[str, Field(pattern=r"^SITE-[A-Z0-9]{2,6}(-[A-Z0-9]{2,8})?$")]
ServiceId = Annotated[str, Field(pattern=r"^SVC-\d{2}$")]
RoleKey = Annotated[str, Field(pattern=r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$", max_length=40)]
InterestedPartyId = Annotated[str, Field(pattern=r"^IP-\d{2}$")]
LegalId = Annotated[str, Field(pattern=r"^LEG-\d{2}$")]
SemVer = Annotated[str, Field(pattern=r"^\d+\.\d+\.\d+$")]
# pydantic-core has no look-around, so "at least one component" is spelled out.
IsoDuration = Annotated[
    str,
    Field(
        pattern=(
            r"^P(?:\d+Y(?:\d+M)?(?:\d+W)?(?:\d+D)?|\d+M(?:\d+W)?(?:\d+D)?|\d+W(?:\d+D)?|\d+D)$"
        )
    ),
]
ClauseRef = Annotated[str, Field(pattern=r"^(?:[4-9]|10)(?:\.\d+){0,2}$")]
LanguageCode = Annotated[str, Field(pattern=r"^[a-z]{2}$")]
CountryCode = Annotated[str, Field(pattern=r"^[A-Z]{2}$")]

_CONTROL_RE = re.compile(r"^A\.(\d+)\.(\d+)$")


def control_sort_key(control_id: str) -> tuple[int, int]:
    """Numeric sort key so that ``A.5.9`` sorts before ``A.5.10``."""
    match = _CONTROL_RE.match(control_id)
    if match is None:
        raise ValueError(f"not an Annex A control id: {control_id!r}")
    return int(match.group(1)), int(match.group(2))


def semver_key(version: str) -> tuple[int, int, int]:
    """Sort key for ``MAJOR.MINOR.PATCH`` strings.

    >>> semver_key("1.10.0") > semver_key("1.9.3")
    True
    """
    major, minor, patch = (int(part) for part in version.split("."))
    return major, minor, patch


def slugify(text: str) -> str:
    """Lower-case, ASCII-only, hyphen-separated slug used for document folder names."""
    normalised = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", normalised.lower()).strip("-")
    return re.sub(r"-{2,}", "-", slug)
