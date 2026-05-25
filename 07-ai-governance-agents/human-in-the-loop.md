<!-- kso:product-relevance
repo-scope: product
classification: product-module
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Human-in-the-loop for krisensicherOS Agents

## Purpose

This document describes which decisions always remain with humans when using krisensicherOS agents and how agent work is embedded in governance routines in a controlled way.

Agents structure, review, and prepare. They do not assume responsibility.

## Basic Rule

Every agent output needs at least one accountable human role if it results in a decision, approval, external statement, or change to real governance routines.

## Human Gates

### H1 — Scope Gate

Before starting, humans clarify:

- affected organizational unit, services, or processes,
- non-scope,
- permitted data and sources,
- desired output,
- accountable owner.

### H2 — Source Gate

Human review is required for:

- legal applicability,
- regulatory interpretation,
- interpretation of customer or supplier contracts,
- data protection assessment,
- licensed standards,
- unclear confidentiality.

Agents may reference sources, map them, and prepare questions. They do not make binding decisions about meaning or obligation.

### H3 — Risk Gate

Human review is required for:

- risk acceptance,
- prioritization with resource impact,
- deviations from existing policies,
- material residual risks,
- escalation to management or committees.

### H4 — Evidence Gate

Human review is required when evidence:

- is incomplete or outdated,
- is contradictory,
- contains confidential information,
- is intended to become the basis for external statements or management decisions.

### H5 — Output Gate

Before use or sharing, humans review:

- Are scope, assumptions, and boundaries visible?
- Are claims limited?
- Is there no legal advice, data protection advice, certification assurance, or compliance assurance?
- Are owner, review cadence, and next step clear?
- Is the result public-safe or only usable internally?

### H6 — External Gate

Always require human approval before:

- publication,
- sending to customers, authorities, auditors, or insurers,
- Git push to public repos,
- release tags,
- official management or board materials.

## Human Gate Matrix

| Situation | Agent may | Human must |
| --- | --- | --- |
| new source | capture metadata, derive questions | review applicability and interpretation |
| NIS2/ISMS gap | structure the gap, derive evidence needs | decide risk and priority |
| Evidence Pack | review completeness and traceability | approve suitability for decision-making |
| Management Review | prepare agenda, options, risks | make the decision |
| Incident Readiness | prepare escalation logic and exercise | lead live decisions |
| Data protection interface | prepare review questions and handoff | remain accountable for data protection assessment |
| Contract requirement | structure requirements as metadata | remain accountable for contract interpretation |

## Stop Points

Agent work stops when:

- real confidential data could end up in public artifacts,
- licensed standard texts are to be reproduced,
- a binding legal or data protection assessment is requested,
- an agent is expected to make a management decision,
- external communication is prepared without approval,
- a result sounds like a guarantee, certification, or confirmation of compliance.

## Definition of Done

Human-in-the-loop is fulfilled when:

- accountable human role is named,
- human gates are visible in the workflow,
- open decisions have not been smoothed over,
- output boundaries and assumptions are documented,
- handoff to management, legal, data protection, owner, or reviewer is clear.
