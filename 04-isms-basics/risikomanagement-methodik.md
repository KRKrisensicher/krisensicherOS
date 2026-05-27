# ISMS Risk Management Methodology

## Purpose

This methodology describes how organizations can identify, assess, treat, connect with measures and control/SoA references, and regularly steer information security risks in the ISMS. A complete SoA requires the organization’s own license-compliant ISO 27001 basis or an organization-specific control taxonomy.

It is intentionally not a risk tool. krisensicherOS provides the working logic, templates, and review points so that user organizations can operate risk analyses in their own registers, ticketing systems, document repositories, or GRC tools.

## Principle

In krisensicherOS, a risk is described as the interaction of three elements:

```text
Risk = vulnerability + asset + threat
```

An entry in the risk register can only be assessed once all three elements are named:

- **Asset:** affected information asset, process, service, system, location, role, or service provider.
- **Vulnerability:** property, gap, or condition that makes harm possible.
- **Threat:** event, actor, error, outage, misuse, or environmental condition that can exploit the vulnerability.

Example structure, without real organizational data:

```text
If [threat] exploits the vulnerability [vulnerability] at the asset [asset],
then [impact] may occur.
```

## Dialog-Based Risk Process

The risk process can be carried out as a guided question process. For this, krisensicherOS uses the skill `isms-risk-analysis` and the session state `templates/risikoanalyse-session-state.md`.

The wizard works in phases:

1. Start or continue session.
2. Describe risk as vulnerability + asset + threat.
3. Capture the current measures situation using a questionnaire.
4. Assess gross risk.
5. Prepare strategy as a human gate.
6. Plan measures and control/SoA mapping.
7. Assess net/residual risk.
8. Generate reporting.

Each phase produces usable fields for the risk analysis register, Risk-Control Map / later SoA, decision log, and risk report.

## Roles and Responsibility

| Role | Responsibility in the risk process |
| --- | --- |
| Management / executive management | Approve risk criteria, decide on resources, remain accountable for risk acceptance and residual risks. |
| Information security officer / CISO / ISMS owner | Steer the process, maintain the methodology, facilitate workshops, prepare reporting, ensure control/SoA and measures mapping. |
| Asset owner / process owner | Report, assess, or technically confirm risks; propose measures and assess effectiveness. |
| Control owner / measures owner | Implement measures, generate evidence, report implementation status and effectiveness. |
| Reviewer / audit role | Challenge traceability, evidence, open decisions, and effectiveness review. |

Agents can structure, ask, map, and prepare proposals. Risk acceptance, resource decisions, and approvals remain human decisions.

## Process Overview

The risk assessment is performed twice: first as gross risk after describing the risk and presenting the current measures situation, then as net/residual risk after the strategy decision and measures planning.

1. **Clarify scope:** Define ISMS scope, assets considered, out-of-scope items, and assessment horizon.
2. **Identify and describe risk:** Evaluate reports, incidents, audits, changes, asset reviews, vulnerabilities, requirements, and workshops.
3. **Formulate risk scenario:** Capture vulnerability, asset, threat, and impact in a verifiable sentence.
4. **Capture current measures situation:** Record existing controls, routines, organizational practices, technical safeguards, crisis/emergency capabilities, and evidence sources. This step can be prepared through AI-assisted questionnaires; technical confirmation remains with the asset owner and information security officer.
5. **Assess gross risk:** Assess the risk using the assessment criteria for likelihood and damage extent. Gross risk describes the inherent risk situation of the scenario and, despite capturing the current measures, is documented in a way that keeps the original risk exposure visible. Current measures are captured as context but are not used to make the risk look better.
6. **Select strategy:** Define acceptance, avoidance, transfer, or minimization, or prepare it as a management decision. Transfer can mean, for example, insurance, outsourcing, or handing over specific response components to crisis management / BCMS; responsibility and residual risk remain visible.
7. **Plan measures:** Derive measures from vulnerability, asset, threat, and desired effect; define control/SoA reference, owner, due date, evidence, and effectiveness review.
8. **Assess net/residual risk:** After existing and planned or approved measures, assess the expected residual risk using the same criteria for likelihood and damage extent. If measures have not yet been implemented or effectiveness-checked, the net/residual risk is marked as a planned value and later confirmed or corrected.
9. **Review implementation and effectiveness:** Review measure status, evidence, actual risk change, and control/SoA status.
10. **Report and decide:** Transfer top risks, residual risks, acceptances, transfers, overdue measures, and control/SoA gaps into reporting and management review.

## Gross-Net Logic

krisensicherOS distinguishes between two mandatory assessments and one implementation status:

