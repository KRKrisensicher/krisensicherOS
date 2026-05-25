<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Prompt Library

krisensicherOS follows an empowerment-first approach.

The goal is not to make users dependent on consultants or agents. The goal is to enable internal information security officer/CISO and governance teams to understand, build, review, and further develop their own agentic working model.

## Purpose

The prompt library helps users to:

- brief agents effectively,
- build their own compliance registers,
- work through NIS2/ISMS/BCMS questions in a structured way,
- critically review results,
- prepare management decisions,
- avoid outsourcing responsibility to agents.

## Basic Rule

Prompts in krisensicherOS should not appear magical. They should explain which inputs are needed, which outputs are produced, and where human review is required.

## Files

- [`empowerment-first-prompt-bibliothek.md`](empowerment-first-prompt-bibliothek.md) — Starter library for users.

## Prompt Quality Criteria

A good krisensicherOS prompt includes:

1. context
2. agent role
3. objective
4. input data
5. desired output format
6. boundaries
7. review/approval note
8. next step

## Anti-Patterns

Do not use:

- “Build me a finished ISMS.”
- “Confirm that we are NIS2-compliant.”
- “Create ISO 27001-compliant documentation.”
- “Provide a binding assessment of the contract.”

Better:

- “Help me prepare a gap analysis.”
- “Derive questions for human review.”
- “Map this internal summary to possible evidence needs.”
- “Formulate decision options for management.”
