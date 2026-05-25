<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Codex CLI Adapter

This adapter describes how krisensicherOS should be used with Codex CLI.

## Basic idea

Codex CLI primarily reads clear repo instructions and works well with precise Markdown profiles, verifiable working rules, and concrete quality gates.

The most important usage path is an **approved local IDE or local repository workspace**: the repository is available locally, Codex works in the project context, and the user clarifies scope, data class, AI usage approval, roles, human gates, and the next useful governance work step together with Codex.

Codex should not only edit files. It should act as a working companion that helps translate management-system work into questions, conversations, evidence, reviews, and decisions.

## Using a local IDE

1. Clone or open this repository in an approved local work environment, such as VS Code, Cursor, JetBrains, or another IDE with Codex integration.
2. Make sure the local environment is approved for the planned data class. Do not introduce real personal, customer, contract, incident, secret, or licensed standard content without appropriate approval.
3. Open Codex in the repository context and start with a concrete goal, such as: “Help me prepare a minimal NIS2 start for our organization.”
4. Let Codex ask the clarification questions first: scope, data class, AI usage approval, roles, existing evidence, human gates, and desired result.
5. Then let Codex select the appropriate profiles, skills, templates, or playbooks from the repository and create one small usable artifact.
6. Review changes in the IDE via diff, review, and quality gate before accepting them.

## Repository usage

- Public-safe repo instructions belong in `AGENTS.md`.
- Agent roles are canonical under `07-ai-governance-agents/agents/public/*.md`.
- The role manifest is under `07-ai-governance-agents/agents/manifest.yaml`.
- Skills are under `07-ai-governance-agents/skills/<skill-name>/SKILL.md`.
- Workflows are under `workflows/*.yaml`.

## Working rule

When Codex simulates or uses a krisensicherOS agent:

1. Read the appropriate profile in `07-ai-governance-agents/agents/public/*.md`.
2. Mark input data, data class, AI usage approval, and missing information.
3. Clarify open questions with the user instead of inventing assumptions about the organization, legal position, or risk acceptance.
4. Follow the profile's standard workflow.
5. Deliver the result in the defined output format.
6. Check quality gates.
7. Make boundaries, human gates, and review needs visible.

## Do not do

- Do not claim legal advice.
- Do not derive a certification guarantee.
- Do not publish private OpenClaw workspace files.
- Do not treat workrepo artifacts as product content.
- Do not treat vault files as operational truth.
