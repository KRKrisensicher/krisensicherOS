# A.5.28 — Preservation of evidence traces

## Purpose

Preservation of evidence traces ensures that relevant information after a security event is retained in a traceable, protected, and usable way. This does not only mean “copy logs”, but clear decisions: Which traces are relevant, who may preserve them, how are integrity and confidentiality maintained, and when must Legal, data protection, or external specialists take over?

## Control objective in repository language

The organization operates a routine through which digital and organizational traces in security events are identified, preserved, documented, protected, and passed on in a controlled way. The routine supports internal clarification, risk assessment, lessons learned, and — if required — human-reviewed legal or contractual steps.

## Typical risks

- If logs, systems, or devices are cleaned up too quickly, important traces are lost.
- If evidence is collected unsystematically, origin, time, completeness, or freedom from alteration are not traceable.
- If too much data is copied, unnecessary data protection, confidentiality, or access risks arise.
- If access to evidence traces is not limited, sensitive content can spread uncontrolled.
- If service providers or cloud providers are not involved, available logs or export deadlines expire.
- If legal assessment is asserted instead of obtained, false certainty and wrong decisions arise.

## Triggers

- Security incident or well-founded suspicion of compromise, data leakage, manipulation, or misuse.
- Incident Owner requests preservation of traces for analysis, recovery, or decision-making.
- Indication of possible legal, contractual, insurance-related, or reporting-related relevance.
- Before an affected system is reinstalled, cleaned, shut down, or overwritten.
- Request by Legal, data protection, management, forensic service provider, or internal audit.
- Exercise or review shows gaps in log retention, access, or evidence preservation.

## Roles and responsibilities

- **Incident Owner:** decides in the incident process which preservation of traces is needed and coordinates priorities.
- **Forensics/security role:** defines preservation method, documents chain of handovers, and protects integrity.
- **IT operations / platform team:** provides systems, logs, snapshots, backups, or devices in a controlled way.
- **Asset Owner / Service Owner:** assesses business criticality and operational consequences of preservation.
- **Data protection / Legal:** reviews personal data, legal questions, external transfer, retention, and communication.
- **Supplier management:** coordinates cloud, SaaS, managed-service, or service provider traces.
- **Management:** decides on resources, external engagement, conflicting objectives, or risky disclosure.

## Implementation

### Minimum start

Goal: do not lose relevant traces in critical events and treat them traceably.

1. Define who may order preservation of traces in an incident.
2. Create a short checklist: affected systems, logs, time window, devices, accounts, communication data, service providers.
3. Before cleanup or recovery, check whether a snapshot, log export, or device preservation is needed.
4. Before mass data exports, make a data minimization decision: Which data is required for the purpose, which can be excluded or added later?
5. Document every preservation: what, when, by whom, from which system, with which method, where stored, who has access.
6. Store evidence traces in a protected storage area with limited access.
7. Trigger Legal/data protection handoff if personal-data-related, contractual, or external-use questions are touched.
8. Name an owner for retained traces for retention, access review, and deletion decisions.

Minimum evidence:

- trace preservation checklist,
- preservation protocol,
- protected storage or ticket evidence,
- access list,
- handoff or approval note.

### Solid practice

Goal: preservation of traces is integrated into incident response, logging, and supplier control.

1. Relevant evidence sources are inventoried in advance: central logs, endpoints, cloud services, IAM, mail, network, backups, tickets.
2. Retention periods and export options for critical logs are known.
3. Preservations are documented with hash value, time reference, processing steps, and handovers.
4. Every copy, analysis transfer, external transfer, or return is logged as a chain-of-custody event with purpose, approval, recipient, time, and storage reference.
5. Access to preserved traces follows need-to-know and is regularly reviewed.
6. Retention, deletion, and follow-up are documented with owner, deadline, and decision rationale.
7. Supplier contracts and contact paths contain practical support for log exports and incident cases.
8. After every relevant use, it is reviewed whether traces were missing or preserved too late.

### Advanced practice

Goal: evidence traces are technically available, usable in a controlled way, and manageable in crises.

1. Critical systems provide central logs with a coordinated time base and resistance to manipulation.
2. Incident playbooks contain case-specific preservation paths for endpoints, cloud, SaaS, identities, and network.
3. Automated workflows freeze relevant data in a controlled way without producing unnecessarily large data volumes.
4. External forensics, Legal, data protection, and communication are prepared in escalation paths.
5. Access, transfer, deletion, and retention of evidence traces are checked in reviews.
6. Exercises test whether traces can be preserved and handed over traceably under time pressure.

## Routine flow

1. **Suspicion arises:** incident triage recognizes possible relevance of traces.
2. **Define scope:** determine affected systems, accounts, time windows, data types, and service providers.
3. **Decide preservation need:** internal analysis, recovery, legal review, insurance, or external forensics.
4. **Perform preservation:** preserve log export, snapshot, image, backup copy, mail/IAM extract, or configuration state.
5. **Document integrity and origin:** time, source, method, responsible person, storage location, hash, or comparable control information.
6. **Maintain chain of custody:** log copies, analyses, handovers, external transfers, returns, and deletion decisions in a traceable way.
7. **Limit access:** protect storage, log accesses, have transfer approved, and review access regularly.
8. **Check handoff:** involve Legal, data protection, service provider, management, or forensics.
9. **Separate evaluation:** document analysis results, keep original traces as unchanged as possible.
10. **Follow up:** record missing logs, too-short retention, or unclear responsibilities as actions.

