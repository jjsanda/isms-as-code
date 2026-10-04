# Auditor guide — how to audit this repository

This repository *is* the ISMS document set. Everything an auditor asks for in a Stage 1 review and
most of what a Stage 2 audit samples is either a file here or generated from one. No demo licence,
no screenshots — clone it or read it on the web.

## Thirty-minute orientation

| Question | Where to look |
| --- | --- |
| What is in scope? | [`generated/isms-scope-statement.md`](../generated/isms-scope-statement.md) — generated from `isms/context/organisation.yaml`, interested parties and the legal register |
| Which controls apply and how far are they implemented? | [`generated/statement-of-applicability.md`](../generated/statement-of-applicability.md); per entity under `generated/soa/` |
| Which documents exist, who owns them, when are they reviewed? | [`generated/document-register.md`](../generated/document-register.md) |
| How are risks assessed and which controls treat them? | `isms/risk/risk-criteria.yaml`, [`generated/risk-register.md`](../generated/risk-register.md), PROC-RISK |
| Where is each ISO/IEC 27001 clause 4–10 answered? | [`generated/coverage-iso27001-clauses.md`](../generated/coverage-iso27001-clauses.md) |
| How are the NIS2 Art. 21(2) measures covered? | [`generated/coverage-nis2-article-21.md`](../generated/coverage-nis2-article-21.md) |
| How are documents controlled? | PROC-DOC — and this repository is the mechanism it describes |

## Tracing a control end to end

1. Open the SoA row, e.g. **A.5.15** → it links to `isms/controls/5-organizational/A.5.15.md`.
2. The guide's front matter states applicability, the *justification* (citing risks `R-004`,
   legal items `LEG-01`, interested parties `IP-02`), the implementing documents (`POL-ACC`), the
   owner role, the evidence items with their location and frequency, and the metrics.
3. Follow `POL-ACC` → the policy statements (`ACC-1` …) are the rules; the CHANGELOG shows how
   they evolved and when each version was approved.
4. `git log --follow isms/policies/POL-ACC-access-control-policy/README.md` shows every change
   with author, reviewer and date; the merge commit of the pull request is the approval record.
5. The evidence items name the system of record (ticket queue, identity provider report, fleet
   plane) — that is what to sample on site.

The picture: ![Traceability](diagrams/rendered/02-traceability.png)

## Verifying a released PDF

Releases publish signed PDFs, `SHA256SUMS` and `signing-trust-anchor.pem`.

```bash
uv run isms verify --out <download-dir> --trust <download-dir>/signing-trust-anchor.pem
sha256sum -c SHA256SUMS      # inside the download directory
```

`isms verify` reports, per file, whether the signature is cryptographically valid, covers the
entire file and chains to the trust anchor, plus the signer name and signing time. In a PDF
reader, import the trust anchor once and the signature panel shows the same. A PDF signed with
the development key says **UNTRUSTED DEVELOPMENT KEY** in the signer name and the stamp — it is a
build artefact, not a controlled copy (ADR 0004).

## Checking document control in operation

- `uv run isms validate` — the whole consistency check the pipeline runs on every change.
- `uv run isms generate --check` — proves the committed SoA and registers match the sources.
- `uv run isms review-due --within 90` — what is due or overdue on a given day (`ISMS_NOW=2027-01-01`
  to simulate a date).
- `.github/CODEOWNERS` — generated review routing: owner role and approver role per document.
- `.github/workflows/` — the gate (`ci.yml`), the signed release (`release.yml`) and the weekly
  review reminders (`review-reminders.yml`).

## Reading the git history as records

| Record | Command |
| --- | --- |
| Who changed a document and when | `git log --format='%h %ad %an %s' --date=short -- isms/policies/POL-HR-hr-security-awareness-policy/` |
| The exact text of an approved version | `git show v1.0.0:isms/policies/POL-ISMS-information-security-policy/README.md` |
| All changes to the risk register | `git log -p -- isms/risk/risk-register.yaml` |
| Review decisions for a change | the pull request linked from the merge commit |

## Known limitations (read before you write a finding)

This is a demonstration corpus for a fictional group: the evidence locations are named but the
ticket systems behind them do not exist, and the control guides state an implementation status
that is illustrative. What is real is the mechanism — the way the set is validated, versioned,
reviewed, generated, rendered and signed.
