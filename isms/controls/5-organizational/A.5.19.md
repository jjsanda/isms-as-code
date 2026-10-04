---
control: A.5.19
applicability: applicable
justification: 'Treats R-006 (supplier or cloud provider compromise): carriers, the cloud provider, the
  hardware manufacturer and the German subcontractors all hold access or deliver components; NIS2 Art.
  21(2)(d).'
implementation_status: implemented
implemented_by:
- POL-SUP
owner: head-of-procurement
risks:
- R-006
evidence:
- description: Supplier register with tiers, owners and assessment dates
  location: Supplier register
  frequency: quarterly
- description: Onboarding security assessments of tier 1 and tier 2 suppliers
  location: Supplier register; ticket system, project ISMS-SUP
  frequency: on-event
metrics:
- Tier 1 and tier 2 suppliers with a current security assessment (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.19 — Information security in supplier relationships

## Objective

Know which suppliers matter for security, assess them before they get access or deliver components, and manage the relationship with security in mind throughout.

## Implementation

- POL-SUP SUP-1 (tiers and register) and SUP-2 (proportionate assessment, ISMS Manager approval of tier 1, DPO consultation) govern onboarding; SUP-10 covers the German subcontractors and SUP-15 offboarding.
- Supplier owners are roles; the reseller joint venture PaketPort Italia is handled as a third party under the same rules.

## Evidence

- Supplier register with tiers, owners and assessment dates — Supplier register.
- Onboarding security assessments of tier 1 and tier 2 suppliers — Supplier register; ticket system, project ISMS-SUP.

## Metrics

- Tier 1 and tier 2 suppliers with a current security assessment (target 100 %)

## Common pitfalls

- Every supplier treated the same — tiers keep the effort where the risk is.
- Assessments done once at onboarding — SUP-8 reviews keep them current.
