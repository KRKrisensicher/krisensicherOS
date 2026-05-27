# A.6.8 — Reporting security events by employees

## Purpose

Reporting security events by employees ensures that suspicions, mistakes, losses, unusual observations and possible incidents become visible early. The aim is a low-threshold, known and practised reporting routine — not blame, but rapid classification, containment, learning and decision.

## Control objective in repository language

The organisation operates a clear reporting path through which employees and relevant external staff can recognise and report security events and hand them over into incident triage. The routine connects awareness, leadership, helpdesk/security, data protection/Legal handoffs, escalation and lessons learned.

## Typical risks

- If employees do not know reporting paths, phishing, device loss, misdirected sending or suspicious access are handled too late.
- If reporting feels punitive, people do not report mistakes or uncertainties at all or only informally.
- If helpdesk, manager and security use different paths, reports are lost or prioritised incorrectly.
- If events are not triaged cleanly, possible incidents, data protection questions or external reporting decisions remain unclear.
- If the organisation does not learn from reports, mistakes repeat in processes, tools or training.

## Triggers

- Suspected phishing, suspicious message, unusual login or malware indication.
- Loss or theft of device, ID card, token, documents or data carrier.
- Misdirected sending, wrong sharing, accidental publication or unauthorised viewing.
- Unusual system behaviour, unknown person in a protected area or suspicious request.
- Security question in everyday work where employees are unsure.
- Onboarding, awareness campaign, reporting-path test or role change.
- Incident, near miss, audit finding or review of the reporting process.

## Roles and responsibilities

- **Employees and external staff in scope:** report suspicions, mistakes and events quickly through defined paths.
- **Managers:** promote a reporting-friendly culture, do not block reports and escalate conflicts of objectives.
- **Helpdesk / service desk:** receives reports, records minimum information and forwards them to triage roles.
- **Security/incident role:** assesses events, prioritises, coordinates containment and decides on incident escalation.
- **ISMS owner:** defines reporting process, evidence logic, training reference and review.
- **Data protection / Legal:** reviews personal-data-related, data protection, legal or communication questions.
- **Management:** decides on critical incidents, resource needs, cultural problems or external communication questions.

## Implementation

### Minimum start

Goal: every person in scope knows what they should report and through which path.

1. A central reporting path is defined: email, phone, ticket, chat channel or hotline with clear responsibility.
2. Short examples explain what is reportable: phishing, loss, misdirected sending, suspicious access, unknown person, wrong sharing.
3. Onboarding and awareness explicitly name the reporting path.
4. The helpdesk or security role uses a simple triage checklist.
5. Reports are recorded traceably: time, reporter role, event type, initial assessment, next step.
6. Critical reports are escalated to Incident Response, data protection, Legal or management.

Minimum evidence:

- published reporting path,
- onboarding or awareness evidence,
- report or triage tickets,
- escalation evidence,
- review note on reports and improvements.

### Solid practice

Goal: reports are triaged uniformly, escalated promptly and used for learning.

1. Event categories and priorities are defined without overwhelming employees with technical jargon.
2. Reporting paths are tested regularly, for example with a phishing exercise or reporting-path drill.
3. Managers receive guidance to take reports seriously and not resolve them informally.
4. Data protection, Legal, BCM and communication handoffs are described for certain event types.
5. Lessons learned from reports flow into awareness, technical measures, process changes or management review.
6. Repeated reporting barriers, long response times or unclear responsibilities are tracked as measures.

### Advanced practice

Goal: the reporting routine becomes part of a robust security situation picture and a trust-based security culture.

1. Reporting channels, ticketing, incident triage and security monitoring are connected.
2. Metrics consider not only the number of reports, but quality, response time, escalation accuracy and learning effect.
3. High-risk areas receive scenario exercises: misdirected sending, suspected ransomware, social engineering, physical observation.
4. Anonymous or confidential reporting paths are assessed where culture, hierarchy or external roles would otherwise inhibit reports.
5. Management receives decision-ready information on reporting culture, resources, critical patterns and process gaps.

## Routine flow

1. **Notice event:** person sees, loses, receives, sends or experiences something security-relevant.
2. **Report immediately:** defined channel is used; where uncertain, “better report than wait” applies.
3. **Record minimum information:** what, when, where, affected system or information, steps already taken.
4. **Perform triage:** helpdesk or security assesses urgency, possible impact and handoffs.
5. **Escalate:** Incident Response, data protection, Legal, facility, HR, BCM or management are involved when triggers apply.
6. **Track measures:** containment, follow-up question, correction, communication or technical check are documented.
7. **Give feedback:** reporter or manager receives suitable information so trust develops.
8. **Learn:** patterns are translated into awareness, process improvement, technical controls or management decisions.

