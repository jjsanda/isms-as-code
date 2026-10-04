---
control: A.7.7
applicability: applicable
justification: Printed manifests, credentials on notes and unlocked screens in offices, the depot and
  vehicles are easy wins for an intruder or a visitor; the rule is simple and checkable.
implementation_status: implemented
implemented_by:
- POL-AUP
owner: it-operations-lead
risks: []
evidence:
- description: Screen lock configuration on managed devices
  location: Endpoint management
  frequency: continuous
- description: Clear desk spot checks
  location: Ticket system, project ISMS-CAPA
  frequency: quarterly
metrics:
- Devices with the five-minute screen lock enforced (target 100 %)
- Clear desk spot check findings per quarter (target ≤ 2)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.7.7 — Clear desk and clear screen

## Objective

Keep confidential information off desks, printers, screens and vehicle seats when nobody is attending to it.

## Implementation

- POL-AUP AUP-7 (lock screens, lock away paper and media, collect printouts, shredding bins) enforced by the five-minute screen lock of AUP-4; spot checks under PROC-CAPA; vehicles under POL-PHY PHY-14 and, once approved, POL-REM REM-8.

## Evidence

- Screen lock configuration on managed devices — Endpoint management.
- Clear desk spot checks — Ticket system, project ISMS-CAPA.

## Metrics

- Devices with the five-minute screen lock enforced (target 100 %)
- Clear desk spot check findings per quarter (target ≤ 2)

## Common pitfalls

- Screen lock set long for convenience — it is enforced centrally at five minutes.
- Depot work benches excluded — the rule covers the depot's open areas explicitly.
