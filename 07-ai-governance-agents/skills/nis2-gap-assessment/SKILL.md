---
name: nis2-gap-assessment
version: 1.0.0
description: "Structure NIS2 readiness across gaps, evidence, actions, prioritization, and management decisions."
category: nis2
inputs:
  - scope
  - source-references
  - compliance-register-entries
  - existing-governance-artifacts
  - evidence-inventory
outputs:
  - nis2-gap-worksheet
  - prioritized-gap-backlog
  - evidence-needs-list
  - management-decision-brief
requires_human_review: true
---

<!-- kso:product-relevance
repo-scope: product
classification: agent-skill
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->


# nis2-gap-assessment

## Purpose

This skill helps user organizations structure NIS2 readiness as operable gap work: requirements are mapped to scope, existing routines, evidence, open gaps, measures, and management decisions.

The skill does not produce a legal assessment and does not confirm NIS2 compliance. It makes visible where human review, prioritization, resource decisions, or subject-matter deepening are needed.

## When to use

Use the skill for:

- initial NIS2 readiness screening,
- preparing an internal security governance backlog,
- mapping public reference sources to existing roles, routines, and evidence,
- preparing a management review on NIS2-relevant action areas,
- structuring findings from workshops, audits, or self-assessments.

## When not to use

Do not use for:

- binding legal interpretation of the NIS2 Directive or national implementation laws,
- determining whether an organization legally falls within the scope,
- data protection advice,
- confirmation of regulatory fulfillment,
- certification, security, or liability statements,
- live incident or crisis decisions,
- processing confidential contractual content or licensed standard texts in public artifacts.

## Input data

Required:

- **Scope:** organization unit, services, sites, systems, or processes under consideration.
- **Source references:** public reference anchors from `01-orientation/knowledge-sources/` or own register entries without reproducing full licensed content.
- **Existing artifacts:** role model, policy drafts, risk/measure registers, incident routines, supplier process, or evidence packs, where available.

Optional:

- existing gap lists,
- audit or workshop findings,
- risk assessments,
- management requirements,
- organization-specific prioritization logic,
- evidence sources and tool exports as redacted metadata.

Assumptions:

- Missing information is marked as open review points.
- The skill assesses maturity only as a working assumption, not as an external assurance.

## Prerequisites

Helpful inputs are:

- `01-orientation/knowledge-sources/hardwired-sources.yaml`,
- `02-governance-operating-model/02-governance-operating-model/compliance-register/sources.example.yaml` or an own register,
- `templates/nis2-gap-worksheet.md`, once available,
- `templates/evidence-pack-index.md`, once available,
- `07-ai-governance-agents/agents/public/regulatory-source-mapper.md`,
- `07-ai-governance-agents/agents/public/risk-and-obligation-prioritizer.md`,
- `07-ai-governance-agents/agents/public/control-evidence-architect.md`,
- `07-ai-governance-agents/agents/public/management-review-facilitator.md`,
- `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md`.

## Workflow

1. **Define scope and non-scope**  
   Describe the area under consideration and explicitly mark which parts are not assessed. If the scope of application is legally unclear, stop the statement and formulate a question for qualified review.

2. **Collect sources as reference anchors**  
   Capture public legal/regulatory sources and internal register entries as metadata: source, topic, location/reference, owner, status, review need. Do not reproduce standard texts or confidential content.

3. **Cluster requirements into work areas**  
   Assign the references to operational fields, e.g., governance, risk, incident, business continuity, suppliers, training, policies, controls, evidence, management review.

4. **Map existing routines and evidence**  
   For each work area, ask: Which role operates the topic? Which trigger starts work? Which routine exists? Which evidence is produced? Who reviews it?

5. **Formulate gaps**  
   Describe gaps as verifiable work statements: missing owner, unclear trigger, missing routine, missing evidence, unreviewed effectiveness, open management decision.

6. **Determine evidence needs**  
   Define which evidence is needed, where it is produced, how current it must be, and what quality it has for decisions.

