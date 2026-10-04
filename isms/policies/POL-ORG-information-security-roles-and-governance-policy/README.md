---
id: POL-ORG
title: Information Security Roles and Governance Policy
type: policy
status: approved
version: 1.1.0
classification: internal
owner: isms-manager
approver: managing-director
effective_date: &id001 2026-02-16
last_reviewed: *id001
review_cycle: P1Y
next_review: 2027-02-16
controls:
- A.5.2
- A.5.3
- A.5.5
- A.5.6
- A.5.8
clauses:
- '5.3'
- '7.4'
applies_to:
- all
related:
- POL-ISMS
- PROC-MR
- PROC-IR
- PROC-RISK
supersedes: []
language: en
tags:
- governance
- roles
---

# POL-ORG — Information Security Roles and Governance Policy

## Purpose

POL-ISMS makes the Managing Director accountable for information security and requires every
document, control, risk and asset to have an owner (ISMS-6). This policy defines the governance
structure that makes that work across three entities: who decides, who operates, who is
consulted, how duties are separated in a small team, who speaks to authorities and peers, and how
security is built into projects and communicated.

## Scope

All entities in scope, every role that carries information security responsibilities, every
project that changes services, systems, sites or suppliers, and all communication about
information security inside and outside the group.

## Policy statements

### Accountability and the ISMS function

- **ORG-1** The Managing Director is accountable for information security in the group, approves
  the documents listed in PROC-DOC stage 3, decides on the retention of medium and high residual
  risks under PROC-RISK, and chairs the management review.
- **ORG-2** The Information Security Officer / ISMS Manager shall report directly to the Managing
  Director, shall have the authority to stop a change, a release or a project that introduces a
  risk nobody entitled to has accepted, and shall hold a budget line for the ISMS. The role shall
  not be combined with operational responsibility for the systems it assesses.
- **ORG-3** A Security Steering Committee shall meet at least quarterly. Members: Managing
  Director (chair), Information Security Officer / ISMS Manager, Head of Platform & SRE, IT
  Operations Lead, Software Engineering Lead, Head of Procurement, HR Manager, Facilities &
  Physical Security Lead, Data Protection Officer, Country Manager Germany and Site Lead Brno. It
  reviews the risk register, the status of controls and corrective actions, incidents and audit
  results, and decides on exceptions that exceed a single owner's authority. Minutes shall be
  recorded within five working days.

### Ownership through roles (A.5.2)

- **ORG-4** Every controlled document, Annex A control, risk, information system and asset class
  shall have exactly one owner role recorded in the role register. Owners are accountable for the
  operation, review and evidence of what they own; the deputies named in the role register act
  when an owner is unavailable.
- **ORG-5** The Country Manager Germany and the Site Lead Brno are accountable for applying the
  group ISMS at their entity: they ensure that local staff and subcontractors follow the policies,
  maintain the local contacts with authorities and CSIRTs, and report local incidents, exceptions
  and significant changes to the Information Security Officer / ISMS Manager within one working day.
- **ORG-6** Line managers shall ensure that the people in their area know the policies that
  concern them, complete their training and have the access, tools and time needed to comply
  (POL-ISMS ISMS-7).

### Segregation of duties (A.5.3)

- **ORG-7** The following duties shall be performed by different people and, where the platform
  allows, enforced technically: (a) developing a firmware or backend change and approving its
  release; (b) holding the firmware signing role and merging code into the release branch;
  (c) approving an access request and administering the account; (d) raising a change and
  approving it; (e) operating a control and auditing it; (f) administering the central log store
  and administering the systems it monitors.
- **ORG-8** Where a team is too small to separate a duty pair, the owner shall record the conflict
  in the risk register and apply compensating controls: a four-eyes review recorded in the ticket
  or pull request, privileged-session logging under POL-LOG, and a quarterly review of the
  conflicting assignments. The Information Security Officer / ISMS Manager confirms every such
  arrangement at the steering committee.

### Contact with authorities (A.5.5)

