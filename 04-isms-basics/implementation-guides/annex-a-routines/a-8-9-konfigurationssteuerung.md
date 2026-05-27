# A.8.9 — Configuration control

## Purpose

Configuration control ensures that security-relevant settings of systems, applications, cloud services, network components, endpoints, and platforms are deliberately defined, changed, checked, and corrected. The core is not a one-time baseline, but a routine against configuration drift, shadow changes, and insecure defaults.

## Control objective in repository language

The organization operates a traceable routine for secure and operationally viable configurations. Baselines, responsibilities, changes, exceptions, checks, drift handling, and management decisions are connected in such a way that configurations are created and maintained not by chance, but under control.

## Typical risks

- If systems are operated with insecure default configurations, avoidable attack surfaces arise.
- If changes are made without review, security functions can be disabled, ports opened, or data provided without protection.
- If cloud, SaaS, or network configurations are not monitored, incorrect sharing and exposure remain unnoticed.
- If baselines are not versioned, it is unclear which state was intended.
- If exceptions are not documented, deviation becomes normality.
- If configurations are not connected to vulnerability, change, and incident processes, causes are repeatedly overlooked.

## Triggers

- new system, new application, new cloud resource, new network component, or new SaaS feature.
- change to firewall, identity, logging, encryption, backup, admin rights, or exposure.
- vulnerability finding, misconfiguration, audit finding, incident, or monitoring hit.
- vendor or platform change, new default behavior, or deprecated function.
- architecture, release, change, or migration decision.
- recovery, reinstallation, or infrastructure-as-code change.
- periodic review of baselines, drift, exceptions, and critical configurations.

## Roles and responsibilities

- **System / platform owner:** is responsible for technical configuration, baseline implementation, and corrections.
- **Service owner / application owner:** assesses business impacts, availability, and protection needs.
- **Security role / ISMS owner:** defines minimum logic, review focus areas, exception handling, and reporting.
- **Change owner:** ensures review, approval, testing, and rollback for relevant changes.
- **Cloud / network owner:** manages cloud, network, firewall, DNS, and exposure configurations.
- **Development / DevOps:** maintains configurations in code, deployments, pipelines, and environment variables.
- **Management:** decides on conflicts of objectives, permanent deviations, resource needs, or accepted residual risk.

## Implementation

### Minimum start

Goal: make critical configurations visible, owned, and reviewable.

1. Critical systems, cloud resources, network components, endpoints, applications, and security functions are named in scope.
2. An owner is defined for each critical target.
3. For the most important configuration areas, a desired minimum state is described: access, logging, updates, encryption, exposure, backup, admin rights.
4. Changes to critical configurations run through a ticket, change, or traceable approval.
5. Deviations and exceptions are documented with justification, risk, compensation, and expiry date.
6. At least by sample, it is checked whether the actual state and desired state match.

Minimum evidence:

- scope of critical configuration objects with owner,
- simple baseline or minimum configuration,
- change/ticket evidence,
- configuration extract or review log,
- exception decision with resubmission.

### Solid practice

Goal: configurations are versioned, checked regularly, and connected to change management.

1. Baselines are defined by asset type or platform class: servers, endpoints, network, cloud, database, SaaS, containers, CI/CD.
2. Configurations are versioned or maintained in traceable templates.
3. Critical changes are reviewed for security impact, operational impact, and rollback before implementation.
4. Drift or compliance checks compare actual state and desired state.
5. Recurring deviations lead to root cause analysis: missing automation, unclear owners, tool limits, legacy systems.
6. Exceptions are maintained in the risk or measure log and reviewed regularly.
7. Review results flow into vulnerability management, incident lessons learned, and management review.

### Advanced practice

Goal: configuration control is operated in an automated, risk-based, and auditable way.

1. Infrastructure as code, policy as code, or central management systems define and distribute desired states.
2. Automated drift detection, cloud security checks, or baseline scans generate tickets with owner, risk, and deadline.
3. Critical configurations are checked before deployment in CI/CD or change gates.
4. Emergency changes are reviewed promptly afterwards and returned to the target state.
5. Configuration data supports incident response, forensics, vulnerability assessment, and BCM.
6. Management sees risk development, exception rate, overdue drift corrections, and technical debt.

## Routine flow

