# A.8.29 — Security testing in development and acceptance

## Purpose

Security testing in development and acceptance ensures that security requirements, architecture assumptions and coding decisions are reviewed before productive use. The objective is not as much test volume as possible, but risk-based test capability: the right things are tested at the right time, findings are decided and acceptances remain traceable.

The core is a testing and acceptance routine that connects development, Security, QA, operations and Product Owner.

## Control objective in repository language

The organization plans, performs and evaluates security tests on a risk basis in development, release and acceptance. Test results lead to remediation, compensation, risk decision or release blocking. Acceptances show which security requirements were tested and which residual risks remain open.

## Typical risks

- If security tests take place only after completion, findings are expensive, politically difficult or accepted despite risk.
- If tests are not linked to requirements and architecture, they check random points instead of relevant risks.
- If test environments are unlike production, configuration, authorization or integration errors remain undiscovered.
- If findings are not triaged, long lists without decision and without remediation arise.
- If external tests run without scope, rules and follow-up, gaps, operational risks or unclear responsibilities arise.
- If acceptance records do not show open security risks, the Product Owner does not make a real release decision.

## Triggers

- new product, new application, relevant release or new critical function.
- change to authentication, authorization, interfaces, data flows, cryptography, logging or platform.
- new external accessibility, new data class, new tenant separation or new supplier integration.
- security requirement, architecture review, code finding or vulnerability notification.
- penetration test, red-team exercise, bug report, incident or audit finding.
- acceptance before go-live, customer approval, operational handover or material change.
- regular review of the test portfolio for critical applications.

## Roles and responsibilities

- **Product Owner / Service Owner:** decides release, prioritization, acceptance of open findings and business impacts.
- **Test/QA role:** plans test cases, documents results and connects requirements with acceptance.
- **Development team:** remediates findings, adds tests and explains technical causes.
- **Security/AppSec role:** defines test depth, supports triage and assesses critical findings.
- **Architecture role:** reviews whether tests cover relevant trust boundaries, interfaces and data flows.
- **IT operations / Platform team:** ensures testable environments, configuration, logging, monitoring and operational handover.
- **External testers / Service providers:** deliver tests within agreed scope, rules and evidence format.
- **Management:** decides in release conflicts, resource constraints, risk acceptance or recurring critical findings.

## Implementation

### Minimum start

Objective: security-relevant releases are not accepted without traceable review and decision.

1. Critical applications, releases and changes are identified.
2. For these initiatives, security requirements are translated into test or acceptance points.
3. At least basic checks are defined: roles/rights, inputs, error cases, interfaces, logging, secrets, known vulnerabilities.
4. Findings are maintained in a ticket or action log with owner, priority and decision.
5. Before go-live, the Product Owner documents which critical findings are remediated, open, compensated or accepted.
6. Test scope and test results are stored so that they remain traceable later.

Minimum evidence:

- list of security-relevant releases or applications,
- test scope with security requirements,
- test record or tool evidence,
- finding list with decisions,
- acceptance record with open residual risks.

### Solid practice

Objective: security tests are risk-based, repeatable and connected with development and acceptance.

1. Test depth is determined by criticality, exposure, data class, change type and architecture.
2. Test types are combined meaningfully: manual security checks, automated scans, code/dependency checks, API tests, configuration checks, penetration tests or acceptance tests.
3. Test environments, test data and authorizations are provided in a controlled way.
4. Findings are triaged by risk, exploitability, affected scope and operational impact.
5. Release criteria define which findings block and which can be accepted with action or exception.
6. Re-tests or validations confirm remediation of critical findings.
7. Test results feed back into backlog, security requirements, coding guidelines and architecture standards.

Strong evidence:

- risk-based test plan,
- mapping of requirements to test cases,
- test records, scan reports or external test reports with scope,
- finding log with triage and owners,
- re-test or validation evidence,
- release and acceptance decision,
- lessons learned and improvement actions.

### Advanced practice

Objective: security tests provide continuous steering information for product, architecture and operations.

1. Automated tests and security gates are integrated into CI/CD and release processes.
2. Critical systems regularly receive independent or in-depth tests according to a risk-based plan.
3. Test coverage is reviewed against architecture, data flows, threat scenarios and past findings.
4. External tests, internal tool signals and operational monitoring are consolidated into a shared finding and risk picture.
5. Management receives decision-ready metrics on open critical findings, re-test success, exception rate, test coverage and recurring causes.
6. Test methodology is updated after incidents, new attack patterns and technology changes.

## Routine flow

