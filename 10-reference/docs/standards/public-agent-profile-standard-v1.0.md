# Public Agent Profile Standard v1.0

Status: 2026-05-23

This standard applies to all public target-repo agents under `07-ai-governance-agents/agents/public/`.

## Purpose

Public agent profiles must at least meet the quality of the internal krisensicherOS project agents, while remaining portable for user organizations.

They should enable organizations to build their own compliance, security governance, NIS2, ISMS, and BCMS work in an agentic way, without outsourcing responsibility, legal review, or management decisions to agents.

## Mandatory Structure

Each profile contains:

1. YAML frontmatter
2. Brief summary for Codex CLI
3. Identity & Operating Voice
4. Mandate
5. Primary leverage
6. When to use
7. When not to use
8. Input data
9. Working mode
10. Standard workflow
11. Typical deliverables
12. Output format
13. Success metrics
14. Quality gates
15. Mini example
16. Anti-patterns
17. Boundaries and red lines
18. Interfaces and handoffs
19. Handoff protocol
20. Example prompts
21. Definition of Done

## Additional Requirements for Public User Agents

Public agents must additionally make visible:

- **Human-in-the-loop:** Who must review, decide, or approve?
- **Relevant skills:** Which skills should the agent use once they are available?
- **Output artifacts:** Which repo artifacts are created or used?
- **Mandatory handoff points:** When must work be handed over to other agents?
- **Portability:** No tool-specific commands in the canonical profile.
- **Work reduction:** Which work is reduced or made more decision-ready?

## Red Lines

No public profile may:

- claim to provide legal advice,
- claim to provide data protection advice,
- confirm NIS2 compliance,
- confirm ISO certification readiness,
- replace management decisions,
- request real customer data or confidential contract data,
- reproduce ISO standard texts or licensed content,
- position agents as a replacement for internal accountable roles.

## Review Gates

Before merging a public agent profile, check:

- frontmatter complete,
- mandate narrow and distinguishable,
- non-responsibility clear,
- inputs/outputs concrete,
- success metrics verifiable,
- quality gates present,
- mini example present,
- handoff protocol executable,
- human-in-the-loop visible,
- no private workspace details,
- no tool adapter logic,
- no false assurance,
- contribution to enabling the user organization clear.

## Manifest Rule

Each profile in `07-ai-governance-agents/agents/public/*.md` must be referenced in `07-ai-governance-agents/agents/manifest.yaml`.

Each manifest entry must contain at least:

- `name`
- `path`
- `family`
- `purpose`
- `use_when`
- `do_not_use_when`
- `handoffs_to`
- `human_review_required_for`
- `adapters`

## Adapter Rule

Claude Code, Codex, OpenClaw, Hermes, or other adapters may export or reference public profiles. They must not contain divergent subject-matter logic.
