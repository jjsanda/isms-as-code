---
control: A.8.4
applicability: applicable
justification: Firmware and backend source code is confidential and the route to the fleet; write access
  through reviewed pull requests, protected release branches and restricted signing rights prevent unauthorised
  changes (supports R-009 and R-001).
implementation_status: implemented
implemented_by:
- POL-SDLC
owner: software-engineering-lead
risks: []
evidence:
- description: Repository permission and branch protection configuration
  location: Source control platform
  frequency: continuous
- description: Semi-annual review of repository access
  location: Ticket system, project ISMS-AR
  frequency: semi-annual
metrics:
- Direct pushes to protected branches (target 0)
- Repository access reviews completed on time (target 100 %)
entity_overrides:
  ENT-DE:
    applicability: not-applicable
    justification: PaketPort Deutschland GmbH performs no software development; the control is met for
      the group by PaketPort Systems GmbH and PaketPort Software s.r.o.
last_assessed: 2026-06-15
---

# A.8.4 — Access to source code

## Objective

Protect the source code and build definitions of the locker firmware, the backend and the app from unauthorised reading and — above all — unauthorised change.

## Implementation

- POL-SDLC SDLC-12 (read and write rules, protected branches, signed commits and tags, release rights per POL-ACC ACC-16) and SDLC-11 (pipeline-only deployments); segregation under POL-ORG ORG-7; reviews under POL-ACC ACC-7.
- Not applicable at PaketPort Deutschland GmbH, which performs no development; the control is met for the group by the Austrian and Czech entities.

## Evidence

- Repository permission and branch protection configuration — Source control platform.
- Semi-annual review of repository access — Ticket system, project ISMS-AR.

## Metrics

- Direct pushes to protected branches (target 0)
- Repository access reviews completed on time (target 100 %)

## Common pitfalls

- Bots and integrations with broad write tokens — service accounts scoped per repository and rotated (STD-AUTH AUTH-3).
- Forks or copies outside the platform — the source control platform is the only approved location.
