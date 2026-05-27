# A.8.12 — Preventing unintended data leakage

## Purpose

Preventing unintended data leakage ensures that sensitive information does not leave controlled environments unintentionally or without authorization. The core is not a single DLP tool, but a routine that brings together data flows, roles, technical channels, user error, service providers, and incident response.

## Control objective in repository language

The organization operates a traceable routine to identify, limit, monitor, and respond to critical data leakage paths. It connects data classification, access, secure configuration, endpoint/mail/cloud controls, development, supplier control, training, and human gates for Data Protection, Legal, and Management.

## Typical risks

- If sensitive data is shared in an uncontrolled way via email, cloud shares, private devices, chat, tickets, or exports, it can end up outside the intended protection space.
- If applications allow bulk downloads or open interfaces, authorized accounts can extract large volumes of data unnoticed.
- If misconfigurations exist in cloud storage, repositories, or SaaS services, information becomes public or externally accessible.
- If DLP alerts are not triaged, many alarms arise but no risk treatment follows.
- If suppliers and external roles are not included, data leakage outside the organization’s own IT remains invisible.

## Triggers

- New data class, new data repository, new export, new interface, or new analytics function.
- Introduction or change of email, cloud, collaboration, endpoint, MDM, or DLP controls.
- New service provider, external access, outsourcing, support access, or data transfer.
- Security event, DLP alert, suspicious download, misdirected sending, or repository made public.
- Change to roles, permissions, sharing settings, API keys, or mobile work methods.
- Audit finding, customer requirement, data protection/legal review, or management question.
- Regular review of critical data flows and permitted exceptions.

## Roles and responsibilities

- **Information Owner / Business Unit:** determines protection need, legitimate recipients, permitted use, and necessary exports.
- **IT / Platform Owner:** implements technical controls for endpoints, mail, cloud, network, SaaS, APIs, and devices.
- **Security Operations / ISMS Owner:** defines DLP logic, triage, escalation, reporting, and improvement measures.
- **Data Protection / Legal:** reviews personal data, external disclosure, employment-law questions, monitoring, and breach notification assessment.
- **HR / Managers:** support role clarification, training, and work-related measures after human review.
- **Supplier Management:** governs external data flows, evidence, and incidents at service providers.
- **Management:** decides on residual risks, blocking controls, resources, exceptions, and target conflicts.

## Implementation

### Minimum start

Goal: make the most important data leakage paths visible and enable clear responses.

1. Critical data types and core systems in the ISMS scope are identified.
2. The most common leakage paths are recorded: email, cloud share, download, USB, print, API, support ticket, chat, external service provider.
3. Rules, owner, and triage are defined for at least one critical path.
4. Open approvals, external shares, and bulk download rights are checked by sample.
5. Misdirected sending or DLP hits are recorded in an incident or action log.
6. Exceptions are time-limited and documented with business need.

Minimum evidence:

- data flow/leakage path list for critical data,
- sharing or export review,
- DLP/alert or incident triage evidence,
- action ticket for correction,
- exception decision with follow-up date.

### Solid practice

Goal: data leakage prevention is risk-based, repeatable, and connected with incident response.

1. Data classes are connected with permitted transfer channels, recipients, and protection measures.
2. Technical controls are coordinated: email warning, external sharing restriction, endpoint control, CASB/SaaS rules, API limitation, logging, encryption.
3. DLP rules are tested and improved iteratively so false positives are reduced and relevant hits are escalated.
4. Critical functions such as bulk download, export, admin access, and external approval receive reviews.
5. Incident response describes how misdirected sending, external share, suspicious export, or compromised account is handled.
6. Trainings explain secure sharing, reporting paths, and stop points for sensitive data.
7. Supplier and SaaS data flows are controlled through contracts, configuration, and evidence.

Strong evidence:

- data flow and channel overview,
- defined DLP/sharing/export rules,
- tested alert and triage processes,
- review of critical approvals and bulk download rights,
- incident or near-miss evidence with measures,
- training/communication evidence,
- management decision on blocking controls or accepted exceptions.

### Advanced practice

Goal: data leakage protection is integrated into architecture, operations, and situational awareness.

1. Classification, IAM, endpoint, email, cloud, SaaS, SIEM, and ticketing provide a coherent view of critical data movements.
2. Risk indicators connect data class, user role, target channel, volume, recipient, location, and behavior.
3. Exports and APIs receive technical limits, approvals, rate limits, purpose limitation, or additional logging.
4. Critical alerts are linked with incident triage, forensics, data protection/legal handoff, and management decision.
5. Architecture and procurement decisions consider data leakage risks at an early stage.
6. Metrics show external shares, DLP hits, confirmed incidents, overdue exceptions, bulk downloads, and repeated error patterns.

## Routine flow

