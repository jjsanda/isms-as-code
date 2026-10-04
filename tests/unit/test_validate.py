from __future__ import annotations

from datetime import date

import pytest

from isms_as_code.clock import FrozenClock
from isms_as_code.loader import load_repository
from isms_as_code.validate import Finding, count, has_errors, validate_repository
from tests.conftest import EVIDENCE, RepoBuilder, document_body

pytestmark = pytest.mark.unit


def run(builder: RepoBuilder, clock: FrozenClock | None = None) -> list[Finding]:
    return validate_repository(load_repository(builder.root), clock)


def errors(findings: list[Finding]) -> list[str]:
    return [f.message for f in findings if f.is_error]


def warnings(findings: list[Finding]) -> list[str]:
    return [f.message for f in findings if not f.is_error]


def test_minimal_repository_is_clean(builder: RepoBuilder, clock: FrozenClock) -> None:
    findings = run(builder, clock)
    assert findings == []
    assert not has_errors(findings) and count(findings) == (0, 0)


def test_folder_name_and_location(builder: RepoBuilder) -> None:
    builder.add_document(folder="POL-TEST-wrong")
    assert any("folder must be named POL-TEST-test-policy" in m for m in errors(run(builder)))


def test_document_structure(builder: RepoBuilder) -> None:
    builder.add_document(body="# POL-TEST — Test Policy\n\n## Purpose\n\nOnly purpose.\n")
    found = errors(run(builder))
    assert any("missing required sections: Scope, Policy statements" in m for m in found)
    builder.add_document(
        body="# Wrong Title\n" + document_body("POL-TEST", "Test Policy", "policy")
    )
    assert any("exactly one H1" in m for m in errors(run(builder)))


def test_changelog_agreement(builder: RepoBuilder) -> None:
    builder.add_document(version="1.1.0")
    assert any("does not match the newest CHANGELOG entry 1.0.0" in m for m in errors(run(builder)))
    builder.add_document(last_reviewed=date(2026, 2, 1), next_review=date(2027, 2, 1))
    assert any("must equal the newest CHANGELOG date" in m for m in errors(run(builder)))
    builder.add_document(effective_date=date(2025, 12, 1))
    assert any("precedes the approval date" in m for m in errors(run(builder)))
    builder.add_document(changelog="# Changelog\n\n## [Unreleased]\n\n### Added\n\n- x\n")
    assert any("not of the form" in m for m in errors(run(builder)))


def test_reference_resolution(builder: RepoBuilder) -> None:
    builder.add_document(
        owner="nobody",
        approver="ghost",
        controls=["A.5.15", "A.5.99"],
        related=["POL-NONE"],
        applies_to=["ENT-CC", "ENT-ZZ"],
    )
    found = errors(run(builder))
    assert any("owner 'nobody'" in m for m in found)
    assert any("approver 'ghost'" in m for m in found)
    assert any("unknown Annex A control A.5.99" in m for m in found)
    assert any("related document POL-NONE" in m for m in found)
    assert any("out-of-scope entity ENT-CC" in m for m in found)
    assert any("unknown entity ENT-ZZ" in m for m in found)


def test_control_guide_rules(builder: RepoBuilder) -> None:
    builder.add_control(
        "A.5.16",
        implementation_status="implemented",
        implemented_by=["POL-TEST", "POL-NONE"],
        evidence=[EVIDENCE],
        risks=["R-999"],
        owner="nobody",
        entity_overrides={
            "ENT-CC": {
                "applicability": "not-applicable",
                "justification": "Out of scope entity used for the test.",
            }
        },
    )
    found = errors(run(builder))
    assert any("POL-TEST is credited with A.5.16 but does not list it" in m for m in found)
    assert any("unknown document POL-NONE" in m for m in found)
    assert any("unknown risk R-999" in m for m in found)
    assert any("owner 'nobody'" in m for m in found)
    assert any("out-of-scope entity ENT-CC" in m for m in found)


def test_missing_guide_wrong_theme_dir_and_structure(builder: RepoBuilder) -> None:
    (builder.root / "isms/controls/8-technological/A.8.34.md").unlink()
    builder.write(
        "isms/controls/6-people/A.8.33.md", builder.read("isms/controls/8-technological/A.8.33.md")
    )
    (builder.root / "isms/controls/8-technological/A.8.33.md").unlink()
    builder.add_control("A.7.1", body="# A.7.1 — Synthetic control 7.1\n\n## Objective\n\nx\n")
    found = errors(run(builder))
    assert any("no implementation guide: A.8.34" in m for m in found)
    assert any("A.8.33 belongs under 8-technological/" in m for m in found)
    assert any("missing required sections: Implementation, Evidence" in m for m in found)


