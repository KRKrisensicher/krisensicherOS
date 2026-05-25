<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# 07 AI Governance Agents

Dieses Modul beschreibt, wie Nutzerorganisationen krisensicherOS-Agenten kontrolliert einsetzen, um Security Governance, NIS2-Readiness, ISMS, BCMS, Evidenzarbeit und Management Reviews zu unterstützen.

Agenten sind keine Ersatzverantwortlichen. Sie strukturieren Arbeit, bereiten Entscheidungen vor, prüfen Qualität und machen Handoffs sichtbar.

## Inhalte

- [`human-in-the-loop.md`](human-in-the-loop.md) — menschliche Freigabepunkte, Entscheidungen und Stop-Punkte.
- [`agent-operating-rules.md`](agent-operating-rules.md) — Betriebsregeln für Aufträge, Daten, Quellen, Handoffs und Reviews.
- [`risk-and-limits.md`](risk-and-limits.md) — typische Risiken agentischer Governance-Arbeit und Gegenmaßnahmen.
- [`../01-orientation/getting-started/eu-ai-act-readiness-start.md`](../01-orientation/getting-started/eu-ai-act-readiness-start.md) — KI-Systeme als Inventar-, Vorprüfungs- und Handoff-Routine starten.
- [`./agents/public/role-model.md`](./agents/public/role-model.md) — öffentliches Rollenmodell der Zielrepo-Agenten.
- [`./agents/manifest.yaml`](./agents/manifest.yaml) — Manifest für Agentenfamilien, Handoffs und Adapter.

## Empfohlener Einstieg

1. Ziel und Scope festlegen.
2. Minimal benötigte Agenten aus dem Rollenmodell wählen.
3. Human Gates festlegen.
4. passende Skills, Templates oder Workflows auswählen.
5. Output gegen Qualitätsgates prüfen.
6. Entscheidungen menschlich treffen und dokumentieren.

## Betriebslogik

Ein Agentenlauf ist nur nützlich, wenn klar ist:

- wer ihn beauftragt,
- welche Daten und Quellen erlaubt sind,
- welcher Output entstehen soll,
- wer reviewed,
- welche Entscheidung vorbereitet wird,
- wo gestoppt oder eskaliert werden muss.
