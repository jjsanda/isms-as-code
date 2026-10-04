UV ?= uv

# Pin the PDF creation timestamp so `make build` is reproducible run-to-run (2026-08-20T00:00:00Z).
# Signing times are the one deliberate exception: a signature records when it was applied.
SOURCE_DATE_EPOCH ?= 1787184000
DIST ?= dist

.DEFAULT_GOAL := help
.PHONY: help setup fmt fmt-check lint lint-yaml lint-md type test test-cov security ci \
        validate generate generate-check review-due render sign verify build samples \
        diagrams keygen clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'

## ---------- Setup & quality gate ----------

setup: ## Install dependencies (dev + pdf extra) and pre-commit hooks
	$(UV) sync --dev --extra pdf
	$(UV) run pre-commit install || true

fmt: ## Auto-fix lint issues and format the code
	$(UV) run ruff check --fix .
	$(UV) run black .

fmt-check: ## Check formatting without modifying files
	$(UV) run black --check --diff .

lint: ## Lint with ruff
	$(UV) run ruff check .

lint-yaml: ## Lint YAML registers, workflows and configs
	$(UV) run yamllint -s .

lint-md: ## Lint Markdown (documents, docs, README) with markdownlint-cli2 (needs Node)
	npx -y markdownlint-cli2 "**/*.md" "#node_modules" "#.venv" "#dist"

type: ## Strict type-check with mypy
	$(UV) run mypy

test: ## Run the offline test suite
	$(UV) run pytest -q

test-cov: ## Run tests with coverage and enforce the 90% gate
	$(UV) run pytest --cov=isms_as_code --cov-report=term-missing --cov-fail-under=90

security: ## Audit Python dependencies for known vulnerabilities
	$(UV) run pip-audit || true

ci: fmt-check lint lint-yaml type test-cov security validate generate-check ## Run the full local gate (mirrors GitHub Actions)

## ---------- ISMS document lifecycle ----------

validate: ## Validate front matter, cross-references, CHANGELOGs and the control catalogue
	$(UV) run isms validate

generate: ## Regenerate generated/ (SoA, scope statement, registers, coverage, CODEOWNERS, badges)
	$(UV) run isms generate

generate-check: ## Fail if generated/ or CODEOWNERS are out of date with the sources
	$(UV) run isms generate --check

review-due: ## List documents whose review is due within 60 days (or overdue)
	$(UV) run isms review-due --within 60

render: ## Render every document, the SoA and the scope statement to HTML + PDF under dist/
	SOURCE_DATE_EPOCH=$(SOURCE_DATE_EPOCH) $(UV) run --extra pdf isms render --out $(DIST)

sign: ## Apply PAdES signatures to the rendered PDFs (CI key, or an ephemeral dev key)
	$(UV) run --extra pdf isms sign --out $(DIST)

verify: ## Verify the PDF signatures and the SHA256SUMS manifest
	$(UV) run --extra pdf isms verify --out $(DIST)

build: ## validate -> generate -> render -> sign -> manifest -> verify
	SOURCE_DATE_EPOCH=$(SOURCE_DATE_EPOCH) $(UV) run --extra pdf isms build --out $(DIST)

samples: build ## Refresh the committed sample PDFs and cover-page screenshots under docs/
	./scripts/refresh_samples.sh $(DIST)

keygen: ## Create a PKCS#12 signing key for real deployments (never commit the .p12)
	$(UV) run --extra pdf isms keygen --out .local/signing

## ---------- Docs & media (build-time; need node/network) ----------

diagrams: ## Render the Mermaid diagrams to SVG + PNG
	./scripts/render_diagrams.sh

clean: ## Remove caches, coverage and build artifacts
	rm -rf .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage coverage.xml $(DIST)
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
