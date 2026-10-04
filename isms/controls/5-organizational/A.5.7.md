---
control: A.5.7
applicability: applicable
justification: 'Treats R-007 (exploitation of unpatched vulnerabilities) and improves detection for R-002;
  part of the cyber-hygiene measures of NIS2 Art. 21(2)(g) (LEG-01). The programme is young: sources and
  weekly triage exist, automated enrichment of detections is still being built.'
implementation_status: partially-implemented
implemented_by:
- POL-IR
owner: security-engineer
risks:
- R-007
evidence:
- description: Weekly threat intelligence triage notes with actions
  location: Threat intelligence log, ticket system project ISMS-TI
  frequency: weekly
- description: Detection rules and vulnerability priorities traced to intelligence items
  location: Detection content repository; vulnerability tracker
  frequency: on-event
metrics:
- Intelligence items triaged within one week of receipt (target 100 %)
- Detection use cases updated from intelligence per quarter (target ≥ 3)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.7 — Threat intelligence

## Objective

Turn information about threats to lockers, the backend, the app and staff into concrete defensive action — detection rules, patch priorities, awareness content — instead of letting it sit in mailboxes.

## Implementation

- POL-IR IR-15 defines the sources, the weekly triage by the Security Engineer and the four outputs (detection, vulnerability priorities, awareness, risk updates).
- Inputs arrive through the memberships of POL-ORG ORG-11 and the vulnerability feeds of POL-VULN VULN-2; strategic items feed the risk assessment (PROC-RISK stage 2).
- Partially implemented: indicator feeds are not yet ingested automatically into the central log store; the work is tracked in the risk treatment plan.

## Evidence

- Weekly threat intelligence triage notes with actions — Threat intelligence log, ticket system project ISMS-TI.
- Detection rules and vulnerability priorities traced to intelligence items — Detection content repository; vulnerability tracker.

## Metrics

- Intelligence items triaged within one week of receipt (target 100 %)
- Detection use cases updated from intelligence per quarter (target ≥ 3)

## Common pitfalls

- Collecting feeds without a consumer — every item has a named output or is closed.
- Only technical intelligence — strategic items (regulation, sector attacks) are routed to the risk assessment and the steering committee.
