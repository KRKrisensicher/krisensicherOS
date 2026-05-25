<!-- kso:product-relevance
repo-scope: product
classification: template
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->

# Risk Analysis Register

## Purpose

This template supports risk analyses in the ISMS following the logic:

```text
Risk = vulnerability + asset + threat
```

It is not a risk tool. It is a register schema that can be transferred into Markdown, a spreadsheet, a ticketing system, or a GRC tool.

## Triggers

Use when:

- new risks arise from incidents, audits, changes, asset reviews, or workshops,
- existing risks are reviewed,
- measures are derived or linked to a control taxonomy or SoA,
- gross, net, and target risks need to be made traceable.

## Users

- information security officer / CISO / ISMS owner,
- asset owner / process owner,
- control owner / measure owner,
- management review facilitator,
- reviewer or internal audit role.

## Working rules

SoA optional: If no ISO 27001 SoA exists yet, control references are initially maintained as an internal risk-control map. A later ISO 27001 SoA requires its own license-compliant standard basis.


1. Do not record any risk without an asset, vulnerability, and threat.
2. Before the gross assessment, document the current measures situation; AI can prepare this via questionnaire, owners confirm professionally.
3. Assess gross risk using the criteria for likelihood and impact; existing measures are documented as context but do not automatically lower the gross value.
4. Choose a strategy: acceptance, avoidance, transfer, or reduction with measures.
5. Plan measures and link them to control/SoA entries, owners, evidence, and effectiveness review.
6. Assess net/residual risk after strategy and measure planning using the same criteria; mark measures that are not yet effective as planned values.
7. Document confirmed net risk only after implementation and effectiveness review.

## Assessment scales

See [`04-isms-basics/risikomanagement-methodik.md`](../risikomanagement-methodik.md) for the binding operating logic:

- Likelihood: maximum value from detectability, exploitability, and hiddenness.
- Impact: maximum value from property damage, personal injury, financial loss, and immaterial damage.
- Risk value: likelihood factor × impact factor.

## Register fields

| Field | Entry |
| --- | --- |
| Risk ID | R-001 |
| Status | new / under assessment / in treatment / accepted / closed / resubmission |
| Scope / area |  |
| Asset / process / service |  |
| Asset owner |  |
| Vulnerability |  |
| Threat |  |
| Risk scenario | If [threat] exploits the vulnerability [vulnerability] on the asset [asset], then [impact] may occur. |
| Impact / damage description |  |
| Source / trigger | Incident / audit / change / workshop / asset review / external notification / other |
| Collection status of current measures | open / prepared via questionnaire / confirmed by owner / evidence-reviewed |
| Current organizational measures |  |
| Current technical measures |  |
| Current personnel / process measures |  |
| Current crisis management / BCMS / incident response capabilities |  |
| Evidence of current measures |  |
| Current control/SoA references |  |
| AI questionnaire reference | Link or storage location; no confidential full texts in public examples |
| Gross: detectability | 1-5 |
| Gross: exploitability | 1-5 |
| Gross: hiddenness | 1-5 |
| Gross: likelihood factor | max(detectability, exploitability, hiddenness) |
| Gross: property damage | 1-5 |
| Gross: personal injury | 1-5 |
| Gross: financial loss | 1-5 |
| Gross: immaterial damage | 1-5 |
| Gross: impact factor | max(property damage, personal injury, financial loss, immaterial damage) |
| Gross: risk value / category | L × I / very low to very high |
| Strategy | acceptance / avoidance / transfer / reduction |
| Strategy rationale | Why this strategy? Which alternative was rejected? |
| Transfer target, if relevant | insurance / outsourcing / crisis management / BCMS / other |
| Planned measures |  |
| Measure IDs |  |
| Planned control/SoA references |  |
| Expected measure effect | likelihood / impact / both |
| Net/residual risk: assessment status | planned value / confirmed |
| Net: detectability | 1-5 |
| Net: exploitability | 1-5 |
| Net: hiddenness | 1-5 |
| Net: likelihood factor | max(...) |
| Net: property damage | 1-5 |
| Net: personal injury | 1-5 |
| Net: financial loss | 1-5 |
| Net: immaterial damage | 1-5 |
| Net: impact factor | max(...) |
| Net: risk value / category | L × I / very low to very high |
| Confirmed net risk after effectiveness review | value / category / date |
| Decision / approval needed | yes / no; who decides? |
| Management decision / acceptance | reference to decision log |
| Review cadence | quarterly / annually / event-driven |
| Next review | date |
| Open questions / assumptions |  |

## Example without real organizational data

| Field | Example |
| --- | --- |
| Risk ID | R-001 |
| Asset / process / service | Fictional cloud file exchange |
| Vulnerability | External shares are not reviewed regularly. |
| Threat | Former project participants or external third parties continue to access files. |
| Risk scenario | If external third parties exploit existing shares, confidential project documents may be disclosed without authorization. |
| Gross: likelihood factor | 4 |
| Gross: impact factor | 3 |
| Gross: risk value / category | 12 / medium |
| Existing measures | Manual approval by project management. |
| Net: risk value / category | 9 / medium |
| Treatment decision | treat |
| Planned measures | Quarterly sharing review, expiration date for new shares, sample check in management review. |
| Planned control/SoA references | organization-specific control ID, do not copy standard texts. |
| Net/residual risk | 4 / low, planned value |

## Output

- assessed risk scenario,
- gross and net/residual risk assessment with planned value/confirmation status,
- measure and control/SoA linkage,
- open management decisions,
- review and evidence needs.

## Evidence

The register itself, workshop notes, control/SoA mapping, measure status, decision log, effectiveness reviews, and management review excerpts are created as evidence.

## Limits

This template does not replace legal advice, data protection assessment, certification review, or a risk acceptance decision. Real organizational, personal, and customer data belong only in approved internal working environments.
