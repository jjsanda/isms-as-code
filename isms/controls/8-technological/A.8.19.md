---
control: A.8.19
applicability: applicable
justification: 'Treats R-007: unapproved or unsupported software on servers, lockers and endpoints is
  unpatched software; controlled installation keeps the estate known and patchable (NIS2 Art. 21(2)(g)).'
implementation_status: implemented
implemented_by:
- POL-AUP
- POL-VULN
owner: it-operations-lead
risks:
- R-007
evidence:
- description: Software catalogue and installation requests
  location: Endpoint management; ticket system
  frequency: on-event
- description: Pipeline and fleet-management records of software deployment
  location: Pipeline; fleet-management plane
  frequency: continuous
- description: End-of-life software register
  location: Risk register entries
  frequency: quarterly
metrics:
- Unapproved software found on endpoints and servers per month (target 0)
- End-of-life software without a replacement date (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.19 — Installation of software on operational systems

## Objective

Ensure that only approved, supported software reaches servers, lockers, network equipment and endpoints — through controlled channels, never by hand.

## Implementation

- POL-VULN VULN-11 (repositories, pipeline and fleet plane only; emergency changes) and VULN-12 (supported versions, end-of-life register); POL-AUP AUP-9 and AUP-10 (endpoint catalogue, no installs on servers); POL-SDLC SDLC-11 (pipeline deployments).

## Evidence

- Software catalogue and installation requests — Endpoint management; ticket system.
- Pipeline and fleet-management records of software deployment — Pipeline; fleet-management plane.
- End-of-life software register — Risk register entries.

## Metrics

- Unapproved software found on endpoints and servers per month (target 0)
- End-of-life software without a replacement date (target 0)

## Common pitfalls

- Developers installing tools on staging that drift into production — environments separated and baselined.
- Unsupported firmware generations kept running — VULN-6 support periods and decommissioning.
