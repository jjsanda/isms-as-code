"""Front matter of a controlled document (policy, standard or procedure)."""

from __future__ import annotations

from datetime import date
from typing import Self

from pydantic import Field, model_validator

from isms_as_code.durations import Duration
from isms_as_code.ids import (
    ClauseRef,
    ControlId,
    DocumentId,
    IsoDuration,
    LanguageCode,
    RoleKey,
    SemVer,
    semver_key,
)
from isms_as_code.models.base import Classification, DocumentStatus, DocumentType, StrictModel

__all__ = ["DocumentMeta", "APPLIES_TO_ALL"]

APPLIES_TO_ALL = "all"
_ENTITY_RE = r"^ENT-[A-Z]{2,4}$"


def _duplicates(values: list[str]) -> list[str]:
    seen: set[str] = set()
    dupes: list[str] = []
    for value in values:
        if value in seen and value not in dupes:
            dupes.append(value)
        seen.add(value)
    return dupes


class DocumentMeta(StrictModel):
    """The YAML front matter every document under ``isms/{policies,standards,procedures}`` carries."""

    id: DocumentId
    title: str = Field(min_length=3, max_length=120)
    type: DocumentType
    status: DocumentStatus
    version: SemVer
    classification: Classification = Classification.INTERNAL
    owner: RoleKey = Field(description="Role key from roles.yaml -- never a person.")
    approver: RoleKey | None = None
    effective_date: date | None = None
    last_reviewed: date | None = None
    review_cycle: IsoDuration = Field(description="ISO 8601 duration, e.g. P1Y or P6M.")
    next_review: date | None = None
    retired_date: date | None = None
    controls: list[ControlId] = Field(default_factory=list)
    clauses: list[ClauseRef] = Field(default_factory=list)
    applies_to: list[str] = Field(default_factory=lambda: [APPLIES_TO_ALL])
    related: list[DocumentId] = Field(default_factory=list)
    supersedes: list[DocumentId] = Field(default_factory=list)
    superseded_by: DocumentId | None = None
    language: LanguageCode = "en"
    tags: list[str] = Field(default_factory=list)

    @property
    def is_approved(self) -> bool:
        return self.status is DocumentStatus.APPROVED

    @property
    def applies_to_all(self) -> bool:
        return self.applies_to == [APPLIES_TO_ALL]

    @property
    def cycle(self) -> Duration:
        return Duration.parse(self.review_cycle)

    @model_validator(mode="after")
    def _check(self) -> Self:
        problems: list[str] = []
        major = semver_key(self.version)[0]
        released = self.status in (DocumentStatus.APPROVED, DocumentStatus.RETIRED)

        if released:
            if major < 1:
                problems.append("approved/retired documents need a version >= 1.0.0")
            if self.approver is None:
                problems.append("approved/retired documents need an approver")
            for name in ("effective_date", "last_reviewed", "next_review"):
                if getattr(self, name) is None:
                    problems.append(f"approved/retired documents need {name}")
        elif major >= 1:
            problems.append("draft/in-review documents use 0.x.y versions until first approval")

        if self.approver is not None and self.approver == self.owner:
            problems.append("approver must differ from owner (segregation of duties)")

        if self.status is DocumentStatus.RETIRED:
            if self.superseded_by is None:
                problems.append("retired documents must name superseded_by")
            if self.retired_date is None:
                problems.append("retired documents must carry retired_date")
        else:
            if self.superseded_by is not None:
                problems.append("only retired documents may set superseded_by")
            if self.retired_date is not None:
                problems.append("only retired documents may set retired_date")

        try:
            cycle = Duration.parse(self.review_cycle)
        except ValueError as exc:
            problems.append(str(exc))
            cycle = None
        if cycle is not None and self.last_reviewed is not None and self.next_review is not None:
            expected = cycle.add_to(self.last_reviewed)
            if self.next_review != expected:
                problems.append(
                    f"next_review {self.next_review} must equal last_reviewed + review_cycle "
                    f"({expected})"
                )

        if not self.applies_to:
            problems.append("applies_to must not be empty")
        elif APPLIES_TO_ALL in self.applies_to and self.applies_to != [APPLIES_TO_ALL]:
            problems.append("applies_to is either ['all'] or a list of entity ids, not both")
        elif self.applies_to != [APPLIES_TO_ALL]:
            import re

            bad = [item for item in self.applies_to if not re.match(_ENTITY_RE, item)]
            if bad:
                problems.append(f"applies_to entries must be entity ids (ENT-XX): {bad}")

        if not self.controls and not self.clauses:
            problems.append("a document must address at least one Annex A control or ISO clause")
        for field_name in ("controls", "related", "supersedes", "applies_to", "tags", "clauses"):
            dupes = _duplicates(getattr(self, field_name))
            if dupes:
                problems.append(f"duplicate entries in {field_name}: {dupes}")
        if self.id in self.related or self.id in self.supersedes or self.id == self.superseded_by:
            problems.append("a document cannot reference itself")

        if problems:
            raise ValueError(f"{self.id}: " + "; ".join(problems))
        return self
