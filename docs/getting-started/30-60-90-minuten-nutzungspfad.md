<!-- kso:product-relevance
repo-scope: product
classification: getting-started-guidance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Use krisensicherOS in 30 / 60 / 90 Minutes

Status: 2026-05-23

## Purpose

This user path connects the existing agents, skills, templates, and workflows into a simple entry point. It is not a new specialist module, but user guidance for the first robust walkthrough.

## Before You Start

Define:

- which area is being considered,
- whether only fictional/public or internal data will be used,
- who will perform the subject-matter review,
- which AI environment is allowed,
- whether `templates/ki-nutzungsfreigabe-matrix.md` is complete enough,
- where results will be stored.

Stop for legal interpretation, data protection assessment, risk acceptance, management decision, external sending, confidential content without approval, or licensed standard texts.

## 30 Minutes: Orientation and Scope

Goal: Understand the working frame and define the first scope.

1. Read `README.md`.
2. Formulate the management question: Which decision must be prepared in the next 30 days?
2. Select `docs/setup/ki-setups-bedienungsanleitung.md`: ChatGPT, M365 Copilot, Claude Code, or local AI.
3. Read `agents/public/role-model.md` and choose a suitable role:
   - `compliance-operating-system-lead` for orchestration,
   - `nis2-readiness-analyst` for the NIS2 start,
   - `isms-operating-model-designer` for ISMS,
   - `internal-audit-planner` for audit,
   - `evidence-pack-reviewer` for evidence.
4. Open the first template:
   - `templates/compliance-source-register.md`,
   - `templates/governance-operating-model-canvas.md`,
   - `templates/nis2-gap-worksheet.md`.

Output after 30 minutes:

- management question for the next 30 days,
- scope sentence,
- selected agent role,
- first source / requirement / register row,
- open human gate questions.

## 60 Minutes: First NIS2 / ISMS / Audit Walkthrough

Goal: Turn one requirement into an operable governance routine.

1. Capture the source or requirement as a reference, not by copying standard text.
2. Use `governance-operating-model` to derive:
   - role,
   - trigger,
   - routine,
   - decision point,
   - evidence.
3. Use `nis2-gap-assessment` or `minimum-viable-isms` to document the gap.
4. If audit is needed:
   - `audit-questionnaire-builder`,
   - `audit-test-procedure-mapper`,
   - `evidence-request-list-builder`.
5. Fill suitable templates:
   - `templates/nis2-gap-worksheet.md`,
   - `templates/audit-questionnaire.md`,
   - `templates/audit-test-program.md`,
   - `templates/evidence-request-list.md`.

Output after 60 minutes:

- gap or audit row,
- required evidence,
- owner questions,
- first review or action approach.

## 90 Minutes: Prepare Evidence Pack and Management Review

Goal: Turn analysis into a review basis ready for decision-making.

1. Structure evidence in `templates/evidence-pack-index.md`.
2. If findings arise:
   - `audit-finding-writer`,
   - `corrective-action-planner`,
   - `templates/audit-finding-report.md`,
   - `templates/corrective-action-plan.md`.
3. If actions have been completed:
   - `remediation-effectiveness-review`,
   - `templates/remediation-effectiveness-review.md`.
4. Prepare management review:
   - `management-review-prep`,
   - `templates/management-review-agenda.md`,
   - `templates/decision-log.md`.
5. Check quality gates:
   - Public safety,
   - Claim safety,
   - operating logic,
   - human review,
   - handoff.

Output after 90 minutes:

- evidence pack index,
- action or decision log entry,
- review questions for management or owner,
- next workflow step.

## Universal Prompt

```text
You support me with krisensicherOS.

Use only provided content or content available in the repo.
No legal advice, data protection advice, compliance, certification, or security assurance.
No management decision.
Mark assumptions, gaps, evidence needs, and human gates.

Task:
Guide me through a 30/60/90-minute walkthrough for this scope: <Scope>.

Output:
1. Which file / which template I should open.
2. Which agent role or skill fits.
3. Which questions I need to answer.
4. Which evidence is created.
5. Which decision remains with humans.
```

## Definition of Done

The first walkthrough is complete when:

- scope and source are documented,
- at least one template is filled,
- evidence needs and owners are visible,
- human gates are marked,
- the next step in audit, evidence pack, or management review is clear.
