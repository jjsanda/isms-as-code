---
control: A.7.12
applicability: applicable
justification: Exposed cabling at locker sites and in offices invites tapping and disruption; protected
  conduits and treating the locker uplink as untrusted limit the impact.
implementation_status: implemented
implemented_by:
- POL-PHY
owner: facilities-lead
risks: []
evidence:
- description: Cabling and patch documentation
  location: Facilities documentation (confidential)
  frequency: annual
- description: Locker installation reports confirming concealed cabling
  location: Installation records
  frequency: on-event
metrics:
- Cabling deviations found in site inspections (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.7.12 — Cabling security

## Objective

Protect power and network cabling from interception, interference and damage, in buildings and at locker sites.

## Implementation

- POL-PHY PHY-17 (conduits, separation, locked cabinets, concealed site cabling; the uplink treated as untrusted under POL-NET NET-5 with mutual TLS) and PHY-13 for conduits at lockers.

## Evidence

- Cabling and patch documentation — Facilities documentation (confidential).
- Locker installation reports confirming concealed cabling — Installation records.

## Metrics

- Cabling deviations found in site inspections (target 0)

## Common pitfalls

- Relying on cable protection for confidentiality — encryption under POL-CRYP is the real control; cabling protects availability.
- Patch panels open in shared building rooms — locked cabinets.
