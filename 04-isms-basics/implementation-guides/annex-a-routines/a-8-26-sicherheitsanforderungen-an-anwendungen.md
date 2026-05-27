# A.8.26 — Security requirements for applications

## Purpose

Security requirements for applications ensure that applications not only work functionally, but also handle identities, data, interfaces, errors, logging, availability and abuse scenarios appropriately.

The core is an early, reviewable requirements routine: Which security needs arise from use, data, exposure and business process — and how are they tracked in specification, backlog, acceptance and operation?

## Control objective in repository language

The organization defines, prioritizes and reviews security requirements for applications on a risk basis. Requirements are formulated so that Product Owner, development, architecture, testing and operations can understand, implement, accept and reassess them when changes occur.

## Typical risks

- If security requirements are not defined early, the development team implicitly decides on protection needs and risk.
- If requirements are too generic, features are created without reviewable acceptance criteria.
- If authentication, authorization, session handling or logging remain unclear, unauthorized access or missing traceability can arise.
- If interfaces, data flows and error cases are not considered, data leakage, manipulation opportunities or unstable services can arise.
- If legal, contractual or customer expectations are translated into technical requirements without review, false commitments or gaps arise.
- If requirements are not updated after changes, security assumptions become outdated.

## Triggers

- new application, new module, new interface or material functional change.
- processing of new data classes, new tenants, new user roles or external access.
- change to architecture, platform, authentication, authorization model or logging.
- new risk, vulnerability, incident, audit finding or customer requirement.
- tendering, procurement or adaptation of standard software or SaaS application.
- release planning, acceptance decision or handover to operations.
- regular review of critical applications and their security requirements.

## Roles and responsibilities

- **Product Owner / Business unit:** describes business process, protection need, user roles, abuse impacts and acceptance criteria.
- **Development team:** translates requirements into technical implementation and makes feasibility visible.
- **Architecture role:** reviews data flows, interfaces, trust boundaries and technical dependencies.
- **Security role / AppSec role:** supports security requirements, threat scenarios, prioritization and testability.
- **Test/QA role:** tracks security requirements in test cases, acceptance criteria and findings.
- **IT operations / Platform team:** names operational requirements such as monitoring, logging, backup, patchability and configuration.
- **Data protection / Legal:** reviews personal data, contractual commitments, retention, logging and regulatory questions.
- **Management:** decides in conflicts between functional scope, schedule, cost and security risk.

## Implementation

### Minimum start

Objective: critical security requirements become visible before implementation and release.

1. For each relevant application, owners, user groups, data classes and exposure are described.
2. A short requirements catalog is used: access, roles/rights, data flow, inputs, error cases, logging, availability, interfaces, operational handover.
3. Security requirements are recorded as tickets, acceptance criteria or acceptance points.
4. Requirements with data protection, contractual or risk impact receive a human-review handoff.
5. Before release, it is checked which requirements are fulfilled, open, compensated or accepted.

Minimum evidence:

- application scope with owner,
- security requirements in backlog or specification,
- acceptance criteria or test cases,
- review note on open requirements,
- decision on deviation or residual risk.

### Solid practice

Objective: security requirements are steered on a risk basis, repeatably and testably.

1. Applications are prioritized by criticality, data, exposure and business process.
2. Standard requirements are maintained for typical topics: identity, authorization, input validation, cryptography, logging, interfaces, fault tolerance, tenant separation, secrets, operation.
3. For critical applications, abuse cases or threat scenarios are translated into requirements.
4. Requirements include acceptance criteria, test path and responsible role.
5. Changes to data, roles, interfaces or platform trigger a requirements review.
6. Open requirements are tracked in the risk register, action log or technical debt backlog.
7. Procured applications and SaaS are included through security requirements, supplier evidence and acceptance.

Strong evidence:

- application criticality and protection-need note,
- risk-based security requirements catalog,
- tickets with acceptance criteria,
- test and acceptance records,
- change review for relevant releases,
- exception or risk decision,
- supplier responses or acceptances for third-party applications.

### Advanced practice

Objective: security requirements are used as a living part of product steering, architecture and operation.

1. Requirements building blocks are integrated into templates, Definition of Ready/Done, architecture decisions and test management.
2. Threat modeling, data protection review and operational requirements are coordinated for critical applications without mixing responsibilities.
3. Automated tests and pipeline gates continuously check selected requirements.
4. Product metrics show open security requirements, exception rates, recurring requirements errors and release blockers.
5. Requirements are updated after incidents, vulnerabilities, customer feedback and platform changes.
6. Management receives a decision-ready view of risks, not only fulfillment rates.

