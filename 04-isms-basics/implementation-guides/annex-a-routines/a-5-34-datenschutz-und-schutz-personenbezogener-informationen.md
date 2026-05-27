# A.5.34 — Privacy and protection of personal information

## Purpose

This routine connects information security with the protection of personal information. It helps organizations treat personal data not only as a legal or data-protection topic, but as an operational protection area with owners, data flows, access, technical measures, evidence, and clear handoffs.

The core is not data-protection advice by the ISMS, but robust collaboration: Security makes risks, systems, access, and safeguards visible; Data Protection and responsible business roles assess legal bases, data subject rights, and obligations.

## Control objective in repository language

The organization operates a routine through which personal information in processes, systems, service providers, and security measures is identified, protected, reviewed, and handed over to Data Protection, Legal, the business function, or Management when changes occur. Protection need, access, logging, sharing, deletion, and incident capability remain traceable.

## Typical risks

- If personal data in systems or shadow processes remains unknown, safeguards, deletion, and incident assessment cannot take effect.
- If access to employee, customer, or usage data is too broad, confidentiality and misuse risks arise.
- If logs, monitoring, or AI tools process personal data without data-protection clarification, governance and trust risks arise.
- If service providers process personal information but technical and organizational protection points are not tracked, supply-chain risks remain open.
- If deletion, blocking, or retention logic is not connected with system operations, data is retained too long, too briefly, or inconsistently.
- If a security event affects personal information but handoffs are unclear, assessment, decision, and communication are delayed.

## Triggers

- new or changed process with employee, customer, user, applicant, or contact data.
- new system, SaaS tool, AI tool, interface, data export, or reporting.
- change in data class, protection need, access, logging, or retention.
- service provider change, new sub-processors, cloud region, or data transfer.
- security event, suspected data leakage, misdirected sending, incorrect authorization, or lost device.
- audit finding, data-protection request, management question, or internal review.
- planned review of processing activities, access, logs, deletion concepts, or safeguards.

## Roles and responsibilities

- **Business Process Owner:** knows purpose, data types, user groups, and business need of the processing.
- **Data Protection role / DPO:** assesses data-protection requirements, legal bases, data subject rights, TOMs, and data protection impact questions.
- **ISMS owner / Security role:** connects personal information with protection need, risks, controls, incident capability, and evidence.
- **IT / Platform Owner:** implements access, encryption, logging, backup, deletion, and technical safeguards.
- **HR / People function:** is responsible for employee data processes and work-related handoffs.
- **Procurement / Vendor Management:** tracks service providers, contract references, and evidence references.
- **Incident Response:** coordinates technical analysis and handoffs during security events.
- **Management:** decides resources, residual risks, prioritization, and external communication after responsible review.

## Implementation

### Minimum start

Goal: personal information in ISMS scope is visible and receives clear handoffs.

1. The most important processes and systems with personal information are listed.
2. For each entry, owner, data categories, affected groups of persons, service providers, and protection need are roughly recorded.
3. Critical access is reviewed: admins, business roles, external roles, and technical accounts.
4. Safeguards are assigned: access protection, MFA, encryption, backup, logging, deletion/blocking path, incident reporting path.
5. Unclear legal, data-protection, or deletion questions are not decided in the ISMS, but handed over to Data Protection/Legal.
6. Security events with possible personal-data relevance receive a fixed Data Protection handoff.

Minimum evidence:

- process/system list with personal information,
- owner and protection need,
- access sample for critical systems,
- handoff evidence to Data Protection for open questions,
- incident checkpoint for personal information.

### Solid practice

Goal: data-protection and security routines work together repeatably.

1. Processing overviews, asset inventory, risk register, and action log are cross-referenced.
2. New systems and process changes pass through a security/data-protection check before productive use.
3. Logging, monitoring, and analyses are reviewed for personal-data relevance and purpose limitation.
4. Service providers with personal information are tracked with security evidence and data-protection handoffs.
5. Deletion, blocking, and retention requirements are translated into operations, backup, archiving, and applications.
6. Access reviews consider particularly sensitive data, employee data, and external access.
7. Incidents, incorrect authorizations, and findings lead to actions in the ISMS and data-protection process.

Strong evidence:

- referenced processing/asset/risk entries,
- security/data-protection checklists for changes,
- access reviews for systems with personal-data relevance,
- technical evidence for safeguards,
- service provider and contract references,
- incident handoff protocols,
- action log for data-protection/security findings.

### Advanced practice

Goal: personal information protection is integrated into architecture, tooling, and situational awareness.

1. Data flows, data classification, asset inventory, and safeguards are connected for critical processes.
2. Privacy- and security-by-design checks are part of product development, procurement, cloud, and AI approvals.
3. Sensitive personal data receives stronger access control, logging, encryption, pseudonymization, or segmentation, insofar as professionally decided.
4. Monitoring detects suspicious access, mass exports, or misconfigurations and leads to incident triage.
5. Deletion and retention requirements are tested in a technically traceable way.
6. Management receives decision-capable information on residual risks, overdue actions, service provider topics, and resource needs.

## Routine flow

