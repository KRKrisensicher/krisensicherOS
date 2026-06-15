---
name: minimum-viable-isms
version: 1.0.0
description: "Design a Minimum Viable ISMS as scope, risk, control, evidence, and review routines."
category: isms
inputs:
  - scope
  - risks
  - existing-controls
  - governance-roles
  - evidence-sources
outputs:
  - isms-scope-canvas
  - risk-control-routine-map
  - evidence-and-review-plan
  - minimum-viable-isms-backlog
requires_human_review: true
---


# minimum-viable-isms

## Purpose

This skill helps user organizations design a Minimum Viable ISMS as a workable operating routine: clear scope, understandable risk logic, a small number of effective controls, traceable evidence, review cadence, and management decisions.

The goal is not a perfect manual, but a viable starting point that enables responsibility, learning, and improvement.

## When to use

Use the skill for:

- building an initial ISMS operating mode,
- transferring scattered security activities into recurring routines,
- preparing an ISMS scope,
- clarifying risk, control, and evidence flows,
- reducing overloaded documentation initiatives to a usable start,
- preparing a management review for ISMS setup.

## When not to use

Do not use for:

- certification assurances or external confirmations,
- binding interpretation of standards or laws,
- data protection advice,
- replacing management decisions,
- building a complete ISMS without accountable owners,
- incorporating licensed standard texts into public artifacts,
- live crisis steering or incident decisions.

## Input data

Required:

- **Scope candidates:** organizational units, services, processes, locations, or systems to be considered.
- **Risk topics:** known threats, vulnerabilities, findings, management concerns, or operational dependencies.
- **Governance roles:** human owners, review roles, and decision-making bodies, where available.

Optional:

- existing policies,
- existing controls,
- risk or action registers,
- evidence packs,
- supplier or incident routines,
- internal requirements or compliance register entries as metadata.

Assumptions:

- If scope, risk acceptance, or owners are missing, the skill marks decision questions instead of creating fictional certainty.
- Maturity descriptions are working assumptions, not external assurance.

## Prerequisites

Helpful are:

- `08-templates-playbooks/templates/isms-scope-canvas.md`, once available,
- `08-templates-playbooks/templates/evidence-pack-index.md`, once available,
- `07-ai-governance-agents/skills/governance-operating-model/SKILL.md`,
- `07-ai-governance-agents/skills/nis2-gap-assessment/SKILL.md`,
- `07-ai-governance-agents/agents/public/isms-operating-model-designer.md`,
- `07-ai-governance-agents/agents/public/security-governance-architect.md`,
- `07-ai-governance-agents/agents/public/risk-and-obligation-prioritizer.md`,
- `07-ai-governance-agents/agents/public/control-evidence-architect.md`,
- `07-ai-governance-agents/agents/public/management-review-facilitator.md`,
- `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md`.

## Process

1. **Clarify ISMS purpose**  
   Describe which decision readiness the ISMS should create first: understanding risks, steering actions, bundling evidence, clarifying responsibilities, or enabling management reviews.

2. **Define scope minimally and with rationale**  
   Define the starting scope as small as reasonable and as large as necessary. Explicitly mark what is not in scope and when expansion will be reviewed.

3. **Derive critical assets and processes**  
   Capture the most important services, information, dependencies, and operating processes in scope. Use only fictional examples or user-internal private data outside public repo artifacts.

4. **Build risk logic**  
   Formulate a small number of traceable risk topics with cause, possible impact, affected role, current treatment, and open decision.

5. **Describe controls as operating routines**  
   Describe controls with owner, trigger, process, output, evidence, review frequency, and escalation point.

6. **Create evidence plan**  
   Define which evidence is produced by which routines, how current it must be, where it is stored, and who reviews it.

7. **Define review cadence**  
   Define minimal routines: risk review, action review, evidence pack review, and management review. Remove routines without decision or evidence value.

8. **Prioritize backlog**  
   Create a Minimum Viable ISMS backlog with actions, proposed owner, effort, impact, dependencies, evidence output, and next review point.

