<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Adapter

Adapter übersetzen krisensicherOS in konkrete KI-Oberflächen, ohne Fachlogik zu duplizieren.

Kanonische Fachlogik bleibt in:

- `AGENTS.md`,
- `CLAUDE.md`,
- `07-ai-governance-agents/agents/public/`,
- `07-ai-governance-agents/skills/`,
- `templates/`,
- `workflows/`,
- `governance/`,
- `06-evidence-management-review/evals/`.

## Vorhandene Adapter

- [`codex/`](codex/) — Codex CLI.
- [`claude-cli/`](claude-cli/) — Claude Code CLI.
- [`m365-copilot/`](m365-copilot/) — Microsoft 365 Copilot, SharePoint Agents und Copilot Studio.
- [`orgavision-mcp/`](orgavision-mcp/) — Orgavision MCP als optionaler Verteil- und Wissenszugang für freigegebene Governance-Artefakte.

## Adapter-Regel

Ein Adapter darf erklären:

- welche Dateien zuerst gelesen werden,
- welche Toolfunktionen genutzt werden,
- welche Prompts passen,
- welche Setup- und Sicherheitsgrenzen gelten.

Ein Adapter darf nicht:

- Rechts-, Datenschutz-, Konformitäts- oder Zertifizierungslogik verstecken,
- Produktgrenzen abschwächen,
- Human Gates entfernen,
- vertrauliche oder lizenzpflichtige Inhalte einbetten,
- direkte Veröffentlichung oder externe Kommunikation automatisieren.
