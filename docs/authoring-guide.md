# Authoring guide

How to write a document in this repository so that it reads well, can be audited, and passes
`isms validate`. Read this before opening a pull request; reviewers apply it.

## 1. Document types and where each sits

| Type | Id prefix | Answers | Length | Approver |
| --- | --- | --- | --- | --- |
| **Policy** | `POL-` | *What* is required and *why* — mandatory rules for a topic | 1–3 pages | Managing Director (POL-ISMS, POL-ORG, POL-ACC, POL-IR, POL-LEG, POL-CLS) or ISMS Manager |
| **Standard** | `STD-` | *Which* measurable technical requirements implement a policy statement | 1–2 pages | ISMS Manager |
| **Procedure** | `PROC-` | *How* something is done: steps, roles, deadlines, records | 1–4 pages | Managing Director (ISMS-core procedures) or ISMS Manager |
| **Control guide** | `A.x.y` | How one Annex A control is realised at PaketPort, and how that is evidenced | 25–60 lines | Owner role of the control |

Policies state rules; they never contain step-by-step instructions. Procedures contain steps; they
never introduce new obligations. Standards contain numbers. If you find yourself writing the wrong
thing in the wrong type, split it.

## 2. Voice

- **Plain English, short sentences, active voice.** "The IT Operations Lead disables the account
  within 24 hours", not "accounts are to be disabled in a timely manner by the responsible party".
- **Modal verbs are load-bearing.** *shall* = mandatory; *should* = recommended, deviation must be
  justified; *may* = permitted. Do not use *must*, *will* or *needs to* for requirements.
- **Every requirement is testable.** An auditor can ask "show me". If you cannot name the evidence,
  rewrite the requirement until you can.
- **Roles, never people.** Write "Head of Platform & SRE", not a name. Role titles come from
  `isms/context/roles.yaml`; the current holder is data, not document content.
- **PaketPort-specific.** Mention lockers, the fleet-management plane, the backend, carriers, the
  Vienna depot, the Munich field service, the Brno test lab — whatever the rule is really about.
  Generic boilerplate that could be pasted into any company is a review finding.
- **British English** (organisation, authorisation, programme, licence as a noun). ISO dates
  (`2026-08-20`), amounts as `250 kEUR`, durations in words ("within 24 hours").
- **No vendor or product names** for tools (say "the identity provider", "the ticket system").
- **Never reproduce ISO text.** Control titles are used as headings; every description is original.

## 3. Structure

The validator enforces the H1 (`# <id> — <title>`, em dash) and the required H2 sections, in any
order, with extra sections allowed.

| Type | Required H2 sections |
| --- | --- |
| policy | Purpose · Scope · Policy statements · Roles and responsibilities · Compliance and exceptions · Related documents |
| standard | Purpose · Scope · Requirements · Compliance and exceptions · Related documents |
| procedure | Purpose · Scope · Procedure · Records · Related documents |
| control guide | Objective · Implementation · Evidence · Metrics · Common pitfalls |

### Policy statements and requirements carry stable ids

Group statements under H3 topic headings and give each one an id `<MNEMONIC>-<n>` in bold, where
the mnemonic is the document id without its prefix (`POL-ACC` → `ACC-1`, `STD-AUTH` → `AUTH-1`):

```markdown
### Identity life cycle

- **ACC-1** Every person, service and device that accesses PaketPort systems shall have a unique
  identity; shared accounts are prohibited except documented break-glass accounts (ACC-13).
```

Ids are stable references: control guides, procedures and audit findings cite `POL-ACC ACC-1`. An
id is never reused — when a statement is removed, say so in the CHANGELOG and leave the number
unused.

### Roles and responsibilities

A two-column table, roles by title, one line each, only roles that actually do something in this
document. Ownership and approval are in the front matter; do not repeat them.

### Compliance and exceptions

