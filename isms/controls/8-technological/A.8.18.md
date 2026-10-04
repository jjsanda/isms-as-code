---
control: A.8.18
applicability: applicable
justification: 'Treats R-010: database consoles, fleet administration tools and system utilities can bypass
  application controls; restricting them to named roles through the bastion with session recording keeps
  them accountable.'
implementation_status: implemented
implemented_by:
- POL-ACC
owner: head-of-platform
risks:
- R-010
evidence:
- description: Bastion session recordings and access logs
  location: Bastion; central log store
  frequency: continuous
- description: List of privileged utilities and their authorised roles
  location: Platform documentation
  frequency: semi-annual
metrics:
- Privileged utility use outside the bastion or without a ticket (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.18 — Use of privileged utility programs

## Objective

Make sure the powerful tools — database clients, fleet administration commands, cloud command lines, system utilities — are used only by authorised roles, for a recorded reason, through a recorded channel.

## Implementation

- POL-ACC ACC-11 (named roles, bastion with session recording, change or incident ticket) and ACC-10 (just-in-time elevation); POL-VULN VULN-11 (no ad-hoc software on servers); segregation under POL-ORG ORG-7.

## Evidence

- Bastion session recordings and access logs — Bastion; central log store.
- List of privileged utilities and their authorised roles — Platform documentation.

## Metrics

- Privileged utility use outside the bastion or without a ticket (target 0)

## Common pitfalls

- Utilities installed on laptops with production credentials — production access only through the bastion.
- Recordings nobody reviews — quarterly privileged access reviews sample them.
