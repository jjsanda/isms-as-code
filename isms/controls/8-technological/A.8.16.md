---
control: A.8.16
applicability: applicable
justification: 'Treats R-002 and R-008: logs are useless without someone watching; detection use cases
  and round-the-clock alert handling are what achieve the NIS2 deadlines. Partially implemented: core
  use cases and SOC coverage exist, anomaly detection for API usage and automated intelligence enrichment
  are being added.'
implementation_status: partially-implemented
implemented_by:
- POL-LOG
owner: head-of-platform
risks:
- R-002
- R-008
evidence:
- description: Detection use case catalogue with review dates
  location: Detection content repository
  frequency: quarterly
- description: Alert handling statistics (acknowledge and resolve times)
  location: SOC dashboards; steering committee pack
  frequency: monthly
- description: Detection test and exercise records
  location: Ticket system, project ISMS-EXERCISE
  frequency: semi-annual
metrics:
- S1 and S2 alerts acknowledged within 15 minutes (target ≥ 95 %)
- Detection use cases reviewed in the last quarter (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.16 — Monitoring activities

## Objective

Watch the logs and the systems continuously for signs of attack, misuse or failure — and get the right people moving within minutes.

## Implementation

- POL-LOG LOG-6 (use cases), LOG-7 (alert routing and response times) and LOG-8 (monthly review); intelligence input from POL-IR IR-15; alerts become incidents under PROC-IR stage 1.
- Partially implemented: API anomaly detection and automated enrichment are in the risk treatment plan.

## Evidence

- Detection use case catalogue with review dates — Detection content repository.
- Alert handling statistics (acknowledge and resolve times) — SOC dashboards; steering committee pack.
- Detection test and exercise records — Ticket system, project ISMS-EXERCISE.

## Metrics

- S1 and S2 alerts acknowledged within 15 minutes (target ≥ 95 %)
- Detection use cases reviewed in the last quarter (target 100 %)

## Common pitfalls

- A monitoring platform with no detection engineering — use cases are owned and reviewed quarterly.
- Alert fatigue — false positives are tuned, never silenced without a record.
