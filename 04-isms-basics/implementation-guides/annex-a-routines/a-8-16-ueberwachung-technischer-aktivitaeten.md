# A.8.16 — Monitoring technical activities

## Purpose

Monitoring technical activities makes security-relevant behavior in systems, networks, applications, cloud environments and administrative processes visible in time. The focus is not on continuous observation for its own sake, but on clear use cases, permissible evaluations, response to anomalies and decision-ready steering.

## Control objective in repository language

The organization operates a routine through which selected technical activities are monitored, anomalies are assessed, responses are triggered and blind spots are improved. Monitoring is connected with logging, incident response, access protection, data protection/legal review and management decisions.

## Typical risks

- If technical activities are not monitored, attacks, misconfigurations or misuse remain undetected until damage occurs.
- If monitoring runs without defined use cases, many alerts arise without response and relevant signals are lost.
- If alert rules are not maintained, they no longer fit new systems, threats or business processes.
- If nobody is responsible for triage, warnings are generated but not assessed.
- If monitoring interferes with employee or customer data without checked boundaries and purposes, legal and trust risks arise.
- If external services remain outside monitoring, a false situational picture emerges.

## Triggers

- New or changed critical system, network segment, cloud account, identity service or SaaS service.
- New monitoring hit, incident, near miss or lessons learned.
- New vulnerability, threat situation or attack indicator.
- Change of roles, privileged accounts, interfaces or data classes.
- Introduction or adjustment of SIEM, EDR, NDR, cloud security monitoring or operational monitoring.
- Regular review of use cases, alert quality, response times and blind spots.
- Audit finding, customer requirement or management question on detection capability.

## Roles and responsibilities

- **Security operations / security role:** defines monitoring use cases, triage criteria, escalation paths and quality review.
- **IT/platform owner:** provides telemetry, sensors, agents, log forwarding and technical operability.
- **Service owner / application owner:** assesses functional context, criticality and permissible response measures.
- **Incident response role:** takes over confirmed suspected cases and carries out investigation or containment.
- **Data protection/legal role:** checks purposes, boundaries and evaluations involving personal or employee-related data.
- **Supplier management:** clarifies monitoring interfaces, alerts and responsibilities for external services.
- **Management:** decides on missing coverage, resource needs, accepted risks or conflicts of objectives.

## Implementation

### Minimum start

Goal: The most important technical activities of critical systems are monitored with a clear response.

1. Name critical monitoring areas: identity, privileged actions, internet-exposed systems, malware/EDR alerts, backup errors, cloud admin activities, network access.
2. For each area, define: signal source, owner, alert criterion, triage role and escalation path.
3. Start a small number of relevant use cases instead of activating many unreviewed alerts.
4. Track alerts in a ticket, incident or review log.
5. Make false positives, unhandled alerts and missing sources visible in review.
6. Define a data protection/legal handoff before personal evaluations are used regularly.

### Solid practice

Goal: Monitoring becomes repeatable, risk-based and connected to incident response.

1. Monitoring use cases are prioritized by risk, asset criticality and expected response.
2. Alert rules have owner, purpose, data sources, thresholds, triage steps and escalation criteria.
3. Triage results are documented: confirmed, harmless, false positive, technical fault, improvement need.
4. Response times and handover into incident response are defined.
5. Use cases are updated after incidents, vulnerabilities, architecture changes and new services.
6. Monitoring outages, missing agents or data sources are treated as operational deviations.
7. Regular reviews consider alert quality, blind spots, workload and decision needs.

### Advanced practice

Goal: Monitoring provides a reliable technical situation picture and supports fast, appropriate response.

1. Log, EDR, network, cloud, identity and application signals are correlated.
2. Use cases are connected with threat intelligence, attack paths, vulnerability situation and critical business services.
3. Automated responses are limited based on risk and have human approval or review points where impacts may be significant.
4. Detection engineering maintains rules, tests, tuning and version history.
5. Exercises and purple-team-like tests check whether relevant activities are detected and handled.
6. Metrics show not only alert volume, but coverage, quality, response capability and open decisions.
7. Supplier and SaaS signals feed into the situation picture as far as contractually and technically possible.

## Routine flow

1. **Select use case:** determine risk, asset and expected response.
2. **Check data source:** check log, agent, sensor or supplier alert for availability and quality.
3. **Set up rule:** define alert criterion, threshold, context and owner.
4. **Define triage:** describe initial check, priority, escalation path and documentation.
5. **Observe operation:** track hits, false alarms, outages and unhandled alerts.
6. **Escalate:** hand confirmed suspected cases to incident response or service owner.
7. **Conduct review:** assess alert quality, blind spots, new risks and workload.
8. **Improve:** tune rule, add data source, change playbook or prepare management decision.

