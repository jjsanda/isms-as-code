"""Pydantic models for every kind of record in the repository (all ``extra="forbid"``)."""

from isms_as_code.models.base import (
    Applicability,
    Classification,
    ControlType,
    CyberConcept,
    DocumentStatus,
    DocumentType,
    EvidenceFrequency,
    ImplementationStatus,
    LegalKind,
    Nis2Status,
    PartyType,
    RiskStatus,
    RiskTreatment,
    SecurityProperty,
    SiteKind,
    StrictModel,
    Theme,
)
from isms_as_code.models.catalogue import EXPECTED_THEME_COUNTS, Catalogue, CatalogueControl
from isms_as_code.models.control import ControlGuideMeta, EntityOverride, EvidenceItem
from isms_as_code.models.document import DocumentMeta
from isms_as_code.models.mapping import Mapping, MappingRequirement
from isms_as_code.models.organisation import (
    Entity,
    InformationSystem,
    Interface,
    Organisation,
    Service,
    Site,
)
from isms_as_code.models.parties import (
    InterestedParty,
    InterestedPartyRegister,
    LegalRegister,
    LegalRequirement,
)
from isms_as_code.models.risk import Band, Risk, RiskCriteria, RiskRegister, ScaleLevel
from isms_as_code.models.roles import Role, RoleRegister

__all__ = [
    # base
    "StrictModel",
    "Applicability",
    "Classification",
    "ControlType",
    "CyberConcept",
    "DocumentStatus",
    "DocumentType",
    "EvidenceFrequency",
    "ImplementationStatus",
    "LegalKind",
    "Nis2Status",
    "PartyType",
    "RiskStatus",
    "RiskTreatment",
    "SecurityProperty",
    "SiteKind",
    "Theme",
    # records
    "Catalogue",
    "CatalogueControl",
    "EXPECTED_THEME_COUNTS",
    "ControlGuideMeta",
    "EntityOverride",
    "EvidenceItem",
    "DocumentMeta",
    "Mapping",
    "MappingRequirement",
    "Entity",
    "InformationSystem",
    "Interface",
    "Organisation",
    "Service",
    "Site",
    "InterestedParty",
    "InterestedPartyRegister",
    "LegalRegister",
    "LegalRequirement",
    "Band",
    "Risk",
    "RiskCriteria",
    "RiskRegister",
    "ScaleLevel",
    "Role",
    "RoleRegister",
]
