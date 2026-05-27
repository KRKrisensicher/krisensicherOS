# A.5.22 — Monitoring and changes to supplier services

## Purpose

This routine ensures that outsourced or externally sourced services do not disappear from view after contract start. Supplier services change: scope of services, subcontractors, interfaces, locations, security evidence, service quality, or dependencies. The organization therefore needs a recurring way of working to identify changes, reassess risks, and make decisions traceably.

## Control objective in repository language

The organization operates a routine with which relevant supplier services are monitored, changes are assessed, and, where needed, transferred into risk, contract, operational, or management decisions. The goal is not supplier control for its own sake, but reliable management of critical dependencies.

## Typical risks

- If a critical service provider changes its service, platform, or subcontractors without the organization assessing this, new security or availability risks may arise.
- If service reports are only filed but not read, recurring disruptions, SLA deviations, or security gaps remain without a decision.
- If supplier changes are not connected with asset, risk, and contract data, blind spots arise in the supply chain.
- If security evidence becomes outdated, the organization relies on obsolete assumptions.
- If business function, procurement, IT, and ISMS work separately, changes are escalated too late or not at all.

## Triggers

- new, changed, or terminated supplier service.
- change to service scope, architecture, location, data processing, interfaces, or subcontractors.
- security notification, vulnerability notice, incident, SLA breach, or recurring quality problems at the supplier.
- expiry or update of security evidence, certificates, insurance, audit reports, or self-assessments.
- changed protection need of the supported business process.
- contract review, supplier review, ISMS risk review, or management question about critical dependencies.

## Roles and responsibilities

- **Service Owner / Business function:** assesses business criticality, service quality, and business impact.
- **Supplier management / Procurement:** keeps contract, contact, service, and review data up to date.
- **ISMS owner / Security role:** defines security requirements, assessment logic, and escalation criteria.
- **IT/platform owner:** assesses technical interfaces, integrations, access, and operational dependencies.
- **Legal / Data protection:** reviews contractual, data protection, or legal issues for relevant changes.
- **Management:** decides on critical dependencies, unacceptable residual risks, resource needs, or change strategy.

## Implementation

### Minimum start

Goal: make critical supplier services visible and reviewable.

1. Critical supplier services in the ISMS scope are identified.
2. Each service receives a service owner and a contract/supplier contact.
3. Minimum information is maintained for each critical service: purpose, supported process, data types, interfaces, criticality, contract term, review date.
4. Supplier changes are recorded through a simple change or review point.
5. Anomalies are referenced in the risk register or action log.
6. Open residual risks, missing evidence, or critical deviations are escalated.

Minimum evidence:

- list of critical supplier services with owner,
- last review date,
- documented supplier change or service assessment,
- open action or risk log,
- escalation or management decision for critical findings.

### Solid practice

Goal: supplier monitoring becomes risk-based, repeatable, and connected with contract management.

1. Supplier services are classified by criticality and information risk.
2. Review frequencies and minimum evidence are based on criticality.
3. Service reports, security evidence, incidents, audit findings, and performance deviations are assessed together.
4. Changes are reviewed for security, availability, and contractual impact before implementation or at the latest when they become known.
5. Exceptions or unmet requirements receive an owner, deadline, action, and follow-up date.
6. Results flow into supplier assessment, risk register, contract review, and management review.

Strong evidence:

- supplier/service register with criticality,
- review minutes with decisions,
- change assessments,
- evidence for SLA, security notifications, or audit reports,
- action log with owner and deadline,
- documented escalations or contract decisions.

### Advanced practice

Goal: critical supplier dependencies are managed as an ongoing situation picture.

1. Supplier register, asset inventory, risk register, and contract data are linked.
2. Critical service changes automatically trigger review or approval workflows.
3. Supplier risks are connected with incident management, vulnerability management, BCM, and exit planning.
4. Subcontractors, concentration risks, and regional dependencies are reviewed regularly.
5. Management receives decision-ready metrics: critical services without current review, open supplier actions, recurring SLA deviations, overdue evidence, high dependencies.

## Routine flow

