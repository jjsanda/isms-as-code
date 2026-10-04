# ADR 0005 — Ownership by role, review routing generated from it

- **Status:** Accepted
- **Date:** 2026-08

## Context

A.5.2 requires defined responsibilities; in practice documents name people, people leave, and the
"owner" field rots. Review routing in repositories (CODEOWNERS) is usually a hand-maintained file
that drifts from the documents it is supposed to protect.

## Decision

Documents and control guides name an **owner role and an approver role** from `roles.yaml`
(`isms-manager`, `head-of-platform`, `country-manager-de` …); the role register maps each role to
a title, a fictional current holder, a deputy and a GitHub handle or team. The approver must
differ from the owner. **`.github/CODEOWNERS` is generated** from this metadata, so a pull request
that touches a document is routed to exactly the roles that must review and approve it.

## Consequences

- **A change of holder is a one-line change in `roles.yaml`**, touching no controlled document.
- **Segregation of duties is enforced by data** (approver ≠ owner) and surfaced in the PR.
- **The role register doubles as the responsibility matrix** for clause 5.3.
- **Trade-off.** CODEOWNERS needs real handles or teams; in this portfolio repository every role
  resolves to the maintainer, which the generated file states in its header.
