---
name: interview-to-document-drafter
version: 1.0.0
description: "Erstellt Governance-Entwürfe aus Interviews mit Struktur, Ton, Annahmen, Lücken und Reviewpunkten."
category: governance
inputs:
  - scope
  - requirements-or-raw-material
  - existing-artifacts
  - evidence-or-source-references
outputs:
  - governance-document-draft
  - review-notes
  - decision-or-action-backlog
requires_human_review: true
---


# interview-to-document-drafter

## Zweck

Dieser Skill hilft Nutzerorganisationen, Interviews und Rohmaterial in konsistente Governance-Dokumente nach Vorgaben, Zielgruppe, Struktur und Freigabepunkten zu überführen.

Er arbeitet mit Quellen, Anforderungen, Normen, Controls, Dokumenten oder Rohmaterial nur als Referenzen, Metadaten, eigene Zusammenfassungen oder private Nutzerinhalte. Er erzeugt keine Rechtsberatung, keine Datenschutzberatung und keine Konformitäts-, Audit- oder Zertifizierungszusage.

## Wann verwenden

Nutze den Skill, wenn Workshops, Interviews, Rohnotizen oder Stichpunkte in Policies, Prozessbeschreibungen, Reviewnotizen oder Managementunterlagen übertragen werden sollen.

Typische Auslöser:

- neue oder geänderte Anforderungen,
- interne Audits oder Self-Assessments,
- Dokumentenreviews,
- Evidence-Pack-Reviews,
- Management Review-Vorbereitung,
- Handoffs aus Risiko-, Control- oder Compliance-Register-Arbeit.

## Wann nicht verwenden

Nicht verwenden für:

- verbindliche Rechts- oder Vertragsauslegung,
- Datenschutzbewertung,
- externe Audit- oder Zertifizierungszusage,
- Managemententscheidung,
- Live-Incident- oder Krisensteuerung,
- Reproduktion lizenzpflichtiger Normtexte,
- öffentliche Verarbeitung vertraulicher Dokumente, Interviews oder personenbezogener Daten.

## Eingangsdaten

Pflicht:

- **Scope:** Audit-, Dokumenten-, Prozess-, Control- oder Reviewbereich.
- **Anforderungen oder Rohmaterial:** Registereinträge, Quellenreferenzen, Controls, Interviewnotizen, Dokumentauszüge oder Findings.
- **Zieloutput:** Fragebogen, Prüfprogramm, Finding, Gap-Matrix oder Dokumententwurf.

Optional:

- bestehende Dokumente oder Templates,
- Norm-/Control-Referenzen als Metadaten,
- Evidence Pack oder Nachweisverzeichnis,
- Rollen und Owner,
- Bewertungsskala oder Auditmethodik,
- Zielgruppe und Tonalität.

Annahmen:

- Unklare Aussagen werden als Annahmen oder offene Prüfpunkte markiert.
- Fehlende Quellen oder Evidenz werden nicht erfunden.

## Voraussetzungen

Hilfreich sind:

- `07-ai-governance-agents/agents/public/governance-document-drafter.md`, sobald vorhanden,
- `07-ai-governance-agents/agents/public/control-evidence-architect.md`,
- `07-ai-governance-agents/agents/public/evidence-pack-reviewer.md`,
- `07-ai-governance-agents/agents/public/management-review-facilitator.md`,
- `07-ai-governance-agents/agents/public/agent-quality-and-safety-reviewer.md`,
- `08-templates-playbooks/templates/governance-document-outline.md`,
- `08-templates-playbooks/templates/evidence-pack-index.md`,
- `08-templates-playbooks/templates/decision-log.md`,
- `07-ai-governance-agents/evals/quality-gates.md`.

## Ablauf

1. **Scope und Ziel klären**  
   Lege fest, welcher Audit-, Dokumenten- oder Governance-Bereich betrachtet wird und welcher Output entstehen soll.

2. **Kriterien und Anforderungen sammeln**  
   Erfasse Quellen, Registereinträge, Norm-/Control-Referenzen, interne Vorgaben oder Interviewaussagen nur als zulässige Referenzen, Metadaten oder eigene Zusammenfassungen.

3. **Mapping erstellen**  
   Ordne Anforderungen passenden Controls, Dokumentabschnitten, Fragen, Evidenzarten, Prüfmethoden oder Maßnahmen zu. Markiere unklare Mappings.

4. **Arbeitsartefakt erzeugen**  
   Erstelle den konkreten Entwurf mit Kriterium, Zustand/Frage, Methode, Evidenzziel, Bewertungshinweis, Owner, Risiko oder Follow-up.

5. **Lücken und Annahmen markieren**  
   Trenne bestätigte Evidenz, Annahmen, offene Fragen, Abweichungen, Beobachtungen und Verbesserungspotenziale.

6. **Review und Entscheidung vorbereiten**  
   Markiere, wer prüfen, freigeben oder entscheiden muss. Bereite Maßnahmen, Decision Log oder Management Review-Handoff vor.

