<!-- kso:product-relevance
repo-scope: product
classification: tool-adapter
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# CLAUDE.md — Claude CLI Adapter für krisensicherOS

## Auftrag

Arbeite an krisensicherOS als KI-unterstütztem Produktrepo für Security Governance. Nutze Claude CLI als Ausführungsoberfläche, nicht als neue fachliche Quelle.

## Source of Truth

Lies bei relevanter Arbeit zuerst:

1. `AGENTS.md`
2. `CLAUDE.md`
3. `README.md`
4. `agents/public/role-model.md`
5. passendes Profil unter `agents/public/`
6. ggf. passenden Skill unter `skills/<skill>/SKILL.md`
7. `evals/quality-gates.md`
8. `governance/product-relevance-process.md`, wenn Dateien angelegt oder geändert werden

## Arbeitsregeln

- krisensicherOS setzt freigegebene KI-Nutzung voraus.
- Vor mehrdateiigen Änderungen Plan zeigen.
- Nur notwendige Dateien ändern.
- Fachlogik bleibt in Repo-Artefakten, nicht in Claude-spezifischer Konfiguration.
- Neue oder geänderte Dateien brauchen gültigen `kso:product-relevance`-Tag.
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
