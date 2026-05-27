
# Öffentliche Zielrepo-Agenten

Dieser Ordner enthält die Agentenprofile, die spätere Nutzer von krisensicherOS für ihr eigenes Compliance- und Security-Governance-System übernehmen können.

## Zweck

Die Zielrepo-Agenten helfen Organisationen, ein eigenes agentisches Arbeitsmodell für NIS2, ISMS, BCMS, Compliance-Register, Evidenzarbeit und Management Reviews aufzubauen.

Sie sind keine Berater-Ersatzbehauptung und keine Verantwortungsmaschine. Sie strukturieren Arbeit, bereiten Entscheidungen vor, prüfen Artefakte und machen offene Punkte sichtbar.

## Rollenmodell

Das Rollenmodell steht in:

- [`role-model.md`](role-model.md)
- [`anwender-routing.md`](anwender-routing.md) — reduzierte Einstiegsauswahl mit maximal acht Startagenten.

## Profilstandard

Alle öffentlichen Agentenprofile folgen dem krisensicherOS-Profilstandard:

- klares Mandat,
- klare Nicht-Zuständigkeit,
- Eingangsdaten,
- Standard-Workflow,
- Deliverables,
- Erfolgskriterien,
- Qualitätsgates,
- Anti-Patterns,
- Handoff-Protokoll,
- Definition of Done.

## Agentenfamilien

### 1. Steuerung und Operating System

- `compliance-operating-system-lead` — orchestriert den Aufbau des nutzereigenen Compliance- und Security-Governance-Systems.
- `agent-quality-and-safety-reviewer` — prüft Agentenergebnisse auf Grenzen, Scheinsicherheit, Quellen- und Freigaberisiken.

### 2. Quellen, Register und Anforderungen

- `regulatory-source-mapper` — ordnet öffentliche Rechtsquellen und regulatorische Referenzen ein.
- `compliance-register-curator` — pflegt die Struktur für nutzereigene Vorgaben wie Normen, Verträge und interne Policies.
- `third-party-requirements-analyst` — übersetzt Kunden-/Lieferantenanforderungen in prüfbare Governance-Arbeit.
- `data-protection-interface-reviewer` — markiert Datenschutzschnittstellen, ohne Datenschutzberatung zu behaupten.

### 3. Managementsysteme und Governance-Routinen

- `security-governance-architect` — baut Rollen, Routinen, Entscheidungen und Evidenzflüsse.
- `isms-operating-model-designer` — entwirft ein Minimum Viable ISMS als Betriebsmodell.
- `bcms-readiness-designer` — strukturiert BCMS-/Krisenfähigkeitsarbeit.
- `risk-and-obligation-prioritizer` — priorisiert Anforderungen, Risiken und Maßnahmen.

### 4. Evidenz, Dokumente und Reviews

- `control-evidence-architect` — verbindet Controls, Routinen und Nachweise.
- `evidence-pack-reviewer` — prüft Evidence Packs auf Vollständigkeit, Qualität und Grenzen.
- `policy-and-controls-drafter` — erstellt Entwürfe für Policies/Controls als interne Arbeitsgrundlage.
- `management-review-facilitator` — bereitet Managemententscheidungen und Reviews vor.

### 5. Readiness und Übungen

- `nis2-readiness-analyst` — bereitet NIS2-Gap- und Readiness-Arbeit vor.
- `incident-readiness-coach` — strukturiert Incident-Eskalation und Übungslogik.

## Handoff-Grundregel

Kein Agent löst alles allein. Wenn ein Ergebnis fachliche, rechtliche, operative oder Quellen-Grenzen berührt, wird intern an den zuständigen Agenten übergeben.

Fragen an Menschen entstehen erst, wenn Agenten den Konflikt mit vorhandenen Repo-Regeln, Quellen, Templates und Qualitätsgates nicht auflösen können.
