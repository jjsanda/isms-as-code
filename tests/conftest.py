"""Shared fixtures: a pinned clock and a builder that writes a minimal, *valid* repository.

The builder produces a synthetic ISMS (a 93-control catalogue with placeholder titles, three
roles, a two-entity group, one risk, one mapping, one approved policy and a guide per control).
Tests then break exactly one thing and assert on the resulting error or warning, which keeps every
rule in the loader and validator covered without depending on the real corpus under ``isms/``.
"""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

import pytest
import yaml

from isms_as_code.clock import FrozenClock
from isms_as_code.ids import slugify
from isms_as_code.sections import REQUIRED_SECTIONS

TODAY = date(2026, 8, 20)
NEW_IN_2022 = {
    "A.5.7",
    "A.5.23",
    "A.5.30",
    "A.7.4",
    "A.8.9",
    "A.8.10",
    "A.8.11",
    "A.8.12",
    "A.8.16",
    "A.8.23",
    "A.8.28",
}
THEME_SIZES = {
    5: ("organizational", 37),
    6: ("people", 8),
    7: ("physical", 14),
    8: ("technological", 34),
}
THEME_DIR = {
    "organizational": "5-organizational",
    "people": "6-people",
    "physical": "7-physical",
    "technological": "8-technological",
}
DOC_DIR = {"policy": "isms/policies", "standard": "isms/standards", "procedure": "isms/procedures"}


def synthetic_catalogue() -> dict[str, Any]:
    controls: list[dict[str, Any]] = []
    for prefix, (theme, size) in THEME_SIZES.items():
        for number in range(1, size + 1):
            control_id = f"A.{prefix}.{number}"
            controls.append(
                {
                    "id": control_id,
                    "title": f"Synthetic control {prefix}.{number}",
                    "theme": theme,
                    "control_type": ["preventive"],
                    "properties": ["confidentiality"],
                    "concepts": ["protect"],
                    "new_in_2022": control_id in NEW_IN_2022,
                }
            )
    return {
        "standard": "ISO/IEC 27001:2022 Annex A (synthetic test catalogue)",
        "controls": controls,
    }


def document_body(doc_id: str, title: str, doc_type: str) -> str:
    sections = REQUIRED_SECTIONS[doc_type]
    return f"# {doc_id} — {title}\n\n" + "".join(
        f"## {section}\n\nText for {section.lower()}.\n\n" for section in sections
    )


def control_body(control_id: str, title: str) -> str:
    sections = REQUIRED_SECTIONS["control-guide"]
    return f"# {control_id} — {title}\n\n" + "".join(
        f"## {section}\n\nText for {section.lower()}.\n\n" for section in sections
    )


def front_matter(meta: dict[str, Any]) -> str:
    return "---\n" + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True) + "---\n\n"


def default_roles() -> dict[str, Any]:
    return {
        "roles": [
            {
                "key": "managing-director",
                "title": "Managing Director",
                "description": "Top management; approves the information security policy.",
                "holder": "Test Director",
                "email": "director@example.test",
                "github": "@owner",
                "deputy": "isms-manager",
            },
            {
                "key": "isms-manager",
                "title": "ISMS Manager",
                "description": "Runs the ISMS day to day and owns most documents.",
                "holder": "Test Manager",
                "email": "manager@example.test",
                "github": "@owner",
                "deputy": "security-engineer",
            },
            {
                "key": "security-engineer",
                "title": "Security Engineer",
                "description": "Implements and operates technical controls.",
                "holder": "Test Engineer",
                "email": "engineer@example.test",
                "github": "@owner",
            },
        ]
    }


def default_organisation() -> dict[str, Any]:
    return {
        "group_name": "Test Group",
        "parent_entity": "ENT-AA",
        "description": "A synthetic organisation used by the unit tests of the toolkit.",
        "sector": "Testing",
        "certification_target": "ISO/IEC 27001:2022",
        "isms_owner": "isms-manager",
        "management_representative": "managing-director",
        "external_issues": ["Regulatory pressure"],
        "internal_issues": ["Small team"],
        "entities": [
            {
                "id": "ENT-AA",
                "legal_name": "Alpha Test GmbH",
                "short_name": "Alpha",
                "country": "AT",
                "registered_office": "Vienna",
                "role": "Parent entity that operates the service.",
                "headcount": 10,
                "nis2_status": "essential",
                "in_scope": True,
            },
            {
                "id": "ENT-BB",
                "legal_name": "Beta Test s.r.o.",
                "short_name": "Beta",
                "country": "CZ",
                "registered_office": "Brno",
                "role": "Development centre of the group.",
                "headcount": 5,
                "nis2_status": "not-covered",
                "in_scope": True,
            },
            {
                "id": "ENT-CC",
                "legal_name": "Gamma Test S.r.l.",
                "short_name": "Gamma",
                "country": "IT",
                "registered_office": "Milan",
                "role": "Minority-held reseller joint venture.",
                "headcount": 3,
                "ownership_percent": 40,
                "nis2_status": "not-covered",
                "in_scope": False,
                "justification": "Minority holding without access to group systems; excluded.",
            },
        ],
        "sites": [
            {
                "id": "SITE-AA-HQ",
                "name": "Alpha head office",
                "entity": "ENT-AA",
                "city": "Vienna",
                "country": "AT",
                "kind": "office",
                "functions": ["Head office"],
                "in_scope": True,
            }
        ],
        "services": [
            {
                "id": "SVC-01",
                "name": "Test service",
                "description": "The service the synthetic ISMS protects.",
                "entities": ["ENT-AA"],
            }
        ],
        "information_systems": [
            {
                "name": "Test platform",
                "description": "Backend of the test service.",
                "owner": "isms-manager",
                "hosted_at": ["SITE-AA-HQ"],
                "classification": "confidential",
            }
        ],
        "interfaces": [
            {
                "party": "Cloud provider",
                "direction": "bidirectional",
                "description": "Hosting of the backend under the shared-responsibility model.",
                "governed_by": ["Cloud master agreement"],
            }
        ],
    }


