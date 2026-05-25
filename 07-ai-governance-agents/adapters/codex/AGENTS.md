<!-- kso:product-relevance
repo-scope: product
classification: tool-adapter
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# AGENTS.md — Codex Adapter for krisensicherOS

## Project

krisensicherOS is an open product repository for AI-assisted security governance; this branch provides the English product version. The goal is governance capability rather than document-driven compliance.

## Agent Profiles

Public agent profiles are located in `07-ai-governance-agents/agents/public/*.md`. Read the relevant profile in full before creating or revising an artifact.

The manifest is located in `07-ai-governance-agents/agents/manifest.yaml`.

## Basic Rules

- krisensicherOS requires approved AI usage.
- The preferred Codex path is an approved local repository workspace in an IDE; work through diffs, small artifacts, and clear reviews.
- First clarify scope, data class, AI usage approval, roles, human gates, and existing evidence with the user.
- No artifact without operating logic.
- No compliance clichés.
- No false assurance.
- No legal advice.
- No data protection advice.
- No certification or compliance guarantees.
- Responsibility remains human.
- Agents relieve, structure, and review; they do not decide on anyone’s behalf.
- Every recommendation includes observation, risk/opportunity, recommendation, and next step.

## Quality Check Before Completion

Check:

1. Is it clear who uses the artifact?
2. Is it clear when it is used?
3. Is it clear which decision or routine is supported?
4. Are boundaries and assumptions visible?
5. Are data class, AI usage approval, and human gates visible?
6. Are there no private data, tokens, or real customer data?
7. Are NIS2/ISMS statements formulated as governance support, not as legal or certification assurance?
