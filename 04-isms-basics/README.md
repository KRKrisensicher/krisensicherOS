<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# 04 ISMS Basics

This module describes a minimum viable ISMS as operable routines instead of a document graveyard.

**Operating logic:** Connects scope, risks, controls, reviews, and improvements into a running operating model. It uses ISO/IEC 27001 only as a reference anchor and does not reproduce standard text.

## Start here

1. Clarify ISMS scope with [`templates/isms-scope-canvas.md`](templates/isms-scope-canvas.md).
2. Use [`playbooks/minimum-viable-isms-setup.md`](playbooks/minimum-viable-isms-setup.md) when a small start is needed instead of a full system.
3. Run risk work with [`risikomanagement-methodik.md`](risikomanagement-methodik.md) and [`templates/risikoanalyse-register.md`](templates/risikoanalyse-register.md).
4. Connect risks, measures, controls, and SoA decisions through [`templates/soa-risk-control-map.md`](templates/soa-risk-control-map.md).
5. Move evidence and decisions into [`06 Evidence & Management Review`](../06-evidence-management-review/README.md).

## Operating flow

`NIS2/governance gap from 03 → assess risk → plan controls/measures → review evidence in 06 → management review → decision log`

## Key artifacts

- [`implementation-guides/isms/`](implementation-guides/isms/) — practical ISMS implementation guide.
- [`workflows/minimum-viable-isms.yaml`](workflows/minimum-viable-isms.yaml) — ISMS start workflow.
- [`workflows/isms-risk-to-soa.yaml`](workflows/isms-risk-to-soa.yaml) — risk-to-SoA workflow.
- [`playbooks/isms-risikoworkshop.md`](playbooks/isms-risikoworkshop.md) — prepare a risk workshop.
- [`../07-ai-governance-agents/skills/isms-risk-analysis/SKILL.md`](../07-ai-governance-agents/skills/isms-risk-analysis/SKILL.md) — dialog-based risk analysis skill.

## Human gates

Risk acceptance, protection-needs/impact assessment, control decisions, SoA approvals, audit readiness, and certification questions remain with accountable humans.

## Typical outputs

- ISMS scope,
- risk register,
- measure and control decisions,
- evidence pack preparation,
- management review inputs.
