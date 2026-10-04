---
id: POL-SUP
title: Supplier & Cloud Security Policy
type: policy
status: approved
version: 1.1.0
classification: internal
owner: head-of-procurement
approver: isms-manager
effective_date: &id001 2025-12-01
last_reviewed: *id001
review_cycle: P1Y
next_review: 2026-12-01
controls:
- A.5.19
- A.5.20
- A.5.21
- A.5.22
- A.5.23
- A.8.30
clauses: []
applies_to:
- all
related:
- POL-ACC
- POL-IR
- POL-SDLC
- POL-LEG
- PROC-JML
supersedes: []
language: en
tags:
- suppliers
- cloud
- supply-chain
---

# POL-SUP — Supplier & Cloud Security Policy

## Purpose

PaketPort's service depends on parties it does not control: the cloud provider that hosts the
backend, the carriers that exchange handover data, the manufacturer of the locker hardware,
software and software-as-a-service suppliers, and the field-service subcontractors in Germany.
This policy defines how information security is addressed in these relationships — before a
contract is signed, in the agreement, through the supply chain, during the relationship and when
it ends — and treats risk R-006.

## Scope

All suppliers, partners and service providers with access to PaketPort information or systems,
or whose products or services form part of the locker service, for all entities in scope. The
reseller joint venture PaketPort Italia S.r.l. is treated as a supplier-type third party under
this policy.

## Policy statements

### Supplier categories and tiers (A.5.19)

- **SUP-1** Suppliers shall be recorded in the supplier register with an owner role and a tier:

| Tier | Criteria | Examples |
| --- | --- | --- |
| 1 — critical | Access to confidential or restricted data, or the service cannot operate without them | Cloud provider, carrier partners, locker hardware manufacturer, identity provider |
| 2 — significant | Access to internal data or systems, or supports a key process | Software-as-a-service tools, field-service subcontractors, payment service provider, connectivity providers |
| 3 — standard | No access to PaketPort data or systems | Office supplies, agencies working without PaketPort data |

- **SUP-2** Before a tier 1 or tier 2 supplier is onboarded, the Head of Procurement shall obtain a
  security assessment proportionate to the tier: for tier 1 a review of certifications or
  assurance reports, a questionnaire and — where production access is involved — a technical
  review by the Security Engineer; for tier 2 a questionnaire and evidence of basic controls. The
  Information Security Officer / ISMS Manager approves tier 1 onboarding; the Data Protection
  Officer is consulted wherever personal data is processed.

### Agreements (A.5.20)

- **SUP-3** Contracts with tier 1 and tier 2 suppliers shall include the information security
  annex covering: confidentiality and the handling rules of POL-CLS; access limited to what the
  service requires under POL-ACC ACC-14; notification of security incidents affecting PaketPort
  within 24 hours of the supplier becoming aware; the right to audit or to receive assurance
  reports; approval of sub-processors and subcontractors; return and deletion of data at contract
  end; personnel vetting and training; vulnerability disclosure and patching commitments; a
  software bill of materials for delivered software and firmware components; and data-processing
  terms under POL-LEG where personal data is involved.
- **SUP-4** Carrier agreements shall additionally specify the API security requirements of
  POL-NET, availability commitments and the mutual incident-notification duties recorded in the
  legal register (LEG-05).

### ICT supply chain (A.5.21)

- **SUP-5** Hardware and software components built into lockers or the backend shall come with
  provenance information and a software bill of materials. The Software Engineering Lead reviews
  the bill of materials for known vulnerabilities and licence conflicts before acceptance and at
  each release under POL-VULN and POL-SDLC.
- **SUP-6** Locker controllers and spare parts shall be delivered to the Vienna depot or the
  Munich store in tamper-evident packaging, checked against the order and the manufacturer's
  shipment record, and provisioned with PaketPort firmware and certificates before use. Devices
  showing signs of tampering are quarantined and reported under POL-IR.
