---
control: A.5.26
applicability: applicable
justification: 'Treats R-002 and R-011: controlled containment, eradication and recovery limit the damage
  to the service and the data and are the substance of NIS2 Art. 21(2)(b).'
implementation_status: implemented
implemented_by:
- POL-IR
- PROC-IR
owner: isms-manager
risks:
- R-002
evidence:
- description: Incident tickets with containment, eradication and recovery steps and approvals
  location: Ticket system, project INC
  frequency: on-event
- description: Post-incident reviews
  location: Ticket system, project INC
  frequency: on-event
metrics:
- Mean time to contain S1 and S2 incidents (target ≤ 4 hours)
- Incidents closed with all reporting obligations met (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.26 — Response to information security incidents

## Objective

Handle incidents to a plan — contain without destroying evidence, eradicate the cause, recover safely and decide deliberately when to touch the service.

## Implementation

- POL-IR IR-9 (incident manager, playbooks, service-affecting decisions) and IR-11 (communication approvals).
- PROC-IR stage 4: isolation through the fleet-management plane, credential and key rotation, restore under POL-BC, staged re-enablement; security controls stay on during recovery (POL-BC BC-3).

## Evidence

- Incident tickets with containment, eradication and recovery steps and approvals — Ticket system, project INC.
- Post-incident reviews — Ticket system, project INC.

## Metrics

- Mean time to contain S1 and S2 incidents (target ≤ 4 hours)
- Incidents closed with all reporting obligations met (target 100 %)

## Common pitfalls

- Wiping a locker controller before imaging it — PROC-IR stage 5 preserves evidence first.
- Declaring closure before the indicators are gone — recovery ends only after verification.
