"""The ``isms`` command line: validate, generate, render, sign and verify the document set."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from isms_as_code import __version__
from isms_as_code.build import CERT_NAME, run_build, sign_outputs, verify_outputs
from isms_as_code.clock import default_clock
from isms_as_code.generate import build_artefacts, check_artefacts, compute_digest, write_artefacts
from isms_as_code.generate.register import render_register
from isms_as_code.generate.scope import render_scope
from isms_as_code.generate.soa import render_soa, render_soa_csv
from isms_as_code.gitcheck import check_changelogs
from isms_as_code.layout import find_repo_root
from isms_as_code.loader import LoaderError, Repository, load_repository
from isms_as_code.render import PDF_AVAILABLE, render_all
from isms_as_code.review import due_items, render_due_json, render_due_markdown, render_due_table
from isms_as_code.scaffold import scaffold_document
from isms_as_code.signing import (
    DEV_COMMON_NAME,
    SIGNING_AVAILABLE,
    generate_key_material,
    load_key_material,
    to_pkcs12,
)
from isms_as_code.validate import count, has_errors, validate_repository

app = typer.Typer(
    help="ISMS-as-code: validate, generate, render and sign an ISO/IEC 27001:2022 document set.",
    no_args_is_help=True,
    add_completion=False,
    rich_markup_mode=None,
)

RootOption = Annotated[
    Path | None,
    typer.Option(
        "--root", help="Repository root (default: auto-detected from the current directory)."
    ),
]


def _resolve_root(root: Path | None) -> Path:
    return (root or find_repo_root()).resolve()


def _load(root: Path) -> Repository:
    try:
        return load_repository(root)
    except LoaderError as exc:
        typer.echo(f"{len(exc.errors)} problem(s) loading the repository:", err=True)
        for error in exc.errors:
            typer.echo(f"  ERROR   {error}", err=True)
        raise typer.Exit(code=1) from None


@app.command()
def validate(
    root: RootOption = None,
    strict: Annotated[bool, typer.Option("--strict", help="Treat warnings as errors.")] = False,
) -> None:
    """Validate front matter, cross-references, CHANGELOGs, structure and the control catalogue."""
    repo = _load(_resolve_root(root))
    findings = validate_repository(repo, default_clock())
    for finding in findings:
        typer.echo(f"  {finding.level.upper():7} {finding.where}: {finding.message}")
    errors, warnings = count(findings)
    typer.echo(
        f"validated {len(repo.documents)} documents, {len(repo.controls)} control guides, "
        f"{len(repo.risks.risks)} risks and {len(repo.mappings)} mappings: "
        f"{errors} error(s), {warnings} warning(s)"
    )
    if errors or (strict and warnings):
        raise typer.Exit(code=1)


def _load_valid(root: Path) -> Repository:
    """Load the repository and refuse to continue on validation errors."""
    repo = _load(root)
    findings = validate_repository(repo)
    if has_errors(findings):
        for finding in findings:
            if finding.is_error:
                typer.echo(f"  ERROR   {finding.where}: {finding.message}", err=True)
        typer.echo("the repository does not validate; fix the errors above first", err=True)
        raise typer.Exit(code=1)
    return repo


@app.command()
def generate(
    root: RootOption = None,
    check: Annotated[
        bool,
        typer.Option("--check", help="Do not write; fail if any generated file is out of date."),
    ] = False,
) -> None:
    """Generate the SoA, scope statement, registers, coverage reports, CODEOWNERS and badges."""
    repo_root = _resolve_root(root)
    repo = _load_valid(repo_root)
    artefacts = build_artefacts(repo)
    if check:
        stale = check_artefacts(repo_root, artefacts)
        if stale:
            typer.echo(
                "generated artefacts are out of date; run `isms generate` and commit:", err=True
            )
            for path in stale:
                typer.echo(f"  STALE   {path}", err=True)
            raise typer.Exit(code=1)
        typer.echo(
            f"{len(artefacts)} generated artefacts are up to date (digest {compute_digest(repo)[:12]})"
        )
        return
    written = write_artefacts(repo_root, artefacts)
    for written_path in written:
        typer.echo(f"  wrote   {repo.relpath(written_path)}")
    typer.echo(f"generated {len(written)} artefacts (digest {compute_digest(repo)[:12]})")


@app.command()
def soa(
    root: RootOption = None,
    entity: Annotated[
        str | None, typer.Option("--entity", help="Entity id for an entity-level SoA.")
    ] = None,
    fmt: Annotated[str, typer.Option("--format", help="md or csv")] = "md",
) -> None:
    """Print the Statement of Applicability (Markdown or CSV) to standard output."""
    repo = _load_valid(_resolve_root(root))
    if entity is not None and entity not in repo.organisation.entities_by_id():
        typer.echo(f"unknown entity {entity}", err=True)
        raise typer.Exit(code=2)
    if fmt == "csv":
        typer.echo(render_soa_csv(repo), nl=False)
    elif fmt == "md":
        typer.echo(render_soa(repo, compute_digest(repo), entity), nl=False)
    else:
        typer.echo("--format must be md or csv", err=True)
        raise typer.Exit(code=2)


@app.command()
def scope(root: RootOption = None) -> None:
    """Print the ISMS scope statement to standard output."""
    repo = _load_valid(_resolve_root(root))
    typer.echo(render_scope(repo, compute_digest(repo)), nl=False)


@app.command()
def register(root: RootOption = None) -> None:
    """Print the document register to standard output."""
    repo = _load_valid(_resolve_root(root))
    typer.echo(render_register(repo, compute_digest(repo)), nl=False)


@app.command("review-due")
def review_due(
    root: RootOption = None,
    within: Annotated[int, typer.Option("--within", help="Horizon in days.")] = 60,
    fmt: Annotated[str, typer.Option("--format", help="table, md or json")] = "table",
) -> None:
    """List documents and control assessments due (or overdue) within a number of days."""
    repo = _load(_resolve_root(root))
    today = default_clock().today()
    items = due_items(repo, today, within)
    if fmt == "json":
        typer.echo(render_due_json(items, today), nl=False)
    elif fmt == "md":
        typer.echo(render_due_markdown(items, repo, today), nl=False)
    elif fmt == "table":
        typer.echo(f"as of {today.isoformat()}, horizon {within} days")
        typer.echo(render_due_table(items, repo), nl=False)
    else:
        typer.echo("--format must be table, md or json", err=True)
        raise typer.Exit(code=2)


OutOption = Annotated[Path, typer.Option("--out", help="Output directory (default: dist/).")]
OnlyOption = Annotated[
    list[str] | None,
    typer.Option("--only", help="Restrict to these document/artefact ids (repeatable)."),
]


@app.command()
def render(
    root: RootOption = None,
    out: OutOption = Path("dist"),
    only: OnlyOption = None,
    html_only: Annotated[bool, typer.Option("--html-only", help="Skip the PDF step.")] = False,
    no_guides: Annotated[
        bool, typer.Option("--no-guides", help="Skip the control-guide compendium.")
    ] = False,
) -> None:
    """Render documents, the SoA, the scope statement and the registers to HTML and PDF."""
    repo = _load_valid(_resolve_root(root))
    if not html_only and not PDF_AVAILABLE:
        typer.echo("PDF rendering needs the 'pdf' extra: uv sync --extra pdf", err=True)
        raise typer.Exit(code=1)
    results = render_all(
        repo, out, set(only) if only else None, pdf=not html_only, include_guides=not no_guides
    )
    for result in results:
        typer.echo(f"  rendered {result.stem} ({'html+pdf' if result.pdf_path else 'html'})")
    typer.echo(f"rendered {len(results)} pages into {out}")


P12Option = Annotated[
    Path | None,
    typer.Option(
        "--p12", help="PKCS#12 signing key (default: ISMS_SIGNING_P12 or an ephemeral dev key)."
    ),
]


def _require_signing() -> None:
    if not SIGNING_AVAILABLE:
        typer.echo("signing needs the 'pdf' extra: uv sync --extra pdf", err=True)
        raise typer.Exit(code=1)


def _echo_signatures(reports: list[object]) -> None:
    for report in reports:
        typer.echo(f"  {report.summary()}")  # type: ignore[attr-defined]


@app.command()
def sign(root: RootOption = None, out: OutOption = Path("dist"), p12: P12Option = None) -> None:
    """Apply PAdES signatures to the rendered PDFs under OUT/pdf and write the public certificate."""
    _require_signing()
    repo = _load(_resolve_root(root))
    material = load_key_material(p12)
    if material.ephemeral:
        typer.echo(
            "no signing key configured: signing with an EPHEMERAL, UNTRUSTED development key",
            err=True,
        )
    reports = sign_outputs(repo, out, material)
    _echo_signatures(list(reports))
    typer.echo(
        f"signed {sum(1 for r in reports if r.ok)}/{len(reports)} PDFs; certificate written to {out / CERT_NAME}"
    )
    if not all(r.ok for r in reports):
        raise typer.Exit(code=1)


@app.command()
def verify(
    out: OutOption = Path("dist"),
    trust: Annotated[
        Path | None,
        typer.Option(
            "--trust", help="PEM certificate to anchor trust (default: OUT/signing-cert.pem)."
        ),
    ] = None,
) -> None:
    """Verify the signatures of the PDFs under OUT/pdf and the SHA256SUMS manifest."""
    _require_signing()
    reports, problems = verify_outputs(out, trust.read_bytes() if trust else None)
    _echo_signatures(list(reports))
    for problem in problems:
        typer.echo(f"  MANIFEST {problem}")
    good = sum(1 for r in reports if r.ok)
    typer.echo(
        f"{good}/{len(reports)} signatures valid; manifest {'intact' if not problems else 'BROKEN'}"
    )
    if good != len(reports) or problems or not reports:
        raise typer.Exit(code=1)


@app.command()
def build(
    root: RootOption = None,
    out: OutOption = Path("dist"),
    p12: P12Option = None,
    no_guides: Annotated[
        bool, typer.Option("--no-guides", help="Skip the control-guide compendium.")
    ] = False,
) -> None:
    """validate -> generate -> render -> sign -> manifest -> verify, in one go."""
    _require_signing()
    if not PDF_AVAILABLE:
        typer.echo("PDF rendering needs the 'pdf' extra: uv sync --extra pdf", err=True)
        raise typer.Exit(code=1)
    repo = _load_valid(_resolve_root(root))
    material = load_key_material(p12)
    if material.ephemeral:
        typer.echo(
            "no signing key configured: signing with an EPHEMERAL, UNTRUSTED development key",
            err=True,
        )
    report = run_build(repo, out, material, include_guides=not no_guides)
    typer.echo(
        f"generated {len(report.generated)} artefacts, rendered {len(report.rendered)} pages"
    )
    _echo_signatures(list(report.signatures))
    for problem in report.manifest_problems:
        typer.echo(f"  MANIFEST {problem}")
    typer.echo(f"build {'OK' if report.ok else 'FAILED'}: {out}")
    if not report.ok:
        raise typer.Exit(code=1)


@app.command()
def keygen(
    out: Annotated[Path, typer.Option("--out", help="Directory for the key files.")] = Path(
        ".local/signing"
    ),
    common_name: Annotated[str, typer.Option("--common-name")] = "ISMS Document Control",
    organisation: Annotated[str, typer.Option("--organisation")] = "PaketPort Group",
    days: Annotated[int, typer.Option("--days", help="Validity in days.")] = 3650,
    passphrase: Annotated[
        str | None, typer.Option("--passphrase", envvar="ISMS_SIGNING_PASSPHRASE")
    ] = None,
) -> None:
    """Create a PKCS#12 signing key for real deployments (store it as a CI secret, never commit it)."""
    if not passphrase:
        typer.echo("set --passphrase or ISMS_SIGNING_PASSPHRASE", err=True)
        raise typer.Exit(code=2)
    if common_name == DEV_COMMON_NAME:
        typer.echo("choose a real common name", err=True)
        raise typer.Exit(code=2)
    material = generate_key_material(common_name, organisation, days)
    out.mkdir(parents=True, exist_ok=True)
    p12_path = out / "isms-signing.p12"
    p12_path.write_bytes(to_pkcs12(material, passphrase))
    cert_path = out / "isms-signing-trust-anchor.pem"
    cert_path.write_bytes(material.trust_anchor_pem)
    typer.echo(
        f"wrote {p12_path} (keep secret) and {cert_path} (public trust anchor, commit under certs/)"
    )
    typer.echo(
        "CI secret: base64 -w0 "
        + str(p12_path)
        + "  ->  ISMS_SIGNING_P12; passphrase -> ISMS_SIGNING_PASSPHRASE"
    )


