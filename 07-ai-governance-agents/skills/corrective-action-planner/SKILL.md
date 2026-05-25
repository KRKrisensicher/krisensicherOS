---
name: corrective-action-planner
version: 1.0.0
description: "Übersetzt Findings und Gaps in Maßnahmen mit Ursache, Owner, Frist, Evidenz und Review."
category: evidence
inputs:
  - scope
  - requirements-or-findings
  - existing-evidence
  - owners-and-constraints
outputs:
  - corrective-action-plan
  - action-backlog
  - decision-log-entry
requires_human_review: true
---

<!-- kso:product-relevance
repo-scope: product
classification: agent-skill
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->


# corrective-action-planner

## Zweck

Dieser Skill strukturiert Maßnahmen aus Findings oder Gaps mit Ursache, Zielzustand, Owner, Evidenz und Reviewpunkt.

Der Skill erzeugt keine Rechtsberatung, keine Datenschutzberatung, keine Audit-, Konformitäts- oder Zertifizierungszusage und keine Managemententscheidung.

## Wann verwenden

Nutze den Skill, wenn aus Auditfeststellungen, Dokumentengaps, Control-Test-Ergebnissen oder Managemententscheidungen umsetzbare Maßnahmen entstehen müssen.

Typische Auslöser:

- interne Audits oder Self-Assessments,
- NIS2-/ISMS-/BCMS-Gap-Arbeit,
- Evidence-Pack- oder Management-Review-Vorbereitung,
- Findings, Abweichungen, Beobachtungen oder Maßnahmenreviews,
- neue oder geänderte Anforderungen aus Registereinträgen.

## Wann nicht verwenden

Nicht verwenden für:

- verbindliche Rechts-, Norm- oder Vertragsauslegung,
- Datenschutzbewertung,
- externe Audit-, Prüfungs- oder Zertifizierungszusage,
- Risikoakzeptanz oder Managemententscheidung,
- Live-Incident-Steuerung,
- Reproduktion lizenzpflichtiger Normtexte,
- öffentliche Verarbeitung vertraulicher oder personenbezogener Inhalte.

## Eingangsdaten

Pflicht:

- **Scope:** Prozess, Control, Auditbereich, Finding oder Maßnahme.
- **Kriterien:** Anforderungen, Registereinträge, Control-Referenzen oder eigene Zusammenfassungen.
- **Ist-Stand:** vorhandene Evidenz, offene Lücken, Findings oder Maßnahmenstatus.
- **Owner-/Fristinformationen:** soweit bekannt.

Optional:

- Bewertungsskala oder Auditmethodik,
- Risikokontext,
- bestehende Evidence Packs,
- Managemententscheidungen oder Decision Logs,
- Stichproben- oder Prüfmethodenvorgaben.

Annahmen:

- Fehlende Evidenz wird als Lücke markiert.
- Unklare Zuständigkeiten werden nicht erfunden, sondern als Klärungsbedarf ausgewiesen.

## Voraussetzungen

Hilfreiche Artefakte:

- `templates/corrective-action-plan.md`
- `templates/decision-log.md`
- `templates/audit-finding-report.md`
- `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md`
- `02-governance-operating-model/governance/review-process.md`

Hilfreiche Rollen:

- Fach- oder Prozessowner,
- ISB/CISO oder GRC-Verantwortliche,
- interne Revision oder Auditverantwortliche,
- Managementrolle bei Risiko- oder Ressourcenentscheidungen.

## Ablauf

1. **Scope und Kriterium festlegen**  
   Definiere, welcher Prozess, Control, Finding- oder Maßnahmenbereich betrachtet wird und welche Kriterien gelten.

2. **Ist-Stand und Evidenz trennen**  
   Unterscheide bestätigte Evidenz, Behauptungen, Annahmen, offene Punkte und fehlende Nachweise.

3. **Arbeitslogik ableiten**  
   Übersetze Kriterien in konkrete Requests, Tests, Maßnahmen oder Reviewfragen. Halte Owner, Frist, Qualität und Eskalation fest.

4. **Risiko- und Entscheidungsbezug markieren**  
   Zeige, welche Lücken operative Bedeutung haben und wo Management-, Risiko- oder Ressourcenentscheidungen nötig sind.

5. **Output-Artefakt ausfüllen**  
   Erzeuge das passende Template mit nachvollziehbaren Feldern, nicht nur Freitext.

6. **Handoffs vorbereiten**  
   Weise offene Punkte an Owner, Auditverantwortliche, Evidence Reviewer oder Management Review weiter.

