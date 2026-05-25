<!-- kso:product-relevance
repo-scope: product
classification: template
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->

# AI usage approval matrix

## Purpose

This template clarifies, before using AI systems, which data may be processed with which AI environment and which safeguards are required.

It does not replace a data protection assessment, legal review, or internal organizational AI usage approval. It creates a working artifact for human review.

## Trigger

- a document, interview, evidence pack, or register entry is to be processed with AI,
- a new AI environment is to be used for krisensicherOS,
- cloud AI, M365 Copilot, local AI, or redaction tools are to be used.

## Roles

- CISO/information security officer or GRC lead,
- data protection / legal for review questions,
- IT/AI system owner,
- business owner,
- management for risk or approval decisions.

## Approval table

| Field | Classification / decision | Owner | Human Gate |
| --- | --- | --- | --- |
| Work purpose |  |  |  |
| Data class | public / internal / confidential / personal / licensed |  |  |
| Contains personal data? | no / yes / unclear |  | data protection handoff if yes/unclear |
| Contains secrets or credentials? | no / yes / unclear |  | Stop until cleaned |
| Contains licensed standard texts? | no / yes / unclear |  | Stop until clarified |
| Permitted AI environment | approved cloud AI / M365 Copilot / local AI / isolated environment / not approved |  | Stop if not approved |
| Redaction/masking required? | no / yes / unclear |  |  |
| Optional redaction tool | e.g., OpenAI Privacy Filter / other / not used |  |  |
| Redaction reviewed? | not needed / reviewed / open |  | Human review for sensitive data |
| Storage location for input/output |  |  |  |
| Logging / traceability |  |  |  |
| Approval for this use case | approved / restricted / not approved |  |  |


## Local AI: link operating checklist

If `local AI` or a local redaction tool is selected, `docs/setup/lokale-ki.md` must also be reviewed. Model/checkpoint approval, Windows pilot, storage locations, logging, network binding, team use, evaluation, and offboarding are clarified there. The summary overview is additionally available in `docs/setup/ki-setups-bedienungsanleitung.md`.

## Redaction note

PII/secret redaction tools such as OpenAI Privacy Filter can be used as an additional protective layer. They are not an anonymization guarantee, not a data protection assessment, and not compliance evidence.

Review before production use:

- Which categories are detected?
- Which local data formats may be missed?
- How are false positives and false negatives reviewed?
- Who decides on approval after redaction?
- Are inputs, outputs, or logs stored?

## If no AI usage approval exists

If no AI usage approval exists, krisensicherOS is not used in production. This matrix then only serves to prepare the approval decision:

- describe the use case,
- clarify data classes,
- define the permitted AI environment,
- define prohibited content and human gates,
- reassess AI use later.

## Quality gates

- Data class is known or marked as open.
- Prohibited content is excluded or leads to stop.
- Permitted AI environment is documented.
- Redaction is not confused with anonymization.
- Human gates are visible.
- Output contains no legal, data protection, compliance, or certification assurance.
