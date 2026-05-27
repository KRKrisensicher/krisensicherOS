# A.5.26 — Response to security incidents

## Purpose

Response to security incidents ensures that a confirmed or plausible security incident is handled in a coordinated way: contain, investigate, decide, communicate, recover, and learn. The goal is not heroics in an exceptional situation, but a resilient routine that maintains responsibility, evidence, and human gates under pressure.

## Control objective in repository language

The organization operates an incident response routine through which security incidents are prioritized, coordinated, treated technically and organizationally, documented, escalated, and reviewed afterward. Decisions on containment, restart, communication, residual risk, and external parties remain traceable and under human responsibility.

## Typical risks

- If technical teams respond without shared leadership, contradictory actions arise and evidence is lost.
- If containment happens too late, an attack may spread or data may be further endangered.
- If systems are shut down too quickly, critical services may fail without a management decision.
- If communication is not controlled, incorrect, premature, or legally risky statements may arise.
- If lessons learned are missing, causes and response gaps repeat.

## Triggers

- A security event has been classified as an incident or must be treated precautionarily as an incident.
- confirmed or suspected compromise of an account, system, data, application, or service provider.
- malware, ransomware, suspected data leakage, cloud misconfiguration, active exploitation, or significant policy violation.
- supplier incident affecting own services or data.
- incident exercise, tabletop, or lessons-learned review.
- management, legal, data protection, customer, or authority question about an incident.

## Roles and responsibilities

- **Incident Lead:** coordinates incident response, situation picture, tasks, decisions, and escalations.
- **Technical response roles:** analyze, isolate, preserve logs, and implement containment and recovery.
- **Service Owner / Business function:** assesses business impact, priorities, and restart needs.
- **ISMS owner / Security role:** ensures process, evidence, risk, and lessons-learned connection.
- **Legal / Data protection:** reviews legal, data protection, contractual, and reporting obligation questions.
- **Communication / Management:** decides and controls approved internal or external communication.
- **BCM/crisis role:** takes over or supports when the incident affects critical services, the crisis team, or emergency operations.
- **Supplier management:** coordinates external providers, managed services, forensics, or SaaS dependencies.

## Implementation

### Minimum start

Goal: an incident is led, documented, and escalated in a controlled way.

1. An Incident Lead is named for every incident.
2. An incident ticket or situation log records timeline, facts, decisions, actions, owners, and status.
3. Immediate actions are decided according to risk and operational impact: isolate, block, preserve, observe, restore.
4. Legal, data protection, management, and communication are involved according to defined criteria.
5. After closure, there is a short lessons-learned note with actions.
6. Open points are transferred to the action, risk, or improvement log.

Minimum evidence:

- incident ticket or situation log,
- named Incident Lead,
- timeline and decision log,
- actions with owner and status,
- handoff evidence,
- closure and lessons-learned note.

### Solid practice

Goal: incident response is role-based, scenario-related, and decision-capable.

1. Incident categories and severity levels steer escalation, communication needs, and management involvement.
2. Response playbooks describe typical actions for account compromise, malware, suspected data leakage, cloud incident, supplier incident, and outage of critical services.
3. Evidence preservation, log exports, and technical changes are documented in a controlled way.
4. Communication takes place only through approved roles and with human review.
5. Recovery is aligned with service owners, change, BCM, and risk decision.
6. Lessons learned lead to concrete improvements in detection, access, vulnerability handling, training, supplier control, or BCM.

Strong evidence:

- incident classification and severity level,
- situation and decision log,
- technical analysis and action references,
- approvals for communication or critical actions,
- recovery and validation evidence,
- lessons-learned actions with owner and deadline,
- management decision for high residual risk.

### Advanced practice

Goal: incident response is integrated into security operations, crisis management, and management reporting.

1. Incident ticketing, monitoring, asset data, communication channels, and action management are connected.
2. Situation picture, technical facts, business impact, and decision needs are synchronized regularly.
3. Forensics, legal, communication, and service provider support are prepared and contractually or organizationally available.
4. After closure, incidents are tracked with cause analysis, control improvement, and effectiveness review.
5. Metrics show response capability: time to containment, time to recovery, open lessons learned, recurring causes, escalation quality.

## Routine flow