## Routine flow

1. **Application need arises:** new product, change, procurement or release.
2. **Record context:** describe users, data, interfaces, exposure, criticality and operating model.
3. **Derive security requirements:** select standard requirements and add risk-specific requirements.
4. **Clarify testability:** define acceptance criteria, test cases and acceptance points.
5. **Plan implementation:** include requirements in backlog, specification or supplier requirement.
6. **Perform review:** involve Security, architecture, data protection/legal or operations when triggers apply.
7. **Decide acceptance:** document fulfilled, open, compensated and accepted requirements.
8. **Observe operation:** feed incidents, findings and changes back into requirements.
9. **Improve:** adapt requirements catalog, templates and test cases.

## Decisions

- Which applications need full security requirements and which only minimum requirements?
- Which requirements are release blockers?
- Who decides if a requirement is not implemented for technical or economic reasons?
- Which requirements belong in contracts or supplier acceptances?
- Which requirements require data protection, legal or management review?
- How are security requirements prioritized against functional, schedule and budget pressure?

## Evidence

### Strong evidence

- application list with owner, criticality and data classes,
- security requirements with acceptance criteria,
- risk or threat scenarios as rationale,
- review and acceptance records,
- test evidence for security requirements,
- documented deviations with deadline and decision,
- updated requirements after change or incident.

### Weak evidence

- blanket statement “application must be secure”,
- generic catalog without relation to the application,
- specification without security acceptance criteria,
- test record without connection to requirements,
- supplier statement without review question, evidence or acceptance decision.

### Evidence gaps

- no owners for applications or requirements,
- no mapping between data class and security requirement,
- open security requirements without release decision,
- interfaces and role model not described,
- requirements become outdated after architecture or process changes.

## Effectiveness review

Review questions:

- Are security requirements visible before implementation and not only at acceptance?
- Are requirements formulated testably and assigned to an owner?
- Are data class, exposure, user roles and interfaces considered?
- Can open requirements be assigned to a decision or action?
- Are requirements updated after incidents, vulnerabilities and changes?
- Are third-party applications and SaaS included in the requirements routine?

Possible metrics:

- share of critical applications with current security requirements,
- open security requirements per release,
- requirements without acceptance criterion,
- exceptions and overdue follow-ups,
- recurring findings from missing requirements,
- third-party applications with documented security acceptance.

## BSIG/NIS2 connection point

Security requirements for applications are a connection point for NIS2-oriented topics such as risk management, secure development, secure procurement, vulnerability management, cyber hygiene and protection of digital services. The concrete relationship should be assessed in an organization-specific way through requirements register, risk analysis and human review.

This artifact is not legal advice and confirms no legal applicability or conformity.

## Boundaries

- This artifact is not a complete technical requirements catalog.
- It does not replace a data protection impact assessment, legal review or contract review.
- It does not guarantee a secure application or certifiability.
- It contains no ISO 27002 texts and no confidential customer requirements.
- It does not replace security tests, code reviews or architecture reviews.

## Handoffs

- **Architecture handoff:** new interfaces, trust boundaries, tenant separation, platform change or critical data flows.
- **Data protection/legal handoff:** personal data, logging, retention, contractual commitments, international use or customer requirements.
- **Test handoff:** requirements need concrete test cases, acceptance criteria or penetration test scope.
- **Operations handoff:** logging, monitoring, backup, patchability, configuration and support model.
- **Supplier handoff:** standard software, SaaS, external development or missing evidence.
- **Management handoff:** release blockers, schedule/security conflicts, accepted residual risk or resource need.

## Typical mistakes

- Security requirements are derived only from test findings.
- Requirements remain abstract and are not testable.
- The business unit describes functions, but no abuse or damage scenarios.
- Third-party applications are introduced without formulating security requirements.
- Data protection, operational and security requirements are brought together too late.
- Open requirements disappear in the backlog without a risk decision.
- Requirements are not reviewed after changes.

## Fictional mini example

A fictional company plans a self-service application for business customers. In the requirements workshop, user roles, tenant separation, password reset, logging of security-relevant actions and API access are recorded as security requirements. QA adds test cases, architecture reviews the data flows, data protection assesses the logging. Before release, a logging dashboard remains open; the Product Owner documents a time-limited action and files the decision in the release record.

Evidence:

- application scope with data classes,
- security requirements with acceptance criteria,
- architecture and data protection review,
- test cases and test results,
- release record with open action.
