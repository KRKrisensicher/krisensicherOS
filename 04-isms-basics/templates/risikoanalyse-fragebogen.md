<!-- kso:product-relevance
repo-scope: product
classification: template
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->

# Risk Analysis Questionnaire

## Purpose

This questionnaire supports capturing the current status of measures before the gross assessment and prepares the later strategy, measures, and net/residual risk assessment.

It can be evaluated by AI so that answers can be transferred in a structured way into the risk analysis register and the Risk-Control Map / SoA extension. Subject-matter confirmation remains with the asset owner, information security officer/CISO, and, where applicable, management.

## Use with AI

SoA optional: Questions on control/SoA references can initially target an internal control taxonomy. ISO 27001 SoA references may only be finalized based on the organization’s own licensed standard basis.

AI may:

- cluster answers,
- flag missing information,
- convert vulnerability, asset, and threat into a risk scenario,
- structure notes on existing measures and evidence sources,
- mark possible control/SoA references as hypotheses,
- suggest measure options.

AI must not:

- decide risk acceptance,
- claim effectiveness without evidence,
- replace legal or data protection assessments,
- transfer confidential content into public artifacts.

## Questionnaire

### 1. Risk and Scope Description

| Question | Answer |
| --- | --- |
| Which process, service, location, service provider, or system is affected? |  |
| Which asset or information value is affected? |  |
| Who is the asset owner or subject-matter owner? |  |
| Which vulnerability, gap, or insecure property makes the risk possible? |  |
| Which threat can exploit this vulnerability? |  |
| What impact would be realistic? |  |
| Which assumptions are still unclear? |  |

### 2. Current Status of Measures

| Question | Answer |
| --- | --- |
| Which organizational measures already exist? |  |
| Which technical measures already exist? |  |
| Which personnel-related or procedural measures already exist? |  |
| Which detection, monitoring, or review mechanisms exist? |  |
| Which incident response, crisis management, or BCMS capabilities limit the damage? |  |
| Which measures are operated regularly and not only documented? |  |
| Which measures are informal, unreviewed, or dependent on individuals? |  |

### 3. Evidence and Control/SoA Reference

| Question | Answer |
| --- | --- |
| Which evidence shows that the current measures exist? |  |
| Which evidence shows that the measures are operated effectively? |  |
| Which control/SoA IDs or control clusters are affected? |  |
| Which control/SoA entries are missing, planned, or unclear? |  |
| Which evidence gaps exist? |  |

### 4. Prepare Gross Assessment

| Question | Answer |
| --- | --- |
| How visible is the vulnerability without optimistic offsetting by measures? Value 1-5 with rationale. |  |
| How exploitable is the vulnerability without optimistic offsetting by measures? Value 1-5 with rationale. |  |
| How hidden would exploitation be without optimistic offsetting by measures? Value 1-5 with rationale. |  |
| What property damage would be plausible? Value 1-5 with rationale. |  |
| What personal injury would be plausible? Value 1-5 with rationale. |  |
| What financial loss would be plausible? Value 1-5 with rationale. |  |
| What intangible damage would be plausible? Value 1-5 with rationale. |  |

### 5. Strategy Options

| Question | Answer |
| --- | --- |
| Can the risk be accepted? If yes, why and by whom? |  |
| Can the risk be avoided, e.g., by shutdown, process change, or scope change? |  |
| Can the risk be transferred, e.g., insurance, outsourcing, crisis management, or BCMS? |  |
| Can the risk be minimized through measures? |  |
| Which decision requires management, information security officer, asset owner, or another body? |  |

### 6. Measures Planning and Residual Risk

| Question | Answer |
| --- | --- |
| Which measure reduces which vulnerability? |  |
| Which measure prevents, complicates, detects, or limits which threat? |  |
| Which measure lowers likelihood of occurrence, impact level, or both? |  |
| Who is the measure owner? |  |
| By when should the measure be implemented? |  |
| Which evidence results from implementation and operation? |  |
| How is effectiveness reviewed? |  |
| Which net/residual risk assessment is plausible after measures planning? |  |
| Is this assessment a planned value or already confirmed? |  |

## AI Output Format

```text
1. Risk scenario:
2. Current status of measures:
3. Evidence status and gaps:
4. Gross assessment proposal with rationale:
5. Strategy options:
6. Measure proposals with control/SoA reference:
7. Net/residual risk assessment proposal:
8. Human gates / open decisions:
9. Reporting notes:
```

## Output

- structured preparatory work for the risk analysis register,
- open questions for owners,
- measure and control/SoA mapping hypotheses,
- decision needs for management review.
