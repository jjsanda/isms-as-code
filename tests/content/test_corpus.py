"""Compliance checks over the real corpus under isms/ — the repository audits itself."""

from __future__ import annotations

import re
from pathlib import Path

import pytest
import yaml

from isms_as_code.clock import FrozenClock
from isms_as_code.generate import build_artefacts, check_artefacts
from isms_as_code.loader import Repository, load_repository
from isms_as_code.models import DocumentStatus
from isms_as_code.validate import validate_repository

pytestmark = pytest.mark.content

STATEMENT_RE = re.compile(r"\*\*([A-Z]+)-(\d+)\*\*")


@pytest.fixture(scope="module")
def corpus(repo_root: Path) -> Repository:
    return load_repository(repo_root)


def test_corpus_validates_without_errors(corpus: Repository) -> None:
    findings = validate_repository(corpus, FrozenClock.at("2026-08-20"))
    errors = [f for f in findings if f.is_error]
    assert errors == [], [f"{f.where}: {f.message}" for f in errors]


def test_corpus_shape(corpus: Repository) -> None:
    assert len(corpus.controls) == 93
    assert len(corpus.catalogue.controls) == 93
    assert {g.meta.control for g in corpus.controls} == set(corpus.catalogue.by_id())
    assert len(corpus.documents) >= 27
    statuses = {d.meta.status for d in corpus.documents}
    assert statuses == set(DocumentStatus), "the corpus should show every life-cycle state"
    assert len(corpus.organisation.in_scope_entities()) == 3
    assert any(not e.in_scope for e in corpus.organisation.entities)
    assert sum(1 for g in corpus.controls if g.meta.entity_overrides) >= 1


def test_no_placeholders_left(repo_root: Path) -> None:
    offenders = []
    for path in [*(repo_root / "isms").rglob("*.md"), *(repo_root / "generated").rglob("*.md")]:
        text = path.read_text(encoding="utf-8")
        if "<!-- TODO" in text or "TODO " in text:
            offenders.append(path.relative_to(repo_root).as_posix())
    assert offenders == []


def test_generated_artefacts_are_in_sync(repo_root: Path, corpus: Repository) -> None:
    assert check_artefacts(repo_root, build_artefacts(corpus)) == []


def test_statement_ids_are_unique_sequential_and_match_the_document(corpus: Repository) -> None:
    for document in corpus.documents:
        if document.meta.type.value == "procedure":
            continue
        mnemonic = document.meta.id.split("-", 1)[1]
        found = STATEMENT_RE.findall(document.body)
        assert found, f"{document.meta.id} has no statement ids"
        prefixes = {p for p, _ in found}
        assert prefixes == {
            mnemonic
        }, f"{document.meta.id}: foreign statement ids {prefixes - {mnemonic}}"
        numbers = [int(n) for _, n in found]
        assert numbers == list(
            range(1, len(numbers) + 1)
        ), f"{document.meta.id}: ids not sequential: {numbers}"


def test_related_documents_section_matches_front_matter(corpus: Repository) -> None:
    for document in corpus.documents:
        section = document.body.split("## Related documents", 1)[1]
        listed = set(re.findall(r"^- ((?:POL|STD|PROC)-[A-Z]+) — ", section, flags=re.MULTILINE))
        assert listed == set(
            document.meta.related
        ), f"{document.meta.id}: {listed ^ set(document.meta.related)}"


def test_documents_name_roles_not_people(repo_root: Path, corpus: Repository) -> None:
    holders = [role.holder for role in corpus.roles.roles]
    for document in corpus.documents:
        for holder in holders:
            assert (
                holder not in document.body
            ), f"{document.meta.id} names a person ({holder}) instead of a role"
    for guide in corpus.controls:
        for holder in holders:
            assert holder not in guide.body, f"{guide.meta.control} names a person ({holder})"


def test_documents_have_substance(corpus: Repository) -> None:
    for document in corpus.documents:
        lines = len(document.body.splitlines())
        minimum = 45 if document.meta.status is DocumentStatus.RETIRED else 80
        assert lines >= minimum, f"{document.meta.id} has only {lines} body lines"
    for guide in corpus.controls:
        assert len(guide.body.splitlines()) >= 18, f"{guide.meta.control} guide is too thin"


def test_catalogue_attributes_are_complete(repo_root: Path) -> None:
    data = yaml.safe_load(
        (repo_root / "isms/catalogue/iso27001-2022-annex-a.yaml").read_text(encoding="utf-8")
    )
    new = [c["id"] for c in data["controls"] if c["new_in_2022"]]
    assert new == [
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
    ]
    for control in data["controls"]:
        assert control["control_type"] and control["properties"] and control["concepts"], control[
            "id"
        ]


def test_every_risk_is_cited_by_a_control_guide(corpus: Repository) -> None:
    cited = {r for g in corpus.controls for r in g.meta.risks}
    assert cited == set(corpus.risks.by_id()), set(corpus.risks.by_id()) - cited


def test_every_approved_document_implements_a_control_or_clause(corpus: Repository) -> None:
    credited = {d for g in corpus.controls for d in g.meta.implemented_by}
    for document in corpus.approved_documents():
        assert document.meta.id in credited or document.meta.clauses, document.meta.id
