# A.5.16 — Identity management

## Purpose

Identity management ensures that digital and organizational identities are unique, traceable, and managed across their lifecycle. This includes employees, external staff, service providers, technical accounts, service accounts, API identities, and privileged identities.

The core is not “a user account exists”, but a reliable identity routine: who or what is an identity, which owner is responsible, when is it created, changed, blocked, reviewed, or deleted, and how does misuse become visible?

## Control objective in repository language

The organization operates a traceable routine for creating, changing, reviewing, and ending identities in the ISMS scope. The routine connects HR and supplier events, authoritative identity sources, role references, technical implementation, access control, evidence, exception handling, and escalation.

## Typical risks

- If identities are not clearly assigned to people, roles, or technical purposes, actions cannot be traced.
- If accounts remain active without a valid reason, unnoticed access and attack opportunities arise.
- If collective accounts or shared accounts are used, accountability and traceability are lost.
- If external or technical identities have no owner, expiry, rotation, permissions, and deactivation remain unclear.
- If identity data from HR, supplier management, and IT do not match, joiner/mover/leaver processes fail.

## Triggers

- Hiring, role change, team change, longer absence, or departure.
- Start, change, or end of external work or service provider access.
- New system, new platform, new interface, new API, or new service account.
- Change to role model, organizational structure, or identity source.
- Security event, account compromise, suspicious login, or audit finding.
- Periodic identity and account review.
- Migration to cloud, SSO, IAM, PAM, or a new collaboration environment.

## Roles and responsibilities

- **HR / People function:** provides reliable events for internal personal identities.
- **Manager / Process owner:** confirms role reference, start, change, end, and business need.
- **Supplier management / Procurement:** manages external parties, contract reference, and end of external identities.
- **Identity owner / IAM responsible role:** operates identity source, account logic, lifecycle, and reconciliation.
- **IT/platform owner:** implements accounts, groups, technical identities, and system integration.
- **Asset owner / Service owner:** is responsible for identities with access to own systems or data.
- **ISMS owner / Security role:** defines minimum requirements, reviews, exception handling, and escalation.
- **Data protection / Legal:** assesses personal-data analysis, employee data, logging, and contractual questions.
- **Management:** decides on collective accounts, resource conflicts, residual risks, or tool investments.

## Implementation

### Minimum start

Goal: Critical identities are unique, assigned, and can be ended.

1. The organization names an authoritative source for internal personal identities and a responsible body for external identities.
2. New identities are created only with a reason, owner, role, or purpose.
3. Departure, role change, and contract end trigger blocking, change, or deletion.
4. Critical systems and privileged accounts are checked for orphaned, shared, or non-assignable identities.
5. Technical accounts receive at least an owner, purpose, system reference, and review date.
6. Exceptions such as collective accounts are justified, time-limited, and risk-assessed.

Minimum evidence:

- identity or account list for critical systems,
- joiner/mover/leaver tickets,
- owner and purpose evidence for technical accounts,
- review record for critical identities,
- exception decision for shared or non-standard accounts.

### Solid practice

Goal: Identity lifecycles are repeatable and connected with access control.

1. Identity types are distinguished: internal person, external person, privileged identity, technical identity, service account, break-glass account.
2. Lifecycle rules define creation, change, blocking, deletion, expiry, and review by identity type.
3. HR, supplier, and IT processes are connected with account creation and termination.
4. Naming conventions, unique IDs, and responsibilities prevent confusion.
5. Shared accounts are avoided or managed as exceptions with additional controls.
6. Identity reviews examine orphaned, inactive, duplicate, privileged, and external identities.
7. Findings lead to blocking, correction, exception, or management decision.

Strong evidence:

- identity type and lifecycle model,
- joiner/mover/leaver evidence,
- account exports from critical systems,
- review list with decisions,
- evidence of blocked or deleted accounts,
- technical accounts with owner, purpose, and expiry,
- exception and risk acceptance log.

### Advanced practice

Goal: Identities are operated as a controlled, measurable, and integrated governance building block.

1. Central identity source, SSO, IAM, PAM, MDM, and relevant business systems are integrated based on risk.
2. External and technical identities have expiry dates, automatic follow-up, or recertification.
3. Privileged and break-glass identities are monitored particularly closely and tested regularly.
4. Machine identities, API tokens, certificates, and secrets are managed with rotation, expiry, and owner.
5. Notable identity events feed into monitoring and incident triage.
6. Metrics show orphaned accounts, external identities, technical accounts, overdue reviews, and lifecycle times.
7. Management decides structural target conflicts, such as legacy collective accounts, tooling, or resources.

## Routine flow

