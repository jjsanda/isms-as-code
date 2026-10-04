---
control: A.7.2
applicability: applicable
justification: Badge-controlled entry, visitor management and per-visit locker authorisation keep people
  out of rooms and enclosures they have no business in (supports R-001 and R-010).
implementation_status: implemented
implemented_by:
- POL-PHY
owner: facilities-lead
risks: []
evidence:
- description: Badge access rights and quarterly restricted-zone reviews
  location: Access control system; ticket system, project ISMS-AR
  frequency: quarterly
- description: Visitor logs
  location: Reception system
  frequency: on-event
- description: Locker opening logs reconciled with work orders
  location: Fleet-management plane
  frequency: continuous
metrics:
- Restricted-zone access reviews completed on time (target 100 %)
- Unexplained locker openings without a matching work order (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.7.2 — Physical entry

## Objective

Ensure that only authorised people enter PaketPort's offices, restricted rooms and locker enclosures, that visitors are identified and escorted, and that every entry is recorded.

## Implementation

- POL-PHY PHY-3 (badges, reviews, removal through PROC-JML), PHY-4 (visitors) and PHY-5 (per-visit locker authorisation through the fleet-management plane and the tablet); logs go to the central store (POL-LOG LOG-1).

## Evidence

- Badge access rights and quarterly restricted-zone reviews — Access control system; ticket system, project ISMS-AR.
- Visitor logs — Reception system.
- Locker opening logs reconciled with work orders — Fleet-management plane.

## Metrics

- Restricted-zone access reviews completed on time (target 100 %)
- Unexplained locker openings without a matching work order (target 0)

## Common pitfalls

- Tailgating tolerated as politeness — PHY-3 prohibits it and the awareness training covers it.
- Technician badges that open any locker anywhere — per-visit authorisation ties openings to work orders.