- **ORG-9** The group shall maintain current contacts, for each entity, with the NIS2 competent
  authority and national CSIRT (CERT.at for Austria), the data protection authority, the police
  cybercrime unit and the certification body, as recorded in the legal register. The Information
  Security Officer / ISMS Manager owns the Austrian and group-level contacts; the Country Manager
  Germany and the Site Lead Brno own the German and Czech contacts. Contact data shall be verified
  every six months and after every change in law.
- **ORG-10** Only the Information Security Officer / ISMS Manager, the Data Protection Officer for
  personal-data matters, the entity leads for their national authorities and the Managing Director
  shall communicate with authorities about information security. Incident reporting follows PROC-IR.

### Contact with special interest groups (A.5.6)

- **ORG-11** The Information Security Officer / ISMS Manager and the Security Engineer shall
  maintain membership of the national CSIRT community, of at least one sector association for
  postal and logistics operators and of the security advisory channels of the hardware and
  software suppliers, and shall attend at least one security conference or peer exchange per
  year. Relevant intelligence is fed into threat intelligence under POL-IR and into vulnerability
  management under POL-VULN within two working days.

### Information security in projects (A.5.8)

- **ORG-12** Every project — a locker roll-out, a new carrier integration, a new site or entity, a
  new product feature, a supplier change — shall pass a security gate at initiation
  (classification of the information involved, risk assessment per PROC-RISK, applicable legal
  and contractual requirements) and a security acceptance before go-live (requirements met,
  residual risks accepted by the role entitled to accept them, evidence filed). The project owner
  names a security contact; the Information Security Officer / ISMS Manager signs both gates.

### Communication (clause 7.4)

- **ORG-13** Information security communication shall follow this matrix:

| What | To whom | When | How | Responsible |
| --- | --- | --- | --- | --- |
| New or changed policies (MAJOR versions) | Everyone in scope | Before the effective date | Announcement, team briefings, training update | Document owner |
| Security posture, objectives, risks | Management body | Quarterly and at the management review | Steering committee pack, review minutes | Information Security Officer / ISMS Manager |
| Incidents | Staff, carriers, customers, site hosts, authorities | Per the severity and deadlines in POL-IR and PROC-IR | Incident channels, contractual and regulatory reports | Incident manager |
| Awareness content, phishing results | All staff and technicians | Monthly | Intranet, training platform | HR Manager |
| Audit and certification results | Managing Director, auditees | Within ten working days of the audit | Audit report | Internal Audit Lead |
| Security requirements for suppliers | Suppliers | At onboarding and on change | Contract annex, supplier review | Head of Procurement |

## Roles and responsibilities

| Role | Responsibility |
| --- | --- |
| Managing Director | Accountable for information security; approvals and risk retention; chairs the steering committee and the management review |
| Information Security Officer / ISMS Manager | Owns this policy, runs the ISMS, maintains the role register, signs project security gates, holds the group-level authority contacts |
| Country Manager Germany; Site Lead Brno | Apply the ISMS at their entity, own the national authority contacts, report locally arising issues |
| Heads of function | Own the documents, controls and assets of their area; enforce segregation of duties in their teams |
| Security Engineer | Participates in special interest groups and routes intelligence into the ISMS |
| Data Protection Officer | Speaks to data protection authorities; advises projects that process personal data |
| Internal Audit Lead | Independent of operations; reports audit results to the Managing Director |

## Compliance and exceptions

Compliance is monitored through the completeness of the role register (every document, control,
risk and system has an owner, which `isms validate` checks on every change), the register of
segregation-of-duties conflicts and their compensating controls, the semi-annual verification of
authority contacts, and the project gate records. Exceptions — for example a temporary
combination of conflicting duties during recruitment — shall be requested through a control
exception request, approved by the Information Security Officer / ISMS Manager and the Managing
Director, time-limited to at most twelve months and recorded in the exception register.

## Related documents

- POL-ISMS — Information Security Policy
- PROC-MR — Management Review Procedure
- PROC-IR — Incident Response and NIS2 Reporting Procedure
- PROC-RISK — Risk Assessment and Treatment Procedure
