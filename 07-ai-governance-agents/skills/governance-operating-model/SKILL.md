---
name: governance-operating-model
version: 1.0.0
description: "Turn requirements into roles, routines, decisions, escalations, and evidence flows."
category: governance
inputs:
  - scope
  - requirements
  - existing-roles
  - existing-routines
  - evidence-sources
outputs:
  - governance-operating-model-canvas
  - role-routine-map
  - evidence-flow-map
  - management-decision-log
requires_human_review: true
---


# governance-operating-model

## Purpose

This skill helps user organizations structure requirements not as a stack of documents, but as an operable governance operating model.

It answers:

- Which roles are needed?
- Which routines operate the requirements?
- Which decisions need to be prepared?
- What evidence is created in operation?
- Where is escalation or management review needed?

## When to use

Use the skill for:

- building a security governance operating model,
- NIS2/ISMS/BCMS readiness work,
- translating requirements into responsibilities,
- unclear roles, committees, reviews, or evidence flows,
- preparing a management review.

## When not to use

Do not use for:

- no legal advice or binding interpretation,
- no data protection advice,
- no certification or compliance statements,
- no live crisis leadership,
- no pure policy creation without an operating model,
- no replacement of management decisions.

## Input data

Required:

- **Scope:** affected organizational unit, services, processes, or governance domain.
- **Requirements:** public sources, register entries, risks, audit findings, or management requirements.
- **Existing roles:** information security officer/CISO, data protection, IT, business unit, management, crisis team, internal audit, or similar roles.

Optional:

- existing routines,
- known evidence sources,
- management review dates,
- risk or action registers,
- existing templates.

Assumptions:

- If information is missing, the skill does not guess. It marks owner questions and open review points.

## Prerequisites

Helpful are:

- `07-ai-governance-agents/agents/public/security-governance-architect.md`,
- `07-ai-governance-agents/agents/public/risk-and-obligation-prioritizer.md`,
- `07-ai-governance-agents/agents/public/control-evidence-architect.md`,
- `templates/governance-operating-model-canvas.md`, once available,
- `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md`,
- relevant entries from `01-orientation/knowledge-sources/` and `02-governance-operating-model/compliance-register/`.

## Process

1. **Narrow the scope**  
   Describe the area for which the operating model should apply. Mark what is out of scope.

2. **Cluster requirements**  
   Group requirements by topics, e.g., risk, incident, suppliers, management review, evidence, BCMS, ISMS.

3. **Identify roles**  
   Assign at least one responsible human role and supporting roles to each requirement.

4. **Derive routines**  
   Translate requirements into recurring or event-based routines with trigger, frequency, input, process, and output.

5. **Determine decision points**  
   Mark which questions require management, risk acceptance, budget, prioritization, or escalation decisions.

6. **Model evidence flows**  
   Determine which evidence is created from which routine and who reviews it.

7. **Define handoffs and escalations**  
   Define when other agents, skills, or human roles must take over.

8. **Check workload**  
   Remove routines that do not create risk reduction, evidence quality, or decision readiness.

9. **Prepare review**  
   Create a concise management or owner review note with open decisions.

## Output artifacts

Depending on the assignment, the skill creates:

- Governance Operating Model Canvas,
- role/routine matrix,
- RACI draft,
- Evidence Flow Map,
- escalation and handoff map,
- Management Decision Log,
- action and routine backlog.

## Human-in-the-loop

Human review is required for:

- legal or regulatory interpretation,
- data protection questions,
- final assignment of roles and responsibilities,
- risk acceptance,
- budget or resource decisions,
- approval of management reviews,
- external communication or publication.

## Verification

Check before completion:

```text
Verification:
- Public-Safety: pass / notes / stop
- Claim-Safety: pass / notes / stop
- Operating logic: pass / notes / stop
- Workload: pass / notes / stop
- Human Review: pass / notes / stop
- Handoffs: pass / notes / stop
- Result: pass / pass with notes / stop
```

Minimum questions:

- Does every routine have a trigger?
- Does every routine have an owner?
- Is there an output and an evidence source?
- Are decisions and escalations visible?
- Has unnecessary meeting or documentation effort been removed?

## Quality gates

To be applied from `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md`:

- U1 Public-Safe Gate,
- U2 Claim-Safety Gate,
- U3 Operating Logic Gate,
- U4 Empowerment Gate,
- U5 Workload Gate,
- U6 Portability Gate,
- A2 Skill Gate,
- for templates additionally A3 Template Gate,
- for workflows additionally A5 Workflow Gate.

## Handoffs

Typical handoffs:

- to `regulatory-source-mapper` if sources or references are unclear,
- to `compliance-register-curator` if register entries are missing,
- to `risk-and-obligation-prioritizer` if prioritization is needed,
- to `control-evidence-architect` if evidence flows need to be detailed,
- to `management-review-facilitator` if decisions need to be prepared,
- to `agent-quality-and-safety-reviewer` if claims, workload, or boundaries are critical.

## Boundaries and red lines

This skill does not provide legal advice, does not provide data protection advice, does not provide certification or compliance guarantees, and does not make management decisions.

It must not transfer confidential content, real customer data, or licensed standard texts into public artifacts.

## Example

Initial situation:

A fictional organization wants to translate requirements from NIS2 readiness, ISMS setup, and incident readiness into an initial operating mode.

Good skill output:

- Monthly risk and action routine with the information security officer as owner, management review escalation when resources are needed, and action log as evidence.
- Quarterly evidence pack review routine with control owners and gap list.
- Event-based incident escalation routine with roles, triggers, communication points, and after-action review.
- Open human review: applicability of requirements, risk acceptance, management prioritization.

Poor skill output:

- “Create an information security policy and review it regularly.”

Why poor:

- No roles, no trigger, no decision, no evidence, no review, and no operating logic.

## Definition of Done

The skill is complete when:

- scope and boundaries are named,
- requirements are clustered,
- roles and routines are derived,
- decision points are visible,
- evidence flows are described,
- handoffs and human review points are clear,
- workload has been checked,
- verification is documented.
