---
control: A.5.8
applicability: applicable
justification: Locker roll-outs, carrier integrations and new entities are how risk enters PaketPort;
  security gates in projects prevent retrofitting controls (supports R-006 and R-009).
implementation_status: implemented
implemented_by:
- POL-ORG
owner: isms-manager
risks: []
evidence:
- description: Project security gate records at initiation and acceptance
  location: Project tickets with the gate checklist signed by the ISMS Manager
  frequency: on-event
- description: Risk assessments performed for projects
  location: Ticket system, project ISMS-RISK
  frequency: on-event
metrics:
- Projects that went live without a signed security acceptance (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.8 — Information security in project management

## Objective

Build security into every project — from a new locker generation to a new carrier API or a new site host — at the start, where it is cheap, rather than at go-live, where it is a surprise.

## Implementation

- POL-ORG ORG-12 defines the two gates, the project security contact and the ISMS Manager's sign-off.
- The initiation gate requires classification (POL-CLS) and a risk assessment (PROC-RISK stage 1 trigger); product projects additionally follow POL-SDLC SDLC-2 and SDLC-3, supplier projects POL-SUP SUP-2.

## Evidence

- Project security gate records at initiation and acceptance — Project tickets with the gate checklist signed by the ISMS Manager.
- Risk assessments performed for projects — Ticket system, project ISMS-RISK.

## Metrics

- Projects that went live without a signed security acceptance (target 0)

## Common pitfalls

- Gates applied only to IT projects — the Munich locker roll-out and a new site-host contract are projects too.
- A security contact named but never consulted — the acceptance gate needs the evidence filed, not just a signature.
