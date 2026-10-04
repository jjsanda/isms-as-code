---
control: A.5.2
applicability: applicable
justification: Clause 5.3 and NIS2 Art. 20 (LEG-01) require assigned and communicated responsibilities;
  with three entities and a two-person security function, explicit role ownership is what keeps the ISMS
  operating (supports R-012 and R-013).
implementation_status: implemented
implemented_by:
- POL-ORG
owner: isms-manager
risks: []
evidence:
- description: Role register with holders, deputies and review handles
  location: isms/context/roles.yaml
  frequency: on-event
- description: Owner and approver of every document and control
  location: Front matter; generated CODEOWNERS; document register
  frequency: on-event
- description: Security Steering Committee minutes with attendance
  location: Ticket system, project ISMS-MR
  frequency: quarterly
metrics:
- Documents, controls, risks and systems without a valid owner role (target 0, checked by `isms validate`)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.2 — Information security roles and responsibilities

## Objective

Make sure that every security task has a named role behind it — the Managing Director's accountability, the ISMS Manager's mandate, the heads of function, the entity leads in Munich and Brno — and that those responsibilities are written down and known.

## Implementation

- POL-ORG ORG-1 to ORG-6 define the governance structure, the Security Steering Committee and the entity-level responsibilities of the Country Manager Germany and the Site Lead Brno.
- The role register is the single source of role titles, holders and deputies; documents, controls, risks and systems reference role keys, never people.
- CODEOWNERS is generated from the ownership metadata, so pull-request review routing follows the documents (PROC-DOC stage 3); a change of holder is a one-line change in roles.yaml reviewed by the ISMS Manager.

## Evidence

- Role register with holders, deputies and review handles — isms/context/roles.yaml.
- Owner and approver of every document and control — Front matter; generated CODEOWNERS; document register.
- Security Steering Committee minutes with attendance — Ticket system, project ISMS-MR.

## Metrics

- Documents, controls, risks and systems without a valid owner role (target 0, checked by `isms validate`)

## Common pitfalls

- Responsibilities assigned to people rather than roles, which break at every departure — roles.yaml separates the role from its holder.
- Subsidiaries without a locally accountable person — the entity leads are explicit roles with deputies and duties under ORG-5.
