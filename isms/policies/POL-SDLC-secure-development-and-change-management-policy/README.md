---
id: POL-SDLC
title: Secure Development and Change Management Policy
type: policy
status: approved
version: 1.0.0
classification: internal
owner: software-engineering-lead
approver: isms-manager
effective_date: &id001 2026-03-02
last_reviewed: *id001
review_cycle: P1Y
next_review: 2027-03-02
controls:
- A.8.4
- A.8.25
- A.8.26
- A.8.27
- A.8.28
- A.8.29
- A.8.31
- A.8.32
- A.8.33
clauses:
- '6.3'
applies_to:
- all
related:
- POL-VULN
- POL-CRYP
- POL-ACC
- POL-SUP
- POL-CLS
supersedes: []
language: en
tags:
- development
- change-management
- cra
---

# POL-SDLC — Secure Development and Change Management Policy

## Purpose

PaketPort writes the firmware that runs on street-sited lockers, the backend that routes parcels
and the app customers use. A vulnerability shipped to the fleet is expensive to fix and
dangerous to leave. This policy sets the rules for building security into development from
requirements to release, for separating environments and protecting test data, for controlling
change, and for protecting source code. It treats risk R-009 and supports the product-security
duties under the Cyber Resilience Act.

## Scope

All software developed by or for the in-scope entities — locker firmware, the backend services
and APIs, the fleet-management plane, the customer app, internal tools and infrastructure as code
— in Vienna and Brno and at outsourced developers under POL-SUP, and all changes to production
systems whatever their origin.

## Policy statements

### Secure development life cycle (A.8.25)

- **SDLC-1** Development shall follow the defined life cycle with security activities at every
  phase: requirements (SDLC-2), design (SDLC-3 threat model), implementation (SDLC-4 secure
  coding), verification (SDLC-5 testing), release (SDLC-8 change and signing) and operation
  (vulnerability handling under POL-VULN). The Software Engineering Lead owns the life cycle and
  its tooling; the Security Engineer reviews it annually.

### Application security requirements (A.8.26)

- **SDLC-2** Every product and significant feature shall have documented security requirements
  derived from the classification of the data it handles (POL-CLS), the applicable legal and
  contractual requirements (POL-LEG, carrier agreements), the risk assessment (PROC-RISK) and the
  Cyber Resilience Act essential requirements for the locker product; they cover authentication,
  authorisation, input validation, cryptography (POL-CRYP), logging (POL-LOG), error handling,
  privacy by design and secure update.
- **SDLC-3** Designs of new services, of changes to the locker-backend protocol and of features
  touching personal data or payments shall be threat-modelled before implementation, and the
  identified threats tracked to mitigations or accepted risks.

### Secure architecture and engineering principles (A.8.27)

- **SDLC-4** Systems shall be designed on these principles: defence in depth; least privilege
  for services and users; secure defaults; fail secure (a locker that loses trust in the backend
  stops accepting administrative commands, not parcels); no implicit trust between locker,
  backend and app — every call authenticated and authorised; minimal attack surface; separation
  of duties in the pipeline (POL-ORG ORG-7); and designs that can be updated in the field for the
  product's support period.

### Secure coding (A.8.28)

- **SDLC-5** Code shall follow the secure coding standard maintained by the Software Engineering
  Lead for each language in use; it requires input validation, parameterised queries, safe memory
  handling in firmware, approved cryptographic libraries only, no secrets in code, and the use of
  the linters and static analysis configured in the pipeline. Every change is reviewed by a second
  developer before merge (four-eyes), and the pipeline blocks merges with critical or high static
  analysis or dependency findings.
- **SDLC-6** Third-party and open-source components shall be taken from approved registries,
  recorded in the software bill of materials, scanned for vulnerabilities and licence compliance
  (POL-LEG) on every build, and kept to supported versions under POL-VULN.

### Security testing (A.8.29)

