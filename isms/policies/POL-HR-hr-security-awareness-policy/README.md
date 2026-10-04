---
id: POL-HR
title: HR Security & Awareness Policy
type: policy
status: approved
version: 1.4.0
classification: internal
owner: hr-manager
approver: isms-manager
effective_date: &id001 2025-09-15
last_reviewed: *id001
review_cycle: P1Y
next_review: 2026-09-15
controls:
- A.6.1
- A.6.2
- A.6.3
- A.6.4
- A.6.5
- A.6.6
clauses:
- '7.2'
- '7.3'
applies_to:
- all
related:
- POL-AUP
- POL-ACC
- PROC-JML
- POL-LEG
- POL-ISMS
supersedes: []
language: en
tags:
- people
- awareness
- training
---

# POL-HR — HR Security & Awareness Policy

## Purpose

People operate the lockers, write the firmware, administer the platform and receive the phishing
emails. This policy covers information security across the employment life cycle — before,
during and after — and the awareness and training that give everyone the competence their role
needs (clauses 7.2 and 7.3). It treats risk R-005.

## Scope

All employees, apprentices, temporary staff, contractors and field-service subcontractor
technicians working for any in-scope entity, and the managers responsible for them.

## Policy statements

### Screening (A.6.1)

- **HR-1** Before employment or engagement, candidates shall be screened in proportion to the role
  and within the limits of the labour and privacy law of the entity's country (legal register
  LEG-06): identity and right to work for everyone; references and qualifications for all
  employees; and, where local law permits, a criminal-record certificate for roles with
  privileged access to production systems, access to customer personal data, firmware signing
  rights or field access to lockers.
- **HR-2** Subcontractor technicians and agency staff shall be screened by their employer to at
  least the same standard, confirmed in writing under POL-SUP before access is granted.

### Terms and conditions (A.6.2) and confidentiality (A.6.6)

- **HR-3** Contracts of employment and engagement shall state the person's information security
  responsibilities, the obligation to follow the ISMS policies, the consequences of breaches and a
  confidentiality clause covering PaketPort, customer, carrier and site-host information that
  survives the end of the engagement. Contractors, suppliers' staff and visitors to secure areas
  sign a confidentiality agreement before access.
- **HR-4** Confidentiality agreements shall be reviewed by the Data Protection Officer and legal
  counsel every two years and whenever the law or the business changes.

### Awareness, education and training (A.6.3)

- **HR-5** Nobody shall receive access to PaketPort systems before completing the onboarding
  security training and acknowledging POL-AUP. All staff and technicians complete the annual
  refresher, and completion stays at or above 98 % at any time (POL-ISMS ISMS-2).
- **HR-6** Training shall be role-based:

| Audience | Additional content | Frequency |
| --- | --- | --- |
| All staff | Policies, classification, phishing, passwords and multi-factor authentication, incident reporting, clear desk, remote work | Onboarding and annually |
| Field technicians and subcontractors | Recognising locker tampering, physical security of sites, handling of keys, tablets and spare parts, reporting from the field | Onboarding and annually, plus a practical module |
| Developers | Secure coding, dependency and secrets handling, threat modelling, Cyber Resilience Act duties | Onboarding and annually |
| Platform and IT operations | Hardening baselines, privileged-access rules, logging, incident playbooks | Onboarding and annually |
| Managers | Their responsibilities under POL-ORG; handling reports and violations | Annually |
| Management body | NIS2 governance duties, risk appetite, incident reporting obligations | Annually |

- **HR-7** Training ends with a quiz; the pass mark is 80 % with two retries before a conversation
  with the line manager. Phishing simulations run at least quarterly; people who click receive
  short targeted training, never public blame.
- **HR-8** The HR Manager shall track completion per person and entity. Staff more than 30 days
  overdue have their access suspended by the IT Operations Lead until completion, and overdue
  rates are reported to the Security Steering Committee.
- **HR-9** Awareness shall be kept alive between trainings through a monthly communication
  (lessons from incidents, new threats, reminders), and the effectiveness of the programme is
  measured through phishing click and report rates, quiz results and reporting behaviour.

### Disciplinary process (A.6.4)

- **HR-10** Breaches of the ISMS policies shall be handled through a fair, graded and documented
  process — from a documented conversation and retraining through written warnings to, for
  serious or repeated breaches, termination — in line with employment law, with the works council
  at PaketPort Deutschland GmbH involved where required and the Information Security Officer /
  ISMS Manager consulted on the security facts. Reporting an event in good faith is never a
  disciplinary matter.

### Change and termination (A.6.5)

- **HR-11** On a change of role or entity, the HR Manager shall trigger the mover steps of
  PROC-JML so that access, assets and training are adjusted within five working days; on
  termination, the leaver steps so that access ends by the last working day — immediately for
  involuntary terminations — and all assets are returned.
- **HR-12** Leavers shall be reminded in writing of their continuing confidentiality obligations,
  of the duty to return or destroy PaketPort information and of the contact for questions;
  knowledge of critical processes is handed over before departure.

### Competence (clause 7.2)

- **HR-13** Competence requirements for roles with security responsibilities — the ISMS,
  platform, security engineering, development, internal audit — shall be recorded in the role
  profiles. Competence is built through qualification, experience and training, and records of
  training and certifications are kept in the HR system.

## Roles and responsibilities

| Role | Responsibility |
| --- | --- |
| HR Manager | Owns this policy; screening, contracts, training tracking, the disciplinary process and the joiner, mover and leaver triggers |
| Information Security Officer / ISMS Manager | Training content and phishing simulations; consulted on breaches; trains the management body |
| Line managers | Ensure completion, hold the conversations, notify HR of changes and departures on the day they are decided |
| IT Operations Lead | Suspends access for overdue training; removes leaver access under PROC-JML |
| Country Manager Germany; Site Lead Brno | Apply the policy within national law; coordinate with the works council |
| Data Protection Officer | Reviews confidentiality agreements and the lawfulness of screening |

## Compliance and exceptions

Compliance is monitored through training completion and quiz results per entity, phishing click
and report rates, screening records and the log of disciplinary cases. Exceptions — for example
an urgently needed contractor who starts before screening is complete — shall be requested through
a control exception request, approved by the HR Manager and the Information Security Officer /
ISMS Manager, limited to restricted access and at most twelve months, and recorded in the
exception register.

## Related documents

- POL-AUP — Acceptable Use Policy
- POL-ACC — Access Control Policy
- PROC-JML — Joiner, Mover and Leaver Access Procedure
- POL-LEG — Legal, Regulatory and Privacy Compliance Policy
- POL-ISMS — Information Security Policy
