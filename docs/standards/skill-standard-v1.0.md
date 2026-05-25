<!-- kso:product-relevance
repo-scope: product
classification: product-standard
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; product-safety; release-readiness
-->

# Skill Standard v1.0

As of: 2026-05-23

This standard applies to all krisensicherOS skills under `skills/<skill-name>/SKILL.md`.

## Purpose

Skills are repeatable workflows. They are not knowledge repositories, not mere prompt collections, and not substitute accountable parties.

A skill should enable user organizations to perform a specific governance task repeatedly: with inputs, process, outputs, evidence, boundaries, and verification.

## Path and naming rule

Each skill is located in its own folder:

```text
skills/<skill-name>/SKILL.md
```

The skill name is:

- lowercase,
- kebab-case,
- professionally specific,
- not tool- or provider-specific.

## Required structure for `SKILL.md`

Each skill contains these sections:

1. YAML frontmatter
2. Purpose
3. When to use
4. When not to use
5. Input data
6. Prerequisites
7. Process
8. Output artifacts
9. Human-in-the-loop
10. Verification
11. Quality gates
12. Handoffs
13. Boundaries and red lines
14. Example
15. Definition of Done

## Frontmatter

```yaml
---
name: skill-name
version: 1.0.0
description: Brief description of the repeatable workflow.
category: governance|nis2|isms|bcms|evidence|incident|management|quality
inputs:
  - input-name
outputs:
  - output-name
requires_human_review: true
---
```

## Section requirements

### Purpose

Describes the specific work task and its benefit.

Not sufficient: “Helps with compliance.”  
Good: “Translates requirements into roles, routines, decisions, and evidence flows.”

### When to use

Specific triggers for which the skill is useful.

### When not to use

Boundaries, red lines, and cases where other skills or human review are needed.

### Input data

List of required inputs. Each input should state whether it is mandatory, optional, or an assumption.

### Prerequisites

Required artifacts, registers, roles, or decisions.

### Process

Sequence of steps with operational logic. Each step should make clear:

- what is reviewed,
- which artifact is used,
- which output is created,
- when to stop or escalate.

### Output artifacts

Specific target artifacts, e.g.:

- canvas,
- worksheet,
- review note,
- register entry,
- evidence pack,
- management decision brief,
- measures backlog.

### Human-in-the-loop

Explicitly name:

- who must review,
- who must decide,
- when approval is required,
- which questions the skill must not answer.

### Verification

At minimum:

- completeness check,
- claim-safety check,
- public-safety check,
- operating logic check,
- handoff check.

### Quality gates

Reference to `evals/quality-gates.md` and relevant artifact-specific gates.

### Handoffs

Which agents, skills, or human roles take over afterward?

### Boundaries and red lines

Always include:

- does not provide legal advice,
- does not provide data protection advice,
- no certification or compliance guarantee,
- no management decision,
- do not reproduce confidential or licensed content,
- no real customer data in public examples.

### Example

A small fictional example with safe, limited output.

### Definition of Done

Specific criteria for when the skill is cleanly completed.

## Skill vs. Agent vs. Template vs. Workflow

- **Agent**: role, voice, mandate, responsibility, boundaries.
- **Skill**: repeatable workflow.
- **Template**: fillable artifact.
- **Workflow**: orchestrates agents, skills, templates, registers, and approvals.

A skill may use agents or templates, but does not replace them.

## Verification block template

```text
Verification:
- Public-Safety: pass / notes / stop
- Claim-Safety: pass / notes / stop
- Operating logic: pass / notes / stop
- Human Review: pass / notes / stop
- Handoffs: pass / notes / stop
- Result: pass / pass with notes / stop
```

## Minimal example skeleton

```markdown
---
name: example-skill
version: 1.0.0
description: Repeatable workflow for ...
category: governance
inputs:
  - scope
  - existing-evidence
outputs:
  - decision-brief
requires_human_review: true
---

# example-skill

## Purpose

...

## When to use

...

## When not to use

...

## Input data

...

## Prerequisites

...

## Process

1. ...

## Output artifacts

...

## Human-in-the-loop

...

## Verification

...

## Quality gates

...

## Handoffs

...

## Boundaries and red lines

...

## Example

...

## Definition of Done

...
```

## Review gate for new skills

A new skill may only be considered complete when:

- `SKILL.md` exists,
- the required structure is complete,
- inputs/outputs are specific,
- verification is executable,
- relevant quality gates are referenced,
- human approvals are visible,
- the example is public-safe,
- no false assurance is created.