- **SDLC-7** Before release, code shall pass static analysis, dependency scanning, automated
  security tests for authentication and authorisation, and dynamic testing of the APIs; firmware
  shall additionally pass hardware-in-the-loop tests in the Brno lab, including secure boot,
  signature verification, offline behaviour and tamper response. Internet-facing systems and the
  locker product shall be penetration-tested by an independent party at least annually and after
  major changes; findings are handled under POL-VULN.

### Separation of environments (A.8.31) and test information (A.8.33)

- **SDLC-8** Development, test, staging and production shall be separate environments with
  separate credentials, keys and network zones (POL-NET); developers have no standing access to
  production (POL-ACC ACC-10), and production data shall never be copied into non-production
  environments — tests use masked or synthetic data under POL-CLS CLS-12. Pre-production lockers
  in the Brno lab use test certificates that the production backend rejects.

### Change management (A.8.32)

- **SDLC-9** Every change to production — code, infrastructure, configuration, firmware — shall
  go through change management with a ticket, an impact and risk assessment, testing evidence, a
  rollback plan, approval and a record. Change types:

| Type | Examples | Approval |
| --- | --- | --- |
| Standard | Pre-approved, low-risk, repeatable (routine dependency updates, scaling) | Automated checks; recorded |
| Normal | Feature releases, infrastructure changes, firmware updates | Change advisory review: Head of Platform & SRE and Software Engineering Lead, security review for changes affecting controls |
| Emergency | Security patches, incident containment | Head of Platform & SRE, reviewed retrospectively within five working days |

- **SDLC-10** Firmware shall reach lockers only as signed images through the fleet-management
  plane in a staged roll-out: a canary group of at least 1 % of the estate for 24 hours, then
  10 %, then the fleet, with automatic halt and rollback on elevated failure rates; emergency
  updates may shorten the stages with the Head of Platform & SRE's approval.
- **SDLC-11** Releases of backend services and the app shall be built, signed and deployed by the
  pipeline from the release branch; manual deployments to production are prohibited outside
  emergency changes.

### Access to source code (A.8.4)

- **SDLC-12** Source code is classified confidential (POL-CLS). Repository access follows
  POL-ACC: read access for developers of the entity's products, write access through reviewed
  pull requests only, protected release branches, signed commits and tags, and release and
  signing rights restricted to the release role (POL-ACC ACC-16). Access is reviewed
  semi-annually and removed through PROC-JML.

### Outsourced development and product duties

- **SDLC-13** Outsourced development shall meet this policy through the contract terms of POL-SUP
  SUP-14. For the locker product, the Software Engineering Lead maintains the technical
  documentation, the bill of materials and the vulnerability-handling process required by the
  Cyber Resilience Act, and coordinates disclosure and reporting with POL-VULN and PROC-IR.

## Roles and responsibilities

| Role | Responsibility |
| --- | --- |
| Software Engineering Lead | Owns this policy, the life cycle, the coding standard, the pipeline controls and source-code access |
| Head of Platform & SRE | Change advisory, production deployments, staged OTA roll-out, emergency changes |
| Security Engineer | Threat-model and design reviews, penetration-test coordination, annual life-cycle review |
| Site Lead Brno | Hardware-in-the-loop testing and the lab's test certificates |
| Developers | Follow the coding standard, review each other's code, keep secrets out of code |
| Information Security Officer / ISMS Manager | Security gates for projects under POL-ORG ORG-12; exception approval |

## Compliance and exceptions

Compliance is monitored through pipeline metrics (blocked merges, open findings by severity,
review coverage), change records, penetration-test reports and the staged roll-out statistics.
Exceptions — for example merging with an open high finding under a documented risk acceptance —
shall be requested through a control exception request, approved by the Software Engineering
Lead and the Information Security Officer / ISMS Manager, time-limited to at most twelve months
and recorded in the exception register.

## Related documents

- POL-VULN — Vulnerability & Configuration Management Policy
- POL-CRYP — Cryptography Policy
- POL-ACC — Access Control Policy
- POL-SUP — Supplier & Cloud Security Policy
- POL-CLS — Asset Management and Information Classification Policy
