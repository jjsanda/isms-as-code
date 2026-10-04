---
control: A.8.1
applicability: applicable
justification: Laptops, phones and maintenance tablets are where phishing lands and where confidential
  data is handled; managed, encrypted, patched endpoints without local administrator rights limit R-004
  and R-005.
implementation_status: implemented
implemented_by:
- POL-AUP
owner: it-operations-lead
risks: []
evidence:
- description: Endpoint baseline and compliance reports (encryption, patch level, protection, no local
    administrator)
  location: Endpoint management
  frequency: monthly
- description: Device inventory with assignment
  location: Endpoint management; inventory
  frequency: continuous
metrics:
- Managed endpoints compliant with the baseline (target ≥ 98 %)
- Unmanaged devices found on corporate networks (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.1 — User endpoint devices

## Objective

Ensure every device used for PaketPort work is known, managed, encrypted, up to date, protected and recoverable — including the tablets technicians carry into the field.

## Implementation

- POL-AUP AUP-4 to AUP-6: managed devices only, encryption, updates, screen lock, no local administrator rights, loss reporting, personal phones only in the managed container.
- Hardening baselines under POL-VULN VULN-8 and endpoint protection under VULN-7; remote and mobile specifics in POL-REM (in review).

## Evidence

- Endpoint baseline and compliance reports (encryption, patch level, protection, no local administrator) — Endpoint management.
- Device inventory with assignment — Endpoint management; inventory.

## Metrics

- Managed endpoints compliant with the baseline (target ≥ 98 %)
- Unmanaged devices found on corporate networks (target 0)

## Common pitfalls

- Developer machines exempted from management — exceptions are recorded and compensated, not silent.
- Tablets treated as consumer devices — they are managed endpoints with device certificates (STD-AUTH AUTH-14).
