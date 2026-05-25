<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# 06 Evidence & Management Review

This module structures evidence, audit questions, findings, remediation, effectiveness review, and management decisions.

**Operating logic:** Ensures that evidence comes from real governance work and that management reviews lead to decisions.

## Start here

1. Collect existing evidence with [`templates/evidence-pack-index.md`](templates/evidence-pack-index.md).
2. Request missing evidence specifically through [`templates/evidence-request-list.md`](templates/evidence-request-list.md).
3. Test controls with [`templates/control-test-plan.md`](templates/control-test-plan.md) and [`evals/quality-gates.md`](evals/quality-gates.md).
4. Document findings through [`templates/audit-finding-report.md`](templates/audit-finding-report.md) and measures through [`templates/corrective-action-plan.md`](templates/corrective-action-plan.md).
5. Prepare management decisions with [`templates/management-review-agenda.md`](templates/management-review-agenda.md) and the [`decision log`](../02-governance-operating-model/templates/decision-log.md).

## Operating flow

`Gap from 03 → risk/controls from 04 → evidence request → control test/finding → corrective action → effectiveness review → management review → decision log`

## Key artifacts

- [`workflows/evidence-management-review.yaml`](workflows/evidence-management-review.yaml) — evidence pack and review workflow.
- [`workflows/audit-evidence-remediation-chain.yaml`](workflows/audit-evidence-remediation-chain.yaml) — audit-finding-remediation chain.
- [`playbooks/evidence-pack-prep.md`](playbooks/evidence-pack-prep.md) — prepare an evidence pack.
- [`playbooks/management-review-prep.md`](playbooks/management-review-prep.md) — prepare a management review.
- [`playbooks/monthly-security-governance-review.md`](playbooks/monthly-security-governance-review.md) — recurring governance routine.

## Human gates

Evidence assessment, finding severity, risk acceptance, measure prioritization, deadlines, management decisions, and external communication must be reviewed and approved by humans.

## Typical outputs

- evidence pack,
- evidence requests,
- audit or control-test findings,
- corrective actions,
- effectiveness review,
- management review decisions in the decision log.
