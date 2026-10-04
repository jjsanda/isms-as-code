---
control: A.5.18
applicability: applicable
justification: 'Treats R-004: over-provisioned and never-reviewed rights turn one compromised account
  into broad access; approval and periodic review are also carrier and insurer expectations (LEG-05, LEG-08).'
implementation_status: implemented
implemented_by:
- POL-ACC
owner: it-operations-lead
risks:
- R-004
evidence:
- description: Access requests with line-manager and system-owner approval
  location: Ticket system, queue ACCESS
  frequency: on-event
- description: Quarterly privileged and semi-annual general access review attestations
  location: Ticket system, project ISMS-AR
  frequency: quarterly
- description: Removal records from reviews and leaver processing
  location: Ticket system
  frequency: on-event
metrics:
- Access reviews completed by their due date (target 100 %)
- Rights found without a documented approval per review (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.18 — Access rights

## Objective

Grant access only on approved need, adjust it when roles change, remove it when people leave, and review it regularly — for staff, subcontractors and service accounts alike.

## Implementation

- POL-ACC ACC-2, ACC-3 and ACC-5 to ACC-7 set the rules and ACC-14 the external-party rules; the role bundles in the identity provider implement role-based assignment.
- PROC-JML stages 1 to 3 and 5 (in draft) describe the steps; attestations are recorded in project ISMS-AR and rights without approval are removed, not legitimised.

## Evidence

- Access requests with line-manager and system-owner approval — Ticket system, queue ACCESS.
- Quarterly privileged and semi-annual general access review attestations — Ticket system, project ISMS-AR.
- Removal records from reviews and leaver processing — Ticket system.

## Metrics

- Access reviews completed by their due date (target 100 %)
- Rights found without a documented approval per review (target 0)

## Common pitfalls

- Reviews that rubber-stamp — rights without approval records are removed (PROC-JML 5.1).
- Rights accumulating through moves — ACC-5 re-evaluates all rights within five working days.
