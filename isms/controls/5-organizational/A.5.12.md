---
control: A.5.12
applicability: applicable
justification: Consumer personal data, carrier credentials, firmware signing keys and public locker locations
  need very different handling; classification drives the handling rules, encryption and access decisions
  (supports R-009).
implementation_status: implemented
implemented_by:
- POL-CLS
owner: isms-manager
risks: []
evidence:
- description: Classification scheme and handling rules
  location: POL-CLS CLS-5 to CLS-8
  frequency: annual
- description: Classification tags on data stores and repositories
  location: Cloud data-classification tags; repository metadata
  frequency: continuous
- description: Annual classification review of confidential and restricted information
  location: Ticket system, project ISMS-ASSET
  frequency: annual
metrics:
- Data stores with a classification tag (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.12 — Classification of information

## Objective

Give every piece of information a level — public, internal, confidential, restricted — with a clear definition and PaketPort examples, so that people and systems apply the right protection without case-by-case debate.

## Implementation

- POL-CLS CLS-5 defines the four levels with examples, CLS-6 the review triggers including aggregation, and CLS-8 the handling table.
- Tags in the cloud platform and repositories make the level machine-readable for access (POL-ACC ACC-15), encryption (POL-CRYP) and leakage prevention (CLS-13).

## Evidence

- Classification scheme and handling rules — POL-CLS CLS-5 to CLS-8.
- Classification tags on data stores and repositories — Cloud data-classification tags; repository metadata.
- Annual classification review of confidential and restricted information — Ticket system, project ISMS-ASSET.

## Metrics

- Data stores with a classification tag (target 100 %)

## Common pitfalls

- Too many levels, or none used — four levels with concrete examples keep the scheme usable.
- Aggregation ignored — CLS-6 raises the level for bulk exports of parcel events.
