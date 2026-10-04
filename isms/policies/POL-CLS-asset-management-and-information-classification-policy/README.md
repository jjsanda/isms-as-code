---
id: POL-CLS
title: Asset Management and Information Classification Policy
type: policy
status: approved
version: 1.1.0
classification: internal
owner: isms-manager
approver: managing-director
effective_date: &id001 2026-01-12
last_reviewed: *id001
review_cycle: P1Y
next_review: 2027-01-12
controls:
- A.5.9
- A.5.11
- A.5.12
- A.5.13
- A.5.14
- A.7.10
- A.8.10
- A.8.11
- A.8.12
clauses: []
applies_to:
- all
related:
- POL-ACC
- POL-AUP
- POL-LEG
- POL-CRYP
- POL-PHY
supersedes: []
language: en
tags:
- assets
- classification
- data-protection
---

# POL-CLS — Asset Management and Information Classification Policy

## Purpose

Every control in the ISMS starts from knowing what exists and how sensitive it is. This policy
requires an inventory of information and of the assets that carry it — from the customer database
to every street-sited locker — assigns owners, classifies information into four levels with
handling rules, and governs transfer, storage media, deletion, masking and leakage prevention.

## Scope

All information and associated assets of the in-scope entities: information (customer and carrier
data, parcel events, source code, keys, business records), hardware (lockers and their
controllers, servers, network equipment, endpoints, maintenance tools, media), software and cloud
services, and services provided by suppliers. It applies to everyone who creates, handles or owns
such assets.

## Policy statements

### Inventory and ownership (A.5.9)

- **CLS-1** The group shall maintain an inventory of information and associated assets recording,
  for each asset or asset class, a unique identifier, the owner role, the classification, the
  location or hosting site, the entity and the life-cycle status. The sources of truth are the
  fleet-management plane for lockers and controllers, the cloud inventory for cloud resources,
  endpoint management for laptops, phones and tablets, the configuration database for everything
  else, and the supplier register under POL-SUP for services.
- **CLS-2** Asset owners shall confirm their inventory entries at least every six months and
  whenever assets are procured, moved between entities, decommissioned or disposed of. The
  Information Security Officer / ISMS Manager reconciles the inventory against discovery scans
  every quarter.
- **CLS-3** Lockers shall be recorded individually from provisioning in the Vienna depot to
  decommissioning, with site, hardware generation, firmware version and certificate status. A
  locker that is not registered in the fleet-management plane shall not accept parcels.

### Return of assets (A.5.11)

- **CLS-4** On termination or change of role everyone shall return all PaketPort assets —
  laptops, phones, tablets, tokens, badges, locker keys and master keys, maintenance tools, spare
  parts, documents and media — following the leaver steps of PROC-JML. Line managers confirm the
  return; the IT Operations Lead and the Facilities & Physical Security Lead record it. Information
  needed by PaketPort shall be handed over before departure.

### Classification (A.5.12)

- **CLS-5** Information shall be classified by its owner into one of four levels:

| Level | Definition | PaketPort examples |
| --- | --- | --- |
| Public | Intended for, or harmless when disclosed outside, the group | Locker locations and opening hours, marketing material, POL-ISMS |
| Internal | For staff and contractors; disclosure causes limited harm | Most policies and procedures, internal announcements, non-sensitive operating data |
| Confidential | Disclosure would harm customers, partners or PaketPort; restricted to roles with a need to know | Consumer personal data, parcel events, carrier API credentials, source code, network documentation, contracts, the risk register |
| Restricted | Disclosure would cause severe harm; access limited to named roles with the strongest protection | Firmware signing and root keys, master credentials, incident forensic data, HR and payroll data, security test results |

- **CLS-6** Classification shall be reviewed when information is created, when its sensitivity
  changes and at least annually for confidential and restricted information. Aggregation — for
  example an export of many parcel events — may raise the level.

### Labelling (A.5.13)

- **CLS-7** Confidential and restricted information shall be labelled: in documents and
  repositories through the `classification` metadata and a visible header, in systems through the
  data-classification tags of the cloud platform and the data stores, in email through the subject
  prefix set by the sender, and on paper and media through a printed label. Internal is the default
  where no label is present; public information is labelled explicitly.

### Handling rules

- **CLS-8** Information shall be handled according to its level:

