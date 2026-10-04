---
id: POL-IR
title: Information Security Incident Response Policy
type: policy
status: approved
version: 1.2.0
classification: internal
owner: isms-manager
approver: managing-director
effective_date: &id001 2025-11-01
last_reviewed: *id001
review_cycle: P1Y
next_review: 2026-11-01
controls:
- A.5.7
- A.5.24
- A.5.25
- A.5.26
- A.5.27
- A.5.28
- A.6.8
clauses: []
applies_to:
- all
related:
- PROC-IR
- POL-LOG
- POL-BC
- POL-LEG
- POL-ORG
supersedes: []
language: en
tags:
- incidents
- nis2
---

# POL-IR — Information Security Incident Response Policy

## Purpose

Street-sited lockers and an internet-facing platform will have incidents; what matters is that
PaketPort detects them quickly, responds in a controlled way, meets its reporting duties under
NIS2, the GDPR and its contracts, and learns from every one. This policy sets the rules for
preparing for, reporting, assessing, responding to and learning from information security events
and incidents, and for the threat intelligence that feeds preparation. It treats risks R-002,
R-008 and R-012; PROC-IR is the step-by-step procedure.

## Scope

All entities; all staff, technicians, contractors and suppliers with access; all systems and
sites in scope; and every event that may affect the confidentiality, integrity or availability of
PaketPort information or the locker service — including events at suppliers and carriers that
affect PaketPort.

## Policy statements

### Definitions and severity

- **IR-1** An *event* is any observation that may indicate a security problem: an alert, a tamper
  signal, a suspicious email, a lost device. An *incident* is an event assessed as compromising,
  or likely to compromise, the confidentiality, integrity or availability of PaketPort information
  or services. A *significant incident* in the sense of NIS2 is one that has caused or can cause
  severe operational disruption or financial loss to PaketPort, or has affected or can affect
  other persons by causing considerable material or non-material damage. A *personal-data breach*
  is an incident affecting personal data as defined in the GDPR.
- **IR-2** Incidents shall be classified at triage and re-assessed while they are handled:

| Severity | Definition | PaketPort examples | Response start | Status updates |
| --- | --- | --- | --- | --- |
| S1 — critical | Significant incident; service-wide impact; personal data of many customers; key compromise | Fleet-wide locker compromise, firmware signing key compromise, breach of the customer database, ransomware in production | 30 minutes, 24/7 | Every 2 hours |
| S2 — high | Serious impact on one entity, region or system; limited personal data | Attack-induced outage of a backend region, leaked carrier API credential, malware on a field-service laptop with production access | 1 hour, 24/7 | Every 4 hours |
| S3 — medium | Contained impact; no personal data; no service impact | Single locker tamper without data loss, policy violation by a user, successful phishing without further access | Next working day | Daily |
| S4 — low | Event without impact | Reported phishing email, scanner noise, lost badge recovered | Within 3 working days | At closure |

### Preparation (A.5.24)

- **IR-3** The Information Security Officer / ISMS Manager shall maintain the incident response
  capability: the roles (incident manager, response team from platform, security and IT
  operations, communications lead, Data Protection Officer, legal counsel), a 24/7 on-call rota
  for S1 and S2, playbooks for the main scenarios (locker compromise, backend intrusion,
  personal-data breach, ransomware, denial of service, lost device, insider misuse, supplier
  incident), contact lists for authorities, carriers, the insurer and suppliers, and the tooling
  (ticket project INC, war-room channel, forensic toolkit, out-of-band communication).
- **IR-4** Tabletop exercises shall be held at least twice a year, one rehearsing the NIS2
  reporting clock and one including PaketPort Deutschland GmbH; playbooks are reviewed after
  every S1 or S2 incident and after every exercise.
- **IR-5** Detection relies on the logging and monitoring under POL-LOG, including alerts from
  the fleet-management plane (tamper, unexpected reboots, failed signature checks), the cloud
  platform, endpoint protection and the mail gateway.

### Reporting of events (A.6.8)

- **IR-6** Everyone shall report suspected events immediately — within one hour of noticing —
  through the security mailbox, the 24/7 hotline or the ticket form, without investigating
  themselves and without fear of blame for a report made in good faith, including reports of
  their own mistakes. Suppliers and carriers report through the channels in their contracts.
- **IR-7** Field technicians shall report tamper signs, damaged enclosures and suspicious
  behaviour at locker sites through the maintenance tablet immediately and before continuing work.

