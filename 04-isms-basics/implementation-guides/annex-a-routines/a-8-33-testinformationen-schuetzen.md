# A.8.33 — Protecting test information

## Purpose

Test information enables development, quality assurance, migrations, training and error analysis. At the same time, test data can contain sensitive business logic, personal data, secrets, production structures or realistic attack paths. This routine ensures that test information is used for a specific purpose, protected, limited and reviewable.

The core is not “test data exists”, but: Which information is used for what? Is real data required? Who approves it? How is it protected, cleaned up and deleted?

## Control objective in repository language

The organisation operates a routine for selecting, approving, protecting, using, storing and deleting test information. It connects test need, data classification, data protection handoff, environment separation, access protection and evidence.

## Typical risks

- If production data is copied into test environments without review, confidential or personal information may be unnecessarily exposed.
- If test data contains real credentials, tokens or keys, production systems may be compromised.
- If test data remains for a long time, forgotten data stores with weaker protection arise.
- If external testers or developers receive broad test data, data leakage or unclear responsibilities may result.
- If anonymisation or masking remains unreviewed, re-identification or inference about real persons, customers or trade secrets may be possible.
- If test data does not fit the test objective, pseudo-tests and undetected errors arise.

## Triggers

- new test, development, training, analysis or migration activity.
- copy, extract or provision of production or production-like data.
- use of external testers, service providers, developers or cloud test services.
- error analysis with realistic data or log extracts.
- new data class, new system, new interface or changed data flows.
- audit finding, data protection question, incident or suspected data leakage.
- periodic review of test data stores and test environments.

## Roles and responsibilities

- **Test Owner / QA lead:** describes test purpose, data need and acceptance criteria.
- **Data Owner / Information Owner:** decides which data or data classes are permissible for the test.
- **Product Owner / Service Owner:** prioritises test need and accepts functional limitations when synthetic data is used.
- **IT / Platform Owner:** provides test environment, access protection, cleanup, deletion and technical protective measures.
- **Security role / ISMS Owner:** defines protection requirements, review logic, exception handling and evidence.
- **Data Protection / Legal:** reviews personal data, anonymisation, masking, retention, service providers and purpose limitation.
- **Management:** decides on conflicts between test quality, effort, data protection/protection needs and delivery dates.

## Implementation

### Minimum start

Goal: test information is not copied from production without review.

1. Each test data need for critical systems is briefly described: purpose, system, data class, user group and duration.
2. The default is synthetic, anonymised, masked or reduced test information where it fulfils the test objective.
3. Production or production-like data requires traceable approval by the Data Owner and, where necessary, data protection/legal handoff.
4. Test data access is limited to necessary persons and duration.
5. Secrets, passwords, tokens and keys are not transferred from production into test data stores.
6. After the test ends, data is deleted, cleaned up or transferred into a controlled store.

Minimum evidence:

- test data request or test data profile,
- Data Owner approval,
- protection or masking decision,
- access evidence for test data,
- deletion or cleanup evidence,
- exception decision for production-like data.

### Solid practice

Goal: test data management is repeatable and risk-based.

1. Data classes and test data types are distinguished: synthetic, anonymised, masked, pseudonymised, production-like, log data, reference data.
2. Minimum protection is defined for each class: access, storage location, encryption, retention, sharing, deletion.
3. Masking and anonymisation procedures are reviewed by Data Owner and Data Protection according to the risk.
4. Test data stores are inventoried: system, purpose, owner, data class, creation date, expiry date, environment.
5. External use is connected with supplier, access and contract control.
6. Test data reviews check orphaned stores, overly broad access and overdue deletion.
7. Findings from tests, incidents or audits improve test data rules and environment standards.

Strong evidence:

- test data register,
- data classification per test store,
- approvals and data protection/legal handoffs,
- masking or synthetic generation evidence,
- access reviews,
- deletion logs,
- exception and risk decisions.

### Advanced practice

Goal: test information is provided in an automated, reproducible and data-minimised way.

1. Test data is generated, masked, synthesised or provided through defined pipelines.
2. Automated checks prevent transfer of secrets, production identifiers or impermissible data classes.
3. Test data stores have technical expiry dates, cleanup jobs or deletion workflows.
4. Role-based self-service provisioning connects test purpose, approval, data class and access.
5. The quality of synthetic or masked test data is checked against test objectives so that protection does not lead to pseudo-tests.
6. Metrics show production-like test data, overdue stores, external use, deletion deadlines and exceptions.

## Routine flow

