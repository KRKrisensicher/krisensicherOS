# A.8.15 — Logging

## Purpose

Logging ensures that security-relevant events in systems, applications, identity services and platforms become traceable. Its value is not in collecting as many logs as possible, but in an operable routine: capturing relevant events, protecting them, keeping them evaluable and making them usable for investigations, reviews and decisions.

## Control objective in repository language

The organization defines which events are logged for operational security, access protection, error analysis, incident response and traceability, who is responsible for log sources, how logs are protected and retained, and when log data leads to a review, escalation or improvement action.

## Typical risks

- If critical systems do not generate usable logs, attacks, operating errors or outages cannot be traced.
- If log sources are configured inconsistently, blind spots emerge between endpoints, servers, cloud, network and applications.
- If logs remain unprotected, attackers can alter or delete traces.
- If too much irrelevant data is collected, relevant events are lost and privacy/retention questions become unnecessarily complex.
- If personal or employee data is processed without clarified rules, legal and trust-related risks arise.
- If retention periods, access and deletion are unclear, logs may be unavailable in an emergency or retained longer than necessary.

## Triggers

- New or materially changed system, application, cloud service or identity process.
- New incident, suspected misuse or lessons learned from an investigation.
- Introduction or change of SIEM, EDR, monitoring, IAM, network or cloud logging.
- New data class, new interface or new administrative role.
- Audit finding, internal review or management question on traceability.
- Regular review of log sources, retention, access and evaluability.
- Supplier or managed service change affecting log availability or release.

## Roles and responsibilities

- **IT/platform owner:** operates log sources, forwarding, storage, protection mechanisms and technical availability.
- **Service owner / application owner:** defines functionally relevant events, error events and security events for the service.
- **Security role / ISMS owner:** defines minimum requirements, priorities, review logic and escalation paths.
- **Incident response role:** uses logs for triage, investigation and lessons learned.
- **Data protection/legal role:** checks organization-specific requirements where personal data, employee context, retention or evaluation purposes are involved.
- **Supplier management:** clarifies log access, release, retention and responsibilities for externally operated services.
- **Management:** decides on resource needs, residual risks, missing coverage or conflicts between transparency, effort and protective rights.

## Implementation

### Minimum start

Goal: Critical systems have usable, protected and findable logs.

1. Name critical log sources in scope: identity service, central servers, internet-exposed services, core applications, firewalls, VPN, cloud admin layer.
2. Define owner, purpose, event types and storage location for each log source.
3. Define minimum events, for example sign-in events, failed access attempts, administrative actions, permission changes, security-relevant configuration changes and system errors.
4. Limit access to logs and prevent modification/deletion by unauthorized roles.
5. Define retention and deletion pragmatically and set a review date.
6. Maintain simple evidence: log source list, configuration excerpt, sample check and open gaps.

### Solid practice

Goal: Logging is risk-based, repeatable and connected to incident response.

1. Logging requirements are defined by system class: endpoints, servers, applications, cloud, network, identity, databases.
2. Log forwarding, timestamps, integrity protection and roles for access/evaluation are documented.
3. Missing or failing log sources are detected and treated as operational deviations.
4. Log access and evaluations are limited to authorized purposes and roles.
5. Retention, deletion and release are checked with data protection/legal when personal or employee data is affected.
6. Incident playbooks state which logs are needed in typical scenarios.
7. Regular samples check whether logs are complete, readable and usable for investigations.

### Advanced practice

Goal: Logs are used as a reliable basis for situational awareness, detection, forensic readiness and management decisions.

1. Critical log sources are centrally connected, normalized and linked with asset, identity and service context.
2. Tamper protection, separated permissions and tiered retention are technically implemented.
3. Use cases for detection, incident response and compliance-related traceability are maintained and tested.
4. Log coverage and outages are monitored and reported.
5. Cloud, SaaS and supplier logs are considered in responsibilities, contracts and operating routines.
6. Findings from incidents, tests and reviews improve log scope, quality and evaluation.
7. Management receives decision-ready statements on blind spots, costs, risks and required capabilities.

## Routine flow

1. **Determine scope:** define critical systems and relevant events.
2. **Set up log source:** enable events, configure forwarding, secure time reference.
3. **Define protection:** regulate access, protection against modification, retention and deletion.
4. **Check sample:** do relevant actions actually create evaluable entries?
5. **Monitor operations:** treat log outages, missing sources or storage problems as deviations.
6. **Use evaluation:** review specifically during incidents, reviews, vulnerability situations or management questions.
7. **Decide on gaps:** hand missing coverage, costs or legal questions to suitable handoffs.
8. **Improve:** feed findings from incidents, exercises and reviews back into logging requirements.

