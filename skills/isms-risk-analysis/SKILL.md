---
name: isms-risk-analysis
version: 1.0.0
description: "Guide ISMS risk analysis: scenario, assessment, strategy, actions, SoA link, and reporting."
category: governance
inputs:
  - scope
  - asset-or-process
  - vulnerability
  - threat
  - current-measures
  - evidence-sources
outputs:
  - risk-analysis-session-state
  - risk-register-entry
  - soa-risk-control-map-entry
  - measure-backlog
  - decision-log-items
  - risk-report-input
requires_human_review: true
---

<!-- kso:product-relevance
repo-scope: product
classification: agent-skill
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->


# isms-risk-analysis

## Purpose

This skill guides users dialogically through an ISMS risk analysis. It asks step-by-step questions until enough information is available to document the risk, current measure status, gross risk, strategy, measures, control/SoA reference, net/residual risk, and reporting input in a traceable way.

It is not a risk tool and does not make risk decisions. It structures preparatory work for accountable humans.

## When to use

Use this skill for:

- new or changed risk analysis in the ISMS,
- risk workshops,
- control/SoA review with risk reference,
- deriving measures from risks,
- preparing risk reporting or management review,
- continuing an interrupted risk analysis based on a session state.

## When not to use

Do not use for:

- risk acceptance on behalf of management,
- legal or data protection advice,
- certification, compliance, or security assurances,
- automated effectiveness confirmation without evidence,
- processing confidential content in public examples,
- reproducing licensed standard texts.

## Guiding principles

- SoA optional: If no dedicated ISO 27001 SoA is available, a Risk-Control Map is maintained first. ISO 27001 references require license-compliant use of standards and subject-matter approval.

- A risk can only be assessed once **vulnerability + asset + threat** have been named separately.
- The skill asks **only the next sensible question** instead of overwhelming the user with all questions at once.
- Unclear answers are marked as **assumption** or **open question**.
- AI may structure and suggest; owners must confirm from a subject-matter perspective.
- Risk acceptance, transfer, avoidance, and resources are human gates.
- Report confirmed net risk only after implementation and effectiveness review.

## Required artifacts

Primary artifacts in the repo:

- `04-isms-basics/risikomanagement-methodik.md`
- `templates/risikoanalyse-fragebogen.md`
- `templates/risikoanalyse-session-state.md`
- `templates/risikoanalyse-register.md`
- `templates/soa-risk-control-map.md`
- `templates/risikoreport.md`
- `templates/risikoreport-html.html`
- `templates/decision-log.md`
- `playbooks/isms-risikoworkshop.md`
- `workflows/isms-risk-to-soa.yaml`

## Dialogic flow

### Phase 0: Start or continue session

Check whether a session state already exists.

If yes:
- identify open mandatory fields,
- review the last human gates and assumptions,
- continue with the next open phase.

If no:
- create a new session state according to `templates/risikoanalyse-session-state.md` or maintain it mentally.

Output: `risk-analysis-session-state`.

### Phase 1: Describe scope and risk

Goal: Formulate the risk as a verifiable scenario.

Mandatory fields:
- scope / area,
- asset / process / service,
- asset owner or subject-matter owner,
- vulnerability,
- threat,
- impact.

Guiding questions:
- Which asset, process, or service is affected?
- Which specific vulnerability makes the risk possible?
- Which threat can exploit this vulnerability?
- What would be the plausible impact?

If users answer vaguely, separate the elements:
- “Cloud is insecure” → Which cloud service? Which vulnerability? Which threat?
- “Ransomware” → Which asset? Which vulnerability enables the attack?

Output: Risk scenario in the format:

```text
If [threat] exploits the vulnerability [vulnerability] on asset [asset],
then [impact] may occur.
```

### Phase 2: Capture current measure status

Goal: Make current controls, routines, evidence, and gaps visible.

Guiding questions:
- Which organizational measures already exist?
- Which technical measures already exist?
- Which procedural or personnel-related measures already exist?
- Which incident response, crisis management, or BCMS capabilities limit the damage?
- Which measures are actually operated regularly?
- Which evidence shows implementation and operation?
- Which control/SoA references are affected?

Rule:
- Mark answers as `confirmed`, `assumption`, `open`, or `evidence-checked`.
- Do not claim effectiveness without owner confirmation.

Output: Measure status snapshot and evidence gaps.

### Phase 3: Assess gross risk

Goal: Assess gross risk using the same criteria that will later be used for net/residual risk.

