---
control: A.5.1
applicability: applicable
justification: Required by ISO/IEC 27001 clause 5.2 and by NIS2 Art. 20 and 21 (LEG-01, LEG-04); the management
  body (IP-06) and the competent authority (IP-04) expect an approved, communicated policy set. Treats
  R-012.
implementation_status: implemented
implemented_by:
- POL-ISMS
owner: isms-manager
risks:
- R-012
evidence:
- description: Approved POL-ISMS and topic-specific policies with version history
  location: Repository main branch; signed PDFs in the release assets
  frequency: on-event
- description: Communication records of MAJOR policy versions
  location: Announcement archive; training platform
  frequency: on-event
- description: Periodic review entries of every policy
  location: Document CHANGELOGs; generated document register
  frequency: annual
metrics:
- Policies reviewed by their due date (target ≥ 95 %)
- Staff acknowledgement of POL-AUP and POL-ISMS in the annual training (target ≥ 98 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.1 — Policies for information security

## Objective

Give everyone at PaketPort one approved, current and communicated set of rules — the top-level policy and the topic-specific policies under it — so that security decisions in all three entities follow the same direction and auditors and authorities can see management's commitment.

## Implementation

- POL-ISMS is the top-level policy approved by the Managing Director; ISMS-8 names the topic-specific policies, which are approved under PROC-DOC stage 3 and published as signed PDFs with every release.
- Every policy carries owner, approver, effective and review dates in its front matter; the generated document register is the index, and `isms review-due` together with the weekly reminder job drives periodic review (PROC-DOC stage 5).
- MAJOR versions are communicated before their effective date (POL-ORG ORG-13) and acknowledged through the training platform (POL-HR HR-5).
- The policy set applies to all entities; deviations are handled through `applies_to` and the exception register, never through local policies.

## Evidence

- Approved POL-ISMS and topic-specific policies with version history — Repository main branch; signed PDFs in the release assets.
- Communication records of MAJOR policy versions — Announcement archive; training platform.
- Periodic review entries of every policy — Document CHANGELOGs; generated document register.

## Metrics

- Policies reviewed by their due date (target ≥ 95 %)
- Staff acknowledgement of POL-AUP and POL-ISMS in the annual training (target ≥ 98 %)

## Common pitfalls

- Policies that exist but are never read: acknowledgement is tied to the training platform, and access is suspended for overdue training (POL-HR HR-8).
- Local versions drifting in the subsidiaries: one repository and one document set for the group, entity-specific rules only through `applies_to`.
- Reviews skipped silently: the review clock is data, checked by `isms validate` and surfaced by the reminder job.
