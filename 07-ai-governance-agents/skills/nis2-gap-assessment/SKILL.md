---
name: nis2-gap-assessment
version: 1.0.0
description: "Strukturiert NIS2-Readiness über Gaps, Evidenz, Maßnahmen, Priorisierung und Managemententscheidungen."
category: nis2
inputs:
  - scope
  - source-references
  - compliance-register-entries
  - existing-governance-artifacts
  - evidence-inventory
outputs:
  - nis2-gap-worksheet
  - prioritized-gap-backlog
  - evidence-needs-list
  - management-decision-brief
requires_human_review: true
---

<!-- kso:product-relevance
repo-scope: product
classification: agent-skill
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->


# nis2-gap-assessment

## Zweck

Dieser Skill hilft Nutzerorganisationen, NIS2-Readiness als betreibbare Gap-Arbeit zu strukturieren: Anforderungen werden auf Scope, bestehende Routinen, Evidenz, offene Lücken, Maßnahmen und Managemententscheidungen abgebildet.

Der Skill erzeugt keine rechtliche Bewertung und bestätigt keine NIS2-Konformität. Er macht sichtbar, wo menschliche Prüfung, Priorisierung, Ressourcenentscheidung oder fachliche Vertiefung nötig ist.

## Wann verwenden

Nutze den Skill bei:

- erster NIS2-Readiness-Sichtung,
- Vorbereitung eines internen Security-Governance-Backlogs,
- Abgleich öffentlicher Referenzquellen mit vorhandenen Rollen, Routinen und Nachweisen,
- Vorbereitung eines Management Reviews zu NIS2-relevanten Handlungsfeldern,
- Strukturierung von Findings aus Workshops, Audits oder Selbstbewertungen.

## Wann nicht verwenden

Nicht verwenden für:

- verbindliche rechtliche Auslegung der NIS2-Richtlinie oder nationaler Umsetzungsgesetze,
- Feststellung, ob eine Organisation rechtlich in den Anwendungsbereich fällt,
- Datenschutzberatung,
- Bestätigung regulatorischer Erfüllung,
- Zertifizierungs-, Sicherheits- oder Haftungsaussagen,
- Live-Incident- oder Krisenentscheidungen,
- Verarbeitung vertraulicher Vertragsinhalte oder lizenzpflichtiger Normtexte in öffentlichen Artefakten.

## Eingangsdaten

Pflicht:

- **Scope:** betrachtete Organisationseinheit, Services, Standorte, Systeme oder Prozesse.
- **Quellenreferenzen:** öffentliche Referenzanker aus `01-orientation/knowledge-sources/` oder eigene Registereinträge ohne Volltextübernahme lizenzpflichtiger Inhalte.
- **Bestehende Artefakte:** Rollenmodell, Policy-Entwürfe, Risiko-/Maßnahmenregister, Incident-Routinen, Lieferantenprozess oder Evidence Packs, sofern vorhanden.

Optional:

- bestehende Gap-Listen,
- Audit- oder Workshop-Findings,
- Risikoeinschätzungen,
- Managementvorgaben,
- Priorisierungslogik der Organisation,
- Nachweisquellen und Tool-Exporte als redigierte Metadaten.

Annahmen:

- Fehlende Informationen werden als offene Prüfpunkte markiert.
- Der Skill bewertet Reifegrad nur als Arbeitsannahme, nicht als externe Zusicherung.

## Voraussetzungen

Hilfreich sind:

- `01-orientation/knowledge-sources/hardwired-sources.yaml`,
- `02-governance-operating-model/02-governance-operating-model/compliance-register/sources.example.yaml` oder ein eigenes Register,
- `templates/nis2-gap-worksheet.md`, sobald vorhanden,
- `templates/evidence-pack-index.md`, sobald vorhanden,
- `07-ai-governance-agents/agents/public/regulatory-source-mapper.md`,
- `07-ai-governance-agents/agents/public/risk-and-obligation-prioritizer.md`,
- `07-ai-governance-agents/agents/public/control-evidence-architect.md`,
- `07-ai-governance-agents/agents/public/management-review-facilitator.md`,
- `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md`.

## Ablauf