1. **Identify service or change:** through supplier notification, contract review, service report, business function, incident, or procurement.
2. **Determine scope:** affected process, data, systems, interfaces, locations, and user groups.
3. **Review criticality:** assess business impact, protection need, dependency, and alternatives.
4. **Assess change:** classify security, availability, data protection, contractual, and operational consequences.
5. **Make decision:** accept, set conditions, plan action, trigger escalation, or adapt service.
6. **File evidence:** document review, assessment, decision, and actions traceably.
7. **Track:** review open points through to closure and escalate delays.
8. **Learn:** feed patterns from disruptions, changes, or supplier problems back into procurement and contract design.

## Decisions

- Which supplier services are critical enough for regular monitoring?
- Which changes may suppliers implement without prior approval, and which may they not?
- Which evidence is accepted, and when is it too old or too weak?
- When does a supplier deviation become a risk, incident, contractual problem, or management topic?
- Which exceptions are tolerable for a limited time?
- When does the organization need an exit plan, second provider, or technical compensation?

## Evidence

### Strong evidence

- current register of critical supplier services with owner and criticality,
- review minutes with concrete decisions,
- change assessments before or after supplier change,
- evidence of tracked supplier actions,
- linked risk or action register entries,
- management decision for critical dependency or residual risk.

### Weak evidence

- general supplier list without criticality,
- filed certificates without review date or scope reference,
- contractual clauses without operational routine,
- service reports without assessment,
- generic statement “secured by the provider” without evidence.

### Evidence gaps

- no owners for critical supplier services,
- unknown subcontractors or interfaces,
- no assessment of supplier changes,
- overdue security evidence,
- open supplier deviations without deadline or decision,
- critical dependencies without exit or escalation logic.

## Effectiveness review

Review questions:

- Are critical supplier services captured completely and with owners?
- Are changes to service, platform, subcontractors, or security evidence identified?
- Can service reports or supplier notifications be traced back to decisions and actions?
- Are recurring deviations or missing evidence escalated?
- Are risks and actions connected with the ISMS risk register?
- Does management recognize critical concentration or exit risks?

Possible metrics:

- share of critical supplier services with current review,
- overdue supplier evidence,
- open supplier actions by criticality,
- recurring SLA or security deviations,
- critical services without exit consideration,
- time to complete a supplier change assessment.

## BSIG/NIS2 connection point

The routine is a connection point for NIS2-oriented topics such as supply chain security, risk management, management of external services, business continuity, and incident capability. For affected organizations, the concrete connection should be assessed in the requirements register, risk register, and supplier management.

This artifact does not replace legal assessment of duties, contracts, data protection questions, or reporting requirements.

## Boundaries

- No legal, contractual, or data protection advice.
- No statement that a supplier is secure or conformant through individual pieces of evidence.
- No adoption of licensed standard texts or certification commitment.
- No assessment of real suppliers or confidential contract data in public examples.
- No replacement for technical review, incident response, BCM, or exit planning.

## Handoffs

- **Procurement/vendor handoff:** contract change, supplier review, missing evidence, service deviation.
- **Legal/data protection handoff:** change to data processing, locations, subcontractors, contract clauses, or proximity to reporting duties.
- **IT/architecture handoff:** new interfaces, technical integrations, platform change, or access expansion.
- **Incident handoff:** security notification, suspicion of compromise, service disruption with security relevance.
- **BCM handoff:** critical dependency, missing fallback option, exit or emergency need.
- **Management handoff:** high residual risk, provider change, budget need, strategic dependency.
- **Audit/evidence handoff:** missing or weak evidence for review, decision, or action tracking.

## Typical mistakes

- Suppliers are reviewed only during onboarding and no longer managed afterwards.
- Certificates are collected but not checked for scope, currency, or relevance.
- Business functions learn about changes, but ISMS, procurement, or IT do not.
- SLA problems are handled operationally without risk or contract decision.
- Subcontractors and technical interfaces remain outside the review.
- Open supplier actions have no owner or due date.
- Management receives lists, but no decision-ready dependencies.

## Fictional mini example

A fictional SaaS provider announces that it will move part of its operation to a new platform. The business function reports the change to procurement and ISMS. The service owner reviews affected processes and data, the IT owner assesses interfaces, and data protection and Legal clarify points that require review. Until clarification, a time-limited action is documented: additional review of admin access and an updated exit note. The result is recorded in the supplier review.

Evidence:

- supplier notification,
- change assessment,
- updated register entry,
- action log with owner and deadline,
- review decision on continued use.
