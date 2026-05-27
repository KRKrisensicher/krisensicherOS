
# Adapter

Adapter übersetzen krisensicherOS in konkrete KI-Oberflächen, ohne Fachlogik zu duplizieren.

Kanonische Fachlogik bleibt in:

- `AGENTS.md`,
- `CLAUDE.md`,
- `agents/public/`,
- `skills/`,
- `templates/`,
- `workflows/`,
- `governance/`,
- `evals/`.

## Vorhandene Adapter

- [`codex/`](codex/) — Codex CLI.
- [`claude-cli/`](claude-cli/) — Claude Code CLI.
- [`m365-copilot/`](m365-copilot/) — Microsoft 365 Copilot, SharePoint Agents und Copilot Studio.

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
