---
control: A.7.13
applicability: applicable
justification: Maintenance is when equipment is opened and technicians — including subcontractors — have
  their hands on controllers; authorised, recorded maintenance keeps integrity and evidence (supports
  R-001).
implementation_status: implemented
implemented_by:
- POL-PHY
owner: facilities-lead
risks: []
evidence:
- description: Maintenance records for lockers with work order, parts and technician
  location: Fleet-management plane
  frequency: on-event
- description: Maintenance records for servers and network equipment
  location: Change log
  frequency: on-event
metrics:
- Maintenance actions without a work order (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.7.13 — Equipment maintenance

## Objective

Keep equipment working and secure through maintenance done by authorised people, on schedule, recorded — and without exposing data or keys when equipment leaves a site.

## Implementation

- POL-PHY PHY-18 (manufacturer schedule, authorised technicians, records in the change log and the fleet plane, wiping before repair); PHY-5 authorises each locker visit; POL-SUP SUP-10 for subcontractors; POL-CLS CLS-10 for storage removed before repair.

## Evidence

- Maintenance records for lockers with work order, parts and technician — Fleet-management plane.
- Maintenance records for servers and network equipment — Change log.

## Metrics

- Maintenance actions without a work order (target 0)

## Common pitfalls

- Repairs shipped with data on board — storage is wiped or removed first.
- Maintenance recorded on paper in vehicles — the tablet records it in the fleet plane.
