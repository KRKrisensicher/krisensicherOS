<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Codex CLI Adapter

Dieser Adapter beschreibt, wie krisensicherOS mit Codex CLI genutzt werden soll.

## Grundidee

Codex CLI liest vor allem klare Repo-Instruktionen und arbeitet gut mit präzisen Markdown-Profilen, überprüfbaren Arbeitsregeln und konkreten Qualitätsgates.

Der wichtigste Nutzungspfad ist eine **freigegebene lokale IDE oder ein lokaler Repo-Workspace**: Das Repository liegt lokal vor, Codex arbeitet im Projektkontext, und der Anwender klärt mit Codex Schritt für Schritt Scope, Datenklasse, KI-Freigabe, Rollen, Human Gates und den nächsten sinnvollen Governance-Arbeitsschritt.

Codex soll dabei nicht nur Dateien bearbeiten. Es soll als Arbeitsbegleiter helfen, Managementsystemarbeit in Fragen, Gespräche, Nachweise, Reviews und Entscheidungen zu übersetzen.

## Nutzung mit lokaler IDE

1. Klone oder öffne dieses Repository in einer freigegebenen lokalen Arbeitsumgebung, z. B. VS Code, Cursor, JetBrains oder einer anderen IDE mit Codex-Integration.
2. Stelle sicher, dass die lokale Umgebung für die geplante Datenklasse freigegeben ist. Keine echten Personen-, Kunden-, Vertrags-, Incident-, Secret- oder lizenzpflichtigen Norminhalte ohne passende Freigabe einbringen.
3. Öffne Codex im Repository-Kontext und starte mit einem konkreten Ziel, z. B.: „Hilf mir, einen NIS2-Minimalstart für unsere Organisation vorzubereiten.“
4. Lass Codex zuerst die Klärungsfragen stellen: Scope, Datenklasse, KI-Freigabe, Rollen, vorhandene Nachweise, Human Gates und gewünschtes Ergebnis.
5. Lass Codex anschließend die passenden Profile, Skills, Templates oder Playbooks aus dem Repo auswählen und ein kleines nutzbares Artefakt erzeugen.
6. Prüfe Änderungen in der IDE per Diff, Review und Qualitätsgate, bevor du sie übernimmst.

## Repo-Nutzung

- Public-safe Repo-Instruktionen gehören in `AGENTS.md`.
- Agentenrollen liegen kanonisch unter `07-ai-governance-agents/agents/public/*.md`.
- Das Rollenmanifest liegt unter `07-ai-governance-agents/agents/manifest.yaml`.
- Skills liegen unter `07-ai-governance-agents/skills/<skill-name>/SKILL.md`.
- Workflows liegen unter `workflows/*.yaml`.

## Arbeitsregel

Wenn Codex einen krisensicherOS-Agenten simuliert oder nutzt:

1. Passendes Profil in `07-ai-governance-agents/agents/public/*.md` lesen.
2. Eingangsdaten, Datenklasse, KI-Freigabe und fehlende Informationen markieren.
3. Mit dem Anwender offene Fragen klären, statt Annahmen über Organisation, Rechtslage oder Risikoakzeptanz zu erfinden.
4. Standard-Workflow des Profils befolgen.
5. Ergebnis im definierten Output-Format liefern.
6. Qualitätsgates prüfen.
7. Grenzen, Human Gates und Reviewbedarf sichtbar machen.

## Nicht tun

- Keine Rechtsberatung behaupten.
- Keine Zertifizierungsgarantie ableiten.
- Keine privaten OpenClaw-Workspace-Dateien veröffentlichen.
- Keine Workrepo-Artefakte als Produktinhalt behandeln.
- Keine Vault-Dateien als operative Wahrheit behandeln.