Assess likelihood:
- detectability,
- exploitability,
- concealment.

Assess extent of damage:
- property damage,
- personal injury,
- financial loss,
- intangible damage.

Rules:
- Likelihood factor = maximum value from detectability, exploitability, concealment.
- Damage factor = maximum value from property damage, personal injury, financial loss, intangible damage.
- Risk value = likelihood factor × damage factor.
- Current measure status is context; it does not automatically reduce the gross value.

Output: Gross value, category, rationale.

### Phase 4: Select or prepare strategy

Goal: Prepare the treatment strategy as a human gate.

Options:
- acceptance,
- avoidance,
- transfer,
- minimization through measures.

Transfer may mean:
- insurance,
- outsourcing,
- contractual arrangement,
- handover of specific response components into crisis management or BCMS.

Guiding questions:
- Which strategy is plausible and why?
- Which strategy is unsuitable and why?
- Who must decide?
- What is the consequence of inaction?

Output: Strategy options, recommendation as preparatory work, human gate.

### Phase 5: Derive measures and map controls / SoA

Goal: Derive measures from the specific risk and connect them with control/SoA logic.

Guiding questions:
- Which measure reduces which vulnerability?
- Which measure prevents, makes harder, detects, or limits which threat?
- Which measure reduces likelihood, extent of damage, or both?
- Which owner implements it?
- Which evidence is created?
- How is effectiveness reviewed?
- Which control/SoA ID or which control cluster is affected?

Output:
- measure backlog,
- Risk-Control Map / SoA extension,
- decision log entries.

### Phase 6: Assess net/residual risk

Goal: Assess residual risk after strategy and measure planning.

Use the same criteria as in Phase 3:
- detectability,
- exploitability,
- concealment,
- property damage,
- personal injury,
- financial loss,
- intangible damage.

Rules:
- Mark net/residual risk as `planned value` if measures have not yet been implemented or have not been effectiveness-reviewed.
- Mark as `confirmed` only after evidence and effectiveness review.
- Justify every change compared with gross risk.

Output: Net/residual risk value, category, status, rationale.

### Phase 7: Generate reporting

Goal: Condense results for workshop, management review, or steering committee.

Reporting content:
- risk scenario,
- current measure status,
- gross and net/residual risk,
- strategy,
- measure status,
- control/SoA reference,
- evidence status,
- open decisions,
- next reviews.

Output:
- make `templates/risikoreport.md` fillable,
- optionally prepare HTML presentation according to `templates/risikoreport-html.html`.

## Conversation control

Work with short, precise questions. Ask a maximum of 1-3 questions at the same time.

If a mandatory field is missing, ask about it first.

If an answer mixes multiple concepts, separate them visibly:

```text
I read this as:
- Asset: ...
- Vulnerability: ...
- Threat: ...
Is that correct?
```

If enough information is available for a phase:
- briefly summarize the phase,
- mark open assumptions,
- announce the next phase.

## Output format for each interim status

```text
Status:
- Phase:
- Completed:
- Open:
- Assumptions:
- Human Gate:
- Next question:
```

## Verification

Check before completion:

```text
Verification:
- Risk formula: pass / notes / stop
- Assessment sequence: pass / notes / stop
- Gross criteria: pass / notes / stop
- Strategy human gate: pass / notes / stop
- Measure logic: pass / notes / stop
- Control/SoA mapping: pass / notes / stop
- Net/residual risk status: pass / notes / stop
- Reporting readiness: pass / notes / stop
- Public Safety: pass / notes / stop
- Claim Safety: pass / notes / stop
- Result: pass / pass with notes / stop
```

## Quality gates

To be applied from `evals/quality-gates.md`:

- U1 Public-Safe Gate,
- U2 Claim-Safety Gate,
- U3 Operating-Logic Gate,
- U4 Empowerment Gate,
- U5 Workload Gate,
- U6 Portability Gate,
- A2 Skill Gate.

## Handoffs

Typical handoffs:

- to `control-evidence-architect` if evidence or control mapping needs to be deepened,
- to `management-review-facilitator` if decisions need to be prepared,
- to `remediation-effectiveness-review` if measure effectiveness should be reviewed,
- to data protection, legal, or procurement if transfer, contracts, or personal data are affected.

## Boundaries

This skill does not provide legal advice, does not provide data protection advice, does not provide certification or compliance assurance, and does not make management decisions.

It must not include confidential content, real customer data, or licensed standard texts in public artifacts.