9. **Prepare management decision**  
   Create a decision brief with scope options, top risks, resource needs, accepted assumptions, open decisions, and proposed start cycle.

10. **Run verification**  
   Check operating logic, workload, human review, evidence linkage, claim safety, and portability.

## Output artifacts

Depending on the assignment, the skill creates:

- ISMS Scope Canvas,
- Minimum Viable ISMS Operating Model,
- Risk-Control-Routine Map,
- Evidence and Review Plan,
- Management Decision Brief,
- action and improvement backlog,
- handoff list to agents, skills, or human roles.

## Human-in-the-loop

Human review is required for:

- final scope decision,
- risk acceptance,
- control selection and prioritization,
- role and resource decisions,
- legal or normative interpretation,
- data protection assessment,
- approval of management reviews,
- external communication or audit/customer statements.

## Verification

Check before completion:

```text
Verification:
- Public-Safety: pass / notes / stop
- Claim-Safety: pass / notes / stop
- Operating logic: pass / notes / stop
- Workload: pass / notes / stop
- Scope clarity: pass / notes / stop
- Risk-control linkage: pass / notes / stop
- Evidence and review plan: pass / notes / stop
- Human Review: pass / notes / stop
- Handoffs: pass / notes / stop
- Result: pass / pass with notes / stop
```

Minimum questions:

- Is the scope clear, justified, and limited?
- Does every central risk have at least one treatment idea or open decision?
- Are controls described as routines with owner, trigger, output, and evidence?
- Is there a review cadence that prepares decisions?
- Has unnecessary documentation been removed?
- Are certification, legal, and security promises excluded?

## Quality gates

Apply from `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md`:

- U1 Public-Safe Gate,
- U2 Claim-Safety Gate,
- U3 Operating Logic Gate,
- U4 Empowerment Gate,
- U5 Workload Gate,
- U6 Portability Gate,
- A2 Skill Gate,
- for templates additionally A3 Template Gate,
- for examples additionally A6 Example Gate.

## Handoffs

Typical handoffs:

- to `security-governance-architect` when roles, committees, or routines are missing,
- to `risk-and-obligation-prioritizer` when risks and actions need to be prioritized,
- to `control-evidence-architect` when control and evidence chains need to be specified,
- to `evidence-pack-reviewer` when existing evidence packs are reviewed,
- to `management-review-facilitator` when management decisions are prepared,
- to `policy-and-controls-drafter` when policy or control drafts should be created from approved operating logic,
- to `agent-quality-and-safety-reviewer` when workload, claim safety, or public safety are critical.

## Boundaries and red lines

This skill does not provide legal advice, does not provide data protection advice, does not provide certification or compliance assurance, and does not make management decisions.

It must not include confidential content, real customer data, or licensed standard texts in public artifacts.

It must not treat an ISMS as a mere document collection. If an artifact has no owner, trigger, output, evidence, or decision linkage, it is shortened, redesigned, or marked as not prioritized.

## Example

Initial situation:

A fictional organization starts with a digital core service. There are individual security measures, but no clear ISMS scope, no review cadence, and no standardized evidence repository.

Good skill output:

- **Scope:** digital core service including operations team and two supporting IT processes; sales systems initially outside the starting scope.  
- **Risk:** unclear recovery capability in the event of an operating platform outage.  
- **Control routine:** quarterly review of backup and restore evidence with service owner and IT operations.  
- **Evidence:** restore test note, action log, management decision when resources are needed.  
- **Review:** monthly action review, quarterly management review for top risks.

Poor skill output:

- “Create a complete ISMS manual with all policies and have it reviewed annually.”

Why poor:

- Too document-heavy, no starting scope, no risk and control logic, no evidence routine, no owners, and no management decision.

## Definition of Done

The skill is complete when:

- ISMS purpose and starting scope are documented,
- out-of-scope items and expansion criteria are visible,
- central risks are described,
- controls are formulated as routines,
- evidence and review plan is available,
- action backlog is prioritized,
- management decisions and human review points are named,
- handoffs are clear,
- verification is documented.