1. **Test need arises:** feature, release, error analysis, migration, training or acceptance test.
2. **Describe data need:** clarify test objective, required fields, degree of realism, data class, user group and duration.
3. **Choose protection variant:** synthetic, anonymised, masked, reduced or justified production-like.
4. **Obtain approval:** involve Data Owner and, for personal or sensitive data, Data Protection/Legal.
5. **Provide data:** use controlled environment, separated secrets, appropriate access restriction and logging.
6. **Perform test:** limit use to purpose and duration.
7. **Review store:** delete data no longer needed, withdraw access, close exceptions.
8. **Secure evidence:** document request, decision, protective measure, access and deletion.
9. **Improve:** feed recurring test data problems back into data model, test strategy or platform standard.

## Decisions

- When are synthetic or reduced data sufficient for the test purpose?
- Which data classes may never, or only with special approval, enter test environments?
- Who may approve production-like test data and for how long?
- Which masking or anonymisation is sufficient without replacing a data protection assessment?
- Which external parties may receive test information?
- When does missing test data quality become a risk for release or acceptance?
- Which legacy stores must be cleaned up or escalated into management review?

## Evidence

### Strong evidence

- test data profile with purpose, data class, owner and duration,
- Data Owner approval and data protection/legal handoff where needed,
- evidence of masking, anonymisation, reduction or synthetic generation,
- test data register with expiry date,
- access evidence and reviews,
- deletion or cleanup logs,
- exception with risk decision and review date.

### Weak evidence

- generic statement “test data is anonymised” without evidence or scope,
- database copy without approval,
- test environment with unclear data store,
- screenshot of a masking rule without result review,
- access group without owner or expiry date,
- old test data policy without inventory review.

### Evidence gaps

- production data copies without documented purpose,
- secrets or real credentials in test data,
- external use without supplier or access clarification,
- no deletion deadlines for test stores,
- no review of masking quality,
- orphaned test environments with sensitive data.

## Effectiveness review

Review questions:

- Can purpose, owner, data class and duration be traced for critical test data stores?
- Is production-like use justified and approved?
- Are secrets and production credentials reliably removed from test data?
- Is test data access limited to necessary persons and time periods?
- Are old test data stores deleted or reviewed?
- Is Data Protection/Legal involved when personal or particularly sensitive data is affected?
- Do the chosen test data support the test objective without creating unnecessary protection risks?

Possible metrics:

- number of production-like test data stores,
- overdue test data deletions,
- test data stores without owner,
- external access to test information,
- exceptions for use of production data,
- findings on secrets or impermissible data in test environments.

## BSIG/NIS2 connection point

The protection of test information is connectable to NIS2-oriented topics such as secure development, data-protection-adjacent protective measures, access protection, risk management, supply chain security and protection of digital services. The concrete connection should be assessed organisation-specifically through data classification, requirements register and human review.

This artefact does not replace data protection advice or legal review of data processing.

## Boundaries

- This artefact is not a data protection impact assessment and not a legal opinion.
- It does not replace technical assessment of anonymisation, masking or re-identification risks.
- It does not guarantee data protection conformity, security or certification readiness.
- It contains no real data, secrets or ISO 27002 texts.
- It must not encourage copying production data into test environments for convenience.

## Handoffs

- **Data protection/legal handoff:** personal data, re-identification risk, masking, purpose limitation, service providers, retention or risks to data subjects.
- **Data Owner handoff:** approval of data classes, data minimisation, quality and permissible test purpose.
- **Access handoff:** test data access, external testers, service providers and expiry of permissions.
- **Environment handoff:** test, staging or development environment with production-like data.
- **Development/QA handoff:** test objective, data quality, synthetic data, error analysis and release risks.
- **Incident handoff:** suspected test data leakage, secrets in test data or impermissible data copy.
- **Management handoff:** conflict between test realism, delivery date, protection need and effort.

## Typical mistakes

- Production data is copied because it is the fastest way.
- Masking is claimed, but not checked for result and inference risks.
- Test data contains real passwords, tokens or keys.
- Test data is not deleted after project end.
- External developers receive broad data packages without purpose and duration limits.
- Test data is so heavily distorted that important errors are not found.
- Data Protection is asked only after data has already been copied.

## Fictional mini example

A fictional development team needs realistic data for a migration test. The Test Owner describes the required fields and determines that real names and contact data are not necessary. The Data Owner approves a masked extract with reduced scope. Data Protection reviews the personal-data reference. The platform creates the extract in a protected staging environment and sets a deletion date. After test completion, the store is deleted and closed in the test data register.

Evidence:

- test data profile,
- Data Owner approval,
- data protection handoff,
- masking evidence,
- access list for staging,
- deletion log,
- closed register entry.
