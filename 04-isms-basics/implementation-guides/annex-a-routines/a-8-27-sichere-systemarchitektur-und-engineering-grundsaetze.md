# A.8.27 — Secure system architecture and engineering principles

## Purpose

Secure system architecture and engineering principles ensure that systems do not have to become secure by chance. Security principles are anchored in architecture decisions, platform standards, integrations, operating models and technical guardrails.

The core is an architecture and engineering routine: critical systems are designed, reviewed and improved along clear principles before insecure structures become difficult to correct in operation.

## Control objective in repository language

The organization uses traceable security principles for the design, change and operation of systems. Architecture decisions make trust boundaries, data flows, identities, dependencies, segmentation, failure scenarios, monitoring and maintainability visible and decidable.

## Typical risks

- If architecture decisions are made without security principles, structural weaknesses that are difficult to remediate arise.
- If trust boundaries and data flows are unclear, access, interfaces and logging can be designed incorrectly.
- If complexity grows uncontrolled, errors, dependencies and operational risks become invisible.
- If security requirements are implemented only as individual measures, robust system principles such as limitation of rights, separation, robustness and observability are missing.
- If legacy exceptions are not steered, technical debt permanently becomes a security risk.
- If cloud, platform or supplier architectures are not reviewed, blind spots arise outside own operations.

## Triggers

- new system, new platform, new application or new integration architecture.
- major change to network, cloud, identity, data storage, multi-tenancy or interfaces.
- introduction of external services, managed services, APIs or development platforms.
- security event, vulnerability pattern, penetration test or audit finding.
- migration, modernization, replacement or decommissioning.
- recurring operational disruptions, scaling problems or technical debt.
- periodic architecture review of critical systems.

## Roles and responsibilities

- **Architecture role / Enterprise or Solution Architect:** leads architecture decisions, principles and reviews.
- **System Owner / Service Owner:** responsible for protection need, business risk and prioritization.
- **Tech Lead / Engineering team:** technically implements architecture and engineering decisions.
- **Security role:** assesses security principles, risks, deviations and control needs.
- **Platform/cloud/network team:** provides technical guardrails, baselines and operational capabilities.
- **IT operations:** assesses maintainability, monitoring, backup, patchability and incident readiness.
- **ISMS Owner:** connects architecture decisions with risk register, actions and management review.
- **Management:** decides in conflicts, technical debt, high migration costs or accepted residual risks.

## Implementation

### Minimum start

Objective: critical architecture decisions become visible and are reviewed from a security perspective.

1. The organization names critical systems, platforms and integrations in scope.
2. For these systems, owners, data flows, external interfaces and central dependencies are described.
3. A short set of engineering principles is agreed, for example least privilege, clear trust boundaries, secure defaults, traceability, maintainability and failure scenarios.
4. New or changed critical architectures receive a security review before implementation or go-live.
5. Deviations are documented with rationale, risk, compensation and follow-up.

Minimum evidence:

- list of critical systems and integrations,
- architecture overview or data flow diagram,
- documented engineering principles,
- review note on architecture decisions,
- exception or action log.

### Solid practice

Objective: architecture and engineering are steered repeatably on a risk basis.

1. Architecture decisions are documented as Architecture Decision Records or comparable short decision notes.
2. Reviews consider identities, authorizations, segmentation, data flows, cryptography needs, logging, operational readiness, backup, resilience and supplier dependencies.
3. Platform standards and secure reference patterns reduce individual decisions.
4. Critical deviations are tracked in risk or debt registers.
5. Architecture reviews are connected with security requirements, development, change management and vulnerability management.
6. Recurring findings trigger adaptations to standards, templates or platform guardrails.
7. Management receives transparency about major technical debt and accepted architecture residual risks.

Strong evidence:

- architecture principles and reference patterns,
- system and data flow documentation,
- Architecture Decision Records,
- review minutes with decisions,
- action log for deviations,
- risk decisions on technical debt,
- evidence of adapted platform or engineering standards.

### Advanced practice

Objective: secure architecture is supported by platforms, automation and continuous review.

1. Security principles are embedded in cloud policies, infrastructure templates, CI/CD gates, network zones and identity platforms.
2. Critical architecture decisions use threat modeling, resilience analyses or attack-surface views.
3. Architecture and operational data provide indicators on exposure, dependencies, technical debt and control gaps.
4. Reference architectures and self-service platforms make secure paths easier than insecure special solutions.
5. Legacy and exception architectures are managed with target state, migration path and management decision.
6. Architecture lessons learned from incidents, tests and audits actively change standards and guardrails.

## Routine flow

