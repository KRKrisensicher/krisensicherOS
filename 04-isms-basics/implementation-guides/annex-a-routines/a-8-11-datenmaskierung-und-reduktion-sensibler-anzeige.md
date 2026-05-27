# A.8.11 — Data masking and reduction of sensitive display

## Purpose

Data masking and reduced display ensure that people, systems, and service providers only see the sensitive details they truly need for their task. The core is not “redacting data somehow”, but a deliberately designed display and processing routine: which fields are shown fully, partially, pseudonymized, aggregated, or not at all to whom?

## Control objective in repository language

The organization operates a routine that specifically minimizes or masks sensitive information in applications, reports, test data, support cases, logs, exports, and interfaces. The routine connects data classification, role need, access, development, reporting, data protection/legal handoff, and technical validation.

## Typical risks

- If full sensitive data appears in support screens, reports, or screenshots, it can be copied, shared, or disclosed unnecessarily.
- If production data is used unchanged in test or training environments, unnecessary confidentiality and data protection risks arise.
- If roles only receive access to an application but field visibility is not differentiated, people see more details than needed for their task.
- If logs, error messages, or exports contain sensitive values, data reaches secondary repositories that are difficult to control.
- If masking is not tested, edge cases, APIs, or admin views can bypass the protection logic.

## Triggers

- New system, new data field, new report, new interface, or new support function.
- Processing of sensitive data in test, development, training, or analytics environments.
- Role change, new service provider access, or new external support service.
- Data protection/legal review, data classification change, or new protection needs assessment.
- Incident, data leakage, screenshot/export finding, or audit finding.
- Change to logging, monitoring, debugging, BI, AI/analytics functions, or data warehouse.
- Regular review of masking rules and samples of actual display.

## Roles and responsibilities

- **Information Owner / Business Unit:** assesses which fields must be visible for which task.
- **Product Owner / Application Owner:** prioritizes masking, field permissions, and UI/API requirements.
- **Development / Platform Team:** implements masking, tokenization, pseudonymization, aggregation, or field suppression.
- **Data Protection / Legal:** reviews personal data, purpose limitation, test data, reporting, and external disclosure.
- **ISMS Owner / Security Role:** defines minimum requirements, review logic, evidence, and escalation.
- **Support / Operations Owner:** ensures that operations and support processes remain workable with reduced display.
- **Management:** decides on target conflicts between workability, transparency, costs, and residual risk.

## Implementation

### Minimum start

Goal: reduce unnecessary display of especially sensitive fields in critical processes.

1. Critical data fields and displays in the ISMS scope are identified: identifiers, financial data, health data, secrets, credentials, confidential business details.
2. For each critical display, it is defined which roles need full, partial, or no visibility.
3. At least support, reporting, export, and test data processes are reviewed.
4. Simple masking is implemented: partial display, placeholders, aggregation, separate approval for full visibility.
5. Exceptions are documented with purpose, duration, owner, and review date.
6. A sample checks whether masking actually works in the user interface, export, and screenshot scenario.

Minimum evidence:

- list of sensitive fields or data classes,
- role/display matrix,
- ticket for masking implementation,
- test or screenshot evidence with fictional data,
- exception decision with follow-up date.

### Solid practice

Goal: masking is operated as a design and review routine.

1. Data classification and protection need control display, export, logging, and test data rules.
2. Masking requirements are included in development, procurement, and change processes.
3. Production, test, training, and analytics environments are considered separately.
4. APIs, reports, search functions, admin views, and bulk downloads are included in the review.
5. Role-specific full visibility is justified, approved, and regularly reviewed.
6. Masking errors trigger corrective tickets, root cause analysis, and incident triage where needed.
7. Data protection/legal handoffs are triggered when personal or especially sensitive data is affected.

Strong evidence:

- data field/protection needs catalog,
- role and display concept,
- development or change tickets with acceptance criteria,
- test cases for UI, API, export, report, and logs,
- review evidence for full-visibility roles,
- approvals and exceptions with expiry date,
- management decision where reduction cannot be implemented.

### Advanced practice

Goal: sensitive display is systematically minimized and technically monitored.

1. Masking rules are implemented centrally or reuseably through platform, API, or data access layers.
2. Test data is generated synthetically or anonymized/pseudonymized in a controlled way where suitable and reviewed.
3. Data loss prevention, discovery, or logging checks detect sensitive fields in exports, reports, and secondary repositories.
4. Permissions for full visibility are granted with time limits, case-based approval, or additional approval.
5. Architecture and data protection reviews consider re-identification risks, combination of data sources, and analytics purposes.
6. Metrics show full-visibility roles, masking coverage, findings in logs/exports, and overdue exceptions.

## Routine flow