### Assessment and decision (A.5.25)

- **IR-8** Every reported event shall be triaged by the on-call responder within 30 minutes for a
  suspected S1, one hour for a suspected S2 and one working day otherwise. The responder decides
  whether it is an incident, assigns the severity, applies the NIS2 significance test and — with
  the Data Protection Officer — the personal-data test, and records the decision with reasons in
  the ticket.

### Response (A.5.26)

- **IR-9** Incidents shall be handled by an incident manager following the playbooks: contain
  (isolate lockers through the fleet-management plane, block accounts and credentials, segment
  networks), eradicate, recover under POL-BC, and verify before declaring closure. Only the
  incident manager may authorise actions that affect the service, such as taking lockers or the
  API offline.
- **IR-10** Regulatory and contractual reporting shall follow PROC-IR: an early warning to the
  competent authority or CSIRT within 24 hours of becoming aware of a significant incident, a
  notification within 72 hours and a final report within one month; the supervisory authority
  within 72 hours of becoming aware of a personal-data breach and the data subjects where the
  risk to them is high; carriers within 24 hours of confirming impact on them; the insurer as its
  policy conditions require. The reporting clock starts when PaketPort becomes aware, not when
  the analysis is complete.
- **IR-11** Communication with customers, site hosts, the public and the press shall be approved
  by the Managing Director; authorities are addressed only by the roles named in POL-ORG ORG-10.

### Evidence (A.5.28)

- **IR-12** Evidence shall be collected and preserved so that it can be relied on in regulatory,
  contractual or criminal proceedings: logs exported from the central log store, forensic images
  of affected systems and locker controllers, screenshots and timelines, each with a
  chain-of-custody record naming who collected what, when and how. Evidence is classified
  restricted, stored in the incident evidence store and retained for at least three years after
  closure, longer under legal hold.

### Learning (A.5.27)

- **IR-13** Every S1 and S2 incident, and every S3 incident with a lesson in it, shall have a
  post-incident review within ten working days of closure covering the timeline, the root cause,
  what worked, what did not, and the actions. Actions are tracked under PROC-CAPA, changes to
  controls flow into the risk register under PROC-RISK, and lessons are shared with all three
  entities through the monthly awareness communication.
- **IR-14** Incident statistics — numbers by severity, time to detect, time to contain, reporting
  deadlines met — shall be reported quarterly to the Security Steering Committee and annually to
  the management review.

### Threat intelligence (A.5.7)

- **IR-15** The Security Engineer shall collect threat intelligence from the national CSIRT,
  sector associations, supplier advisories, the vulnerability feeds under POL-VULN and
  PaketPort's own incidents; triage it weekly for relevance to lockers, the backend, the app and
  staff; turn relevant items into detection rules, vulnerability priorities, awareness content or
  risk updates; and share sanitised observations with the CSIRT community and carriers where that
  helps others.

## Roles and responsibilities

| Role | Responsibility |
| --- | --- |
| Information Security Officer / ISMS Manager | Owns this policy, the playbooks and the on-call rota; incident manager for S1 and S2; regulatory reporting |
| Head of Platform & SRE | Technical response for backend and fleet; containment; recovery under POL-BC |
| Security Engineer | Detection engineering, forensics, threat intelligence |
| IT Operations Lead | Response for corporate systems and endpoints; account and device containment |
| Data Protection Officer | Personal-data breach assessment and notification |
| Country Manager Germany; Site Lead Brno | Local response coordination and the national reporting hand-off under PROC-IR |
| Managing Director | Approves external communication; informed of every S1 within one hour |
| All staff, technicians and suppliers | Report events immediately |

## Compliance and exceptions

Compliance is monitored through the statistics in IR-14, the exercise records, the share of
events triaged within the IR-8 deadlines and the share of significant incidents reported within
the statutory deadlines (target 100 %, POL-ISMS ISMS-2). No exceptions are granted to the
reporting duties. Exceptions to other statements follow the control exception request, approved
by the Information Security Officer / ISMS Manager and the Managing Director, time-limited to at
most twelve months and recorded in the exception register.

## Related documents

- PROC-IR — Incident Response and NIS2 Reporting Procedure
- POL-LOG — Logging and Monitoring Policy
- POL-BC — Business Continuity & Backup Policy
- POL-LEG — Legal, Regulatory and Privacy Compliance Policy
- POL-ORG — Information Security Roles and Governance Policy
