---
control: A.5.25
applicability: applicable
justification: 'Treats R-002: the significance test and the awareness time decide whether the 24-hour
  NIS2 clock is running; fast, recorded triage is the difference between compliance and a missed deadline.'
implementation_status: implemented
implemented_by:
- POL-IR
- PROC-IR
owner: isms-manager
risks:
- R-002
evidence:
- description: Triage records with severity, significance and personal-data tests
  location: Ticket system, project INC
  frequency: on-event
- description: Triage time statistics
  location: Incident dashboard; quarterly steering committee pack
  frequency: quarterly
metrics:
- Suspected S1 events triaged within 30 minutes (target 100 %)
- Incidents with a recorded significance test (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.25 — Assessment and decision on information security events

## Objective

Decide quickly and consistently whether an event is an incident, how severe it is, whether it is significant under NIS2 and whether personal data is involved — and record when PaketPort became aware.

## Implementation

- POL-IR IR-1 (definitions), IR-2 (severity table) and IR-8 (triage deadlines and decision record); PROC-IR stage 2 runs the two tests with the Data Protection Officer.
- A 'not yet determinable' significance is re-assessed every four hours (PROC-IR 6.2); in doubt, the early warning is sent.

## Evidence

- Triage records with severity, significance and personal-data tests — Ticket system, project INC.
- Triage time statistics — Incident dashboard; quarterly steering committee pack.

## Metrics

- Suspected S1 events triaged within 30 minutes (target 100 %)
- Incidents with a recorded significance test (target 100 %)

## Common pitfalls

- Waiting for certainty before starting the clock — the clock starts at awareness.
- Severity set once and never revisited — IR-2 requires re-assessment during handling.
