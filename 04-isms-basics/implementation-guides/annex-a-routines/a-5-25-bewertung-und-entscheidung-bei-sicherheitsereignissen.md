# A.5.25 — Assessment and decision-making for security events

## Purpose

Security events become manageable only through assessment and decision-making. This routine helps to avoid handling reports, alerts, notices, or suspicions in an unordered way, and instead triage them traceably: What happened? How severe is it? Who decides? Does it become a security incident, a risk, an action, or a false alarm?

## Control objective in repository language

The organization operates a triage and decision routine for security events. Events are recorded, assessed, classified, prioritized, and handed over to the appropriate handling path. Decisions remain traceable, especially when escalated, closed, observed, or treated as an incident.

## Typical risks

- If events are not assessed, real incidents remain buried in alert noise.
- If every event is treated the same way, teams become overloaded and critical cases are delayed.
- If classification and decision are not documented, it is later not traceable why escalation did not happen.
- If data protection, Legal, or management are involved too late, decision and communication risks arise.
- If false alarms are not evaluated, detection does not improve.

## Triggers

- security report from employees, customers, suppliers, or external parties.
- monitoring, SIEM, EDR, cloud, IAM, network, or application hit.
- vulnerability notice with suspected exploitation.
- unusual behavior, suspected data leakage, account compromise, or policy violation.
- result from audit, test, exercise, or service provider notification.
- new information about an already assessed event.

## Roles and responsibilities

- **Triage Owner / Security role:** receives events, assesses initial information, and proposes classification.
- **Incident Lead:** takes over when the event is treated as a security incident or escalation is needed.
- **IT/platform owner:** provides technical classification, logs, system status, and initial containment options.
- **Service Owner / Business function:** assesses business and process impact.
- **ISMS owner / Risk owner:** connects events with risks, actions, and lessons learned.
- **Legal / Data protection:** assesses legal, data protection, or reporting-duty proximity requiring review.
- **Management:** decides on high impact, residual risk, external communication, resources, or crisis potential.

## Implementation

### Minimum start

Goal: every relevant event is recorded, assessed, and decided traceably.

1. An intake channel for security events is defined.
2. A simple triage template records source, time, affected systems, initial indications, possible impact, and immediate need.
3. A small assessment scheme distinguishes at least: false alarm, observation, security event with action, security incident with escalation.
4. For every assessment, a decision is documented: close, investigate further, escalate, create action, or start incident.
5. Data protection/legal and management handoffs are marked as stop points.
6. Events are regularly reviewed for patterns and recurring causes.

Minimum evidence:

- event log or ticket list,
- triage decision,
- classification,
- handoff to action or incident,
- documented closure reason for false alarm,
- escalation evidence for critical cases.

### Solid practice

Goal: assessment and decision-making become consistent, risk-based, and reviewable.

1. Severity levels are defined based on technical indications, data reference, exposure, business impact, and spread potential.
2. Triage deadlines are based on severity and criticality.
3. Events are linked with assets, service owners, data classes, and risks.
4. Classification decisions are safeguarded by four-eyes principle or review for critical cases.
5. Events with personal data reference, suspected data leakage, customer impact, or proximity to external reporting duties trigger human review.
6. Recurring events lead to detection improvement, training, vulnerability treatment, or risk adjustment.

Strong evidence:

- defined classification and severity logic,
- event tickets with assessment and decision,
- log or analysis excerpts with case reference,
- handoffs to incident response, change, IAM, data protection, or supplier management,
- review of false alarms and recurring patterns,
- management decision for critical or ambiguous cases.

### Advanced practice

Goal: event assessment is part of a resilient security situation picture.

1. Monitoring, ticketing, asset data, criticality, and incident process are connected.
2. Correlations help to combine individual events into incident patterns.
3. Runbooks support frequent triage cases without replacing human decision-making at critical points.
4. Metrics show assessment quality: time to triage, escalation rate, false alarm rate, reopened cases, critical events without owner.
5. Lessons learned improve detection rules, playbooks, training, and risk assessment.

## Routine flow

