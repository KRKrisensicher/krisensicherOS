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

## Vibe Governance

Just as **vibe coding** describes how people use AI to move faster from an idea to working code, **Vibe Governance** describes the next step for organizations: treating governance not as a static documentation project, but as an AI-assisted workflow of questions, roles, evidence, decisions, and reviews.

In krisensicherOS, Vibe Governance does not mean automating away responsibility or claiming compliance from prompts. It means using AI to reach useful drafts, sharper review questions, visible gaps, and decision-ready handoffs faster — while human gates, professional accountability, and organization-specific approvals remain explicit.

The “vibe” is not arbitrariness. It is the working speed and clarity that emerge when agents do the preparation and humans operate governance deliberately.

## Why this repository exists

krisensicherOS is based on a simple conviction: organizations should be able to operate management systems meaningfully themselves. Good governance is not created by consultants writing documents that add no value inside the organization. It is created when management system owners prioritize the important topics, speak with people across the organization, prepare decisions, and operate routines.

Many software tools distract from what matters most: management. krisensicherOS therefore does not start with tool screens, but with roles, conversations, evidence, reviews, escalations, and management decisions.

Management system owners in particular should use AI productively: first, so they can advise their organization on AI governance from practical experience; second, so efficiency gains become possible where management systems otherwise create mainly cost but too little output.

**Clarification:** Without an approved AI environment, krisensicherOS is not a meaningful operating mode. Organizations can read individual templates or prepare AI usage approval, but the product value comes from AI-assisted work with human gates.

## Start in 15 minutes

1. Give this repository to an approved AI environment or open it in an approved AI-enabled work context.
2. Tell the AI which management-system topic you want to work on, such as NIS2, ISMS, evidence review, incident readiness, or EU AI Act readiness.
3. Let the AI clarify the open questions with you: scope, data class, AI usage approval, roles, human gates, existing evidence, and the next useful work step.
4. If you want to start manually, open [`01-orientation/getting-started/README.md`](01-orientation/getting-started/README.md) and choose a user path.
5. For the smallest NIS2 start, use the [`5-artifact quick start`](01-orientation/getting-started/minimaler-nis2-start-in-5-artefakten.md).

## Five quick user paths

- **Start NIS2:** Scope, register entry, gap, evidence requests, and decision log handoff.
- **Start ISMS:** Scope, risks, control routines, evidence pack, and review date.
- **Build evidence/management review:** Bundle evidence and prepare management decisions.
- **Practice incident/notification readiness:** Train escalation, triage, and human gates.
- **Start EU AI Act readiness:** Inventory AI systems, flag role questions, and prepare legal/data protection/management handoffs.

Details are in [`01-orientation/getting-started/anwenderpfade.md`](01-orientation/getting-started/anwenderpfade.md).

## Minimal start sequence

1. Choose a path or package from [`01-orientation/getting-started/`](01-orientation/getting-started/README.md).
2. Check AI usage approval with [`07-ai-governance-agents/templates/ki-nutzungsfreigabe-matrix.md`](./07-ai-governance-agents/templates/ki-nutzungsfreigabe-matrix.md).
3. Choose exactly one approved AI environment from [`01-orientation/setup/README.md`](01-orientation/setup/README.md).
4. Use no more than one artifact package from [`01-orientation/getting-started/artefaktpakete.md`](01-orientation/getting-started/artefaktpakete.md).
5. Mark human gates for management, risk acceptance, legal, data protection, and external communication.

## Mission

krisensicherOS helps translate compliance work into roles, routines, evidence, and management decisions.

Product guardrail: krisensicherOS builds only components that increase decision readiness, evidence flow, or operating routine. Anything that only creates more documents, consultant optics, or apparent compliance stays out. See [`01-orientation/product-positioning/was-wir-bewusst-nicht-bauen.md`](01-orientation/product-positioning/was-wir-bewusst-nicht-bauen.md).

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

Important: Licensed standards such as ISO/IEC 27001 are not included in the repository as standard text. The repository provides only metadata, mapping, and working structures. See [`01-orientation/legal-boundaries/iso-normen-lizenzkonform-nutzen.md`](01-orientation/legal-boundaries/iso-normen-lizenzkonform-nutzen.md).

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

The numbered folders are the primary product structure. Domain content, templates, playbooks, workflows, examples, and agent components live where they are used operationally. The repository root intentionally stays slim and contains only entry points, license, security/contribution rules, and technical infrastructure.

```text
01-orientation/                    # onboarding, setup, boundaries, sources
02-governance-operating-model/     # roles, registers, decisions, governance rules
03-nis2-readiness/                 # NIS2 pre-check, gap, management and notification readiness
04-isms-basics/                    # ISMS setup, risk, controls, implementation guides
05-incident-crisis-readiness/      # incident, BCMS, escalation, exercises
06-evidence-management-review/     # evidence, audit, remediation, management review
07-ai-governance-agents/           # agents, skills, adapters, prompts, AI governance
08-templates-playbooks/            # cross-cutting catalogs and reusable components
09-implementation-roadmaps/        # examples, roadmaps, and implementation walkthroughs
.github/                           # GitHub quality gate and Dependabot
scripts/                           # local QA and build helpers
i18n/                              # language/glossary support
```