1. **Determine configuration object:** system, platform, cloud resource, application, network component, or security function.
2. **Define target state:** describe minimum configuration, owner, protection need, operational requirements, and deviation tolerance.
3. **Control change:** document request, review, test, approval, implementation, and rollback need.
4. **Check actual state:** use export, scan, IaC review, console check, or sample.
5. **Assess deviation:** assess security impact, exposure, data relevance, operational risk, and compensation.
6. **Treat:** correct, time-limit exception, change architecture, or obtain risk decision.
7. **Evidence:** file baseline, change, review, decision, and correction.
8. **Review:** assess drift patterns, exceptions, tool coverage, and recurring causes.
9. **Escalate:** bring deviations that cannot be corrected or are high-risk into the management review.

## Decisions

- Which platforms and configuration areas are critical enough for the start?
- Who may change security-relevant configurations?
- Which changes need security, change, or management approval?
- Which deviations are temporarily acceptable and which are not?
- How are emergency changes reviewed afterwards?
- Which configurations belong in code, templates, or central management systems?

## Evidence

### Strong evidence

- current scope of critical configuration objects with owners,
- versioned baselines, templates, or IaC definitions,
- change tickets with review, testing, and approval,
- configuration scans, exports, or drift reports,
- correction tickets with evidence of implementation,
- exception decisions with risk, compensation, and expiry date,
- management decision for permanent deviation or resource needs.

### Weak evidence

- general hardening policy without system reference,
- screenshot of a setting without date, scope, or owner,
- tool report without triage,
- non-versioned checklist,
- change approval without security assessment,
- statement “vendor default configuration” without review.

### Evidence gaps

- unknown or unowned configuration objects,
- no baseline for critical platforms,
- changes outside the change process,
- drift without ticket or decision,
- exceptions without expiry date,
- no connection to incident, vulnerability, or risk work.

## Effectiveness review

Review questions:

- Is there a defined and known target state for critical platforms?
- Are security-relevant configuration changes approved traceably?
- Are actual state and target state compared regularly?
- Do drift findings lead to correction, exception, or management decision?
- Are emergency changes reviewed afterwards?
- Are recurring misconfigurations treated structurally?

Possible metrics:

- share of critical platforms with baseline,
- number of open drift findings by criticality,
- overdue configuration corrections,
- exception rate and overdue exceptions,
- unplanned or emergency changes with post-review,
- recurring misconfigurations per platform,
- time to correct critical deviations.

## BSIG/NIS2 connection point

Configuration control is compatible with NIS2-oriented topics such as cyber hygiene, secure operational processes, vulnerability management, incident prevention, access protection, monitoring, and business continuity. The specific connection point should be assessed in an organization-specific way in the requirements register, risk analyses, and change/architecture process.

This artifact does not replace legal review, data protection review, or certification assurance.

## Boundaries

- This artifact is not a technical hardening baseline and not a vendor guide.
- It does not replace architecture review, penetration tests, or vulnerability scans.
- It does not guarantee secure configuration without actual implementation and review.
- No binding statement on legal obligations or conformity.
- No confidential system details, secrets, or customer data in public examples.

## Handoffs

- **Change handoff:** security-relevant change, testing need, rollback, emergency change, or release.
- **Vulnerability handoff:** misconfiguration increases exploitability or is reported as a finding.
- **Incident handoff:** configuration change causes or contributes to a security event.
- **Cloud/network handoff:** exposure, firewall, IAM, storage sharing, DNS, or platform policy affected.
- **Development/DevOps handoff:** IaC, CI/CD, environment variables, container and deployment configuration.
- **BCM handoff:** correction endangers availability of critical services or recovery objectives.
- **Management handoff:** permanent deviation, resource need, legacy conflict, or accepted residual risk.
- **Audit/evidence handoff:** missing baselines, incomplete drift evidence, or unclear exception handling.

## Typical mistakes

- A baseline is created but never checked against real systems.
- Changes are implemented technically without assessing security impact.
- Cloud and SaaS configurations are missing from scope.
- Emergency changes become permanent.
- Drift reports are generated but not prioritized.
- Exceptions have no expiry date and no compensation.
- Management receives technical deviation lists without a decision template.

## Fictional mini example

A fictional platform operator checks the configuration of its cloud storage monthly. A drift report shows that a test bucket is publicly readable. The cloud owner blocks access, creates a ticket, and checks the change history. The cause was an emergency change without post-review. The team adds a CI/CD gate for public storage sharing and documents a management decision that production-like test data will not be used in future without protection classification.

Evidence:

- cloud configuration baseline,
- drift report,
- correction ticket,
- root cause analysis for the emergency change,
- added CI/CD gate,
- management decision on test data use.
