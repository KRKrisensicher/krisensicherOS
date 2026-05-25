<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Workflows

Workflows connect agents, skills, templates, registers, and human approval points into operable flows.

## Operating flow across modules

`02 Governance model → 03 gap → 04 risk/controls → 06 evidence/review → decision log`

## Workflow baseline v1.0

- [`governance-operating-model.yaml`](../../02-governance-operating-model/workflows/governance-operating-model.yaml) — translate requirements into roles, routines, evidence, and decisions.
- [`nis2-readiness-gap.yaml`](../../03-nis2-readiness/workflows/nis2-readiness-gap.yaml) — capture and prioritize NIS2 readiness gaps.
- [`nis2-vorab-betroffenheitspruefung.yaml`](../../03-nis2-readiness/workflows/nis2-vorab-betroffenheitspruefung.yaml) — prepare NIS2 preliminary assessment with legal handoff.
- [`minimum-viable-isms.yaml`](../../04-isms-basics/workflows/minimum-viable-isms.yaml) — design ISMS start mode with scope, risk, controls, evidence, and review.
- [`isms-risk-to-soa.yaml`](../../04-isms-basics/workflows/isms-risk-to-soa.yaml) — assess risks, derive measures, and map them to control/SoA entries.
- [`nis2-incident-and-management-readiness.yaml`](../../05-incident-crisis-readiness/workflows/nis2-incident-and-management-readiness.yaml) — connect incident/notification readiness and management readiness.
- [`evidence-management-review.yaml`](../../06-evidence-management-review/workflows/evidence-management-review.yaml) — review evidence packs and prepare management review.
- [`audit-evidence-remediation-chain.yaml`](../../06-evidence-management-review/workflows/audit-evidence-remediation-chain.yaml) — connect audit question, test, evidence request, finding, corrective action, effectiveness, and review.
- [`eu-ai-act-readiness-precheck.yaml`](../../07-ai-governance-agents/workflows/eu-ai-act-readiness-precheck.yaml) — inventory AI systems and mark handoff questions.

## Workflow gate

Before use, check trigger, inputs, outputs, agents/skills/templates, stop points, human gates, and decision value.
