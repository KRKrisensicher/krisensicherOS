<!-- kso:product-relevance
repo-scope: product
classification: tool-adapter
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# CLAUDE.md — Claude CLI Adapter for krisensicherOS

## Mission

Work on krisensicherOS as an AI-assisted product repo for security governance. Use Claude CLI as an execution interface, not as a new subject-matter source.

## Source of Truth

For relevant work, read first:

1. `AGENTS.md`
2. `CLAUDE.md`
3. `README.md`
4. `agents/public/role-model.md`
5. appropriate profile under `agents/public/`
6. if needed, appropriate skill under `skills/<skill>/SKILL.md`
7. `evals/quality-gates.md`
8. `governance/product-relevance-process.md` when files are created or changed

## Working Rules

- krisensicherOS requires approved AI usage.
- Show a plan before multi-file changes.
- Change only necessary files.
- Subject-matter logic remains in repo artifacts, not in Claude-specific configuration.
- New or changed files need a valid `kso:product-relevance` tag.
- No commit, push, tag, release, or external sending without explicit approval.

## Boundaries

No:

- legal advice,
- data protection advice,
- compliance, certification, or security assurance,
- management decision,
- risk acceptance,
- processing of real personal, customer, contract, incident, system, or secret data without approval,
- reproduction of licensed standard texts.

## Final Report

At the end, report:

1. Changed files.
2. Which source-of-truth files were read.
3. Which quality gates were checked.
4. Which human gates remain open.
5. Whether commit/push/release was omitted or explicitly approved.
