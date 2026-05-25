<!-- kso:product-relevance
repo-scope: product
classification: template
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->

# AI system inventory and preliminary risk check

## Purpose

This template captures AI systems, AI functions, or AI use cases as a working inventory. It helps make data classes, responsibilities, human oversight, and open handoffs visible.

It does not replace legal advice, data protection assessment, EU AI Act classification, technical security review, or management decision.

## Trigger

Use this template when:

- a new AI system is procured, activated, or piloted,
- an existing application receives new AI functions,
- cloud AI, M365 Copilot, local AI, or a business application with AI is to be used,
- AI usage becomes relevant in NIS2, ISMS, data protection, supplier, or management review work,
- it is unclear which human gates are needed.

## Roles

- Business system or process owner,
- IT/security owner,
- AI/tool owner,
- data protection,
- legal / contract management,
- management for risk, budget, or approval decisions.

## Inventory

| Field | Entry |
| --- | --- |
| Inventory ID |  |
| System / service / AI function |  |
| Provider / operator |  |
| Internal responsible role |  |
| Business purpose |  |
| Affected process |  |
| User group |  |
| Usage status | idea / pilot / production / suspended / decommissioned |
| Deployment location | cloud / M365 / local AI / business application / embedded / unclear |
| External dependencies |  |
| Contract/supplier reference | no / yes / unclear |
| Source / reference |  |

## Preliminary check

| Check field | Working assumption | Owner | Human Gate |
| --- | --- | --- | --- |
| Role of the organization | uses / operates / integrates / provides / unclear |  | Legal/Management |
| Data class | public / internal / confidential / personal / especially sensitive / unclear |  | Data protection/Security |
| Personal data reference | no / yes / unclear |  | Data protection |
| Affected groups of persons | none / employees / customers / citizens / suppliers / unclear |  | Data protection/Legal |
| Decision proximity | assisting / recommending / prioritizing / automating / unclear |  | Business owner/Legal |
| Effect on persons | none / low / relevant / high / unclear |  | Legal/Data protection/Management |
| Criticality for process | low / medium / high / critical / unclear |  | IT/Security/Management |
| Security relevance | no / yes / unclear |  | Security |
| Human oversight defined | yes / no / unclear |  | Business owner/Management |
| Logging / traceability | available / partial / missing / unclear |  | IT/Security |
| Redaction or data minimization needed | no / yes / unclear |  | Data protection/Security |
| Approved AI environment available | yes / no / restricted / unclear |  | AI/IT owner |
| Handoff needed | Legal / Data protection / Management / IT security / Supplier / none / unclear |  | respective role |

## Human oversight

| Question | Answer |
| --- | --- |
| Who may approve inputs? |  |
| Who reviews AI outputs from a business perspective? |  |
| Who may adopt or reject AI outputs? |  |
| When must work be stopped? |  |
| How are errors, complaints, or anomalies reported? |  |
| When is the approval reviewed? |  |

## Risks and open questions

| Topic | Observation | Decision needed? | Owner | Deadline |
| --- | --- | --- | --- | --- |
| Data / data protection |  |  |  |  |
| Legal / EU AI Act role |  |  |  |  |
| Security / misuse |  |  |  |  |
| Supplier / contract |  |  |  |  |
| Process impact |  |  |  |  |
| Evidence / logging |  |  |  |  |

## Handoff decision

| Target role | Question | Context | Required feedback | Status |
| --- | --- | --- | --- | --- |
| Legal |  |  |  | open |
| Data protection |  |  |  | open |
| Management |  |  |  | open |
| IT/Security |  |  |  | open |
| Supplier/contract management |  |  |  | open |

## Output

- Inventory entry for an AI system or AI use case,
- data class and usage assumption,
- marked human gates,
- open questions for legal, data protection, management, IT/security, or supplier management,
- decision log entry with next step.

## Quality gates

- Do not enter real personal, customer, contract, or system secrets in public examples.
- Do not claim a final legal, data protection, or EU AI Act classification.
- Data class and human oversight are known or marked as open.
- Critical or unclear usage leads to handoff, not automatic approval.
- Decisions are documented in [`decision-log.md`](../../02-governance-operating-model/templates/decision-log.md).
