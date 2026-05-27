# Risk Analysis Session State

## Purpose

This template records the state of a guided risk analysis. It makes it possible to pause the dialog-based risk process, continue it later, and keep open questions, assumptions, human gates, and artifact outputs traceable.

It is a working state, not a final risk report.

## Usage

- maintain one session state file or section per risk scenario,
- update after each dialog phase,
- keep open mandatory fields and human gates visible,
- transfer to the register, Risk-Control Map / SoA extension, or report only after business confirmation.

## State Header

| Field | Entry |
| --- | --- |
| Session ID | RS-001 |
| Risk ID | R-001 or open |
| Title / short name |  |
| Scope / area |  |
| current process step | 0 Start / 1 Risk / 2 Current measures / 3 Gross / 4 Strategy / 5 Measures+Controls/SoA / 6 Net / 7 Reporting |
| Status | in progress / waiting for owner / waiting for management / ready for review / completed |
| last update | Date |
| next appointment / review | Date |

## Phase 1: Describe Risk

| Mandatory field | Value | Status |
| --- | --- | --- |
| Asset / process / service |  | open / assumption / confirmed |
| Asset owner / business owner |  | open / assumption / confirmed |
| Vulnerability |  | open / assumption / confirmed |
| Threat |  | open / assumption / confirmed |
| Impact |  | open / assumption / confirmed |
| Risk scenario | If [Threat] exploits the vulnerability [Vulnerability] on asset [Asset], then [Impact] may occur. | open / assumption / confirmed |

## Phase 2: Current Measures

| Measure field | Description | Evidence | Status |
| --- | --- | --- | --- |
| organizational measures |  |  | open / assumption / confirmed / evidence-reviewed |
| technical measures |  |  | open / assumption / confirmed / evidence-reviewed |
| process-related / personnel measures |  |  | open / assumption / confirmed / evidence-reviewed |
| monitoring / detection / review |  |  | open / assumption / confirmed / evidence-reviewed |
| incident response / crisis management / BCMS |  |  | open / assumption / confirmed / evidence-reviewed |
| current control-/SoA references |  |  | open / assumption / confirmed |

## Phase 3: Gross Risk

| Criterion | Value 1-5 | Rationale |
| --- | --- | --- |
| Detectability |  |  |
| Exploitability |  |  |
| Hiddenness |  |  |
| Probability factor | max(...) |  |
| Property damage |  |  |
| Personal injury |  |  |
| financial loss |  |  |
| intangible damage |  |  |
| Impact factor | max(...) |  |
| Gross risk value / category | W × S |  |

## Phase 4: Strategy

| Field | Entry |
| --- | --- |
| Strategy options | Acceptance / avoidance / transfer / reduction |
| recommended strategy as preparation |  |
| Rationale |  |
| rejected options |  |
| Human Gate | who must decide? |
| Decision log reference |  |

## Phase 5: Measures and Control-/SoA Mapping

| Measure | Effect | Owner | Due | Control-/SoA relation | Evidence | Effectiveness review | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | likelihood / impact level / both |  |  |  |  |  | planned / in implementation / implemented / effectiveness-reviewed |

## Phase 6: Net-/Residual Risk

| Criterion | Value 1-5 | Rationale |
| --- | --- | --- |
| Assessment status | planned value / confirmed |  |
| Detectability |  |  |
| Exploitability |  |  |
| Hiddenness |  |  |
| Probability factor | max(...) |  |
| Property damage |  |  |
| Personal injury |  |  |
| financial loss |  |  |
| intangible damage |  |  |
| Impact factor | max(...) |  |
| Net-/residual risk value / category | W × S |  |
| Change compared to gross |  |  |

## Phase 7: Reporting

| Report field | Status / content |
| --- | --- |
| Top risk relevant? | yes / no |
| Management decision open? |  |
| Measures status reportable? |  |
| Control-/SoA gap reportable? |  |
| HTML report desired? | yes / no |
| Report reference |  |

## Open Questions

| Question | to whom | by when | Status |
| --- | --- | --- | --- |
|  |  |  | open / answered / escalated |

## Assumptions

| Assumption | Risk if assumption is incorrect | Review by | Status |
| --- | --- | --- | --- |
|  |  |  | open / confirmed / rejected |

## Human Gates

| Decision | Decision-maker | prepared by | Deadline | Status |
| --- | --- | --- | --- | --- |
| Risk acceptance |  |  |  | open / decided |
| Transfer |  |  |  | open / decided |
| Avoidance |  |  |  | open / decided |
| Resources for measures |  |  |  | open / decided |
| Criteria change |  |  |  | open / decided |

## Artifact Transfer

| Target artifact | Entry transferred? | Reference |
| --- | --- | --- |
| Risk analysis register | no / yes |  |
| Risk-Control Map / SoA extension | no / yes |  |
| Measures list / backlog | no / yes |  |
| Decision log | no / yes |  |
| Risk report | no / yes |  |

## Boundaries

This Session State must not contain real customer, personal, or confidential organizational data if used as a public example. Risk acceptance and management decisions remain human gates.
