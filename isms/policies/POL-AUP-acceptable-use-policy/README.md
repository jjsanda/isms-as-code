---
id: POL-AUP
title: Acceptable Use Policy
type: policy
status: approved
version: 1.2.0
classification: internal
owner: it-operations-lead
approver: isms-manager
effective_date: &id001 2026-03-10
last_reviewed: *id001
review_cycle: P1Y
next_review: 2027-03-10
controls:
- A.5.10
- A.5.14
- A.6.7
- A.7.7
- A.8.1
- A.8.19
- A.8.23
clauses: []
applies_to:
- all
related:
- POL-CLS
- POL-REM
- POL-HR
- POL-IR
- POL-ACC
- POL-EMAIL
supersedes:
- POL-EMAIL
language: en
tags:
- acceptable-use
- endpoints
---

# POL-AUP — Acceptable Use Policy

## Purpose

This policy sets the rules everyone follows when using PaketPort's information, systems, devices
and communication channels, so that everyday behaviour does not undo the technical controls. Since
2026-03-10 it also contains the email, messaging and information-transfer rules that were
previously in POL-EMAIL.

## Scope

Everyone with access to PaketPort information or systems in any entity — employees, field
technicians, contractors, subcontractors and suppliers' staff — and every device, account and
channel used for PaketPort work, including managed laptops and phones, the maintenance tooling
used in the field and the lab equipment in Brno. Remote working is covered here at the level
needed until POL-REM is approved; POL-REM will then take precedence for remote and mobile work.

## Policy statements

### General rules (A.5.10)

- **AUP-1** PaketPort information and systems shall be used for PaketPort's business. Limited
  personal use of the internet, email and phone is permitted as long as it does not interfere with
  work, create cost or risk, or breach a policy. Any personal use of customer or carrier data is
  prohibited.
- **AUP-2** Everyone shall handle information according to its classification under POL-CLS, use
  only the accounts and access granted under POL-ACC, and shall never circumvent a security
  control, test the security of a system without written authorisation from the Information
  Security Officer / ISMS Manager, or access lockers, devices or data they are not assigned to.
- **AUP-3** The following are prohibited: sharing credentials or one-time codes; storing
  PaketPort data in personal cloud, email or messaging accounts; connecting unmanaged devices to
  the office or production networks; installing or running software not approved under AUP-9;
  disabling or tampering with security tools; and using PaketPort systems for unlawful, offensive
  or harassing content.

### Endpoint devices (A.8.1)

- **AUP-4** Work shall be done on devices issued and managed by the IT Operations Lead. Devices
  keep full-disk encryption, automatic updates, endpoint protection and the five-minute screen lock
  enabled; users do not hold local administrator rights; devices are restarted for updates within
  three days of being prompted.
- **AUP-5** Loss or theft of a device, token, locker key or maintenance tool shall be reported to
  the IT Operations Lead and to the security mailbox within two hours of discovery so that the
  device can be wiped and access revoked.
- **AUP-6** Personal devices shall not hold PaketPort data, with one exception: personal phones
  enrolled in mobile device management may be used for email and calendar. Field technicians use
  the maintenance tablets issued to them for all work on lockers.

### Clear desk and clear screen (A.7.7)

- **AUP-7** Screens shall be locked whenever a device is left, even briefly. Confidential and
  restricted information on paper or media shall be locked away when not in use and never left on
  desks, on printers, in vehicles or in the open areas of the Vienna depot; printouts are collected
  immediately and disposed of in the shredding bins.

### Remote working (A.6.7)

- **AUP-8** Remote work shall use the managed device, the zero-trust gateway or VPN with
  multi-factor authentication and a private, lockable workspace. Confidential information shall
  not be printed at home or discussed where others can overhear; public and hotel networks may be
  used only through the VPN.

### Software installation (A.8.19)

- **AUP-9** Software shall be installed only from the catalogue maintained by the IT Operations
  Lead. Requests for new software go through the ticket system and are assessed for licensing
  (POL-LEG) and security before approval; browser extensions, scripts and tools downloaded from
  the internet count as software.
- **AUP-10** No software shall be installed on servers, lockers or the maintenance tooling outside
  the change and release processes of POL-VULN and POL-SDLC.

### Web filtering (A.8.23)

- **AUP-11** Web access from managed devices, including field-service laptops and tablets, passes
  through the web filter, which blocks malicious sites and categories not needed for work (malware
  and phishing domains, anonymisers, file-sharing, gambling, adult content). Access that is needed
  for work is requested through the ticket system; circumventing the filter is prohibited.

### Email, messaging and information transfer (A.5.14)

- **AUP-12** Only PaketPort email and the approved messaging and file-sharing tools shall be used
  for PaketPort information. Automatic forwarding to external addresses is prohibited, and private
  email or messaging accounts shall not be used for work.
- **AUP-13** Messages from outside the group are marked by the mail gateway. Unexpected
  attachments, links and requests for credentials, payments or data shall be treated with
  suspicion and reported with the report button or to the security mailbox rather than answered
  or forwarded.
- **AUP-14** Confidential information shall be sent externally only through encrypted channels:
  the secure file-transfer service, end-to-end encrypted messaging approved by the IT Operations
  Lead, or encrypted attachments with the password sent through a different channel. Restricted
  information shall not be sent by email at all. Customer and carrier data is transferred to
  carriers only through the authenticated APIs under POL-NET and to any other party only under a
  transfer agreement under POL-CLS.
- **AUP-15** Physical transfer of media and devices — spare controllers, lockers in transit,
  backup media — follows POL-CLS and POL-PHY: encrypted, tracked and handed over against signature.

### Monitoring and consequences

- **AUP-16** The use of PaketPort systems is logged and monitored in accordance with POL-LOG and,
  at PaketPort Deutschland GmbH, with the agreement concluded with the works council. Monitoring
  serves security and legal obligations, not performance assessment.
- **AUP-17** Breaches are handled under the disciplinary process of POL-HR or under the contract of
  the party concerned. Everyone shall acknowledge this policy at onboarding and again in the annual
  awareness training.

## Roles and responsibilities

| Role | Responsibility |
| --- | --- |
| IT Operations Lead | Owns this policy, the device baseline, the software catalogue and the web filter; processes loss reports and software requests |
| Information Security Officer / ISMS Manager | Authorises security testing, handles reports of violations together with HR, reviews monitoring |
| HR Manager | Onboarding acknowledgement, annual training, disciplinary process |
| Line managers | Ensure their staff follow this policy; approve work-justified web-filter exceptions |
| Country Manager Germany | Coordinates monitoring with the works council; obtains subcontractor acknowledgements |
| All users | Follow the rules, report losses and suspicious messages |

## Compliance and exceptions

Compliance is monitored through endpoint compliance reports (encryption, patch level, protection
enabled), web-filter and mail-gateway statistics, phishing-simulation results under POL-HR and the
annual acknowledgement rate. Exceptions — for example a developer workstation with local
administrator rights or a tool outside the catalogue — shall be requested through a control
exception request, approved by the IT Operations Lead and the Information Security Officer / ISMS
Manager, time-limited to at most twelve months and recorded in the exception register.

## Related documents

- POL-CLS — Asset Management and Information Classification Policy
- POL-REM — Remote Working and Mobile Devices Policy
- POL-HR — HR Security & Awareness Policy
- POL-IR — Information Security Incident Response Policy
- POL-ACC — Access Control Policy
- POL-EMAIL — Email Security Policy
