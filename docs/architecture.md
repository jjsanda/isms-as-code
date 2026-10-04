# Architecture

`isms-as-code` is a small Python toolkit around a set of plain files. The files are the product;
the tool keeps them consistent and turns them into the artefacts an ISMS has to produce.

![What is this](diagrams/rendered/00-what-is-this.png)

## Data model

| Source | Location | Model |
| --- | --- | --- |
| Controlled documents | `isms/{policies,standards,procedures}/<id>-<slug>/README.md` + `CHANGELOG.md` | `DocumentMeta` (front matter), `Changelog` |
| Control implementation guides | `isms/controls/<theme>/A.x.y.md` | `ControlGuideMeta` |
| Annex A catalogue | `isms/catalogue/iso27001-2022-annex-a.yaml` | `Catalogue` (93 controls, attributes) |
| Organisation and scope | `isms/context/organisation.yaml` | `Organisation` (entities, sites, services, systems, interfaces) |
| Roles | `isms/context/roles.yaml` | `RoleRegister` |
| Interested parties, legal register | `isms/context/*.yaml` | `InterestedPartyRegister`, `LegalRegister` |
| Risk criteria and register | `isms/risk/*.yaml` | `RiskCriteria`, `RiskRegister` |
| Requirement mappings | `isms/mappings/*.yaml` | `Mapping` |

All models are Pydantic with `extra="forbid"`; identifier shapes are part of the schema
(`POL-[A-Z]{2,6}`, `A\.[5-8]\.\d+`, `R-\d{3}` …). The loader (`loader.py`) reads everything,
aggregates every problem into one `LoaderError`, and hands a `Repository` to the validator
(`validate.py`), which checks the *set*: references resolve, every control has exactly one guide,
CHANGELOG and front matter agree, supersession is mutual, risks are treated by applicable
controls, retained risks are accepted by the role the criteria allow, and so on.

## Pipeline

```text
validate ──► generate ──► render ──► sign ──► manifest ──► verify
 (schema,     (SoA, scope,  (HTML →    (PAdES,    (SHA256SUMS)  (chain, coverage,
  cross-refs)  registers,    PDF)       stamp)                    manifest)
               coverage,
               CODEOWNERS,
               badges)
```

- `generate/` — pure functions `(Repository, digest) -> str`. Outputs are deterministic and carry
  a source digest; `--check` compares a fresh render with the committed files (ADR 0003).
- `render/` — python-markdown → Jinja2 template (`render/assets/document.html.j2`, cover block,
  revision history, approval block, watermark) → WeasyPrint with CSS paged media (`print.css`:
  running headers, "uncontrolled when printed" footer, page numbers). PDF dates come from the
  document data, so unsigned PDFs are byte-stable.
- `signing.py` — two-tier key material (`generate_key_material`, PKCS#12 round trip), PAdES
  signing with a visible stamp in the cover's signature area, verification with an explicit
  trust anchor (ADR 0004). `build.py` orchestrates the whole chain.
- `review.py` — date-relative reporting (what is due) through an injectable `Clock`
  (`ISMS_NOW`, `SOURCE_DATE_EPOCH`), the only place "today" enters the system.
- `gitcheck.py` / `scaffold.py` — the pull-request guard (`changelog-check`) and `isms new`.

## Determinism

Generated files never contain timestamps; iteration is sorted; JSON is canonical; the digest over
the inputs is the only "version" of an artefact. Rendering twice yields identical PDFs; signing
adds the signing time (by design). Tests assert byte-equality of repeated runs.

## Extension points

- **New entity or site** — add it to `organisation.yaml`; per-entity SoAs and the scope statement
  follow. Use `applies_to` in documents and `entity_overrides` in guides for deviations
  (see [multi-entity.md](multi-entity.md)).
- **New requirement set** (another regulation, a customer framework) — add `isms/mappings/<name>.yaml`;
  a coverage report and a badge appear automatically.
- **New document** — `isms new policy --id POL-XYZ --title … --owner … --approver …`.
- **Real signing key** — `isms keygen`, store the PKCS#12 as `ISMS_SIGNING_P12` (base64) and the
  passphrase as `ISMS_SIGNING_PASSPHRASE`; commit only the trust anchor PEM.
