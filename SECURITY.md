# Security policy

This is a **portfolio / demonstration project**. It models a fictional company group
("PaketPort") and contains **no real, confidential, or personal data** — every policy, risk,
evidence reference, metric and role holder is illustrative.

## Reporting

If you spot a security issue in the tooling (not in the fictional content), please open a GitHub
issue or contact the author. There is no production deployment and no bug bounty.

## Threat model & design choices

Even as a demo, the project is built to be safe by construction:

- **No secrets in the repository.** Signing keys come from CI secrets or are generated
  ephemerally per build; `.gitignore` blocks `*.p12`, `*.pfx`, `*.key` and private PEM files, and
  the pre-commit `detect-private-key` hook guards commits. Only the public trust anchor is ever
  published.
- **Untrusted builds look untrusted.** Without a configured key the signer's common name is
  "UNTRUSTED DEVELOPMENT KEY" and the visible stamp says so.
- **Strict input validation.** All structured data is parsed through Pydantic v2 with
  `extra="forbid"`; the validator refuses to generate or build from an inconsistent corpus.
- **No network at runtime.** Validation, generation, rendering, signing and verification run
  offline; certificate revocation fetching is disabled and trust is anchored explicitly.
- **Output safety.** Templates auto-escape; Markdown is converted with a fixed extension set.
- **Supply chain.** Dependencies are pinned in `uv.lock`; CI runs `pip-audit` and CodeQL; release
  assets carry a build-provenance attestation and a SHA-256 manifest.

See [`docs/adr/`](docs/adr/) for the rationale behind these choices.
