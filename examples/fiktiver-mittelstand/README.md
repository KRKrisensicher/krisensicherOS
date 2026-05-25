<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Fictional Example: Mid-sized Organization

## Fictional Nature

This example is entirely fictional. It contains no real organizational, customer, personal, contract, incident, or system data.

## Starting Point

A fictional mid-sized organization operates a digital core service and several internal IT processes. Security responsibility exists, but roles, evidence, and management decisions are not yet cleanly connected.

## Objective

Set up a small governance start for krisensicherOS:

- clarify scope,
- capture NIS2 readiness gaps,
- set up a minimum viable ISMS,
- prepare an evidence pack,
- make the management review ready for decisions.

## Agents Used

- `compliance-operating-system-lead`
- `security-governance-architect`
- `nis2-readiness-analyst`
- `isms-operating-model-designer`
- `risk-and-obligation-prioritizer`
- `control-evidence-architect`
- `management-review-facilitator`
- `agent-quality-and-safety-reviewer`

## Skills Used

- `governance-operating-model`
- `nis2-gap-assessment`
- `minimum-viable-isms`
- `risk-prioritization`
- `evidence-pack-review`
- `management-review-prep`

## Templates Used

- `templates/governance-operating-model-canvas.md`
- `templates/nis2-gap-worksheet.md`
- `templates/isms-scope-canvas.md`
- `templates/evidence-pack-index.md`
- `templates/management-review-agenda.md`
- `templates/decision-log.md`

## Guided Mini Walkthrough

See [`nis2-minidurchstich.md`](nis2-minidurchstich.md) for a concrete NIS2 mini walkthrough with source/requirement, gap, audit question, evidence request, and management decision point.

See [`isms-90-minuten-durchstich.md`](isms-90-minuten-durchstich.md) for a compact ISMS walkthrough with scope, three risks, three measure routines, evidence pack, and review date.

## Example Flow

1. Limit the scope to the digital core service and two supporting IT processes.
2. Capture sources and register entries only as references.
3. Formulate NIS2 readiness gaps as role, routine, evidence, or decision gaps.
4. Start the minimum viable ISMS with a small number of control routines.
5. Create an evidence pack index for the most important evidence.
6. Prepare the management review with three decisions.
7. Review claim safety and workload.

## Example Output

### Scope

- Start scope: digital core service, operations team, change process, backup/restore routine.
- Out of scope: all other business processes, as long as there is no dependency on the core service.

### Top Gaps

| Gap | Evidence Need | Decision |
| --- | --- | --- |
| Restore evidence is not bundled in a reviewable way | Restore test note and measure log | Confirm review cadence and owner |
| Risk acceptance is not documented | Decision log | Management decides on residual risk |
| Supplier dependency is only informally known | Register entry and escalation path | Name owner for third-party review |

### Next Measures

| Measure | Proposed Owner | Evidence | Review |
| --- | --- | --- | --- |
| Create evidence pack index for restore routine | Service owner | Evidence pack | next monthly review |
| Add role matrix for core service | Security-responsible role | Role matrix | Management review |
| Start decision log for risk acceptance | Management review facilitator | Decision log | quarterly |

## Limits

This example does not confirm regulatory fulfillment, certification capability, or security. Legal review, data protection assessment, risk acceptance, and management decisions remain human.
