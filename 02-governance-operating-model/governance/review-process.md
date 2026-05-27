
# Reviewprozess

## Zweck

Der Reviewprozess hilft zu prüfen, ob krisensicherOS-Artefakte public-safe, betreibbar, toolneutral und entscheidungsorientiert bleiben.

## Review-Prinzipien

1. Betriebslogik vor Dokument: Jedes Artefakt braucht Owner, Trigger, Output, Evidenz und Review.
2. Human-in-the-loop: Rechtliche Bewertung, Datenschutzbewertung, Risikoakzeptanz, Managemententscheidung und externe Kommunikation bleiben bei den zuständigen Menschen.
3. Public-safe by default: Öffentliche Artefakte enthalten keine echten Kunden-, Personen-, Vertrags-, Incident-, System- oder privaten Workspace-Daten.
4. Quellenklarheit: Lizenzpflichtige Normen und vertrauliche Inhalte werden nur als Metadaten, Referenzen oder eigene Zusammenfassungen geführt.
5. Portabilität: Fachlogik lebt in kanonischen Artefakten, nicht in Tooladaptern.

## Review-Stufen

### R1 — Selbstcheck durch Ersteller

Vor Übergabe prüfen:

- Zweck und Scope klar?
- Nutzerrolle und Trigger benannt?
- Inputs, Ablauf, Outputs und Evidenz sichtbar?
- Grenzen und Stop-Punkte enthalten?
- Keine unzulässigen Claims?
- Keine echten oder vertraulichen Daten?

### R2 — Fachreview

Passender Review durch Fachrolle oder Agentenprofil:

- Agentenprofile: `agent-quality-and-safety-reviewer`
- Governance/ISMS/NIS2: `security-governance-architect` oder `nis2-readiness-analyst`
- BCMS/Incident: `bcms-readiness-designer` oder `incident-readiness-coach`
- Evidenz: `control-evidence-architect` oder `evidence-pack-reviewer`
- Managemententscheidungen: `management-review-facilitator`

### R3 — Quality Gate Review

Gegen `07-ai-governance-agents/evals/quality-gates.md` prüfen:

- U1 Public-Safe Gate
- U2 Claim-Safety Gate
- U3 Betriebslogik-Gate
- U4 Empowerment-Gate
- U5 Workload-Gate
- U6 Portabilitäts-Gate
- passendes artefaktspezifisches Gate

### R4 — Release Review

Vor Release Candidate zusätzlich prüfen:

- README und Navigation konsistent?
- Queue ohne offene veröffentlichungsrelevante Ready-Tasks?
- Blocker dokumentiert?
- Lizenz vorhanden?
- keine privaten Runtime-/Workspace-Inhalte?
- keine Secrets oder personenbezogenen Daten?
- keine Normtexte oder vertraulichen Inhalte?
- keine Veröffentlichung ohne Freigabe?

## Review-Nachweis

```text
Artefakt:
Reviewer:
Datum:
Geprüfte Gates:
Pass:
Pass with notes:
Stop-Punkte:
Korrekturen:
Menschliche Prüfung erforderlich:
Ergebnis:
```

## Stop-Punkte

Review stoppt bei:

- Rechtsberatung oder Datenschutzberatung,
- Managemententscheidung durch Agenten,
- Risikoakzeptanz ohne verantwortliche Rolle,
- Konformitäts-, Zertifizierungs- oder Sicherheitszusage,
- echten oder vertraulichen Daten,
- lizenzpflichtigen Normtexten,
- externer Veröffentlichung ohne Freigabe,
- Lizenz-/Disclaimer-Änderung ohne Freigabe.

## Definition of Done

Ein Artefakt ist reviewfähig, wenn:

- alle relevanten Qualitätsgates bestanden sind oder Notes dokumentiert sind,
- Stop-Punkte entweder ausgeschlossen oder als Blocker markiert sind,
- Human-Review-Punkte sichtbar sind,
- Handoffs klar sind,
- Änderungen kohärent committed werden können.
