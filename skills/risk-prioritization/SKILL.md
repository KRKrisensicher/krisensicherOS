---
name: risk-prioritization
version: 1.0.0
description: "Priorisiert Risiken, Gaps und Maßnahmen nach Wirkung, Dringlichkeit, Evidenzbedarf und Aufwand."
category: governance
inputs:
  - scope
  - existing-artifacts
  - risks-or-findings
  - evidence-sources
outputs:
  - prioritized-risk-backlog
  - decision-brief
  - action-backlog
requires_human_review: true
---

<!-- kso:product-relevance
repo-scope: product
classification: agent-skill
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->


# risk-prioritization

## Zweck

Dieser Skill unterstützt Nutzerorganisationen dabei, priorisiert Risiken, Gaps und Maßnahmen nach Wirkung, Dringlichkeit, Evidenzbedarf, Aufwand und Managementrelevanz.

Er erzeugt betreibbare Arbeitsartefakte mit Ownern, Triggern, Evidenz, Reviewpunkten und menschlichen Entscheidungen. Er ersetzt keine verantwortliche Rolle.

## Wann verwenden

Nutze den Skill bei:

- Risikobacklogs, Gap-Listen, Maßnahmenpriorisierung oder Management Review-Vorbereitung,
- Vorbereitung von Reviews oder Workshops,
- Umwandlung unklarer Anforderungen in konkrete Routinen,
- Sichtbarmachung von Evidenzlücken und Entscheidungen,
- Aufbau eines priorisierten Verbesserungsbacklogs.

## Wann nicht verwenden

Nicht verwenden für:

- Rechtsberatung oder verbindliche Auslegung,
- Datenschutzberatung,
- Zertifizierungs-, Konformitäts- oder Sicherheitszusagen,
- automatisierte Managemententscheidungen,
- externe Kommunikation ohne Freigabe,
- Live-Krisenleitung oder operative Notfallsteuerung,
- Übernahme vertraulicher Inhalte oder lizenzpflichtiger Normtexte in öffentliche Artefakte.

## Eingangsdaten

Pflicht:

- **Scope:** betrachteter Prozess, Service, Governance-Bereich oder Reviewkontext.
- **Bestehende Artefakte:** vorhandene Register, Templates, Playbooks, Maßnahmen, Nachweise oder Rolleninformationen.
- **Risiken oder Findings:** bekannte Lücken, Unsicherheiten, Abhängigkeiten oder Managementfragen.

Optional:

- bestehende Evidenzquellen,
- Compliance-Registereinträge als Metadaten,
- Lessons Learned,
- Managementprioritäten,
- Ressourcen- oder Terminrahmen.

Annahmen:

- Fehlende Informationen werden als offene Prüfpunkte markiert.
- Reifegrade und Prioritäten sind Arbeitsannahmen, keine externe Zusicherung.

## Voraussetzungen

Hilfreich sind:

- `agents/public/risk-and-obligation-prioritizer.md`,
- `agents/public/control-evidence-architect.md`,
- `agents/public/risk-and-obligation-prioritizer.md`,
- `agents/public/management-review-facilitator.md`,
- `agents/public/agent-quality-and-safety-reviewer.md`,
- `templates/risikoregister-starter.md`, sobald vorhanden,
- `evals/quality-gates.md`.

## Ablauf

1. **Scope klären**  
   Beschreibe Ziel, Nicht-Scope, betroffene Rollen und erwartete Entscheidung.

2. **Ausgangslage erfassen**  
   Sammle vorhandene Artefakte, Routinen, Evidenzquellen, Risiken und Findings als Referenzen.

3. **Betriebslogik ableiten**  
   Formuliere Owner, Trigger, Ablauf, Output, Evidenz, Review-Kadenz und Eskalationspunkt.

4. **Lücken sichtbar machen**  
   Markiere fehlende Owner, fehlende Evidenz, unklare Entscheidungen, nicht geprüfte Annahmen und Abhängigkeiten.

5. **Maßnahmen und Optionen entwickeln**  
   Erzeuge ein kleines Backlog mit Wirkung, Aufwand, Abhängigkeit, Evidenzoutput und menschlichem Entscheidungspunkt.

6. **Priorisieren**  
   Priorisiere nach Risiko, Dringlichkeit, Entscheidungsrelevanz, Evidenzbedarf und Umsetzbarkeit.

7. **Review oder Brief vorbereiten**  
   Verdichte Ergebnisse in ein Review-Artefakt mit offenen Entscheidungen, Optionen, Risiken bei Nicht-Handeln und nächstem Schritt.

