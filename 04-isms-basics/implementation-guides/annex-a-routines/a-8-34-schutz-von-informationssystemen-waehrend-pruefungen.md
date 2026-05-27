# A.8.34 — Protection of information systems during testing and review activities

## Purpose

Examinations, audits, penetration tests, vulnerability scans and technical reviews should make risks visible, but must not themselves create unnecessary risks to availability, confidentiality or integrity. This routine ensures that testing and review activities are planned, authorised, limited, monitored and followed up.

The core is not “testing is allowed”, but safe execution: What is being tested? With which methods? When? Who is informed? Which boundaries apply? How is the organisation to respond if the activity triggers disruptions, data access or security events?

## Control objective in repository language

The organisation operates a routine for safely preparing, approving, performing, accompanying and following up reviews and tests on information systems. It connects test objective, system criticality, operational window, access, data use, monitoring, emergency stop, evidence and action tracking.

## Typical risks

- If active tests run without operational coordination, systems may be overloaded, disrupted or unintentionally changed.
- If testers receive overly broad access, confidential data or production functions may be unnecessarily exposed.
- If test methods, scope or time window are unclear, security monitoring cannot distinguish real attacks from authorised tests.
- If tests take place during critical periods, they increase operational and crisis risks.
- If findings contain confidential technical details and are shared insecurely, new attack surfaces arise.
- If stop criteria are missing, response to disruptions comes too late.

## Triggers

- internal or external audit with technical system review.
- penetration test, red-team exercise, vulnerability scan, configuration review or load/security test.
- customer, supplier or regulatory request involving testing activities.
- new critical application, major architecture change or go-live review.
- incident lessons learned, vulnerability wave or management mandate.
- recurring test plan for critical systems.
- change of test scope, method, service provider or time window.

## Roles and responsibilities

- **Test sponsor / Audit Owner:** defines test objective, scope, expectations and use of results.
- **Asset Owner / Service Owner:** assesses operational risk, approval, time window and stop criteria.
- **IT / Platform Owner:** prepares technical access, monitoring, backup/rollback readiness and support.
- **Security role / ISMS Owner:** coordinates test boundaries, rules of engagement, finding triage and action tracking.
- **Testers / external service provider:** comply with scope, method, reporting channels, confidentiality and stop rules.
- **Data Protection / Legal:** reviews personal data, logging, confidentiality, contractual and liability questions.
- **Management:** decides on tests of particularly critical systems, residual risks, resources and publication of results.

## Implementation

### Minimum start

Goal: technical testing activities run only with a clear mandate, scope and operational safeguards.

1. Each active test receives a test profile: objective, scope, systems, method, period, testers, contacts and stop criteria.
2. Asset Owner and IT/Platform Owner confirm that timing and method fit the operational risk.
3. Access for testers is set up for a specific purpose, time-limited and traceable.
4. Monitoring, service desk or incident role are informed so that test activities can be classified.
5. Critical or production systems receive clear boundaries: no destructive tests without special approval, no data extraction without clarification.
6. Findings are handed over securely, prioritised and tracked in actions.

Minimum evidence:

- test profile or rules of engagement,
- approval by Asset/Service Owner,
- access evidence for testers,
- information to operations/SOC/service desk,
- finding list with owners,
- closure or follow-up note.

### Solid practice

Goal: testing and review activities are part of a risk-based testing and improvement process.

1. Test types are distinguished: passive review, authenticated scan, active penetration test, social/physical component, red-team exercise, load test.
2. For each test type, minimum requirements are defined for scope, approval, method, time window, data handling and stop.
3. Critical systems are tested with operational windows, communication plan and readiness to respond to disruptions.
4. Test accounts, IP addresses, tools and permitted techniques are documented.
5. Sensitive findings and technical details are shared in protected channels and with a limited recipient group.
6. After completion, access is withdrawn, logs are reviewed, findings are prioritised and actions tracked.
7. Recurring findings flow back into architecture, vulnerability management, secure development or operations.

Strong evidence:

- approved test plan,
- rules of engagement,
- operational approval and communication evidence,
- access and test account log,
- monitoring/stop readiness,
- findings with risk, owner and deadline,
- evidence of access withdrawal after testing.

### Advanced practice

Goal: testing improves security measurably without endangering operations in an uncontrolled way.

1. Test planning is connected with asset criticality, threat situation, vulnerability management and release planning.
2. Technical test environments, staging or controlled production windows are chosen according to risk.
3. SOC/monitoring can mark test activities and still detect real anomalies.
4. Testers receive temporary identities, controlled access paths and secure result repositories.
5. Findings are transferred automatically or structurally into risk, ticket and action management.
6. Lessons learned review not only findings, but also test execution: disruptions, false alarms, communication gaps, overly broad access.
7. Management receives a decision-ready view of critical findings, remediation backlog, test coverage and accepted residual risks.

## Routine flow

