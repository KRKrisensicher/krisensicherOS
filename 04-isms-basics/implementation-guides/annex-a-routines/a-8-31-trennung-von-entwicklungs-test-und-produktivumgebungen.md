# A.8.31 — Separation of development, test and production environments

## Purpose

Separation of development, test and production environments prevents unfinished code, test data, debug access, experiments or faulty changes from endangering production operations. At the same time, it protects against data leakage and silent shortcuts between development and operations.

The core is not “there are three environments”, but an operated boundary: Who may access what? Which data may be used? How do changes move in a controlled way from development through test into production? How are exceptions decided?

## Control objective in repository language

The organisation operates a traceable routine for controlling environments, data flows, access, deployment paths and exceptions between development, test, staging and production. The goal is clear separation between experimentation, verification and production operations.

## Typical risks

- If developers have direct production access, unintended or unapproved changes may disrupt production services.
- If production data is used unprotected in test environments, confidentiality and data protection risks may arise.
- If test and production systems use the same credentials, keys or interfaces, misconfigurations may affect real data or services.
- If deployments bypass environment boundaries, acceptance, rollback and traceability are missing.
- If test environments are protected more weakly, they can serve as an entry point into production-like systems.
- If emergency access is not documented, separation is eroded in daily work.

## Triggers

- new system, new application, new platform or new CI/CD pipeline.
- change to architecture, hosting, network segmentation or cloud accounts.
- introduction or change of development, test, staging or production environments.
- use of production or production-like data outside production.
- release, hotfix, emergency change or rollback.
- audit finding, incident, failed deployment or suspected data leakage.
- periodic review of environments, access and deployment paths.

## Roles and responsibilities

- **Product Owner / Service Owner:** decides functional need for environments, test depth and go-live.
- **Development team:** uses development and test environments according to approvals and delivers deployable changes.
- **IT / Platform Owner:** operates environments, segmentation, identities, secrets, pipelines and production access.
- **Change / Release Owner:** controls transition from test to production, acceptance, rollback and evidence.
- **Security role / ISMS Owner:** defines minimum separation, review logic, exception handling and risk handoff.
- **Data Protection / Legal:** reviews personal or confidential data in test and development environments.
- **Management:** decides permanent exceptions, resource needs or accepted operational risks.

## Implementation

### Minimum start

Goal: production systems and production data are traceably separated from development and test.

1. Critical applications and platforms in scope receive a simple environment overview: development, test, staging, production or justified deviation.
2. For each environment, owner, purpose, data class, access groups and deployment path are named.
3. Direct changes in production are limited to defined roles and emergencies.
4. Production data in test is avoided or used only after approval, protective measure and review date.
5. Secrets, credentials and interfaces are managed separately for each environment.
6. Exceptions are documented: reason, duration, risk, compensation and decision.

Minimum evidence:

- environment overview for critical systems,
- access and role evidence per environment,
- documented deployment or change path,
- decision on test data,
- exception or emergency access record.

### Solid practice

Goal: environments are technically, organisationally and procedurally separated.

1. Environments are classified by criticality and production proximity.
2. Network, identities, secrets, logging, databases, cloud accounts and interfaces are separated or coupled in a controlled way.
3. Deployments take place through defined pipeline, change or release steps with review and approval.
4. Production access is separately approved, logged and reviewed.
5. Test data management defines when synthetic, anonymised, masked or production data is permissible.
6. Staging and test environments receive appropriate protective measures when they are production-like.
7. Environment reviews regularly check access, data stores, secrets, interfaces and deviations.

Strong evidence:

- environment and data flow diagram,
- role concept per environment,
- pipeline/release records,
- production access reviews,
- test data approvals,
- secret/configuration evidence without disclosure of secret values,
- exception decisions with expiry date.

### Advanced practice

Goal: separation is built into platform, automation and governance.

1. Infrastructure as code, policy as code or platform standards enforce environment boundaries.
2. CI/CD pipelines separate build, test, approval, deployment and rollback in a technically traceable way.
3. Production access runs through just-in-time, break-glass or privileged access procedures with review.
4. Data masking, synthetic data and automated cleanup reduce test data risks.
5. Deviations are detected through monitoring, cloud policy, configuration checks or audit logs.
6. Management sees decision-ready metrics on direct production access, bypasses, test data risks and overdue exceptions.

## Routine flow

