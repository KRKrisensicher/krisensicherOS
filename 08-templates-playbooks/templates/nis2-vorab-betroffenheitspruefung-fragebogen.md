# NIS2 preliminary applicability check — questionnaire

## Mandatory note

This questionnaire only creates a structured preliminary assessment. It does not provide legal advice and is not a binding determination of NIS2 applicability.

**Every result must be reviewed by a qualified lawyer or an appropriately responsible legal function.**

## Purpose

The questionnaire places an evaluation logic before the BSI FAQ and the BSI applicability assessment. It first collects the hard structural information, then maps it to BSIG, annexes, EnWG and implementing regulation, and uses the BSI FAQ only for plausibility checks.

## Source anchors

- NIS2 Directive: <https://eur-lex.europa.eu/eli/dir/2022/2555/oj?locale=de>
- BSIG: <https://www.gesetze-im-internet.de/bsig_2025/>
- § 28 BSIG: <https://www.gesetze-im-internet.de/bsig_2025/__28.html>
- Annex 1 BSIG: <https://www.gesetze-im-internet.de/bsig_2025/anlage_1.html>
- Annex 2 BSIG: <https://www.gesetze-im-internet.de/bsig_2025/anlage_2.html>
- EnWG § 5c: <https://www.gesetze-im-internet.de/enwg_2005/__5c.html>
- EnWG § 5d: <https://www.gesetze-im-internet.de/enwg_2005/__5d.html>
- EnWG § 5e: <https://www.gesetze-im-internet.de/enwg_2005/__5e.html>
- BSI sector-specific FAQ: <https://www.bsi.bund.de/DE/Themen/Regulierte-Wirtschaft/NIS-2-regulierte-Unternehmen/NIS-2-FAQ/NIS-2-FAQ-sektorspezifisch/NIS-2-Sektorspezifische-FAQ_node.html>
- Implementing Regulation (EU) 2024/2690: <https://eur-lex.europa.eu/eli/reg_impl/2024/2690/oj?locale=de>

## Section 1 — Basic data

| Question | Answer | Evidence / source | Uncertainty | Legal review required? |
| --- | --- | --- | --- | --- |
| Which legal entity is being assessed? |  |  |  | yes |
| Which goods or services does the entity offer for remuneration to other natural or legal persons? |  |  |  | yes |
| Are there multiple sites, companies, group/partner companies or legally dependent organizational units? |  |  |  | yes |
| Which IT systems, services, facilities or platforms are essential for service delivery? |  |  |  | yes |
| Are there regulated special areas such as energy, telecommunications, finance/DORA, telematics or public administration? |  |  |  | yes |

## Section 2 — Size and threshold logic under § 28 BSIG

| Question | Answer | Evidence / source | Evaluation note |
| --- | --- | --- | --- |
| Does the entity employ at least 250 employees? |  |  | possible indicator for an essential entity if an Annex 1 entity type is present |
| Does the entity have more than EUR 50 million annual turnover and more than EUR 43 million annual balance sheet total? |  |  | possible indicator for an essential entity if an Annex 1 entity type is present |
| Does the entity employ at least 50 employees? |  |  | possible indicator for an important entity if an Annex 1 or Annex 2 entity type is present |
| Does the entity have more than EUR 10 million annual turnover and more than EUR 10 million annual balance sheet total? |  |  | possible indicator for an important entity if an Annex 1 or Annex 2 entity type is present |
| Are partner/linked enterprises or group constellations present? |  |  | § 28 BSIG refers to SME recommendation and exceptions; force legal review |
| Are activities possibly negligible in relation to the overall activity? |  |  | have § 28 para. 3 BSIG reviewed |

## Section 3 — Special categories under § 28 BSIG

| Question | Answer | Evaluation note | Legal review required? |
| --- | --- | --- | --- |
| Does the entity operate a critical facility? |  | Operators of critical facilities are considered essential entities; review thresholds and BSI-KritisV | yes |
| Is the entity a qualified trust service provider, TLD name registry or DNS service provider? |  | special indicator for an essential entity | yes |
| Does it offer publicly accessible telecommunications services or operate public telecommunications networks? |  | review § 28 para. 1/2 and para. 5 BSIG as well as TKG | yes |
| Is the entity an energy supply network operator, energy facility operator or digital energy service operator? |  | evaluate EnWG § 5c to § 5e as special logic | yes |
| Does the entity fall under finance/DORA or telematics special rules? |  | review § 28 para. 6/7 BSIG | yes |
| Is the entity public administration/regional authority or a legally dependent unit? |  | review § 28 para. 8 BSIG and state law | yes |

