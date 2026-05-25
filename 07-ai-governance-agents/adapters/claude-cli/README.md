<!-- kso:product-relevance
repo-scope: product
classification: tool-adapter
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Claude CLI Adapter

## Zweck

Dieser Adapter beschreibt, wie krisensicherOS mit Claude Code CLI genutzt wird, ohne Fachlogik in Claude-spezifische Konfiguration zu verlagern.

Kanonische Inhalte bleiben im Repo:

- `AGENTS.md` — repo-weite Arbeitsregeln,
- `CLAUDE.md` — Claude-kompatible Projektinstruktionen,
- `07-ai-governance-agents/agents/public/*.md` — öffentliche Agentenrollen,
- `07-ai-governance-agents/agents/manifest.yaml` — Rollen-/Routingmanifest,
- `07-ai-governance-agents/skills/*/SKILL.md` — wiederholbare Skills,
- `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md` — Qualitäts- und Sicherheitsgates.

## Recherchebasis

Stand: 2026-05-25.

Geprüfte öffentliche Herstellerdokumentation:

- Claude Code Docs: Commands — u. a. `/init`, `/memory`, `/mcp`, `/agents`, `/permissions`, `/plan`, `/diff`, `/code-review`, `/security-review`.
- Claude Code Docs: Settings — Scope-Modell mit Managed, User, Project und Local; Projektkonfiguration in `.claude/`; `CLAUDE.md` bzw. `.claude/CLAUDE.md`; lokale Overrides in `CLAUDE.local.md`.

## Adapter-Prinzip

Claude CLI darf krisensicherOS nicht neu erfinden. Der Adapter übersetzt nur:

- welche Dateien Claude zuerst lesen soll,
- welche Claude-Kommandos typischerweise nützlich sind,
- welche Konfiguration committed werden darf,
- welche lokalen Einstellungen nicht ins Produktrepo gehören,
- welche Qualitätsgates vor Abschluss berichtet werden müssen.

## Empfohlener Start in Claude CLI

Im lokalen Repo:

```bash
claude
```

Erster lesender Prompt:

```text
Arbeite zunächst nur lesend.
Lies AGENTS.md, CLAUDE.md, README.md, 07-ai-governance-agents/agents/manifest.yaml und 06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md.
Lies keine Dateien außerhalb dieses Repo-Ordners.
Führe keine Schreiboperationen, Shell-Kommandos mit Seiteneffekt, Git-Aktionen, Pushes, Releases oder externen Nachrichten aus.
Gib mir danach:
1. Welche krisensicherOS-Regeln gelten.
2. Welche Agentenrolle für meinen Auftrag passt.
3. Welche Human Gates zu beachten sind.
4. Welche Qualitätsgates vor Änderungen erfüllt sein müssen.
```

## Sinnvolle Claude-Kommandos

| Situation | Claude-Kommando | krisensicherOS-Regel |
| --- | --- | --- |
| Erstinitialisierung | `/init` | Nur nutzen, wenn bestehende `CLAUDE.md` nicht überschrieben wird. |
| Projektmemory prüfen | `/memory` | Keine privaten Workspace- oder Kundendaten in geteilte Projektmemory schreiben. |
| Große Änderung planen | `/plan` | Vor jeder mehrdateiigen Änderung Pflicht. |
| Agenten/Subagents prüfen | `/agents` | Fachlogik bleibt in `07-ai-governance-agents/agents/public/*.md`, nicht nur in Claude-Konfiguration. |
| MCP konfigurieren | `/mcp` | Nur freigegebene Server, keine Secrets in Repo-Dateien. |
| Berechtigungen setzen | `/permissions` | Schreib-, Shell- und Netzwerkrechte restriktiv halten. |
| Diff prüfen | `/diff` | Vor Commit/Freigabe immer prüfen. |
| Review durchführen | `/code-review` oder `/security-review` | Ergänzt, ersetzt aber nicht Human Review. |

## Projektkonfiguration

Wenn Claude-Projektkonfiguration genutzt wird:

- `.claude/settings.json` darf nur public-safe, teamfähige Einstellungen enthalten.
- `.claude/settings.local.json` bleibt lokal und darf nicht committed werden.
- `CLAUDE.local.md` bleibt lokal und darf keine Produktlogik ersetzen.
- MCP-Server, Hooks oder Plugins werden nur dokumentiert, wenn sie für das Produktrepo portabel und freigegeben sind.

## Empfohlene Claude-Arbeitssequenz

1. Read-only-Erstlauf.
2. Passende Rolle aus `07-ai-governance-agents/agents/public/role-model.md` wählen.
3. Relevantes Profil vollständig lesen.
4. Bei wiederholbarer Aufgabe passenden Skill aus `07-ai-governance-agents/skills/` lesen.
5. Plan erstellen.
6. Änderung minimal durchführen.
7. `git diff --check` und passende Repo-QS ausführen.
8. Diff und Qualitätsgates berichten.
9. Kein Commit, Push, Tag oder Release ohne ausdrückliche menschliche Freigabe.

## Änderungs-Prompt

```text
Aufgabe: <konkrete Änderung>

Nutze krisensicherOS mit Claude CLI.
Lies zuerst AGENTS.md, CLAUDE.md, 07-ai-governance-agents/agents/public/role-model.md und das passende Profil unter 07-ai-governance-agents/agents/public/.
Wenn ein Skill passt, lies zusätzlich 07-ai-governance-agents/skills/<skill>/SKILL.md.

Regeln:
- Zeige zuerst den Plan.
- Ändere nur notwendige Dateien.
- Keine Rechtsberatung, Datenschutzberatung, Konformitäts-, Zertifizierungs- oder Sicherheitszusage.
- Keine echten Personen-, Kunden-, Vertrags-, Incident-, System- oder Secret-Daten.
- Keine lizenzpflichtigen Normtexte reproduzieren.
- Markiere Annahmen, Lücken, Evidenzbedarf und Human Gates.
- Prüfe Produktrelevanz-Tags, wenn Dateien neu angelegt oder geändert werden.
- Kein Commit, Push, Tag, Release oder externer Versand ohne explizite Freigabe.

Output:
1. Plan.
2. Geänderte Dateien.
3. QS-Ergebnis.
4. Human Gates.
5. Offene Punkte.
```

## Stop-Punkte

Stoppen und menschliche Freigabe einholen bei:

- fehlender KI-Freigabe,
- unklarer Datenklasse,
- echten Organisations-, Kunden- oder Personendaten,
- Secrets oder Zugangsdaten,
- lizenzpflichtigen Normtexten,
- Rechts- oder Datenschutzbewertung,
- Risikoakzeptanz oder Managemententscheidung,
- Veröffentlichung, Push, Tag, Release oder externer Kommunikation,
- Claude-Konfiguration mit nicht-portabler Fachlogik.

## Adapter-Qualitätsgate

Vor Abschluss berichtet Claude CLI:

```text
Adapter-Gate:
- Source-of-Truth-Dateien gelesen: ja/nein
- Fachlogik im Repo statt Adapter: ja/nein
- Produktrelevanz-Tags geprüft: ja/nein
- Public-Safety geprüft: ja/nein
- Claim-Safety geprüft: ja/nein
- Human Gates markiert: ja/nein
- Nicht ausgeführt: Push/Release/externer Versand
```
