---
control: A.5.9
applicability: applicable
justification: A locker nobody knows about cannot be patched, monitored or recovered; the inventory underpins
  vulnerability management, backup and incident response for a dispersed estate and the knowledge inventory
  supports R-013. NIS2 Art. 21(2)(i).
implementation_status: implemented
implemented_by:
- POL-CLS
owner: it-operations-lead
risks:
- R-013
evidence:
- description: Inventory exports per source of truth (fleet-management plane, cloud inventory, endpoint
    management, configuration database)
  location: Configuration database; quarterly reconciliation report
  frequency: quarterly
- description: Owner confirmations of inventory entries
  location: Ticket system, project ISMS-ASSET
  frequency: semi-annual
- description: Locker records with site, generation, firmware and certificate status
  location: Fleet-management plane
  frequency: continuous
metrics:
- Assets found by discovery scans but missing from the inventory (target 0 per quarter)
- Asset classes with a confirmed owner (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.9 — Inventory of information and other associated assets

## Objective

Maintain one reliable picture of what PaketPort has — information, lockers, servers, endpoints, software, services — who owns it and how sensitive it is, across all three entities.

## Implementation

- POL-CLS CLS-1 to CLS-3 define the inventory, its sources of truth, the six-monthly owner confirmation and the quarterly reconciliation against discovery scans.
- The fleet-management plane is authoritative for lockers: a locker that is not registered accepts no parcels (CLS-3).
- Suppliers' services are inventoried through the supplier register (POL-SUP SUP-1); information assets carry owners and classifications like hardware does.

## Evidence

- Inventory exports per source of truth (fleet-management plane, cloud inventory, endpoint management, configuration database) — Configuration database; quarterly reconciliation report.
- Owner confirmations of inventory entries — Ticket system, project ISMS-ASSET.
- Locker records with site, generation, firmware and certificate status — Fleet-management plane.

## Metrics

- Assets found by discovery scans but missing from the inventory (target 0 per quarter)
- Asset classes with a confirmed owner (target 100 %)

## Common pitfalls

- A spreadsheet inventory that is out of date the day it is saved — the operational systems are the sources of truth and are reconciled.
- Information assets forgotten in favour of hardware — data stores are inventory entries with owners and classifications.
