<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# krisensicherOS 🛡️

krisensicherOS is an open English-language product branch of the German source repository for **AI-assisted security governance**: NIS2 readiness, ISMS basics, crisis readiness, evidence work, and management reviews as operable routines instead of a document graveyard.

The repository contains public agent profiles, skills, templates, workflows, and playbooks. It is intended for organizations that have approved AI or want to prepare AI usage approval in a targeted way.

**Clarification:** Without an approved AI environment, krisensicherOS is not a meaningful operating mode. Organizations can read individual templates or prepare AI usage approval, but the product value comes from AI-assisted work with human gates.

## Start in 15 minutes

1. Open [`docs/getting-started/README.md`](docs/getting-started/README.md) and choose a user path.
2. For the smallest NIS2 start, use the [`5-artifact quick start`](docs/getting-started/minimaler-nis2-start-in-5-artefakten.md).
3. If you already know what you need, go directly to the [`user paths`](docs/getting-started/anwenderpfade.md) or [`artifact packages`](docs/getting-started/artefaktpakete.md).

## Five quick user paths

- **Start NIS2:** Scope, register entry, gap, evidence requests, and decision log handoff.
- **Start ISMS:** Scope, risks, control routines, evidence pack, and review date.
- **Build evidence/management review:** Bundle evidence and prepare management decisions.
- **Practice incident/notification readiness:** Train escalation, triage, and human gates.
- **Start EU AI Act readiness:** Inventory AI systems, flag role questions, and prepare legal/data protection/management handoffs.

Details are in [`docs/getting-started/anwenderpfade.md`](docs/getting-started/anwenderpfade.md).

## Minimal start sequence

1. Choose a path or package from [`docs/getting-started/`](docs/getting-started/README.md).
2. Check AI usage approval with [`templates/ki-nutzungsfreigabe-matrix.md`](templates/ki-nutzungsfreigabe-matrix.md).
3. Choose exactly one approved AI environment from [`docs/setup/README.md`](docs/setup/README.md).
4. Use no more than one artifact package from [`docs/getting-started/artefaktpakete.md`](docs/getting-started/artefaktpakete.md).
5. Mark human gates for management, risk acceptance, legal, data protection, and external communication.

## Mission

krisensicherOS helps translate compliance work into roles, routines, evidence, and management decisions.

Product guardrail: krisensicherOS builds only components that increase decision readiness, evidence flow, or operating routine. Anything that only creates more documents, consultant optics, or apparent compliance stays out. See [`docs/product/was-wir-bewusst-nicht-bauen.md`](docs/product/was-wir-bewusst-nicht-bauen.md).

## Core thesis

AI can accelerate documentation, mapping, and evidence work. Responsibility remains with the accountable roles.

Value emerges when governance becomes visible in operations:

- clarify responsibility,
- prepare decisions,
- prioritize risks,
- generate evidence from real work,
- involve management,
- practice crisis readiness,
- operate security routines sustainably.

Agents prepare. Humans review, decide, and remain accountable.

## Who is krisensicherOS for?

krisensicherOS is intended for:

- CISOs,
- information security officers,
- security managers,
- governance/risk/compliance managers,
- organizations close to critical infrastructure,
- regulated mid-sized organizations,
- municipal and public institutions.

A clarified or deliberately prepared use of AI for suitable data classes is required.

## What krisensicherOS does differently

Traditional compliance work often produces documents, lists, and evidence requests. krisensicherOS thinks differently:

> Governance must be operated, not filed away.

Every artifact in this repository must answer:

1. Who uses it?
2. When is it used?
3. Which decision, routine, or escalation does it support?
4. What evidence results from it?
5. Who remains accountable?

## Knowledge sources and compliance register

krisensicherOS works on two levels:

1. **Hard-wired public reference sources** such as the NIS2 Directive, BSIG, EnWG, GDPR, BDSG, and BSI-KritisV.
2. **User-owned compliance registers** for standards, customer contracts, internal policies, audit findings, and sector-specific requirements.

Important: Licensed standards such as ISO/IEC 27001 are not included in the repository as standard text. The repository provides only metadata, mapping, and working structures. See [`docs/legal/iso-normen-lizenzkonform-nutzen.md`](docs/legal/iso-normen-lizenzkonform-nutzen.md).

Purchased ISO, DIN, EVS, BSI, or other standards documents must not be transferred into this repository, prompts, agents, RAG systems, embeddings, vector databases, or other AI systems without an appropriate license. For krisensicherOS: obtain and read standards externally in line with license terms, but maintain only your own summaries, IDs, mappings, decision fields, and public-safe working structures in the repository.

## v1.0 scope

Version 1.0 focuses on a resilient basic system:

- NIS2 readiness,
- security governance basic system,
- ISMS basics,
- incident and crisis readiness,
- AI-assisted evidence and management review work,
- EU AI Act readiness as an inventory, preliminary assessment, and handoff starter,
- agents and skills for routine CISO/information security officer work.

## Non-goals

krisensicherOS is explicitly not:

- legal advice,
- data protection advice,
- certification assurance,
- a complete ISO 27001 replacement,
- a manual template repository without AI use,
- a tool for automating responsibility,
- a collection of arbitrary policy templates,
- false assurance through checklists,
- a substitute for management decisions, risk owners, or security managers.

