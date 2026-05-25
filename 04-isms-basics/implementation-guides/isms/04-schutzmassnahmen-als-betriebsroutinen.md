<!-- kso:product-relevance
repo-scope: product
classification: implementation-guide-module
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->

# 04 — Protective Measures as Operating Routines

## Purpose

This module turns protective measures into concrete ways of working. A measure is only useful when owner, trigger, process, evidence, escalation, and review are clear.

## Reference Framework

- ISO/IEC 27001:2022 — Sections 6.1, 8.1, and Annex A as reference anchors.
- BSIG § 30 in case of possible applicability.

## Users and Roles

- Control owner,
- information security officer/CISO,
- IT/OT/service owner,
- process owners,
- evidence owner,
- internal review role.

## Trigger

- Risk requires a measure,
- existing measure cannot be evidenced,
- technical or organizational change,
- finding or incident,
- management prioritizes protection need.

## Process

1. Derive the measure from a risk or work requirement.
2. Describe the operating routine: purpose, owner, trigger, steps, output.
3. Determine the evidence source: log, ticket, minutes, configuration, review note.
4. Define escalation: When is the routine considered violated or blocked?
5. Define the review method: sample, test, review, technical check, or management report.
6. Link the measure in the backlog and in the risk-control map.

## Decisions

| Decision | Options | Human Gate |
| --- | --- | --- |
| Measure mandatory? | yes / no / pilot | ISMS owner / management |
| Implementation sufficient? | yes / partial / no | Control owner + reviewer |
| Allow exception? | no / time-limited / with condition | Risk owner / management |
| Evidence sufficient? | yes / incomplete / missing | Evidence owner |

## Evidence

- Control routine description,
- measures backlog,
- technical or organizational evidence,
- exception decisions,
- effectiveness checks,
- review notes.

## Review

Review questions:

- Does the measure reduce a named risk?
- Is it actually performed?
- Is there usable evidence?
- Are exceptions decided and time-limited?
- Is the effort manageable?

## BSIG/NIS2 Relation

In case of possible applicability, protective measures can help translate risk management requirements into operational routines. The specific legal relevance remains to be assessed.

## Boundaries

No reproduction of ISO control texts, no security guarantee, no technical architecture decision without the responsible specialist role.

## Handoffs

- to IT/OT operations,
- to service owner,
- to risk owner,
- to evidence owner,
- to management in case of exceptions or resource needs.
