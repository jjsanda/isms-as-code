---
control: A.5.36
applicability: applicable
justification: Policies that are not checked erode; regular compliance checks by owners, automation and
  spot checks are how PaketPort knows its rules are followed (LEG-04; NIS2 Art. 21(2)(f)).
implementation_status: implemented
implemented_by:
- POL-ISMS
- PROC-CAPA
owner: isms-manager
risks: []
evidence:
- description: Automated compliance check results (isms validate, drift monitoring, identity and endpoint
    reports)
  location: Pipeline and monitoring dashboards
  frequency: continuous
- description: Quarterly spot check records
  location: Ticket system, project ISMS-CAPA
  frequency: quarterly
- description: Owner review entries
  location: Document CHANGELOGs; control guide last_assessed dates
  frequency: annual
metrics:
- Spot checks performed per quarter (target 8, two per theme)
- Nonconformities from compliance checks closed within deadline (target ≥ 90 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.36 — Compliance with policies, rules and standards for information security

## Objective

Check regularly — automatically where possible, by sampling otherwise — that the policies, standards and procedures are actually followed in every entity, and treat what is not as a nonconformity.

## Implementation

- POL-ISMS ISMS-10 and ISMS-11 set consequences and assurance; PROC-CAPA step 1.2 defines the automated checks, the quarterly spot checks across entities and the owners' reviews, and steps 2 to 7 handle what they find.
- This repository's `isms validate` and the generation drift check are two of the automated checks.

## Evidence

- Automated compliance check results (isms validate, drift monitoring, identity and endpoint reports) — Pipeline and monitoring dashboards.
- Quarterly spot check records — Ticket system, project ISMS-CAPA.
- Owner review entries — Document CHANGELOGs; control guide last_assessed dates.

## Metrics

- Spot checks performed per quarter (target 8, two per theme)
- Nonconformities from compliance checks closed within deadline (target ≥ 90 %)

## Common pitfalls

- Compliance measured by self-declaration only — automation and spot checks add independent evidence.
- Checks that find the same issue every quarter — PROC-CAPA's root-cause analysis and trend review.
