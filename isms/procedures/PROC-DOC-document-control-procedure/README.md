---
id: PROC-DOC
title: Document Control Procedure
type: procedure
status: approved
version: 1.2.0
classification: internal
owner: isms-manager
approver: managing-director
effective_date: 2026-07-06
last_reviewed: 2026-07-06
review_cycle: P1Y
next_review: 2027-07-06
controls: [A.5.37]
clauses: ["6.3", "7.5", "7.5.1", "7.5.2", "7.5.3"]
applies_to: [all]
related: [POL-ISMS, POL-CLS, POL-LEG, POL-HR]
supersedes: []
language: en
tags: [document-control, governance]
---

# PROC-DOC — Document Control Procedure

## Purpose

This procedure defines how the documented information of the PaketPort ISMS is created, reviewed,
approved, published, periodically reviewed, changed and retired. Its aim is simple: anyone who
needs a document finds the current approved version, and every change can be traced to an author,
a reviewer, an approver and a date (ISO/IEC 27001:2022 clause 7.5; Annex A control A.5.37).

## Scope

All documented information of the ISMS across all in-scope entities: policies, standards,
procedures, the Annex A control implementation guides, the context and risk registers, the
requirement mappings, and the artefacts generated from them (the ISMS scope statement, the
Statement of Applicability, the document register and the coverage reports). Records produced
by *operating* the ISMS — tickets, minutes, logs, training records — are governed by POL-CLS and
POL-LEG, not by this procedure.

## Procedure

### 1. The document set and its single source of truth

1. The repository `isms-as-code` is the only authoritative location for ISMS documents. Copies
   outside it — PDFs, intranet pages, printouts — are uncontrolled unless produced by the release
   pipeline described in stage 6.
2. Every document is a folder named `<id>-<slug>` that contains `README.md` (metadata header and
   body) and `CHANGELOG.md`. Registers are YAML files under `isms/context/`, `isms/risk/` and
   `isms/mappings/`; one control guide per Annex A control lives under `isms/controls/`.
3. Every document is identified by its id (`POL-`, `STD-` or `PROC-` plus a mnemonic; control
   guides use the Annex A identifier) and carries the following metadata in its header:

   | Field | Meaning |
   | --- | --- |
   | `status` | `draft` → `in-review` → `approved` → `retired` |
   | `version` | semantic version; the newest CHANGELOG entry |
   | `owner`, `approver` | role keys from the role register, never people, never the same role |
   | `effective_date` | the date the current version applies from |
   | `last_reviewed`, `review_cycle`, `next_review` | the review clock |
   | `controls`, `clauses` | the Annex A controls and ISO/IEC 27001 clauses the document addresses |
   | `applies_to` | all entities, or the entity ids the document is limited to |
   | `related`, `supersedes`, `superseded_by` | links to other documents |

4. The tooling (`isms validate`) rejects a document whose metadata is incomplete, whose
   references do not resolve, whose structure misses a required section or whose CHANGELOG
   disagrees with its header. Nothing that fails validation can be merged.

### 2. Creating a new document

1. Whoever identifies the need opens a *policy change request* in the issue tracker stating the
   purpose, the affected Annex A controls and risks, and the proposed owner role. The ISMS Manager
   confirms the document type and assigns the id within five working days.
2. The author creates a branch named `docs/<id>-<topic>` and runs `isms new <type>` with the id,
   title, owner and approver; the scaffold creates the folder from the template with
   `status: draft`, `version: 0.1.0` and a CHANGELOG.
3. The author writes the document to the authoring guide (`docs/authoring-guide.md`), runs
   `make validate` and `make generate`, and opens a pull request when the draft is ready for
   review. Drafts may be shared for comment but are never distributed as applicable rules.

### 3. Review and approval

1. Opening the pull request triggers the checks: validation, regeneration of the derived artefacts
   (a stale Statement of Applicability fails the check), the CHANGELOG check, and linting. The
   `CODEOWNERS` file, generated from the ownership metadata of all documents, automatically
   requests review from the owner role and the approver role of every document touched.
2. Reviewers assess content against the authoring guide, the impact on other documents and on the
   Statement of Applicability, the correctness of the CHANGELOG entry and the version bump, and
   whether the requirements are testable. Review comments and their resolution stay with the pull
   request.
3. Approval consists of the approver role's approving review and the merge into `main`. The merge
   is the approval record: it fixes the author, the reviewers, the date and the exact content.
   No separate signature sheet exists.
4. Approver roles. The Managing Director approves POL-ISMS, POL-ORG, POL-ACC, POL-IR, POL-LEG,
   POL-CLS and the ISMS-core procedures (PROC-DOC, PROC-RISK, PROC-AUDIT, PROC-MR, PROC-CAPA,
   PROC-IR). The ISMS Manager approves all other policies, standards and procedures. Control
   guides are approved by the owner role of the control with the ISMS Manager as second reviewer.
   The approver of a document is never its owner.
