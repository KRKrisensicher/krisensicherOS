<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Workflows

Workflows verbinden Agenten, Skills, Templates, Register und menschliche Freigabepunkte zu betreibbaren Abläufen.

Sie sind bewusst toolneutral. Ein Workflow beschreibt Fachlogik und Handoffs; konkrete Ausführung in Claude, Codex, OpenClaw, Hermes oder anderen Systemen erfolgt über dünne Adapter.

## Grundregeln

- Jeder Workflow hat Scope, Trigger, Inputs, Schritte, Outputs, Stop-Punkte und Human Gates.
- Agenten unterstützen; sie übernehmen keine Verantwortung.
- Rechtliche Auslegung, Datenschutzbewertung, Risikoakzeptanz, Managemententscheidungen und externe Kommunikation bleiben menschliche Aufgaben.
- Öffentliche Beispiele bleiben fiktiv und enthalten keine echten Organisations-, Kunden- oder Personendaten.
- Lizenzpflichtige Normen und vertrauliche Vorgaben werden nur als Metadaten, Verweise oder eigene Zusammenfassungen genutzt.

## Grundset v1.0

- `governance-operating-model.yaml` — Anforderungen in Rollen, Routinen, Evidenz und Entscheidungen übersetzen.
- `nis2-readiness-gap.yaml` — NIS2-Readiness-Gaps strukturiert erfassen und priorisieren.
- `minimum-viable-isms.yaml` — ISMS-Startmodus mit Scope, Risiko, Controls, Evidenz und Review entwerfen.
- `isms-risk-to-soa.yaml` — ISMS-Risiken nach Brutto-/Netto-Methodik bewerten, Maßnahmen ableiten und mit Control-/SoA-Einträgen mappen.
- `evidence-management-review.yaml` — Evidence Packs prüfen und Management Review vorbereiten.
- `audit-evidence-remediation-chain.yaml` — Anforderung, Auditfrage, Prüfprogramm, Evidence Request, Finding, Corrective Action, Wirksamkeitsreview und Management Review verbinden.
- `eu-ai-act-readiness-precheck.yaml` — KI-Systeme inventarisieren, Risikosignale markieren und Legal-/Datenschutz-/Management-Handoffs vorbereiten.

## Workflow-Gate

Vor Nutzung prüfen:

- Sind Trigger, Inputs und Output klar?
- Sind Agenten, Skills und Templates explizit verbunden?
- Gibt es Stop-/Eskalationspunkte?
- Sind Human Gates vor rechtlichen, datenschutzrechtlichen, Management- oder externen Aussagen sichtbar?
- Erzeugt der Workflow Entscheidungsfähigkeit statt Bürokratie?
