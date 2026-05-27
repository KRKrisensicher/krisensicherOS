# A.5.33 — Protection of records and evidence

## Purpose

This routine ensures that business-, security-, and evidence-relevant records are not created by chance, stored in scattered locations, or changed without review. It protects evidence so that decisions, reviews, incidents, audits, and management questions remain traceable.

The core is not the maximum amount of documentation, but robust evidence: Which record is important, who is responsible, how long is it needed, how is it protected, and when may it be deleted or archived?

## Control objective in repository language

The organization operates a routine for creation, storage, protection, access, retention, integrity, retrievability, and orderly deletion of relevant records. Legal, contractual, data-protection, and business requirements are clarified through responsible human roles.

## Typical risks

- If security evidence cannot be found afterwards, decisions, incidents, or reviews cannot be substantiated.
- If records can be changed without control, evidence loses its explanatory value.
- If sensitive evidence is accessible too broadly, confidentiality and data-protection risks arise.
- If retention periods are unclear, evidence is deleted too early or retained unnecessarily long.
- If logs, approvals, and exceptions exist only in personal mailboxes, the organization depends on individuals.
- If automated logs and manual documents are not connected, gaps remain in the event or decision history.

## Triggers

- new process, new system, new register, new service provider, or new evidence type.
- audit, internal review, customer requirement, management question, or evidence request.
- security event, suspected data-protection incident, escalation, or lessons learned.
- change in retention, contractual, legal, or data-protection requirements.
- migration, archiving, system shutdown, or change of storage platform.
- planned review of evidence packs, logs, approvals, exceptions, or management decisions.
- role change or departure of persons with evidence responsibility.

## Roles and responsibilities

- **Record Owner / Process Owner:** defines which records arise, what they are needed for, and who maintains them.
- **ISMS owner:** defines minimum requirements for security evidence, review logic, and evidence packs.
- **IT / Platform Owner:** provides storage, backup, access, logging, and technical safeguards.
- **Legal:** assesses legal retention, evidentiary needs, contractual requirements, and deletion holds.
- **Data Protection:** reviews personal content, storage limitation, access need, and deletion logic.
- **Business functions:** create business approvals, decisions, reviews, and operational evidence.
- **Internal review / Audit:** checks traceability, completeness, and evidence quality.
- **Management:** decides in cases of resource need, retention/deletion conflicts, or accepted evidence gaps.

## Implementation

### Minimum start

Goal: the most important evidence is findable, protected, and owned.

1. Critical evidence types are named: policies, approvals, risk decisions, exceptions, access reviews, incident evidence, supplier evidence, training evidence.
2. An owner and storage location are defined for each evidence type.
3. Access is limited to roles that need to create, review, or decide on evidence.
4. Changes to critical evidence remain traceable, for example through versioning, ticket, or log.
5. A simple review checks regularly whether evidence exists, is current, and can be found again.
6. Unclear retention or deletion is escalated to Legal/Data Protection.

Minimum evidence:

- evidence type list with owner,
- defined storage location,
- access or role overview,
- review note on retrievability,
- documented clarification of open retention or deletion questions.

### Solid practice

Goal: records management and ISMS evidence are operated repeatably.

1. An evidence register describes purpose, owner, protection need, retention, access, format, and review frequency.
2. Critical evidence receives versioning, change log, or approval status.
3. Records are classified by confidentiality and integrity need.
4. Evidence packs are compiled per process, control, or audit question without copying original evidence in an uncontrolled way.
5. Archiving, deletion, and blocking are coordinated with Legal and Data Protection.
6. System shutdowns and migrations include a records check.
7. Findings lead to corrections in the storage, access, or creation process.

Strong evidence:

- evidence register,
- storage and access concept,
- versioning or change evidence,
- review protocols on evidence quality,
- archiving or deletion decisions,
- evidence pack with source references,
- action log for evidence gaps.

### Advanced practice

Goal: evidence is integrated into governance, operations, and auditability.

1. Ticketing, GRC, DMS, SIEM, IAM, training, and supplier processes provide evidence in a structured and referenceable way.
2. Important decisions receive unique references, owner, expiry date, and risk/control relation.
3. Integrity and access of critical evidence are technically monitored or reviewed regularly.
4. Retention and deletion rules are supported automatically, but applied only after professional responsibility has been clarified.
5. Evidence packs show not only documents, but execution, review, decision, and improvement.
6. Management receives a decision-capable view of evidence gaps, overdue reviews, and processes that cannot be reviewed.

## Routine flow