1. **Architecture trigger arises:** new system, change, migration, external integration or finding.
2. **Record context:** capture purpose, data, users, interfaces, dependencies, exposure and operating model.
3. **Apply principles:** review trust boundaries, least privilege, separation, secure defaults, observability and maintainability.
4. **Assess risks:** classify structural weaknesses, dependencies, legacy components and failure scenarios.
5. **Document decision:** record chosen architecture, alternatives, residual risks and open actions.
6. **Accompany implementation:** include technical guardrails, platform standards and reviews in implementation and change.
7. **Validate:** review tests, operational handover, monitoring, vulnerability findings or architecture acceptance.
8. **Steer deviations:** time-limit, compensate, escalate or transfer into a migration plan.
9. **Improve standards:** feed patterns from findings back into reference architecture and engineering principles.

## Decisions

- Which systems need an architecture security review?
- Which engineering principles are mandatory and which are target state?
- Which deviations are tolerable and who accepts them?
- When is technical debt a management risk?
- Which platform standards should relieve teams?
- When must a legacy architecture be replaced instead of compensated?

## Evidence

### Strong evidence

- current architecture and data flow overviews of critical systems,
- documented security and engineering principles,
- review or decision records,
- Architecture Decision Records with security reference,
- evidence on segmentation, identity model, logging, backup or monitoring,
- actions and target dates for deviations,
- management decisions on technical debt or residual risks.

### Weak evidence

- outdated architecture diagram without owner or date,
- general principles slide without application to systems,
- tool configuration without documented architecture decision,
- review with open points without follow-up,
- statement “cloud provider handles security” without clarification of responsibility.

### Evidence gaps

- no overview of critical data flows or interfaces,
- no documented trust boundaries,
- technical debt without risk or migration decision,
- deviations without expiry date,
- missing operational requirements in architecture decisions,
- supplier or platform dependencies without owner.

## Effectiveness review

Review questions:

- Are critical systems described traceably with architecture, owners and data flows?
- Are security principles applied to new and changed architectures?
- Do reviews lead to concrete decisions, actions or exceptions?
- Are technical debt and legacy risks transparent and prioritized?
- Are recurring findings translated into architecture standards?
- Are cloud, platform and supplier dependencies visible in the architecture?

Possible metrics:

- share of critical systems with current architecture review,
- open architecture deviations by criticality,
- technical debt with management decision,
- recurring architecture findings,
- systems without current data flow overview,
- exception rate for reference architectures.

## BSIG/NIS2 connection point

Secure system architecture and engineering principles are a connection point for NIS2-oriented topics such as risk management, protection of digital services, secure development, business continuity, supply chain security, vulnerability management and cyber hygiene. The concrete relationship should be assessed in the requirements register and in risk and management reviews in an organization-specific way.

This artifact does not replace legal review or a technical security assurance.

## Boundaries

- This artifact is not a complete reference architecture and not a technical hardening baseline.
- It does not replace detailed cloud, network, product or resilience review.
- It makes no statement on certifiability or legal conformity.
- It contains no ISO 27002 texts and no confidential architecture details.
- It does not replace human decision-making on target architecture, migration or risk acceptance.

## Handoffs

- **Development handoff:** architecture decisions must be implemented in backlog, code, tests and release gates.
- **Operations handoff:** clarify monitoring, backup, patchability, restart, logging and support model before handover.
- **Cloud/platform handoff:** landing zones, infrastructure templates, identity, network zones and technical guardrails.
- **Data protection/legal handoff:** personal data flows, retention, logging, tenant separation or contractual commitments.
- **Supplier handoff:** external platforms, managed services, proprietary dependencies or unclear responsibilities.
- **BCM/crisis handoff:** architecture decisions with effects on availability, restart or critical processes.
- **Management handoff:** major technical debt, migration need, non-compensable risks or conflicts.

## Typical mistakes

- Architecture reviews take place only for large projects, not for risky small changes.
- Diagrams are maintained, but decisions and risks are not documented.
- Security principles are known, but not translated into platforms or templates.
- Legacy exceptions become permanent because no target state exists.
- Operational requirements become visible only after go-live.
- Supplier and cloud responsibilities remain implicit.
- Management receives technical details, but no clear risk or investment decision.

## Fictional mini example

A fictional industrial company migrates an internal application to a cloud environment. The architecture review shows new external interfaces, a changed identity model and higher monitoring requirements. The team documents the decision, uses an approved network and identity template and creates a time-limited exception for a legacy protocol. In the management review, it is decided to replace the legacy component within six months.

Evidence:

- architecture and data flow overview,
- documented architecture decision,
- review minutes with security principles,
- platform template as implementation evidence,
- exception with migration target,
- management decision on replacement.