1. **Change or new data context arises:** process, system, tool, export, service provider, log source, or incident.
2. **Identify personal-data relevance:** roughly record data types, affected groups, purpose, and data flow.
3. **Clarify owner and protection need:** connect business function, system responsibility, security role, and data-protection role.
4. **Review safeguards:** access, encryption, logging, backup, deletion, service provider, monitoring, and incident path.
5. **Trigger handoffs:** Data Protection/Legal for legal basis, data subject rights, retention, analysis, transfer, or high sensitivity.
6. **Implement and provide evidence:** document measures in tickets, configurations, approvals, or register entries.
7. **Review:** check access, data flow, service provider, deletion, and events regularly or trigger-based.
8. **Escalate:** bring unresolved residual risks, resource gaps, or incidents into the responsible decision format.

## Decisions

- Which processes and systems with personal information are critical?
- Which data types need additional safeguards?
- Which roles may view, export, or analyze personal data?
- Which logging or monitoring is necessary and clarified from a data-protection perspective?
- Which service providers, cloud regions, or interfaces need review?
- How are deletion, retention, backup, and archiving brought together?
- When is a security event handed over to Data Protection, Legal, Management, or Communications?

## Evidence

### Strong evidence

- process/system overview with personal-data relevance, owner, and protection need,
- referenced data-protection and security checks,
- access review and evidence of corrected rights,
- technical safeguard and configuration evidence,
- service provider and contract references with security relation,
- deletion/blocking or retention evidence,
- incident handoff with data-protection assessment by the responsible role,
- management decision for accepted residual risk or resource gap.

### Weak evidence

- general privacy notice without system or operational relation,
- asset list without data types or owner,
- TOM document without evidence of implementation,
- access list without review decision,
- blanket statement “DPO is informed” without open point or decision,
- training evidence without relation to concrete roles and data processes.

### Evidence gaps

- unknown data flows or shadow exports,
- no connection between processing, system, and safeguard,
- external service providers without security/data-protection handoff,
- logs with personal-data relevance without clarified purpose and access,
- deletion requirements not technically implemented or tested,
- incident process without data-protection checkpoint.

## Effectiveness review

Review questions:

- Are the most important personal information assets in ISMS scope known and assigned to an owner?
- Are access, export, logging, and service providers for critical data reviewed regularly?
- Are Data Protection handoffs actually triggered for changes and incidents?
- Is there evidence that safeguards are technically implemented and not only described?
- Are deletion, blocking, and retention requirements traceable in operations?
- Are findings translated into actions, risk decisions, or management decisions?

Possible metrics:

- share of critical systems with personal-data relevance and owner,
- overdue security/data-protection checks,
- open actions relating to personal information,
- critical access deviations,
- service providers with open evidence status,
- incidents with documented Data Protection handoff.

## BSIG/NIS2 connection point

The protection of personal information is connectable to NIS2-oriented risk management measures, incident handling, access protection, supply-chain security, secure procurement, cyber hygiene, and management oversight. The specific connection should be assessed in an organization-specific way in the requirements register, data-protection process, and ISMS risk register.

This artifact does not replace data-protection advice, legal advice, or a binding assessment of reporting, information, or documentation obligations.

## Boundaries

- No legal or data-protection advice and no statement on the lawfulness of processing.
- No assessment of data subject rights, legal bases, reporting obligations, or international transfers by the artifact.
- No certification, conformity, or security commitment.
- No ISO 27002 text or standards-substitute wording.
- No real personal data, customer information, or secret data in public examples.

## Handoffs

- **Data Protection handoff:** new or changed processing, logs/monitoring, analyses, deletion, data subject rights, incident with personal-data relevance.
- **Legal handoff:** contract, liability, reporting, communication, or transfer questions.
- **HR handoff:** employee data, role change, training, monitoring with work relation.
- **IT/Platform handoff:** technical safeguards, access, encryption, backup, deletion, logging.
- **Procurement/Vendor handoff:** service providers, SaaS, sub-processors, evidence, and security requirements.
- **Incident handoff:** suspected data leakage, incorrect authorization, misdirected sending, compromised account.
- **Management handoff:** resources, residual risks, prioritization, external communication after responsible review.
- **Audit/Evidence handoff:** missing evidence, unclear owners, actions that cannot be reviewed.

## Typical mistakes

- Data protection is treated as a separate documentation topic and not connected with system operations.
- TOMs are described, but technical implementation and review are missing.
- Logs and reports contain personal data without clarified access and purpose.
- Deletion concepts ignore backups, archives, or SaaS exports.
- Service providers are managed contractually, but security evidence is not tracked.
- Security events are handled technically without Data Protection handoff.
- AI or analytics tools are tested with personal data before approval and data class are clarified.

## Fictional mini example

A fictional business function wants to use a new SaaS tool for support requests. The Process Owner records that customer names, email addresses, and ticket contents are processed. IT checks MFA, roles, export functions, and logging. Data Protection assesses the processing and open contract questions. Procurement tracks the service provider relation. Before production start, an access matrix is approved; an open deletion point remains as an action with follow-up in the ISMS log.

Evidence:

- system entry with personal-data relevance and owner,
- security/data-protection check,
- access matrix,
- service provider reference,
- action ticket for the deletion point,
- approval protocol before production start.
