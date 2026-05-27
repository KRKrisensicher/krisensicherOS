# A.5.24 — Preparation for security incidents

## Purpose

Preparation for security incidents creates the ability to act before pressure arises. The organization defines roles, reporting paths, escalations, communication paths, decision rights, technical access, and exercise routines so that a security event does not first have to be organized during the actual situation.

## Control objective in repository language

The organization operates an incident preparedness routine: it knows who acts when there is suspicion, how events are reported and triaged, which roles can be reached, which information is needed, which human gates apply, and how preparation is regularly tested and improved.

## Typical risks

- If reporting paths are unclear, early indications are lost or reach the wrong people.
- If roles are only determined during the incident, containment, decision-making, and communication are delayed.
- If technical access, logs, or contacts are missing, the incident cannot be assessed reliably.
- If external service providers, Legal, data protection, or management are not prepared, gaps arise in assessment and escalation.
- If exercises never happen, playbooks look good in documents but break down in operations.

## Triggers

- setup or review of the incident response process.
- new critical system, new cloud service, new service provider, or new business process.
- security event, near miss, vulnerability finding, audit finding, or lessons learned.
- change to reporting paths, on-call duty, management structure, or external contacts.
- legal, contractual, or customer-related requirement that must be legally reviewed.
- regular exercise, tabletop, crisis team test, or ISMS review.

## Roles and responsibilities

- **Incident Owner / Incident Lead:** coordinates preparation, triage capability, and incident routine.
- **ISMS owner / Security role:** defines minimum process, classification logic, evidence, and review.
- **IT operations / Platform team:** provides technical contact paths, logs, access, and recovery capability.
- **Business function / Service Owner:** assesses business consequences and prioritizes critical services.
- **Communication / Management:** prepares internal and external communication decisions.
- **Legal / Data protection:** assesses legal, data protection, and reporting-duty questions in human review.
- **BCM/crisis role:** connects security incidents with emergency and crisis management.

## Implementation

### Minimum start

Goal: when there is suspicion, everyone knows where to report and who performs the first assessment.

1. A central reporting path for security events is defined and communicated.
2. A small incident core role is named: Incident Lead, IT contact, ISMS/Security, management escalation.
3. A simple triage form records: what happened, when, affected system, first impact, reporting party, immediate actions.
4. A contact and escalation list is maintained.
5. Critical systems and log sources are identified for initial analyses.
6. At least annually, a reporting path or tabletop test is performed.

Minimum evidence:

- published reporting path,
- role and contact list,
- triage template,
- list of critical systems/log sources,
- exercise or test evidence,
- actions from lessons learned.

### Solid practice

Goal: preparation becomes risk-based, exercised, and connected with business processes.

1. Incident categories and severity levels are described in the organization’s own language.
2. Playbooks or checklists cover typical scenarios: phishing, account compromise, malware, suspected data leakage, cloud misconfiguration, supplier incident, outage of critical services.
3. Roles, deputies, and reachability are reviewed regularly.
4. Decision and human-gate points are defined in advance: shutdown, external communication, risk acceptance, data protection/legal review, management escalation.
5. Exercises review not only technology, but decisions, communication, and evidence flow.
6. Insights from exercises and real incidents update playbooks, training, and technical prerequisites.

Strong evidence:

- incident response role model,
- current contact and escalation list,
- scenario-specific checklists,
- exercise minutes with actions,
- evidence of log access and critical information sources,
- management decision on resources or readiness model.

### Advanced practice

Goal: incident preparedness is integrated into the situation picture, BCM, supplier management, and technical detection.

1. Incident response plan, crisis management, business continuity, and communication processes are aligned.
2. Critical logs, alerts, forensic access, and service provider contacts are tested in advance.
3. Scenarios are prioritized by risk and regularly exercised with business functions, management, and external partners.
4. Decision spaces are prepared: shutdown, isolation, recovery, customer communication, authority contact, supplier escalation.
5. Metrics show preparedness status: exercised scenarios, open preparedness actions, reachable roles, log coverage, exercise findings.

## Routine flow

