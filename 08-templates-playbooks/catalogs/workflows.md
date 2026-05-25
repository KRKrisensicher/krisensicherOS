<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Workflows

Workflows verbinden Agenten, Skills, Templates, Register und menschliche Freigabepunkte zu betreibbaren Abläufen.

## Betriebsfluss über Module

`02 Governance-Modell → 03 Gap → 04 Risiko/Controls → 06 Evidence/Review → Decision Log`

## Workflow-Grundset v1.0

- [`governance-operating-model.yaml`](../../02-governance-operating-model/workflows/governance-operating-model.yaml) — Anforderungen in Rollen, Routinen, Evidenz und Entscheidungen übersetzen.
- [`nis2-readiness-gap.yaml`](../../03-nis2-readiness/workflows/nis2-readiness-gap.yaml) — NIS2-Readiness-Gaps erfassen und priorisieren.
- [`nis2-vorab-betroffenheitspruefung.yaml`](../../03-nis2-readiness/workflows/nis2-vorab-betroffenheitspruefung.yaml) — NIS2-Vorprüfung mit Legal-Handoff vorbereiten.
- [`minimum-viable-isms.yaml`](../../04-isms-basics/workflows/minimum-viable-isms.yaml) — ISMS-Startmodus mit Scope, Risiko, Controls, Evidenz und Review entwerfen.
- [`isms-risk-to-soa.yaml`](../../04-isms-basics/workflows/isms-risk-to-soa.yaml) — Risiken bewerten, Maßnahmen ableiten und mit Control-/SoA-Einträgen mappen.
- [`nis2-incident-and-management-readiness.yaml`](../../05-incident-crisis-readiness/workflows/nis2-incident-and-management-readiness.yaml) — Incident-/Melde- und Management-Readiness verbinden.
- [`evidence-management-review.yaml`](../../06-evidence-management-review/workflows/evidence-management-review.yaml) — Evidence Packs prüfen und Management Review vorbereiten.
- [`audit-evidence-remediation-chain.yaml`](../../06-evidence-management-review/workflows/audit-evidence-remediation-chain.yaml) — Auditfrage, Test, Evidence Request, Finding, Corrective Action, Wirksamkeit und Review verbinden.
- [`eu-ai-act-readiness-precheck.yaml`](../../07-ai-governance-agents/workflows/eu-ai-act-readiness-precheck.yaml) — KI-Systeme inventarisieren und Handoff-Fragen markieren.

## Workflow-Gate

Vor Nutzung prüfen: Trigger, Inputs, Outputs, Agenten/Skills/Templates, Stop-Punkte, Human Gates und Entscheidungsnutzen.