- **SUP-7** Component suppliers shall commit to security updates for the support period of the
  locker generation and to coordinated vulnerability disclosure, in line with the Cyber
  Resilience Act obligations tracked in the legal register.

### Monitoring, review and change (A.5.22)

- **SUP-8** Tier 1 suppliers shall be reviewed at least annually and tier 2 suppliers at least
  every two years by the supplier owner together with the Head of Procurement: current assurance
  reports and certificates, incidents and service-level performance, changes to the service, its
  sub-processors or its ownership, and open findings. Results are recorded in the supplier
  register and reported to the Security Steering Committee.
- **SUP-9** Suppliers shall notify PaketPort of material changes to their service, security
  posture, sub-processors or location of processing before they take effect. The supplier owner
  assesses the change under PROC-RISK and may require a new assessment.
- **SUP-10** Field-service subcontractors of PaketPort Deutschland GmbH shall be sponsored by the
  Country Manager Germany, hold personal accounts on the maintenance tooling only (POL-ACC
  ACC-14), complete the technician training under POL-HR and be reviewed every twelve months.
  Their access is removed through PROC-JML when the engagement ends.

### Cloud services (A.5.23)

- **SUP-11** Cloud services shall be selected against documented criteria: certifications and
  assurance reports covering the service, EU data location, contractual security and
  data-processing terms, exit and portability options, and support for PaketPort's requirements
  (encryption with customer-managed keys, logging, identity integration).
- **SUP-12** For every cloud service the shared-responsibility matrix shall be recorded: what the
  provider secures and what PaketPort must configure and operate. PaketPort's part — identities,
  keys, network configuration, hardening baselines, logging — is implemented under POL-ACC,
  POL-CRYP, POL-NET, POL-VULN and POL-LOG and checked by configuration-drift monitoring.
- **SUP-13** An exit plan shall exist for every tier 1 cloud service: export format and
  procedure, alternative hosting options and the time needed to move. It is confirmed at the
  annual supplier review.

### Outsourced development (A.8.30)

- **SUP-14** Where development is outsourced — for example parts of the customer app — the
  contract shall require the secure development practices of POL-SDLC, PaketPort's ownership of
  the code and the build, security testing before acceptance, no production data in the
  supplier's environment, and access under POL-ACC ACC-14. Delivered code is reviewed and scanned
  before it is merged.

### Ending a relationship

- **SUP-15** At the end of a contract the supplier owner shall confirm the removal of all access,
  the return or deletion of PaketPort data with written confirmation, the return of equipment and
  keys, and the update of the supplier register and of the inventory under POL-CLS.

## Roles and responsibilities

| Role | Responsibility |
| --- | --- |
| Head of Procurement | Owns this policy and the supplier register; negotiates the security annex; runs the review schedule |
| Supplier owners | Day-to-day relationship, reviews, change assessment, offboarding |
| Information Security Officer / ISMS Manager | Approves tier 1 onboarding; assesses questionnaires; reports to the steering committee |
| Security Engineer | Technical reviews; bill-of-materials and vulnerability assessment with the Software Engineering Lead |
| Head of Platform & SRE | Cloud configuration, the shared-responsibility matrix and exit plans |
| Data Protection Officer | Data-processing terms and sub-processor approval |
| Country Manager Germany | Sponsorship and review of field-service subcontractors |

## Compliance and exceptions

Compliance is monitored through the supplier register (every tier 1 and tier 2 supplier with a
current assessment, annex and review date), the review completion rate, supplier-related
incidents and the bill-of-materials review records. Exceptions — for example onboarding a
supplier before the annex is signed — shall be requested through a control exception request,
approved by the Head of Procurement and the Information Security Officer / ISMS Manager,
time-limited to at most twelve months and recorded in the exception register.

## Related documents

- POL-ACC — Access Control Policy
- POL-IR — Information Security Incident Response Policy
- POL-SDLC — Secure Development and Change Management Policy
- POL-LEG — Legal, Regulatory and Privacy Compliance Policy
- PROC-JML — Joiner, Mover and Leaver Access Procedure