1. **Test need arises:** audit plan, penetration test, go-live, incident lesson learned, customer question or management mandate.
2. **Define scope:** clarify systems, interfaces, environments, data, methods, exclusions and test depth.
3. **Assess risk:** review operational impact, data access, criticality, time window, dependencies and emergency capability.
4. **Obtain approval:** involve Asset Owner, Platform Owner, Security and, where needed, Management, Data Protection or Legal.
5. **Prepare execution:** define test accounts, IPs, contacts, communication plan, monitoring, stop criteria and secure storage.
6. **Accompany test:** observe activities, report disruptions, stop scope deviations or re-approve them.
7. **Secure results:** hand over findings in a protected way, prioritise and assign actions.
8. **Follow up:** withdraw access, review logs, assess the test and document lessons learned.
9. **Improve:** feed findings and execution problems back into operations, development, architecture and risk management.

## Decisions

- Which testing methods are permissible for production systems?
- When must testing be done in test/staging instead of production?
- Who may approve destructive, invasive or data-intensive tests?
- Which systems, time windows or functions are excluded for operational reasons?
- Which data may testers view, store or export?
- Which findings must be escalated immediately as an incident or management topic?
- When are testing risks assessed as higher than the benefit of the test?

## Evidence

### Strong evidence

- test mandate with objective, scope, method, period and responsible persons,
- approved rules of engagement,
- operational and security approval,
- communication evidence to SOC, service desk or operations,
- test account/access evidence with time limit,
- protected finding handover,
- action log with owners and deadlines,
- closure note including access withdrawal and lessons learned.

### Weak evidence

- test report without prior approval or scope,
- calendar entry “pentest” without method and contact information,
- generic admin access for testers,
- findings via unprotected distribution list,
- scan log without operational coordination,
- final report without action tracking.

### Evidence gaps

- unknown testing activities in the production network,
- no stop criteria or emergency contacts,
- no clarification of data access,
- test accounts remain active after completion,
- critical findings without owner or deadline,
- monitoring cannot distinguish test activities from attacks,
- no follow-up of disruptions caused by testing.

## Effectiveness review

Review questions:

- Is there an approved scope and clear boundaries for active tests?
- Are Asset Owner, operations and Security informed and able to decide before testing starts?
- Is test access time-limited and withdrawn after completion?
- Are stop criteria and emergency contacts known?
- Are sensitive findings shared in a protected way and tracked?
- Have tests led to improvements, not only reports?
- Were disruptions, false alarms or scope deviations followed up?

Possible metrics:

- share of active tests with complete test profile,
- test accounts still active after completion,
- critical findings without owner or deadline,
- disruptions caused by testing,
- overdue actions from tests,
- recurring findings,
- tests without follow-up.

## BSIG/NIS2 connection point

The protection of information systems during testing and review activities is connectable to NIS2-oriented topics such as risk management, security testing, vulnerability handling, incident prevention, cyber hygiene and secure operations. The concrete connection should be assessed organisation-specifically in the requirements register, test plan and management review.

This artefact does not replace legal, data protection or contractual assessment of testing activities and sharing of results.

## Boundaries

- This artefact is not a complete penetration testing standard and not a technical test methodology.
- It does not replace legal review of test approvals, liability, data protection or customer communication.
- It does not guarantee safe or disruption-free testing.
- It contains no ISO 27002 texts and no confidential system or vulnerability details.
- It must not be used as approval for destructive tests without a human decision.

## Handoffs

- **Operations/service handoff:** production systems, maintenance windows, monitoring, disruption readiness and stop criteria.
- **Security/SOC handoff:** test activities, source IP addresses, time windows, permitted techniques and incident distinction.
- **Data protection/legal handoff:** access to personal data, data exports, contracts, confidentiality, liability or sharing of results.
- **Vendor handoff:** external testers, subcontractors, tool use, evidence and secure result storage.
- **Incident handoff:** active exploitation, unexpected critical vulnerability, suspected data leakage or disruption caused by testing.
- **Change/release handoff:** testing in the go-live context, test window, rollback and action implementation.
- **Management handoff:** testing of critical systems, high residual risks, non-remediable findings or publication of results.

## Typical mistakes

- Penetration tests start without operational contact and stop rule.
- Testers receive broad permanent access that remains active after completion.
- The test report is filed, but findings are not controlled.
- Critical tests run during peak load or blackout periods.
- SOC/monitoring is not informed and treats tests either as false alarms or misses real attacks.
- Sensitive findings are distributed too broadly.
- For fear of disruptions, only harmless tests are performed, so relevant risks remain invisible.

## Fictional mini example

A fictional operator of a customer portal plans an external penetration test. The Security Owner creates rules of engagement with scope, test window, permitted methods, contact chain and stop criteria. The Service Owner excludes a peak-load time window. The SOC receives source IP addresses and test times. After the test, two critical findings are transferred into tickets, the test accounts are disabled and a short follow-up is documented. A finding on insecure session configuration is additionally incorporated into the secure development standard.

Evidence:

- test mandate and rules of engagement,
- operational approval,
- SOC communication,
- test account log,
- finding tickets,
- access withdrawal,
- lessons-learned note.
