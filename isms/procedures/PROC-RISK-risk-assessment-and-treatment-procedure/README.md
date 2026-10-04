---
id: PROC-RISK
title: Risk Assessment and Treatment Procedure
type: procedure
status: approved
version: 1.1.0
classification: internal
owner: isms-manager
approver: managing-director
effective_date: &id001 2026-01-26
last_reviewed: *id001
review_cycle: P1Y
next_review: 2027-01-26
controls: []
clauses:
- 6.1.1
- 6.1.2
- 6.1.3
- '8.2'
- '8.3'
applies_to:
- all
related:
- POL-ISMS
- PROC-MR
- PROC-CAPA
- PROC-DOC
supersedes: []
language: en
tags:
- risk
---

# PROC-RISK — Risk Assessment and Treatment Procedure

## Purpose

This procedure defines how PaketPort identifies, analyses, evaluates and treats information
security risks, how residual risk is accepted, and how the results drive the selection of
controls and the Statement of Applicability (POL-ISMS ISMS-3 and ISMS-4; clauses 6.1 and 8.2 to
8.3). The criteria are data in `isms/risk/risk-criteria.yaml`; the register is
`isms/risk/risk-register.yaml`.

## Scope

All information security risks to the in-scope entities, services, systems and sites, including
risks arising from suppliers, products and projects, and the opportunities for improving the ISMS
that the assessment surfaces.

## Procedure

### 1. Planning and triggers

1. The Information Security Officer / ISMS Manager runs a full risk assessment once a year,
   scheduled to finish six weeks before the management review (PROC-MR), and updates the risk
   treatment plan from its results.
2. An assessment of the affected area is triggered within one month by: a new entity, site,
   service, product generation or tier 1 supplier; an S1 or S2 incident; a major change to the
   platform or the locker protocol; a new or changed requirement in the legal register; or a
   project gate under POL-ORG ORG-12.
3. Each entity is assessed explicitly: group-level risks, plus entity-specific risks for
   PaketPort Deutschland GmbH (field service, German estate, subcontractors) and PaketPort
   Software s.r.o. (lab, development). The Country Manager Germany and the Site Lead Brno take
   part in their entity's workshops.

### 2. Inputs

1. The asset inventory and classifications under POL-CLS, the scope statement and the
   interested-party requirements, the legal register, threat intelligence under POL-IR,
   vulnerability and monitoring data under POL-VULN and POL-LOG, incident and audit results,
   supplier reviews and the previous register.

### 3. Risk identification

1. Risks are identified in workshops per area — platform and fleet, development, corporate IT,
   people, physical, suppliers, legal — led by the Information Security Officer / ISMS Manager
   with the area's owner roles, plus one workshop per entity.
2. Each risk is written as "*threat* exploits *vulnerability* of *asset*, causing *consequence*"
   and receives an id `R-nnn` (never reused), an owner role, the asset, and the affected
   interested parties and legal requirements.
3. Opportunities (clause 6.1.1) — automation that removes a manual control, a certification that
   opens a market — are recorded in the continual improvement register under PROC-CAPA.

### 4. Risk analysis

1. Each risk is scored as likelihood × impact on the five-point scales of the risk criteria,
   first *inherent* (assuming only legally unavoidable controls) and then *residual* (after the
   existing or planned treatment):

| Likelihood | Impact |
| --- | --- |
| 1 Rare — less than once in ten years | 1 Negligible — under 10 kEUR, no customer impact |
| 2 Unlikely — once in three to ten years | 2 Minor — 10–50 kEUR; a single site or a few lockers for under four hours |
| 3 Possible — once in one to three years | 3 Moderate — 50–250 kEUR; service degraded for up to a day; limited personal data |
| 4 Likely — about once a year | 4 Major — 250 kEUR to 1 MEUR; outage beyond a day or a significant breach |
| 5 Almost certain — several times a year | 5 Severe — over 1 MEUR; multi-day outage, large-scale breach, sanctions, safety impact |

2. Scores fall into bands: low 1–4, medium 5–9, high 10–15, critical 16–25. The owner records the
   reasoning behind the scores in the register entry.

### 5. Risk evaluation

1. Risks are compared with the bands: critical and high risks must be treated; medium risks are
   treated within twelve months unless retained by the Managing Director; low risks may be
   retained by the Information Security Officer / ISMS Manager.
2. Risk appetite statement: *PaketPort accepts no critical residual risk, accepts high residual
   risk only temporarily while a funded treatment plan runs, and prefers treatment over retention
   wherever the cost is proportionate to the exposure of customers, carriers and the service.*

### 6. Risk treatment and control selection (clause 6.1.3)

1. For each risk the owner proposes a treatment option: **modify** (implement or strengthen
   controls), **retain** (accept within appetite), **avoid** (stop or change the activity) or
   **share** (insurance or contractual allocation — accountability stays with PaketPort).
2. For *modify*, the necessary controls are chosen and compared with Annex A: the controls are
   named in the risk entry, and the corresponding control guides under `isms/controls/` are
   updated — applicability, justification citing the risk id, implementation status, implementing
   documents, evidence. `isms generate` then regenerates the Statement of Applicability, so the
   SoA always reflects the register, and a control cannot be marked not applicable while a risk
   relies on it (`isms validate` rejects the combination).
3. The risk treatment plan — every open treatment with owner, actions, deadline and resources —
   is maintained in the ticket system (project ISMS-RTP) and summarised in the register through
   `status` and `review_date`.

### 7. Acceptance of residual risk

1. Residual risk is accepted by the role the band allows: low by the Information Security
   Officer / ISMS Manager; medium and high only by the Managing Director, with a documented
   rationale and, for high, a funded plan with a deadline; critical never. The acceptance is
   recorded in the register entry (`accepted_by`, `acceptance_rationale`) and in the management
   review minutes; `isms validate` enforces the authority per band.
2. Accepted risks are re-confirmed annually and whenever their scores change.

### 8. Monitoring and review (clause 8.2)

1. The Security Steering Committee reviews the register quarterly: treatment progress, new
   risks, key risk indicators (overdue vulnerabilities, failed restore tests, phishing click
   rate, locker tamper events, overdue reviews) and re-scoring where evidence has changed.
2. Risk owners review their risks by the `review_date` in the register; overdue reviews appear in
   the steering committee pack.

### 9. Records and tooling (clause 8.3)

1. The register is changed only through pull requests reviewed by the Information Security
   Officer / ISMS Manager and the risk owner; the version-control history is the record of every
   assessment and acceptance (PROC-DOC).
2. The generated risk register view and the Statement of Applicability are published with every
   release and presented at the management review together with the treatment plan status.

## Records

| Record | Where it is kept | Retention | Owner |
| --- | --- | --- | --- |
| Risk register and its history | `isms/risk/risk-register.yaml` in the repository | Life of the ISMS plus 3 years | Information Security Officer / ISMS Manager |
| Workshop notes and scoring rationale | Ticket system, project ISMS-RISK | 3 years | Information Security Officer / ISMS Manager |
| Risk treatment plan | Ticket system, project ISMS-RTP | Until closure plus 3 years | Risk owners |
| Acceptance decisions | Register entries; management review minutes | Life of the ISMS plus 3 years | Managing Director |
| Statement of Applicability | `generated/statement-of-applicability.md`; release assets | Life of the ISMS plus 3 years | Information Security Officer / ISMS Manager |

## Related documents

- POL-ISMS — Information Security Policy
- PROC-MR — Management Review Procedure
- PROC-CAPA — Nonconformity and Corrective Action Procedure
- PROC-DOC — Document Control Procedure
