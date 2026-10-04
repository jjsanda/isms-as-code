---
control: A.8.32
applicability: applicable
justification: Uncontrolled changes to production, the fleet or the ISMS cause outages and security gaps;
  typed changes with approval, testing, rollback and staged firmware roll-outs keep change safe (NIS2
  Art. 21(2)(e); clause 6.3).
implementation_status: implemented
implemented_by:
- POL-SDLC
owner: software-engineering-lead
risks: []
evidence:
- description: Change records with type, approval, test evidence and rollback plan
  location: Ticket system, project CHG
  frequency: on-event
- description: Staged roll-out statistics and halts
  location: Fleet-management plane
  frequency: on-event
- description: Retrospective reviews of emergency changes
  location: Ticket system, project CHG
  frequency: on-event
metrics:
- Production changes without a change record (target 0)
- Emergency changes reviewed within five working days (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.32 — Change management

## Objective

Make every change to production — code, infrastructure, configuration, firmware — deliberate: assessed, tested, approved, reversible and recorded, with firmware reaching the fleet in stages.

## Implementation

- POL-SDLC SDLC-9 (change types and approvals), SDLC-10 (staged OTA roll-out with automatic halt) and SDLC-11 (pipeline releases); baselines under POL-VULN VULN-8; changes to the ISMS's own documents follow PROC-DOC stage 4.

## Evidence

- Change records with type, approval, test evidence and rollback plan — Ticket system, project CHG.
- Staged roll-out statistics and halts — Fleet-management plane.
- Retrospective reviews of emergency changes — Ticket system, project CHG.

## Metrics

- Production changes without a change record (target 0)
- Emergency changes reviewed within five working days (target 100 %)

## Common pitfalls

- Emergency changes as the normal path — retrospective review and statistics to the steering committee.
- Fleet-wide roll-outs in one go — canary, 10 %, then the fleet, with automatic halt.
