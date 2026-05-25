<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Documentation

## Purpose

This folder contains the public user paths, setup notes, standards, and product boundaries for krisensicherOS.

krisensicherOS is a product repository for AI-assisted security governance. Internal working notes, review traces, briefings, roadmaps, and release engineering do not belong in this product repository.

## Getting started for v1.0

Start here:

1. [`../README.md`](../README.md) — product overview and boundaries.
2. [`getting-started/README.md`](getting-started/README.md) — navigation through the entry paths.
3. [`getting-started/anwenderpfade.md`](getting-started/anwenderpfade.md) — NIS2, ISMS, evidence/management review, and incident/notification readiness.
4. [`getting-started/artefaktpakete.md`](getting-started/artefaktpakete.md) — reusable packages from templates, workflows, playbooks, and guides.
5. [`setup/README.md`](setup/README.md) — selection of an approved AI environment.
6. [`getting-started/30-60-90-minuten-nutzungspfad.md`](getting-started/30-60-90-minuten-nutzungspfad.md) — first end-to-end pass.
7. [`product/was-wir-bewusst-nicht-bauen.md`](product/was-wir-bewusst-nicht-bauen.md) — product guardrail against feature creep, apparent compliance, and template volume.

## Setup

Setup documents explain approved AI working methods:

- [`setup/chatgpt-lokale-ide.md`](setup/chatgpt-lokale-ide.md)
- [`setup/m365-copilot.md`](setup/m365-copilot.md)
- [`setup/claude-code.md`](setup/claude-code.md)
- [`setup/lokale-ki.md`](setup/lokale-ki.md)
- [`setup/ki-setups-bedienungsanleitung.md`](setup/ki-setups-bedienungsanleitung.md)

If there is no AI usage approval yet, krisensicherOS is not yet operational. In that case, use only [`../templates/ki-nutzungsfreigabe-matrix.md`](../templates/ki-nutzungsfreigabe-matrix.md) to prepare the approval.

## Readiness

NIS2 readiness artifacts:

- [`readiness/nis2-erwaegungsgruende-implementierungslogik.md`](readiness/nis2-erwaegungsgruende-implementierungslogik.md) — recitals of the NIS2 Directive as implementation logic.

## Standards

Current standards:

- [`standards/public-agent-profile-standard-v1.0.md`](standards/public-agent-profile-standard-v1.0.md)
- [`standards/skill-standard-v1.0.md`](standards/skill-standard-v1.0.md)

## Boundaries

This documentation does not replace legal advice, data protection advice, certification advice, or a management decision. It provides working tools and review logic for AI-assisted governance work.
