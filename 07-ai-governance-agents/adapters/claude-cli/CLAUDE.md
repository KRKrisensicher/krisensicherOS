
# CLAUDE.md — Claude CLI Adapter für krisensicherOS

## Auftrag

Arbeite an krisensicherOS als KI-unterstütztem Produktrepo für Security Governance. Nutze Claude CLI als Ausführungsoberfläche, nicht als neue fachliche Quelle.

## Source of Truth

Lies bei relevanter Arbeit zuerst:

1. `AGENTS.md`
2. `CLAUDE.md`
3. `README.md`
4. `07-ai-governance-agents/agents/public/role-model.md`
5. passendes Profil unter `07-ai-governance-agents/agents/public/`
6. ggf. passenden Skill unter `07-ai-governance-agents/skills/<skill>/SKILL.md`
7. `07-ai-governance-agents/evals/quality-gates.md`
8. `02-governance-operating-model/governance/quality-rules.md`, wenn Inhalte fachlich erweitert werden

## Arbeitsregeln

- krisensicherOS setzt freigegebene KI-Nutzung voraus.
- Vor mehrdateiigen Änderungen Plan zeigen.
- Nur notwendige Dateien ändern.
- Fachlogik bleibt in Repo-Artefakten, nicht in Claude-spezifischer Konfiguration.
- Neue oder geänderte Inhalte müssen public-safe, claim-safe und für externe Nutzer nachvollziehbar sein.
- Kein Commit, Push, Tag, Release oder externer Versand ohne explizite Freigabe.

## Grenzen

Keine:

- Rechtsberatung,
- Datenschutzberatung,
- Konformitäts-, Zertifizierungs- oder Sicherheitszusage,
- Managemententscheidung,
- Risikoakzeptanz,
- Verarbeitung echter Personen-, Kunden-, Vertrags-, Incident-, System- oder Secret-Daten ohne Freigabe,
- Reproduktion lizenzpflichtiger Normtexte.

## Abschlussbericht

Berichte am Ende:

1. Geänderte Dateien.
2. Welche Source-of-Truth-Dateien gelesen wurden.
3. Welche Qualitätsgates geprüft wurden.
4. Welche Human Gates offen bleiben.
5. Ob Commit/Push/Release unterlassen oder explizit freigegeben wurde.
