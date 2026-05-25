<!-- kso:product-relevance
repo-scope: product
classification: source-register-structure
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# NIS2 Primary Sources and Evaluation Anchors

Status: 2026-05-25

## Purpose

This file consolidates official reference anchors for NIS2 readiness. It does not replace legal advice and does not contain a binding applicability assessment.

**Mandatory notice:** Every preliminary assessment of applicability must be reviewed by a qualified lawyer or an appropriately responsible legal function.

## Official Sources

### EU: NIS2 Directive

- Directive (EU) 2022/2555 — NIS2: <https://eur-lex.europa.eu/eli/dir/2022/2555/oj?locale=de>
- Use: terms, objectives, recitals, minimum requirements, notification and supervisory logic.
- Working rule: use the directive as a reference anchor; check national implementation, sector rules, and individual-case assessment separately.

### Germany: BSIG 2025

- BSIG, unofficial table of contents: <https://www.gesetze-im-internet.de/bsig_2025/>
- Section 28 BSIG — particularly important and important entities: <https://www.gesetze-im-internet.de/bsig_2025/__28.html>
- Annex 1 BSIG — sectors of particularly important and important entities: <https://www.gesetze-im-internet.de/bsig_2025/anlage_1.html>
- Annex 2 BSIG — sectors of important entities: <https://www.gesetze-im-internet.de/bsig_2025/anlage_2.html>
- Use: German preliminary applicability logic, categories, sector/entity types, threshold logic, exceptions, and handoffs.

### Energy Sector: EnWG Sections 5c to 5e

Rico had named “Sections 5c to 5e” as mandatory anchors. In the current official source landscape, these provisions are located in the EnWG and refer to BSIG categories.

- Section 5c EnWG — IT security in the context of facilities, networks, and energy services: <https://www.gesetze-im-internet.de/enwg_2005/__5c.html>
- Section 5d EnWG — documentation, notification, and registration obligations: <https://www.gesetze-im-internet.de/enwg_2005/__5d.html>
- Section 5e EnWG — executive management obligations and training: <https://www.gesetze-im-internet.de/enwg_2005/__5e.html>
- Use: special logic for energy supply networks, energy facilities, and digital energy services.

### BSI: FAQ and Applicability Assessment

- BSI NIS-2 applicability assessment: <https://www.bsi.bund.de/DE/Themen/Regulierte-Wirtschaft/NIS-2-regulierte-Unternehmen/NIS-2-Betroffenheitspruefung/nis-2-betroffenheitspruefung_node.html>
- BSI sector-specific FAQ: <https://www.bsi.bund.de/DE/Themen/Regulierte-Wirtschaft/NIS-2-regulierte-Unternehmen/NIS-2-FAQ/NIS-2-FAQ-sektorspezifisch/NIS-2-Sektorspezifische-FAQ_node.html>
- BSI NIS-2 for IT and telecommunications / Implementing Regulation (EU) 2024/2690: <https://www.bsi.bund.de/DE/Themen/Regulierte-Wirtschaft/NIS-2-regulierte-Unternehmen/Sektorspezifische-NIS-2-Informationen/NIS-2-fuer-IT-und-TK/NIS-2-fuer-IT-und-TK_node.html>
- Use: plausibility check, sector guidance, current BSI interpretation guidance. Do not use as the sole legal basis.

### EU: Implementing Regulation (EU) 2024/2690

- Implementing Regulation (EU) 2024/2690: <https://eur-lex.europa.eu/eli/reg_impl/2024/2690/oj?locale=de>
- PDF view: <https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=OJ:L_202402690>
- Use: technical and methodological requirements for risk management measures and specification of significant incidents for certain types of digital entities.

Affected entity types according to the BSI summary:

- DNS service providers,
- TLD name registries,
- providers of cloud computing services,
- providers of data center services,
- operators of content delivery networks,
- managed services providers,
- managed security services providers,
- providers of online marketplaces,
- online search engines,
- social networking services platforms,
- trust service providers.

## Evaluation Sequence

1. Capture the organizational and service profile.
2. Pre-check sector/entity type under BSIG Annex 1/2.
3. Capture size, revenue, and balance sheet total logic under Section 28 BSIG.
4. Check special categories: critical facilities, DNS/TLD, telecommunications, energy, finance/DORA, telematics, local authorities.
5. If energy: additionally check EnWG Sections 5c to 5e.
6. If digital infrastructure/digital services/trust services: additionally evaluate Implementing Regulation (EU) 2024/2690.
7. Place the BSI applicability assessment and sector-specific FAQ as a plausibility check before the final human legal review.
8. Output the result only as a working assumption: “possibly affected”, “not sufficiently evidenced”, “currently no match in the queried criteria”.

## Prohibited Output Wording

Do not output:

- “You are subject to NIS2.”
- “You are not affected.”
- “This is legally certain.”
- “NIS2 compliance is given.”
- “No legal review needed.”

Allowed:

- “The preliminary check shows indicators of possible applicability.”
- “The preliminary check currently shows no clear match; open points remain to be reviewed by legal counsel.”
- “The classification depends on legal interpretation, group/partner logic, entity type, and actual activity.”
