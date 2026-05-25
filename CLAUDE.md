<!-- kso:product-relevance
repo-scope: product
classification: product-governance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; product-safety; release-readiness
-->

# CLAUDE.md — krisensicherOS

Notes for Claude Code and comparable coding agents in this repository.

## Mission

Work on krisensicherOS as an open, portable operating repository for security governance, NIS2 readiness, ISMS, BCMS, crisis readiness, and AI-assisted governance.

The repo does not build governance for a specific organization. It provides building blocks that organizations can use to operate their own governance.

## Working rules

- Write public-safe artifacts.
- Use fictional examples.
- No real customer data, personal data, or private workspace details.
- No legal advice, data protection advice, certification guarantees, or compliance guarantees.
- Do not reproduce ISO standard texts or confidential contract content.
- Treat licensed sources only as metadata, references, mappings, or own summaries.
- Operating logic before document logic: every artifact needs purpose, users, trigger, input, process, output, evidence, and boundaries.

## Important paths

- `README.md` — product positioning and orientation
- `knowledge/` — fixed public reference sources
- `compliance-register/` — structure for user-owned requirements
- `agents/` — canonical agent profiles and manifest
- `agents/public/` — public target-repo agents for user organizations
- `skills/` — reusable AgentSkills
- `templates/` — usable work templates
- `workflows/` — agentic workflow models
- `evals/` — quality and safety gates
- `docs/standards/` — profile, skill, and artifact standards

## Quality check before completion

Check at minimum:

1. Public-safe: no private details, real data, or secrets.
2. Claim-safe: no legal, data protection, compliance, or certification statements.
3. Operational: roles, triggers, inputs, outputs, evidence, and review points are clear.
4. Empowerment-first: the user organization remains able to decide and learn.
5. Portability: no tool-specific domain logic in the canonical artifact.

## Commit notes

Coherent changes may be committed locally only if the task or human approval explicitly permits it. No push, no publication, no license/disclaimer change, and no external transmission without explicit approval.