1. **Define preparation scope:** determine critical processes, systems, data, service providers, and scenarios.
2. **Define reporting path and roles:** Incident Lead, technical roles, business function, management, Legal, data protection, communication, BCM.
3. **Establish triage capability:** prepare templates, severity levels, contact lists, log sources, and first actions.
4. **Create playbooks:** short, usable process aids for the most important scenarios.
5. **Communicate and enable:** anchor reporting path and roles in awareness, onboarding, and leadership briefings.
6. **Exercise:** conduct tabletop, reporting path test, technical test, or crisis exercise.
7. **Improve:** feed findings back into action log, playbooks, roles, tooling, and training.
8. **Review:** review at least annually or after significant changes.

## Decisions

- Which scenarios are most important for the organization?
- Who may initiate immediate technical actions during an incident?
- When must management, Legal, data protection, communication, or BCM be involved?
- Which information must be available in the first minutes or hours?
- Which external service providers, forensic specialists, or providers must be prepared?
- Which readiness or resource gaps does the organization not accept?

## Evidence

### Strong evidence

- current incident response plan in the organization’s own language,
- communicated reporting path,
- role, contact, and deputy list,
- triage and playbook templates,
- exercise minutes with decisions and actions,
- evidence of tested log, access, or escalation paths,
- management decisions on readiness, tools, or external support.

### Weak evidence

- general emergency document without roles and contacts,
- playbook without test or update,
- reporting path only on the intranet but not known,
- contact list without owner or review date,
- technical tool list without verified access.

### Evidence gaps

- no central reporting path,
- no first triage responsibility,
- no reachable deputies,
- unclear Legal/data protection escalation,
- missing log sources for critical systems,
- exercises without action tracking.

## Effectiveness review

Review questions:

- Can employees and external staff report security suspicion?
- Is it clear who performs the first assessment and who escalates?
- Are contact lists, deputies, and service provider contacts current?
- Were relevant scenarios exercised and findings tracked?
- Are Legal, data protection, communication, BCM, and management prepared at the right points?
- Are critical logs and technical access available during the actual situation?

Possible metrics:

- reporting path awareness or test result,
- number of exercised scenarios,
- open actions from exercises,
- currency of the contact list,
- critical systems with available log source,
- time until Incident Lead is reachable.

## BSIG/NIS2 connection point

Preparation for security incidents is a connection point for NIS2-oriented topics such as incident handling, reporting and escalation capability, business continuity, risk management, supplier dependencies, and management responsibility. Concrete legal reporting or evidence duties must be assessed organization-specifically and legally.

This artifact does not replace legal advice or a binding assessment of applicability.

## Boundaries

- No replacement for legal assessment of reporting duties or data protection incidents.
- No complete forensic, crisis, or communication handbook.
- No guarantee that an incident is prevented or fully controlled.
- No ISO 27002 texts or certification commitment.
- No real incident data, customer data, or personal data in public examples.

## Handoffs

- **Incident handoff:** from the reporting path into triage, classification, and incident handling.
- **Legal/data protection handoff:** possible personal data reference, data leakage, proximity to reporting duties, external communication.
- **Communication handoff:** internal situation communication, customer, partner, or public communication only with approval.
- **BCM/crisis handoff:** outage of critical services, reputation risk, management situation, or crisis mode.
- **Supplier handoff:** provider incident, SaaS outage, managed service dependency, missing logs.
- **Management handoff:** resources, readiness model, shutdown, residual risk, external support.
- **Audit/evidence handoff:** missing exercise evidence, unclear roles, untracked findings.

## Typical mistakes

- Incident response is only organized during the incident.
- Playbooks are too long and not usable under stress.
- Reporting paths exist, but employees do not know them.
- Exercises test technology, but not decisions and communication.
- Contact lists are outdated or without deputies.
- Data protection, Legal, and communication are involved too late.
- Lessons learned do not lead to actions.

## Fictional mini example

A fictional company conducts a tabletop test on compromised cloud credentials. The exercise shows that the reporting path works, but the deputy cloud admin cannot be reached and it remains unclear who approves external communication. The Incident Lead documents two actions: updated call list and management decision on the communication approval process.

Evidence:

- exercise scenario,
- participant and role list,
- findings,
- action log with owner and deadline,
- updated contact list,
- management decision on approval.
