---
name: corrective-action-planner
version: 1.0.0
description: "Turn findings and gaps into actions with cause, owner, due date, evidence, and review."
category: evidence
inputs:
  - scope
  - requirements-or-findings
  - existing-evidence
  - owners-and-constraints
outputs:
  - corrective-action-plan
  - action-backlog
  - decision-log-entry
requires_human_review: true
---


# corrective-action-planner

## Purpose

This skill structures actions from findings or gaps with cause, target state, owner, evidence, and review point.

The skill does not provide legal advice, data protection advice, audit, compliance, or certification assurance, and does not make management decisions.

## When to use

Use the skill when audit findings, document gaps, control test results, or management decisions need to be turned into actionable measures.

Typical triggers:

- internal audits or self-assessments,
- NIS2/ISMS/BCMS gap work,
- evidence pack or management review preparation,
- findings, deviations, observations, or action reviews,
- new or changed requirements from register entries.

## When not to use

Do not use for:

- binding interpretation of law, standards, or contracts,
- data protection assessment,
- external audit, assessment, or certification assurance,
- risk acceptance or management decision,
- live incident steering,
- reproduction of licensed standard texts,
- public processing of confidential or personal content.

## Input data

Required:

- **Scope:** process, control, audit area, finding, or action.
- **Criteria:** requirements, register entries, control references, or own summaries.
- **Current state:** existing evidence, open gaps, findings, or action status.
- **Owner/deadline information:** where known.

Optional:

- assessment scale or audit methodology,
- risk context,
- existing evidence packs,
- management decisions or decision logs,
- sampling or test method specifications.

Assumptions:

- Missing evidence is marked as a gap.
- Unclear responsibilities are not invented, but shown as items requiring clarification.

## Prerequisites

Helpful artifacts:

- `templates/corrective-action-plan.md`
- `templates/decision-log.md`
- `templates/audit-finding-report.md`
- `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md`
- `02-governance-operating-model/governance/review-process.md`

Helpful roles:

- business or process owner,
- information security officer/CISO or GRC responsible role,
- internal audit or audit responsible role,
- management role for risk or resource decisions.

## Workflow

1. **Define scope and criterion**  
   Define which process, control, finding, or action area is being considered and which criteria apply.

2. **Separate current state and evidence**  
   Distinguish confirmed evidence, claims, assumptions, open points, and missing evidence.

3. **Derive operating logic**  
   Translate criteria into concrete requests, tests, actions, or review questions. Record owner, deadline, quality, and escalation.

4. **Mark risk and decision relevance**  
   Show which gaps have operational relevance and where management, risk, or resource decisions are needed.

5. **Complete output artifact**  
   Generate the appropriate template with traceable fields, not only free text.

6. **Prepare handoffs**  
   Forward open points to owners, audit responsible roles, evidence reviewers, or management review.

7. **Perform verification**  
   Check public safety, claim safety, source/evidence reference, operating logic, workload, human gates, and handoffs.

## Output artifacts

Depending on the assignment, the skill generates:

- corrective-action-plan
- action-backlog
- decision-log-entry
- open questions and assumptions,
- handoff to owner, audit, or management review,
- verification note.

## Human-in-the-loop

Human review is required for:

- legal, normative, or contractual interpretation,
- data protection assessment,
- final audit assessment or finding classification,
- action approval and resource decision,
- risk acceptance,
- closure or reopening of findings,
- external communication.

## Verification

```text
Verification:
- Public-Safety: pass / notes / stop
- Claim-Safety: pass / notes / stop
- Criteria reference: pass / notes / stop
- Evidence reference: pass / notes / stop
- Operating logic: pass / notes / stop
- Workload: pass / notes / stop
- Human Review: pass / notes / stop
- Handoffs: pass / notes / stop
- Result: pass / pass with notes / stop
```

Minimum questions:

- Are scope, criteria, owner, and target output clear?
- Are sources referenced or summarized only in permitted ways?
- Are evidence, assumptions, and gaps clearly separated?
- Is it visible who must act, review, or decide?
- Were no guarantees, final compliance statements, or management decisions asserted?

## Quality gates

To be applied from `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md`:

- U1 Public-Safe Gate,
- U2 Claim-Safety Gate,
- U3 Operating Logic Gate,
- U4 Empowerment Gate,
- U5 Workload Gate,
- U6 Portability Gate,
- A2 Skill Gate,
- A3 Template Gate,
- A8 Sources/Register Gate.

## Handoffs

Typical handoffs:

- to `internal-audit-planner` for audit planning,
- to `control-evidence-architect` for evidence and control mapping,
- to `audit-finding-reviewer` for findings,
- to `evidence-pack-reviewer` for evidence pack review,
- to `management-review-facilitator` for decision and review points,
- to `agent-quality-and-safety-reviewer` for claim, confidentiality, and workload review.

## Boundaries and red lines

This skill does not provide legal advice, data protection advice, certification, audit, or compliance assurance, and does not make management decisions.

It must not transfer confidential content, personal data, real customer data, or licensed standard texts into public artifacts.

It must not invent evidence, smooth over gaps, or confirm actions as effective without marking a review basis and human approval.

## Example

From a fictional finding note about missing owners, a cause hypothesis, immediate action, structural action, owner, deadline, evidence, and management handoff are created.

Good output:

- Criterion and scope are traceable.
- Evidence need, test, action, or review question is concrete.
- Owner, deadline, quality, and handoff are visible.
- Assumptions and human gates are marked.

Poor output:

- “Everything is complete; the finding can be closed without further review.”

Why poor:

- This creates false assurance, replaces human assessment, and asserts an impermissible assurance.

## Definition of Done

The skill is complete when:

- scope, criteria, and current state are documented,
- evidence, assumptions, and gaps are separated,
- output artifact and handoffs are available,
- human review and decision points are marked,
- verification is documented,
- next steps for owner, audit, or management review are clear.
