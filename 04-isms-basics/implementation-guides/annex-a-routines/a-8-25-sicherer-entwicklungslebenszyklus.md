# A.8.25 — Secure development life cycle

## Purpose

A secure development life cycle ensures that information security is not reviewed only shortly before go-live. Security questions are carried along from idea, requirements, architecture, implementation, testing, release, operation and decommissioning.

The core is not large process bureaucracy, but a clear way of working: Which security decisions must be made in which development step, who makes them, which minimum reviews apply and what evidence is created?

## Control objective in repository language

The organization operates development so that security requirements, risks, architecture decisions, code quality, tests, approvals, operational handover and lessons learned are traceably connected. The development process makes visible when security risks are accepted, treated or escalated.

## Typical risks

- If security requirements are considered only at the end, expensive rework or insecure releases arise.
- If product, development and operations teams have different security assumptions, gaps remain between design, implementation and operation.
- If external development contributions are not included in the same governance, unknown dependencies, insecure components or missing evidence arise.
- If findings from tests do not feed into release decisions, known weaknesses go into production.
- If security decisions are not documented, exceptions, residual risks and technical debt can no longer be traced later.
- If decommissioning and end of maintenance are missing, outdated applications, repositories or interfaces remain active.

## Triggers

- new product, new application, major feature or relevant release.
- architecture, technology, cloud, platform or interface change.
- new data class, new user group, external accessibility or increased criticality.
- vulnerability, security event, penetration test or audit finding.
- change of development provider, framework, build pipeline or operating model.
- decision on go-live, exception, end of maintenance or decommissioning.
- periodic review of the development process and its security gates.

## Roles and responsibilities

- **Product Owner / Service Owner:** responsible for business need, protection need, prioritization and release decision.
- **Development team / Tech Lead:** implements security requirements, secure programming practices and technical measures.
- **Security role / AppSec role:** defines minimum gates, supports risk and test logic and assesses critical findings.
- **Architecture role:** reviews architecture decisions, trust boundaries, integrations and technical debt.
- **IT operations / Platform team:** takes over operational requirements, monitoring, configuration and patchability.
- **ISMS Owner:** connects the development routine with risk register, action log, evidence and management review.
- **Procurement / Supplier management:** includes external development, SaaS, components and service providers.
- **Management:** decides in cases of resource shortages, accepted residual risks, schedule/security conflicts and permanent exceptions.

## Implementation

### Minimum start

Objective: make security decisions visible in every relevant development initiative.

1. The organization defines which applications and development initiatives are in scope.
2. For each initiative, the Product Owner, technical owner and security contact are named.
3. A short security checklist is used in planning, implementation, testing and release.
4. Security requirements, critical architecture assumptions and open risks are recorded in the ticket or action log.
5. Before go-live, it is checked whether critical findings are closed, accepted or escalated.
6. External development contributions are included with minimum evidence and contacts.

Minimum evidence:

- initiative list with owners,
- security checklist or gate evidence,
- documented security requirements and open risks,
- test or review evidence,
- release decision with open findings or exception decisions.

### Solid practice

Objective: security is integrated into the development process in a repeatable way.

1. The development process contains defined security activities per phase: requirements analysis, design, code, build, test, release, operation.
2. Risk and protection-need logic determine which security gates are necessary.
3. Architecture reviews, code reviews, dependency checks and security tests are planned on a risk basis.
4. Findings are prioritized, assigned to an owner and decided before release.
5. External development is included through contracts, deliverables, evidence and acceptance.
6. Security-related technical debt is maintained in the backlog and reviewed.
7. Lessons learned from incidents, tests and operational problems feed back into standards and templates.

Strong evidence:

- defined SDLC with security gates,
- risk-based gate criteria,
- architecture and code review evidence,
- test and findings log,
- release approvals with security decision,
- backlog for security measures and technical debt,
- supplier evidence for external development contributions.

### Advanced practice

Objective: the development life cycle continuously generates controllable security information.

1. Security gates are integrated into CI/CD, ticketing, architecture decisions and release processes.
2. Threat modeling, abuse cases or comparable methods are used for critical initiatives.
3. Build, dependency, secret and container checks deliver automated signals to teams.
4. Release decisions use risk indicators such as open critical findings, test coverage, exceptions and operational readiness.
5. Security patterns, secure templates and platform controls reduce repeated effort.
6. Management sees not only tool metrics, but decision needs: overdue security work, technical debt, risk acceptances and resource bottlenecks.

## Routine flow

