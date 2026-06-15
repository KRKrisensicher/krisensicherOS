
# CLAUDE.md — krisensicherOS

Hinweise für Claude Code und vergleichbare Coding-Agenten in diesem Repository.

## Auftrag

Arbeite an krisensicherOS als offenem, portablen Betriebsrepo für Security Governance, NIS2-Readiness, ISMS, BCMS, Krisenfähigkeit und AI-assisted Governance.

Das Repo baut keine Governance für eine konkrete Organisation. Es liefert Bausteine, mit denen Organisationen ihre eigene Governance betreiben können.

## Arbeitsregeln

- Schreibe public-safe Artefakte.
- Nutze fiktive Beispiele.
- Keine echten Kundendaten, personenbezogenen Daten oder privaten Workspace-Details.
- Keine Rechtsberatung, Datenschutzberatung, Zertifizierungs- oder Konformitätsgarantien.
- Keine ISO-Normtexte oder vertraulichen Vertragsinhalte reproduzieren.
- Lizenzpflichtige Quellen nur als Metadaten, Verweise, Mappings oder eigene Zusammenfassungen behandeln.
- Betriebslogik vor Dokumentenlogik: jedes Artefakt braucht Zweck, Nutzer, Trigger, Input, Ablauf, Output, Evidenz und Grenzen.

## Wichtige Pfade

- `README.md` — Produktpositionierung und Orientierung
- `10-reference/knowledge/` — feste öffentliche Referenzquellen
- `10-reference/compliance-register/` — Struktur für nutzereigene Vorgaben
- `07-ai-governance-agents/agents/` — kanonische Agentenprofile und Manifest
- `07-ai-governance-agents/agents/public/` — öffentliche Zielrepo-Agenten für Nutzerorganisationen
- `07-ai-governance-agents/skills/` — wiederverwendbare AgentSkills
- `08-templates-playbooks/templates/` — nutzbare Arbeitsvorlagen
- `08-templates-playbooks/workflows/` — agentische Ablaufmodelle
- `07-ai-governance-agents/evals/` — Qualitäts- und Sicherheitsgates
- `10-reference/docs/standards/` — Profil-, Skill- und Artefaktstandards

## Qualitätscheck vor Abschluss

Mindestens prüfen:

1. Public-safe: keine privaten Details, echten Daten oder Secrets.
2. Claim-safe: keine Rechts-, Datenschutz-, Konformitäts- oder Zertifizierungsaussagen.
3. Operational: Rollen, Trigger, Inputs, Outputs, Evidenz und Reviewpunkte klar.
4. Empowerment-first: Nutzerorganisation bleibt entscheidungs- und lernfähig.
5. Portabilität: keine tool-spezifische Fachlogik im kanonischen Artefakt.

## Commit-Hinweise

Kohärente Änderungen dürfen lokal nur committed werden, wenn der Auftrag oder eine menschliche Freigabe das ausdrücklich erlaubt. Kein Push, keine Veröffentlichung, keine Lizenz-/Disclaimer-Änderung und kein externer Versand ohne ausdrückliche Freigabe.
