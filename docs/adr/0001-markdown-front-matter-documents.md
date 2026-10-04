# ADR 0001 — Markdown documents with YAML front matter as the controlled-document format

- **Status:** Accepted
- **Date:** 2026-08

## Context

ISMS documents are usually kept as Office files in a document management system or as pages in
a wiki or GRC tool. Those formats make three things hard: seeing exactly what changed between two
versions, proving who approved which version, and producing derived artefacts (the Statement of
Applicability, a document register) without re-typing. The group needed one document set for
three entities with an approval trail an auditor can follow without a demo licence.

## Decision

Every controlled document is a **folder with `README.md` and `CHANGELOG.md`**. The README opens
with **YAML front matter** (id, type, status, version, owner and approver *roles*, effective and
review dates, Annex A controls, clauses, applicability, related documents) validated by a Pydantic
model with `extra="forbid"`; the body is Markdown with a fixed set of sections per type. Control
implementation guides follow the same pattern, one file per Annex A control. Registers
(organisation, roles, risks, legal, interested parties, mappings) are YAML files.

## Consequences

- **Review is line by line.** A pull request shows the exact wording change, the version bump and
  the CHANGELOG entry together; the merge is the approval record.
- **GitHub renders it.** Front matter appears as a table, the folder README inline — no build
  needed to read a policy.
- **Derived artefacts are generated, not maintained.** The SoA, the scope statement, the
  registers and CODEOWNERS are computed from the same metadata, so they cannot disagree with the
  documents.
- **Trade-off.** Markdown has no track-changes view and no rich layout, and non-technical owners
  must use the pull-request interface. The templates, `isms new`, the validator's precise error
  messages and the web editor keep the barrier low; the signed PDF gives readers the familiar
  controlled-document look.
