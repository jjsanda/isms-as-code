---
control: A.7.9
applicability: applicable
justification: Technician laptops, tablets, tools, spare parts and locker units are outside PaketPort
  premises every day; loss or theft of a tablet with maintenance access or a controller with keys is a
  direct risk (supports R-001 and R-004).
implementation_status: implemented
implemented_by:
- POL-PHY
owner: facilities-lead
risks: []
evidence:
- description: Loss and theft reports and response records
  location: Ticket system, project INC
  frequency: on-event
- description: Vehicle equipment rules and technician acknowledgement
  location: Training platform
  frequency: annual
- description: Handover records for units in transit
  location: Depot and store handover log
  frequency: on-event
metrics:
- Device losses reported within two hours (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.7.9 — Security of assets off-premises

## Objective

Protect PaketPort equipment and information wherever it is — in a vehicle, at a site, in transit, at home — to the same standard as on premises.

## Implementation

- POL-PHY PHY-14 (personal control, nothing left in vehicles overnight, tamper-evident transit with handover records); POL-AUP AUP-4 to AUP-6 for devices; POL-CLS CLS-9 for physical transfers.
- POL-REM REM-8 to REM-10 (in review) will add the field-service and travel specifics once approved.

## Evidence

- Loss and theft reports and response records — Ticket system, project INC.
- Vehicle equipment rules and technician acknowledgement — Training platform.
- Handover records for units in transit — Depot and store handover log.

## Metrics

- Device losses reported within two hours (target 100 %)

## Common pitfalls

- Spare controllers stored in technicians' garages — transit and storage rules send them back to the depot or the store.
- Losses reported the next morning — the two-hour rule and remote wipe.
