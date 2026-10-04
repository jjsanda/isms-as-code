from __future__ import annotations

import json

import pytest
from typer.testing import CliRunner

from isms_as_code import __version__
from isms_as_code.cli import app
from tests.conftest import RepoBuilder

pytestmark = pytest.mark.cli

runner = CliRunner()


def test_version() -> None:
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0 and result.output.strip() == __version__


def test_validate_and_strict(builder: RepoBuilder, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ISMS_NOW", "2026-08-20")
    result = runner.invoke(app, ["validate", "--root", str(builder.root)])
    assert result.exit_code == 0, result.output
    assert "0 error(s), 0 warning(s)" in result.output
    builder.add_document(controls=["A.5.15", "A.5.31", "A.5.16"])
    result = runner.invoke(app, ["validate", "--root", str(builder.root)])
    assert result.exit_code == 0 and "WARNING" in result.output
    result = runner.invoke(app, ["validate", "--root", str(builder.root), "--strict"])
    assert result.exit_code == 1
    builder.add_document(version="9.9.9")
    result = runner.invoke(app, ["validate", "--root", str(builder.root)])
    assert result.exit_code == 1 and "ERROR" in result.output


def test_loader_errors_exit_one(builder: RepoBuilder) -> None:
    (builder.root / "isms/context/roles.yaml").unlink()
    result = runner.invoke(app, ["validate", "--root", str(builder.root)])
    assert result.exit_code == 1 and "roles.yaml: file not found" in result.output


def test_generate_check_cycle(builder: RepoBuilder) -> None:
    result = runner.invoke(app, ["generate", "--root", str(builder.root), "--check"])
    assert result.exit_code == 1 and "STALE" in result.output
    result = runner.invoke(app, ["generate", "--root", str(builder.root)])
    assert result.exit_code == 0 and "generated 14 artefacts" in result.output
    result = runner.invoke(app, ["generate", "--root", str(builder.root), "--check"])
    assert result.exit_code == 0 and "up to date" in result.output
    builder.add_document(version="9.9.9")
    result = runner.invoke(app, ["generate", "--root", str(builder.root)])
    assert result.exit_code == 1 and "does not validate" in result.output


def test_soa_scope_register_outputs(builder: RepoBuilder) -> None:
    result = runner.invoke(app, ["soa", "--root", str(builder.root), "--format", "csv"])
    assert result.exit_code == 0 and result.output.startswith("control,title")
    result = runner.invoke(app, ["soa", "--root", str(builder.root), "--entity", "ENT-BB"])
    assert result.exit_code == 0 and "Beta Test s.r.o." in result.output
    assert (
        runner.invoke(app, ["soa", "--root", str(builder.root), "--entity", "ENT-ZZ"]).exit_code
        == 2
    )
    assert (
        runner.invoke(app, ["soa", "--root", str(builder.root), "--format", "xml"]).exit_code == 2
    )
    assert (
        "# ISMS Scope Statement"
        in runner.invoke(app, ["scope", "--root", str(builder.root)]).output
    )
    assert (
        "# Document register"
        in runner.invoke(app, ["register", "--root", str(builder.root)]).output
    )


def test_review_due_formats(builder: RepoBuilder, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ISMS_NOW", "2027-08-01")
    result = runner.invoke(app, ["review-due", "--root", str(builder.root), "--within", "30"])
    assert result.exit_code == 0 and "POL-TEST" in result.output and "late" in result.output
    result = runner.invoke(app, ["review-due", "--root", str(builder.root), "--format", "json"])
    payload = json.loads(result.output)
    assert payload["as_of"] == "2027-08-01" and any(i["id"] == "POL-TEST" for i in payload["items"])
    result = runner.invoke(app, ["review-due", "--root", str(builder.root), "--format", "md"])
    assert result.exit_code == 0 and result.output.startswith("# Reviews due as of 2027-08-01")
    assert (
        runner.invoke(app, ["review-due", "--root", str(builder.root), "--format", "xml"]).exit_code
        == 2
    )
