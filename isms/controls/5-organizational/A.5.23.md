---
control: A.5.23
applicability: applicable
justification: The backend runs entirely on one cloud provider under a shared-responsibility model (LEG-07,
  IP-08); misconfiguration on PaketPort's side is the realistic failure mode (R-006, R-004).
implementation_status: implemented
implemented_by:
- POL-SUP
owner: head-of-platform
risks:
- R-006
evidence:
- description: Shared-responsibility matrix per cloud service
  location: Supplier register; platform documentation
  frequency: annual
- description: Configuration baseline compliance and drift reports for cloud services
  location: Configuration-drift monitoring
  frequency: continuous
- description: Provider assurance reports reviewed
  location: Supplier register
  frequency: annual
metrics:
- Cloud configuration baseline compliance (target ≥ 98 %)
- Tier 1 cloud services with a confirmed exit plan (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.23 — Information security for use of cloud services

## Objective

Use cloud services knowingly — with clear responsibility boundaries, a secure configuration that PaketPort owns and checks, EU data location and a way out.

## Implementation

- POL-SUP SUP-11 (selection criteria), SUP-12 (shared-responsibility matrix; PaketPort's duties implemented under POL-ACC, POL-CRYP, POL-NET, POL-VULN and POL-LOG) and SUP-13 (exit plan).
- Baselines as code and drift monitoring under POL-VULN VULN-8 and VULN-9; customer-managed keys under STD-CRYPTO CRYPTO-3.

## Evidence

- Shared-responsibility matrix per cloud service — Supplier register; platform documentation.
- Configuration baseline compliance and drift reports for cloud services — Configuration-drift monitoring.
- Provider assurance reports reviewed — Supplier register.

## Metrics

- Cloud configuration baseline compliance (target ≥ 98 %)
- Tier 1 cloud services with a confirmed exit plan (target 100 %)

## Common pitfalls

- Assuming the provider's certification covers PaketPort's configuration — the matrix makes PaketPort's share explicit.
- No exit plan until the contract ends — SUP-13 keeps one current.
