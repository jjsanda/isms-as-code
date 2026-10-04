---
control: A.5.5
applicability: applicable
justification: NIS2 registration and incident reporting (LEG-01, IP-04) depend on current contacts with
  the competent authority and CSIRT in each country; treats R-012.
implementation_status: implemented
implemented_by:
- POL-ORG
- PROC-IR
owner: isms-manager
risks:
- R-012
evidence:
- description: Authority contact list per entity with verification dates
  location: Legal register; ticket system, project ISMS-CONTACTS
  frequency: semi-annual
- description: Registration confirmations from the competent authorities
  location: ISMS records area
  frequency: on-event
- description: Reporting log of incidents reported to authorities
  location: Ticket system, project INC
  frequency: on-event
metrics:
- Authority contacts verified within the last six months (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.5 — Contact with authorities

## Objective

Know whom to call — and be known to — the NIS2 authorities and CSIRTs, the data protection authorities and the police in Austria, Germany and Czechia before an incident forces the question.

## Implementation

- POL-ORG ORG-9 assigns contact ownership per entity (ISMS Manager for Austria and the group, the entity leads for Germany and Czechia) and requires semi-annual verification; ORG-10 limits who speaks to authorities.
- PROC-IR stage 6 lists every reporting obligation with deadline, content and reporter; the reporting log records each contact.
- Registrations are tracked in the legal register (POL-LEG LEG-3) and confirmed at the management review.

## Evidence

- Authority contact list per entity with verification dates — Legal register; ticket system, project ISMS-CONTACTS.
- Registration confirmations from the competent authorities — ISMS records area.
- Reporting log of incidents reported to authorities — Ticket system, project INC.

## Metrics

- Authority contacts verified within the last six months (target 100 %)

## Common pitfalls

- Contacts kept in one person's address book — the legal register and the contacts project make them shared and verified.
- Several people contacting an authority with conflicting information — ORG-10 and the reporting log keep a single voice.
