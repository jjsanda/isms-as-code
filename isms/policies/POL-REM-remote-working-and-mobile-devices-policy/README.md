---
id: POL-REM
title: Remote Working and Mobile Devices Policy
type: policy
status: in-review
version: 0.3.0
classification: internal
owner: it-operations-lead
approver: isms-manager
review_cycle: P1Y
controls:
- A.6.7
- A.7.9
- A.8.1
clauses: []
applies_to:
- all
related:
- POL-AUP
- POL-ACC
- POL-PHY
supersedes: []
language: en
tags:
- remote-work
- mobile
---

# POL-REM — Remote Working and Mobile Devices Policy

> **In review.** Version 0.3.0 is under review by the owner and the approver. Until it is
> approved, the remote-working and device rules of POL-AUP apply.

## Purpose

Office staff work from home for part of the week, developers travel between Vienna and Brno, and
field technicians work entirely out of vehicles with tablets, tools, spare parts and locker keys.
This policy sets the rules for working outside PaketPort premises and for the mobile devices and
assets involved, so that information stays protected wherever the work happens.

## Scope

All staff and contractors of the in-scope entities who work outside PaketPort premises or carry
PaketPort devices and assets: home offices, travel, co-working spaces, carrier and site-host
premises and field-service vehicles. It complements POL-AUP (general use), POL-ACC (access) and
POL-PHY (assets off-premises).

## Policy statements

### Remote working (A.6.7)

- **REM-1** Remote working is permitted for roles approved by the line manager. Tasks involving
  restricted information — firmware signing, HR and payroll, incident forensics — are performed
  only from PaketPort premises or through the bastion with session recording.
- **REM-2** Remote work shall use the managed device and the zero-trust gateway or VPN with
  multi-factor authentication (POL-ACC ACC-8); split tunnelling to corporate resources is
  disabled, and public or hotel networks are used only through the VPN.
- **REM-3** The workspace shall be private: screens not visible to others, calls about
  confidential matters held where nobody can overhear, the device locked when unattended and
  stored out of sight, no printing of confidential information outside the office, and household
  members never using the device.
- **REM-4** Working from a country other than that of the employing entity for more than ten
  working days a year requires the approval of the HR Manager and the Information Security
  Officer / ISMS Manager because of tax, labour-law and export considerations; working from a
  country listed as high-risk in the legal register requires a loaner device and a pre-travel
  briefing.

### Mobile devices (A.8.1)

- **REM-5** Laptops, phones and tablets used for PaketPort work shall be enrolled in device
  management, encrypted, protected by a screen lock and multi-factor authentication, kept updated
  and capable of remote wipe. Local data is limited to what the task needs and is synchronised to
  PaketPort storage.
- **REM-6** Personal devices shall not hold PaketPort data, with the single exception of personal
  phones enrolled in mobile device management for email and calendar (POL-AUP AUP-6); the managed
  container may be wiped by the IT Operations Lead on loss or departure.
- **REM-7** Loss or theft of a device shall be reported within two hours (POL-AUP AUP-5). The IT
  Operations Lead wipes the device, revokes its certificates and tokens and records the event
  under POL-IR.

### Assets off-premises and field service (A.7.9)

- **REM-8** Field technicians shall keep tablets, tools, spare parts and locker keys under
  personal control or locked in the vehicle's secured compartment during the working day and
  shall never leave them in a vehicle overnight. Master keys are signed out and back in at the
  depot or the Munich store on the same day.
- **REM-9** Locker units and controllers in transit travel in tamper-evident packaging with a
  handover record (POL-CLS CLS-9) and are never stored at a technician's home.
- **REM-10** Travelling staff shall carry devices as hand luggage, use privacy screens, avoid
  working on confidential matters in public and shall not connect unknown USB devices or
  chargers to PaketPort devices.

## Roles and responsibilities

| Role | Responsibility |
| --- | --- |
| IT Operations Lead | Owns this policy; device management, remote-access tooling, loss handling |
| Line managers | Approve remote-working roles; ensure their staff have suitable equipment and know the rules |
| HR Manager | Approves cross-border working together with the Information Security Officer / ISMS Manager |
| Country Manager Germany | Applies the field-service rules to the German technicians and subcontractors |
| Facilities & Physical Security Lead | Key sign-out at the depot and the Munich store |
| All remote and mobile workers | Follow the rules and report losses |

## Compliance and exceptions

Compliance is monitored through device-management compliance reports, VPN and gateway
statistics, loss reports and the key sign-out records. Exceptions follow the control exception
request, approved by the IT Operations Lead and the Information Security Officer / ISMS Manager,
time-limited to at most twelve months and recorded in the exception register.

## Related documents

- POL-AUP — Acceptable Use Policy
- POL-ACC — Access Control Policy
- POL-PHY — Physical and Environmental Security Policy
