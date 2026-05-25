<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Adapters

Adapters translate krisensicherOS into specific AI interfaces without duplicating domain logic.

Canonical domain logic remains in:

- `AGENTS.md`,
- `CLAUDE.md`,
- `agents/public/`,
- `skills/`,
- `templates/`,
- `workflows/`,
- `governance/`,
- `evals/`.

## Existing adapters

- [`codex/`](codex/) — Codex CLI.
- [`claude-cli/`](claude-cli/) — Claude Code CLI.
- [`m365-copilot/`](m365-copilot/) — Microsoft 365 Copilot, SharePoint Agents, and Copilot Studio.
- [`orgavision-mcp/`](orgavision-mcp/) — Orgavision MCP as an optional distribution and knowledge-access path for approved governance artifacts.

## Adapter rule

An adapter may explain:

- which files are read first,
- which tool functions are used,
- which prompts fit,
- which setup and security boundaries apply.

An adapter must not:

- hide legal, data protection, compliance, or certification logic,
- weaken product boundaries,
- remove human gates,
- embed confidential or licensed content,
- automate direct publication or external communication.