1. **Identity need arises:** new person, external role, technical purpose, system, or interface.
2. **Check reason and owner:** clarify business need, role, contract, system reference, or technical purpose.
3. **Create identity:** record unique ID, type, start date, owner, expiry, or review date.
4. **Link access:** grant permissions through the separate access control routine.
5. **Process changes:** update role change, team change, contract change, or purpose change.
6. **Perform review:** check inactive, external, privileged, technical, and orphaned identities.
7. **End:** block, delete, revoke tokens, rotate certificates, or replace service account.
8. **Escalate deviations:** handle non-assignable, shared, or critical identities.
9. **Improve:** correct causes of orphaned or incorrect identities in HR, supplier, or IT processes.

## Decisions

- Which source is authoritative for which identity types?
- Which identities may exist without an expiry date?
- How are external and technical identities owned and reviewed?
- Which collective accounts are prohibited, and which are temporarily tolerated?
- When does an identity issue become an incident?
- Which systems must be included in lifecycle reviews first?
- Which target conflicts between operations, legacy systems, and traceability go to management review?

## Evidence

### Strong evidence

- identity model with types, owners, and lifecycle rules,
- HR/supplier events with IT tickets,
- account exports from critical systems at review time,
- review records with blocking, deletion, or correction decisions,
- evidence for deactivated former or orphaned accounts,
- technical identities with owner, purpose, expiry, and rotation,
- exception decision for collective or legacy accounts,
- management decision for permanent residual risk.

### Weak evidence

- user list without owner, role, or status,
- general IAM policy without execution,
- manual Excel list without reconciliation with systems,
- statement “HR reports departures” without ticket or blocking evidence,
- technical accounts with descriptive names, but without accountable owner.

### Evidence gaps

- external identities without contract end or owner,
- technical accounts without purpose and review date,
- collective accounts without exception decision,
- inactive accounts without blocking,
- no connection between identity and access,
- no logging of critical identity changes.

## Effectiveness review

Review questions:

- Are critical identities clearly assigned to a person, role, organization, or technical purpose?
- Are departures, role changes, and contract ends reliably translated into account changes?
- Are there reviews for external, privileged, and technical identities?
- Are orphaned, inactive, or duplicate accounts found and cleaned up?
- Are collective accounts justified traceably and limited in time?
- Are notable cases escalated to incident response or management?

Possible metrics:

- overdue identity reviews,
- number of orphaned or inactive accounts,
- external identities without expiry date,
- technical accounts without owner,
- time from departure to account blocking,
- exception rate for collective accounts,
- number of corrected identity findings.

## BSIG/NIS2 connection point

Identity management is compatible with NIS2-oriented risk management measures, access protection, cyber hygiene, secure administration, incident prevention, supply chain security, and governance. For affected organizations, the requirements register should be used to assess which identity types, systems, and evidence are relevant.

This artifact does not replace legal review of employee data, monitoring, contractual relationships, or statutory requirements.

## Boundaries

- This artifact is not a complete IAM, SSO, or PAM architecture design.
- It does not replace a data protection review for logging, analysis, or employee data.
- It makes no certification, conformity, or security guarantee.
- It contains no ISO 27002 text and no product recommendation.
- Identity management does not replace the separate decision on concrete access rights.

## Handoffs

- **HR handoff:** hiring, role change, absence, departure, master data quality.
- **Supplier handoff:** external identities, contract start, contract end, subcontractors, evidence.
- **Access control handoff:** permissions, recertification, privileged rights, and withdrawal.
- **IT/platform handoff:** IAM, SSO, directory services, local accounts, service accounts, certificates, tokens.
- **Data protection/legal handoff:** personal-data analysis, monitoring, employee data, contractual questions.
- **Incident handoff:** compromised account, unclear identity, suspicious login, suspected misuse.
- **Management handoff:** legacy collective accounts, resource need, accepted residual risks, or tool decision.
- **Audit/evidence handoff:** incomplete account lists, missing owners, or non-traceable lifecycle decisions.

## Typical mistakes

- Identity management is confused with permission management.
- External persons are treated like internal accounts, but without contract end.
- Service accounts remain permanently active because nobody owns them.
- Collective accounts are used for convenience and not managed as exceptions.
- HR data, supplier lists, and system accounts are not reconciled.
- Reviews consider only active employees, not technical and privileged identities.
- Accounts are blocked, but tokens, certificates, or API keys remain active.

## Fictional mini example

A fictional SaaS service is introduced for customer service. In addition to internal users, an external implementation partner needs three time-limited accounts and one technical API account. The process owner confirms purpose and duration. IT creates the identities with expiry dates and links rights to access control. In the review after project end, two external accounts are deactivated; the API account remains, but receives a service owner, rotation date, and follow-up.

Evidence:

- identity creation with type, owner, purpose, and expiry,
- supplier reference for external accounts,
- review record after project end,
- deactivation evidence,
- API account entry with owner and rotation date,
- open follow-up for the next review.
