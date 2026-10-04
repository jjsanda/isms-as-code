from __future__ import annotations

from datetime import date
from typing import Any

import pytest
from pydantic import ValidationError

from isms_as_code.models import (
    Catalogue,
    ControlGuideMeta,
    DocumentMeta,
    InterestedParty,
    LegalRequirement,
    Mapping,
    Organisation,
    Risk,
    RiskCriteria,
    RoleRegister,
)
from tests.conftest import (
    RepoBuilder,
    default_criteria,
    default_legal,
    default_mapping,
    default_organisation,
    default_risks,
    default_roles,
    synthetic_catalogue,
)

pytestmark = pytest.mark.unit


def doc(**over: Any) -> dict[str, Any]:
    return RepoBuilder.document_meta(**over)


def test_valid_document_meta_round_trips() -> None:
    meta = DocumentMeta.model_validate(doc())
    assert meta.is_approved and meta.applies_to_all and meta.cycle.humanize() == "1 year"


@pytest.mark.parametrize(
    ("overrides", "message"),
    [
        ({"approver": None}, "need an approver"),
        ({"approver": "isms-manager"}, "segregation of duties"),
        ({"version": "0.9.0"}, "version >= 1.0.0"),
        ({"status": "draft", "version": "1.0.0"}, "0.x.y versions"),
        ({"next_review": date(2027, 2, 1)}, "must equal last_reviewed"),
        ({"status": "retired"}, "superseded_by"),
        ({"superseded_by": "POL-OLD"}, "only retired documents"),
        ({"applies_to": ["all", "ENT-AA"]}, "not both"),
        ({"applies_to": ["Alpha"]}, "entity ids"),
        ({"controls": [], "clauses": []}, "at least one Annex A control"),
        ({"controls": ["A.5.15", "A.5.15"]}, "duplicate entries in controls"),
        ({"related": ["POL-TEST"]}, "cannot reference itself"),
        ({"effective_date": None}, "need effective_date"),
        ({"review_cycle": "P0D"}, "positive"),
        ({"unknown": 1}, "Extra inputs"),
    ],
)
def test_document_meta_rules(overrides: dict[str, Any], message: str) -> None:
    with pytest.raises(ValidationError, match=message):
        DocumentMeta.model_validate(doc(**overrides))


def test_draft_document_needs_no_dates() -> None:
    meta = DocumentMeta.model_validate(
        doc(
            status="draft",
            version="0.1.0",
            approver=None,
            effective_date=None,
            last_reviewed=None,
            next_review=None,
        )
    )
    assert meta.effective_date is None and not meta.is_approved


def test_retired_document() -> None:
    meta = DocumentMeta.model_validate(
        doc(status="retired", superseded_by="POL-NEW", retired_date=date(2026, 3, 1))
    )
    assert meta.superseded_by == "POL-NEW"


def ctl(**over: Any) -> dict[str, Any]:
    return RepoBuilder.control_meta("A.5.15", **over)


@pytest.mark.parametrize(
    ("overrides", "message"),
    [
        (
            {"applicability": "not-applicable", "implementation_status": "planned"},
            "no implementation status",
        ),
        (
            {
                "applicability": "not-applicable",
                "implementation_status": None,
                "implemented_by": ["POL-TEST"],
            },
            "cannot list implementing",
        ),
        ({"implementation_status": None}, "needs an implementation_status"),
        ({"implementation_status": "implemented"}, "at least one implementing document"),
        (
            {"implementation_status": "implemented", "implemented_by": ["POL-TEST"]},
            "at least one evidence item",
        ),
        (
            {"implemented_by": ["POL-AA", "POL-AA"], "implementation_status": "planned"},
            "duplicate entries in implemented_by",
        ),
        (
            {
                "entity_overrides": {
                    "ENT-AA": {
                        "applicability": "not-applicable",
                        "justification": "No development at this entity.",
                        "implementation_status": "planned",
                    }
                }
            },
            "cannot carry an implementation status",
        ),
        ({"justification": "short"}, "at least 10"),
    ],
)
def test_control_guide_rules(overrides: dict[str, Any], message: str) -> None:
    with pytest.raises(ValidationError, match=message):
        ControlGuideMeta.model_validate(ctl(**overrides))


def test_control_guide_entity_resolution() -> None:
    meta = ControlGuideMeta.model_validate(
        ctl(
            implementation_status="implemented",
            implemented_by=["POL-TEST"],
            evidence=[{"description": "Access review records"}],
            entity_overrides={
                "ENT-BB": {
                    "applicability": "not-applicable",
                    "justification": "No such systems at this entity.",
                },
                "ENT-AA": {
                    "applicability": "applicable",
                    "justification": "Applies with a stricter baseline.",
                    "implementation_status": "partially-implemented",
                },
            },
        )
    )
    assert meta.applicability_for("ENT-BB")[0].value == "not-applicable"
    assert meta.status_for("ENT-BB") is None
    overridden = meta.status_for("ENT-AA")
    assert overridden is not None and overridden.value == "partially-implemented"
    assert meta.applicability_for("ENT-ZZ")[1].startswith("Synthetic")
    inherited = meta.status_for("ENT-ZZ")
    assert inherited is not None and inherited.value == "implemented"


def risk(**over: Any) -> dict[str, Any]:
    data = dict(default_risks()["risks"][0])
    data.update(over)
    return data


