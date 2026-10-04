---
control: A.8.3
applicability: applicable
justification: 'Treats R-004 and supports R-009: consumer personal data and restricted keys must be reachable
  only by roles with a purpose; restriction by classification makes least privilege concrete.'
implementation_status: implemented
implemented_by:
- POL-ACC
owner: isms-manager
risks:
- R-004
evidence:
- description: Role-to-data access matrix for confidential and restricted data stores
  location: Identity provider role catalogue; cloud IAM export
  frequency: semi-annual
- description: Access logs of confidential data stores
  location: Central log store
  frequency: continuous
metrics:
- Roles with access to customer personal data without a documented processing purpose (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.3 — Information access restriction

## Objective

Restrict access to information according to its classification and the person's need — especially consumer personal data and restricted keys — and keep production data out of non-production environments.

## Implementation

- POL-ACC ACC-15 (access by classification, personal data only with a purpose, no production data in test) and ACC-2 (least privilege); POL-CLS CLS-8 handling rules and CLS-12 masking.
- Technical enforcement through application roles, views and the bastion, as described in the A.5.15 guide.

## Evidence

- Role-to-data access matrix for confidential and restricted data stores — Identity provider role catalogue; cloud IAM export.
- Access logs of confidential data stores — Central log store.

## Metrics

- Roles with access to customer personal data without a documented processing purpose (target 0)

## Common pitfalls

- Access granted to a whole database because one table is needed — application roles and views narrow it.
- Analytics teams copying production data — masking under CLS-12.
