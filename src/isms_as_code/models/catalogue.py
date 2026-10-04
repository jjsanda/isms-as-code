"""The ISO/IEC 27001:2022 Annex A reference catalogue (identifiers, titles and attributes)."""

from __future__ import annotations

from collections import Counter
from typing import Self

from pydantic import Field, model_validator

from isms_as_code.ids import ControlId, control_sort_key
from isms_as_code.models.base import (
    ControlType,
    CyberConcept,
    SecurityProperty,
    StrictModel,
    Theme,
)

__all__ = ["CatalogueControl", "Catalogue", "EXPECTED_THEME_COUNTS", "THEME_BY_PREFIX"]

EXPECTED_THEME_COUNTS: dict[Theme, int] = {
    Theme.ORGANIZATIONAL: 37,
    Theme.PEOPLE: 8,
    Theme.PHYSICAL: 14,
    Theme.TECHNOLOGICAL: 34,
}
THEME_BY_PREFIX: dict[int, Theme] = {
    5: Theme.ORGANIZATIONAL,
    6: Theme.PEOPLE,
    7: Theme.PHYSICAL,
    8: Theme.TECHNOLOGICAL,
}


class CatalogueControl(StrictModel):
    id: ControlId
    title: str = Field(min_length=3, max_length=120)
    theme: Theme
    control_type: list[ControlType] = Field(min_length=1)
    properties: list[SecurityProperty] = Field(min_length=1)
    concepts: list[CyberConcept] = Field(min_length=1)
    new_in_2022: bool = False

    @model_validator(mode="after")
    def _check(self) -> Self:
        expected = THEME_BY_PREFIX[control_sort_key(self.id)[0]]
        if self.theme is not expected:
            raise ValueError(
                f"{self.id}: theme must be {expected.value} (id prefix), not {self.theme}"
            )
        return self


class Catalogue(StrictModel):
    standard: str = Field(min_length=3)
    source_note: str = ""
    controls: list[CatalogueControl] = Field(min_length=1)

    def by_id(self) -> dict[str, CatalogueControl]:
        return {control.id: control for control in self.controls}

    def sorted(self) -> list[CatalogueControl]:
        return sorted(self.controls, key=lambda c: control_sort_key(c.id))

    def by_theme(self, theme: Theme) -> list[CatalogueControl]:
        return [control for control in self.sorted() if control.theme is theme]

    @model_validator(mode="after")
    def _check(self) -> Self:
        problems: list[str] = []
        ids = [control.id for control in self.controls]
        dupes = sorted({cid for cid, count in Counter(ids).items() if count > 1})
        if dupes:
            problems.append(f"duplicate control ids: {dupes}")
        counts = Counter(control.theme for control in self.controls)
        for theme, expected in EXPECTED_THEME_COUNTS.items():
            if counts.get(theme, 0) != expected:
                problems.append(
                    f"theme {theme.value} has {counts.get(theme, 0)} controls, expected {expected}"
                )
        if len(ids) != 93:
            problems.append(f"Annex A:2022 has 93 controls, catalogue lists {len(ids)}")
        new = sum(1 for control in self.controls if control.new_in_2022)
        if new != 11:
            problems.append(f"Annex A:2022 introduced 11 new controls, catalogue flags {new}")
        if problems:
            raise ValueError("catalogue: " + "; ".join(problems))
        return self
