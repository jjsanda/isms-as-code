---
control: A.5.14
applicability: applicable
justification: Parcel events and personal data flow between lockers, backend, carriers and suppliers every
  minute; transfer rules and agreements protect them in motion (supports R-009; NIS2 Art. 21(2)(j) secured
  communications).
implementation_status: implemented
implemented_by:
- POL-AUP
- POL-CLS
owner: isms-manager
risks: []
evidence:
- description: Transfer agreements with carriers and suppliers
  location: Supplier register; contract files
  frequency: on-event
- description: Mail gateway and secure file-transfer service logs
  location: Central log store
  frequency: continuous
- description: Handover records for physical transfers
  location: Depot and store handover log
  frequency: on-event
metrics:
- External transfers of confidential information outside approved channels found in spot checks (target
  0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.14 — Information transfer

## Objective

Make sure information leaves PaketPort only through channels that match its classification — encrypted APIs for carriers, the secure transfer service for files, tamper-evident handovers for hardware — under agreements that say what the recipient may do.

## Implementation

- POL-CLS CLS-9 requires transfer agreements and approved channels and governs physical transfer; POL-AUP AUP-12 to AUP-15 set the user-facing rules for email, messaging, files and media.
- Carrier APIs follow POL-NET NET-5 and POL-CRYP CRYP-1; leakage prevention (POL-CLS CLS-13) monitors the channels.

## Evidence

- Transfer agreements with carriers and suppliers — Supplier register; contract files.
- Mail gateway and secure file-transfer service logs — Central log store.
- Handover records for physical transfers — Depot and store handover log.

## Metrics

- External transfers of confidential information outside approved channels found in spot checks (target 0)

## Common pitfalls

- Agreements that cover the data but not the channel — CLS-9 names both.
- Hardware in transit treated as logistics rather than information transfer — locker controllers carry keys and buffered transactions.
