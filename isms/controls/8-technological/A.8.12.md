---
control: A.8.12
applicability: applicable
justification: 'Bulk exports of consumer data and uncontrolled channels are the realistic leakage paths
  (supports R-009 and R-010); monitoring and restriction are proportionate to classification. Partially
  implemented: export alerts and USB blocking are live, outbound content inspection is being tuned.'
implementation_status: partially-implemented
implemented_by:
- POL-CLS
owner: security-engineer
risks: []
evidence:
- description: Export alert rules and alert handling records
  location: Central log store; ticket system, project INC
  frequency: monthly
- description: Channel restrictions (USB blocking, web filter, mail gateway policies)
  location: Endpoint management; gateway consoles
  frequency: continuous
metrics:
- Bulk-export alerts triaged within the POL-IR deadlines (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.12 — Data leakage prevention

## Objective

Detect and prevent confidential information leaving PaketPort through email, file sharing, web uploads, removable media or bulk exports.

## Implementation

- POL-CLS CLS-13 (restricted channels, export alerts, USB blocking, gateway inspection); POL-AUP AUP-12 to AUP-14; POL-LOG LOG-6 (bulk-export detection); alerts under POL-IR.
- Partially implemented: content-inspection rules at the mail gateway are in tuning to reduce false positives.

## Evidence

- Export alert rules and alert handling records — Central log store; ticket system, project INC.
- Channel restrictions (USB blocking, web filter, mail gateway policies) — Endpoint management; gateway consoles.

## Metrics

- Bulk-export alerts triaged within the POL-IR deadlines (target 100 %)

## Common pitfalls

- Blocking everything and breaking work — proportionate rules by classification.
- Alerts without an owner — the SOC triages them under POL-IR.
