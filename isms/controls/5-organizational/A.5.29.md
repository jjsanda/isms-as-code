---
control: A.5.29
applicability: applicable
justification: 'Treats R-003: recovery under pressure is when controls get switched off; keeping access
  control, logging and encryption in force during disruption prevents a second incident.'
implementation_status: implemented
implemented_by:
- POL-BC
owner: head-of-platform
risks:
- R-003
evidence:
- description: Continuity plans with security requirements for recovery environments
  location: Runbook repository
  frequency: annual
- description: Exercise records noting security deviations and their closure
  location: Ticket system, project ISMS-EXERCISE
  frequency: semi-annual
metrics:
- Security deviations accepted during exercises or incidents closed within ten working days (target 100
  %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.29 — Information security during disruption

## Objective

Keep PaketPort's security level intact while it recovers from disruption — in the secondary region, on restored systems, in temporary workplaces and on lockers running offline.

## Implementation

- POL-BC BC-3 (controls remain in force, break-glass only), BC-4 (recovery environments meet the baselines, deviations closed within ten working days) and BC-5 (lockers keep local security functions offline).
- PROC-IR stage 4 applies the same rules to incident recovery.

## Evidence

- Continuity plans with security requirements for recovery environments — Runbook repository.
- Exercise records noting security deviations and their closure — Ticket system, project ISMS-EXERCISE.

## Metrics

- Security deviations accepted during exercises or incidents closed within ten working days (target 100 %)

## Common pitfalls

- Shared emergency credentials handed out in a crisis — only break-glass accounts under POL-ACC ACC-13.
- A secondary region built once and never re-baselined — drift monitoring under POL-VULN covers both regions.
