---
name: audit-questionnaire-builder
version: 1.0.0
description: "Build audit questionnaires from requirements, sources, mappings, prompts, and evidence targets."
category: evidence
inputs:
  - scope
  - requirements-or-raw-material
  - existing-artifacts
  - evidence-or-source-references
outputs:
  - audit-questionnaire
  - review-notes
  - decision-or-action-backlog
requires_human_review: true
---

<!-- kso:product-relevance
repo-scope: product
classification: agent-skill
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->


# audit-questionnaire-builder

## Purpose

This skill helps user organizations derive internal audit questionnaires from requirements and structure them so that auditors can work with guiding questions, criteria, evidence targets, and human gates.

It works with sources, requirements, standards, controls, documents, or raw material only as references, metadata, own summaries, or private user content. It does not provide legal advice, does not provide data protection advice, and does not provide compliance, audit, or certification assurance.

## When to use

Use the skill when preparing internal audits, self-assessments, supplier reviews, or management system reviews.

Typical triggers:

- new or changed requirements,
- internal audits or self-assessments,
- document reviews,
- evidence pack reviews,
- management review preparation,
- handoffs from risk, control, or compliance register work.

## When not to use

Do not use for:

- binding interpretation of law or contracts,
- data protection assessment,
- external audit or certification assurance,
- management decision,
- live incident or crisis steering,
- reproduction of licensed standard texts,
- public processing of confidential documents, interviews, or personal data.

## Input data

Required:

- **Scope:** Audit, document, process, control, or review area.
- **Requirements or raw material:** Register entries, source references, controls, interview notes, document excerpts, or findings.
- **Target output:** Questionnaire, audit program, finding, gap matrix, or document draft.

Optional:

- existing documents or templates,
- standard/control references as metadata,
- evidence pack or evidence register,
- roles and owners,
- rating scale or audit methodology,
- target group and tone.

Assumptions:

- Unclear statements are marked as assumptions or open review points.
- Missing sources or evidence are not invented.

## Prerequisites

Helpful resources include:

- `agents/public/internal-audit-planner.md`, once available,
- `agents/public/control-evidence-architect.md`,
- `agents/public/evidence-pack-reviewer.md`,
- `agents/public/management-review-facilitator.md`,
- `agents/public/agent-quality-and-safety-reviewer.md`,
- `templates/audit-questionnaire.md`,
- `templates/evidence-pack-index.md`,
- `templates/decision-log.md`,
- `evals/quality-gates.md`.

## Workflow

1. **Clarify scope and objective**  
   Define which audit, document, or governance area is being considered and what output should be created.

2. **Collect criteria and requirements**  
   Record sources, register entries, standard/control references, internal requirements, or interview statements only as permitted references, metadata, or own summaries.

3. **Create mapping**  
   Map requirements to suitable controls, document sections, questions, evidence types, audit methods, or measures. Mark unclear mappings.

4. **Create working artifact**  
   Create the concrete draft with criterion, status/question, method, evidence target, rating note, owner, risk, or follow-up.

5. **Mark gaps and assumptions**  
   Separate confirmed evidence, assumptions, open questions, deviations, observations, and improvement potential.

6. **Prepare review and decision**  
   Mark who must review, approve, or decide. Prepare measures, decision log, or management review handoff.

7. **Perform verification**  
   Check public safety, claim safety, source/evidence linkage, workload, human review, and handoffs.

## Output artifacts

Depending on the assignment, the skill creates:

- audit-questionnaire,
- mapping between requirement, control, question, method, evidence, and owner,
- open audit questions,
- gap or finding list,
- measures or review backlog,
- management or owner handoff.

## Human-in-the-loop

Human review is required for:

- interpretation of laws, standards, or contracts,
- data protection assessment,
- final audit assessment,
- deviation classification with organizational impact,
- measure approval,
- risk acceptance,
- document approval,
- external communication.

## Verification

```text
Verification:
- Public Safety: pass / notes / stop
- Claim Safety: pass / notes / stop
- Source/criteria linkage: pass / notes / stop
- Evidence linkage: pass / notes / stop
- Operating logic: pass / notes / stop
- Workload: pass / notes / stop
- Human Review: pass / notes / stop
- Handoffs: pass / notes / stop
- Result: pass / pass with notes / stop
```

Minimum questions:

- Are scope, criteria, and target output clear?
- Are requirements referenced or summarized only in permitted ways?
- Are questions, methods, findings, or document sections mapped traceably?
- Are evidence needs and rating notes verifiable?
- Are assumptions, gaps, and human gates visible?
- Have no guarantees or final decisions been asserted?

## Quality gates

Apply from `evals/quality-gates.md`:

- U1 Public-Safe Gate,
- U2 Claim-Safety Gate,
- U3 Operating Logic Gate,
- U4 Empowerment Gate,
- U5 Workload Gate,
- U6 Portability Gate,
- A2 Skill Gate,
- A3 Template Gate, if templates are created or used,
- A8 Source/Register Gate, if sources or standard/register entries are affected.

## Handoffs

Typical handoffs:

- to `internal-audit-planner` if subject-matter deepening is needed,
- to `control-evidence-architect` if evidence or control mapping is missing,
- to `evidence-pack-reviewer` if evidence must be reviewed,
- to `management-review-facilitator` if decisions must be prepared,
- to `agent-quality-and-safety-reviewer` if claims, confidentiality, or workload are critical.

## Limits and red lines

This skill does not provide legal advice, data protection advice, certification, audit, or compliance assurance, and does not make management decisions.

It must not transfer confidential content, personal data, real customer data, or licensed standard texts into public artifacts.

It must not invent evidence, smooth over gaps, or formulate final assessments without human review.

## Example

Initial situation:

A fictional organization wants to derive internal audit questions, document gaps, or findings from existing register entries and evidence pack notes. Some requirements are unclear, and several pieces of evidence are missing.

Good skill output:

- Requirements are captured as references.
- Guiding question, method, evidence target, and owner are visible.
- Assumptions and missing evidence are marked.
- Findings are factual and traceable.
- Management or owner decisions are marked as a human gate.

Poor skill output:

- “The audit is complete; no further evidence or human assessment is needed.”

Why poor:

- This creates false assurance, replaces human assessment, and contains an impermissible assurance.

## Definition of Done

The skill is complete when:

- scope, criteria, and target output are documented,
- requirements and mappings are traceable,
- questions, methods, findings, or document structure are verifiable,
- evidence needs and gaps are visible,
- human review and approval points are marked,
- handoffs and next steps are clear,
- verification is documented.