@app.command()
def new(
    doc_type: Annotated[str, typer.Argument(help="policy, standard or procedure")],
    doc_id: Annotated[str, typer.Option("--id", help="Document id, e.g. POL-XYZ")],
    title: Annotated[str, typer.Option("--title")],
    owner: Annotated[str, typer.Option("--owner", help="Owner role key")],
    approver: Annotated[str, typer.Option("--approver", help="Approver role key")],
    control: Annotated[
        list[str] | None, typer.Option("--control", help="Annex A control id (repeatable)")
    ] = None,
    root: RootOption = None,
) -> None:
    """Scaffold a new draft document from the templates."""
    repo_root = _resolve_root(root)
    try:
        folder = scaffold_document(
            repo_root,
            doc_type,
            doc_id,
            title,
            owner,
            approver,
            control or [],
            default_clock().today(),
        )
    except (ValueError, FileExistsError) as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=2) from None
    typer.echo(
        f"created {folder.relative_to(repo_root).as_posix()} (draft 0.1.0) — now write the body and run `isms validate`"
    )


@app.command("changelog-check")
def changelog_check(
    base: Annotated[
        str, typer.Option("--base", help="Git revision to compare against, e.g. origin/main.")
    ],
    root: RootOption = None,
) -> None:
    """Fail if a document changed since BASE without a CHANGELOG entry and a version bump."""
    repo_root = _resolve_root(root)
    try:
        problems = check_changelogs(repo_root, base)
    except RuntimeError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=2) from None
    for problem in problems:
        typer.echo(f"  ERROR   {problem}")
    if problems:
        typer.echo(f"{len(problems)} document(s) need a CHANGELOG entry and a version bump")
        raise typer.Exit(code=1)
    typer.echo(f"all documents changed since {base} carry a CHANGELOG entry and a version bump")


@app.command()
def version() -> None:
    """Print the toolkit version."""
    typer.echo(__version__)


def main() -> None:
    app()


if __name__ == "__main__":  # pragma: no cover
    main()
