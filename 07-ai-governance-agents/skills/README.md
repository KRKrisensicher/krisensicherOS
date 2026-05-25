<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Skills

Skills sind wiederholbare Arbeitsabläufe für krisensicherOS. Sie übersetzen Governance-Aufgaben in konkrete Schritte mit Inputs, Outputs, Verification, Handoffs und menschlichen Freigabepunkten.

Sie sind keine Wissensablagen, keine bloßen Prompts und kein Ersatz für verantwortliche Rollen.

## Standard

Alle Skills folgen [`07-ai-governance-agents/standards/skill-standard-v1.0.md`](../standards/skill-standard-v1.0.md).

Pfadregel:

```text
07-ai-governance-agents/skills/<skill-name>/SKILL.md
```

## Grundsätze

Ein guter Skill:

- löst eine klar abgegrenzte Governance-Aufgabe,
- nennt benötigte Eingangsdaten,
- führt durch einen wiederholbaren Ablauf,
- erzeugt konkrete Output-Artefakte,
- enthält Verification und Qualitätsgates,
- benennt Human-in-the-loop-Punkte,
- vermeidet Rechts-, Datenschutz-, Zertifizierungs- und Konformitätsclaims,
- nutzt nur fiktive Beispiele und public-safe Inhalte.

## Startliste v1.0

### `governance-operating-model`

Übersetzt Anforderungen in Rollen, Routinen, Entscheidungswege, Eskalationen und Evidenzflüsse.

### `nis2-gap-assessment`

Strukturiert NIS2-Readiness-Arbeit mit Prüffragen, Gaps, Evidenzbedarf, Maßnahmen und Managemententscheidungen — ohne Rechts- oder Konformitätsversprechen.

### `minimum-viable-isms`

Entwirft ein Minimum Viable ISMS als Scope-, Risiko-, Control-, Evidenz- und Review-Routine.

### `evidence-pack-review`

Prüft Evidence Packs auf Vollständigkeit, Traceability, Annahmen, Lücken, Qualität und Entscheidungsfähigkeit.

### `management-review-prep`

Bereitet Management Reviews mit Agenda, Entscheidungsfragen, Risiken, Optionen, Maßnahmen und Follow-up vor.

### `incident-escalation-playbook`

Erstellt Incident-Eskalationslogik mit Triggern, Rollen, Kommunikationspunkten, Entscheidungen und Nachbereitung.

### `tabletop-exercise-design`

Entwickelt Tabletop-Übungen mit Szenario, Lernzielen, Rollen, Injects, Beobachtungspunkten und After-Action-Review.

### `risk-prioritization`

Priorisiert Risiken, Gaps und Maßnahmen nach Wirkung, Dringlichkeit, Evidenzbedarf, Aufwand und Managementrelevanz.

### `isms-risk-analysis`

Führt dialogisch durch ISMS-Risikoanalysen: Risiko als Schwachstelle + Asset + Bedrohung beschreiben, aktuelle Maßnahmenlage erheben, Brutto bewerten, Strategie vorbereiten, Maßnahmen und SoA-Mapping ableiten, Netto-/Restrisiko bewerten und Reporting erzeugen.

### `bcms-readiness-starter`

Startet BCMS-Readiness mit kritischen Prozessen, Abhängigkeiten, Impact-Annahmen, Wiederanlauf-Routinen, Evidenz und Managemententscheidungen.

### `board-briefing-generator`

Erzeugt entscheidungsorientierte Board-/Management-Briefs aus geprüften Risiken, Evidenz, Optionen und offenen Entscheidungen.

### `audit-questionnaire-builder`

Erstellt interne Audit-Fragebögen aus Anforderungen, Quellen-/Registereinträgen, Norm-/Control-Mappings, Leitfragen und Evidenzzielen.

### `audit-test-procedure-mapper`

Ordnet Auditfragen geeigneten Prüfmethoden, Stichprobenlogik, Evidenzarten, Bewertungshinweisen und Eskalationspunkten zu.

### `audit-finding-writer`

Schreibt Feststellungen, Abweichungen, Beobachtungen und Verbesserungspotenziale aus geprüfter Evidenz.

### `document-gap-analysis`

Vergleicht Dokumente mit Anforderungen, neuen Vorgaben und Registereinträgen und klassifiziert Änderungsbedarf.

### `interview-to-document-drafter`

Erstellt Governance-Dokumententwürfe aus Interviews, Stichpunkten und Rohmaterial nach Struktur, Zielgruppe und Reviewpunkten.

### `evidence-request-list-builder`

Erstellt Evidence Request Lists aus Anforderungen, Auditfragen, Prüfprogrammen und Evidence-Pack-Zielen mit Ownern, Fristen, Qualitätshinweisen und Human Gates.

### `control-test-designer`

Entwirft prüfbare Control Tests mit Testziel, Methode, Stichprobenlogik, Evidenz, Bewertungshinweisen und Eskalationspunkten.

### `corrective-action-planner`

Übersetzt Findings, Gaps und Abweichungen in konkrete Corrective Actions mit Ursache, Owner, Frist, Evidenz, Entscheidungspunkt und Reviewlogik.

### `remediation-effectiveness-review`

Prüft abgeschlossene Maßnahmen auf Umsetzungsnachweis, Wirksamkeitsindikatoren, Restrisiko, Wiedereröffnungsbedarf und Management-Handoff.

Hinweis: Policy-/Control-Entwürfe und KI-gestützte Compliance-Workflows werden in v1.0 über bestehende Skills, Workflows und Governance-Dokumente abgedeckt, nicht als separate Skill-Ordner geführt.

## Qualitätsgates

Alle Skills müssen gegen [`06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md`](../../06-evidence-management-review/evals/quality-gates.md) geprüft werden.

Minimal erforderlich:

- Public-Safety,
- Claim-Safety,
- Betriebslogik,
- Empowerment,
- Workload,
- Portabilität,
- Skill-Gate.

## Stop-Punkte

Skill-Arbeit stoppt bei:

- echten Personen-, Kunden- oder Organisationsdaten,
- vertraulichen Vertragsinhalten,
- lizenzpflichtigen Normtexten,
- Rechts- oder Datenschutzberatung,
- Konformitäts-, Zertifizierungs- oder Sicherheitsgarantien,
- Managemententscheidungen,
- externer Veröffentlichung oder Lizenz-/Disclaimer-Änderung ohne Freigabe.
