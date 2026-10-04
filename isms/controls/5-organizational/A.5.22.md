---
control: A.5.22
applicability: applicable
justification: 'Supplier posture changes after onboarding; annual reviews and change notification keep
  assurance current (R-006; LEG-05 attestations). Partially implemented: tier 1 reviews run, the tier
  2 review cycle is being scheduled.'
implementation_status: partially-implemented
implemented_by:
- POL-SUP
owner: head-of-procurement
risks:
- R-006
evidence:
- description: Annual tier 1 supplier review records
  location: Supplier register; ticket system, project ISMS-SUP
  frequency: annual
- description: Supplier change notifications and their assessments
  location: Ticket system, project ISMS-SUP
  frequency: on-event
metrics:
- Tier 1 suppliers reviewed within the last twelve months (target 100 %)
- Tier 2 suppliers reviewed within the last 24 months (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.22 — Monitoring, review and change management of supplier services

## Objective

Notice when a supplier's service, security or ownership changes and re-assess before the change affects PaketPort, and keep assurance reports and performance under regular review.

## Implementation

- POL-SUP SUP-8 (review cadence and content), SUP-9 (change notification and re-assessment under PROC-RISK) and SUP-10 (annual subcontractor review); results go to the Security Steering Committee.
- Cloud exit plans are confirmed at the review (SUP-13). Partially implemented: the tier 2 cycle starts with the next review round.

## Evidence

- Annual tier 1 supplier review records — Supplier register; ticket system, project ISMS-SUP.
- Supplier change notifications and their assessments — Ticket system, project ISMS-SUP.

## Metrics

- Tier 1 suppliers reviewed within the last twelve months (target 100 %)
- Tier 2 suppliers reviewed within the last 24 months (target 100 %)

## Common pitfalls

- Reviews limited to reading the supplier's certificate — incidents, service levels and changes are reviewed too.
- Sub-processor changes noticed after the fact — the annex requires prior notification.