7. **Verification durchführen**  
   Prüfe Public-Safety, Claim-Safety, Quellen-/Evidenzbezug, Betriebslogik, Workload, Human Gates und Handoffs.

## Output-Artefakte

Je nach Auftrag erzeugt der Skill:

- corrective-action-plan
- action-backlog
- decision-log-entry
- offene Fragen und Annahmen,
- Handoff an Owner, Audit oder Management Review,
- Verification-Notiz.

## Human-in-the-loop

Menschliche Prüfung ist erforderlich für:

- rechtliche, normative oder vertragliche Auslegung,
- Datenschutzbewertung,
- finale Auditbewertung oder Finding-Klassifikation,
- Maßnahmenfreigabe und Ressourcenentscheidung,
- Risikoakzeptanz,
- Schließung oder Wiedereröffnung von Findings,
- externe Kommunikation.

## Verification

```text
Verification:
- Public-Safety: pass / notes / stop
- Claim-Safety: pass / notes / stop
- Kriterienbezug: pass / notes / stop
- Evidenzbezug: pass / notes / stop
- Betriebslogik: pass / notes / stop
- Workload: pass / notes / stop
- Human Review: pass / notes / stop
- Handoffs: pass / notes / stop
- Ergebnis: pass / pass with notes / stop
```

Mindestfragen:

- Sind Scope, Kriterien, Owner und Zieloutput klar?
- Sind Quellen nur zulässig referenziert oder zusammengefasst?
- Sind Evidenz, Annahmen und Lücken sauber getrennt?
- Ist sichtbar, wer handeln, prüfen oder entscheiden muss?
- Wurden keine Garantien, finalen Konformitätsaussagen oder Managemententscheidungen behauptet?

## Qualitätsgates

Anzuwenden aus `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md`:

- U1 Public-Safe Gate,
- U2 Claim-Safety Gate,
- U3 Betriebslogik-Gate,
- U4 Empowerment-Gate,
- U5 Workload-Gate,
- U6 Portabilitäts-Gate,
- A2 Skill-Gate,
- A3 Template-Gate,
- A8 Quellen-/Register-Gate.

## Handoffs

Typische Handoffs:

- an `internal-audit-planner` für Auditplanung,
- an `control-evidence-architect` für Evidenz- und Control-Mapping,
- an `audit-finding-reviewer` für Findings,
- an `evidence-pack-reviewer` für Evidence-Pack-Prüfung,
- an `management-review-facilitator` für Entscheidungs- und Reviewpunkte,
- an `agent-quality-and-safety-reviewer` für Claim-, Vertraulichkeits- und Workload-Prüfung.

## Grenzen und rote Linien

Dieser Skill leistet keine Rechtsberatung, keine Datenschutzberatung, keine Zertifizierungs-, Audit- oder Konformitätszusage und keine Managemententscheidung.

Er darf keine vertraulichen Inhalte, personenbezogenen Daten, echten Kundendaten oder lizenzpflichtigen Normtexte in öffentliche Artefakte übernehmen.

Er darf keine Evidenz erfinden, keine Lücken glätten und keine Maßnahmen als wirksam bestätigen, ohne Reviewgrundlage und menschliche Freigabe zu markieren.

## Beispiel

Aus einer fiktiven Finding-Notiz zu fehlenden Ownern entstehen Ursachenhypothese, Sofortmaßnahme, strukturelle Maßnahme, Owner, Frist, Evidenz und Management-Handoff.

Guter Output:

- Kriterium und Scope sind nachvollziehbar.
- Evidenzbedarf, Test, Maßnahme oder Reviewfrage ist konkret.
- Owner, Frist, Qualität und Handoff sind sichtbar.
- Annahmen und Human Gates sind markiert.

Schlechter Output:

- „Alles ist erledigt; das Finding kann ohne weitere Prüfung geschlossen werden.“

Warum schlecht:

- Das erzeugt Scheinsicherheit, ersetzt menschliche Bewertung und behauptet eine unzulässige Zusage.

## Definition of Done

Der Skill ist abgeschlossen, wenn:

- Scope, Kriterien und Ist-Stand dokumentiert sind,
- Evidenz, Annahmen und Lücken getrennt sind,
- Output-Artefakt und Handoffs vorliegen,
- Human-Review- und Entscheidungspunkte markiert sind,
- Verification dokumentiert ist,
- nächste Schritte für Owner, Audit oder Management Review klar sind.