1. **Record event:** document source, time, reporter, affected systems, and initial facts.
2. **Perform initial review:** assess plausibility, urgency, known patterns, and immediate danger.
3. **Add context:** check asset, owner, data class, user, supplier, logs, and current situation.
4. **Define severity:** assess possible impact, spread, data reference, and operational relevance.
5. **Make decision:** close, observe, start technical action, record risk, or escalate incident.
6. **Trigger handoffs:** involve incident, data protection, Legal, management, supplier, IAM, BCM, or change.
7. **Secure evidence:** document assessment, decision rationale, and handoff.
8. **Review:** evaluate samples, false alarms, and recurring events.

## Decisions

- Which events are escalated immediately?
- Which criteria turn an event into a security incident?
- Who may close an event and when is four-eyes review needed?
- When are data protection, Legal, communication, or management involved?
- Which information is sufficient for a decision, and which must be requested?
- When does a recurring event become a risk or action problem?

## Evidence

### Strong evidence

- event log with source, time, owner, and status,
- documented triage decision with rationale,
- classification and severity,
- technical analysis or log references,
- handoffs to incident, action, risk, or human review,
- closure decision for false alarm,
- evaluation of recurring patterns.

### Weak evidence

- alert export without decision,
- chat history without ticket or owner,
- severity only from tool score without context,
- closed report without rationale,
- monthly number of events without quality assessment.

### Evidence gaps

- events without central intake,
- no criteria for escalation,
- no connection to assets or data classes,
- no traceable decision,
- no Legal/data protection review despite data reference,
- recurring false alarms without improvement.

## Effectiveness review

Review questions:

- Are security events captured reliably?
- Is it traceable from samples why escalation or closure happened?
- Are critical events triaged quickly enough?
- Are owners, assets, and data reference visible?
- Are human-gate points triggered in time?
- Do patterns from events lead to improvements in detection, training, or actions?

Possible metrics:

- time to initial triage by severity,
- share of events with documented decision,
- escalation rate to incident response,
- false alarm rate and recurring false alarms,
- events without owner,
- overdue triage cases.

## BSIG/NIS2 connection point

Assessment and decision-making for security events is a connection point for NIS2-oriented topics such as incident handling, detection, reporting and escalation capability, risk management, and management responsibility. Whether a concrete event triggers legal reporting duties or data protection duties must be assessed case by case by responsible humans.

This artifact does not replace legal advice or a binding assessment of reporting duties.

## Boundaries

- No legal classification of incidents or personal data breaches.
- No replacement for forensic analysis, incident response, or crisis communication.
- No statement that a triage decision is regulatorily sufficient.
- No ISO 27002 texts or certification commitment.
- No real incident, customer, person, or log data in public examples.

## Handoffs

- **Incident handoff:** event meets defined criteria for incident, spread, compromise, or high impact.
- **Data protection/legal handoff:** personal data reference, suspected data leakage, customer impact, proximity to reporting duties, or labor-law questions.
- **IAM handoff:** account anomaly, privilege misuse, suspicious login, or technical identity misuse.
- **Change/operations handoff:** technical correction, configuration change, patch, or blocking action.
- **Supplier handoff:** provider event, SaaS alert, managed service notice, or missing information.
- **BCM/crisis handoff:** possible significant business interruption or crisis potential.
- **Management handoff:** high impact, resource need, external communication, residual risk, or unclear decision situation.

## Typical mistakes

- Alerts are collected but not decided.
- Tool severity levels replace context assessment.
- Critical events get lost in chat channels.
- False alarms are closed without improving detection rules.
- Data protection or Legal are involved only after external communication.
- Triage decisions are not auditable.
- Recurring events are not translated into risks or actions.

## Fictional mini example

A fictional monitoring system reports several failed admin logins from an unusual country. The Triage Owner records the event, checks asset criticality and log context, and shortly afterwards identifies a successful login. The case is escalated as a possible security incident. The Incident Lead starts account blocking and analysis; data protection and management are marked as human gates because data may be affected.

Evidence:

- event ticket,
- log references,
- triage decision with severity,
- handoff to incident response,
- documented human-gate marking,
- action status.
