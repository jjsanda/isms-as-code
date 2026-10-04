---
control: A.7.10
applicability: applicable
justification: Removable media and the storage inside lockers and controllers carry keys, buffered transactions
  and backups; encryption, registration and disposal rules prevent leakage (supports R-001 and R-009).
implementation_status: implemented
implemented_by:
- POL-CLS
owner: it-operations-lead
risks: []
evidence:
- description: USB blocking configuration on endpoints
  location: Endpoint management
  frequency: continuous
- description: Media register and destruction certificates
  location: Facilities records
  frequency: on-event
metrics:
- Unregistered removable media detected on endpoints (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.7.10 — Storage media

## Objective

Control storage media through its life — only where needed, encrypted, registered, and wiped or destroyed at the end — including the media built into lockers.

## Implementation

- POL-CLS CLS-10 (media only where no channel exists, encryption, registration, USB blocked by default, depot and store storage, locker storage bound to the device) and CLS-11 (deletion); POL-PHY PHY-19 for disposal; POL-CRYP CRYP-2 for encryption.

## Evidence

- USB blocking configuration on endpoints — Endpoint management.
- Media register and destruction certificates — Facilities records.

## Metrics

- Unregistered removable media detected on endpoints (target 0)

## Common pitfalls

- USB allowed 'just for the lab' — the lab follows the same rule with registered media.
- Locker storage forgotten at decommissioning — CLS-11 and PHY-19 wipe and revoke before re-use.
