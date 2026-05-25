<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# 04 ISMS Basics

Dieses Modul beschreibt ein Minimum Viable ISMS als betreibbare Routinen statt Dokumentenfriedhof.

**Betriebslogik:** Verbindet Scope, Risiken, Controls, Reviews und Verbesserungen zu einem laufenden Betriebsmodell. Es nutzt ISO/IEC 27001 nur als Referenzanker und übernimmt keine Normtexte.

## Start hier

1. Kläre den ISMS-Scope mit [`templates/isms-scope-canvas.md`](templates/isms-scope-canvas.md).
2. Nutze [`playbooks/minimum-viable-isms-setup.md`](playbooks/minimum-viable-isms-setup.md), wenn ein kleiner Start statt Vollsystem nötig ist.
3. Führe Risikoarbeit mit [`risikomanagement-methodik.md`](risikomanagement-methodik.md) und [`templates/risikoanalyse-register.md`](templates/risikoanalyse-register.md).
4. Verbinde Risiken, Maßnahmen, Controls und SoA-Entscheidungen über [`templates/soa-risk-control-map.md`](templates/soa-risk-control-map.md).
5. Überführe Nachweise und Entscheidungen nach [`06 Evidence & Management Review`](../06-evidence-management-review/README.md).

## Betriebsfluss

`NIS2-/Governance-Gap aus 03 → Risiko bewerten → Controls/Maßnahmen planen → Evidenz in 06 prüfen → Management Review → Decision Log`

## Wichtigste Artefakte

- [`implementation-guides/isms/`](implementation-guides/isms/) — praktischer ISMS-Umsetzungsleitfaden.
- [`workflows/minimum-viable-isms.yaml`](workflows/minimum-viable-isms.yaml) — ISMS-Startworkflow.
- [`workflows/isms-risk-to-soa.yaml`](workflows/isms-risk-to-soa.yaml) — Risiko-zu-SoA-Workflow.
- [`playbooks/isms-risikoworkshop.md`](playbooks/isms-risikoworkshop.md) — Risikoworkshop vorbereiten.
- [`../07-ai-governance-agents/skills/isms-risk-analysis/SKILL.md`](../07-ai-governance-agents/skills/isms-risk-analysis/SKILL.md) — dialogischer Risikoanalyse-Skill.

## Human Gates

Risikoakzeptanz, Schutzbedarfs-/Impact-Bewertung, Control-Entscheidungen, SoA-Freigaben, Auditfähigkeit und Zertifizierungsfragen bleiben bei verantwortlichen Menschen.

## Typische Outputs

- ISMS-Scope,
- Risikoregister,
- Maßnahmen- und Control-Entscheidungen,
- Evidence-Pack-Vorbereitung,
- Management-Review-Inputs.