1. **Environment need arises:** new system, feature, test need, platform change or release process.
2. **Define scope:** determine purpose, criticality, data class and production proximity of the environment.
3. **Design boundaries:** separate access, network, secrets, data, interfaces and deployment paths.
4. **Define approvals:** who may develop, test, accept, deploy and intervene in an emergency?
5. **Control data:** review test data need and define protective measure.
6. **Move changes:** perform development, test, acceptance, release and rollback traceably.
7. **Handle exceptions:** time-limit and review emergency access, direct production changes or production test data.
8. **Review effectiveness:** check access lists, deployment logs, environment deviations and test data inventories.
9. **Improve:** feed findings back into platform standard, change process or test data management.

## Decisions

- Which systems need separate development, test, staging and production environments?
- Which deviations are acceptable for small systems and how are they compensated?
- Who may have direct production access and under which conditions?
- Which data may be used in test or development environments?
- Which deployment paths may change production?
- When does missing separation block a go-live?
- Which technical debt in environments must go into management review?

## Evidence

### Strong evidence

- current environment overview with owners and data classes,
- role and access model per environment,
- release, change or pipeline evidence,
- records of direct production access and reviews,
- test data decisions with protective measures,
- technical evidence for separated secrets, accounts or configurations,
- documented exceptions with risk decision and expiry date.

### Weak evidence

- architecture diagram without access or data reference,
- statement “prod and test are separated” without evidence,
- screenshots of individual cloud resources without scope,
- pipeline exists but can be bypassed manually,
- test data rule without actual data review,
- admin access without usage evaluation.

### Evidence gaps

- no overview of production-like test environments,
- shared secrets or accounts across environments,
- production data in test without approval,
- direct production changes without change evidence,
- no reviews of privileged production access,
- exceptions without expiry date or management decision.

## Effectiveness review

Review questions:

- Can it be traced for critical systems which environments exist and for what purpose?
- Are production access, data and secrets separated from development and test?
- Are changes brought into production through defined release or change paths?
- Is direct production access rare, justified and reviewed?
- Is production data in test environments avoided or appropriately decided?
- Are production-like test environments protected according to their risk?
- Are bypasses and exceptions tracked and reduced?

Possible metrics:

- share of critical systems with current environment overview,
- number of direct production accesses per period,
- overdue environment or access reviews,
- test environments with production data,
- open exceptions to environment separation,
- failed or rolled-back releases due to environment deviations.

## BSIG/NIS2 connection point

The separation of development, test and production environments is connectable to NIS2-oriented topics such as secure development, change control, access protection, cyber hygiene, protection of production services and risk management. The concrete connection should be assessed through the requirements register, asset criticality and data classification.

This artefact does not replace legal or data protection assessment.

## Boundaries

- This artefact is not a detailed network, cloud or CI/CD design.
- It does not replace data protection review for production data in test environments.
- It does not guarantee availability, security or conformity.
- It contains no ISO 27002 texts and no secret configuration values.
- It must not be considered sufficient if environment boundaries can be technically bypassed and nobody reviews it.

## Handoffs

- **Change/release handoff:** transition into production, emergency change, rollback or missing acceptance.
- **Access handoff:** direct production access, admin rights, external developers or technical accounts.
- **Data protection/legal handoff:** production or personal data in test, logging, masking, retention or third-party access.
- **Architecture/platform handoff:** segmentation, cloud accounts, CI/CD, secrets, interfaces and environment standard.
- **Incident handoff:** failed deployment, data leakage from test, compromised test environment or unauthorised production change.
- **Management handoff:** permanent exceptions, missing platform resources, technical debt or go-live despite separation deficiencies.
- **Audit/evidence handoff:** unclear environment list, missing review evidence or deployment paths that cannot be audited.

## Typical mistakes

- Test environments contain production data but are treated like harmless sandboxes.
- Developers have permanent admin rights on production because it is faster.
- Pipeline and change process exist, but are regularly bypassed for hotfixes.
- Secrets are copied between environments.
- Staging is production-like but significantly less protected.
- Environments are created but never cleaned up.
- Management sees release speed, but not the risks from shortcuts.

## Fictional mini example

A fictional online service operates development, staging and production in separate cloud accounts. During review, it becomes apparent that staging contains a copy of production customer data. The Platform Owner stops new copies, the Product Owner confirms the test need and Data Protection is involved for the protection assessment. The team decides to switch to synthetic test data. Until then, the staging environment is more strongly isolated and the exception is documented with an expiry date.

Evidence:

- environment overview,
- review finding on staging data,
- decision to change test data,
- temporary protective measure,
- exception with review date,
- updated test data rule.
