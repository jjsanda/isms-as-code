---
control: A.7.8
applicability: applicable
justification: 'Treats R-001: how a locker is anchored, where its controller compartment faces and how
  its cables run decide how easy tampering is; the same applies to racks and screens in the offices.'
implementation_status: implemented
implemented_by:
- POL-PHY
owner: facilities-lead
risks:
- R-001
evidence:
- description: Installation standard and installation reports
  location: Fleet-management plane; installation records
  frequency: on-event
- description: Rack and room layout documentation
  location: Facilities documentation
  frequency: annual
metrics:
- Installations deviating from the installation standard found in inspections (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.7.8 — Equipment siting and protection

## Objective

Place and protect equipment so that it is hard to tamper with, overlook or damage — lockers anchored with controllers out of reach, racks locked, screens away from public view.

## Implementation

- POL-PHY PHY-12 (racks, environmental monitoring, screen positioning) and PHY-13 (locker anchoring, controller orientation, protected conduits, tamper-triggering enclosure); site survey under PHY-10.

## Evidence

- Installation standard and installation reports — Fleet-management plane; installation records.
- Rack and room layout documentation — Facilities documentation.

## Metrics

- Installations deviating from the installation standard found in inspections (target 0)

## Common pitfalls

- Installation quality varying between technicians and subcontractors — one installation standard and inspections.
- Controller compartments facing the street — PHY-13 requires them away from public reach.