7. **Derive measures**  
   Translate gaps into concrete measures with suggested owner, expected evidence, dependencies, effort estimate, and review point.

8. **Prioritize**  
   Prioritize by impact, urgency, risk, evidence gap, implementation effort, dependencies, and management relevance. Unclear criteria are marked as decision questions.

9. **Prepare management decisions**  
   Create a short decision brief: top gaps, options, resource needs, risks of inaction, open legal/subject-matter reviews, and proposed next routine.

10. **Perform verification**  
   Check claim safety, public safety, operating logic, evidence linkage, handoffs, and workload. Stop in case of impermissible claims or real/confidential data.

## Output artifacts

Depending on the assignment, the skill produces:

- NIS2 gap worksheet,
- prioritized gap and measures backlog,
- evidence needs list,
- source/register mapping,
- roles/routines gap list,
- management decision brief,
- handoff list to agents, skills, or human roles.

## Human-in-the-loop

Human review is required for:

- legal applicability and interpretation,
- data protection assessment,
- final risk acceptance,
- measure prioritization when resources or budget are affected,
- owner and role decisions,
- approval of management briefs,
- external communication to authorities, customers, auditors, or the public.

## Verification

Check before completion:

```text
Verification:
- Public Safety: pass / notes / stop
- Claim Safety: pass / notes / stop
- NIS2 subject-matter boundaries: pass / notes / stop
- Operating logic: pass / notes / stop
- Evidence linkage: pass / notes / stop
- Prioritization: pass / notes / stop
- Human Review: pass / notes / stop
- Handoffs: pass / notes / stop
- Result: pass / pass with notes / stop
```

Minimum questions:

- Is the scope clear and limited?
- Are sources used only as reference anchors or own summaries?
- Does each gap have an operational link to a role, routine, evidence, or decision?
- Is there a traceable prioritization?
- Are legal and management decisions marked as human review points?
- Does the output contain no compliance, certification, or security guarantee?

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
- for source/register work additionally A8 Source/Register Gate.

## Handoffs

Typical handoffs:

- to `regulatory-source-mapper` if sources, locations, or reference anchors are unclear,
- to `compliance-register-curator` if register entries are missing or outdated,
- to `security-governance-architect` if roles and routines are missing,
- to `risk-and-obligation-prioritizer` if gaps need to be prioritized,
- to `control-evidence-architect` if evidence packs or evidence chains need to be built,
- to `management-review-facilitator` if decisions need to be prepared,
- to `agent-quality-and-safety-reviewer` if claim safety, workload, or public safety are critical.

## Boundaries and red lines

This skill does not provide legal advice, data protection advice, certification or compliance guarantees, or management decisions.

It must not include confidential content, real customer data, or licensed standard texts in public artifacts.

It must not smooth over uncertainty: open applicability, unclear source situation, missing evidence, or conflicting priorities are visibly marked.

## Example

Initial situation:

A fictional organization wants to check which NIS2 readiness work is useful next for a critical digital service. Available inputs include a rough role model, an incident process draft, and an incomplete measures register.

Good skill output:

- **Gap:** Incident routine has a trigger and escalation path, but no after-action review and no evidence repository.  
  **Measure:** Add after-action review step and evidence pack index.  
  **Suggested owner:** Incident owner with information security officer review.  
  **Evidence:** Review minutes, measures list, decision log.  
  **Priority:** high, because the routine already exists and the evidence gap makes management decisions harder.  
  **Human Review:** Management decides resources and target date.

Poor skill output:

- “A documented incident process is sufficient; no further review is needed.”

Why poor:

- Replaces subject-matter review with false assurance, contains no operating logic, no evidence quality, no human decision, and no robust boundary.

## Definition of Done

The skill is complete when:

- scope and non-scope are documented,
- sources are captured as permissible reference anchors,
- work areas are clustered,
- existing roles, routines, and evidence are mapped,
- gaps are formulated in a verifiable way,
- evidence needs and measures are described,
- prioritization is traceable,
- management decisions and human review points are visible,
- handoffs are named,
- verification is documented.