1. **Initiative starts:** Product Owner or Tech Lead reports a new or changed development initiative.
2. **Clarify scope and risk:** classify data, user groups, exposure, criticality, suppliers and operating model.
3. **Plan security activities:** define necessary requirements, architecture review, tests and approvals.
4. **Accompany implementation:** include security requirements in tickets, Definition of Done or acceptance criteria.
5. **Perform reviews and tests:** review architecture, code, dependencies, pipeline and application on a risk basis.
6. **Decide findings:** remediate, compensate, defer, accept or escalate.
7. **Approve release:** go-live only with a traceable security and residual-risk decision.
8. **Secure operational handover:** hand over monitoring, patchability, owners, documentation and support paths.
9. **Learn:** feed findings, incidents and operational problems back into standards, backlog and training.

## Decisions

- Which development initiatives fall under the secured development process?
- Which security gates are mandatory for which criticality?
- When may a release go live despite open findings?
- Who accepts technical debt or residual risks and for how long?
- Which external development evidence is sufficient?
- Which automation is worthwhile without overloading teams with false alarms?

## Evidence

### Strong evidence

- initiative or application register with criticality and owners,
- security requirements in backlog or specification,
- architecture decisions and review minutes,
- code, dependency, pipeline and security test evidence,
- finding log with priority, owner, deadline and status,
- release approval with residual-risk decision,
- evidence of operational handover and lessons learned.

### Weak evidence

- general development policy without concrete application to initiatives,
- tool reports without triage or release reference,
- verbal statement “Security reviews as well” without gate or evidence,
- backlog tickets without security prioritization,
- supplier assurance without verifiable delivery evidence.

### Evidence gaps

- no list of applications or development initiatives in scope,
- no named owners for security in the initiative,
- open critical findings without release decision,
- external development without security evidence,
- no feedback of incidents or tests into the development process.

## Effectiveness review

Review questions:

- Are security-relevant development initiatives visible early in the process?
- Are security requirements, architecture decisions and tests planned on a risk basis?
- Can open findings be assigned to a release or risk decision?
- Are external development contributions included in gates and evidence?
- Does the process lead to fewer recurring findings or faster decisions?
- Does management receive decision-ready information on residual risks and resource needs?

Possible metrics:

- share of critical initiatives with security gate,
- open critical findings before release,
- overdue security measures in the backlog,
- share of external development contributions with evidence,
- recurring finding types,
- number of accepted residual risks and their follow-up dates.

## BSIG/NIS2 connection point

A secure development life cycle is a connection point for NIS2-oriented topics such as risk management, secure development, vulnerability treatment, supply chain security, cyber hygiene and security of digital services. The concrete relationship should be assessed in the requirements register, in risk analyses and in management decisions in an organization-specific way.

This artifact does not replace legal assessment, data protection review or any statement on applicability.

## Boundaries

- This artifact is not a complete AppSec program and not a CI/CD tool design.
- It does not replace technical architecture, code or penetration test review.
- It makes no certification, conformity or security guarantee.
- It contains no ISO 27002 texts and no confidential development details.
- It must not be used as a substitute for human risk and release decisions.

## Handoffs

- **Architecture handoff:** new trust boundaries, critical interfaces, cloud/platform change, high technical debt.
- **Secure coding handoff:** recurring code errors, insecure patterns, missing developer enablement.
- **Security testing handoff:** new critical function, external go-live, high criticality or unresolved findings.
- **Operations handoff:** monitoring, patchability, incident contacts, configuration and support model before go-live.
- **Supplier handoff:** external development, third-party components, SaaS, missing evidence or unclear responsibilities.
- **Data protection/legal handoff:** personal data, contractual commitments, terms of use, logging or cross-border processing.
- **Management handoff:** release despite critical findings, resource shortage, permanent exception, accepted residual risk.

## Typical mistakes

- Security is included as a late acceptance obstacle instead of as a development routine.
- Gates exist but are skipped under schedule pressure.
- Tool findings are produced but not decided on a risk basis.
- External development is commissioned faster than it is steered from a security perspective.
- Release approvals document functionality, but not open security risks.
- Lessons learned from incidents change neither templates nor standards.
- The process is so heavyweight that teams bypass it.

## Fictional mini example

A fictional software provider develops a new customer module. At initiative start, an architecture review is defined because of external accessibility and personal data. The development team adds security requirements to the backlog, performs dependency scans and code reviews and documents two findings. One critical finding is remediated before release; one medium finding receives a time-limited exception with an action in the next sprint. Operations takes over monitoring and patch responsibility.

Evidence:

- initiative entry with criticality,
- security requirements in the backlog,
- architecture review,
- scan and code review evidence,
- finding decision before release,
- operational handover with owners.
