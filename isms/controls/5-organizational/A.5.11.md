---
control: A.5.11
applicability: applicable
justification: Leavers and technicians hold laptops, tablets, locker keys and master keys; unreturned
  assets are a direct path into lockers and systems (supports R-004 and R-001).
implementation_status: implemented
implemented_by:
- POL-CLS
owner: it-operations-lead
risks: []
evidence:
- description: Leaver asset return records
  location: Inventory; ticket system, queue ACCESS
  frequency: on-event
- description: Key register sign-out and sign-in entries
  location: Key register at the Vienna depot and the Munich store
  frequency: daily
metrics:
- Leavers with all assets returned by the last working day (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.11 — Return of assets

## Objective

Get every device, key, tool and document back when someone leaves or changes role — above all the locker master keys — and know immediately when something is missing.

## Implementation

- POL-CLS CLS-4 states the rule; PROC-JML stage 3.3 (in draft) is the checklist with the line manager's confirmation and the key check by the Facilities & Physical Security Lead.
- Missing items are incidents under POL-IR; subcontractor equipment is confirmed by the Country Manager Germany within one working day (PROC-JML 3.5).

## Evidence

- Leaver asset return records — Inventory; ticket system, queue ACCESS.
- Key register sign-out and sign-in entries — Key register at the Vienna depot and the Munich store.

## Metrics

- Leavers with all assets returned by the last working day (target 100 %)

## Common pitfalls

- Keys not tracked individually — the key register records every master key movement.
- Contractors offboarded by their employer but not by PaketPort — the sponsor confirms removal and return.