7. **Verification durchführen**  
   Prüfe Public-Safety, Claim-Safety, Quellen-/Evidenzbezug, Workload, Human Review und Handoffs.

## Output-Artefakte

Der Skill erzeugt je nach Auftrag:

- governance-document-draft,
- Mapping zwischen Anforderung, Control, Frage, Methode, Evidenz und Owner,
- offene Prüffragen,
- Lücken- oder Finding-Liste,
- Maßnahmen- oder Review-Backlog,
- Management- oder Owner-Handoff.

## Human-in-the-loop

Menschliche Prüfung ist erforderlich für:

- Auslegung von Gesetzen, Normen oder Verträgen,
- Datenschutzbewertung,
- finale Auditbewertung,
- Abweichungsklassifikation mit Organisationswirkung,
- Maßnahmenfreigabe,
- Risikoakzeptanz,
- Dokumentenfreigabe,
- externe Kommunikation.

## Verification

```text
Verification:
- Public-Safety: pass / notes / stop
- Claim-Safety: pass / notes / stop
- Quellen-/Kriterienbezug: pass / notes / stop
- Evidenzbezug: pass / notes / stop
- Betriebslogik: pass / notes / stop
- Workload: pass / notes / stop
- Human Review: pass / notes / stop
- Handoffs: pass / notes / stop
- Ergebnis: pass / pass with notes / stop
```

Mindestfragen:

- Sind Scope, Kriterien und Zieloutput klar?
- Sind Anforderungen nur zulässig referenziert oder zusammengefasst?
- Sind Fragen, Methoden, Findings oder Dokumentabschnitte nachvollziehbar gemappt?
- Sind Evidenzbedarf und Bewertungshinweise prüfbar?
- Sind Annahmen, Lücken und Human Gates sichtbar?
- Wurden keine Garantien oder finalen Entscheidungen behauptet?

## Qualitätsgates

Anzuwenden aus `07-ai-governance-agents/evals/quality-gates.md`:

- U1 Public-Safe Gate,
- U2 Claim-Safety Gate,
- U3 Betriebslogik-Gate,
- U4 Empowerment-Gate,
- U5 Workload-Gate,
- U6 Portabilitäts-Gate,
- A2 Skill-Gate,
- A3 Template-Gate, wenn Templates erzeugt oder genutzt werden,
- A8 Quellen-/Register-Gate, wenn Quellen oder Norm-/Registereinträge betroffen sind.

## Handoffs

Typische Handoffs:

- an `governance-document-drafter`, wenn fachliche Vertiefung nötig ist,
- an `control-evidence-architect`, wenn Evidenz- oder Control-Mapping fehlt,
- an `evidence-pack-reviewer`, wenn Nachweise geprüft werden müssen,
- an `management-review-facilitator`, wenn Entscheidungen vorbereitet werden müssen,
- an `agent-quality-and-safety-reviewer`, wenn Claims, Vertraulichkeit oder Workload kritisch sind.

## Grenzen und rote Linien

Dieser Skill leistet keine Rechtsberatung, keine Datenschutzberatung, keine Zertifizierungs-, Audit- oder Konformitätszusage und keine Managemententscheidung.

Er darf keine vertraulichen Inhalte, personenbezogenen Daten, echten Kundendaten oder lizenzpflichtigen Normtexte in öffentliche Artefakte übernehmen.

Er darf keine Evidenz erfinden, keine Lücken glätten und keine finalen Bewertungen ohne menschliche Prüfung formulieren.

## Beispiel

Ausgangslage:

Eine fiktive Organisation möchte interne Auditfragen, Dokumentengaps oder Findings aus vorhandenen Registereinträ­gen und Evidence-Pack-Notizen ableiten. Einige Anforderungen sind unklar, mehrere Nachweise fehlen.

Guter Skill-Output:

- Anforderungen sind als Referenzen erfasst.
- Leitfrage, Methode, Evidenzziel und Owner sind sichtbar.
- Annahmen und fehlende Evidenz sind markiert.
- Feststellungen sind sachlich und nachvollziehbar.
- Management- oder Owner-Entscheidungen sind als Human Gate gekennzeichnet.

Schlechter Skill-Output:

- „Die Prüfung ist erledigt; weitere Evidenz oder menschliche Bewertung ist nicht nötig.“

Warum schlecht:

- Das erzeugt Scheinsicherheit, ersetzt menschliche Bewertung und enthält eine unzulässige Zusage.

## Definition of Done

Der Skill ist abgeschlossen, wenn:

- Scope, Kriterien und Zieloutput dokumentiert sind,
- Anforderungen und Mappings nachvollziehbar sind,
- Fragen, Methoden, Findings oder Dokumentstruktur prüfbar sind,
- Evidenzbedarf und Lücken sichtbar sind,
- Human-Review- und Freigabepunkte markiert sind,
- Handoffs und nächste Schritte klar sind,
- Verification dokumentiert ist.