1. **Data flow arises or becomes conspicuous:** new process, export, external share, DLP hit, incident, or review finding.
2. **Classify:** determine data class, source, target, recipient, volume, purpose, and role.
3. **Check permissibility:** clarify business need, approval, contractual/data protection/legal aspects, and protection measures.
4. **Choose technical measure:** block, warn, encrypt, approve, log, restrict, or create exception.
5. **Perform triage:** assess alerts, clean up false positives, escalate real incidents.
6. **File evidence:** document decision, event, measure, approval, and remaining problem.
7. **Review:** regularly check external shares, export rights, DLP rules, and exceptions.
8. **Learn:** feed error patterns back into training, process, configuration, architecture, or supplier control.

## Decisions

- Which data classes and leakage paths should be controlled first?
- Which channels are permitted, restricted, approval-required, or prohibited?
- When is warning used, when is blocking used, and when is only logging used?
- Which DLP hits are an incident, a data protection/legal topic, or normal user error?
- Who may approve external shares, bulk downloads, or exceptions?
- Which target conflicts between workability, data protection, monitoring, and security must go to management?

## Evidence

### Strong evidence

- overview of critical data flows and channels,
- configured and tested DLP/sharing/export rules,
- triage logs for alerts and misdirected sending,
- evidence of corrected approvals or blocked exports,
- review of critical SaaS, cloud, and endpoint settings,
- documented exceptions with expiry date,
- management decision on residual risk or resource need.

### Weak evidence

- enabled DLP tool without triage process,
- policy “do not share data externally” without technical or organizational routine,
- alarm statistics without decision or measures,
- one-time screenshot of cloud settings,
- training slide without reporting path or review.

### Evidence gaps

- unknown external shares,
- no owners for DLP rules or alerts,
- bulk downloads without logging or review,
- supplier transfers outside the data flow view,
- personal data monitoring without data protection/legal handoff,
- permanent exceptions without risk decision.

## Effectiveness review

Review questions:

- Are critical data leakage paths known and prioritized?
- Are DLP or sharing alerts assessed and converted into measures?
- Can external shares, exports, and bulk downloads be traced?
- Are misdirected sending and suspicious data movements connected with incident response?
- Are suppliers, SaaS services, and mobile work included?
- Do repeated error patterns lead to process, training, or architecture changes?

Possible metrics:

- open external shares with sensitive data,
- DLP hits by channel and confirmation,
- confirmed misdirected sending or leakage events,
- overdue exception approvals,
- bulk downloads from critical systems,
- time from alert to triage decision.

## BSIG/NIS2 connection point

Data leakage protection is compatible as a connection point with NIS2-oriented risk management measures, cyber hygiene, access protection, incident handling, secure supply chain, encryption, and protection of critical services. The concrete connection should be assessed in an organization-specific way in the requirements register, in data protection/legal reviews, and in incident response governance.

This artifact does not replace legal assessment of notification obligations, monitoring, data protection questions, or responsibilities.

## Boundaries

- This artifact is not a complete DLP product architecture.
- DLP does not replace data classification, access control, training, or secure development.
- Monitoring of user behavior needs suitable data protection/legal and, where applicable, co-determination review.
- No statutory notification obligations are assessed or confirmed.
- It contains no ISO 27002 text and no certification assurance.

## Handoffs

- **Incident Handoff:** confirmed data leakage, misdirected sending, suspicious export, compromised account.
- **Data Protection / Legal Handoff:** personal data, monitoring, external disclosure, notification assessment, contractual questions.
- **Access / IAM Handoff:** bulk download rights, external shares, privileged roles, role changes.
- **Development / Architecture Handoff:** export functions, APIs, logging, rate limits, secure default configuration.
- **Supplier Handoff:** external processing, SaaS sharing, subprocessors, incidents, and evidence.
- **Management Handoff:** blocking decisions, productivity conflicts, resource need, accepted residual risk.
- **Audit / Evidence Handoff:** incomplete alert triage, unclear approvals, or missing evidence.

## Typical mistakes

- A DLP tool is activated, but no one triages hits.
- Only email is considered while cloud shares and exports remain open.
- Alarms are disabled due to fear of false positives without a risk decision.
- Bulk downloads by authorized users are not monitored.
- Suppliers receive data without clarifying data flow, purpose, and return/deletion.
- Misdirected sending is corrected but not used as a learning signal.
- User monitoring is introduced without data protection/legal handoff.

## Fictional mini example

A fictional software provider allows customer service exports from a ticketing system. During review, it becomes apparent that full ticket attachments can be shared externally through CSV links. The application owner restricts exports to team lead approval, IT activates a warning for external shares, and Security defines triage for hits with sensitive attachments. A test with fictional tickets confirms that external links expire after seven days.

Evidence:

- data flow note for the ticketing system,
- change ticket for export restriction,
- tested sharing rule,
- triage instruction for DLP hits,
- review evidence for external links,
- exception process for justified exports.
