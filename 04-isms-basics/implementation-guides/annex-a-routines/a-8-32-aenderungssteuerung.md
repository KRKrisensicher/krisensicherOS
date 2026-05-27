# A.8.32 — Change control

## Purpose

Change control ensures that changes to systems, applications, platforms, configurations, processes and security measures are planned, assessed, approved, implemented and reviewed. It protects against unintended outages, security gaps, data loss and operational states that cannot be traced.

The core is not a heavy change board for every small item, but a risk-appropriate routine: Which changes need which review? Who decides? How are emergencies handled? Where does evidence arise?

## Control objective in repository language

The organisation operates a traceable change routine for information-security-relevant systems and processes. The routine connects need, risk and impact assessment, approval, testing, implementation, rollback, communication, evidence and lessons learned.

## Typical risks

- If changes are implemented without assessment, services may fail or protective measures may be unintentionally disabled.
- If security impacts are not reviewed, new vulnerabilities, misconfigurations or permission gaps arise.
- If emergency changes are not reviewed afterwards, shortcuts become normal practice.
- If rollback and tests are missing, disruptions and incidents last longer.
- If changes are not documented, causes cannot be traced during incidents or audits.
- If change processes are too heavy, teams bypass them and thereby lose controllability.

## Triggers

- new release, patch, configuration change, infrastructure change or cloud adjustment.
- change to identities, network, logging, backup, monitoring, cryptography or security tools.
- introduction, change or decommissioning of a system, service or supplier.
- vulnerability, incident, emergency, hotfix or urgent workaround.
- change to processes, roles, data flows or interfaces.
- audit finding, customer requirement, risk decision or management mandate.
- periodic review of changes, errors and emergency changes.

## Roles and responsibilities

- **Change Requester:** describes change, reason, scope, risk, test idea and rollback idea.
- **Service Owner / Asset Owner:** assesses functional impact, protection needs and operational risk.
- **IT / Platform Owner:** plans technical implementation, test, rollback and operational communication.
- **Security role / ISMS Owner:** reviews security-relevant changes, exceptions and risk reference.
- **Change / Release Owner:** coordinates approval, time window, dependencies and follow-up.
- **Data Protection / Legal:** reviews changes involving personal data, logging, contracts or legal commitments.
- **Management:** decides on high residual risks, resources, critical go/no-go questions or permanent deviations.

## Implementation

### Minimum start

Goal: critical changes become visible, are assessed and are approved traceably.

1. The organisation defines which changes are at least subject to control: production systems, critical services, security configurations, access, data flows, external interfaces.
2. Changes are recorded in a ticket, change log or action register.
3. Each change contains reason, affected system, owner, implementation time, test idea, rollback idea and approval.
4. Security-relevant or critical changes receive an additional risk or security review.
5. Emergency changes may be implemented quickly, but must be documented and reviewed afterwards.
6. Failed changes and repeated emergency changes are transferred into lessons learned.

Minimum evidence:

- change or ticket list,
- approval by owner,
- risk/impact note,
- test or rollback evidence,
- post-review for emergency changes,
- actions for errors.

### Solid practice

Goal: changes are classified by risk and integrated into operations, development and the ISMS.

1. Changes are managed in categories: standard, normal, critical, emergency, security change.
2. Assessment logic considers availability, confidentiality, integrity, data classes, exposure, dependencies and customer/user impact.
3. Change approvals are risk-appropriate: small standard changes simplified, critical changes with review and go/no-go.
4. Tests, monitoring, communication needs and rollback are planned before implementation.
5. Implementation and result are documented: successful, rolled back, partially implemented, open.
6. Change errors, incidents and vulnerabilities lead to process improvements.
7. Management receives decision-ready information on risky changes, technical debt and resource bottlenecks.

Strong evidence:

- change classification and assessment logic,
- tickets with risk, approval, test and rollback,
- release and deployment evidence,
- post-review of emergency changes,
- lessons-learned actions,
- management decisions for high residual risks.

### Advanced practice

Goal: change control is automated, risk-based and closely connected with development, operations, security and monitoring.

1. CI/CD, infrastructure as code, configuration management and ticketing are connected so that production changes remain traceable.
2. Automated checks detect critical changes to security groups, identities, logging, encryption, backup or external interfaces.
3. Change risk is supported by asset criticality, exposure, incident history and dependencies.
4. Standard changes are pre-qualified and regularly reviewed to enable speed without loss of control.
5. Monitoring, telemetry and post-deployment checks confirm whether changes work as expected.
6. Change metrics show not only number and speed, but error rate, emergency share, rollbacks, security impacts and overdue reviews.

## Routine flow

