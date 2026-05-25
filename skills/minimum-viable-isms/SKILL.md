---
name: minimum-viable-isms
version: 1.0.0
description: "Entwirft ein Minimum Viable ISMS als Scope-, Risiko-, Control-, Evidenz- und Review-Routine."
category: isms
inputs:
  - scope
  - risks
  - existing-controls
  - governance-roles
  - evidence-sources
outputs:
  - isms-scope-canvas
  - risk-control-routine-map
  - evidence-and-review-plan
  - minimum-viable-isms-backlog
requires_human_review: true
---

<!-- kso:product-relevance
repo-scope: product
classification: agent-skill
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->


# minimum-viable-isms

## Zweck

Dieser Skill hilft Nutzerorganisationen, ein Minimum Viable ISMS als arbeitsfähige Betriebsroutine zu entwerfen: klarer Scope, verständliche Risikologik, wenige wirksame Controls, nachvollziehbare Evidenz, Review-Kadenz und Managemententscheidungen.

Ziel ist kein perfektes Handbuch, sondern ein tragfähiger Startpunkt, der Verantwortung, Lernen und Verbesserung ermöglicht.

## Wann verwenden

Nutze den Skill bei:

- Aufbau eines ersten ISMS-Betriebsmodus,
- Überführung verstreuter Security-Aktivitäten in wiederkehrende Routinen,
- Vorbereitung eines ISMS-Scopes,
- Klärung von Risiko-, Control- und Evidence-Flows,
- Reduktion überladener Dokumentationsvorhaben auf einen nutzbaren Start,
- Vorbereitung eines Management Reviews zum ISMS-Aufbau.

## Wann nicht verwenden

Nicht verwenden für:

- Zertifizierungszusagen oder externe Bestätigungen,
- verbindliche Auslegung von Normen oder Gesetzen,
- Datenschutzberatung,
- Ersatz für Managemententscheidungen,
- Aufbau eines kompletten ISMS ohne verantwortliche Owner,
- Übernahme lizenzpflichtiger Normtexte in öffentliche Artefakte,
- Live-Krisensteuerung oder Incident-Entscheidungen.

## Eingangsdaten

Pflicht:

- **Scope-Kandidaten:** Organisationseinheiten, Services, Prozesse, Standorte oder Systeme, die betrachtet werden sollen.
- **Risikothemen:** bekannte Bedrohungen, Schwachstellen, Findings, Managementsorgen oder Betriebsabhängigkeiten.
- **Governance-Rollen:** menschliche Owner, Review-Rollen und Entscheidungsgremien, soweit vorhanden.

Optional:

- bestehende Policies,
- vorhandene Controls,
- Risiko- oder Maßnahmenregister,
- Evidence Packs,
- Lieferanten- oder Incident-Routinen,
- interne Vorgaben oder Compliance-Registereinträge als Metadaten.

Annahmen:

- Wenn Scope, Risikoakzeptanz oder Owner fehlen, markiert der Skill Entscheidungsfragen statt fiktive Gewissheit zu erzeugen.
- Reifegradbeschreibungen sind Arbeitsannahmen, keine externe Zusicherung.

## Voraussetzungen

Hilfreich sind:

- `templates/isms-scope-canvas.md`, sobald vorhanden,
- `templates/evidence-pack-index.md`, sobald vorhanden,
- `skills/governance-operating-model/SKILL.md`,
- `skills/nis2-gap-assessment/SKILL.md`,
- `agents/public/isms-operating-model-designer.md`,
- `agents/public/security-governance-architect.md`,
- `agents/public/risk-and-obligation-prioritizer.md`,
- `agents/public/control-evidence-architect.md`,
- `agents/public/management-review-facilitator.md`,
- `evals/quality-gates.md`.

## Ablauf

1. **ISMS-Zweck klären**  
   Beschreibe, welche Entscheidungsfähigkeit das ISMS zuerst schaffen soll: Risiken verstehen, Maßnahmen steuern, Evidenz bündeln, Verantwortlichkeiten klären oder Management Reviews ermöglichen.

