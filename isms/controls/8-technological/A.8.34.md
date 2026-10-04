---
control: A.8.34
applicability: applicable
justification: Audits and penetration tests touch production and the fleet; read-only access, approved
  windows and confidential handling of audit data prevent the assurance activity from causing an incident.
implementation_status: implemented
implemented_by:
- PROC-AUDIT
owner: internal-audit-lead
risks: []
evidence:
- description: Approvals and windows for testing against production
  location: Ticket system, project ISMS-AUDIT
  frequency: on-event
- description: Audit account issue and removal records
  location: Identity provider; ticket system, queue ACCESS
  frequency: on-event
metrics:
- Audit or test activities against production without an approved window (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.34 — Protection of information systems during audit testing

## Objective

Let auditors and testers do their work without disrupting the locker service or exposing data — planned, approved, read-only where possible, and cleaned up afterwards.

## Implementation

- PROC-AUDIT stage 4.2 (read-only accounts, approval and windows by the Head of Platform & SRE, staging or lab for risky tests, confidential working papers, account removal); penetration tests under POL-SDLC SDLC-7 follow the same approvals; access under POL-ACC ACC-14.

## Evidence

- Approvals and windows for testing against production — Ticket system, project ISMS-AUDIT.
- Audit account issue and removal records — Identity provider; ticket system, queue ACCESS.

## Metrics

- Audit or test activities against production without an approved window (target 0)

## Common pitfalls

- Scanners pointed at the locker fleet during a roll-out — windows are agreed with the Head of Platform & SRE.
- Audit exports of personal data kept in auditors' mailboxes — samples are minimal and classified confidential.