## Decisions

- Which events require formal preservation of traces?
- Which systems and logs are critical for typical scenarios?
- How is recovery prevented from overwriting important traces?
- Who may view, copy, or externally transfer evidence traces?
- How long are preserved traces retained, who is the owner, and who decides deletion?
- Which copies, handovers, or external transfers are permitted and how are they approved?
- When is external forensics or legal assessment required?
- How is priority set between fast operational recovery, data minimization, and preservation of evidence?

## Evidence

### Strong evidence

- incident ticket with preservation decision,
- preservation protocol with source, time, method, and responsible persons,
- integrity evidence or hash value, where appropriate,
- protected storage with access restriction,
- chain-of-custody log for copies, analyses, handovers, accesses, and transfers,
- handover protocol to Legal, data protection, forensics, or service provider,
- retention, deletion, and access review decision,
- review note on missing traces and improvement actions.

### Weak evidence

- screenshots without time and source reference,
- copied log files without origin documentation,
- chat message “logs preserved” without storage or access evidence,
- unprotected storage in general team folders,
- blanket statement that the service provider has stored everything.

### Evidence gaps

- no criteria for preserving traces,
- logs are overwritten before they are exported,
- no evidence of who saw or passed on evidence traces,
- no clarification of personal-data-related content,
- no contractually usable log exports for cloud/SaaS services,
- original data is changed during analysis.

## Effectiveness review

Review questions:

- For a relevant incident, can it be traced which traces were preserved and why?
- Are critical log sources known and available in time?
- Do origin, integrity, access, copies, analyses, and transfer remain traceable?
- Is the time base of critical log sources synchronized or at least documented in a traceable way as a time reference?
- Are personal-data-related, confidential, or contractual questions reviewed before mass data export, analysis, or transfer?
- Are retention, deletion, and access review of preserved traces tracked?
- Are missing traces after incidents transferred into actions?
- Is the flow realistically usable under crisis and recovery pressure?

Possible metrics:

- share of relevant incidents with preservation protocol,
- log sources with known retention period,
- time until preservation of critical traces,
- number of missing or incomplete log sources,
- open actions from trace preservation reviews,
- unauthorized access to evidence traces,
- overdue retention/deletion reviews for preserved traces.

## BSIG/NIS2 connection point

Preservation of traces is a connection point for NIS2-oriented topics such as incident handling, traceability, crisis response, risk management, and governance of security events. Depending on the organization, it can also support evidence, contractual, insurance, or reporting processes.

This artifact makes no legal statement on the usability of evidence, reporting obligations, or retention obligations. These points need human review by qualified roles.

## Boundaries

- This artifact is not a forensic specialist manual and not legal guidance for evidence assessment.
- It does not replace data protection, legal, employment-law, or criminal-procedure assessment.
- It does not guarantee admissibility in court.
- It must not lead to excessive collection of personal or confidential data.
- Public examples contain no real incident data, customer data, or secret technical details.

## Handoffs

- **Incident handoff:** preservation of traces as part of triage, containment, and recovery.
- **Legal handoff:** external use, criminal complaint, contractual dispute, insurance, authority communication, or suspected reporting obligation.
- **Data protection handoff:** personal-data-related logs, employee data, communication content, or possible data protection breach.
- **Forensics handoff:** complex compromise, high damage impact, suspected manipulation, or missing internal capability.
- **Supplier handoff:** cloud/SaaS logs, managed services, device manufacturers, or external operational services.
- **Management handoff:** conflicting objective between preservation of evidence, recovery, cost, reputation, or operational pressure.
- **Evidence handoff:** storage, access, retention, and review of evidence.

## Typical mistakes

- Systems are reinstalled before logs or snapshots have been preserved.
- Evidence traces end up in unprotected project folders.
- Only technical teams decide on transfer, without Legal/data protection review.
- Screenshots replace structured preservation and documentation.
- Service provider logs are requested only when they have already expired.
- Original data is changed during analysis.
- Copies and handovers are not documented as chain-of-custody events.
- Retention and deletion remain open because no owner is named.
- The organization collects too much and thereby creates new data protection and confidentiality risks.

## Fictional mini example

A fictional retail company discovers unusual logins in the admin portal. Before resetting the server, the Platform Owner exports authentication logs, creates a snapshot, and documents source, period, hash value, and storage location. Access is limited to the Incident Owner, security role, and Legal. A SaaS service provider is asked for supplementary login data within the log retention period. The review shows that another cloud service retains logs for only seven days; this is recorded as an action in the supplier review.

Evidence:

- preservation decision in the incident ticket,
- log export and snapshot protocol,
- hash/storage evidence,
- access list,
- service provider request,
- action on log retention in the supplier review.
