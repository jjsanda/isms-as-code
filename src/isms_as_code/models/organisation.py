"""The organisation and its ISMS scope: entities, sites, services, systems, interfaces (clause 4)."""

from __future__ import annotations

from enum import StrEnum
from typing import Self

from pydantic import Field, model_validator

from isms_as_code.ids import CountryCode, EntityId, RoleKey, ServiceId, SiteId
from isms_as_code.models.base import Classification, Nis2Status, SiteKind, StrictModel

__all__ = [
    "Entity",
    "Site",
    "Service",
    "InformationSystem",
    "Interface",
    "InterfaceDirection",
    "Organisation",
]


class InterfaceDirection(StrEnum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"
    BIDIRECTIONAL = "bidirectional"


class Entity(StrictModel):
    id: EntityId
    legal_name: str = Field(min_length=3, max_length=120)
    short_name: str = Field(min_length=2, max_length=40)
    country: CountryCode
    registered_office: str = Field(min_length=3, max_length=120)
    role: str = Field(
        min_length=5, max_length=300, description="What this entity does in the group."
    )
    headcount: int = Field(ge=0)
    ownership_percent: int = Field(default=100, ge=0, le=100)
    nis2_status: Nis2Status
    in_scope: bool
    justification: str = Field(default="", max_length=600)

    @model_validator(mode="after")
    def _check(self) -> Self:
        if not self.in_scope and len(self.justification) < 20:
            raise ValueError(f"{self.id}: an out-of-scope entity needs a justification")
        return self


class Site(StrictModel):
    id: SiteId
    name: str = Field(min_length=3, max_length=120)
    entity: EntityId
    city: str = Field(min_length=2, max_length=60)
    country: CountryCode
    kind: SiteKind
    functions: list[str] = Field(min_length=1)
    in_scope: bool
    justification: str = Field(default="", max_length=600)

    @model_validator(mode="after")
    def _check(self) -> Self:
        if not self.in_scope and len(self.justification) < 20:
            raise ValueError(f"{self.id}: an out-of-scope site needs a justification")
        return self


class Service(StrictModel):
    id: ServiceId
    name: str = Field(min_length=3, max_length=120)
    description: str = Field(min_length=10, max_length=600)
    entities: list[EntityId] = Field(min_length=1)
    in_scope: bool = True
    justification: str = Field(default="", max_length=600)


class InformationSystem(StrictModel):
    name: str = Field(min_length=3, max_length=120)
    description: str = Field(min_length=10, max_length=400)
    owner: RoleKey
    hosted_at: list[SiteId] = Field(min_length=1)
    classification: Classification


class Interface(StrictModel):
    party: str = Field(min_length=3, max_length=120)
    direction: InterfaceDirection
    description: str = Field(min_length=10, max_length=600)
    governed_by: list[str] = Field(min_length=1, description="Contracts, SLAs or document ids.")


class Organisation(StrictModel):
    group_name: str = Field(min_length=3, max_length=120)
    parent_entity: EntityId
    description: str = Field(min_length=20)
    sector: str = Field(min_length=3, max_length=200)
    certification_target: str = Field(min_length=3, max_length=120)
    isms_owner: RoleKey
    management_representative: RoleKey
    external_issues: list[str] = Field(min_length=1, description="Clause 4.1 external issues.")
    internal_issues: list[str] = Field(min_length=1, description="Clause 4.1 internal issues.")
    entities: list[Entity] = Field(min_length=1)
    sites: list[Site] = Field(min_length=1)
    services: list[Service] = Field(min_length=1)
    information_systems: list[InformationSystem] = Field(default_factory=list)
    interfaces: list[Interface] = Field(default_factory=list)

    def entity(self, entity_id: str) -> Entity:
        return self.entities_by_id()[entity_id]

    def entities_by_id(self) -> dict[str, Entity]:
        return {entity.id: entity for entity in self.entities}

    def in_scope_entities(self) -> list[Entity]:
        return [entity for entity in self.entities if entity.in_scope]

    def in_scope_sites(self) -> list[Site]:
        return [site for site in self.sites if site.in_scope]

    def sites_of(self, entity_id: str) -> list[Site]:
        return [site for site in self.sites if site.entity == entity_id]

    @model_validator(mode="after")
    def _check(self) -> Self:
        problems: list[str] = []
        entity_ids = [entity.id for entity in self.entities]
        if len(set(entity_ids)) != len(entity_ids):
            problems.append("duplicate entity ids")
        site_ids = [site.id for site in self.sites]
        if len(set(site_ids)) != len(site_ids):
            problems.append("duplicate site ids")
        service_ids = [service.id for service in self.services]
        if len(set(service_ids)) != len(service_ids):
            problems.append("duplicate service ids")
        known = set(entity_ids)
        if self.parent_entity not in known:
            problems.append(f"parent_entity {self.parent_entity} is not a listed entity")
        elif not self.entity(self.parent_entity).in_scope:
            problems.append("the parent entity must be in scope")
        for site in self.sites:
            if site.entity not in known:
                problems.append(f"site {site.id} belongs to unknown entity {site.entity}")
            elif site.in_scope and not self.entity(site.entity).in_scope:
                problems.append(f"site {site.id} is in scope but its entity {site.entity} is not")
        for service in self.services:
            unknown = sorted(set(service.entities) - known)
            if unknown:
                problems.append(f"service {service.id} names unknown entities {unknown}")
        for system in self.information_systems:
            unknown = sorted(set(system.hosted_at) - set(site_ids))
            if unknown:
                problems.append(f"system '{system.name}' is hosted at unknown sites {unknown}")
        if not any(entity.in_scope for entity in self.entities):
            problems.append("at least one entity must be in scope")
        if problems:
            raise ValueError("organisation: " + "; ".join(problems))
        return self
