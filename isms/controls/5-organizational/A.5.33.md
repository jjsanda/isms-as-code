---
control: A.5.33
applicability: applicable
justification: Handover records, financial records, ISMS records and incident reports have statutory retention
  and must stay intact and retrievable (LEG-02 accountability, certification, NIS2 evidence).
implementation_status: implemented
implemented_by:
- POL-LEG
owner: dpo
risks: []
evidence:
- description: Records schedule
  location: POL-LEG LEG-6
  frequency: annual
- description: Retention and deletion configuration of data stores and the log archive
  location: Platform and log store configuration
  frequency: annual
- description: Legal hold records
  location: Ticket system, project ISMS-LEGAL
  frequency: on-event
metrics:
- Record types with technically enforced retention (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.33 — Protection of records

## Objective

Keep the records PaketPort must keep — for as long as required, protected against loss and tampering — and dispose of them when the period ends.

## Implementation

- POL-LEG LEG-6 (the schedule) and LEG-7 (protection, disposal, legal hold); integrity through POL-LOG LOG-4 and POL-BC backups; access through POL-ACC and POL-CLS; deletion under POL-CLS CLS-11.
- This repository's version history is the ISMS record for documents (PROC-DOC records table).

## Evidence

- Records schedule — POL-LEG LEG-6.
- Retention and deletion configuration of data stores and the log archive — Platform and log store configuration.
- Legal hold records — Ticket system, project ISMS-LEGAL.

## Metrics

- Record types with technically enforced retention (target 100 %)

## Common pitfalls

- Retention defined in a policy but not in the systems — retention is configured in the data stores and checked.
- Keeping everything forever — the schedule sets maxima as well as minima.
