# A.7.4 — Physical security monitoring

## Purpose

Physical security monitoring ensures that relevant events at sites, access points and protected areas do not go unnoticed. The value is not in the existence of cameras, sensors or guard patrols, but in a clarified routine: what is observed, why, by whom, how responses are made and which evidence is created?

## Control objective in repository language

The organisation operates an appropriate monitoring routine for physical security events at sites and protected areas. It connects risk analysis, monitoring means, response paths, data protection/legal handoffs, service provider management, review and management decisions.

## Typical risks

- If unauthorised access attempts, door alarms or tampering are not detected, attacks or misconduct remain without response.
- If monitoring technology exists but no one assesses alarms, it creates false assurance.
- If camera, access or sensor data are processed without clear purposes, data protection, acceptance and governance problems arise.
- If service provider alarms are not connected with internal escalation paths, critical events are lost during handovers.
- If recordings are not protected or are retained too long, they can become a risk themselves.

## Triggers

- New site, new protected area or changed access logic.
- Security event, break-in, suspected sabotage, vandalism, theft or repeated false alarms.
- Introduction, change or shutdown of camera, alarm, sensor or access systems.
- Change of security service, reception, facility provider or control centre.
- Data protection/legal review, works council/co-determination question or complaint.
- Regular test of alerting, response time or recording access.
- Audit finding, risk analysis, BCM review or management decision.

## Roles and responsibilities

- **Site / Facility Owner:** responsible for monitoring needs, operation of physical systems and service provider coordination.
- **Security / ISMS Owner:** defines risk logic, event categories, escalation paths and review requirements.
- **Data protection / Legal:** reviews purposes, legal bases, information for affected persons, retention, access and co-determination questions.
- **Security service / Control centre / Reception:** assesses events according to specification and escalates defined cases.
- **IT / Platform Owner:** supports system protection, logging, interfaces and access to monitoring systems.
- **Incident Response:** takes over in cases of suspected attack, sabotage, information leakage or connection with cyber events.
- **Management:** decides on investments, residual risks, monitoring scope and conflicts of objectives.

## Implementation

### Minimum start

Goal: critical physical events are detected, assessed and escalated in a traceable way.

1. The organisation identifies the sites and areas where physical monitoring is relevant.
2. For each area, it defines which events are important: door open, access outside time window, intrusion alarm, technical room opening, supplier access.
3. Existing monitoring means are recorded: reception, patrol, access system, alarm system, camera, sensor, service provider notification.
4. A simple event and escalation logic describes who is informed and when.
5. A data protection/legal handoff is triggered as soon as personal monitoring data are processed.
6. At least one regular function test or review checks whether notification and response work.

Minimum evidence:

- Scope of monitored areas,
- event and escalation matrix,
- service provider or operating instruction,
- test or alarm log,
- data protection/legal clarification if personal data are affected.

### Solid practice

Goal: monitoring is operated in a risk-based, response-capable and controlled way.

1. Monitoring purposes are documented per area and linked to risks.
2. Event categories receive response deadlines, escalation points and documentation requirements.
3. Access to recordings, alarm data and systems is limited, logged and reviewed regularly.
4. False alarms, missed responses and technical faults are evaluated.
5. Service provider performance is managed through defined reporting channels, reports and review dates.
6. Retention, deletion and evaluation of personal data are clarified with Legal/Data Protection.
7. Results flow into site, access, incident and BCM reviews.

Strong evidence:

- Risk-related monitoring scope,
- event/escalation matrix,
- alarm or patrol logs with response,
- test evidence for alarms and reporting chains,
- access review for monitoring systems,
- data protection/legal approval or review note,
- measures from faults or false alarms.

### Advanced practice

Goal: physical monitoring supports situational awareness, incident response and site resilience without excessive control.

1. Alarm, access, sensor and service provider notifications are integrated into an agreed situational and escalation model.
2. Critical events are connected with cyber incident triage, BCM and crisis communication.
3. Technical systems are protected against tampering, outage and unauthorised access.
4. Metrics show response times, false alarm rate, open faults, unresolved events and service provider performance.
5. Exercises test reporting chains outside regular business hours.
6. Monitoring scope is regularly reviewed against purpose limitation, proportionality, risk and acceptance.

## Routine flow