| Assessment status | Point in time | Meaning | Typical output |
| --- | --- | --- | --- |
| Gross risk | After risk description and capture of the current measures situation. | Inherent risk exposure of the scenario. Existing measures are made visible but do not automatically reduce this value. | Initial risk, current measures situation, rationale for relevance. |
| Net/residual risk | After strategy decision and measures planning. | Residual risk after selected strategy and measure effect. If measures have not yet been implemented, it is a planned value. | Residual risk, strategy, measures, control/SoA reference, decision template. |
| Confirmed net risk | After implementation and effectiveness review. | Actually confirmed residual risk after evidenced measure effect. | Updated register, effectiveness evidence, management review input. |

Rule: Measures only reduce confirmed net risk once they have been implemented, operated, and plausibly effectiveness-checked. Until then, the net/residual risk assessment remains a planned value.

## AI-Assisted Capture of the Current Measures Situation

AI can prepare the risk analysis by structuring indications from a questionnaire about existing measures, missing evidence, SoA references, and possible measure options. However, it must not make risk acceptance decisions and must not claim effectiveness.

Minimum questions for asset owner or process owner:

- Which asset, process, or service is affected?
- Which vulnerability makes the risk possible?
- Which threat can exploit this vulnerability?
- Which organizational, technical, or personnel-related measures already exist?
- Which measures are actually operated regularly?
- Which evidence shows that these measures exist and work?
- Which SoA/control entries are affected or planned?
- Which gaps, exceptions, or dependencies are known?
- Which crisis management, BCMS, or incident response capabilities limit the damage?
- Which decisions does management need to make?

The answers are transferred as a working basis into the risk analysis register and the SoA Risk-Control Map.

## Likelihood

Likelihood primarily relates to the risk-triggering vulnerability. Three aspects are assessed. The likelihood factor is the highest value from the three aspects, not the average.

| Aspect | Value 1 very low | Value 2 low | Value 3 medium | Value 4 high | Value 5 very high |
| --- | --- | --- | --- | --- | --- |
| Detectability of the vulnerability | Detectable only by experts. | Detectable only by some employees. | Detectable by employees. | Detectable by laypersons. | Obvious. |
| Exploitability of the vulnerability | Exploitation requires high effort, extensive tools, and specialist knowledge. | Exploitation requires high effort and advanced tools. | Exploitation is possible with advanced tools. | Exploitation is possible with simple tools. | Exploitation is possible without tools or even accidentally. |
| Hidden nature of exploitation | Exploitation is detected immediately and completely. | Exploitation is detected within one day and completely. | Exploitation is detected completely before delivery, before taking effect, or within one month. | Exploitation is detected only by third parties or before the end of a quarter. | Exploitation is detected only by chance, later than after one quarter, or not at all. |

**Assessment rule:**

```text
Likelihood factor = max(detectability, exploitability, hidden nature)
```

This maximum-value logic prevents a very critical vulnerability property from being averaged down by other, less critical aspects.

## Damage Extent

Damage extent describes the possible impact of the risk. Property damage, personal injury, financial losses, and intangible damage are assessed. The damage factor is the highest value from the damage categories considered.

| Value | Label | Property damage | Personal injury | Financial losses | Intangible damage |
| --- | --- | --- | --- | --- | --- |
| 1 | very low | 0 to 1,000 EUR | Minor injuries, treatable by laypersons or first aiders. | 0 to 1,000 EUR | Incident is noted internally only. |
| 2 | low | 1,000 to 10,000 EUR | Minor injuries requiring outpatient treatment; absence no longer than three working days. | 1,000 to 10,000 EUR | Perception in the organization’s close environment; isolated negative statements. |
| 3 | medium | 10,000 to 100,000 EUR | More severe injuries requiring outpatient treatment; absence longer than three working days. | 10,000 to 100,000 EUR | Active perception by customers, suppliers, or partners; negative consequences are threatened. |
| 4 | high | 100,000 to 1,000,000 EUR | More severe injuries requiring inpatient treatment. | 100,000 to 1,000,000 EUR | Loss of individual customers, partners, or employees. |
| 5 | very high | Over 1,000,000 EUR | Most severe injuries requiring intensive care treatment or worse. | Over 1,000,000 EUR | Extensive public reporting; loss of several customers, partners, or employees. |

**Assessment rule:**

```text
Damage factor = max(property damage, personal injury, financial loss, intangible damage)
```

Organizations may adapt thresholds to size, sector, and risk-bearing capacity. The adaptation must be approved and documented in the decision log.

## Risk Value and Risk Category

```text
Risk value = likelihood factor × damage factor
```

| Risk value | Category | Basic logic |
| --- | --- | --- |
| 1 to 2 | very low | Usually acceptable without further treatment, provided it is documented. |
| 3 to 6 | low | Usually acceptable; measures possible but not mandatory. |
| 7 to 12 | medium | Treatment, reasoned acceptance, or management decision required. |
| 13 to 19 | high | Prioritize treatment; management visibility required. |
| 20 to 25 | very high | Escalate immediately; management decision and measures path required. |

Note: The value 20 is treated as very high because it represents the combination of maximum damage with high likelihood or maximum likelihood with high damage.

## Strategy Decision and Treatment Options