1. **Display or processing need arises:** new feature, report, support case, test environment, export, or interface.
2. **Classify data fields:** determine sensitive fields, purpose, role need, and possible secondary repositories.
3. **Decide visibility:** display fully, partially, aggregated, pseudonymized, anonymized, synthetic, or not at all.
4. **Check human gates:** involve Data Protection/Legal when personal, employment-law, or contractual questions are touched.
5. **Implement technically:** adapt UI, API, export, log, report, and test data rule.
6. **Test:** use fictional or approved test data to check whether masking works in primary and secondary paths.
7. **File evidence:** document decision, implementation, test, and exceptions.
8. **Review:** regularly check roles with full visibility and critical displays.
9. **Improve:** feed findings from incidents, audits, and support practice back into design rules.

## Decisions

- Which data fields are sensitive enough that full visibility must be justified?
- Which roles need full values, and which only partial values or aggregated information?
- How are exports, screenshots, logs, search results, and reports limited?
- Which test data strategy is realistic for the organization?
- When is masking sufficient, and when is access removal, encryption, or process change needed?
- Who may approve time-limited full visibility?

## Evidence

### Strong evidence

- current catalog of sensitive fields and displays,
- role/field visibility matrix,
- documented design or change decisions,
- test evidence for user interface, API, export, report, and logs,
- review of full-visibility and exception permissions,
- evidence of cleaned test data or synthetic data,
- data protection/legal handoff for relevant data categories.

### Weak evidence

- general statement “data is masked” without field and role reference,
- screenshot of a single screen without API/export review,
- test database of unknown origin,
- data minimization policy without technical acceptance criteria,
- role list without review of actual display.

### Evidence gaps

- sensitive values in logs, error messages, BI exports, or tickets,
- admin or support views without reduction,
- production data in test systems without review,
- full-visibility roles without owner or review,
- no consideration of APIs and bulk downloads,
- exceptions without expiry date.

## Effectiveness review

Review questions:

- Are sensitive fields and critical displays known?
- Can it be justified which role sees which details?
- Does masking also work in exports, APIs, logs, reports, and support processes?
- Are test and training data used without unnecessary production details?
- Are full-visibility roles regularly reviewed and adjusted when roles change?
- Do findings lead to corrections in the design or development process?

Possible metrics:

- share of critical applications with role/display matrix,
- number of roles with full visibility into sensitive fields,
- findings of sensitive data in logs or exports,
- overdue masking measures,
- exceptions and expired exceptions,
- test coverage for UI/API/export/log.

## BSIG/NIS2 connection point

Data masking and reduced display are compatible as a connection point with NIS2-oriented risk management measures, access protection, secure development, cyber hygiene, protection of sensitive information, and incident prevention. For affected organizations, the concrete connection should be assessed in the requirements register, data protection concept, and secure development process.

This artifact does not replace a data protection assessment, legal advice, or a binding review of applicability or obligations.

## Boundaries

- Masking is not a substitute for access control, encryption, or a deletion routine.
- Partial masking can be re-identifiable when combined with other data; this needs human review.
- This artifact does not define legally binding anonymization under data protection law.
- It contains no ISO 27002 text and no certification assurance.
- Public examples use only fictional, non-sensitive data.

## Handoffs

- **Data Protection / Legal Handoff:** personal data, special protection needs, test data, re-identification risk, external disclosure.
- **Development Handoff:** UI, API, export, logging, test data, acceptance criteria.
- **Access / IAM Handoff:** full-visibility roles, privileged views, time-limited approvals.
- **Support / Operations Handoff:** workability with reduced display, approval process for full visibility in individual cases.
- **Incident Handoff:** sensitive data in tickets, logs, screenshots, or unintended exports.
- **Management Handoff:** costs, technical limits, target conflicts with business processes, accepted exceptions.
- **Audit / Evidence Handoff:** missing test evidence or masking rules that cannot be reviewed.

## Typical mistakes

- Only the user interface is masked, while API and export remain complete.
- Support receives blanket full visibility because individual approval is missing.
- Production data is copied for tests without reduction or approval.
- Logs contain sensitive values even though the application screens are reduced.
- Masking is implemented once but not reviewed when new fields are added.
- Partial masking is confused with anonymization.
- Exceptions for full visibility are not time-limited.

## Fictional mini example

A fictional payment service provider has so far shown full account details in customer service. After a review, the information owner defines that support only sees the last four digits; full visibility is only possible for a justified clarification case with team lead approval. Development adapts the user interface, export, and API responses. A test with fictional customer data shows that a CSV export still contains full values; the finding is corrected before approval.

Evidence:

- role/display matrix,
- change ticket with acceptance criteria,
- test evidence for screen, API, and CSV export,
- approval process for full visibility,
- review note on the corrected export gap.
