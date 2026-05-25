<!-- kso:product-relevance
repo-scope: product
classification: product-governance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; product-safety; release-readiness
-->

# Quality Rules

## Purpose

These quality rules apply to krisensicherOS artifacts: agent profiles, skills, templates, playbooks, workflows, examples, source registers, and documentation.

## 1. No artifact without operating logic

Every template, skill, playbook, and workflow must answer:

- Who uses it?
- When is it used?
- What is it used for?
- What inputs does it need?
- What steps does it perform?
- Which decision does it support?
- What evidence is produced?
- Who reviews or approves it?
- When is it reviewed?

## 2. No compliance phrases

Unclear terms are operationalized:

- “regularly” → specific frequency or trigger
- “appropriate” → criteria and decision scope
- “ensure” → role, control, evidence, and review
- “promptly” → time window or escalation point
- “relevant” → scope, risk, or decision relevance

## 3. No false assurance

Artifacts must not suggest legal, data protection, audit, security, or certification guarantees.

Permitted are:

- questions,
- checkpoints,
- working assumptions,
- evidence needs,
- decision options,
- handoffs to human roles.

Not permitted are:

- binding legal interpretation,
- data protection assessment as an agent decision,
- compliance confirmation,
- certification assurance,
- security guarantee,
- risk acceptance without a responsible person.

## 4. Protect CISO/information security officer time

Routine work should be prepared, compressed, or reviewed. Management and responsibility decisions must remain visible.

An artifact is only valuable if it improves at least one of the following:

- decision readiness,
- evidence quality,
- prioritization,
- handoff clarity,
- review capability,
- operational implementation.

## 5. Responsibility remains human

Agents relieve workload, structure, and review. They do not replace accountability.

The following always remain human:

- legal assessment,
- data protection assessment,
- contract interpretation,
- risk acceptance,
- management decision,
- external communication,
- publication.

## 6. Governance instead of documentation

Documents are by-products of functioning routines, not the goal.

A document without an owner, trigger, output, evidence, and review is not complete.

## 7. Public-safe by default

Public artifacts contain:

- fictional examples,
- public source references,
- metadata,
- own summaries,
- empty user fields.

Public artifacts do not contain:

- real customer data,
- personal data,
- confidential contract content,
- secrets,
- private runtime/workspace details,
- licensed standard texts.

## 8. Tool neutrality

Canonical subject-matter logic resides in the repo:

- `agents/public/`,
- `skills/`,
- `templates/`,
- `playbooks/`,
- `workflows/`,
- `evals/`,
- `governance/`.

Adapters may execute, but must not create divergent subject-matter logic.

## 9. Review obligation

New or changed artifacts are checked against `evals/quality-gates.md` and the review process.

Minimum evidence:

- public safety checked,
- claim safety checked,
- operating logic checked,
- workload checked,
- handoffs checked,
- human gates visible.
