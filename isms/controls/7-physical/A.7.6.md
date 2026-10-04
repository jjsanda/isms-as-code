---
control: A.7.6
applicability: applicable
justification: Work in server rooms and the key-handling room is where keys and evidence are exposed;
  two-person rules and recording limit insider and accidental risk (supports R-010).
implementation_status: implemented
implemented_by:
- POL-PHY
owner: facilities-lead
risks: []
evidence:
- description: Authorisations and records of work in restricted zones
  location: Ticket system; access logs
  frequency: on-event
metrics:
- Work sessions in restricted zones without authorisation or record (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.7.6 — Working in secure areas

## Objective

Make sure that work inside restricted zones is authorised, supervised where it matters, recorded, and leaves the area locked and alarmed.

## Implementation

- POL-PHY PHY-11: prior authorisation, two-person rule for the server room and the key-handling room, no photography or personal devices, locked and alarmed when unattended; dual control for the firmware root under POL-CRYP CRYP-7 is an instance.

## Evidence

- Authorisations and records of work in restricted zones — Ticket system; access logs.

## Metrics

- Work sessions in restricted zones without authorisation or record (target 0)

## Common pitfalls

- Rules relaxed for regular staff — the two-person rule applies to everyone.
- Unaccompanied vendor technicians — escort or camera supervision under PHY-4.
