# A.8.30 — Managing outsourced development

## Purpose

Outsourced development provides speed and specialist knowledge, but it can make security responsibility, architecture decisions and evidence unclear. This routine ensures that external development work is not only commissioned contractually, but is professionally steered, security-reviewed and accepted in a way that can produce evidence.

The core is not “a service provider has been commissioned”, but: Which development services are external? Which security requirements apply? Who reviews results? How are code, components, access, test data, vulnerabilities and acceptance controlled?

## Control objective in repository language

The organisation operates a traceable steering routine for outsourced development. It connects procurement, product ownership, secure development, access protection, supplier evidence, change control, acceptance and risk decisions.

## Typical risks

- If external developers work without clear security requirements, insecure architecture, insecure components or missing evidence may result.
- If source code, build pipelines or repositories are externally accessible, excessive privileges, unclear ownership or data leakage may occur.
- If security reviews only take place at acceptance, fundamental design flaws become visible late and at high cost.
- If service providers use their own subcontractors, responsibilities, access paths and confidentiality may become unclear.
- If findings from code review, tests or penetration tests are not tracked contractually and operationally, risks move into production.
- If knowledge and documentation remain with the service provider, dependency arises for operations, maintenance and incident response.

## Triggers

- new development project with an external share.
- extension, maintenance or operation of an externally developed application.
- supplier change, new subcontractors or changed delivery model.
- access to repositories, CI/CD, development environments, test data or production-like information.
- security-relevant architecture, technology or component decision.
- vulnerability, audit finding, incident or acceptance problem related to external development.
- contract renewal, project completion or handover into operations.

## Roles and responsibilities

- **Product Owner / Client:** defines functional scope, acceptance criteria and priorities.
- **Development lead / architecture role:** reviews design, code quality, technical debt and handover readiness.
- **Security role / ISMS Owner:** defines security requirements, review points, evidence logic and escalation.
- **IT / Platform Owner:** controls repositories, access, build/deploy pipelines and technical integration.
- **Procurement / Vendor Management:** anchors requirements, evidence, subcontractor logic and exit topics in the supplier process.
- **Data Protection / Legal:** reviews personal data, contractual questions, confidentiality, rights to work results and subcontractors.
- **Management:** decides on residual risks, resources, supplier changes or go-live despite open findings.

## Implementation

### Minimum start

Goal: external development work becomes tangible from a security perspective before it starts and is reviewed at acceptance.

1. For each external development activity, owner, supplier, scope, systems, data classes and access needs are recorded.
2. Minimum requirements are clarified before start: secure development, handling of secrets, test data, components, documentation, review and acceptance.
3. External access to repository, ticketing, build or test environments is requested, time-limited and reviewed.
4. Security-relevant results are reviewed before takeover: code review, dependency check, test evidence, architecture review or acceptance check.
5. Open findings receive an owner, deadline, decision and, where necessary, exception.
6. Handover into operations includes documentation, known risks, operational requirements and support/exit information.

Minimum evidence:

- supplier/project profile with owner and scope,
- security requirements or acceptance criteria,
- access approvals for external participants,
- review or test evidence,
- finding/action list,
- handover note to operations or Product Owner.

### Solid practice

Goal: external development is embedded in procurement, SDLC, change and risk management.

1. Suppliers are classified by criticality, system proximity, data relevance and development share.
2. Security requirements are formulated for reuse: secure coding, secrets, logging, components, vulnerabilities, documentation, access, test data, handover.
3. Project milestones include security gates: architecture, implementation, test, acceptance, go-live and handover.
4. External findings flow into the same action log as internal development and vulnerability findings.
5. Subcontractors, offshore/nearshore models, tool use and repository access are made transparent.
6. Exceptions are time-limited, risk-assessed and brought into management review for critical systems.
7. Contract and supplier reviews check whether evidence, response times, rights, exit and support fit the criticality.

Strong evidence:

- supplier classification with development relevance,
- reusable security requirements,
- security gate records,
- tickets for findings and corrections,
- access reviews for external accounts,
- handover documentation,
- management decision for open residual risks.

### Advanced practice

Goal: external development is controlled technically and from a governance perspective like an integrated part of the organisation’s own supply chain.

1. External teams work in controlled repositories, pipelines and development environments with traceable identities.
2. SAST, dependency scanning, secret scanning, container/IaC checks and review rules are integrated into delivery pipelines.
3. Supplier evidence is linked with risk, asset, change and vulnerability management.
4. Critical components receive software bill of materials or component overviews where required for operations and risk decisions.
5. Service provider performance is reviewed not only functionally, but also with regard to security: findings, response time, repeated errors, documentation quality.
6. Exit and emergency capability are tested: access withdrawal, repository handover, build reproducibility, operational knowledge.

## Routine flow

