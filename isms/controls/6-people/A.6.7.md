---
control: A.6.7
applicability: applicable
justification: Hybrid office work and an entirely mobile field service make remote working the normal
  case (IP-07); rules for devices, networks and workspaces protect information outside the office (supports
  R-004 and R-005).
implementation_status: implemented
implemented_by:
- POL-AUP
owner: it-operations-lead
risks: []
evidence:
- description: Remote-access configuration (zero-trust gateway, VPN with multi-factor authentication)
  location: Identity provider; gateway configuration
  frequency: continuous
- description: Device-management compliance reports
  location: Endpoint management
  frequency: monthly
metrics:
- Remote sessions without multi-factor authentication (target 0)
- Managed devices compliant with the baseline (target ≥ 98 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.6.7 — Remote working

## Objective

Let people work securely wherever they are — at home, on the road, at a locker site — with managed devices, authenticated connections and a private workspace.

## Implementation

- POL-AUP AUP-8 sets the binding rules today; POL-REM (0.3.0, in review) will extend them with REM-1 to REM-10 (eligibility, cross-border work, travel, field-service vehicles) once approved.
- POL-ACC ACC-8 and STD-AUTH AUTH-8 require multi-factor authentication for all remote access; POL-NET NET-4 defines the gateway and device requirements.

## Evidence

- Remote-access configuration (zero-trust gateway, VPN with multi-factor authentication) — Identity provider; gateway configuration.
- Device-management compliance reports — Endpoint management.

## Metrics

- Remote sessions without multi-factor authentication (target 0)
- Managed devices compliant with the baseline (target ≥ 98 %)

## Common pitfalls

- Remote-work rules that ignore the field technicians' vehicles — POL-REM REM-8 and REM-9 address them.
- VPN without device posture checks — the zero-trust gateway admits managed, compliant devices only.
