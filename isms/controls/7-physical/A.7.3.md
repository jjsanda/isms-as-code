---
control: A.7.3
applicability: applicable
justification: Server rooms, the key-handling room and the depot cage hold keys, controllers and forensic
  evidence; locked, unsignposted and purpose-limited rooms reduce opportunistic and targeted access (supports
  R-001 and R-010).
implementation_status: implemented
implemented_by:
- POL-PHY
owner: facilities-lead
risks: []
evidence:
- description: Key register and key safe logs
  location: Facilities records
  frequency: monthly
- description: Room access configuration
  location: Access control system
  frequency: annual
metrics:
- Master keys unaccounted for in the monthly key register check (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.7.3 — Securing offices, rooms and facilities

## Objective

Protect the rooms that matter — server and network rooms, the security operations centre, the depot's secure cage, the Brno key-handling room — by keeping them locked, unobtrusive and used only for their purpose.

## Implementation

- POL-PHY PHY-6 (locked, unsignposted, purpose-limited, key register), PHY-11 (working rules in secure areas) and PHY-12 (equipment in locked racks).

## Evidence

- Key register and key safe logs — Facilities records.
- Room access configuration — Access control system.

## Metrics

- Master keys unaccounted for in the monthly key register check (target 0)

## Common pitfalls

- Keys cut for convenience — the key register tracks every key and master key.
- Storage rooms doubling as server rooms — PHY-6 limits contents to what the room exists for.