## Decisions

- Which systems and events are indispensable for traceability and incident response?
- Which log data is collected centrally, and which remains local or with the service provider?
- Who may administer logs, who may evaluate them, and who may approve exceptions?
- How long is log data needed for different purposes?
- Which blind spots are accepted, compensated for or closed with priority?
- When is log evaluation a security topic, and when does it need data protection/legal review?
- Which costs for storage, tooling and operations are risk-appropriate?

## Evidence

### Strong evidence

- Current log source list with owner, purpose, event types and criticality,
- configuration evidence for central log sources and forwarding,
- samples showing evaluable events,
- access concept for log administration and log evaluation,
- evidence of retention, deletion and protection against unauthorized modification,
- incident or exercise evidence in which logs were actually used,
- documented decisions on gaps, exceptions and improvements.

### Weak evidence

- General logging policy without system reference,
- tool screenshot without statement on coverage,
- log files without owner, time reference or search capability,
- blanket statement “logs are collected” without event types and retention,
- SIEM operation without evidence that critical sources are connected,
- retention periods without reference to purpose and review.

### Evidence gaps

- No list of critical log sources,
- unclear responsibility for log outages,
- no check of readability or completeness,
- no rule for access to log data,
- no coordination for personal or employee data,
- external services without clarified log availability,
- no decision on known blind spots.

## Effectiveness review

Review questions:

- Are the most important identity, network, cloud, server and application systems covered?
- Can relevant security events be found promptly and assigned to a system, account or service?
- Are logs protected against unauthorized modification and unauthorized access?
- Are log outages or missing sources detected and treated?
- Has the usability of logs been checked in incident exercises or samples?
- Have retention, deletion and evaluation for sensitive log data been reviewed by humans?
- Are identified gaps prioritized, decided and tracked?

Possible metrics:

- Coverage of critical log sources,
- share of active and error-free log forwarders,
- unresolved log gaps by criticality,
- time until a log source is connected after a new system is introduced,
- log outages per month,
- share of incident exercises with sufficient log situation.

## BSIG/NIS2 connection point

Logging can connect to NIS2-oriented topics such as risk management, detection, incident handling, access protection, operational monitoring and traceability of security-relevant events. The concrete connection should be assessed organization-specifically in the requirements register, risk analysis and incident response concept.

This artifact does not replace legal assessment of logging, employee data, reporting obligations or evidence obligations.

## Boundaries

- This artifact is not a SIEM architecture, not a forensic policy and not a data protection review.
- More logs do not automatically mean better security; purpose, quality and evaluability are decisive.
- Log data must not be used as public examples or test data with real personal, customer or secret data.
- No certification, conformity or security guarantee.
- No adoption of licensed standard texts.

## Handoffs

- **Incident handoff:** suspected misuse, compromise, manipulation or missing log situation during an incident.
- **Data protection/legal handoff:** personal data, employee context, purpose change, retention, release or evaluation scope.
- **Service/platform handoff:** missing log source, broken forwarding, storage/cost problem or technical protection measure.
- **Supplier handoff:** logs reside with SaaS, managed service or outsourcing partner and are not sufficiently available.
- **Management handoff:** accepted blind spots, budget for central evaluation, storage or personnel.
- **Audit/evidence handoff:** log coverage, access, retention or samples are not traceable.

## Typical mistakes

- Logs are collected, but nobody checks coverage or usability.
- Critical systems are missing while non-critical systems generate large data volumes.
- Administrators can alter logs without this being noticed.
- Retention is technically preset but never decided.
- Data protection questions are first asked during an incident.
- Supplier logs are contractually or practically unavailable.
- Management sees data volume, but no statement on blind spots and risk.

## Fictional mini example

A fictional mid-sized company operates a customer portal and a central identity service. After an incident exercise, the team finds that administrative role changes in the portal cannot be found centrally. The service owner adds these events to the log source list, the platform team enables forwarding and the security role checks a sample. Data protection is involved because user identifiers and employee accounts appear in the logs. A remaining gap in a SaaS service is handed to supplier management and presented as an open residual risk in the next management review.