2. **Scope minimal und begründet festlegen**  
   Definiere den Start-Scope so klein wie sinnvoll und so groß wie nötig. Markiere explizit, was nicht im Scope ist und wann eine Erweiterung geprüft wird.

3. **Kritische Assets und Prozesse ableiten**  
   Erfasse die wichtigsten Services, Informationen, Abhängigkeiten und Betriebsprozesse im Scope. Nutze nur fiktive Beispiele oder nutzerinterne private Daten außerhalb öffentlicher Repo-Artefakte.

4. **Risikologik aufbauen**  
   Formuliere wenige nachvollziehbare Risikothemen mit Ursache, möglicher Auswirkung, betroffener Rolle, aktueller Behandlung und offener Entscheidung.

5. **Controls als Betriebsroutinen beschreiben**  
   Beschreibe Controls mit Owner, Trigger, Ablauf, Output, Evidenz, Review-Frequenz und Eskalationspunkt.

6. **Evidenzplan erstellen**  
   Lege fest, welche Nachweise aus welchen Routinen entstehen, wie aktuell sie sein müssen, wo sie abgelegt werden und wer sie reviewed.

7. **Review-Kadenz festlegen**  
   Definiere minimale Routinen: Risiko-Review, Maßnahmenreview, Evidence-Pack-Review und Management Review. Entferne Routinen ohne Entscheidungs- oder Evidenznutzen.

8. **Backlog priorisieren**  
   Erstelle ein Minimum-Viable-ISMS-Backlog mit Maßnahmen, Owner-Vorschlag, Aufwand, Wirkung, Abhängigkeiten, Evidenzoutput und nächstem Reviewpunkt.

9. **Managemententscheidung vorbereiten**  
   Erzeuge einen Decision Brief mit Scope-Optionen, Top-Risiken, Ressourcenbedarf, akzeptierten Annahmen, offenen Entscheidungen und vorgeschlagenem Startzyklus.

10. **Verification durchführen**  
   Prüfe Betriebslogik, Workload, Human Review, Evidence-Bezug, Claim-Safety und Portabilität.

## Output-Artefakte

Der Skill erzeugt je nach Auftrag:

- ISMS Scope Canvas,
- Minimum-Viable-ISMS Operating Model,
- Risk-Control-Routine Map,
- Evidence and Review Plan,
- Management Decision Brief,
- Maßnahmen- und Verbesserungsbacklog,
- Handoff-Liste an Agenten, Skills oder menschliche Rollen.

## Human-in-the-loop

Menschliche Prüfung ist erforderlich für:

- finale Scope-Entscheidung,
- Risikoakzeptanz,
- Control-Auswahl und Priorisierung,
- Rollen- und Ressourcenentscheidung,
- rechtliche oder normative Auslegung,
- Datenschutzbewertung,
- Freigabe von Management Reviews,
- externe Kommunikation oder Audit-/Kundenaussagen.

## Verification

Prüfe vor Abschluss:

```text
Verification:
- Public-Safety: pass / notes / stop
- Claim-Safety: pass / notes / stop
- Betriebslogik: pass / notes / stop
- Workload: pass / notes / stop
- Scope-Klarheit: pass / notes / stop
- Risiko-Control-Bezug: pass / notes / stop
- Evidenz- und Review-Plan: pass / notes / stop
- Human Review: pass / notes / stop
- Handoffs: pass / notes / stop
- Ergebnis: pass / pass with notes / stop
```

Mindestfragen:

- Ist der Scope klar, begründet und begrenzt?
- Hat jedes zentrale Risiko mindestens eine Behandlungsidee oder offene Entscheidung?
- Sind Controls als Routinen mit Owner, Trigger, Output und Evidenz beschrieben?
- Gibt es eine Review-Kadenz, die Entscheidungen vorbereitet?
- Wurde unnötige Dokumentation entfernt?
- Sind Zertifizierungs-, Rechts- und Sicherheitsversprechen ausgeschlossen?