def test_reverse_credit_and_draft_implementer_are_warnings(builder: RepoBuilder) -> None:
    builder.add_document(controls=["A.5.15", "A.5.31", "A.5.16"])
    assert any(
        "A.5.16 but the control guide does not credit POL-TEST" in m for m in warnings(run(builder))
    )
    builder.add_document(
        id="POL-DRFT",
        title="Draft Policy",
        status="draft",
        version="0.1.0",
        approver=None,
        effective_date=None,
        last_reviewed=None,
        next_review=None,
        controls=["A.5.17"],
        changelog="# Changelog\n\n## [0.1.0] - 2026-08-01\n\n### Added\n\n- First draft.\n",
    )
    builder.add_control(
        "A.5.17",
        implementation_status="partially-implemented",
        implemented_by=["POL-DRFT"],
        evidence=[EVIDENCE],
    )
    found = run(builder)
    assert not has_errors(found)
    assert any("POL-DRFT is draft; it does not yet implement A.5.17" in m for m in warnings(found))


def test_supersession_must_be_mutual(builder: RepoBuilder) -> None:
    builder.add_document(
        id="POL-OLD",
        title="Old Policy",
        status="retired",
        superseded_by="POL-TEST",
        retired_date=date(2026, 3, 1),
        controls=["A.5.10"],
    )
    found = errors(run(builder))
    assert any("POL-TEST does not list POL-OLD in its supersedes field" in m for m in found)
    builder.add_document(supersedes=["POL-OLD"])
    assert errors(run(builder)) == []
    builder.add_document(supersedes=["POL-NONE"])
    assert any("superseded document POL-NONE does not exist" in m for m in errors(run(builder)))


def test_superseded_by_must_point_to_live_document(builder: RepoBuilder) -> None:
    builder.add_document(
        id="POL-OLD",
        title="Old Policy",
        status="retired",
        superseded_by="POL-GONE",
        retired_date=date(2026, 3, 1),
        controls=["A.5.10"],
    )
    assert any("superseded_by POL-GONE does not exist" in m for m in errors(run(builder)))
    builder.add_document(
        id="POL-GONE",
        title="Gone Policy",
        status="retired",
        superseded_by="POL-TEST",
        retired_date=date(2026, 4, 1),
        controls=["A.5.11"],
    )
    builder.add_document(supersedes=["POL-GONE"])
    assert any("superseded_by must point to a live document" in m for m in errors(run(builder)))


def test_risk_rules(builder: RepoBuilder) -> None:
    risks = {
        "risks": [
            {
                "id": "R-001",
                "title": "Synthetic unauthorised access risk",
                "description": "An attacker gains access to the backend through weak authentication.",
                "owner": "nobody",
                "asset": "Backend",
                "threat": "Credential compromise by an attacker",
                "vulnerability": "Weak authentication on administrative paths",
                "inherent_likelihood": 5,
                "inherent_impact": 5,
                "treatment": "retain",
                "controls": ["A.5.16", "A.5.99"],
                "residual_likelihood": 4,
                "residual_impact": 5,
                "status": "accepted",
                "accepted_by": "managing-director",
                "acceptance_rationale": "Accepted for the purpose of this unit test.",
                "review_date": date(2027, 1, 1),
                "interested_parties": ["IP-99"],
                "legal": ["LEG-99"],
            },
            {
                "id": "R-002",
                "title": "Retained risk with the wrong authority",
                "description": "A medium residual risk retained by the wrong role for this test.",
                "owner": "isms-manager",
                "asset": "Backend",
                "threat": "Something plausible happens",
                "vulnerability": "Something is weak",
                "inherent_likelihood": 3,
                "inherent_impact": 3,
                "treatment": "retain",
                "controls": [],
                "residual_likelihood": 2,
                "residual_impact": 3,
                "status": "accepted",
                "accepted_by": "security-engineer",
                "acceptance_rationale": "Accepted by the wrong role on purpose.",
                "review_date": date(2027, 1, 1),
            },
        ]
    }
    builder.write_yaml("isms/risk/risk-register.yaml", risks)
    builder.add_control("A.5.16", applicability="not-applicable", implementation_status=None)
    builder.add_control(
        "A.5.15",
        implementation_status="implemented",
        implemented_by=["POL-TEST"],
        evidence=[EVIDENCE],
    )
    found = errors(run(builder))
    assert any("R-001: owner 'nobody'" in m for m in found)
    assert any("A.5.16 is marked not applicable" in m for m in found)
    assert any("unknown control A.5.99" in m for m in found)
    assert any("unknown interested party IP-99" in m for m in found)
    assert any("unknown legal requirement LEG-99" in m for m in found)
    assert any("residual score 20 (critical) may not be retained" in m for m in found)
    assert any("must be accepted by 'isms-manager', not 'security-engineer'" in m for m in found)


