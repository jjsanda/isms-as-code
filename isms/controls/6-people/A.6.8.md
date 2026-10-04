---
control: A.6.8
applicability: applicable
justification: 'Treats R-002 and R-005: people are the first sensor for phishing, tamper and misuse; a
  fast, no-blame channel is the cheapest detection PaketPort has (IP-07; NIS2 Art. 21(2)(b)).'
implementation_status: implemented
implemented_by:
- POL-IR
- PROC-IR
owner: isms-manager
risks:
- R-002
- R-005
evidence:
- description: Reported events per channel and month
  location: Ticket system, project INC
  frequency: monthly
- description: Phishing report-button statistics
  location: Mail gateway
  frequency: monthly
- description: Awareness content on reporting
  location: Training platform
  frequency: annual
metrics:
- Sampled events reported by staff within one hour of noticing (target ≥ 90 %)
- Phishing simulation report rate (target ≥ 60 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.6.8 — Information security event reporting

## Objective

Make reporting a suspected security event the natural, safe and quick thing to do for every employee, technician and supplier.

## Implementation

- POL-IR IR-6 (one-hour duty, channels, no blame) and IR-7 (field reporting through the tablet); PROC-IR stage 1 defines the channels and what to report; POL-ISMS ISMS-9 makes it everyone's duty.
- The report button in the mail client (POL-AUP AUP-13) and the training under POL-HR keep the habit alive.

## Evidence

- Reported events per channel and month — Ticket system, project INC.
- Phishing report-button statistics — Mail gateway.
- Awareness content on reporting — Training platform.

## Metrics

- Sampled events reported by staff within one hour of noticing (target ≥ 90 %)
- Phishing simulation report rate (target ≥ 60 %)

## Common pitfalls

- Too many channels, or the wrong ones — the mailbox, the hotline, the form and the tablet are the four, all landing in project INC.
- Blame after a click — HR-7 and IR-6 make reporting safe.
