# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html). (Each controlled document under
`isms/` has its own CHANGELOG; this file tracks the repository and the tooling.)

## [1.0.0] - 2026-08-20

### Added

- **Controlled document set** for the fictional PaketPort group: 18 policies, 2 standards and
  7 procedures as Markdown with validated front matter, stable statement ids and a CHANGELOG per
  document; one document in review, one draft and one retired to show the life cycle.
- **93 Annex A control implementation guides** with applicability, justification (risks, legal
  and interested-party references), implementing documents, owner role, evidence and metrics;
  entity-level overrides for the German subsidiary.
- **Registers:** ISO/IEC 27001:2022 Annex A catalogue with ISO/IEC 27002 attributes, organisation
  and scope (three entities, eight sites, services, systems, interfaces), roles, interested
  parties, legal register, risk criteria and a 13-risk register, NIS2 Art. 20/21/23 and
  ISO/IEC 27001 clause mappings.
- **`isms` CLI:** `validate`, `generate [--check]`, `soa`, `scope`, `register`, `review-due`,
  `changelog-check`, `new`, `render`, `sign`, `verify`, `build`, `keygen`.
- **Generators** (deterministic, committed, drift-checked): Statement of Applicability (group and
  per entity, Markdown + CSV), ISMS scope statement, document register with review calendar, risk
  register view with heat map, coverage reports, CODEOWNERS, badge JSON.
- **Rendering and signing:** HTML/PDF with cover, revision history, watermarks and "uncontrolled
  when printed" footer; PAdES signatures with a two-tier document-control key or an ephemeral
  development key; SHA-256 manifest; verification.
- **Governance:** PROC-DOC as the procedure the repository implements, PR template, issue forms,
  generated CODEOWNERS, CI (lint, type, test, content, build, security), signed releases with
  provenance attestation, weekly review-due issues, CodeQL.
- **Docs:** README, authoring guide, auditor guide, multi-entity
  guide, architecture, glossary, five ADRs, rendered diagrams and sample signed PDFs.
- **Quality gate:** ruff, black, `mypy --strict`, pytest with a 90 % coverage gate, `pip-audit`.

[1.0.0]: https://github.com/jjsanda/isms-as-code/releases/tag/v1.0.0