5. A new document is merged as `status: approved` with version `1.0.0` and an `effective_date`.
   Where staff need time to adapt, the effective date may be up to 60 days after approval; the
   owner uses the interval for communication and, with the HR Manager, for training updates.

### 4. Changing a document

1. Every change is a new version with a CHANGELOG entry — including a periodic review that finds
   nothing to change. Versions follow three rules:

   | Bump | When | What follows |
   | --- | --- | --- |
   | MAJOR | a statement is added, removed or changed so that obligations differ | re-approval by the approver role; communication to everyone in scope before the effective date; training material updated where staff behaviour is affected |
   | MINOR | clarification, examples, additional guidance, extension to a further entity without new obligations | approval by the approver role |
   | PATCH | editorial changes, link fixes, periodic review without change | approval by the owner; the approver is informed through the pull request |

2. The author branches, changes the document, updates `version`, `last_reviewed`, `next_review`
   and, where relevant, `effective_date`, adds the CHANGELOG entry naming the affected statement
   ids, regenerates the derived artefacts and opens a pull request. The CHANGELOG check fails any
   pull request that changes a document without an entry and a version bump.
3. For MAJOR changes the owner records the communication (announcement, team briefings) in the
   pull request before the effective date is reached.

### 5. Periodic review

1. Every document has a `review_cycle`; the default is one year. POL-ISMS is reviewed before the
   annual management review so that its objectives can be updated there.
2. Sixty days before `next_review` the weekly review job opens a *document review* issue assigned
   to the owner role. The owner reviews the document, consults the owners of the controls it
   implements, and either changes it (stage 4) or records the review as a PATCH version with the
   CHANGELOG entry "Periodic review — no changes required".
3. `isms validate` reports documents whose `next_review` has passed; the document register lists
   them as overdue. Reviews overdue by more than 90 days are reported to the management review.

### 6. Publication and distribution

1. On every release tag the pipeline renders each approved document, the Statement of
   Applicability, the scope statement and the registers to PDF, applies a digital signature
   (PAdES) with the document-control signing key, writes a SHA-256 manifest and publishes the
   files as release assets.
2. Rendered documents show the id, version, status, classification, owner, approver, effective
   date and next review on the cover, the revision history from the CHANGELOG, and the footer
   "Controlled document — uncontrolled when printed". Drafts and documents in review carry a
   watermark and are never distributed outside the review.
3. The generated document register is the index of current documents; the intranet links to the
   repository and to the latest release rather than hosting copies.
4. Earlier versions remain retrievable from version control and from earlier releases for the
   retention period in the records table; they are never edited.

### 7. Retirement and supersession

1. A document is retired by setting `status: retired`, `retired_date` and `superseded_by`; the
   successor lists the retired document in `supersedes`. The tooling checks that both sides agree.
2. Retired documents stay in the repository, are rendered with a RETIRED watermark, are excluded
   from the Statement of Applicability and from the coverage reports, and their statement ids are
   never reused.

### 8. Documents of external origin

Standards, laws, regulations and contracts the ISMS depends on are listed in the legal register
with an owner role and a verification note; the ISMS Manager confirms the register at every
management review. Supplier documentation (assurance reports, certificates) is held in the
supplier register under POL-SUP.

### 9. Protection and access

Documents are classified `internal` unless their header says otherwise. The repository is readable
by all staff of the in-scope entities and changed through pull requests only. Material classified
`restricted` — keys, detailed network diagrams, incident specifics — is never placed in a document;
documents reference where it is kept and who may access it.

## Records

| Record | Where it is kept | Retention | Owner |
| --- | --- | --- | --- |
| Approved versions and change history | Git history of `main`; release assets | Life of the ISMS plus 3 years | ISMS Manager |
| Pull-request reviews and approvals | Repository hosting platform | Life of the ISMS plus 3 years | ISMS Manager |
| Signed PDFs and SHA-256 manifests | Release assets | 10 years | ISMS Manager |
| Document review issues and outcomes | Issue tracker, label `review-due` | 3 years | Document owners |
| Exception register | Ticket system, project ISMS-EXC | 3 years after expiry | ISMS Manager |
| Communication of MAJOR changes | Announcement archive; training records under POL-HR | 3 years | Document owners |

## Related documents

- POL-ISMS — Information Security Policy
- POL-CLS — Asset Management and Information Classification Policy
- POL-LEG — Legal, Regulatory and Privacy Compliance Policy
- POL-HR — HR Security & Awareness Policy