1. **Evidence type arises or changes:** new process, review, decision, incident, audit question, or system log.
2. **Determine purpose:** What is the evidence needed for and which decision or review does it support?
3. **Define owner and storage:** clarify responsibility, storage location, access, and protection need.
4. **Define creation logic:** define format, minimum content, approval, versioning, and references.
5. **Protect:** implement access, integrity, backup, archiving, and confidentiality.
6. **Review:** sample for completeness, currency, readability, retrievability, and decision usefulness.
7. **Treat gaps:** correct missing, unclear, or outdated evidence or escalate it as a risk.
8. **Clarify retention:** manage deletion, archiving, or blocking after business, legal, and data-protection review.

## Decisions

- Which records are business-, security-, or audit-critical?
- Which evidence must be change-resistant, versioned, or especially protected against access?
- Who may create, change, review, export, or delete evidence?
- Which retention and deletion rules apply per evidence type?
- Which evidence gaps are tolerable, and which must go into management review?
- How is evidence from tools, emails, tickets, and documents brought together?

## Evidence

### Strong evidence

- evidence register with owner, purpose, protection need, and review date,
- defined storage locations and access groups,
- versioning, approval, or change logs,
- sample review with findings and actions,
- traceable archiving, deletion, or blocking decisions,
- evidence packs with sources, date, and responsible persons,
- management decision on critical evidence gaps.

### Weak evidence

- unsorted document repository without owner,
- screenshots without date, source, or context,
- old policies without approval status,
- export lists without protection need or access control,
- evidence only in personal mailboxes,
- blanket backup statement without retrievability of critical records.

### Evidence gaps

- no overview of critical evidence types,
- unclear retention or deletion practice,
- missing change traceability,
- no review evidence,
- evidence packs without original sources,
- unprotected personal or confidential evidence,
- system migration without records transfer.

## Effectiveness review

Review questions:

- Can critical evidence be found and understood within an appropriate time?
- Is it traceable who created, reviewed, or changed evidence?
- Are confidentiality, integrity, and availability of the most important evidence appropriately governed?
- Are there retention and deletion decisions with Legal/Data Protection handoff?
- Do evidence packs show actual execution and decision, not only intent?
- Are evidence gaps tracked as actions or risks?

Possible metrics:

- share of critical evidence types with owner and storage location,
- overdue evidence reviews,
- open evidence gaps by criticality,
- evidence with unclear retention status,
- retrieval time in samples,
- number of uncontrolled personal repositories for critical evidence.

## BSIG/NIS2 connection point

The protection of records and evidence is connectable to NIS2-oriented governance, risk management, incident handling, supply-chain security, management oversight, and evidence capability. The specific connection should be assessed through a requirements register and the organization-specific evidence strategy.

This artifact does not replace legal assessment of retention periods, evidentiary questions, data-protection obligations, or reporting obligations.

## Boundaries

- No legal or data-protection advice.
- No statement that existing documents prove conformity or security.
- No replacement for records management, archiving, or DMS concept.
- No ISO 27002 text or certification commitment.
- No real customer, personal, contract, or secret data in public examples.

## Handoffs

- **Legal handoff:** retention, deletion hold, contractual evidence, disputes, evidentiary need.
- **Data Protection handoff:** personal evidence, storage limitation, access/deletion relation, access restriction.
- **IT/Platform handoff:** DMS, backup, logging, versioning, access rights, migration.
- **Incident handoff:** securing incident-relevant evidence and protection against change.
- **Audit/Evidence handoff:** evidence pack, sample, missing or weak evidence.
- **Management handoff:** evidence gaps that cannot be remediated, resource need, retention/deletion conflicts.

## Typical mistakes

- Evidence is collected only for audits and not managed as an operational artifact.
- Critical decisions are in chat histories or personal emails.
- Evidence packs copy sensitive data unnecessarily broadly.
- Deletion is automated technically without business, legal, or data-protection clarification.
- Versions and approvals cannot be distinguished.
- Logs are retained, but nobody can assign them to a decision or investigation.
- Storage locations change during tool changes without records migration.

## Fictional mini example

A fictional service provider prepares an internal ISMS review. It becomes apparent that exceptions, authorization reviews, and supplier evidence are stored in different team folders. The ISMS Owner creates an evidence register, names owners, and creates an evidence-pack folder with source references. Data Protection checks that no unnecessary personal details are copied. A missing exception decision is added to the review as an action.

Evidence:

- evidence register,
- defined evidence-pack storage location,
- access group,
- review note with evidence gap,
- action ticket for the missing exception decision.
