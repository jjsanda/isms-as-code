from __future__ import annotations

import subprocess
from datetime import date
from pathlib import Path

import pytest
from typer.testing import CliRunner

from isms_as_code.cli import app
from isms_as_code.gitcheck import changed_document_folders, check_changelogs
from isms_as_code.loader import load_repository
from isms_as_code.scaffold import scaffold_document
from isms_as_code.validate import validate_repository
from tests.conftest import RepoBuilder

pytestmark = pytest.mark.cli

runner = CliRunner()
TEMPLATES = Path(__file__).resolve().parents[2] / "isms" / "templates"


def with_templates(builder: RepoBuilder) -> RepoBuilder:
    for name in ("policy.md", "standard.md", "procedure.md", "CHANGELOG.md"):
        builder.write(f"isms/templates/{name}", (TEMPLATES / name).read_text(encoding="utf-8"))
    return builder


def test_scaffold_creates_a_valid_draft(builder: RepoBuilder) -> None:
    with_templates(builder)
    folder = scaffold_document(
        builder.root,
        "policy",
        "POL-NEW",
        "New Topic Policy",
        "isms-manager",
        "managing-director",
        ["A.5.10"],
        date(2026, 8, 20),
    )
    assert folder.name == "POL-NEW-new-topic-policy"
    readme = (folder / "README.md").read_text(encoding="utf-8")
    assert (
        "id: POL-NEW" in readme and "status: draft" in readme and "- **NEW-1** Statement." in readme
    )
    assert "# POL-NEW — New Topic Policy" in readme
    assert "## [0.1.0] - 2026-08-20" in (folder / "CHANGELOG.md").read_text(encoding="utf-8")
    repo = load_repository(builder.root)
    findings = validate_repository(repo)
    assert not any(f.is_error for f in findings), [f.message for f in findings if f.is_error]
    with pytest.raises(FileExistsError):
        scaffold_document(
            builder.root,
            "policy",
            "POL-NEW",
            "New Topic Policy",
            "isms-manager",
            "managing-director",
            [],
            date(2026, 8, 20),
        )
    with pytest.raises(ValueError):
        scaffold_document(
            builder.root,
            "standard",
            "POL-BAD",
            "Bad",
            "isms-manager",
            "managing-director",
            [],
            date(2026, 8, 20),
        )


def test_new_command(builder: RepoBuilder) -> None:
    with_templates(builder)
    result = runner.invoke(
        app,
        [
            "new",
            "procedure",
            "--id",
            "PROC-TEST",
            "--title",
            "Test Procedure",
            "--owner",
            "isms-manager",
            "--approver",
            "managing-director",
            "--root",
            str(builder.root),
        ],
    )
    assert result.exit_code == 0, result.output
    assert "created isms/procedures/PROC-TEST-test-procedure" in result.output
    result = runner.invoke(
        app,
        [
            "new",
            "procedure",
            "--id",
            "PROC-TEST",
            "--title",
            "Test Procedure",
            "--owner",
            "isms-manager",
            "--approver",
            "managing-director",
            "--root",
            str(builder.root),
        ],
    )
    assert result.exit_code == 2


def git(root: Path, *args: str) -> None:
    subprocess.run(
        ["git", "-C", str(root), "-c", "user.name=t", "-c", "user.email=t@example.test", *args],
        check=True,
        capture_output=True,
    )


def test_changelog_check(builder: RepoBuilder) -> None:
    git(builder.root, "init", "-q", "-b", "main")
    git(builder.root, "add", "-A")
    git(builder.root, "commit", "-q", "-m", "base")
    assert check_changelogs(builder.root, "HEAD") == []
    # Edit the policy body without touching the CHANGELOG or version.
    readme = builder.root / "isms/policies/POL-TEST-test-policy/README.md"
    readme.write_text(readme.read_text(encoding="utf-8") + "\nMore text.\n", encoding="utf-8")
    problems = check_changelogs(builder.root, "HEAD")
    assert any("without a CHANGELOG.md entry" in p for p in problems)
    assert any("version must be bumped" in p for p in problems)
    assert changed_document_folders(builder.root, "HEAD") == {
        "isms/policies/POL-TEST-test-policy": {"README.md"}
    }
    # Bump the version and add an entry -> clean.
    builder.add_document(
        version="1.1.0",
        changelog="# Changelog\n\n## [1.1.0] - 2026-08-20\n\n### Changed\n\n- More text.\n\n## [1.0.0] - 2026-01-10\n\n### Added\n\n- Initial approved version.\n",
        last_reviewed=date(2026, 8, 20),
        next_review=date(2027, 8, 20),
        effective_date=date(2026, 8, 20),
    )
    assert check_changelogs(builder.root, "HEAD") == []
    # A brand-new document only needs its CHANGELOG.
    builder.add_document(id="POL-NEWX", title="Another Policy", controls=["A.5.10"])
    assert check_changelogs(builder.root, "HEAD") == []
    result = runner.invoke(app, ["changelog-check", "--base", "HEAD", "--root", str(builder.root)])
    assert result.exit_code == 0, result.output
    readme.write_text(readme.read_text(encoding="utf-8") + "\nEven more.\n", encoding="utf-8")
    (builder.root / "isms/policies/POL-TEST-test-policy/CHANGELOG.md").write_text(
        "# Changelog\n\n## [1.0.0] - 2026-01-10\n\n### Added\n\n- Initial approved version.\n",
        encoding="utf-8",
    )
    result = runner.invoke(app, ["changelog-check", "--base", "HEAD", "--root", str(builder.root)])
    assert result.exit_code == 1 and "need a CHANGELOG entry" in result.output
    assert (
        runner.invoke(
            app, ["changelog-check", "--base", "nonexistent-ref", "--root", str(builder.root)]
        ).exit_code
        == 2
    )
