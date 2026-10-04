# ADR 0003 — Generated artefacts are committed and drift-checked

- **Status:** Accepted
- **Date:** 2026-08

## Context

The Statement of Applicability, the scope statement, the document and risk registers, the
coverage reports and CODEOWNERS are all derived from the sources. They could be produced only in
CI as build artefacts, or committed to the repository. People browsing GitHub — auditors,
colleagues, carriers — should see the SoA without running anything, and reviewers should see how
a change to a control guide changes the SoA.

## Decision

`isms generate` writes the artefacts under `generated/` (and `.github/CODEOWNERS`), **byte-
deterministically**: sorted iteration, canonical formatting, no timestamps — each file carries a
*source digest* (SHA-256 over the inputs) instead. The files are committed. CI runs
`isms generate --check`, which re-renders in memory and fails if any committed file differs.

## Consequences

- **The SoA diff is part of the review.** Marking a control partially implemented shows up as a
  one-line change in the generated SoA in the same pull request.
- **Always readable, always current** on the default branch; a stale SoA cannot be merged.
- **Reproducible.** Two runs on the same tree produce identical bytes; the digest changes only
  when an input changes.
- **Trade-off.** Generated files cause merge conflicts when two branches change sources; the
  resolution is always "regenerate", never hand-edit. The header of each file says so.