| Activity | Internal | Confidential | Restricted |
| --- | --- | --- | --- |
| Storage | Managed systems | Encrypted at rest (POL-CRYP), access by role (POL-ACC) | Encrypted, access by named role, hardware-backed keys where applicable |
| Transfer | Approved channels | Encrypted channels only; transfer agreement with external parties | No email; dedicated secure transfer approved by the Information Security Officer / ISMS Manager |
| External sharing | As needed | Under confidentiality agreement or contract; minimum necessary | Only with the Managing Director's approval |
| Printing and media | Permitted | Locked away, shredded after use | Printing prohibited unless approved; media encrypted and logged |
| Disposal | Standard deletion | Secure deletion; certificate of destruction for media | Secure deletion; witnessed destruction |

### Information transfer (A.5.14)

- **CLS-9** Transfers of confidential information to carriers, suppliers, site hosts and
  authorities shall be covered by a written agreement naming the data, purpose, channel,
  protection and deletion, and shall use the channels approved in POL-AUP and the authenticated
  APIs under POL-NET. Physical transfer — lockers and controllers between the depot, the sites and
  the Brno lab, backup media, returned devices — uses tamper-evident packaging, tracking and a
  handover record.

### Storage media (A.7.10)

- **CLS-10** Removable media shall be used only where no approved transfer channel exists, shall
  be encrypted, registered to an owner and wiped or destroyed after use; USB storage is blocked on
  managed endpoints by default. Media and spare controllers at the Vienna depot and the Munich
  store are kept in the locked secure area under POL-PHY, and the storage in lockers is encrypted
  and bound to the device.

### Information deletion (A.8.10)

- **CLS-11** Information shall be deleted when the retention period in the records schedule of
  POL-LEG ends or the purpose ceases, using the deletion functions of the data stores, the cloud
  provider's deletion guarantees for storage, and secure wiping or destruction for devices and
  media. Decommissioned lockers have their storage wiped and their certificates revoked before
  they leave the fleet. Deletion of personal data is recorded for the Data Protection Officer.

### Data masking (A.8.11)

- **CLS-12** Personal data shall be masked, pseudonymised or replaced by synthetic data outside
  production — in development, test, training and analytics environments — unless the Data
  Protection Officer approves a documented exception. The masking rules are being extended to all
  data stores; the Statement of Applicability shows the current status.

### Data leakage prevention (A.8.12)

- **CLS-13** Channels that can carry information out of the group — email, file-sharing, web
  uploads, removable media, printing, bulk exports from the customer and parcel data stores —
  shall be restricted and monitored in proportion to the classification: bulk exports from
  confidential data stores are limited to named roles and raise an alert in the security
  operations centre, USB storage is blocked, and the web filter and mail gateway inspect outgoing
  transfers. Alerts are handled under POL-IR.

## Roles and responsibilities

| Role | Responsibility |
| --- | --- |
| Information Security Officer / ISMS Manager | Owns this policy and the classification scheme; reconciles the inventory; approves transfers of restricted information |
| Asset and information owners | Classify, label, confirm inventory entries, approve access and transfers |
| IT Operations Lead | Endpoint and media controls, the configuration database, asset return of leavers |
| Head of Platform & SRE | Cloud inventory, locker records in the fleet-management plane, deletion in production systems |
| Data Protection Officer | Advises on the classification of personal data, approves masking exceptions, keeps deletion records |
| Facilities & Physical Security Lead | Physical media, the secure areas of depot and store, destruction certificates |
| Country Manager Germany; Site Lead Brno | Inventory accuracy and asset returns at their entity |

## Compliance and exceptions

Compliance is monitored through the inventory reconciliation results, the share of assets with an
owner and a classification (target 100 %), leakage-prevention alerts and their handling, and the
deletion records. Exceptions follow the control exception request: approval by the Information
Security Officer / ISMS Manager and the information owner — and by the Data Protection Officer
where personal data is involved — time-limited to at most twelve months and recorded in the
exception register.

## Related documents

- POL-ACC — Access Control Policy
- POL-AUP — Acceptable Use Policy
- POL-LEG — Legal, Regulatory and Privacy Compliance Policy
- POL-CRYP — Cryptography Policy
- POL-PHY — Physical and Environmental Security Policy