def default_parties() -> dict[str, Any]:
    return {
        "parties": [
            {
                "id": "IP-01",
                "name": "Customers",
                "kind": "external",
                "requirements": ["Confidentiality of their data"],
                "addressed_by": ["POL-TEST", "A.5.15"],
            }
        ]
    }


def default_legal() -> dict[str, Any]:
    return {
        "requirements": [
            {
                "id": "LEG-01",
                "title": "Test Regulation",
                "kind": "regulation",
                "reference": "Regulation (EU) 0000/0",
                "jurisdiction": "EU",
                "applies_to": ["all"],
                "summary": "A synthetic regulation used to exercise the legal register rules.",
                "obligations": ["Keep records of processing"],
                "owner": "isms-manager",
                "controls": ["A.5.31"],
                "documents": ["POL-TEST"],
            }
        ]
    }


def default_criteria() -> dict[str, Any]:
    levels = ["Rare", "Unlikely", "Possible", "Likely", "Almost certain"]
    impacts = ["Negligible", "Minor", "Moderate", "Major", "Severe"]
    return {
        "method": "5x5 likelihood times impact; residual risk is re-scored after treatment.",
        "likelihood": [
            {
                "level": i + 1,
                "label": label,
                "description": f"Likelihood level {i + 1} description.",
            }
            for i, label in enumerate(levels)
        ],
        "impact": [
            {"level": i + 1, "label": label, "description": f"Impact level {i + 1} description."}
            for i, label in enumerate(impacts)
        ],
        "bands": [
            {
                "name": "low",
                "min_score": 1,
                "max_score": 4,
                "response": "Monitor; retain allowed.",
                "acceptance": "isms-manager",
            },
            {
                "name": "medium",
                "min_score": 5,
                "max_score": 9,
                "response": "Treat within a year.",
                "acceptance": "isms-manager",
            },
            {
                "name": "high",
                "min_score": 10,
                "max_score": 15,
                "response": "Treat within a quarter.",
                "acceptance": "managing-director",
            },
            {
                "name": "critical",
                "min_score": 16,
                "max_score": 25,
                "response": "Treat immediately; never retained.",
            },
        ],
        "treatment_options": {
            "modify": "Reduce likelihood or impact with controls.",
            "retain": "Accept the residual risk within appetite.",
            "avoid": "Stop the activity that causes the risk.",
            "share": "Transfer part of the risk to a third party.",
        },
    }


def default_risks() -> dict[str, Any]:
    return {
        "risks": [
            {
                "id": "R-001",
                "title": "Synthetic unauthorised access risk",
                "description": "An attacker gains access to the backend through weak authentication.",
                "owner": "isms-manager",
                "asset": "Backend",
                "threat": "Credential compromise by an attacker",
                "vulnerability": "Weak authentication on administrative paths",
                "inherent_likelihood": 4,
                "inherent_impact": 4,
                "treatment": "modify",
                "controls": ["A.5.15"],
                "residual_likelihood": 2,
                "residual_impact": 3,
                "status": "in-treatment",
                "review_date": date(2027, 1, 1),
            }
        ]
    }


def default_mapping() -> dict[str, Any]:
    return {
        "name": "test-mapping",
        "title": "Test mapping",
        "source": "Synthetic source",
        "description": "Maps one synthetic requirement onto a control and a document.",
        "requirements": [
            {
                "id": "1",
                "title": "Requirement one",
                "description": "A synthetic requirement.",
                "controls": ["A.5.15"],
                "documents": ["POL-TEST"],
            }
        ],
    }


EVIDENCE = {
    "description": "Quarterly access review records",
    "location": "Ticket system",
    "frequency": "quarterly",
}


