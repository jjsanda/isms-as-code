"""Roles are the stable unit of ownership; holders are data that changes without touching documents."""

from __future__ import annotations

from typing import Self

from pydantic import Field, model_validator

from isms_as_code.ids import RoleKey
from isms_as_code.models.base import StrictModel

__all__ = ["Role", "RoleRegister"]


class Role(StrictModel):
    key: RoleKey
    title: str = Field(min_length=3, max_length=120)
    description: str = Field(min_length=10, max_length=600)
    holder: str = Field(min_length=3, max_length=80, description="Current (fictional) holder.")
    email: str = Field(pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    github: str = Field(
        pattern=r"^@[A-Za-z0-9-]+(/[A-Za-z0-9._-]+)?$",
        description="GitHub user or team used for CODEOWNERS review routing.",
    )
    deputy: RoleKey | None = None


class RoleRegister(StrictModel):
    roles: list[Role] = Field(min_length=1)

    def by_key(self) -> dict[str, Role]:
        return {role.key: role for role in self.roles}

    def get(self, key: str) -> Role:
        return self.by_key()[key]

    @model_validator(mode="after")
    def _check(self) -> Self:
        keys = [role.key for role in self.roles]
        problems: list[str] = []
        if len(set(keys)) != len(keys):
            problems.append("duplicate role keys")
        for role in self.roles:
            if role.deputy is not None and role.deputy not in keys:
                problems.append(f"{role.key}: deputy {role.deputy} is not a known role")
            if role.deputy == role.key:
                problems.append(f"{role.key}: a role cannot deputise for itself")
        if problems:
            raise ValueError("roles: " + "; ".join(problems))
        return self
