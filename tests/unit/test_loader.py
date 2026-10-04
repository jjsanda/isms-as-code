from __future__ import annotations

import pytest

from isms_as_code.loader import LoaderError, load_repository
from tests.conftest import RepoBuilder

pytestmark = pytest.mark.unit


def test_minimal_repository_loads(builder: RepoBuilder) -> None:
    repo = load_repository(builder.root)
    assert len(repo.documents) == 1 and len(repo.controls) == 93 and len(repo.mappings) == 1
    assert repo.document("POL-TEST").changelog.latest.version == "1.0.0"
    assert repo.control("A.5.15").meta.implemented_by == ["POL-TEST"]
    assert (
        repo.relpath(repo.document("POL-TEST").path)
        == "isms/policies/POL-TEST-test-policy/README.md"
    )
    assert len(repo.source_paths()) == 7 + 1 + 2 + 93
    assert [d.meta.id for d in repo.approved_documents()] == ["POL-TEST"]


def test_errors_are_aggregated_across_files(builder: RepoBuilder) -> None:
    (builder.root / "isms/catalogue/iso27001-2022-annex-a.yaml").unlink()
    builder.write("isms/context/roles.yaml", "roles: [\n")
    builder.write("isms/risk/risk-register.yaml", "")
    with pytest.raises(LoaderError) as info:
        load_repository(builder.root)
    joined = "\n".join(info.value.errors)
    assert "iso27001-2022-annex-a.yaml: file not found" in joined
    assert "roles.yaml: invalid YAML" in joined
    assert "risk-register.yaml: file is empty" in joined
    assert str(info.value).startswith("3 problem(s)")


def test_front_matter_and_changelog_problems(builder: RepoBuilder) -> None:
    builder.add_document(approver="isms-manager")
    (builder.root / "isms/policies/POL-TEST-test-policy/CHANGELOG.md").unlink()
    builder.write(
        "isms/policies/POL-NOFM-no-front-matter/README.md", "# POL-NOFM — No Front Matter\n"
    )
    builder.write("isms/policies/POL-BADY-bad-yaml/README.md", "---\nid: [\n---\n")
    with pytest.raises(LoaderError) as info:
        load_repository(builder.root)
    joined = "\n".join(info.value.errors)
    assert "segregation of duties" in joined
    assert "no YAML front matter" in joined
    assert "invalid YAML front matter" in joined
    assert "CHANGELOG.md" not in joined  # the document failed validation first


def test_missing_changelog_is_an_error(builder: RepoBuilder) -> None:
    (builder.root / "isms/policies/POL-TEST-test-policy/CHANGELOG.md").unlink()
    with pytest.raises(LoaderError, match=r"needs a CHANGELOG\.md"):
        load_repository(builder.root)


def test_duplicate_document_and_control_ids(builder: RepoBuilder) -> None:
    builder.write(
        "isms/policies/POL-TEST-copy/README.md",
        builder.read("isms/policies/POL-TEST-test-policy/README.md"),
    )
    builder.write("isms/policies/POL-TEST-copy/CHANGELOG.md", "# Changelog\n")
    builder.write(
        "isms/controls/6-people/A.5.15.md",
        builder.read("isms/controls/5-organizational/A.5.15.md"),
    )
    with pytest.raises(LoaderError) as info:
        load_repository(builder.root)
    joined = "\n".join(info.value.errors)
    assert "duplicate document id POL-TEST" in joined
    assert "duplicate guide for A.5.15" in joined


def test_control_filename_and_mapping_name_must_match(builder: RepoBuilder) -> None:
    builder.write(
        "isms/controls/5-organizational/A.5.99.md",
        builder.read("isms/controls/5-organizational/A.5.1.md"),
    )
    builder.write("isms/mappings/other.yaml", builder.read("isms/mappings/test-mapping.yaml"))
    with pytest.raises(LoaderError) as info:
        load_repository(builder.root)
    joined = "\n".join(info.value.errors)
    assert "must be named A.5.1.md" in joined
    assert "must equal the file stem" in joined


def test_missing_directories_are_reported(builder: RepoBuilder) -> None:
    import shutil

    shutil.rmtree(builder.root / "isms/standards")
    shutil.rmtree(builder.root / "isms/controls/7-physical")
    shutil.rmtree(builder.root / "isms/mappings")
    with pytest.raises(LoaderError) as info:
        load_repository(builder.root)
    joined = "\n".join(info.value.errors)
    assert "isms/standards: directory for standard documents not found" in joined
    assert "7-physical: theme directory not found" in joined
    assert "isms/mappings: directory not found" in joined
