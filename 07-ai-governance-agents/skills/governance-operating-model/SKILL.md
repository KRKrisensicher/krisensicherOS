---
name: governance-operating-model
version: 1.0.0
description: "Formt Anforderungen in Rollen, Routinen, Entscheidungen, Eskalationen und Evidenzflüsse."
category: governance
inputs:
  - scope
  - requirements
  - existing-roles
  - existing-routines
  - evidence-sources
outputs:
  - governance-operating-model-canvas
  - role-routine-map
  - evidence-flow-map
  - management-decision-log
requires_human_review: true
---


# governance-operating-model

## Zweck

Dieser Skill hilft Nutzerorganisationen, Anforderungen nicht als Dokumentenstapel, sondern als betreibbares Governance Operating Model zu strukturieren.

Er beantwortet:

- Welche Rollen werden gebraucht?
- Welche Routinen betreiben die Anforderungen?
- Welche Entscheidungen müssen vorbereitet werden?
- Welche Evidenz entsteht im Betrieb?
- Wo braucht es Eskalation oder Management Review?

## Wann verwenden

Nutze den Skill bei:

- Aufbau eines Security-Governance-Betriebsmodells,
- NIS2-/ISMS-/BCMS-Readiness-Arbeit,
- Übersetzung von Anforderungen in Verantwortlichkeiten,
- unklaren Rollen, Gremien, Reviews oder Evidence-Flows,
- Vorbereitung eines Management Reviews.

## Wann nicht verwenden

Nicht verwenden für:

- keine Rechtsberatung oder verbindliche Auslegung,
- keine Datenschutzberatung,
- keine Zertifizierungs- oder Konformitätsaussagen,
- keine Live-Krisenleitung,
- keine reine Policy-Erstellung ohne Betriebsmodell,
- keine Ersetzung von Managemententscheidungen.

## Eingangsdaten

Pflicht:

- **Scope:** betroffene Organisationseinheit, Services, Prozesse oder Governance-Domäne.
- **Anforderungen:** öffentliche Quellen, Registereinträge, Risiken, Audit Findings oder Managementvorgaben.
- **Bestehende Rollen:** ISB/CISO, Datenschutz, IT, Fachbereich, Management, Krisenstab, interne Revision oder ähnliche Rollen.

Optional:

- bestehende Routinen,
- bekannte Evidenzquellen,
- Management Review-Termine,
- Risiko- oder Maßnahmenregister,
- bestehende Templates.

Annahmen:

- Wenn Informationen fehlen, wird nicht geraten. Der Skill markiert Owner-Fragen und offene Prüfpunkte.

## Voraussetzungen

Hilfreich sind:

- `07-ai-governance-agents/agents/public/security-governance-architect.md`,
- `07-ai-governance-agents/agents/public/risk-and-obligation-prioritizer.md`,
- `07-ai-governance-agents/agents/public/control-evidence-architect.md`,
- `08-templates-playbooks/templates/governance-operating-model-canvas.md`, sobald vorhanden,
- `07-ai-governance-agents/evals/quality-gates.md`,
- relevante Einträge aus `10-reference/knowledge/` und `10-reference/compliance-register/`.

## Ablauf

1. **Scope eingrenzen**  
   Beschreibe, für welchen Bereich das Betriebsmodell gelten soll. Markiere, was nicht im Scope ist.

2. **Anforderungen clustern**  
   Gruppiere Anforderungen nach Themen, z. B. Risiko, Incident, Lieferanten, Management Review, Evidenz, BCMS, ISMS.

3. **Rollen identifizieren**  
   Ordne jeder Anforderung mindestens eine verantwortliche menschliche Rolle und unterstützende Rollen zu.

4. **Routinen ableiten**  
   Übersetze Anforderungen in wiederkehrende oder ereignisbasierte Routinen mit Trigger, Frequenz, Input, Ablauf und Output.

5. **Entscheidungspunkte bestimmen**  
   Markiere, welche Fragen Management-, Risikoakzeptanz-, Budget-, Priorisierungs- oder Eskalationsentscheidungen brauchen.

6. **Evidenzflüsse modellieren**  
   Bestimme, welche Nachweise aus welcher Routine entstehen und wer sie reviewed.

7. **Handoffs und Eskalationen definieren**  
   Lege fest, wann andere Agenten, Skills oder menschliche Rollen übernehmen müssen.

8. **Workload prüfen**  
   Entferne Routinen, die keine Risikoreduktion, Evidenzqualität oder Entscheidungsfähigkeit erzeugen.

