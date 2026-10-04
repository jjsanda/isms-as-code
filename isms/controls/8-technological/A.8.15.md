---
control: A.8.15
applicability: applicable
justification: 'Treats R-002, R-008 and R-010: detection, forensics and NIS2 reporting all depend on complete,
  tamper-evident logs; LEG-06 limits monitoring of staff and shapes what is logged.'
implementation_status: implemented
implemented_by:
- POL-LOG
owner: head-of-platform
risks:
- R-002
- R-008
- R-010
evidence:
- description: Log source coverage report (systems and lockers forwarding)
  location: Central log store
  frequency: monthly
- description: Log store integrity and access configuration
  location: Log store configuration; drift monitoring
  frequency: continuous
- description: Works-council agreement on monitoring (Germany)
  location: HR records
  frequency: annual
metrics:
- Systems and lockers forwarding logs to the central store (target 100 %)
- Lockers silent for more than 24 hours without an open ticket (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.15 — Logging

## Objective

Record the security-relevant events of every system and locker, completely and with synchronised time, in a central store that nobody can quietly alter.

## Implementation

- POL-LOG LOG-1 (categories), LOG-2 (content limits and privacy), LOG-3 (forwarding and locker buffering), LOG-4 (append-only store, separated administration, retention) and LOG-5 (staff privacy); time from LOG-9.

## Evidence

- Log source coverage report (systems and lockers forwarding) — Central log store.
- Log store integrity and access configuration — Log store configuration; drift monitoring.
- Works-council agreement on monitoring (Germany) — HR records.

## Metrics

- Systems and lockers forwarding logs to the central store (target 100 %)
- Lockers silent for more than 24 hours without an open ticket (target 0)

## Common pitfalls

- Logging everything, including secrets and full personal data — LOG-2 limits content.
- Log administrators who also run the systems — LOG-4 separates them (POL-ORG ORG-7).