def test_mapping_and_context_rules(builder: RepoBuilder) -> None:
    builder.write_yaml(
        "isms/mappings/test-mapping.yaml",
        {
            "name": "test-mapping",
            "title": "Test mapping",
            "source": "Synthetic source",
            "description": "Maps one synthetic requirement onto a control and a document.",
            "requirements": [
                {
                    "id": "1",
                    "title": "Requirement one",
                    "description": "A synthetic requirement.",
                    "controls": ["A.5.16", "A.5.99"],
                    "documents": ["POL-NONE"],
                }
            ],
        },
    )
    builder.add_control("A.5.16", applicability="not-applicable", implementation_status=None)
    builder.write_yaml(
        "isms/context/interested-parties.yaml",
        {
            "parties": [
                {
                    "id": "IP-01",
                    "name": "Customers",
                    "kind": "external",
                    "requirements": ["x"],
                    "addressed_by": ["POL-NONE", "A.5.99"],
                }
            ]
        },
    )
    legal = {
        "requirements": [
            {
                "id": "LEG-01",
                "title": "Test Regulation",
                "kind": "regulation",
                "reference": "Regulation (EU) 0000/0",
                "jurisdiction": "EU",
                "applies_to": ["ENT-ZZ"],
                "summary": "A synthetic regulation used to exercise the legal register rules.",
                "obligations": ["Keep records"],
                "owner": "nobody",
                "controls": ["A.5.99"],
                "documents": ["POL-NONE"],
            }
        ]
    }
    builder.write_yaml("isms/context/legal-register.yaml", legal)
    org = builder.read("isms/context/organisation.yaml").replace(
        "isms_owner: isms-manager", "isms_owner: nobody"
    )
    builder.write("isms/context/organisation.yaml", org)
    found = run(builder)
    err = errors(found)
    assert any("1: unknown control A.5.99" in m for m in err)
    assert any("1: unknown document POL-NONE" in m for m in err)
    assert any("IP-01: addressed_by references unknown POL-NONE" in m for m in err)
    assert any("LEG-01: owner 'nobody'" in m for m in err)
    assert any("LEG-01: applies_to names unknown entity ENT-ZZ" in m for m in err)
    assert any("LEG-01: unknown control A.5.99" in m for m in err)
    assert any("LEG-01: unknown document POL-NONE" in m for m in err)
    assert any("isms_owner 'nobody'" in m for m in err)
    assert any(
        "A.5.16 is not applicable; the requirement is not covered" in m for m in warnings(found)
    )


def test_mapping_to_unapproved_document_warns(builder: RepoBuilder) -> None:
    builder.add_document(
        status="in-review",
        version="0.3.0",
        approver=None,
        effective_date=None,
        last_reviewed=None,
        next_review=None,
        changelog="# Changelog\n\n## [0.3.0] - 2026-08-01\n\n### Added\n\n- Draft for review.\n",
    )
    builder.add_control("A.5.15", implementation_status="planned")
    builder.add_control("A.5.31", implementation_status="planned")
    found = run(builder)
    assert not has_errors(found)
    assert any("POL-TEST is in-review, not approved" in m for m in warnings(found))


def test_review_warnings_need_a_clock(builder: RepoBuilder) -> None:
    builder.add_document(
        effective_date=date(2024, 1, 10),
        last_reviewed=date(2024, 1, 10),
        next_review=date(2025, 1, 10),
        changelog="# Changelog\n\n## [1.0.0] - 2024-01-10\n\n### Added\n\n- Initial approved version.\n",
    )
    builder.add_control("A.6.1", last_assessed=date(2025, 1, 1))
    assert warnings(run(builder)) == []
    found = warnings(run(builder, FrozenClock.at("2026-08-20")))
    assert any("review overdue: next_review was 2025-01-10" in m for m in found)
    assert any("older than a year (last_assessed 2025-01-01)" in m for m in found)
