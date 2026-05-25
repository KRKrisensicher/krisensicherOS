<!-- kso:product-relevance
repo-scope: product
classification: tool-adapter
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# AGENTS.md — Codex Adapter für krisensicherOS

## Projekt

krisensicherOS ist ein offenes deutschsprachiges Produktrepo für KI-unterstützte Security Governance. Ziel ist Governance-Fähigkeit statt dokumentengetriebener Compliance.

## Agentenprofile

Öffentliche Agentenprofile liegen in `agents/public/*.md`. Lies das relevante Profil vollständig, bevor du ein Artefakt erstellst oder überarbeitest.

Das Manifest liegt in `agents/manifest.yaml`.

## Grundregeln

- krisensicherOS setzt freigegebene KI-Nutzung voraus.
- Kein Artefakt ohne Betriebslogik.
- Keine Compliance-Floskeln.
- Keine Scheinsicherheit.
- Keine Rechtsberatung.
- Keine Datenschutzberatung.
- Keine Zertifizierungs- oder Konformitätsgarantie.
- Verantwortung bleibt menschlich.
- Agenten entlasten, strukturieren und prüfen; sie entscheiden nicht stellvertretend.
- Jede Empfehlung enthält Beobachtung, Risiko/Chance, Empfehlung und nächsten Schritt.

## Qualitätscheck vor Abschluss

Prüfe:

1. Ist klar, wer das Artefakt nutzt?
2. Ist klar, wann es genutzt wird?
3. Ist klar, welche Entscheidung oder Routine unterstützt wird?
4. Sind Grenzen und Annahmen sichtbar?
5. Sind Datenklasse, KI-Freigabe und Human Gates sichtbar?
6. Gibt es keine privaten Daten, Tokens oder echten Kundendaten?
7. Sind NIS2-/ISMS-Aussagen als Governance-Hilfe formuliert, nicht als Rechts- oder Zertifizierungszusage?