## Public agents

The public agent profiles are located under [`07-ai-governance-agents/agents/public/`](07-ai-governance-agents/agents/public/). They describe roles, boundaries, inputs, outputs, human gates, and handoffs for AI-assisted governance work.

Do not start with all agents at the same time. First use [`07-ai-governance-agents/agents/public/anwender-routing.md`](07-ai-governance-agents/agents/public/anwender-routing.md) and choose exactly the role needed for the next work step.

## Skills, templates, workflows, and playbooks

- [`07-ai-governance-agents/skills/`](07-ai-governance-agents/skills/) — repeatable AgentSkills with process, output, and quality criteria.
- [`08-templates-playbooks/catalogs/templates.md`](./08-templates-playbooks/catalogs/templates.md) — working templates for registers, gaps, evidence, decisions, risks, and reviews.
- [`workflows/`](./08-templates-playbooks/catalogs/workflows.md) — process models for agentic governance routines.
- [`playbooks/`](./08-templates-playbooks/catalogs/playbooks.md) — concrete operating and exercise procedures.
- [`04-isms-basics/implementation-guides/`](04-isms-basics/implementation-guides/) — practical implementation aids, including for ISMS roles, routines, evidence, and reviews.

## Setup

krisensicherOS requires approved AI use. The setup documents help you use a suitable environment in a controlled way:

- [`01-orientation/setup/README.md`](01-orientation/setup/README.md) — setup selection and entry point,
- [`01-orientation/setup/chatgpt-lokale-ide.md`](01-orientation/setup/chatgpt-lokale-ide.md) — ChatGPT with local IDE,
- [`01-orientation/setup/m365-copilot.md`](01-orientation/setup/m365-copilot.md) — Microsoft 365 Copilot,
- [`01-orientation/setup/claude-code.md`](01-orientation/setup/claude-code.md) — Claude Code App, VS Code, and CLI,
- [`01-orientation/setup/lokale-ki.md`](01-orientation/setup/lokale-ki.md) — local AI without cloud.

If there is no AI usage approval, use only the approval matrix as preparation: [`07-ai-governance-agents/templates/ki-nutzungsfreigabe-matrix.md`](./07-ai-governance-agents/templates/ki-nutzungsfreigabe-matrix.md).

## Adapters

Tool-specific adapters are located under [`07-ai-governance-agents/adapters/`](07-ai-governance-agents/adapters/). They explain how krisensicherOS is used in specific AI interfaces without duplicating the subject-matter source of truth:

- [`07-ai-governance-agents/adapters/codex/`](./07-ai-governance-agents/adapters/codex) — Codex CLI,
- [`07-ai-governance-agents/adapters/claude-cli/`](./07-ai-governance-agents/adapters/claude-cli) — Claude Code CLI,
- [`07-ai-governance-agents/adapters/m365-copilot/`](./07-ai-governance-agents/adapters/m365-copilot) — Microsoft 365 Copilot, SharePoint Agents, and Copilot Studio,
- [`07-ai-governance-agents/adapters/orgavision-mcp/`](./07-ai-governance-agents/adapters/orgavision-mcp) — Orgavision MCP as an optional distribution and knowledge-access path for approved governance artifacts.

## Quick usage path

For the first robust walkthrough, there is a 30/60/90-minute path: [`01-orientation/getting-started/30-60-90-minuten-nutzungspfad.md`](01-orientation/getting-started/30-60-90-minuten-nutzungspfad.md).

For direct entry situations, there are also five user paths and four artifact packages:

- [`01-orientation/getting-started/anwenderpfade.md`](01-orientation/getting-started/anwenderpfade.md)
- [`01-orientation/getting-started/artefaktpakete.md`](01-orientation/getting-started/artefaktpakete.md)

For ISMS, there is a compact fictional example: [`09-implementation-roadmaps/examples/fiktiver-mittelstand/isms-90-minuten-durchstich.md`](09-implementation-roadmaps/examples/fiktiver-mittelstand/isms-90-minuten-durchstich.md).

For the NIS2 preliminary applicability check, there is a legally bounded questionnaire: [`templates/nis2-vorab-betroffenheitspruefung-fragebogen.md`](./03-nis2-readiness/templates/nis2-vorab-betroffenheitspruefung-fragebogen.md). The result is always only a working assumption and must be reviewed by a lawyer/legal.

For NIS2 readiness in operations, [`playbooks/nis2-incident-melde-triage.md`](./03-nis2-readiness/playbooks/nis2-incident-melde-triage.md) and [`playbooks/nis2-management-schulung-und-review.md`](./03-nis2-readiness/playbooks/nis2-management-schulung-und-review.md) add notification/incident capability and management decisions.

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
