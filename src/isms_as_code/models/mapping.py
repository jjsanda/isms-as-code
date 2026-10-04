"""External requirement mappings (NIS2 Art. 21, ISO 27001 clauses ...) onto controls and documents."""

from __future__ import annotations

from typing import Self

from pydantic import Field, model_validator

from isms_as_code.ids import ControlId, DocumentId
from isms_as_code.models.base import StrictModel

__all__ = ["MappingRequirement", "Mapping"]


class MappingRequirement(StrictModel):
    id: str = Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9.()\-]*$", max_length=30)
    title: str = Field(min_length=3, max_length=160)
    description: str = Field(min_length=10, max_length=900)
    controls: list[ControlId] = Field(default_factory=list)
    documents: list[DocumentId] = Field(default_factory=list)
    notes: str = Field(default="", max_length=600)

    @model_validator(mode="after")
    def _check(self) -> Self:
        if not self.controls and not self.documents:
            raise ValueError(f"{self.id}: map to at least one control or document")
        if len(set(self.controls)) != len(self.controls):
            raise ValueError(f"{self.id}: duplicate controls")
        if len(set(self.documents)) != len(self.documents):
            raise ValueError(f"{self.id}: duplicate documents")
        return self


class Mapping(StrictModel):
    name: str = Field(pattern=r"^[a-z0-9]+(-[a-z0-9]+)*$", max_length=40)
    title: str = Field(min_length=3, max_length=160)
    source: str = Field(min_length=3, max_length=200, description="Official citation.")
    description: str = Field(min_length=10, max_length=900)
    requirements: list[MappingRequirement] = Field(min_length=1)

    @model_validator(mode="after")
    def _check(self) -> Self:
        ids = [requirement.id for requirement in self.requirements]
        if len(set(ids)) != len(ids):
            raise ValueError(f"mapping {self.name}: duplicate requirement ids")
        return self
