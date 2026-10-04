"""Interested parties (clause 4.2) and the legal, regulatory and contractual register (A.5.31)."""

from __future__ import annotations

import re
from typing import Self

from pydantic import Field, model_validator

from isms_as_code.ids import (
    CONTROL_ID_RE,
    DOCUMENT_ID_RE,
    ControlId,
    DocumentId,
    InterestedPartyId,
    LegalId,
    RoleKey,
)
from isms_as_code.models.base import LegalKind, PartyType, StrictModel

__all__ = ["InterestedParty", "InterestedPartyRegister", "LegalRequirement", "LegalRegister"]

_REF_RE = re.compile(f"(?:{DOCUMENT_ID_RE})|(?:{CONTROL_ID_RE})")


class InterestedParty(StrictModel):
    id: InterestedPartyId
    name: str = Field(min_length=3, max_length=120)
    kind: PartyType
    requirements: list[str] = Field(min_length=1, description="What they need from the ISMS.")
    addressed_by: list[str] = Field(
        min_length=1, description="Document ids and/or control ids that answer the requirements."
    )

    @model_validator(mode="after")
    def _check(self) -> Self:
        bad = [ref for ref in self.addressed_by if not _REF_RE.fullmatch(ref)]
        if bad:
            raise ValueError(
                f"{self.id}: addressed_by must hold document or control ids, got {bad}"
            )
        return self


class InterestedPartyRegister(StrictModel):
    parties: list[InterestedParty] = Field(min_length=1)

    @model_validator(mode="after")
    def _check(self) -> Self:
        ids = [party.id for party in self.parties]
        if len(set(ids)) != len(ids):
            raise ValueError("interested parties: duplicate ids")
        return self


class LegalRequirement(StrictModel):
    id: LegalId
    title: str = Field(min_length=3, max_length=160)
    kind: LegalKind
    reference: str = Field(min_length=3, max_length=200, description="Official citation.")
    jurisdiction: str = Field(min_length=2, max_length=80)
    applies_to: list[str] = Field(min_length=1, description="Entity ids or ['all'].")
    summary: str = Field(min_length=20, max_length=900)
    obligations: list[str] = Field(min_length=1)
    owner: RoleKey
    controls: list[ControlId] = Field(default_factory=list)
    documents: list[DocumentId] = Field(default_factory=list)
    verify_note: str = Field(
        default="",
        max_length=400,
        description="Anything that must be re-checked periodically (e.g. national transposition).",
    )

    @model_validator(mode="after")
    def _check(self) -> Self:
        if "all" in self.applies_to and self.applies_to != ["all"]:
            raise ValueError(f"{self.id}: applies_to is either ['all'] or entity ids")
        if not self.controls and not self.documents:
            raise ValueError(f"{self.id}: map the requirement to at least one control or document")
        return self


class LegalRegister(StrictModel):
    requirements: list[LegalRequirement] = Field(min_length=1)

    @model_validator(mode="after")
    def _check(self) -> Self:
        ids = [item.id for item in self.requirements]
        if len(set(ids)) != len(ids):
            raise ValueError("legal register: duplicate ids")
        return self
