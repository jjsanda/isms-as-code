---
control: A.5.21
applicability: applicable
justification: 'Locker controllers and firmware components come from suppliers; a compromised component
  would reach the whole fleet (R-006), and the Cyber Resilience Act expects bill-of-materials management
  (LEG-03). Partially implemented: bills of materials exist for firmware and backend, hardware provenance
  attestations are still being collected.'
implementation_status: partially-implemented
implemented_by:
- POL-SUP
owner: head-of-procurement
risks:
- R-006
evidence:
- description: Software bills of materials for firmware and backend releases
  location: Build pipeline artefacts
  frequency: on-event
- description: Incoming-goods checks against shipment records at the depot
  location: Depot receiving log
  frequency: on-event
metrics:
- Releases with a complete bill of materials (target 100 %)
- Deliveries with tamper findings investigated under POL-IR (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.21 — Managing information security in the ICT supply chain

## Objective

Reduce the risk that a compromised component — a chip, a library, a firmware module — enters PaketPort's products or platform unnoticed, from the supplier's factory through the Vienna depot to the fleet.

## Implementation

- POL-SUP SUP-5 (provenance and bill-of-materials review by the Software Engineering Lead), SUP-6 (tamper-evident delivery and provisioning before use) and SUP-7 (update and disclosure commitments).
- POL-SDLC SDLC-6 scans components on every build and POL-VULN VULN-1 monitors the bills of materials continuously.
- Partially implemented: hardware provenance verification for older generations and supplier attestations are in the risk treatment plan.

## Evidence

- Software bills of materials for firmware and backend releases — Build pipeline artefacts.
- Incoming-goods checks against shipment records at the depot — Depot receiving log.

## Metrics

- Releases with a complete bill of materials (target 100 %)
- Deliveries with tamper findings investigated under POL-IR (target 100 %)

## Common pitfalls

- A bill of materials generated but never read — VULN-1 and SDLC-6 consume it automatically.
- Trusting packaging alone — controllers are re-provisioned with PaketPort firmware and certificates before use.
