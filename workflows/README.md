<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Workflows

Workflows connect agents, skills, templates, registers, and human approval points into operable processes.

They are intentionally tool-neutral. A workflow describes domain logic and handoffs; concrete execution in Claude, Codex, OpenClaw, Hermes, or other systems is handled through thin adapters.

## Ground Rules

- Every workflow has scope, triggers, inputs, steps, outputs, stop points, and human gates.
- Agents assist; they do not assume responsibility.
- Legal interpretation, data protection assessment, risk acceptance, management decisions, and external communication remain human tasks.
- Public examples remain fictional and contain no real organizational, customer, or personal data.
- Licensed standards and confidential requirements are used only as metadata, references, or proprietary summaries.

## Base Set v1.0

- `governance-operating-model.yaml` — Translate requirements into roles, routines, evidence, and decisions.
- `nis2-readiness-gap.yaml` — Structurally capture and prioritize NIS2 readiness gaps.
- `minimum-viable-isms.yaml` — Design an ISMS start mode with scope, risk, controls, evidence, and review.
- `isms-risk-to-soa.yaml` — Assess ISMS risks using gross/net methodology, derive measures, and map them to control/SoA entries.
- `evidence-management-review.yaml` — Review evidence packs and prepare management review.
- `audit-evidence-remediation-chain.yaml` — Connect requirement, audit question, audit program, evidence request, finding, corrective action, effectiveness review, and management review.
- `eu-ai-act-readiness-precheck.yaml` — Inventory AI systems, flag risk signals, and prepare legal/data protection/management handoffs.

## Workflow Gate

Check before use:

- Are trigger, inputs, and output clear?
- Are agents, skills, and templates explicitly connected?
- Are there stop/escalation points?
- Are human gates visible before legal, data protection, management, or external statements?
- Does the workflow create decision readiness instead of bureaucracy?
