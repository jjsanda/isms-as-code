---
control: A.5.37
applicability: applicable
justification: 'Treats R-013 (bus factor) and satisfies clause 7.5 and the certification body (IP-09,
  LEG-04): procedures and runbooks must be written, controlled and available to the people who operate
  the platform and the ISMS.'
implementation_status: implemented
implemented_by:
- PROC-DOC
owner: isms-manager
risks:
- R-013
evidence:
- description: Controlled procedures with versions and review dates
  location: Repository; generated document register
  frequency: on-event
- description: Operational runbooks versioned in the repository
  location: Runbook repository
  frequency: on-event
- description: CI results of validation and drift checks
  location: Pipeline
  frequency: continuous
metrics:
- Procedures and runbooks reviewed by their due date (target ≥ 95 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.37 — Documented operating procedures

## Objective

Make sure the operating knowledge of the ISMS and the platform — how to control documents, respond to incidents, fail over, provision a locker, review access — is written down, current, reviewed and available, not held in a few heads.

## Implementation

- PROC-DOC governs this repository: identification, review and approval through pull requests, versioning, publication as signed PDFs, periodic review and retirement (stages 1 to 9).
- Operational runbooks follow POL-BC BC-7; the document register lists everything; cross-training under the acceptance rationale of R-013.

## Evidence

- Controlled procedures with versions and review dates — Repository; generated document register.
- Operational runbooks versioned in the repository — Runbook repository.
- CI results of validation and drift checks — Pipeline.

## Metrics

- Procedures and runbooks reviewed by their due date (target ≥ 95 %)

## Common pitfalls

- Procedures in a document system nobody opens — the repository, the register and the signed releases make them findable.
- Runbooks that fail when needed — they are exercised under POL-BC BC-6.
