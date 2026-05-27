# Changelog

All relevant changes to krisensicherOS are documented here.

This project follows a simple, human-readable changelog. Before the first public release, structure and content may still change.

## Unreleased

- ISMS implementation guide added: modules for use/boundaries, scope, roles, risk steering, safeguards, competence/evidence, operations, suppliers, incidents, management review, and internal checks. Product text references ISO/IEC 27001 and relevant BSIG/NIS2 anchors without reproducing standard texts.
- ISO/IEC 27001 requirements map added: section references are translated into krisensicherOS language as routines, decision points, evidence trails, reviews, and human gates; without reproducing standard text.
- User usability sharpened: getting-started navigation, user paths, artifact packages, ISMS 90-minute walkthrough, and reduced agent routing added; mid-sized organization CISO QA performed and should-fixes implemented.
- EU AI Act readiness starter added: AI system inventory, preliminary assessment workflow, getting-started path, and handoff logic without legal or compliance assurance.

### Added

- Adapter navigation added under `07-ai-governance-agents/adapters/`.
- Claude CLI adapter added with source-of-truth rules, Claude CLI command usage, project configuration boundaries, and QA gate.
- Microsoft 365 Copilot adapter for SharePoint Agents and Copilot Studio added, including knowledge source boundaries, human gates, and SharePoint Agent Instructions.
- NIS2 primary source anchors, recitals evaluation, preliminary applicability questionnaire, workflow, and agent `nis2-scope-precheck-analyst` added; result enforces lawyer/legal review.
- NIS2 incident/notification triage playbook added with 24h/72h/final logic, plus executive management training and management review routine.

### Changed

- Product repository cleaned up: build and translation infrastructure removed from the visible product structure; quality gate now runs directly in GitHub Actions.
- Mid-sized organization CISO should-findings implemented: module READMEs `01`, `03`, `04`, `06` sharpened with entry points, human gates, outputs, and operating flow; `08` catalogs made clickable and grouped by module; `09` roadmap labeled as product/release roadmap.
- Product structure cleaned up: domain artifacts moved from loose root collection folders into the numbered `01` to `09` areas; the repository root stays slim, catalogs and the quality gate were adjusted.
- Product positioning sharpened: krisensicherOS is a repo for AI-assisted security governance and requires approved AI usage.
- Setup documentation focused on approved AI environments: ChatGPT, Microsoft 365 Copilot, Claude Code, and local AI.
- Approval path clarified as a side note: if no AI usage approval exists yet, the approval matrix is only used for preparation; productive use stops.
- Internal working, review, persona, roadmap, briefing, release, and queue artifacts removed from the product repo.
- `AGENTS.md` made runtime-clean and aligned with public agent profiles.
- README, getting-started, and setup documentation consistently aligned with AI usage approval, human gates, and product boundaries.
- GitHub Actions quality gate hardened: product boundaries, runtime markers, secret indicators, and local Markdown links are checked.

### Security / Governance

- No publication, no push, no tag, and no external transmission without explicit approval.
- AI usage remains bound to data class, tool approval, operational responsibility, and human gates.
- Redaction tools are only protective layers, not an anonymization guarantee, data protection assessment, or compliance evidence.
- Legal advice, data protection advice, compliance, certification, and security assurances remain excluded.
- Licensed standard texts, confidential contract content, personal data, customer data, and secrets remain hard stop points.

## v1.0.0-rc.1 — prepared

### Added

- 5-artifact quick start for the smallest useful NIS2 walkthrough.
- 30/60/90-minute usage path for the first krisensicherOS walkthrough.
- Setup guides for approved AI working environments.
- Public agent profiles under `07-ai-governance-agents/agents/public/`.
- Agent role model and manifest for compliance and security governance work.
- Skills for governance operating model, NIS2 gap assessment, ISMS, audit, evidence requests, corrective actions, management reviews, and tabletop exercises.
- Templates for registers, gaps, evidence, decisions, risks, findings, measures, reviews, and AI usage approval.
- Workflows for governance operating model, NIS2 readiness, ISMS, evidence management, and audit/remediation chains.
- Fixed public reference source structure under `01-orientation/knowledge-sources/`.
- Compliance register structure under `02-governance-operating-model/compliance-register/`.
- Note on license-compliant use of ISO standards and comparable standards.
- Empowerment-first prompt library.

### Changed

- README sharpened for v1.0 navigation, product boundaries, and AI-assisted entry.
- Product guardrail `01-orientation/product-positioning/was-wir-bewusst-nicht-bauen.md` added: no false compliance, no standard text replication, no template overload, and no AI magic without human gates.
- Standards/AI license boundaries sharpened in README and legal documentation: no standard documents in repo, prompts, RAG, embeddings, or AI systems without a suitable license.
- Mid-sized organization case study sharpened around the end-to-end chain from gap to evidence request, corrective action, effectiveness check, and management decision.

### Security / Governance

- Apache 2.0 license added.
- Governance, review, and quality rules added.
- Claims, licensed standard texts, personal data, and confidential content defined as hard stop points.
