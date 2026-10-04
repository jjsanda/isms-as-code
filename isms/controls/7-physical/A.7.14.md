---
control: A.7.14
applicability: applicable
justification: Decommissioned lockers, controllers, laptops and media leave PaketPort's control; wiping,
  certificate revocation and destruction certificates prevent data and key leakage (supports R-001 and
  R-009).
implementation_status: implemented
implemented_by:
- POL-PHY
owner: facilities-lead
risks: []
evidence:
- description: Destruction certificates and wipe logs
  location: Facilities records; endpoint management
  frequency: on-event
- description: Locker decommissioning records with certificate revocation
  location: Fleet-management plane; certificate authority logs
  frequency: on-event
metrics:
- Disposed devices without a wipe log or destruction certificate (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.7.14 — Secure disposal or re-use of equipment

## Objective

Make sure nothing leaves PaketPort — a scrapped locker, a returned laptop, a failed disk — with data or keys still on it.

## Implementation

- POL-PHY PHY-19 (verified wiping or destruction, certificates, locker decommissioning with storage wiped, certificates revoked and keys removed); POL-CLS CLS-11 (deletion) and CLS-4 (asset return); POL-CRYP CRYP-11 (revocation).

## Evidence

- Destruction certificates and wipe logs — Facilities records; endpoint management.
- Locker decommissioning records with certificate revocation — Fleet-management plane; certificate authority logs.

## Metrics

- Disposed devices without a wipe log or destruction certificate (target 0)

## Common pitfalls

- Returning leased or warranty equipment with disks inside — disks are wiped or removed.
- Re-using enclosures with old controllers — controllers are re-provisioned or destroyed.
