---
control: A.7.1
applicability: applicable
justification: 'Treats R-001: lockers stand on public streets and the depot holds controllers and keys;
  defined perimeters and zones make physical protection deliberate (site hosts IP-03).'
implementation_status: implemented
implemented_by:
- POL-PHY
owner: facilities-lead
risks:
- R-001
evidence:
- description: Zone plans per site
  location: Facilities documentation (confidential)
  frequency: annual
- description: Locker enclosure ratings and installation records
  location: Fleet-management plane; installation reports
  frequency: on-event
metrics:
- Sites with a current zone plan (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.7.1 — Physical security perimeters

## Objective

Define and build the physical boundaries — office, restricted rooms, the depot cage, the security operations centre and the locker enclosure — that keep unauthorised people away from equipment and information.

## Implementation

- POL-PHY PHY-1 (zone model with entry rules per zone) and PHY-2 (solid perimeters); locker enclosures are a field zone with sensor-backed boundaries (PHY-8, PHY-13); site surveys under PHY-10.

## Evidence

- Zone plans per site — Facilities documentation (confidential).
- Locker enclosure ratings and installation records — Fleet-management plane; installation reports.

## Metrics

- Sites with a current zone plan (target 100 %)

## Common pitfalls

- Zones defined on paper while server-room doors stand propped open — PHY-6 and the access log reviews.
- The locker enclosure treated as furniture — it is a security perimeter with a rating and sensors.