## Section 4 — Annex 1 BSIG: possible entity types

Check only if the actual activity plausibly matches. In case of doubt, mark “unclear”.

| Sector | Match? | specific activity / entity type | Evidence | FAQ plausibility check |
| --- | --- | --- | --- | --- |
| Energy |  |  |  | Energy FAQ, EnWG § 5c-5e |
| Transport and traffic |  |  |  | BSI FAQ / sector law |
| Finance |  |  |  | DORA/financial supervision interface |
| Health |  |  |  | BSI health FAQ, e.g. delimitation of emergency medical services/medical technology |
| Drinking water / wastewater |  |  |  | sector law / BSI info |
| Digital infrastructure |  |  |  | BSI FAQ, Implementing Regulation 2024/2690 |
| Space |  |  |  | sector law |

## Section 5 — Annex 2 BSIG: possible entity types

| Sector | Match? | specific activity / entity type | Evidence | FAQ plausibility check |
| --- | --- | --- | --- | --- |
| Postal and courier services |  |  |  | BSI FAQ / sector law |
| Waste management |  |  |  | review main economic activity |
| Chemical substances |  |  |  | review REACH/NACE reference |
| Food |  |  |  | BSI FAQ: wholesale / industrial production / processing |
| Medical devices / IVD |  |  |  | review delimitation from Annex 1 Health |
| Manufacture of data processing equipment / electronics / optics |  |  |  | review NACE C26 |
| Electrical equipment |  |  |  | review NACE C27 |
| Mechanical engineering |  |  |  | review NACE C28 |
| Motor vehicles / motor vehicle parts |  |  |  | review NACE C29 |
| Other transport equipment |  |  |  | review NACE C30 |
| Online marketplaces |  |  |  | Implementing Regulation 2024/2690 |
| Online search engines |  |  |  | Implementing Regulation 2024/2690 |
| Social networking platforms |  |  |  | Implementing Regulation 2024/2690 |
| Research institutions |  |  |  | sponsor/purpose review |

## Section 6 — Implementing Regulation (EU) 2024/2690

Complete only if one of the following entity types is possible: DNS, TLD, cloud, data center, CDN, MSP, MSSP, online marketplace, online search engine, social network, trust service provider.

| Question | Answer | Evaluation note |
| --- | --- | --- |
| Which addressed digital entity type is present? |  | document specific category |
| Which services are provided with EU/Germany relevance? |  | clarify scope of the service |
| Are there documented risk assessments, technical and organizational measures, tracking and training? |  | use minimum requirements of the regulation as gap mapping |
| Are there criteria for assessing significant security incidents? |  | connect incident triage to regulation and BSIG notification process |
| Which evidence packs demonstrate implementation and effectiveness? |  | no compliance assurance, evidence need only |

## Section 7 — BSI FAQ evaluation logic

The BSI FAQ is used only after Sections 1 to 6.

| Preliminary question | If yes | BSI FAQ use |
| --- | --- | --- |
| Health match? | Delimitation of healthcare provider, emergency medical services, medical technology | review Health FAQ |
| Digital infrastructure? | Cloud, MSP/MSSP, DNS, telecommunications, web hosting delimitation | review Digital Infrastructure FAQ |
| Energy? | Energy facilities, networks, digital energy services | review Energy FAQ and EnWG § 5c-5e |
| Food? | Wholesale or industrial production/processing | review Food FAQ |
| No FAQ category fits? | open legal/technical question | direct legal review / BSI applicability assessment / business owner |

## Section 8 — Preliminary result

Select permissible result wording:

- [ ] **Possible applicability with strong indicators** — several criteria from § 28 BSIG, Annex 1/2 or special category plausibly apply. Legal review mandatory.
- [ ] **Possible applicability unclear** — activity, size, group logic, entity type or special law unclear. Legal review mandatory.
- [ ] **Currently no clear match in the criteria queried** — no binding non-applicability. Legal review required for relevant activity, growth, group reference or new source.
- [ ] **Special regime likely relevant** — review energy, telecommunications, finance/DORA, telematics or digital services in depth.

## Section 9 — Handoff

| Handoff | Recipient | Reason | Deadline |
| --- | --- | --- | --- |
| Legal review of applicability | Lawyer / Legal | mandatory note and open legal interpretation |  |
| Sector/business review | Business unit / Service Owner | validate plausibility of activity and entity type |  |
| Risk management gap | NIS2 Readiness Analyst | implementation in Gap Worksheet |  |
| Evidence Pack | Control Evidence Architect | plan evidence |  |
| Management decision | Management Review Facilitator | resources, owners, risk acceptance |  |