@pytest.mark.parametrize(
    ("overrides", "message"),
    [
        ({"residual_likelihood": 5}, "residual likelihood exceeds"),
        ({"residual_impact": 5}, "residual impact exceeds"),
        ({"controls": []}, "must name the modifying controls"),
        ({"treatment": "retain", "status": "accepted"}, "needs accepted_by"),
        (
            {
                "treatment": "retain",
                "accepted_by": "isms-manager",
                "acceptance_rationale": "Within appetite given the compensating controls.",
            },
            "status 'accepted'",
        ),
        ({"status": "accepted"}, "only retained risks"),
    ],
)
def test_risk_rules(overrides: dict[str, Any], message: str) -> None:
    with pytest.raises(ValidationError, match=message):
        Risk.model_validate(risk(**overrides))


def test_risk_scores() -> None:
    item = Risk.model_validate(risk())
    assert (item.inherent_score, item.residual_score) == (16, 6)


def test_risk_criteria_band_lookup_and_rules() -> None:
    criteria = RiskCriteria.model_validate(default_criteria())
    assert criteria.band_for(6).name == "medium"
    assert criteria.band_for(25).acceptance is None
    with pytest.raises(ValueError):
        criteria.band_for(26)
    broken = default_criteria()
    broken["bands"][1]["min_score"] = 6
    with pytest.raises(ValidationError, match="contiguous"):
        RiskCriteria.model_validate(broken)
    broken = default_criteria()
    broken["bands"][-1]["max_score"] = 20
    with pytest.raises(ValidationError, match=r"cover scores 1\.\.25"):
        RiskCriteria.model_validate(broken)
    broken = default_criteria()
    del broken["treatment_options"]["share"]
    with pytest.raises(ValidationError, match="missing"):
        RiskCriteria.model_validate(broken)
    broken = default_criteria()
    broken["likelihood"][0]["level"] = 2
    with pytest.raises(ValidationError, match=r"levels 1\.\.5"):
        RiskCriteria.model_validate(broken)


def test_catalogue_completeness_rules() -> None:
    data = synthetic_catalogue()
    catalogue = Catalogue.model_validate(data)
    assert (
        len(catalogue.sorted()) == 93
        and catalogue.by_theme(catalogue.controls[0].theme)[0].id == "A.5.1"
    )
    data["controls"].pop()
    with pytest.raises(ValidationError, match="93 controls"):
        Catalogue.model_validate(data)
    data = synthetic_catalogue()
    data["controls"][0]["theme"] = "people"
    with pytest.raises(ValidationError, match="theme must be organizational"):
        Catalogue.model_validate(data)
    data = synthetic_catalogue()
    data["controls"][0]["new_in_2022"] = True
    with pytest.raises(ValidationError, match="11 new controls"):
        Catalogue.model_validate(data)
    data = synthetic_catalogue()
    data["controls"][1]["id"] = "A.5.1"
    with pytest.raises(ValidationError, match="duplicate control ids"):
        Catalogue.model_validate(data)


def test_organisation_rules() -> None:
    org = Organisation.model_validate(default_organisation())
    assert [e.id for e in org.in_scope_entities()] == ["ENT-AA", "ENT-BB"]
    assert org.sites_of("ENT-AA")[0].id == "SITE-AA-HQ"
    data = default_organisation()
    data["parent_entity"] = "ENT-ZZ"
    with pytest.raises(ValidationError, match="not a listed entity"):
        Organisation.model_validate(data)
    data = default_organisation()
    data["sites"][0]["entity"] = "ENT-CC"
    with pytest.raises(ValidationError, match="in scope but its entity"):
        Organisation.model_validate(data)
    data = default_organisation()
    data["entities"][2]["justification"] = ""
    with pytest.raises(ValidationError, match="needs a justification"):
        Organisation.model_validate(data)
    data = default_organisation()
    data["information_systems"][0]["hosted_at"] = ["SITE-ZZ-XX"]
    with pytest.raises(ValidationError, match="unknown sites"):
        Organisation.model_validate(data)


def test_role_register_rules() -> None:
    data = default_roles()
    data["roles"][2]["deputy"] = "nobody"
    with pytest.raises(ValidationError, match="not a known role"):
        RoleRegister.model_validate(data)
    data = default_roles()
    data["roles"][2]["deputy"] = "security-engineer"
    with pytest.raises(ValidationError, match="deputise for itself"):
        RoleRegister.model_validate(data)
    data = default_roles()
    data["roles"][0]["github"] = "owner"
    with pytest.raises(ValidationError, match="pattern"):
        RoleRegister.model_validate(data)


def test_mapping_legal_and_party_rules() -> None:
    data = default_mapping()
    data["requirements"][0]["controls"] = []
    data["requirements"][0]["documents"] = []
    with pytest.raises(ValidationError, match="at least one control or document"):
        Mapping.model_validate(data)
    legal = default_legal()["requirements"][0]
    legal["applies_to"] = ["all", "ENT-AA"]
    with pytest.raises(ValidationError, match=r"either \['all'\]"):
        LegalRequirement.model_validate(legal)
    with pytest.raises(ValidationError, match="document or control ids"):
        InterestedParty.model_validate(
            {
                "id": "IP-01",
                "name": "Customers",
                "kind": "external",
                "requirements": ["x"],
                "addressed_by": ["nope"],
            }
        )