1. **Take over incident:** triage hands over to the Incident Lead with facts, severity level, and open questions.
2. **Build situation picture:** record affected assets, data, users, business processes, suppliers, and initial impact.
3. **Decide immediate actions:** block accounts, isolate systems, preserve logs, limit access, increase monitoring, or stabilize operations.
4. **Trigger handoffs:** involve Legal, data protection, management, communication, BCM, suppliers, or forensics.
5. **Investigate and contain:** clarify cause, scope, spread, and active threat; implement actions in a controlled way.
6. **Recover:** return services in an orderly way, perform validation, decide residual risks.
7. **Communicate:** pass on only approved, aligned information internally or externally.
8. **Close:** document status, decisions, evidence, remaining points, and lessons learned.
9. **Improve:** track actions in ISMS, technology, training, supplier control, or BCM.

## Decisions

- Which immediate actions are proportionate and who may approve them?
- When is something isolated, shut down, kept running, or restored?
- Which information is robust enough for management or external communication?
- When is external forensics, provider escalation, or the crisis team needed?
- Which residual risks remain after containment or restart?
- When is an incident closed and who confirms this?

## Evidence

### Strong evidence

- incident ticket with timeline, roles, and status,
- documented severity and escalation decision,
- decision log for containment, recovery, and communication,
- technical evidence for blocking, isolation, analysis, patch, restore, or validation,
- Legal/data protection/management handoff evidence,
- closure report or lessons-learned note,
- action tracking after the incident.

### Weak evidence

- chat log without consolidated decisions,
- technical screenshots without timeline or owner,
- closure message without relation to cause or actions,
- communication draft without approval evidence,
- lessons learned without responsible persons or deadlines.

### Evidence gaps

- no Incident Lead,
- no timeline,
- no documented immediate decisions,
- technical changes without traceability,
- Legal/data protection handoff missing despite data relevance,
- recovery without validation,
- no follow-up review or action tracking.

## Effectiveness review

Review questions:

- Was the incident clearly led and were roles reachable?
- Are timeline, facts, decisions, and actions traceable?
- Were containment and recovery decided based on risk?
- Were Legal, data protection, management, communication, and BCM involved in time?
- Were technical actions validated?
- Did lessons learned lead to concrete improvements?
- Were open residual risks transferred to the risk register or management review?

Possible metrics:

- time until Incident Lead is named,
- time until containment decision,
- time until recovery of critical services,
- number of open lessons-learned actions,
- recurring incident causes,
- incidents with complete decision log,
- overdue follow-up actions.

## BSIG/NIS2 connection point

Response to security incidents is compatible with NIS2-oriented topics such as incident handling, reporting and escalation capability, business continuity, risk management, supplier control, and management responsibility. Whether a concrete incident is reportable or which external steps are required must be assessed organization-specifically and legally.

This artifact does not replace legal advice, data protection advice, or a binding assessment of reporting obligations.

## Boundaries

- No substitute for professional forensics, legal advice, data protection assessment, or crisis communication.
- No guarantee that containment or recovery will be successful.
- No statement on the legal classification of concrete incidents.
- No ISO 27002 texts or certification promise.
- No real incident data, log data, personal data, or confidential customer data in public examples.

## Handoffs

- **Triage handoff:** security event is taken over as an incident or precautionarily as an incident.
- **Legal/data protection handoff:** suspected data leakage, personal data reference, reporting-obligation proximity, evidence preservation, external communication.
- **Communication handoff:** internal situation updates, customer/partner communication, public relations only with approval.
- **BCM/crisis handoff:** critical service interruption, emergency operations, crisis team, restart prioritization.
- **Change/operations handoff:** isolation, patch, restore, configuration change, rollback, validation.
- **Supplier handoff:** provider incident, external forensics, managed service, cloud or SaaS dependency.
- **Management handoff:** significant impact, residual risk, shutdown, restart, resources, or external communication.
- **Audit/evidence handoff:** missing timeline, unclear decisions, incomplete follow-up review.

## Typical mistakes

- Technical actions start without shared situation leadership.
- Communication happens before facts and approvals are clarified.
- Logs or traces of evidence are overwritten by hectic changes.
- Business functions are involved too late and restart priorities are missing.
- Incidents are closed although residual risks or causes remain open.
- Lessons learned remain as a report and are not implemented.
- Management receives technical details, but no decision templates.

## Fictional mini example

A fictional service provider reports suspicious activity in a connected support system. The organization takes over the case as a security incident. The Incident Lead creates a situation log, the IT owner blocks affected integration accounts, the Service Owner assesses business impact, and Legal and data protection review possible data impact. After technical validation, the service is released again with restrictions. In the lessons-learned meeting, it is decided to review integration accounts monthly in the future.

Evidence:

- supplier notification,
- incident situation log,
- blocking and validation evidence,
- Legal/data protection handoff,
- restart decision,
- lessons-learned action with owner and deadline.
