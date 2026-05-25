<!-- kso:product-relevance
repo-scope: product
classification: product-standard
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; product-safety; release-readiness
-->

# Codex-optimized Agent Profile Standard

Status: 2026-05-23

This standard describes how agent profiles are written in krisensicherOS so that they are easy to use for Codex CLI and comparable coding agents.

## Goal

An agent profile should not only describe a role, but give Codex precise work instructions:

- when the agent is relevant,
- which inputs are expected,
- how the work is performed,
- which outputs are created,
- which quality gates apply before completion,
- which boundaries must not be crossed,
- to whom results are handed off.

## Profile Structure

Each profile uses these sections:

1. `Brief Summary for Codex CLI`
2. `Vault Origin and Transformation Logic`
3. `Mandate`
4. `Primary Lever`
5. `When to Use`
6. `When Not to Use`
7. `Input Data`
8. `Working Mode`
9. `Standard Workflow`
10. `Typical Deliverables`
11. `Output Format`
12. `Quality Gates`
13. `Boundaries and Red Lines`
14. `Interfaces and Handoffs`
15. `Example Prompts`
16. `Definition of Done`

## Codex Optimization

Codex CLI benefits from explicit, verifiable rules. Therefore:

- Write concrete action instructions instead of abstract role prose.
- Use checklists, stop rules, and output contracts.
- Clearly mark uncertainties and missing inputs.
- Do not derive external or legal assurances.
- Finish work only after a brief quality check.
- Avoid tool- or runtime-specific assumptions unless they are in the adapter.

## Minimum Quality Gate for Each Agent Result

Each result must answer at least:

- Observation: What is the relevant finding?
- Risk/Opportunity: Why is this important?
- Recommendation: What should be done?
- Next Step: What specifically needs to be done next?
- Boundary: What can this result not provide?

## Public Safety

Agent profiles must not contain private workspace information, tokens, customer data, or personal examples. Examples must be fictional.
