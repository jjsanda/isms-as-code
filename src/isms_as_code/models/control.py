"""Front matter of an Annex A control implementation guide (one file per control)."""

from __future__ import annotations

from datetime import date
from typing import Self

from pydantic import Field, model_validator

from isms_as_code.ids import ControlId, DocumentId, EntityId, RiskId, RoleKey
from isms_as_code.models.base import (
    Applicability,
    EvidenceFrequency,
    ImplementationStatus,
    StrictModel,
)

__all__ = ["ControlGuideMeta", "EvidenceItem", "EntityOverride"]


class EvidenceItem(StrictModel):
    """Where an auditor finds proof that the control operates."""

    description: str = Field(min_length=5, max_length=200)
    location: str = Field(default="", max_length=200)
    frequency: EvidenceFrequency = EvidenceFrequency.ON_EVENT


class EntityOverride(StrictModel):
    """Per-entity deviation from the group-level applicability decision."""

    applicability: Applicability
    justification: str = Field(min_length=10, max_length=600)
    implementation_status: ImplementationStatus | None = None

    @model_validator(mode="after")
    def _check(self) -> Self:
        if self.applicability is Applicability.NOT_APPLICABLE and self.implementation_status:
            raise ValueError("a not-applicable override cannot carry an implementation status")
        return self


class ControlGuideMeta(StrictModel):
    control: ControlId
    applicability: Applicability = Applicability.APPLICABLE
    justification: str = Field(
        min_length=10,
        max_length=600,
        description="Why the control is (not) applicable: risks, legal or contractual drivers.",
    )
    implementation_status: ImplementationStatus | None = None
    implemented_by: list[DocumentId] = Field(default_factory=list)
    owner: RoleKey
    risks: list[RiskId] = Field(default_factory=list)
    evidence: list[EvidenceItem] = Field(default_factory=list)
    metrics: list[str] = Field(default_factory=list)
    entity_overrides: dict[EntityId, EntityOverride] = Field(default_factory=dict)
    last_assessed: date | None = None

    @property
    def is_applicable(self) -> bool:
        return self.applicability is Applicability.APPLICABLE

    def applicability_for(self, entity_id: str) -> tuple[Applicability, str]:
        """Resolve the (applicability, justification) pair for one entity."""
        override = self.entity_overrides.get(entity_id)
        if override is not None:
            return override.applicability, override.justification
        return self.applicability, self.justification

    def status_for(self, entity_id: str) -> ImplementationStatus | None:
        override = self.entity_overrides.get(entity_id)
        if override is not None:
            if override.applicability is Applicability.NOT_APPLICABLE:
                return None
            return override.implementation_status or self.implementation_status
        return self.implementation_status

    @model_validator(mode="after")
    def _check(self) -> Self:
        problems: list[str] = []
        if self.applicability is Applicability.NOT_APPLICABLE:
            if self.implementation_status is not None:
                problems.append("a not-applicable control has no implementation status")
            if self.implemented_by:
                problems.append("a not-applicable control cannot list implementing documents")
        else:
            if self.implementation_status is None:
                problems.append("an applicable control needs an implementation_status")
            elif self.implementation_status in (
                ImplementationStatus.IMPLEMENTED,
                ImplementationStatus.PARTIALLY_IMPLEMENTED,
            ):
                if not self.implemented_by:
                    problems.append(
                        f"an {self.implementation_status.value} control must name at least one "
                        "implementing document"
                    )
                if not self.evidence:
                    problems.append(
                        f"an {self.implementation_status.value} control must name at least one "
                        "evidence item"
                    )
        if len(set(self.implemented_by)) != len(self.implemented_by):
            problems.append("duplicate entries in implemented_by")
        if len(set(self.risks)) != len(self.risks):
            problems.append("duplicate entries in risks")
        if problems:
            raise ValueError(f"{self.control}: " + "; ".join(problems))
        return self