## Qualitätsgates

Anzuwenden aus `evals/quality-gates.md`:

- U1 Public-Safe Gate,
- U2 Claim-Safety Gate,
- U3 Betriebslogik-Gate,
- U4 Empowerment-Gate,
- U5 Workload-Gate,
- U6 Portabilitäts-Gate,
- A2 Skill-Gate,
- bei Templates zusätzlich A3 Template-Gate,
- bei Beispielen zusätzlich A6 Beispiel-Gate.

## Handoffs

Typische Handoffs:

- an `security-governance-architect`, wenn Rollen, Gremien oder Routinen fehlen,
- an `risk-and-obligation-prioritizer`, wenn Risiken und Maßnahmen priorisiert werden müssen,
- an `control-evidence-architect`, wenn Control- und Evidenzketten konkretisiert werden müssen,
- an `evidence-pack-reviewer`, wenn bestehende Evidence Packs geprüft werden,
- an `management-review-facilitator`, wenn Managemententscheidungen vorbereitet werden,
- an `policy-and-controls-drafter`, wenn Policy- oder Control-Entwürfe aus freigegebener Betriebslogik entstehen sollen,
- an `agent-quality-and-safety-reviewer`, wenn Workload, Claim-Safety oder Public-Safety kritisch sind.

## Grenzen und rote Linien

Dieser Skill leistet keine Rechtsberatung, keine Datenschutzberatung, keine Zertifizierungs- oder Konformitätszusage und keine Managemententscheidung.

Er darf keine vertraulichen Inhalte, echten Kundendaten oder lizenzpflichtigen Normtexte in öffentliche Artefakte übernehmen.

Er darf ein ISMS nicht als bloße Dokumentensammlung behandeln. Wenn ein Artefakt keinen Owner, Trigger, Output, Evidenz- oder Entscheidungsbezug hat, wird es gekürzt, umgebaut oder als nicht priorisiert markiert.

## Beispiel

Ausgangslage:

Eine fiktive Organisation startet mit einem digitalen Kernservice. Es gibt einzelne Security-Maßnahmen, aber keinen klaren ISMS-Scope, keine Review-Kadenz und keine einheitliche Evidenzablage.

Guter Skill-Output:

- **Scope:** digitaler Kernservice inklusive Betriebsteam und zwei unterstützenden IT-Prozessen; Vertriebssysteme zunächst außerhalb des Start-Scopes.  
- **Risiko:** unklare Wiederherstellungsfähigkeit bei Ausfall einer Betriebsplattform.  
- **Control-Routine:** quartalsweise Review der Backup- und Restore-Nachweise mit Service Owner und IT-Betrieb.  
- **Evidenz:** Restore-Testnotiz, Maßnahmenlog, Managemententscheidung bei Ressourcenbedarf.  
- **Review:** monatliches Maßnahmenreview, quartalsweiser Management Review für Top-Risiken.

Schlechter Skill-Output:

- „Erstellen Sie ein vollständiges ISMS-Handbuch mit allen Richtlinien und lassen Sie es jährlich prüfen.“

Warum schlecht:

- Zu dokumentenlastig, kein Start-Scope, keine Risiko- und Control-Logik, keine Evidenzroutine, keine Owner und keine Managemententscheidung.

## Definition of Done

Der Skill ist abgeschlossen, wenn:

- ISMS-Zweck und Start-Scope dokumentiert sind,
- Nicht-Scope und Erweiterungskriterien sichtbar sind,
- zentrale Risiken beschrieben sind,
- Controls als Routinen formuliert sind,
- Evidenz- und Review-Plan vorliegt,
- Maßnahmenbacklog priorisiert ist,
- Managemententscheidungen und Human-Review-Punkte benannt sind,
- Handoffs klar sind,
- Verification dokumentiert ist.
