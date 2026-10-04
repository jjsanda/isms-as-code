# ADR 0002 — Semantic versioning and a CHANGELOG per document

- **Status:** Accepted
- **Date:** 2026-08

## Context

Document control (ISO/IEC 27001 clause 7.5) needs version identification, a record of changes and
re-approval where the content changes materially. Date-based versions ("v2024-03") say nothing
about the size of a change; free-text revision tables inside the document drift from the version
field; and a repository-level changelog cannot be read per document.

## Decision

Each document carries a **semantic version** in its front matter and a **Keep-a-Changelog file**
next to it. MAJOR = obligations added, removed or changed (re-approval by the approver role and
communication before the effective date); MINOR = clarifications and additions that change no
obligation; PATCH = editorial changes and periodic reviews without change. The newest CHANGELOG
heading **is** the current version and its date is the approval date; `last_reviewed` must equal
it and `effective_date` may not precede it. There is no "Unreleased" section: every merged change
to a controlled document is an approved version. `isms validate` enforces the invariants;
`isms changelog-check` fails a pull request that changes a document without an entry and a bump.

## Consequences

- **The version tells the reader what happened.** A jump from 1.3.0 to 2.0.0 means new duties and
  triggers communication and training; 1.3.1 means nothing changed for them.
- **Revision history in the PDF is generated** from the CHANGELOG, never typed.
- **Periodic reviews leave a trace** as PATCH versions instead of a note in a spreadsheet.
- **Trade-off.** Many small versions accumulate, and authors must learn the bump rules. The
  PR template, the validator and the `bump_kind` check make the rule mechanical.