## Decisions

- Which technical activities must be monitored because they have high security or operational impact?
- Which alerts trigger immediate triage and which only trigger review or trend analysis?
- Who may block systems, disable accounts or secure data in confirmed anomalies?
- How are false positives, alert fatigue and scarce security capacity managed?
- Which monitoring gaps are accepted, compensated for or closed with priority?
- Which evaluations require data protection/legal review or involvement of additional bodies?
- Which external services must provide alerts and how is their quality assessed?

## Evidence

### Strong evidence

- Prioritized list of monitoring use cases with owner, data source and response,
- alert rule or detection documentation with change history,
- tickets or incident evidence from monitoring hits,
- review records on false positives, blind spots and rule adjustments,
- evidence of monitoring coverage for critical systems,
- exercise or test evidence on detection capability,
- management decisions on resources, accepted gaps or tooling.

### Weak evidence

- Dashboard screenshot without use-case and response reference,
- large alert statistics without triage quality,
- tool has been purchased, but no sources or owners are named,
- generic alert rules without adaptation to critical services,
- alerts are distributed by email but not tracked,
- supplier promises monitoring without evidence or reporting.

### Evidence gaps

- No defined monitoring use cases,
- unclear triage responsibility,
- no review of alert quality and false alarms,
- unknown coverage of critical systems,
- no treatment of monitoring outages,
- no data protection/legal review for sensitive evaluations,
- confirmed anomalies without incident or action handoff.

## Effectiveness review

Review questions:

- Are there concrete monitoring use cases for the most important technical risks?
- Are alerts actually triaged and documented?
- Can critical systems, privileged actions and identity events be monitored?
- Is alert quality improved regularly?
- Are monitoring outages and missing data sources visible?
- Do confirmed anomalies lead to incident response, actions or management decisions?
- Are evaluation purposes and boundaries for sensitive data clarified?

Possible metrics:

- Coverage of critical monitoring use cases,
- share of alerts handled within defined time,
- confirmed security events from monitoring,
- false-positive rate per use case,
- open monitoring gaps by criticality,
- time from signal to triage,
- rule age without review.

## BSIG/NIS2 connection point

Monitoring technical activities can connect to NIS2-oriented topics such as detection, incident handling, cyber hygiene, access protection, risk management and operational capability. The concrete connection should be assessed organization-specifically in the requirements register, incident response concept and risk analysis.

This artifact does not replace legal assessment of monitoring measures, employee data, reporting obligations or evidence obligations.

## Boundaries

- This artifact is not a SOC operations manual and not a technical SIEM rule library.
- Monitoring does not replace prevention, vulnerability management or clear incident responsibility.
- Automated responses need clear boundaries, tests and human review points.
- No legal advice, no data protection advice, no certification commitment.
- No use of real log, customer, personal or secret data in public examples.

## Handoffs

- **Incident handoff:** confirmed suspicion, active exploitation, malware, account misuse or significant anomaly.
- **Data protection/legal handoff:** personal evaluation, employee context, purpose change, monitoring boundaries or release.
- **Platform/service handoff:** missing data source, broken agent, misconfigured rule or affected service context.
- **Supplier handoff:** external services do not provide sufficient signals, reports or escalation paths.
- **Management handoff:** critical monitoring gaps, resource bottleneck, tooling decision or accepted residual risk.
- **Audit/evidence handoff:** use cases, triage or reviews are not traceable.

## Typical mistakes

- Monitoring is confused with buying a tool.
- There are many alerts but no triage responsibility.
- Rules are never adapted to new systems or threats.
- False positives are tolerated until teams ignore alerts.
- Sensitive evaluations start without clarified purpose and human review.
- Supplier alerts remain outside the situation picture.
- Management receives alert volumes, but no statement on risk, coverage and decision needs.

## Fictional mini example

A fictional service provider introduces cloud admin accounts for its product platform. The trigger is the new privileged role. Security and the platform team define a monitoring use case: sign-in without MFA, role change and access from an unusual region create a triage ticket. After two weeks, the review shows several false alarms due to business travel IPs. The rule is adjusted, data protection checks the evaluation purpose, and an open gap in a SaaS admin log goes to supplier management.
