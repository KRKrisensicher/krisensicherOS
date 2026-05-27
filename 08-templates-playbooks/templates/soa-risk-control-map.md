# Risk-Control Map / SoA Extension

## Purpose

This template connects risks, existing and planned measures, control references, evidence, and decisions. It helps operate risk analyses not as an isolated list, but linked to the measure and control system of the ISMS.

If an organization creates an ISO 27001 Statement of Applicability (SoA), this template can be used as a SoA extension. However, krisensicherOS does not provide ISO 27001 controls or standard texts. For an ISO 27001 SoA, the organization needs its own license-compliant standard basis and expert approval.

## Trigger

Use when:

- a risk has been assessed or reassessed,
- measures are derived from a risk,
- an internal control taxonomy or a later SoA is maintained, updated, or prepared for a review,
- existing measures need to be evidenced or planned measures need to be prioritized.

## Users

- information security officer / CISO / ISMS owner,
- risk owner / asset owner,
- control owner,
- management review facilitator,
- internal audit or review role.

## Operating logic

1. Reference the risk from the risk analysis register.
2. Identify existing measures that actually reduce the confirmed net risk.
3. Identify planned measures intended to reach the net/residual risk target value.
4. Maintain control/SoA references with status and rationale.
5. Define evidence source and effectiveness check.
6. Transfer open decisions into the decision log.

## Mapping fields

| Field | Entry |
| --- | --- |
| Mapping ID | M-001 |
| Risk ID | R-001 |
| Risk scenario summary |  |
| Asset / process / service |  |
| Vulnerability |  |
| Threat |  |
| Net risk value / category |  |
| Net/residual risk | Target value / confirmed |
| Control/SoA ID | organization-specific ID, control cluster, or SoA reference |
| Control/SoA status | implemented / planned / partially implemented / not applicable / rejected |
| Rationale for the control/SoA decision | Why is the measure relevant, planned, not applicable, or rejected? |
| Measure / control routine |  |
| Effect on risk | Likelihood / impact / both / no direct effect |
| Expected effect | Which assessment should change, and why? |
| Existing or planned measure | existing / planned |
| Measure ID / ticket / backlog link |  |
| Measure owner |  |
| Evidence source | Minutes, ticket, configuration, review note, test evidence, training evidence, etc. |
| Evidence quality | complete / partial / missing / not reviewed |
| Effectiveness check | Method, timing, reviewer |
| Decision needed | Risk acceptance / resources / scope / exception / none |
| Decision log reference |  |
| Review cadence | monthly / quarterly / annually / event-driven |
| Next review |  |

## Control/SoA decision logic

| Status | Use | Minimum rationale |
| --- | --- | --- |
| implemented | Measure is in place, operated, and evidencable. | Which routine produces which evidence? |
| planned | Measure has been decided or proposed, but is not yet effective. | Which risk should be reduced, who decides resources, by when? |
| partially implemented | Measure exists, but only partially covers scope, evidence, or effect. | Which gap remains, which residual risk arises? |
| not applicable | Control does not fit the scope, asset, or risk scenario. | Why not applicable, who reviewed this? |
| rejected | Measure was deliberately not pursued. | Why rejected, which risk acceptance or alternative exists? |

## Deriving measures

A measure is well formulated when it answers all questions:

- Which vulnerability is reduced?
- Which threat is prevented, made more difficult, detected, or limited?
- Which asset or process is affected?
- Does the measure reduce likelihood, impact, or both?
- Which evidence shows implementation?
- Which check shows effectiveness?
- Which control/SoA reference is maintained as a result?

## Output

- traceable connection between risk, measure, control/SoA reference, and evidence,
- list of planned measures with owners and decision points,
- visible control/SoA gaps and controls without evidence,
- input for management review and measure prioritization.

## Boundaries

This template does not replace interpretation of standards, certification advice, or risk acceptance. Licensed standard texts are not included. ISO 27001 references remain IDs, own short descriptions, or organization-specific mappings based on the licensed standard.
