---
control: A.8.9
applicability: applicable
justification: 'Treats R-001, R-007 and R-013: baselines as code make lockers, cloud and endpoints reproducibly
  secure and recoverable, and drift detection catches silent weakening (LEG-07 shared responsibility).'
implementation_status: implemented
implemented_by:
- POL-VULN
owner: security-engineer
risks:
- R-001
- R-007
- R-013
evidence:
- description: Baselines as code with version history
  location: Baseline repository
  frequency: on-event
- description: Drift monitoring reports and alerts
  location: Configuration-drift monitoring
  frequency: continuous
- description: Provisioning checks before lockers leave the depot
  location: Fleet-management plane provisioning records
  frequency: on-event
metrics:
- Baseline compliance per asset class (target ≥ 98 %)
- Drift events not reverted or handled within 24 hours (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.9 — Configuration management

## Objective

Keep every system in a known, secure, documented configuration — from the locker operating system to cloud services and laptops — and notice when it changes.

## Implementation

- POL-VULN VULN-8 (baselines as code from recognised benchmarks, annual review, change management), VULN-9 (continuous drift detection) and VULN-10 (hardening before production, provisioning checks).
- Changes follow POL-SDLC SDLC-9; runbooks under POL-BC BC-7 rely on the same code.

## Evidence

- Baselines as code with version history — Baseline repository.
- Drift monitoring reports and alerts — Configuration-drift monitoring.
- Provisioning checks before lockers leave the depot — Fleet-management plane provisioning records.

## Metrics

- Baseline compliance per asset class (target ≥ 98 %)
- Drift events not reverted or handled within 24 hours (target 0)

## Common pitfalls

- Baselines documented in a wiki but applied by hand — they are code, applied by pipelines.
- Drift alerts ignored as noise — thresholds and ownership per asset class.