1. **Outsourcing arises:** project, maintenance, extension or supplier change is planned.
2. **Clarify scope and criticality:** determine affected application, data, interfaces, production proximity and business relevance.
3. **Define requirements:** define security, data protection, architecture, documentation and acceptance points.
4. **Control access:** approve and document external identities, privileges, tools and durations.
5. **Accompany development:** track reviews, tests, findings and architecture decisions during delivery.
6. **Perform acceptance:** review security criteria, open risks and operational handover.
7. **Decide risks:** remediate, accept, compensate or escalate open findings.
8. **Secure handover and exit:** clarify documentation, access withdrawal, support, knowledge transfer and ownership/usage rights.
9. **Use supplier review:** feed patterns and weaknesses back into procurement, contracts, SDLC or architecture.

## Decisions

- Which external development services are critical enough for additional security gates?
- Which security requirements are mandatory before commissioning, and which are project-dependent?
- Who may approve external access to code, pipelines, test data or production-like information?
- Which findings block acceptance or go-live?
- How are subcontractors and the service provider’s toolchains made transparent?
- When is a residual risk decided by the Product Owner, and when by management?
- Which documentation and rights are indispensable for operations, maintenance and exit?

## Evidence

### Strong evidence

- project/supplier profile with scope, criticality and owners,
- agreed security and acceptance criteria,
- traceable access approvals and reviews of external accounts,
- architecture, code, test, dependency or vulnerability evidence,
- action log with external findings and decisions,
- acceptance record with open risks,
- handover and exit evidence,
- management decision for accepted critical residual risks.

### Weak evidence

- generic service contract without concrete security reference,
- verbal assurance “the service provider develops securely”,
- code repository without review or acceptance evidence,
- one-off penetration test without finding follow-up,
- access list of external accounts without owner or expiry date,
- project closure without operational handover.

### Evidence gaps

- external development shares are not visible in the supplier register,
- no security requirements before commissioning,
- unclear subcontractors or toolchains,
- no tracking of open findings,
- no overview of external repository or pipeline access,
- missing clarification of rights, documentation or exit.

## Effectiveness review

Review questions:

- Are all external development shares recorded with owner, scope and criticality?
- Are security requirements clarified before start and not only at acceptance?
- Is external access time-limited, traceable and reviewed?
- Can open findings be tracked through to decision or remediation?
- Are acceptance and go-live consciously decided when critical open risks exist?
- Can operations act after handover without silent service provider knowledge?
- Are supplier patterns fed back into procurement, SDLC and risk management?

Possible metrics:

- share of external development projects with security requirements before start,
- open critical findings per supplier or project,
- overdue external access reviews,
- acceptances with open exceptions,
- time to remediate security-relevant supplier findings,
- projects with complete handover documentation.

## BSIG/NIS2 connection point

Outsourced development is connectable to NIS2-oriented topics such as supply chain security, secure development, risk management, access protection, vulnerability handling and maintaining secure digital services. The concrete connection should be assessed in the requirements register, supplier classification and management review.

This artefact does not replace legal, data protection or contractual assessment.

## Boundaries

- This artefact is not a model contract and not legal advice.
- It does not replace technical code, architecture or product security review.
- It does not confirm conformity, certification readiness or supplier suitability.
- It contains no ISO 27002 texts and no confidential supplier information.
- It must not be sufficient as evidence if external development is not practically controlled.

## Handoffs

- **Procurement/vendor handoff:** new development service, supplier classification, subcontractors, contractual or exit questions.
- **Legal/data protection handoff:** personal data, rights to work results, confidentiality, processing on behalf, international service delivery or subcontractors.
- **Development/architecture handoff:** design decisions, code review, components, technical debt, documentation and handover requirements.
- **Access handoff:** external repository, ticketing, pipeline, cloud or test environment access.
- **Change/release handoff:** acceptance, go-live, rollback, operational handover and open findings.
- **Incident handoff:** suspected compromised supplier access, data leakage, manipulated code or insecure component.
- **Management handoff:** critical residual risks, lack of resources, supplier change or go-live with open risks.

## Typical mistakes

- Security requirements are formulated only after contract conclusion or shortly before go-live.
- External developers receive broad access without duration and review.
- Acceptance checks only functional behaviour, not security, operations and handover.
- Findings are treated as project topics and disappear after project end.
- Subcontractors and toolchains remain invisible.
- Operations cannot maintain, build or operate the result in an incident-capable way.
- Management receives delivery status, but not decision-ready residual risks.

## Fictional mini example

A fictional software provider commissions a service provider to extend a customer portal. Before project start, the Product Owner creates a scope profile. The security role adds acceptance criteria for authentication, logging, dependency check and secret handling. External developers receive time-limited repository access. Before go-live, a dependency scan shows a critical library. The service provider delivers an update; a time-limited exception with review date is documented for a medium vulnerability. Operational documentation is supplied as a go-live condition.

Evidence:

- project profile,
- security and acceptance criteria,
- external access approvals,
- dependency scan and correction ticket,
- exception with expiry date,
- handover evidence to operations.
