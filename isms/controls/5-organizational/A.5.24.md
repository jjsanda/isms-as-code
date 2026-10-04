---
control: A.5.24
applicability: applicable
justification: 'Treats R-002 and R-012: NIS2 Art. 21(2)(b) and Art. 23 (LEG-01) require a prepared incident
  process with a 24-hour early warning; preparation is what makes the deadlines achievable.'
implementation_status: implemented
implemented_by:
- POL-IR
- PROC-IR
owner: isms-manager
risks:
- R-002
- R-012
evidence:
- description: Playbooks, on-call rota and contact lists
  location: Incident response runbook repository; ticket system, project INC
  frequency: annual
- description: Tabletop exercise records
  location: Ticket system, project ISMS-EXERCISE
  frequency: semi-annual
- description: Incident tooling configuration (war room, forensic kit, out-of-band channel)
  location: Platform documentation
  frequency: annual
metrics:
- Tabletop exercises per year (target ≥ 2, one on the reporting clock)
- Playbooks reviewed within the last twelve months (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.24 — Information security incident management planning and preparation

## Objective

Have the roles, playbooks, tooling, contacts and practice in place before an incident, so that the response — and the reporting clock — starts within minutes rather than being improvised.

## Implementation

- POL-IR IR-3 to IR-5 define the capability, the exercises and the detection inputs; PROC-IR stages 1 to 9 are the procedure and stage 3 mobilises the team.
- Contacts come from the legal register (POL-ORG ORG-9); lessons update the playbooks (POL-IR IR-13).

## Evidence

- Playbooks, on-call rota and contact lists — Incident response runbook repository; ticket system, project INC.
- Tabletop exercise records — Ticket system, project ISMS-EXERCISE.
- Incident tooling configuration (war room, forensic kit, out-of-band channel) — Platform documentation.

## Metrics

- Tabletop exercises per year (target ≥ 2, one on the reporting clock)
- Playbooks reviewed within the last twelve months (target 100 %)

## Common pitfalls

- Playbooks that only the ISMS Manager knows — exercises involve the platform team and the German entity.
- No rehearsal of the reporting clock — one exercise a year drafts the early warning against the clock.
