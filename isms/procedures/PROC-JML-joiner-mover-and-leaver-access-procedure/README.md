---
id: PROC-JML
title: Joiner, Mover and Leaver Access Procedure
type: procedure
status: draft
version: 0.2.0
classification: internal
owner: it-operations-lead
approver: isms-manager
review_cycle: P1Y
controls:
- A.5.11
- A.5.16
- A.5.18
- A.6.5
clauses: []
applies_to:
- all
related:
- POL-ACC
- POL-HR
- POL-CLS
supersedes: []
language: en
tags:
- access
- jml
---

# PROC-JML — Joiner, Mover and Leaver Access Procedure

> **Draft.** Version 0.2.0 is not yet approved; until approval, the joiner-mover-leaver checklist
> of the IT Operations Lead applies under POL-ACC.

## Purpose

This procedure makes the identity life-cycle statements of POL-ACC (ACC-3 to ACC-7) and the asset
and post-employment rules of POL-CLS and POL-HR operational: who does what, in which order and by
when, whenever a person joins, changes role or entity, or leaves — for employees, contractors and
field-service subcontractor technicians.

## Scope

All identities in the identity provider and in systems that cannot federate, all issue and return
of assets, and all three entities. Service and device identities are covered by the
identity-management rules of stage 4.

## Procedure

### 1. Joiner

1. The HR Manager creates the employment or engagement record with start date, job profile,
   entity, line manager and contract type. For subcontractor technicians the Country Manager
   Germany acts as sponsor and provides the contract reference and the screening confirmation
   (POL-HR HR-2). No record, no account.
2. The IT Operations Lead creates the personal account from the record two working days before
   the start date with the role bundle of the job profile and entity — never more — and issues the
   managed device and, for technicians, the maintenance tablet, recording the assets in the
   inventory (POL-CLS CLS-1).
3. On the first day the person verifies their identity (STD-AUTH AUTH-6), sets their credentials,
   enrols multi-factor authentication, completes the onboarding security training and
   acknowledges POL-AUP; the account is activated only when the training platform confirms
   completion (POL-HR HR-5).
4. Access beyond the role bundle is requested by the line manager through the ACCESS queue and
   approved by the system owner (POL-ACC ACC-3); privileged access additionally requires a
   separate administrative identity and phishing-resistant factors (STD-AUTH AUTH-9).

### 2. Mover

1. The line manager notifies HR on the day a change of role or entity is decided; HR updates the
   record, and the ticket system opens a mover ticket for the IT Operations Lead.
2. Within five working days of the effective date (POL-ACC ACC-5) the IT Operations Lead applies
   the new role bundle, removes the rights the new role does not require, re-points managed
   devices and mailbox memberships and records the changes; the old and the new line manager
   confirm the result in the ticket. Assets not needed in the new role are returned (stage 3.3).
3. For moves between entities the Country Manager Germany or the Site Lead Brno confirms the
   local requirements (works council, local training modules).

### 3. Leaver

1. HR notifies the IT Operations Lead and the Facilities & Physical Security Lead on the day a
   departure is decided, with the last working day and whether the departure is involuntary; for
   subcontractor technicians the Country Manager Germany notifies the end of the engagement.
2. The IT Operations Lead disables all accounts, tokens, keys, VPN, software-as-a-service access
   and device certificates by the end of the last working day — immediately on notification for
   involuntary departures (POL-ACC ACC-6) — revokes active sessions and rotates any shared secret
   the person knew (POL-CRYP CRYP-8).
3. Assets are returned and recorded before the last working day: laptop, phone, tablet, tokens,
   badges, locker keys and master keys, tools, spare parts, documents and media (A.5.11). The line
   manager confirms completeness, the Facilities & Physical Security Lead checks keys against the
   key register, and missing items are reported under POL-IR.
4. The mailbox and the personal drive are transferred to the line manager for 90 days and then
   deleted under the records schedule (POL-LEG LEG-6). The HR Manager holds the exit conversation,
   hands over the written reminder of continuing confidentiality and post-employment
   responsibilities (A.6.5; POL-HR HR-12) and records it.
5. Subcontractor technicians: the Country Manager Germany confirms the removal of the
   technician's maintenance-tooling account and the return of issued equipment within one working
   day of the engagement ending.

### 4. Identity management rules (A.5.16)

1. Every identity is unique and traceable to one person, role or device; naming follows the
   convention of the identity provider; shared accounts are prohibited except the break-glass
   accounts of POL-ACC ACC-13.
2. Service accounts are requested by the owning role with purpose and scope, created with
   vault-managed secrets (STD-AUTH AUTH-3), covered by the owner's access review and disabled
   when the service is retired; device identities follow POL-CRYP CRYP-11.
3. Disabled identities are kept for 90 days for forensic and audit purposes and then deleted,
   except under legal hold; a returning person receives a new identity with a fresh review of
   rights, never a reactivated one.

### 5. Periodic access reviews (A.5.18)

1. The IT Operations Lead prepares the review packs from the identity provider and the system
   owners attest them: privileged access quarterly, all other access semi-annually (POL-ACC
   ACC-7). Every deviation is corrected within ten working days and the attestation recorded in
   project ISMS-AR; rights without a documented approval are removed, never legitimised
   retrospectively.

## Records

| Record | Where it is kept | Retention | Owner |
| --- | --- | --- | --- |
| Joiner, mover and leaver tickets | Ticket system, queue ACCESS | 3 years | IT Operations Lead |
| Access requests and approvals | Ticket system, queue ACCESS | 3 years after removal of the right | System owners |
| Asset issue and return records | Inventory and the key register | Life of the asset plus 1 year | IT Operations Lead; Facilities & Physical Security Lead |
| Training and acknowledgement confirmations | Training platform | Duration of employment plus 3 years | HR Manager |
| Access review attestations | Ticket system, project ISMS-AR | 3 years | System owners |
| Exit records and confidentiality reminders | HR system | Per the employee records schedule | HR Manager |

## Related documents

- POL-ACC — Access Control Policy
- POL-HR — HR Security & Awareness Policy
- POL-CLS — Asset Management and Information Classification Policy
