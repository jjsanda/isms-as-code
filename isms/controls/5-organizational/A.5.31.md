---
control: A.5.31
applicability: applicable
justification: 'Treats R-012: NIS2 (LEG-01), the GDPR, the Cyber Resilience Act and the carrier contracts
  differ per entity and change; an owned, reviewed legal register is the only way to keep the ISMS aligned
  with them.'
implementation_status: implemented
implemented_by:
- POL-LEG
owner: isms-manager
risks:
- R-012
evidence:
- description: Legal register with owners, entities and verification notes
  location: isms/context/legal-register.yaml
  frequency: annual
- description: Management review confirmation of the register
  location: Management review minutes
  frequency: annual
- description: Counsel verification of national transpositions
  location: Ticket system, project ISMS-LEGAL
  frequency: annual
metrics:
- Legal register items verified within the last twelve months (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.31 — Legal, statutory, regulatory and contractual requirements

## Objective

Know every legal, regulatory and contractual requirement with an information security dimension for each entity, who owns it and how it is met — and keep that knowledge current as laws and contracts change.

## Implementation

- POL-LEG LEG-1 to LEG-3: the register, its confirmation and update triggers, and the NIS2 duties per entity.
- The register is data referenced by control guides and the scope statement; changes are reviewed through pull requests and confirmed annually at the management review (PROC-MR).

## Evidence

- Legal register with owners, entities and verification notes — isms/context/legal-register.yaml.
- Management review confirmation of the register — Management review minutes.
- Counsel verification of national transpositions — Ticket system, project ISMS-LEGAL.

## Metrics

- Legal register items verified within the last twelve months (target 100 %)

## Common pitfalls

- A legal register written once for the parent — the German and Czech entities have their own transpositions and authorities.
- Requirements without a link to controls — every register item names the controls and documents that meet it.
