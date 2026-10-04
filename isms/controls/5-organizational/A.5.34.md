---
control: A.5.34
applicability: applicable
justification: PaketPort processes the personal data of every locker user; the GDPR (LEG-02), consumers
  (IP-01) and the data protection authorities (IP-05) require lawful processing, an independent DPO, breach
  notification and privacy by design (supports R-009).
implementation_status: implemented
implemented_by:
- POL-LEG
owner: dpo
risks: []
evidence:
- description: Records of processing per entity
  location: DPO records
  frequency: annual
- description: Data protection impact assessments
  location: DPO records
  frequency: on-event
- description: Data-subject request log with response times
  location: Ticket system, project DSR
  frequency: monthly
- description: Breach notification records
  location: Ticket system, project INC
  frequency: on-event
metrics:
- Data-subject requests answered within one month (target 100 %)
- Personal-data breaches notified within 72 hours where required (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.34 — Privacy and protection of personally identifiable information (PII)

## Objective

Protect the personal data of consumers, carriers' staff and employees as the GDPR and national law require — with an independent Data Protection Officer, documented processing, impact assessments, honoured rights and timely breach notification.

## Implementation

- POL-LEG LEG-8 to LEG-14: principles, the DPO's role and independence, impact assessments, processors and transfers, data-subject rights, breach notification, privacy by design.
- PROC-IR stage 6 carries the breach notifications; POL-CLS CLS-12 masks data outside production; POL-SUP binds processors through data-processing agreements.

## Evidence

- Records of processing per entity — DPO records.
- Data protection impact assessments — DPO records.
- Data-subject request log with response times — Ticket system, project DSR.
- Breach notification records — Ticket system, project INC.

## Metrics

- Data-subject requests answered within one month (target 100 %)
- Personal-data breaches notified within 72 hours where required (target 100 %)

## Common pitfalls

- The DPO consulted after the product is built — POL-ORG ORG-12 and LEG-9 involve the DPO at project initiation.
- Breach notification confused with NIS2 reporting — PROC-IR lists both with their own clocks and reporters.