After the gross assessment, a strategy is selected or prepared as a management decision. From a risk value of 7 onward, the risk must be actively assessed. Permissible strategies:

| Strategy | Meaning | Human gate |
| --- | --- | --- |
| Minimize / treat | Measures reduce likelihood, damage extent, or both factors. | Measures approval by affected owners; resource decision if needed. |
| Transfer | Impacts or response components are transferred to third parties, e.g., insurance, outsourcing, or structured handover of specific damage response into crisis management / BCMS. | Management approval and contract/data protection review where relevant; residual risk remains visible. |
| Accept | Residual risk is deliberately carried because other strategies are not appropriate. | Management decision; document rationale, duration, and review date. |
| Avoid | Process, processing activity, system, service, or step is ended or changed. | Owner and management decision; review operational impact. |

Very low and low risks can be accepted by the asset owner if the organization has approved this approach. Risks assessed as medium, high, and very high require visible treatment or a management decision.

## Deriving Measures

Measures are not taken from a generic control list, but derived from the specific risk scenario:

1. Which vulnerability should be reduced or eliminated?
2. Which threat should be prevented, made more difficult, detected, or limited?
3. Which asset or process should be protected?
4. Does the measure affect likelihood, damage extent, or both?
5. Which existing or planned measure is to be referenced in the control taxonomy or SoA?
6. Which evidence will later show that the measure has been implemented and is effective?

Each measure needs at least:

- measure ID,
- risk reference,
- SoA/control reference,
- owner,
- status,
- due date,
- evidence source,
- effectiveness review point,
- decision point for blockers.

## ISO 27001 and SoA Boundary

A Statement of Applicability (SoA) requires the organization to use its own license-compliant ISO/IEC 27001 basis or its own control taxonomy. krisensicherOS therefore does not provide ISO 27001 controls, Annex A texts, or a complete normative SoA.

krisensicherOS only provides the **SoA-capable working structure**:

- connect risks with measures and control references,
- justify existing and planned measures,
- document applicability, non-applicability, or rejection,
- link evidence and effectiveness review,
- make gaps visible for management review.

If no ISO 27001 SoA exists, the same structure can initially be used as an organization-specific **Risk-Control Map**. Later transfer into an SoA is performed by technically responsible persons based on the licensed standard and organization-specific decisions.

## Control/SoA and Measures Mapping

The SoA is not just a standards table. In krisensicherOS, a Risk-Control Map is maintained first; if an ISO 27001 SoA has been created for the organization, it can connect to it. The structure connects risk, decision, measure, routine, and evidence.

For each relevant risk, the following is checked:

- Which existing measures reduce net risk?
- Which planned measures should achieve the net/residual risk as a planned value?
- Which control clusters, internal control IDs, or SoA entries are affected?
- Which measure is implemented, planned, rejected, or not applicable?
- Which evidence is generated from operating the measure?
- Which risks remain as residual risk despite measures?

References to ISO 27001 or other licensed standards may only be maintained as the organization’s own metadata, IDs, control titles, or organization-specific summaries. Do not copy standard texts into public artifacts.

## Reporting and Reporting Routine

Reporting must be derivable from the risk register. krisensicherOS supports Markdown, table, and HTML outputs for this. A report should contain at least:

- scope, reporting period, and assessment status,
- risk matrix and criteria used,
- top risks by gross and net/residual risk,
- strategy per risk: acceptance, avoidance, transfer, or minimization,
- open management decisions, risk acceptances, and transfers,
- measures status, overdue measures, and effectiveness reviews,
- SoA/control mapping and gaps,
- changes since the last review.

For management reviews, an HTML presentation with colored risk badges, measures status, and decision boxes is suitable. See `templates/risikoreport-html.html`.

## Review and Reporting Routine

| Routine | Minimum content | Frequency / trigger |
| --- | --- | --- |
| Risk workshop | New risks, changed risks, measures status, control/SoA gaps, escalations. | At least quarterly or after material changes. |
| Risk review per entry | Currency of asset, vulnerability, threat, gross and net/residual risk assessment, measures, and evidence. | At least annually or event-driven. |
| Measures review | Overdue measures, blockers, evidence, effectiveness, and residual risk planned value. | Monthly or aligned with the governance cadence. |
| Management review | Top risks, residual risks, acceptances, resource needs, material SoA decisions. | At least annually and event-driven for high / very high risks. |

## Minimum Evidence

- current risk register,
- Risk-Control/SoA mapping,
- measures list with status and owners,
- decision log for risk acceptances and criteria changes,
- review or workshop notes,
- evidence for implementation and effectiveness of central measures,
- management review excerpt on top risks and residual risks.

## Boundaries

- This methodology is a working model and does not provide legal advice.
- It does not replace an organization-specific risk decision.
- It does not confirm ISO, NIS2, or other conformity.
- It must not include confidential customer data, personal data, or licensed standard texts in public examples.
