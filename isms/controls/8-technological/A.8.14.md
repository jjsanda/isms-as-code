---
control: A.8.14
applicability: applicable
justification: 'Treats R-003 and R-011: single points of failure in the backend, the locker uplinks or
  the spare-parts supply would stop the service; redundancy underpins the recovery objectives.'
implementation_status: implemented
implemented_by:
- POL-BC
owner: head-of-platform
risks:
- R-003
evidence:
- description: Architecture documentation showing multi-zone and multi-region deployment
  location: Platform documentation
  frequency: annual
- description: Locker connectivity fall-back test results
  location: Brno lab test records; fleet-management plane
  frequency: on-event
- description: Spare-parts stock levels
  location: Inventory
  frequency: monthly
metrics:
- Production services with a single point of failure in the architecture review (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.14 — Redundancy of information processing facilities

## Objective

Remove single points of failure — in the cloud platform, the locker uplinks and local power, and the spare-parts supply — so that one failure does not stop deposits and collections.

## Implementation

- POL-BC BC-13 (no single point of failure in a region, redundant uplinks with cellular fall-back, local power for safe shutdown, spare parts at depot and store) and BC-6 (multi-zone plus secondary region); POL-PHY PHY-15 and PHY-16 for utilities.

## Evidence

- Architecture documentation showing multi-zone and multi-region deployment — Platform documentation.
- Locker connectivity fall-back test results — Brno lab test records; fleet-management plane.
- Spare-parts stock levels — Inventory.

## Metrics

- Production services with a single point of failure in the architecture review (target 0)

## Common pitfalls

- Redundancy in the cloud but one cellular provider for all lockers — dual providers or wired fall-back.
- Spare parts centralised in Vienna only — the Munich store holds critical parts.
