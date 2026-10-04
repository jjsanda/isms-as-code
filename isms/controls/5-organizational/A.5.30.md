---
control: A.5.30
applicability: applicable
justification: 'Treats R-003 and R-011: customers must collect parcels and carriers must hand over even
  when the backend fails; NIS2 Art. 21(2)(c) requires business continuity and disaster recovery.'
implementation_status: implemented
implemented_by:
- POL-BC
owner: head-of-platform
risks:
- R-003
- R-011
evidence:
- description: Business impact analysis with RTO and RPO per service
  location: Runbook repository; POL-BC BC-1
  frequency: annual
- description: Fail-over exercise records measured against RTO and RPO
  location: Ticket system, project ISMS-EXERCISE
  frequency: semi-annual
- description: Runbooks versioned in the repository
  location: Runbook repository
  frequency: on-event
metrics:
- Fail-over exercises meeting RTO and RPO (target 2 of 2 per year)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.30 — ICT readiness for business continuity

## Objective

Be able to keep the locker service running and to restore the platform within agreed targets — lockers buffering offline for 72 hours, backend fail-over within four hours — and prove it by exercise.

## Implementation

- POL-BC BC-1 (impact analysis and targets), BC-2 (plans), BC-6 to BC-8 (multi-zone plus secondary region, twice-yearly exercises including one unannounced, runbooks, reviews).
- Redundancy under BC-13; crisis invocation under BC-14; capacity reserves under POL-LOG LOG-10.

## Evidence

- Business impact analysis with RTO and RPO per service — Runbook repository; POL-BC BC-1.
- Fail-over exercise records measured against RTO and RPO — Ticket system, project ISMS-EXERCISE.
- Runbooks versioned in the repository — Runbook repository.

## Metrics

- Fail-over exercises meeting RTO and RPO (target 2 of 2 per year)

## Common pitfalls

- Fail-over that has never been tried unannounced — one exercise a year is unannounced.
- RTOs set without the capacity to meet them — BC-7 requires reserves in the secondary region.