1. **Test trigger arises:** new release, critical change, architecture review, finding or acceptance need.
2. **Define test scope:** define application, functions, interfaces, roles, data, environment and exclusions.
3. **Determine test depth:** consider criticality, exposure, data class, change type and previous findings.
4. **Plan tests:** define requirements, test cases, tools, manual checks, external testers and time windows.
5. **Perform:** execute tests in a controlled way and consider operational risks.
6. **Triage findings:** assess severity, exploitability, business risk, false positives and remediation path.
7. **Treat and validate:** document fix, configuration, compensation, re-test or exception.
8. **Decide acceptance:** approve release, block it or attach a residual-risk decision.
9. **Improve:** feed patterns back into requirements, architecture, coding, operations and test methodology.

## Decisions

- Which applications and changes need which test depth?
- Which findings block release or acceptance?
- Who may accept open findings and for how long?
- When is a re-test mandatory?
- Which tests can be automated and which need manual or external review?
- Which test data and test environments are permissible?
- When does a finding become an incident or management topic?

## Evidence

### Strong evidence

- test strategy or risk-based test plan,
- test scope with assumptions and exclusions,
- mapping of security requirements to test cases,
- test records and tool evidence,
- external test reports with scope and date,
- prioritized findings with owner, deadline and status,
- re-test or validation evidence,
- acceptance decision with open residual risks and follow-up.

### Weak evidence

- scan report without scope, triage or remediation status,
- penetration test report without follow-up,
- acceptance record without open security risks,
- test cases without relation to security requirements,
- blanket statement “QA tested”,
- tool dashboard without release decision.

### Evidence gaps

- no criteria for which releases need security tests,
- critical findings without owner or deadline,
- no validation after remediation,
- test environment differs from production in a security-relevant way without assessment,
- external test results are not transferred into backlog or risk decisions,
- open findings go live without documented acceptance.

## Effectiveness review

Review questions:

- Are security tests planned on a risk basis before relevant releases?
- Are test scope, test depth and exclusions traceable?
- Are tests connected with security requirements, architecture and known risks?
- Are findings prioritized, remediated and validated?
- Are release and acceptance decisions traceable when findings are open?
- Do test results improve requirements, architecture, coding and operations?

Possible metrics:

- share of critical releases with security test evidence,
- open critical findings before go-live,
- re-test success rate,
- mean remediation time by criticality,
- findings without owner or decision,
- recurring finding categories,
- deviations between test scope and production reality.

## BSIG/NIS2 connection point

Security testing in development and acceptance is a connection point for NIS2-oriented topics such as secure development, vulnerability management, risk management, cyber hygiene, incident prevention and protection of digital services. The concrete relationship should be assessed in the requirements register, in risk analyses and in management decisions in an organization-specific way.

This artifact does not replace legal assessment, notification-obligation review or certification assurance.

## Boundaries

- This artifact is not a penetration test methodology and not a tool selection.
- It does not replace technical review by qualified testers for critical systems.
- It does not guarantee that an application is free of vulnerabilities.
- It contains no ISO 27002 texts and no confidential findings.
- It does not replace data protection review for test data, logging or external testers.

## Handoffs

- **Requirements handoff:** missing or untestable security requirements must go back into specification or backlog.
- **Architecture handoff:** findings from trust boundaries, interfaces, data flows or platform design.
- **Secure coding handoff:** code errors, dependency findings, secrets or recurring error classes.
- **Operations handoff:** configuration, logging, monitoring, patchability, test environment and production deviations.
- **Incident handoff:** active exploitation, suspected compromise or critical production finding.
- **Data protection/legal handoff:** test data, external testers, personal logs, contractual or customer commitments.
- **Management handoff:** release despite critical findings, resource shortage, exception decision or recurring structural weaknesses.

## Typical mistakes

- Security testing is understood as a one-off penetration test before launch.
- Tests check tool standards instead of the application's concrete risks.
- Critical findings are closed without re-test or validation.
- Acceptances document functional approval, but no security decision.
- Test data contains real personal or confidential information without clarification.
- External test reports land in storage, but not in the backlog.
- Automated scans block teams without triage and prioritization.

## Fictional mini example

A fictional SaaS provider plans a release with a new API function. Because of external accessibility and role model, a security test is scheduled before go-live. QA creates test cases for authorizations and error responses, AppSec performs API tests, and a scan reports a vulnerable library. The team updates the dependency and validates the fix. A low logging finding is carried into the next sprint with a deadline and documented in the acceptance record.

Evidence:

- risk-based test scope,
- test cases for security requirements,
- API test and scan results,
- ticket and validation for the dependency fix,
- acceptance record with open low finding,
- backlog entry for follow-up work.
