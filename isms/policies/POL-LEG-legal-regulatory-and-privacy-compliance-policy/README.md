---
id: POL-LEG
title: Legal, Regulatory and Privacy Compliance Policy
type: policy
status: approved
version: 1.0.0
classification: internal
owner: dpo
approver: managing-director
effective_date: &id001 2026-06-01
last_reviewed: *id001
review_cycle: P1Y
next_review: 2027-06-01
controls:
- A.5.31
- A.5.32
- A.5.33
- A.5.34
clauses: []
applies_to:
- all
related:
- POL-CLS
- PROC-IR
- POL-ISMS
- PROC-MR
- POL-SUP
supersedes: []
language: en
tags:
- legal
- privacy
- nis2
- gdpr
---

# POL-LEG — Legal, Regulatory and Privacy Compliance Policy

## Purpose

PaketPort operates in three jurisdictions as a NIS2 essential entity, as a controller of
consumers' personal data and as a manufacturer of products with digital elements. This policy
defines how the group identifies and tracks its legal, regulatory and contractual obligations, how
it respects intellectual property, how it protects its records and how it protects personal
data — so that compliance is a managed process rather than a hope. It treats risk R-012 and
supports the treatment of R-009.

## Scope

All in-scope entities and every activity that creates legal, regulatory or contractual
obligations for information security: operating the locker service, processing the personal data
of customers, carriers' staff and employees, developing and selling the locker product, and
contracting with carriers, suppliers and site hosts.

## Policy statements

### Legal, statutory, regulatory and contractual requirements (A.5.31)

- **LEG-1** The group shall maintain the legal register (`isms/context/legal-register.yaml`)
  listing every requirement relevant to information security with the entities it applies to,
  the obligations it creates, an owner role, the controls and documents that implement it and a
  note of what must be verified periodically. The Data Protection Officer owns this policy; each
  requirement has its own owner.
- **LEG-2** The register shall be confirmed at every management review and updated within one
  month of a relevant change in law, contract or business — a new entity, product, market or
  processing activity. The national transpositions of NIS2 and the phased application of the
  Cyber Resilience Act are verified per entity with external counsel at least annually.
- **LEG-3** NIS2 duties shall be discharged per entity: registration with the competent authority
  and maintenance of contact data (POL-ORG ORG-9), approval of the risk-management measures and
  annual training of the management body (POL-HR HR-6), implementation of the measures through
  this ISMS, and incident reporting under PROC-IR. Contractual security obligations towards
  carriers, the insurer and the cloud provider are recorded in the register and tested by the
  internal audit programme.

### Intellectual property rights (A.5.32)

- **LEG-4** Software shall be used only under a valid licence. The IT Operations Lead maintains
  the licence inventory for corporate software and the Software Engineering Lead the open-source
  component inventory of firmware and backend with their licences. Components under licences
  incompatible with PaketPort's products, as defined in the open-source licence guideline, shall
  not be used, and licence obligations such as attribution and source availability are met in the
  product documentation.
- **LEG-5** PaketPort's own intellectual property — source code, firmware, designs, documentation
  — is classified confidential or restricted (POL-CLS) and protected accordingly; contributions to
  open-source projects require the Software Engineering Lead's approval. Copyrighted material of
  others — standards, publications, images — is acquired legitimately and not reproduced beyond
  its licence.

### Protection of records (A.5.33)

- **LEG-6** Records shall be retained, protected and disposed of according to the records schedule:

| Record type | Retention | Basis |
| --- | --- | --- |
| Customer account and parcel-event data | 13 months after the last transaction, then deleted or anonymised | Contract; GDPR storage limitation |
| Carrier handover records | 7 years | Commercial law and carrier agreements |
| Financial and tax records | 7 years, 10 where national law requires | Tax and commercial law |
| Employee records | Duration of employment plus the national statutory period | Labour and social-security law |
| Security logs | 90 days searchable, 12 months archive; incident logs closure plus 3 years | POL-LOG; NIS2 evidence |
| ISMS records (audits, reviews, risk assessments, approvals) | Life of the ISMS plus 3 years | ISO/IEC 27001 certification |
| Incident and regulatory reports | 10 years | NIS2 and GDPR accountability |
| Product technical documentation and bills of materials | 10 years after the last unit is placed on the market | Cyber Resilience Act |

