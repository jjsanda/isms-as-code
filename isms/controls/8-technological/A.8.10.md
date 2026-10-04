---
control: A.8.10
applicability: applicable
justification: GDPR storage limitation (LEG-02) and the records schedule require deletion when the purpose
  ends; decommissioned lockers and cloud storage must not keep data behind (supports R-009).
implementation_status: implemented
implemented_by:
- POL-CLS
owner: dpo
risks: []
evidence:
- description: Retention and deletion configuration of data stores
  location: Platform configuration
  frequency: annual
- description: Deletion records for personal data
  location: DPO records; ticket system, project DSR
  frequency: on-event
- description: Locker wipe records at decommissioning
  location: Fleet-management plane
  frequency: on-event
metrics:
- Data stores with automated retention-based deletion (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.10 — Information deletion

## Objective

Delete information — in data stores, cloud storage, backups, devices and lockers — when it is no longer needed or allowed, in a way that is verifiable.

## Implementation

- POL-CLS CLS-11 (schedule-driven deletion, cloud deletion guarantees, device and locker wiping, DPO records); POL-LEG LEG-6 (schedule) and LEG-12 (erasure requests); POL-PHY PHY-19 (disposal); backup retention under POL-BC BC-10.

## Evidence

- Retention and deletion configuration of data stores — Platform configuration.
- Deletion records for personal data — DPO records; ticket system, project DSR.
- Locker wipe records at decommissioning — Fleet-management plane.

## Metrics

- Data stores with automated retention-based deletion (target 100 %)

## Common pitfalls

- Deleting from the database but not from backups and exports — retention applies to every copy.
- Manual deletion scripts — retention is automated and logged.
