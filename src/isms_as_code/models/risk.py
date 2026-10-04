"""Risk criteria (clause 6.1.2) and the risk register that the SoA justifications point to."""

from __future__ import annotations

from datetime import date
from typing import Self

from pydantic import Field, model_validator

from isms_as_code.ids import ControlId, InterestedPartyId, LegalId, RiskId, RoleKey
from isms_as_code.models.base import RiskStatus, RiskTreatment, StrictModel

__all__ = ["ScaleLevel", "Band", "RiskCriteria", "Risk", "RiskRegister"]


class ScaleLevel(StrictModel):
    level: int = Field(ge=1, le=5)
    label: str = Field(min_length=3, max_length=40)
    description: str = Field(min_length=10, max_length=400)


class Band(StrictModel):
    name: str = Field(min_length=3, max_length=20)
    min_score: int = Field(ge=1, le=25)
    max_score: int = Field(ge=1, le=25)
    response: str = Field(min_length=10, max_length=400)
    acceptance: RoleKey | None = Field(
        default=None, description="Role that may retain residual risk in this band; None = never."
    )

    @model_validator(mode="after")
    def _check(self) -> Self:
        if self.max_score < self.min_score:
            raise ValueError(f"band {self.name}: max_score below min_score")
        return self


class RiskCriteria(StrictModel):
    method: str = Field(min_length=10, max_length=600)
    likelihood: list[ScaleLevel] = Field(min_length=5, max_length=5)
    impact: list[ScaleLevel] = Field(min_length=5, max_length=5)
    bands: list[Band] = Field(min_length=2)
    treatment_options: dict[RiskTreatment, str]

    def band_for(self, score: int) -> Band:
        for band in self.bands:
            if band.min_score <= score <= band.max_score:
                return band
        raise ValueError(f"no band covers score {score}")

    @model_validator(mode="after")
    def _check(self) -> Self:
        problems: list[str] = []
        for name, scale in (("likelihood", self.likelihood), ("impact", self.impact)):
            if sorted(level.level for level in scale) != [1, 2, 3, 4, 5]:
                problems.append(f"{name} scale must define levels 1..5 exactly once")
        ordered = sorted(self.bands, key=lambda band: band.min_score)
        expected = 1
        for band in ordered:
            if band.min_score != expected:
                problems.append(f"bands must be contiguous from 1: gap/overlap at {band.name}")
                break
            expected = band.max_score + 1
        else:
            if expected != 26:
                problems.append("bands must cover scores 1..25")
        missing = [option.value for option in RiskTreatment if option not in self.treatment_options]
        if missing:
            problems.append(f"treatment_options must describe every option; missing {missing}")
        if problems:
            raise ValueError("risk criteria: " + "; ".join(problems))
        return self


class Risk(StrictModel):
    id: RiskId
    title: str = Field(min_length=5, max_length=120)
    description: str = Field(min_length=20, max_length=900)
    owner: RoleKey
    asset: str = Field(min_length=3, max_length=120)
    threat: str = Field(min_length=5, max_length=300)
    vulnerability: str = Field(min_length=5, max_length=300)
    inherent_likelihood: int = Field(ge=1, le=5)
    inherent_impact: int = Field(ge=1, le=5)
    treatment: RiskTreatment
    controls: list[ControlId] = Field(default_factory=list)
    residual_likelihood: int = Field(ge=1, le=5)
    residual_impact: int = Field(ge=1, le=5)
    status: RiskStatus
    accepted_by: RoleKey | None = None
    acceptance_rationale: str = Field(default="", max_length=600)
    review_date: date
    interested_parties: list[InterestedPartyId] = Field(default_factory=list)
    legal: list[LegalId] = Field(default_factory=list)

    @property
    def inherent_score(self) -> int:
        return self.inherent_likelihood * self.inherent_impact

    @property
    def residual_score(self) -> int:
        return self.residual_likelihood * self.residual_impact

    @model_validator(mode="after")
    def _check(self) -> Self:
        problems: list[str] = []
        if self.residual_likelihood > self.inherent_likelihood:
            problems.append("residual likelihood exceeds inherent likelihood")
        if self.residual_impact > self.inherent_impact:
            problems.append("residual impact exceeds inherent impact")
        if self.treatment is RiskTreatment.MODIFY and not self.controls:
            problems.append("a risk treated by 'modify' must name the modifying controls")
        if self.treatment is RiskTreatment.RETAIN:
            if self.accepted_by is None or len(self.acceptance_rationale) < 20:
                problems.append("a retained risk needs accepted_by and an acceptance_rationale")
            if self.status is not RiskStatus.ACCEPTED:
                problems.append("a retained risk must have status 'accepted'")
        elif self.status is RiskStatus.ACCEPTED:
            problems.append("only retained risks carry status 'accepted'")
        if len(set(self.controls)) != len(self.controls):
            problems.append("duplicate controls")
        if problems:
            raise ValueError(f"{self.id}: " + "; ".join(problems))
        return self


class RiskRegister(StrictModel):
    risks: list[Risk] = Field(min_length=1)

    def by_id(self) -> dict[str, Risk]:
        return {risk.id: risk for risk in self.risks}

    @model_validator(mode="after")
    def _check(self) -> Self:
        ids = [risk.id for risk in self.risks]
        if len(set(ids)) != len(ids):
            raise ValueError("risk register: duplicate ids")
        return self