- **LEG-7** Records shall be protected against loss, alteration and unauthorised access for their
  retention period — integrity through POL-LOG and POL-BC, access through POL-ACC and POL-CLS —
  and disposed of securely at its end (POL-CLS CLS-11). A legal hold suspends disposal when
  litigation or an investigation is reasonably expected.

### Privacy and protection of personal data (A.5.34)

- **LEG-8** Personal data shall be processed lawfully, fairly and transparently, for specified
  purposes, minimised, accurate, kept no longer than necessary and secured, as the GDPR requires.
  The group processes consumer data (names, contact details, addresses, parcel events, collection
  codes), carrier and site-host contact data and employee data.
- **LEG-9** The Data Protection Officer shall be independent, report directly to the Managing
  Director, be involved early in every project that processes personal data (POL-ORG ORG-12),
  maintain the records of processing of each entity and be the contact for supervisory
  authorities and data subjects.
- **LEG-10** A data protection impact assessment shall be performed before new processing that is
  likely to present a high risk — new locker features that collect data, analytics on parcel
  events, monitoring measures, new processors — and its outcome recorded and acted upon.
- **LEG-11** Processors — the cloud provider, software-as-a-service suppliers, outsourced
  developers, field-service subcontractors with data access — shall be bound by data-processing
  agreements under POL-SUP; transfers outside the EU require a safeguard approved by the Data
  Protection Officer, and data stays in the contracted EU regions (POL-SUP SUP-11).
- **LEG-12** Data-subject requests — access, rectification, erasure, portability, objection —
  shall be answered within one month through the process owned by the Data Protection Officer;
  the app and the customer-service tooling support export and deletion.
- **LEG-13** Personal-data breaches shall be assessed by the Data Protection Officer within the
  incident process and notified to the supervisory authority within 72 hours of awareness where
  required, and to the data subjects without undue delay where the risk to them is high (PROC-IR).
- **LEG-14** Privacy by design and by default shall be applied to the locker product and the app:
  data minimisation in the protocol, pseudonymous identifiers on lockers, masked data outside
  production (POL-CLS CLS-12) and retention enforced technically.

## Roles and responsibilities

| Role | Responsibility |
| --- | --- |
| Data Protection Officer | Owns this policy and the legal register process; records of processing, impact assessments, data-subject requests, breach notification, contact with data protection authorities |
| Information Security Officer / ISMS Manager | NIS2 obligations, ISMS records, coordination with the incident process |
| Managing Director | Accountable for compliance; management-body duties under NIS2 |
| Software Engineering Lead | Open-source licence inventory, product documentation, privacy by design in firmware and app |
| IT Operations Lead | Corporate licence inventory; retention enforcement in corporate systems |
| Head of Platform & SRE | Retention and deletion in production systems; log retention |
| Country Manager Germany; Site Lead Brno | Local legal requirements, registration and authority contacts with counsel |

## Compliance and exceptions

Compliance is monitored through the management-review confirmation of the legal register, the
records-schedule compliance checks, the licence inventory reviews, the data-subject request log
and its response times, the impact-assessment records and the breach notification records. No
exception is possible to a statutory obligation; exceptions to internal rules follow the control
exception request, approved by the Data Protection Officer and the Information Security
Officer / ISMS Manager, time-limited to at most twelve months and recorded in the exception
register.

## Related documents

- POL-CLS — Asset Management and Information Classification Policy
- PROC-IR — Incident Response and NIS2 Reporting Procedure
- POL-ISMS — Information Security Policy
- PROC-MR — Management Review Procedure
- POL-SUP — Supplier & Cloud Security Policy
