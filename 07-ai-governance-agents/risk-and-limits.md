<!-- kso:product-relevance
repo-scope: product
classification: product-module
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Risks and Limits of Agentic Governance Work

## Purpose

This document makes typical risks in the use of governance agents visible and describes countermeasures for krisensicherOS user organizations.

## Central Risks

### 1. False Assurance

Risk: An agent output sounds more authoritative than it is.

Countermeasures:

- explicitly limit claims,
- keep assumptions and gaps visible,
- use `agent-quality-and-safety-reviewer`,
- have management and legal questions reviewed by humans.

### 2. Shift of Responsibility

Risk: Agents are effectively treated as decision-makers.

Countermeasures:

- use human gates mandatorily,
- document owners, reviewers, and decision-makers,
- maintain a decision log,
- treat agent outputs only as preparation.

### 3. Source Misuse

Risk: licensed standard texts, confidential contracts, or private content are copied or used incorrectly.

Countermeasures:

- enter sources only as metadata or as your own summary,
- mark confidentiality and license status for each register entry,
- do not include confidential content in public examples,
- stop unclear sources and have them reviewed by humans.

### 4. Data Protection and Personal Data

Risk: personal data is unnecessarily included in agent contexts.

Countermeasures:

- data minimization,
- pseudonymization or fictional examples,
- escalate data protection interfaces to the responsible roles,
- no personal data in public artifacts.

### 5. Bureaucratization

Risk: Agents create more lists, meetings, and documents without improving decisions.

Countermeasures:

- use the workload gate,
- every artifact needs a trigger, owner, output, evidence, and review,
- remove unnecessary routines,
- check management relevance.

### 6. Tool Lock-in

Risk: Business logic ends up in a single tool prompt or adapter.

Countermeasures:

- maintain canonical artifacts in the repo,
- keep adapters thin,
- describe handoffs and workflows in a tool-neutral way,
- version profiles, skills, and templates.

### 7. Outdated Assumptions

Risk: Sources, risks, or organizational reality change, but agents work with an outdated state.

Countermeasures:

- set review frequencies,
- maintain register status,
- date assumptions,
- review evidence packs regularly.

## Risk Assessment Before Use

Before productive use, check:

| Question | Pass | Stop |
| --- | --- | --- |
| Is the scope clear? | Scope and non-scope documented | unclear or overly broad scope |
| Are the data permitted? | public-safe or internally approved | personal/confidential without approval |
| Are the sources clean? | reference, metadata, or own summary | full text of licensed or confidential content |
| Are human gates visible? | owner/reviewer/decision-maker named | agent is supposed to decide |
| Is the output usable? | routine, evidence, decision clear | only document without operating logic |

## Hard Limits

Agents must not:

- provide legal advice,
- provide data protection advice,
- make management decisions,
- declare risk acceptance,
- make compliance, certification, or security assurances,
- publicly reproduce confidential or licensed content,
- write real customer data into public examples,
- send external communication without approval.

## Definition of Done

Risks and limits are addressed sufficiently when:

- relevant risks are identified,
- countermeasures are visible in the workflow,
- stop points are clear,
- human gates are named,
- quality gates have been applied,
- open uncertainties have not been smoothed over.
