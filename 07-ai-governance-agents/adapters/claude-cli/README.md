# Claude CLI Adapter

## Purpose

This adapter describes how krisensicherOS is used with Claude Code CLI without moving domain logic into Claude-specific configuration.

Canonical content remains in the repo:

- `AGENTS.md` — repo-wide working rules,
- `CLAUDE.md` — Claude-compatible project instructions,
- `07-ai-governance-agents/agents/public/*.md` — public agent roles,
- `07-ai-governance-agents/agents/manifest.yaml` — role/routing manifest,
- `07-ai-governance-agents/skills/*/SKILL.md` — repeatable skills,
- `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md` — quality and safety gates.

## Research basis

Status: 2026-05-25.

Reviewed public vendor documentation:

- Claude Code Docs: Commands — including `/init`, `/memory`, `/mcp`, `/agents`, `/permissions`, `/plan`, `/diff`, `/code-review`, `/security-review`.
- Claude Code Docs: Settings — scope model with Managed, User, Project, and Local; project configuration in `.claude/`; `CLAUDE.md` or `.claude/CLAUDE.md`; local overrides in `CLAUDE.local.md`.

## Adapter principle

Claude CLI must not reinvent krisensicherOS. The adapter only translates:

- which files Claude should read first,
- which Claude commands are typically useful,
- which configuration may be committed,
- which local settings do not belong in the product repo,
- which quality gates must be reported before completion.

## Recommended start in Claude CLI

In the local repo:

```bash
claude
```

Initial read-only prompt:

```text
Work read-only at first.
Read AGENTS.md, CLAUDE.md, README.md, 07-ai-governance-agents/agents/manifest.yaml, and 06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md.
Do not read files outside this repo folder.
Do not perform write operations, shell commands with side effects, Git actions, pushes, releases, or external messages.
Then provide:
1. Which krisensicherOS rules apply.
2. Which agent role fits my task.
3. Which human gates must be observed.
4. Which quality gates must be met before changes.
```

## Useful Claude commands

| Situation | Claude command | krisensicherOS rule |
| --- | --- | --- |
| Initial setup | `/init` | Use only if the existing `CLAUDE.md` is not overwritten. |
| Check project memory | `/memory` | Do not write private workspace or customer data into shared project memory. |
| Plan large change | `/plan` | Required before any multi-file change. |
| Check 07-ai-governance-agents/agents/subagents | `/agents` | Domain logic remains in `07-ai-governance-agents/agents/public/*.md`, not only in Claude configuration. |
| Configure MCP | `/mcp` | Only approved servers, no secrets in repo files. |
| Set permissions | `/permissions` | Keep write, shell, and network rights restrictive. |
| Check diff | `/diff` | Always check before commit/approval. |
| Perform review | `/code-review` or `/security-review` | Supplements but does not replace human review. |

## Project configuration

If Claude project configuration is used:

- `.claude/settings.json` may only contain public-safe, team-ready settings.
- `.claude/settings.local.json` remains local and must not be committed.
- `CLAUDE.local.md` remains local and must not replace product logic.
- MCP servers, hooks, or plugins are documented only if they are portable and approved for the product repo.

## Recommended Claude working sequence

1. Read-only initial run.
2. Select a suitable role from `07-ai-governance-agents/agents/public/role-model.md`.
3. Read the relevant profile fully.
4. For a repeatable task, read the suitable skill from `07-ai-governance-agents/skills/`.
5. Create a plan.
6. Make the minimal change.
7. Run `git diff --check` and suitable repo QA.
8. Report diff and quality gates.
9. No commit, push, tag, or release without explicit human approval.

## Change prompt

```text
Task: <specific change>

Use krisensicherOS with Claude CLI.
First read AGENTS.md, CLAUDE.md, 07-ai-governance-agents/agents/public/role-model.md, and the suitable profile under 07-ai-governance-agents/agents/public/.
If a skill fits, also read 07-ai-governance-agents/skills/<skill>/SKILL.md.

Rules:
- Show the plan first.
- Change only necessary files.
- No legal advice, data protection advice, compliance, certification, or security assurance.
- No real person, customer, contract, incident, system, or secret data.
- Do not reproduce licensed standard texts.
- Mark assumptions, gaps, evidence needs, and human gates.
- Check product relevance tags when files are newly created or changed.
- No commit, push, tag, release, or external sending without explicit approval.

Output:
1. Plan.
2. Changed files.
3. QA result.
4. Human gates.
5. Open points.
```

## Stop points

Stop and obtain human approval for:

- missing AI usage approval,
- unclear data class,
- real organization, customer, or personal data,
- secrets or access credentials,
- licensed standard texts,
- legal or data protection assessment,
- risk acceptance or management decision,
- publication, push, tag, release, or external communication,
- Claude configuration with non-portable domain logic.

## Adapter quality gate

Before completion, Claude CLI reports:

```text
Adapter Gate:
- Source-of-truth files read: yes/no
- Domain logic in repo instead of adapter: yes/no
- Product relevance tags checked: yes/no
- Public safety checked: yes/no
- Claim safety checked: yes/no
- Human gates marked: yes/no
- Not performed: push/release/external sending
```