1. **Change need arises:** functional need, patch, vulnerability, incident, release, technical debt or process adjustment.
2. **Record change:** document purpose, scope, affected asset, owner, planned time window and dependencies.
3. **Assess impact:** consider security, availability, data, interfaces, users, suppliers and compliance requirements without claiming legal assessment.
4. **Obtain approval:** risk-appropriate decision by owner, change role, security or management.
5. **Prepare implementation:** clarify test, backup, rollback, communication, monitoring and responsibilities.
6. **Perform change:** implement in a controlled way and document deviations.
7. **Review result:** assess function, security, monitoring, errors and open points.
8. **Store evidence:** secure ticket, approval, test, rollback, result and decisions.
9. **Learn and escalate:** transfer errors, emergency changes and recurring causes into improvements or management decisions.

## Decisions

- Which changes are subject to control and which may run as standard changes?
- Which changes require security, data protection, architecture or management review?
- Which risks block implementation or go-live?
- Which test and rollback requirements are the minimum standard for critical systems?
- How are emergency changes allowed, limited and reviewed afterwards?
- When is speed more important than complete prior review and who carries the decision?
- Which recurring change problems require structural investment?

## Evidence

### Strong evidence

- change tickets with scope, owner, risk, approval and implementation result,
- defined change categories and approval rules,
- test, deployment, backup or rollback evidence,
- security review for security-relevant changes,
- post-implementation review for critical or failed changes,
- emergency change records with post-approval,
- management decisions for residual risks or conflicting objectives.

### Weak evidence

- generic change policy without ticket or review evidence,
- release calendar without risk or approval information,
- chat approvals without reference to scope and owner,
- automated deployments without traceable approval,
- emergency changes without post-review,
- change statistics without information on errors or security impacts.

### Evidence gaps

- production changes outside the change log,
- missing owners or affected assets,
- no security assessment for critical configuration changes,
- no rollback plan for high risks,
- repeated emergency changes without root cause analysis,
- missing connection to incidents, vulnerabilities or risk register.

## Effectiveness review

Review questions:

- Are critical production changes recorded completely and traceably?
- Is the depth of review controlled according to risk and criticality?
- Is there evidence for approval, testing, implementation and result review?
- Are emergency changes reviewed afterwards and limited?
- Do failed changes lead to improvements?
- Are security-relevant changes to access, logging, backup, network or cryptography separately visible?
- Does management recognise recurring conflicts between speed, stability and security?

Possible metrics:

- share of production changes with complete ticket,
- failed changes and rollback rate,
- share of emergency changes,
- overdue post-implementation reviews,
- security-relevant changes without security review,
- incidents caused by changes,
- open technical debt from change reviews.

## BSIG/NIS2 connection point

Change control is connectable to NIS2-oriented topics such as risk management, secure development and maintenance, vulnerability handling, incident prevention, cyber hygiene and maintaining critical services. The concrete connection should be assessed in the requirements register and in service/asset criticality.

This artefact does not replace legal assessment or binding review of statutory obligations.

## Boundaries

- This artefact is not an ITIL manual and not a complete release management model.
- It does not replace a technical test strategy, architecture review or operational security analysis.
- It does not guarantee absence of outages, security or conformity.
- It contains no ISO 27002 texts and no secret configuration details.
- It must not cause small teams to be pushed into bypassing controls through unnecessary bureaucracy.

## Handoffs

- **Security handoff:** changes to access, network, logging, backup, cryptography, exposure, security tools or critical configurations.
- **Data protection/legal handoff:** new data processing, changed logging, external interfaces, contract changes or changed commitments.
- **Release/development handoff:** code changes, dependency updates, CI/CD, feature releases and hotfixes.
- **Incident handoff:** change causes disruption, security event or suspected compromise.
- **BCM handoff:** change affects critical services, restart, backup, emergency operations or maintenance windows.
- **Management handoff:** go-live despite residual risk, repeated change errors, resource shortage or technical debt.
- **Audit/evidence handoff:** incomplete change evidence, missing post-reviews or unexplained production changes.

## Typical mistakes

- Every change is treated the same; critical changes are therefore too light or small changes too cumbersome.
- Emergency changes become the normal way of working.
- Security is asked only after implementation.
- Rollback is claimed as “we restore the backup” but is not planned or tested.
- Automated deployments are confused with missing control.
- Changes are closed although monitoring or post-review is missing.
- Management receives throughput metrics, but no view of change risks.

## Fictional mini example

A fictional platform operator wants to change firewall rules for a new interface. The Platform Owner creates a change ticket with affected services, desired time window and rollback. The security role reviews exposure and logging. After approval, the change is implemented, a connectivity test is performed and monitoring is checked. Two days later, a review shows that one rule was broader than planned. It is corrected and added as a lesson learned to the firewall change checklist.

Evidence:

- change ticket with scope and risk,
- security approval,
- implementation and test evidence,
- monitoring check,
- correction ticket,
- updated checklist.
