<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# 03 NIS2 Readiness

Dieses Modul unterstützt NIS2-Vorabprüfung, Gap-Analyse, Maßnahmenpriorisierung, Melde-Readiness, Evidenzlogik und Managementkommunikation.

**Betriebslogik:** Übersetzt regulatorischen Druck in steuerbare Arbeitspakete, prüfbare Nachweise und klare Managemententscheidungen. Es ersetzt keine Rechtsberatung und keine verbindliche Betroffenheitsprüfung.

## Start hier

1. Starte bei unklarem Scope mit dem [`NIS2-Vorab-Betroffenheitsfragebogen`](templates/nis2-vorab-betroffenheitspruefung-fragebogen.md).
2. Nutze den [`NIS2-Readiness-Startworkshop`](playbooks/nis2-readiness-startworkshop.md), wenn Managementauftrag, Rollen und erster Scope geklärt werden müssen.
3. Erfasse Lücken im [`NIS2-Gap-Worksheet`](templates/nis2-gap-worksheet.md).
4. Verbinde Findings mit Evidenz und Entscheidungen über [`06 Evidence & Management Review`](../06-evidence-management-review/README.md).
5. Übe Melde- und Eskalationslogik mit [`nis2-incident-melde-triage.md`](playbooks/nis2-incident-melde-triage.md).

## Betriebsfluss

`Gap erfassen → Risiko/Controls in 04 bewerten → Evidence Requests in 06 erstellen → Management Review vorbereiten → Decision Log aktualisieren`

## Wichtigste Artefakte

- [`readiness/nis2-erwaegungsgruende-implementierungslogik.md`](readiness/nis2-erwaegungsgruende-implementierungslogik.md) — Erwägungsgründe in Betriebslogik übersetzen.
- [`workflows/nis2-readiness-gap.yaml`](workflows/nis2-readiness-gap.yaml) — strukturierter Gap-Workflow.
- [`workflows/nis2-vorab-betroffenheitspruefung.yaml`](workflows/nis2-vorab-betroffenheitspruefung.yaml) — Vorprüfungsworkflow mit Legal-Handoff.
- [`templates/nis2-management-review-und-schulung.md`](templates/nis2-management-review-und-schulung.md) — Geschäftsleitungs-Schulung und Review vorbereiten.
- [`../02-governance-operating-model/templates/legal-datenschutz-handoff.md`](../02-governance-operating-model/templates/legal-datenschutz-handoff.md) — Handoff bei Rechts-/Datenschutzfragen.

## Human Gates

Betroffenheit, Rechtsauslegung, Meldefristen, externe Kommunikation, Risikoakzeptanz und Geschäftsleitungsentscheidungen müssen durch zuständige Menschen geprüft und freigegeben werden.

## Typische Outputs

- vorläufiger Scope mit Legal-Handoff,
- priorisierte Gaps,
- Evidence Requests,
- Managemententscheidungen im Decision Log,
- Eskalations- und Meldeübung ohne Live-Krisenleitungsanspruch.