1. **Scope und Nicht-Scope festlegen**  
   Beschreibe den betrachteten Bereich und markiere explizit, welche Teile nicht bewertet werden. Wenn der Anwendungsbereich rechtlich unklar ist, stoppe die Aussage und formuliere eine Frage für qualifizierte Prüfung.

2. **Quellen als Referenzanker sammeln**  
   Erfasse öffentliche Rechts-/Regulierungsquellen und interne Registereinträge als Metadaten: Quelle, Thema, Fundstelle/Referenz, Owner, Status, Reviewbedarf. Keine Normtexte oder vertraulichen Inhalte übernehmen.

3. **Anforderungen in Arbeitsfelder clustern**  
   Ordne die Referenzen operativen Feldern zu, z. B. Governance, Risiko, Incident, Business Continuity, Lieferanten, Schulung, Policies, Controls, Evidenz, Management Review.

4. **Bestehende Routinen und Nachweise zuordnen**  
   Frage je Arbeitsfeld: Welche Rolle betreibt das Thema? Welcher Trigger startet Arbeit? Welche Routine existiert? Welche Evidenz entsteht? Wer reviewed sie?

5. **Gaps formulieren**  
   Beschreibe Lücken als überprüfbare Arbeitsaussagen: fehlender Owner, unklarer Trigger, fehlende Routine, fehlende Evidenz, ungeprüfte Wirksamkeit, offene Managemententscheidung.

6. **Evidenzbedarf bestimmen**  
   Lege fest, welche Nachweise benötigt werden, wo sie entstehen, wie aktuell sie sein müssen und welche Qualität sie für Entscheidungen haben.

7. **Maßnahmen ableiten**  
   Übersetze Gaps in konkrete Maßnahmen mit Owner-Vorschlag, erwarteter Evidenz, Abhängigkeiten, Aufwandsschätzung und Reviewpunkt.

8. **Priorisieren**  
   Priorisiere nach Wirkung, Dringlichkeit, Risiko, Evidenzlücke, Umsetzungsaufwand, Abhängigkeiten und Managementrelevanz. Unklare Kriterien werden als Entscheidungsfrage markiert.

9. **Managemententscheidungen vorbereiten**  
   Erzeuge einen kurzen Decision Brief: Top-Gaps, Optionen, Ressourcenbedarf, Risiken bei Nicht-Handeln, offene rechtliche/fachliche Prüfungen und vorgeschlagene nächste Routine.

10. **Verification durchführen**  
   Prüfe Claim-Safety, Public-Safety, Betriebslogik, Evidence-Bezug, Handoffs und Workload. Stoppe bei unzulässigen Claims oder echten/vertraulichen Daten.

## Output-Artefakte

Der Skill erzeugt je nach Auftrag:

- NIS2 Gap Worksheet,
- priorisiertes Gap- und Maßnahmen-Backlog,
- Evidence Needs List,
- Quellen-/Register-Mapping,
- Rollen-/Routinen-Lückenliste,
- Management Decision Brief,
- Handoff-Liste an Agenten, Skills oder menschliche Rollen.

## Human-in-the-loop

Menschliche Prüfung ist erforderlich für:

- rechtliche Anwendbarkeit und Auslegung,
- Datenschutzbewertung,
- finale Risikoakzeptanz,
- Maßnahmenpriorisierung bei Ressourcen- oder Budgetwirkung,
- Owner- und Rollenentscheidungen,
- Freigabe von Management Briefs,
- externe Kommunikation an Behörden, Kunden, Auditoren oder Öffentlichkeit.

## Verification

Prüfe vor Abschluss:

```text
Verification:
- Public-Safety: pass / notes / stop
- Claim-Safety: pass / notes / stop
- NIS2-Fachgrenzen: pass / notes / stop
- Betriebslogik: pass / notes / stop
- Evidenzbezug: pass / notes / stop
- Priorisierung: pass / notes / stop
- Human Review: pass / notes / stop
- Handoffs: pass / notes / stop
- Ergebnis: pass / pass with notes / stop
```

Mindestfragen:

