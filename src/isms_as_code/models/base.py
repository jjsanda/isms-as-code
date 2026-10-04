"""The strict model base and the closed vocabularies used across the repository."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict

__all__ = [
    "StrictModel",
    "DocumentType",
    "DocumentStatus",
    "Classification",
    "Theme",
    "ControlType",
    "SecurityProperty",
    "CyberConcept",
    "Applicability",
    "ImplementationStatus",
    "EvidenceFrequency",
    "RiskTreatment",
    "RiskStatus",
    "PartyType",
    "LegalKind",
    "Nis2Status",
    "SiteKind",
]


class StrictModel(BaseModel):
    """Base for every record: unknown keys are rejected so schema drift fails fast."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)


class DocumentType(StrEnum):
    POLICY = "policy"
    STANDARD = "standard"
    PROCEDURE = "procedure"


class DocumentStatus(StrEnum):
    DRAFT = "draft"
    IN_REVIEW = "in-review"
    APPROVED = "approved"
    RETIRED = "retired"


class Classification(StrEnum):
    PUBLIC = "public"
    INTERNAL = "internal"
    CONFIDENTIAL = "confidential"
    RESTRICTED = "restricted"


class Theme(StrEnum):
    ORGANIZATIONAL = "organizational"
    PEOPLE = "people"
    PHYSICAL = "physical"
    TECHNOLOGICAL = "technological"


class ControlType(StrEnum):
    PREVENTIVE = "preventive"
    DETECTIVE = "detective"
    CORRECTIVE = "corrective"


class SecurityProperty(StrEnum):
    CONFIDENTIALITY = "confidentiality"
    INTEGRITY = "integrity"
    AVAILABILITY = "availability"


class CyberConcept(StrEnum):
    IDENTIFY = "identify"
    PROTECT = "protect"
    DETECT = "detect"
    RESPOND = "respond"
    RECOVER = "recover"


class Applicability(StrEnum):
    APPLICABLE = "applicable"
    NOT_APPLICABLE = "not-applicable"


class ImplementationStatus(StrEnum):
    IMPLEMENTED = "implemented"
    PARTIALLY_IMPLEMENTED = "partially-implemented"
    PLANNED = "planned"
    NOT_IMPLEMENTED = "not-implemented"


class EvidenceFrequency(StrEnum):
    CONTINUOUS = "continuous"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    SEMI_ANNUAL = "semi-annual"
    ANNUAL = "annual"
    ON_EVENT = "on-event"


class RiskTreatment(StrEnum):
    """ISO/IEC 27005 treatment options (modify = mitigate, retain = accept)."""

    MODIFY = "modify"
    RETAIN = "retain"
    AVOID = "avoid"
    SHARE = "share"


class RiskStatus(StrEnum):
    OPEN = "open"
    IN_TREATMENT = "in-treatment"
    TREATED = "treated"
    ACCEPTED = "accepted"


class PartyType(StrEnum):
    INTERNAL = "internal"
    EXTERNAL = "external"


class LegalKind(StrEnum):
    REGULATION = "regulation"
    DIRECTIVE = "directive"
    LAW = "law"
    STANDARD = "standard"
    CONTRACT = "contract"


class Nis2Status(StrEnum):
    ESSENTIAL = "essential"
    IMPORTANT = "important"
    NOT_COVERED = "not-covered"


class SiteKind(StrEnum):
    OFFICE = "office"
    DEPOT = "depot"
    FIELD_ESTATE = "field-estate"
    CLOUD_REGION = "cloud-region"
    DATA_CENTRE = "data-centre"