## Decisions

- Which events must employees always report?
- Which channels are suitable for urgent, confidential or out-of-hours events?
- Which information may be requested from the reporter without making reporting harder?
- When does a report become an incident, data protection, Legal or management topic?
- How is a reporting-friendly, non-punitive culture implemented concretely?
- Which metrics help without creating personal performance or behaviour monitoring?

## Evidence

### Strong evidence

- published reporting path with responsibility and availability,
- awareness or onboarding evidence for the reporting process,
- triage tickets with event type, time, assessment, decision and status,
- escalation evidence to Incident Response, data protection, Legal or management,
- results of reporting-path tests or exercises,
- lessons-learned measures with owner and deadline,
- management decision for resource, culture or escalation problems.

### Weak evidence

- policy sentence “incidents must be reported” without channel or examples,
- generic awareness slide without evidence of the reporting path,
- email inbox without triage or responsibility logic,
- reporting statistics without assessment, response time or measures,
- informal Teams or chat reports without follow-up.

### Evidence gaps

- external staff do not know the reporting path,
- no availability for urgent events,
- no documented triage or escalation,
- data protection/Legal handoffs are not recognised,
- no feedback and no learning from reports,
- reporting barriers or fear culture are not addressed.

## Effectiveness review

Review questions:

- Can employees name typical reportable events?
- Is the reporting path visible in onboarding and everyday work?
- Are reports recorded, triaged and escalated promptly?
- Are there examples where reports led to measures or lessons learned?
- Are misdirected sending, device loss and phishing reliably recognised and handed over?
- Are data protection, Legal and management decisions cleanly separated from the operational triage process?
- Is reporting culture considered instead of evaluating only low or high report numbers?

Possible metrics:

- time from event to report,
- time from report to triage,
- share of reports with complete triage,
- reporting-path test rate,
- recurring event types,
- open lessons-learned measures,
- share of external staff with reporting-path onboarding.

## BSIG/NIS2 connection point

The reporting routine is compatible with NIS2-oriented topics such as incident handling, cyber hygiene, training, governance, reporting and escalation capability, and management responsibility. The concrete connection, especially to possible external reporting obligations, must be assessed organisation-specifically and by humans.

This artefact does not make a legal assessment of whether an event is reportable and does not replace data protection or legal review.

## Boundaries

- This artefact is not a complete incident response policy.
- It does not replace legal or data protection assessment of reporting obligations.
- It must not be used as a basis for personal performance or behaviour monitoring without suitable clarification.
- Low report numbers do not automatically prove security; high report numbers do not automatically prove insecurity.
- It contains no ISO 27002 texts and no real incident data.

## Handoffs

- **Incident handoff:** suspected compromise, malware, unauthorised access, data outflow or active exploitation.
- **Data protection handoff:** possible personal data breach, misdirected sending of personal information or unauthorised viewing.
- **Legal/communication handoff:** external communication, authority/customer contact, employment-law questions or disputed facts.
- **HR handoff:** reporting culture, training, role duties, repeated non-reporting or team conflicts.
- **Facility handoff:** physical observations, lost ID cards, unknown persons or access events.
- **BCM/crisis handoff:** events with possible impact on critical services or crisis organisation.
- **Management handoff:** critical incidents, resource conflicts, cultural problems or accepted residual risks.
- **Audit/evidence handoff:** missing triage, unclear escalation or lessons learned that cannot be traced.

## Typical mistakes

- The reporting path exists only in a policy and is not present in everyday work.
- Employees are shamed for mistakes and therefore report later or not at all.
- Managers resolve security reports informally instead of sending them into triage.
- Phishing buttons exist, but misdirected sending, device loss or physical observations are not covered.
- Reports are counted but not evaluated or improved.
- Data protection and Legal questions are involved too late.
- External staff and service providers do not know the reporting path.

## Fictional mini example

A fictional employee receives a suspicious email with a link to an alleged document. During onboarding she learned to use the security reporting channel. The helpdesk records the report, Security checks the message and identifies an ongoing phishing wave. The mail is removed from mailboxes, a short warning is published and the example is added as a scenario in the next awareness review.

Evidence:

- awareness evidence for the reporting path,
- triage ticket for the report,
- security analysis and measure,
- communication evidence for the warning,
- lessons-learned entry for awareness update.