@dataclass
class RepoBuilder:
    root: Path

    def write(self, relative: str, text: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def write_yaml(self, relative: str, data: Any) -> Path:
        return self.write(relative, yaml.safe_dump(data, sort_keys=False, allow_unicode=True))

    def read(self, relative: str) -> str:
        return (self.root / relative).read_text(encoding="utf-8")

    @staticmethod
    def document_meta(**overrides: Any) -> dict[str, Any]:
        meta: dict[str, Any] = {
            "id": "POL-TEST",
            "title": "Test Policy",
            "type": "policy",
            "status": "approved",
            "version": "1.0.0",
            "classification": "internal",
            "owner": "isms-manager",
            "approver": "managing-director",
            "effective_date": date(2026, 1, 10),
            "last_reviewed": date(2026, 1, 10),
            "review_cycle": "P1Y",
            "next_review": date(2027, 1, 10),
            "controls": ["A.5.15", "A.5.31"],
            "clauses": [],
            "applies_to": ["all"],
            "related": [],
            "supersedes": [],
            "language": "en",
            "tags": [],
        }
        meta.update(overrides)
        return {key: value for key, value in meta.items() if value is not None}

    def add_document(
        self,
        body: str | None = None,
        changelog: str | None = None,
        folder: str | None = None,
        **overrides: Any,
    ) -> Path:
        meta = self.document_meta(**overrides)
        folder_name = folder or f"{meta['id']}-{slugify(meta['title'])}"
        for stale in (self.root / DOC_DIR[meta["type"]]).glob(f"{meta['id']}-*"):
            if stale.name != folder_name:
                shutil.rmtree(stale)
        base = f"{DOC_DIR[meta['type']]}/{folder_name}"
        text = body if body is not None else document_body(meta["id"], meta["title"], meta["type"])
        path = self.write(f"{base}/README.md", front_matter(meta) + text)
        self.write(
            f"{base}/CHANGELOG.md",
            (
                changelog
                if changelog is not None
                else "# Changelog\n\n## [1.0.0] - 2026-01-10\n\n### Added\n\n- Initial approved version.\n"
            ),
        )
        return path

    @staticmethod
    def control_meta(control_id: str, **overrides: Any) -> dict[str, Any]:
        meta: dict[str, Any] = {
            "control": control_id,
            "applicability": "applicable",
            "justification": "Synthetic justification used by the unit tests.",
            "implementation_status": "planned",
            "implemented_by": [],
            "owner": "isms-manager",
            "risks": [],
            "evidence": [],
            "metrics": [],
            "entity_overrides": {},
            "last_assessed": date(2026, 6, 1),
        }
        meta.update(overrides)
        return {key: value for key, value in meta.items() if value is not None}

    def add_control(self, control_id: str, body: str | None = None, **overrides: Any) -> Path:
        meta = self.control_meta(control_id, **overrides)
        prefix = int(control_id.split(".")[1])
        theme = THEME_SIZES[prefix][0]
        title = f"Synthetic control {control_id[2:]}"
        text = body if body is not None else control_body(control_id, title)
        return self.write(
            f"isms/controls/{THEME_DIR[theme]}/{control_id}.md", front_matter(meta) + text
        )

    def add_all_controls(self) -> None:
        for prefix, (_, size) in THEME_SIZES.items():
            for number in range(1, size + 1):
                self.add_control(f"A.{prefix}.{number}")
        self.add_control(
            "A.5.15",
            implementation_status="implemented",
            implemented_by=["POL-TEST"],
            risks=["R-001"],
            evidence=[EVIDENCE],
        )
        self.add_control(
            "A.5.31",
            implementation_status="implemented",
            implemented_by=["POL-TEST"],
            evidence=[EVIDENCE],
        )

    def minimal(self) -> RepoBuilder:
        self.write("pyproject.toml", "[project]\nname = 'fixture'\n")
        self.write_yaml("isms/catalogue/iso27001-2022-annex-a.yaml", synthetic_catalogue())
        self.write_yaml("isms/context/roles.yaml", default_roles())
        self.write_yaml("isms/context/organisation.yaml", default_organisation())
        self.write_yaml("isms/context/interested-parties.yaml", default_parties())
        self.write_yaml("isms/context/legal-register.yaml", default_legal())
        self.write_yaml("isms/risk/risk-criteria.yaml", default_criteria())
        self.write_yaml("isms/risk/risk-register.yaml", default_risks())
        self.write_yaml("isms/mappings/test-mapping.yaml", default_mapping())
        for directory in DOC_DIR.values():
            (self.root / directory).mkdir(parents=True, exist_ok=True)
        self.add_document()
        self.add_all_controls()
        return self


@pytest.fixture
def today() -> date:
    return TODAY


@pytest.fixture
def clock() -> FrozenClock:
    return FrozenClock.at(TODAY)


@pytest.fixture
def builder(tmp_path: Path) -> RepoBuilder:
    return RepoBuilder(tmp_path).minimal()


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]