9. **Review vorbereiten**  
   Erzeuge eine knappe Management- oder Owner-Review-Notiz mit offenen Entscheidungen.

## Output-Artefakte

Der Skill erzeugt je nach Auftrag:

- Governance Operating Model Canvas,
- Rollen-/Routinen-Matrix,
- RACI-Entwurf,
- Evidence Flow Map,
- Eskalations- und Handoff-Map,
- Management Decision Log,
- Maßnahmen- und Routinen-Backlog.

## Human-in-the-loop

Menschliche Prüfung ist erforderlich für:

- rechtliche oder regulatorische Auslegung,
- Datenschutzfragen,
- finale Rollen- und Verantwortungszuweisung,
- Risikoakzeptanz,
- Budget- oder Ressourcenentscheidungen,
- Freigabe von Management Reviews,
- externe Kommunikation oder Veröffentlichung.

## Verification

Prüfe vor Abschluss:

```text
Verification:
- Public-Safety: pass / notes / stop
- Claim-Safety: pass / notes / stop
- Betriebslogik: pass / notes / stop
- Workload: pass / notes / stop
- Human Review: pass / notes / stop
- Handoffs: pass / notes / stop
- Ergebnis: pass / pass with notes / stop
```

Mindestfragen:

- Hat jede Routine einen Trigger?
- Hat jede Routine einen Owner?
- Gibt es einen Output und eine Evidenzquelle?
- Sind Entscheidungen und Eskalationen sichtbar?
- Wurde unnötiger Meeting- oder Dokumentationsaufwand entfernt?

## Qualitätsgates

Anzuwenden aus `07-ai-governance-agents/evals/quality-gates.md`:

- U1 Public-Safe Gate,
- U2 Claim-Safety Gate,
- U3 Betriebslogik-Gate,
- U4 Empowerment-Gate,
- U5 Workload-Gate,
- U6 Portabilitäts-Gate,
- A2 Skill-Gate,
- bei Templates zusätzlich A3 Template-Gate,
- bei Workflows zusätzlich A5 Workflow-Gate.

## Handoffs

Typische Handoffs:

- an `regulatory-source-mapper`, wenn Quellen oder Fundstellen unklar sind,
- an `compliance-register-curator`, wenn Registereinträge fehlen,
- an `risk-and-obligation-prioritizer`, wenn Priorisierung nötig ist,
- an `control-evidence-architect`, wenn Evidenzflüsse detailliert werden müssen,
- an `management-review-facilitator`, wenn Entscheidungen vorbereitet werden müssen,
- an `agent-quality-and-safety-reviewer`, wenn Claims, Workload oder Grenzen kritisch sind.

## Grenzen und rote Linien

Dieser Skill leistet keine Rechtsberatung, keine Datenschutzberatung, keine Zertifizierungs- oder Konformitätsgarantie und keine Managemententscheidung.

Er darf keine vertraulichen Inhalte, echten Kundendaten oder lizenzpflichtigen Normtexte in öffentliche Artefakte übernehmen.

## Beispiel

Ausgangslage:

Eine fiktive Organisation möchte Anforderungen aus NIS2-Readiness, ISMS-Aufbau und Incident Readiness in einen ersten Betriebsmodus übersetzen.

Guter Skill-Output:

- Monatliche Risiko- und Maßnahmenroutine mit ISB als Owner, Management-Review-Eskalation bei Ressourcenbedarf und Maßnahmenlog als Evidenz.
- Quartalsweise Evidence-Pack-Review-Routine mit Control Ownern und Lückenliste.
- Ereignisbasierte Incident-Eskalationsroutine mit Rollen, Triggern, Kommunikationspunkten und After-Action-Review.
- Offene menschliche Prüfung: Anwendbarkeit der Anforderungen, Risikoakzeptanz, Managementpriorisierung.

Schlechter Skill-Output:

- „Erstellen Sie eine Informationssicherheitsrichtlinie und prüfen Sie diese regelmäßig.“

Warum schlecht:

- Keine Rollen, kein Trigger, keine Entscheidung, keine Evidenz, kein Review und keine Betriebslogik.

## Definition of Done

Der Skill ist abgeschlossen, wenn:

- Scope und Grenzen benannt sind,
- Anforderungen geclustert sind,
- Rollen und Routinen abgeleitet sind,
- Entscheidungspunkte sichtbar sind,
- Evidenzflüsse beschrieben sind,
- Handoffs und Human-Review-Punkte klar sind,
- Workload geprüft wurde,
- Verification dokumentiert ist.