8. **Verification durchführen**  
   Prüfe Public-Safety, Claim-Safety, Betriebslogik, Workload, Human Review und Handoffs.

## Output-Artefakte

Der Skill erzeugt je nach Auftrag:

- Prioritized Risk Backlog,
- Decision Brief,
- priorisiertes Maßnahmenbacklog,
- Evidence Needs List,
- Reviewnotiz,
- Handoff-Liste an Agenten, Skills oder menschliche Rollen.

## Human-in-the-loop

Menschliche Prüfung ist erforderlich für:

- rechtliche oder normative Auslegung,
- Datenschutzbewertung,
- Risikoakzeptanz,
- Ressourcen-, Budget- oder Priorisierungsentscheidungen,
- finale Rollen- und Owner-Zuweisung,
- externe Kommunikation,
- Freigabe von Reviews, Briefings oder Maßnahmen.

## Verification

Prüfe vor Abschluss:

```text
Verification:
- Public-Safety: pass / notes / stop
- Claim-Safety: pass / notes / stop
- Betriebslogik: pass / notes / stop
- Workload: pass / notes / stop
- Evidenzbezug: pass / notes / stop
- Human Review: pass / notes / stop
- Handoffs: pass / notes / stop
- Ergebnis: pass / pass with notes / stop
```

Mindestfragen:

- Sind Scope und Nicht-Scope klar?
- Hat jedes Ergebnis Owner, Trigger, Output und Evidenzbezug?
- Sind Entscheidungen und Eskalationen menschlich markiert?
- Wurde unnötige Dokumentationslast entfernt?
- Sind Grenzen und rote Linien sichtbar?

## Qualitätsgates

Anzuwenden aus `evals/quality-gates.md`:

- U1 Public-Safe Gate,
- U2 Claim-Safety Gate,
- U3 Betriebslogik-Gate,
- U4 Empowerment-Gate,
- U5 Workload-Gate,
- U6 Portabilitäts-Gate,
- A2 Skill-Gate.

## Handoffs

Typische Handoffs:

- an `risk-and-obligation-prioritizer`, wenn fachliche Ausgestaltung vertieft werden muss,
- an `control-evidence-architect`, wenn Evidenzflüsse konkretisiert werden müssen,
- an `risk-and-obligation-prioritizer`, wenn Priorisierung unklar ist,
- an `management-review-facilitator`, wenn Entscheidungen vorbereitet werden müssen,
- an `agent-quality-and-safety-reviewer`, wenn Claim-Safety, Workload oder Public-Safety kritisch sind.

## Grenzen und rote Linien

Dieser Skill leistet keine Rechtsberatung, keine Datenschutzberatung, keine Zertifizierungs- oder Konformitätszusage und keine Managemententscheidung.

Er darf keine vertraulichen Inhalte, echten Kundendaten oder lizenzpflichtigen Normtexte in öffentliche Artefakte übernehmen.

Er darf keine Scheinsicherheit erzeugen: fehlende Evidenz, unklare Owner, offene Entscheidungen und Annahmen werden sichtbar markiert.

## Beispiel

Ausgangslage:

Eine fiktive Organisation möchte ein einzelnes Governance-Thema strukturiert bearbeiten. Es gibt erste Notizen, aber keine klare Routine, keine gesicherte Evidenz und keine priorisierte Entscheidungsvorlage.

Guter Skill-Output:

- Scope und Nicht-Scope sind benannt.
- Ein Owner-Vorschlag und Reviewrolle sind sichtbar.
- Die Routine hat Trigger, Ablauf, Output und Evidenz.
- Offene Entscheidungen sind im Decision Brief markiert.
- Nächste Maßnahme ist klein genug für den nächsten Reviewzyklus.

Schlechter Skill-Output:

- „Das Thema ist erledigt, sobald eine Richtlinie geschrieben wurde.“

Warum schlecht:

- Keine Betriebslogik, kein Owner, kein Evidenzbezug, keine Review-Kadenz und keine menschliche Entscheidung.

## Definition of Done

Der Skill ist abgeschlossen, wenn:

- Scope und Grenzen dokumentiert sind,
- Ausgangslage und Evidenzquellen erfasst sind,
- Rollen, Routinen und Eskalationen beschrieben sind,
- Lücken und Annahmen sichtbar sind,
- Maßnahmen priorisiert sind,
- menschliche Entscheidungen klar markiert sind,
- Verification dokumentiert ist.