1. **Monitoring need emerges:** site, room, event, risk or service provider changes.
2. **Determine purpose and scope:** which areas and events should be monitored, and for what reason?
3. **Check data protection/legal handoff:** clarify personal reference, recording, evaluation, employee context and retention.
4. **Define event logic:** define category, response path, escalation, documentation and responsible persons.
5. **Ensure operation:** set up technology, service provider, reception or patrol routine.
6. **Handle events:** assess alarm, respond, document and, if necessary, trigger an incident.
7. **Protect evidence:** limit and keep traceable access to logs and recordings.
8. **Review effectiveness:** perform tests, samples, false-alarm reviews and lessons learned.
9. **Improve:** adjust technology, processes, service provider requirements or site protection.

## Decisions

- Which areas need monitoring and which explicitly do not?
- Which events are security-relevant enough for alerting or escalation?
- Who may view recordings and under which conditions?
- How long are event and recording data retained?
- When does a physical event become a security incident or BCM topic?
- Which conflicts of objectives exist between protection needs, data protection, costs and work culture?

## Evidence

### Strong evidence

- Current monitoring scope with purpose and owner,
- event and escalation matrix,
- alarm, test or patrol logs with documented response,
- evidence of corrected faults or false alarms,
- access and role review for monitoring systems,
- data protection/legal review note,
- management decision for expansion, restriction or residual risk.

### Weak evidence

- Cameras or alarm system without defined response routine,
- service provider contract without event reports,
- screenshots of a system without test or alarm case,
- logs without assessment or follow-up,
- general statement “is monitored” without purpose and responsible persons.

### Evidence gaps

- No clarification of personal monitoring data,
- alarms run to unstaffed mailboxes or unclear phone numbers,
- recordings without access restriction,
- false alarms are ignored,
- technical faults without measures log,
- service provider notifications without internal assessment.

## Effectiveness review

Review questions:

- Are relevant physical events actually detected and reported to the right place?
- Are response paths clear outside normal working hours as well?
- Are purpose, access, retention and evaluation of monitoring data clarified?
- Do false alarms and faults lead to improvements?
- Is service provider performance measurable and reviewed?
- Are physical security events connected with incident response and BCM?

Possible metrics:

- Successfully tested alarm chains,
- average response time to critical alarms,
- false alarm rate,
- open faults in monitoring systems,
- overdue access reviews,
- unresolved events by site or area.

## BSIG/NIS2 connection point

Physical security monitoring is a connection point for NIS2-oriented risk management measures, protection of critical operating environments, incident handling, business continuity and governance of security measures. The concrete connection should be assessed in the requirements register, in risk analysis and, for personal data, with human review.

This artefact does not replace legal, data protection or co-determination review.

## Boundaries

- This artefact is not camera or alarm-system planning.
- It does not replace a data protection impact assessment, legal review or co-determination clarification.
- It does not guarantee gap-free detection of physical attacks.
- It contains no certification promise and no ISO 27002 text.
- Public examples contain no real site or security details.

## Handoffs

- **Data protection / Legal handoff:** video, access logs, employee data, retention, information requests, co-determination.
- **Facility / Security service handoff:** alarm technology, patrols, control centre, reception, maintenance.
- **IT handoff:** system access, log protection, network connection, resilience of monitoring technology.
- **Incident handoff:** break-in, sabotage, tampering, unauthorised access, connection with cyber event.
- **BCM handoff:** outage of site, control centre, alerting or critical access monitoring.
- **Management handoff:** expansion of monitoring, costs, residual risks, acceptance or objective conflicts.
- **Audit / Evidence handoff:** missing test evidence, unclear retention or non-traceable response.

## Typical mistakes

- Technology is procured before purpose, response and data protection are clarified.
- Alarms are generated, but no one is responsible for assessment and follow-up.
- Recordings are available, but access to them is not controlled.
- False alarms lead to alarm fatigue and are not analysed.
- Service provider reports are filed but not used in risk reviews.
- Monitoring is expanded without management decision and human gate.

## Fictional mini example

A fictional operator of a small data room finds that door alarms at night are sent to a general mailbox. Facility and the ISMS Owner define an escalation matrix: outside business hours, a critical alarm goes to the control centre and to the IT on-call contact. Data Protection reviews the processing of access logs. A test shows that the reporting chain works; two false alarms lead to a maintenance measure on the door contact.

Evidence:

- Event and escalation matrix,
- test log of the alarm chain,
- data protection review note on access logs,
- maintenance ticket for door contact,
- review note in the site security review.