Say how compliance is monitored (which metric, which review, which audit) and restate the standard
exception path: a control exception request, approved by the document owner and the ISMS Manager,
time-limited to at most twelve months, recorded in the exception register.

### Related documents

Bullet list `- <ID> — <Title>`; keep it in sync with `related` in the front matter.

## 4. Front matter

| Field | Rule |
| --- | --- |
| `id` | `POL-`, `STD-`, `PROC-` plus 2–6 capitals, unique; the folder is `<id>-<slug of title>` |
| `status` | `draft` → `in-review` → `approved` → `retired`; drafts and in-review documents use `0.x.y` versions |
| `version` | SemVer; equals the newest CHANGELOG heading |
| `owner` / `approver` | role keys from `roles.yaml`; never the same role |
| `effective_date` | date the current version applies from; on or after the CHANGELOG approval date |
| `last_reviewed` | equals the newest CHANGELOG date |
| `review_cycle` / `next_review` | ISO 8601 duration; `next_review` = `last_reviewed` + cycle (clamped to month end) |
| `controls` | Annex A ids this document addresses; each control guide that names this document in `implemented_by` must appear here |
| `clauses` | ISO/IEC 27001 main-body clauses (procedures mostly) |
| `applies_to` | `[all]` or entity ids from `organisation.yaml` |
| `related`, `supersedes`, `superseded_by` | document ids; supersession is checked in both directions |

## 5. Versioning and the CHANGELOG

Every document folder has a `CHANGELOG.md` in Keep-a-Changelog format with `## [x.y.z] - YYYY-MM-DD`
headings, newest first, and `### Added / Changed / Deprecated / Removed / Fixed / Security` sections.
The date is the approval date (the merge of the pull request). There is no "Unreleased" section:
every merged change to a controlled document is a new, approved version.

| Bump | When | Consequence |
| --- | --- | --- |
| **MAJOR** | A statement is added, removed or changed so that obligations differ | Re-approval by the approver role, communication to everyone in scope, training update if relevant |
| **MINOR** | Clarification, examples, new guidance, scope extension to another entity without new obligations | Approval by the approver role |
| **PATCH** | Editorial, formatting, link fixes, periodic review with no change ("Periodic review — no changes required") | Approval by the owner, approver informed |

Name the affected statement ids in the entry ("Changed: ACC-6 now requires phishing-resistant MFA
for privileged access"). A pull request that changes a document without a CHANGELOG entry and a
version bump fails `isms changelog-check`.

## 6. Control guides

One file per Annex A control under `isms/controls/<theme>/A.x.y.md`. The front matter is the data
the Statement of Applicability is generated from; the body explains it.

- **Objective** — what the control achieves *for PaketPort*, two to four sentences, own words.
- **Implementation** — how it is done: cite the documents and statement ids (`POL-ACC ACC-7`),
  the systems (fleet-management plane, identity provider, CI pipeline), the roles, and per-entity
  differences (Munich field service, Brno lab) where they exist.
- **Evidence** — what an auditor can inspect and where; mirror the `evidence` list.
- **Metrics** — one to three measurable indicators with targets; mirror `metrics`.
- **Common pitfalls** — two to four things that go wrong in practice and how PaketPort avoids them.

`justification` explains *why the control is included* (or excluded): cite risks (`R-004`), legal
items (`LEG-01`) and interested-party requirements (`IP-02`). `implemented_by` lists the documents
that realise the control; each of them must list the control in its own `controls`. A control that
is `implemented` or `partially-implemented` needs at least one evidence item.

## 7. Checklist before you open the pull request

1. `make validate` passes with no errors (warnings explained in the PR).
2. `make generate` run; `generated/` and `.github/CODEOWNERS` committed if they changed.
3. CHANGELOG entry written, version bumped according to section 5, `last_reviewed` and
   `next_review` updated.
4. Statement ids unique and never reused; references to other documents resolve.
5. The PR template checklist is complete and the owner and approver roles are requested as reviewers
   (CODEOWNERS does this automatically).
