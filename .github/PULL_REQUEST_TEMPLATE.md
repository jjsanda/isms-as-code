## What changes

<!-- One paragraph: which documents, controls or registers change and why. Link the issue. -->

## Document control checklist (PROC-DOC)

- [ ] Every changed document has a new **CHANGELOG entry** and a **version bump** (MAJOR = new or changed obligations, MINOR = clarification, PATCH = editorial / periodic review)
- [ ] `last_reviewed`, `next_review` and, where relevant, `effective_date` updated in the front matter
- [ ] Statement ids are stable — none reused, removed ones noted in the CHANGELOG
- [ ] Impact on the **Statement of Applicability** assessed; control guides (`implemented_by`, status, evidence, metrics) updated
- [ ] `make validate` and `make generate` run; `generated/` and `.github/CODEOWNERS` committed if they changed
- [ ] For MAJOR changes: communication plan before the effective date (POL-ORG ORG-13)
- [ ] Owner role and approver role requested as reviewers (CODEOWNERS does this automatically)

## Reviewer notes

<!-- Anything the owner and approver should look at in particular. -->
