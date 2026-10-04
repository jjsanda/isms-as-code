---
control: A.5.13
applicability: applicable
justification: Labels make classification visible to people and enforceable by tools — subject prefixes,
  repository metadata and cloud tags are how the handling rules are applied in practice.
implementation_status: implemented
implemented_by:
- POL-CLS
owner: isms-manager
risks: []
evidence:
- description: Labelling conventions per medium
  location: POL-CLS CLS-7
  frequency: annual
- description: Sample check of labels in repositories and data stores
  location: Quarterly spot check under PROC-CAPA step 1.2
  frequency: quarterly
metrics:
- Confidential and restricted repositories and data stores with a correct label in spot checks (target
  100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.13 — Labelling of information

## Objective

Ensure that classified information carries its level wherever it goes — a document header, a subject prefix, a storage tag, a printed sticker — so that handling rules and technical controls can act on it.

## Implementation

- POL-CLS CLS-7 defines the labels per medium and the default (internal); this repository's own `classification` front-matter field is an instance of the rule.
- The mail gateway and the leakage-prevention rules (CLS-13) act on the labels; spot checks verify them.

## Evidence

- Labelling conventions per medium — POL-CLS CLS-7.
- Sample check of labels in repositories and data stores — Quarterly spot check under PROC-CAPA step 1.2.

## Metrics

- Confidential and restricted repositories and data stores with a correct label in spot checks (target 100 %)

## Common pitfalls

- Labels that nobody applies because the tooling makes it hard — defaults and metadata fields instead of manual stamps.
- Labels on paper but not in systems — the cloud tags are the ones the controls read.
