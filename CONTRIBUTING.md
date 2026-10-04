# Contributing

This is a personal portfolio project, but it is built like a real one. If you want to run it,
adapt it for your organisation or extend the tooling, here is the workflow.

## Setup

```bash
make setup   # uv sync --dev --extra pdf, plus pre-commit hooks
```

Requires Python 3.12 and [`uv`](https://docs.astral.sh/uv/). WeasyPrint needs pango and harfbuzz
(present on most desktops; on Debian/Ubuntu `libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz-subset0`).
Node.js is only needed to re-render the Mermaid diagrams and to run markdownlint locally.

## The gate

Every change should pass the same gate CI runs:

```bash
make ci      # fmt-check + lint + lint-yaml + type + test-cov (90%) + security + validate + generate-check
```

Individual targets: `make fmt`, `make lint`, `make type`, `make test`, `make validate`,
`make generate`, `make build`. `make help` lists everything.

## Changing documents

- **Read [`docs/authoring-guide.md`](docs/authoring-guide.md)** — voice, structure, statement ids,
  front matter, versioning. PROC-DOC is the procedure behind it.
- **Branch naming:** `docs/<id>-<topic>` for document changes, `policy/<id>-<topic>` for new
  obligations, `feat/…`, `fix/…`, `ci/…` for tooling.
- **Every document change = CHANGELOG entry + version bump** (`isms changelog-check --base origin/main`
  tells you if you forgot). Update `last_reviewed`, `next_review` and, if the version takes
  effect later, `effective_date`.
- **Regenerate:** `make generate` and commit `generated/` and `.github/CODEOWNERS` with your change.
- **Review:** the owner role and the approver role of the document are requested automatically
  (generated CODEOWNERS). Approval is the approver's review plus the merge.
- **New document:** `uv run isms new policy --id POL-XYZ --title "…" --owner <role> --approver <role>`.

## Changing the tooling

- **Strict by default:** `mypy --strict`, ruff, black; pure, testable functions; tests mirror the
  source layout (`tests/unit`, `tests/generate`, `tests/render`, `tests/signing`, `tests/cli`,
  `tests/content`).
- **Determinism:** never call `datetime.now()` — use `isms_as_code.clock`; keep output sorted and
  JSON canonical so `isms generate` stays byte-reproducible.
- **Commits:** Conventional Commits (`feat(generate): …`, `docs(policy): …`, `fix:`, `ci:`, `chore:`).
- **Diagrams** are regenerated with `make diagrams`; the rendered PNG/SVG files are committed.

## Releasing

Tag `vX.Y.Z` on `main`. The release workflow builds, signs (with the CI key if configured,
otherwise with an ephemeral development key), attests provenance and publishes the PDFs,
`SHA256SUMS` and the trust anchor as release assets.
