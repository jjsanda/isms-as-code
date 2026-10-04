from __future__ import annotations

import json
from pathlib import Path

import pytest

from isms_as_code.generate import build_artefacts, check_artefacts, write_artefacts
from isms_as_code.generate.coverage import FULL, GAP, PARTIAL, requirement_verdict
from isms_as_code.loader import load_repository
from tests.conftest import EVIDENCE, RepoBuilder

pytestmark = pytest.mark.generate


def paths(builder: RepoBuilder) -> set[str]:
    return {a.relpath.as_posix() for a in build_artefacts(load_repository(builder.root))}


def test_artefact_set(builder: RepoBuilder) -> None:
    assert paths(builder) == {
        "generated/statement-of-applicability.md",
        "generated/statement-of-applicability.csv",
        "generated/isms-scope-statement.md",
        "generated/document-register.md",
        "generated/risk-register.md",
        "generated/soa/ENT-AA.md",
        "generated/soa/ENT-BB.md",
        "generated/coverage-test-mapping.md",
        ".github/CODEOWNERS",
        "generated/badges/documents.json",
        "generated/badges/annex-a.json",
        "generated/badges/implemented.json",
        "generated/badges/risks.json",
        "generated/badges/test-mapping.json",
    }


def test_generation_is_deterministic_and_check_detects_drift(builder: RepoBuilder) -> None:
    repo = load_repository(builder.root)
    first = build_artefacts(repo)
    second = build_artefacts(load_repository(builder.root))
    assert [a.content for a in first] == [a.content for a in second]
    assert check_artefacts(builder.root, first) == [a.relpath.as_posix() for a in first]
    written = write_artefacts(builder.root, first)
    assert len(written) == len(first)
    assert check_artefacts(builder.root, first) == []
    builder.add_document(title="Test Policy", tags=["changed"])
    stale = check_artefacts(builder.root, build_artefacts(load_repository(builder.root)))
    assert "generated/statement-of-applicability.md" in stale  # digest header changed
    assert ".github/CODEOWNERS" in stale


def test_soa_markdown_and_entity_override(builder: RepoBuilder) -> None:
    builder.add_control(
        "A.5.16",
        implementation_status="implemented",
        implemented_by=[],
        evidence=[EVIDENCE],
        applicability="applicable",
        entity_overrides={
            "ENT-BB": {
                "applicability": "not-applicable",
                "justification": "No backend access from the Brno entity.",
            }
        },
    )
    # A.5.16 implemented without documents is rejected by the schema; use planned instead.
    builder.add_control(
        "A.5.16",
        implementation_status="planned",
        entity_overrides={
            "ENT-BB": {
                "applicability": "not-applicable",
                "justification": "No backend access from the Brno entity.",
            }
        },
    )
    artefacts = {
        a.relpath.as_posix(): a.content for a in build_artefacts(load_repository(builder.root))
    }
    group = artefacts["generated/statement-of-applicability.md"]
    assert "Source digest: sha256:" in group
    assert (
        "| [A.5.15](../isms/controls/5-organizational/A.5.15.md) | Synthetic control 5.15 | Yes |"
        in group
    )
    assert "[POL-TEST](../isms/policies/POL-TEST-test-policy/README.md)" in group
    assert "| **All themes** | 93 | 93 | 2 | 0 | 91 | 0 | 0 |" in group
    entity = artefacts["generated/soa/ENT-BB.md"]
    assert "Entity-level statement for Beta Test s.r.o." in entity
    assert "| **No** | No backend access from the Brno entity. | — | — |" in entity
    assert "| **All themes** | 93 | 92 |" in entity
    csv_text = artefacts["generated/statement-of-applicability.csv"]
    assert csv_text.splitlines()[0].startswith("control,title,theme,new_in_2022,applicable")
    assert len(csv_text.splitlines()) == 94


def test_coverage_verdicts(builder: RepoBuilder) -> None:
    repo = load_repository(builder.root)
    requirement = repo.mappings[0].requirements[0]
    assert requirement_verdict(repo, requirement) == FULL
    builder.add_control(
        "A.5.15",
        implementation_status="partially-implemented",
        implemented_by=["POL-TEST"],
        evidence=[EVIDENCE],
        risks=["R-001"],
    )
    repo = load_repository(builder.root)
    assert requirement_verdict(repo, repo.mappings[0].requirements[0]) == PARTIAL
    builder.add_control(
        "A.5.15", applicability="not-applicable", implementation_status=None, risks=[]
    )
    builder.write_yaml(
        "isms/risk/risk-register.yaml",
        {
            "risks": [
                {
                    **__import__("tests.conftest", fromlist=["default_risks"]).default_risks()[
                        "risks"
                    ][0],
                    "controls": ["A.5.31"],
                }
            ]
        },
    )
    repo = load_repository(builder.root)
    assert requirement_verdict(repo, repo.mappings[0].requirements[0]) == GAP
    report = {a.relpath.as_posix(): a.content for a in build_artefacts(repo)}[
        "generated/coverage-test-mapping.md"
    ]
    assert "❌ gap" in report and "| 1 | 0 | 0 | 1 |" in report


def test_codeowners_register_scope_risk_and_badges(builder: RepoBuilder) -> None:
    artefacts = {
        a.relpath.as_posix(): a.content for a in build_artefacts(load_repository(builder.root))
    }
    owners = artefacts[".github/CODEOWNERS"]
    assert owners.startswith("# Generated by `isms generate`")
    assert "*  @owner" in owners
    assert (
        "# POL-TEST: owner isms-manager, approver managing-director\n/isms/policies/POL-TEST-test-policy/  @owner\n"
        in owners
    )
    assert "/isms/controls/5-organizational/A.5.15.md  @owner" in owners
    register = artefacts["generated/document-register.md"]
    assert "## Review calendar" in register and "| 2027-01-10 | [POL-TEST]" in register
    assert "| Policys | 1 | 1 | 0 | 0 | 0 |" not in register  # pluralisation sanity
    assert "| Policies | 1 | 1 | 0 | 0 | 0 |" in register
    scope = artefacts["generated/isms-scope-statement.md"]
    assert "| ENT-CC | Gamma Test S.r.l. | Minority holding" in scope
    assert "All approved documents apply to every entity in scope." in scope
    risk = artefacts["generated/risk-register.md"]
    assert (
        "| R-001 | Synthetic unauthorised access risk |" in risk
        and "Residual risk heat map" in risk
    )
    for name in ("documents", "annex-a", "implemented", "risks", "test-mapping"):
        badge = json.loads(artefacts[f"generated/badges/{name}.json"])
        assert badge["schemaVersion"] == 1 and badge["label"] and badge["message"]
    assert json.loads(artefacts["generated/badges/documents.json"])["message"] == "1 (1 approved)"
    assert json.loads(artefacts["generated/badges/annex-a.json"])["message"] == "93/93 applicable"


def test_write_creates_directories(builder: RepoBuilder, tmp_path: Path) -> None:
    artefacts = build_artefacts(load_repository(builder.root))
    write_artefacts(builder.root, artefacts)
    assert (builder.root / "generated/soa/ENT-AA.md").is_file()
    assert (builder.root / ".github/CODEOWNERS").is_file()