- Ist der Scope klar und begrenzt?
- Sind Quellen nur als Referenzanker oder eigene Zusammenfassung genutzt?
- Hat jeder Gap einen operativen Bezug zu Rolle, Routine, Evidenz oder Entscheidung?
- Gibt es eine nachvollziehbare Priorisierung?
- Sind rechtliche und Managemententscheidungen als menschliche Reviewpunkte markiert?
- Enthält der Output keine Konformitäts-, Zertifizierungs- oder Sicherheitsgarantie?

## Qualitätsgates

Anzuwenden aus `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md`:

- U1 Public-Safe Gate,
- U2 Claim-Safety Gate,
- U3 Betriebslogik-Gate,
- U4 Empowerment-Gate,
- U5 Workload-Gate,
- U6 Portabilitäts-Gate,
- A2 Skill-Gate,
- bei Templates zusätzlich A3 Template-Gate,
- bei Quellen-/Registerarbeit zusätzlich A8 Quellen-/Register-Gate.

## Handoffs

Typische Handoffs:

- an `regulatory-source-mapper`, wenn Quellen, Fundstellen oder Referenzanker unklar sind,
- an `compliance-register-curator`, wenn Registereinträge fehlen oder veraltet sind,
- an `security-governance-architect`, wenn Rollen und Routinen fehlen,
- an `risk-and-obligation-prioritizer`, wenn Gaps priorisiert werden müssen,
- an `control-evidence-architect`, wenn Evidence Packs oder Nachweisketten aufgebaut werden müssen,
- an `management-review-facilitator`, wenn Entscheidungen vorbereitet werden müssen,
- an `agent-quality-and-safety-reviewer`, wenn Claim-Safety, Workload oder Public-Safety kritisch sind.

## Grenzen und rote Linien

Dieser Skill leistet keine Rechtsberatung, keine Datenschutzberatung, keine Zertifizierungs- oder Konformitätsgarantie und keine Managemententscheidung.

Er darf keine vertraulichen Inhalte, echten Kundendaten oder lizenzpflichtigen Normtexte in öffentliche Artefakte übernehmen.

Er darf Unsicherheit nicht glätten: offene Anwendbarkeit, unklare Quellenlage, fehlende Evidenz oder widersprüchliche Prioritäten werden sichtbar markiert.

## Beispiel

Ausgangslage:

Eine fiktive Organisation möchte für einen kritischen digitalen Service prüfen, welche NIS2-Readiness-Arbeit als nächstes sinnvoll ist. Vorhanden sind ein grobes Rollenmodell, ein Incident-Prozessentwurf und ein unvollständiges Maßnahmenregister.

Guter Skill-Output:

- **Gap:** Incident-Routine hat Trigger und Eskalationsweg, aber kein After-Action-Review und keine Evidence-Ablage.  
  **Maßnahme:** After-Action-Review-Schritt und Evidence-Pack-Index ergänzen.  
  **Owner-Vorschlag:** Incident Owner mit ISB-Review.  
  **Evidenz:** Review-Protokoll, Maßnahmenliste, Entscheidungslog.  
  **Priorität:** hoch, weil Routine bereits existiert und Evidenzlücke Managemententscheidungen erschwert.  
  **Human Review:** Management entscheidet Ressourcen und Zieltermin.

Schlechter Skill-Output:

- „Ein dokumentierter Incident-Prozess reicht aus; weitere Prüfung ist nicht nötig.“

Warum schlecht:

- Ersetzt fachliche Prüfung durch Scheinsicherheit, enthält keine Betriebslogik, keine Evidenzqualität, keine menschliche Entscheidung und keine belastbare Abgrenzung.

## Definition of Done

Der Skill ist abgeschlossen, wenn:

- Scope und Nicht-Scope dokumentiert sind,
- Quellen als zulässige Referenzanker erfasst sind,
- Arbeitsfelder geclustert sind,
- bestehende Rollen, Routinen und Evidenz zugeordnet sind,
- Gaps überprüfbar formuliert sind,
- Evidenzbedarf und Maßnahmen beschrieben sind,
- Priorisierung nachvollziehbar ist,
- Managemententscheidungen und Human-Review-Punkte sichtbar sind,
- Handoffs benannt sind,
- Verification dokumentiert ist.