## Disclaimer

krisensicherOS provides working aids, structuring aids, agent roles, skills, templates, and playbooks. The repository does not pre-build governance for a specific organization, but provides components that professionally accountable persons must review, adapt, and approve for their organization. The content does not replace legal review, data protection review, certification consulting, regulatory interpretation, or organization-specific risk decisions.

All results must be reviewed, adapted, and approved by professionally accountable persons. Agents can prepare, structure, check, and accelerate — they do not assume responsibility.

## Repository structure v1.0

```text
01-orientation/
02-governance-operating-model/
03-nis2-readiness/
04-isms-basics/
05-incident-crisis-readiness/
06-evidence-management-review/
07-ai-governance-agents/
08-templates-playbooks/
09-implementation-roadmaps/
agents/public/
skills/
templates/
playbooks/
implementierungsleitfaeden/
examples/
docs/
governance/
knowledge/
compliance-register/
workflows/
prompts/
```

## Public agents

The public agent profiles are located under [`agents/public/`](agents/public/). They describe roles, boundaries, inputs, outputs, human gates, and handoffs for AI-assisted governance work.

Do not start with all agents at the same time. First use [`agents/public/anwender-routing.md`](agents/public/anwender-routing.md) and choose exactly the role needed for the next work step.

## Skills, templates, workflows, and playbooks

- [`skills/`](skills/) — repeatable AgentSkills with process, output, and quality criteria.
- [`templates/`](templates/) — working templates for registers, gaps, evidence, decisions, risks, and reviews.
- [`workflows/`](workflows/) — process models for agentic governance routines.
- [`playbooks/`](playbooks/) — concrete operating and exercise procedures.
- [`implementierungsleitfaeden/`](implementierungsleitfaeden/) — practical implementation aids, including for ISMS roles, routines, evidence, and reviews.

## Setup

krisensicherOS requires approved AI use. The setup documents help you use a suitable environment in a controlled way:

- [`docs/setup/README.md`](docs/setup/README.md) — setup selection and entry point,
- [`docs/setup/chatgpt-lokale-ide.md`](docs/setup/chatgpt-lokale-ide.md) — ChatGPT with local IDE,
- [`docs/setup/m365-copilot.md`](docs/setup/m365-copilot.md) — Microsoft 365 Copilot,
- [`docs/setup/claude-code.md`](docs/setup/claude-code.md) — Claude Code App, VS Code, and CLI,
- [`docs/setup/lokale-ki.md`](docs/setup/lokale-ki.md) — local AI without cloud.

If there is no AI usage approval, use only the approval matrix as preparation: [`templates/ki-nutzungsfreigabe-matrix.md`](templates/ki-nutzungsfreigabe-matrix.md).

## Adapters

Tool-specific adapters are located under [`adapters/`](adapters/). They explain how krisensicherOS is used in specific AI interfaces without duplicating the subject-matter source of truth:

- [`adapters/codex/`](adapters/codex/) — Codex CLI,
- [`adapters/claude-cli/`](adapters/claude-cli/) — Claude Code CLI,
- [`adapters/m365-copilot/`](adapters/m365-copilot/) — Microsoft 365 Copilot, SharePoint Agents, and Copilot Studio.

## Quick usage path

For the first robust walkthrough, there is a 30/60/90-minute path: [`docs/getting-started/30-60-90-minuten-nutzungspfad.md`](docs/getting-started/30-60-90-minuten-nutzungspfad.md).

For direct entry situations, there are also five user paths and four artifact packages:

- [`docs/getting-started/anwenderpfade.md`](docs/getting-started/anwenderpfade.md)
- [`docs/getting-started/artefaktpakete.md`](docs/getting-started/artefaktpakete.md)

For ISMS, there is a compact fictional example: [`examples/fiktiver-mittelstand/isms-90-minuten-durchstich.md`](examples/fiktiver-mittelstand/isms-90-minuten-durchstich.md).

For the NIS2 preliminary applicability check, there is a legally bounded questionnaire: [`templates/nis2-vorab-betroffenheitspruefung-fragebogen.md`](templates/nis2-vorab-betroffenheitspruefung-fragebogen.md). The result is always only a working assumption and must be reviewed by a lawyer/legal.

For NIS2 readiness in operations, [`playbooks/nis2-incident-melde-triage.md`](playbooks/nis2-incident-melde-triage.md) and [`playbooks/nis2-management-schulung-und-review.md`](playbooks/nis2-management-schulung-und-review.md) add notification/incident capability and management decisions.

## Consulting connection without blunt advertising

krisensicherOS is openly usable. Consulting becomes relevant where organizations do not need even more documents, but need support in building their own AI-assisted governance operating system:

- architecture of the governance operating model,
- prioritization under uncertainty,
- responsibility design,
- management alignment,
- crisis and tabletop exercises,
- stakeholder conflicts and internal politics,
- hardening the agentic working method.

The goal remains self-empowerment: organizations should be able to operate security governance effectively internally.

## License

krisensicherOS is available under the Apache License 2.0. See [`LICENSE`](LICENSE).
