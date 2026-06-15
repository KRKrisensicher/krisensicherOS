---
name: incident-escalation-playbook
version: 1.0.0
description: "Design incident escalation with triggers, roles, communications, decisions, and follow-up."
category: incident
inputs:
  - scope
  - existing-artifacts
  - risks-or-findings
  - evidence-sources
outputs:
  - incident-escalation-card
  - decision-brief
  - action-backlog
requires_human_review: true
---


# incident-escalation-playbook

## Purpose

This skill helps user organizations design incident escalation logic with triggers, roles, communication points, decisions, and follow-up.

It creates operable work artifacts with owners, triggers, evidence, review points, and human decisions. It does not replace an accountable role.

## When to use

Use the skill for:

- incident readiness, escalation design, or initial assessment without live crisis leadership,
- preparation of reviews or workshops,
- converting unclear requirements into concrete routines,
- making evidence gaps and decisions visible,
- building a prioritized improvement backlog.

## When not to use

Do not use for:

- legal advice or binding interpretation,
- data protection advice,
- certification, compliance, or security assurances,
- automated management decisions,
- external communication without approval,
- live crisis leadership or operational emergency steering,
- transferring confidential content or licensed standard texts into public artifacts.

## Input data

Required:

- **Scope:** process, service, governance area, or review context under consideration.
- **Existing artifacts:** existing registers, templates, playbooks, measures, evidence, or role information.
- **Risks or findings:** known gaps, uncertainties, dependencies, or management questions.

Optional:

- existing evidence sources,
- compliance register entries as metadata,
- lessons learned,
- management priorities,
- resource or timeline constraints.

Assumptions:

- Missing information is marked as open review points.
- Maturity levels and priorities are working assumptions, not external assurance.

## Prerequisites

Helpful resources include:

- `07-ai-governance-agents/agents/public/incident-readiness-coach.md`,
- `07-ai-governance-agents/agents/public/control-evidence-architect.md`,
- `07-ai-governance-agents/agents/public/risk-and-obligation-prioritizer.md`,
- `07-ai-governance-agents/agents/public/management-review-facilitator.md`,
- `07-ai-governance-agents/agents/public/agent-quality-and-safety-reviewer.md`,
- `08-templates-playbooks/templates/incident-escalation-card.md`, once available,
- `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md`.

## Workflow

1. **Clarify scope**  
   Describe the objective, non-scope, affected roles, and expected decision.

2. **Capture the current situation**  
   Collect existing artifacts, routines, evidence sources, risks, and findings as references.

3. **Derive operating logic**  
   Define owner, trigger, workflow, output, evidence, review cadence, and escalation point.

4. **Make gaps visible**  
   Mark missing owners, missing evidence, unclear decisions, unreviewed assumptions, and dependencies.

5. **Develop actions and options**  
   Create a small backlog with impact, effort, dependency, evidence output, and human decision point.

6. **Prioritize**  
   Prioritize by risk, urgency, decision relevance, evidence need, and feasibility.

7. **Prepare review or brief**  
   Condense results into a review artifact with open decisions, options, risks of inaction, and next step.

8. **Perform verification**  
   Check public safety, claim safety, operating logic, workload, human review, and handoffs.

## Output artifacts

Depending on the assignment, the skill creates:

- Incident Escalation Card,
- Decision Brief,
- prioritized action backlog,
- Evidence Needs List,
- review note,
- handoff list to agents, skills, or human roles.

## Human-in-the-loop

Human review is required for:

- legal or normative interpretation,
- data protection assessment,
- risk acceptance,
- resource, budget, or prioritization decisions,
- final role and owner assignment,
- external communication,
- approval of reviews, briefings, or measures.

## Verification

Check before completion:

```text
Verification:
- Public-Safety: pass / notes / stop
- Claim-Safety: pass / notes / stop
- Operating logic: pass / notes / stop
- Workload: pass / notes / stop
- Evidence reference: pass / notes / stop
- Human Review: pass / notes / stop
- Handoffs: pass / notes / stop
- Result: pass / pass with notes / stop
```

Minimum questions:

- Are scope and non-scope clear?
- Does every result have an owner, trigger, output, and evidence reference?
- Are decisions and escalations marked as human?
- Has unnecessary documentation load been removed?
- Are boundaries and red lines visible?

## Quality gates

Apply from `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md`:

- U1 Public-Safe Gate,
- U2 Claim-Safety Gate,
- U3 Operating Logic Gate,
- U4 Empowerment Gate,
- U5 Workload Gate,
- U6 Portability Gate,
- A2 Skill Gate.

## Handoffs

Typical handoffs:

- to `incident-readiness-coach` when subject-matter design needs to be deepened,
- to `control-evidence-architect` when evidence flows need to be specified,
- to `risk-and-obligation-prioritizer` when prioritization is unclear,
- to `management-review-facilitator` when decisions need to be prepared,
- to `agent-quality-and-safety-reviewer` when claim safety, workload, or public safety are critical.

## Boundaries and red lines

This skill does not provide legal advice, data protection advice, certification assurance, compliance assurance, or a management decision.

It must not transfer confidential content, real customer data, or licensed standard texts into public artifacts.

It must not create false assurance: missing evidence, unclear owners, open decisions, and assumptions are marked visibly.

## Example

Current situation:

A fictional organization wants to address a single governance topic in a structured way. There are initial notes, but no clear routine, no secured evidence, and no prioritized decision template.

Good skill output:

- Scope and non-scope are named.
- A proposed owner and review role are visible.
- The routine has trigger, workflow, output, and evidence.
- Open decisions are marked in the Decision Brief.
- The next action is small enough for the next review cycle.

Poor skill output:

- “The topic is completed as soon as a policy has been written.”

Why poor:

- No operating logic, no owner, no evidence reference, no review cadence, and no human decision.

## Definition of Done

The skill is complete when:

- scope and boundaries are documented,
- current situation and evidence sources are captured,
- roles, routines, and escalations are described,
- gaps and assumptions are visible,
- actions are prioritized,
- human decisions are clearly marked,
- verification is documented.
