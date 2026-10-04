---
control: A.5.32
applicability: applicable
justification: Firmware and backend embed open-source components with licence obligations, and PaketPort's
  own code is a core asset; licence compliance and IP protection are legal duties and part of the Cyber
  Resilience Act documentation (LEG-03).
implementation_status: implemented
implemented_by:
- POL-LEG
owner: isms-manager
risks: []
evidence:
- description: Open-source component inventory with licences
  location: Build pipeline artefacts (bills of materials)
  frequency: on-event
- description: Corporate software licence inventory
  location: Endpoint management; licence records
  frequency: annual
metrics:
- Components with incompatible licences found in release scans (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.32 — Intellectual property rights

## Objective

Use others' intellectual property lawfully — licensed software, open-source components with their obligations — and protect PaketPort's own code and designs.

## Implementation

- POL-LEG LEG-4 (licence inventories by the IT Operations Lead and the Software Engineering Lead, the open-source guideline, product attributions) and LEG-5 (protection of PaketPort's IP, contribution approvals).
- POL-SDLC SDLC-6 scans licences on every build; POL-AUP AUP-9 controls software installation.

## Evidence

- Open-source component inventory with licences — Build pipeline artefacts (bills of materials).
- Corporate software licence inventory — Endpoint management; licence records.

## Metrics

- Components with incompatible licences found in release scans (target 0)

## Common pitfalls

- Licence scanning only for vulnerabilities — the pipeline checks licences too.
- Developers publishing internal code — contributions require approval.
