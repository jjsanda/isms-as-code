# Glossary

| Term | Meaning here |
| --- | --- |
| **ISMS** | Information security management system — the policies, processes, people and controls that manage information security, here specified by ISO/IEC 27001:2022. |
| **Annex A** | The 93 reference controls of ISO/IEC 27001:2022 in four themes (organizational, people, physical, technological). Only their identifiers and titles appear in this repository; the text must be obtained from the standard. |
| **Statement of Applicability (SoA)** | The list of all Annex A controls with, for each, whether it applies, why, and how far it is implemented. Generated here from the control guides and the risk register. |
| **Control implementation guide** | One Markdown file per Annex A control: applicability, justification, implementing documents, owner, evidence, metrics and PaketPort-specific guidance. |
| **Controlled document** | A policy, standard or procedure with front matter, a CHANGELOG and an approval record (PROC-DOC). |
| **Policy / standard / procedure** | Policy: what is required and why. Standard: measurable technical requirements. Procedure: who does what, when, with which record. |
| **Statement id** | The stable identifier of a policy statement or standard requirement, e.g. `ACC-8`, cited by other documents and by control guides. |
| **MAJOR / MINOR / PATCH** | The three version bumps: changed obligations / clarification / editorial or periodic review (ADR 0002). |
| **Retired / superseded** | A document taken out of force; it names its successor and the successor names it. |
| **Entity, site** | A legal entity (`ENT-AT` …) and a physical or logical location (`SITE-VIE-HQ` …) of the group. |
| **NIS2** | Directive (EU) 2022/2555 on a high common level of cybersecurity; Art. 21 lists risk-management measures, Art. 23 the incident-reporting deadlines (24 h / 72 h / 1 month). |
| **CSIRT / competent authority** | The national incident-response team and supervisory authority that receive NIS2 reports (CERT.at in Austria). |
| **GDPR / DSGVO** | Regulation (EU) 2016/679 on the protection of personal data. |
| **Cyber Resilience Act** | Regulation (EU) 2024/2847 on security requirements for products with digital elements — the lockers and their firmware. |
| **Residual risk** | The risk that remains after treatment; scored 1–25 on a 5×5 scale and retained only by the role the criteria allow. |
| **PAdES** | PDF Advanced Electronic Signatures — the format of the digital signatures embedded in the rendered PDFs. |
| **Trust anchor** | The public certificate (issuing CA) that `isms verify` and PDF readers use to decide whether a signature is trusted. |
| **Source digest** | The SHA-256 over all inputs that every generated file carries instead of a timestamp. |
| **Fleet-management plane / OTA** | The platform that inventories, monitors and updates the locker edge devices, delivering signed firmware over the air. |
