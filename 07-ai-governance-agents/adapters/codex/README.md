
# Codex CLI Adapter

Dieser Adapter beschreibt, wie krisensicherOS mit Codex CLI genutzt werden soll.

## Grundidee

Codex CLI liest vor allem klare Repo-Instruktionen und arbeitet gut mit präzisen Markdown-Profilen, überprüfbaren Arbeitsregeln und konkreten Qualitätsgates.

## Nutzung

- Public-safe Repo-Instruktionen gehören in `AGENTS.md`.
- Agentenrollen liegen kanonisch unter `agents/public/*.md`.
- Das Rollenmanifest liegt unter `agents/manifest.yaml`.
- Skills liegen unter `skills/<skill-name>/SKILL.md`.
- Workflows werden später unter `workflows/*.yaml` ergänzt.

## Arbeitsregel

Wenn Codex einen krisensicherOS-Agenten simuliert oder nutzt:

1. Passendes Profil in `agents/public/*.md` lesen.
2. Eingangsdaten und fehlende Informationen markieren.
3. Standard-Workflow des Profils befolgen.
4. Ergebnis im definierten Output-Format liefern.
5. Qualitätsgates prüfen.
6. Grenzen/Disclaimer sichtbar machen.

## Nicht tun

- Keine Rechtsberatung behaupten.
- Keine Zertifizierungsgarantie ableiten.
- Keine privaten OpenClaw-Workspace-Dateien veröffentlichen.
- Keine Workrepo-Artefakte als Produktinhalt behandeln.
- Keine Vault-Dateien als operative Wahrheit behandeln.
