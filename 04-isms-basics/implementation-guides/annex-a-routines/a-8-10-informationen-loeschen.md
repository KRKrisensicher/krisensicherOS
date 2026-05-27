# A.8.10 — Deleting information

## Purpose

Deleting information means taking data, copies, caches, storage media, and access paths out of operation in a controlled way when they are no longer needed or must be deleted. The core is not a deletion promise, but a traceable routine: what is deleted when, by whom, where technical remnants remain, and who decides on exceptions?

## Control objective in repository language

The organization operates a routine for planned, event-driven, and verifiable deletion of information across systems, storage media, cloud services, backups, mobile devices, logs, and service providers. Deletion is connected with information classification, retention rules, permissions, contract termination, system decommissioning, and data protection/legal handoffs.

## Typical risks

- If information remains in repositories, mailboxes, exports, or shadow copies beyond its purpose of use, the risk of unauthorized viewing and later data leakage increases.
- If systems are taken out of operation but databases, snapshots, or storage media are not handled in a controlled way, usable legacy data remains.
- If deletions are only manual and informal, no one can prove which data was actually affected.
- If backups, logs, and archives are not included in the deletion logic, pseudo-evidence and unexpected restoration of old data arise.
- If service provider data is not confirmed as deleted or returned after contract termination, responsibility remains unclear.

## Triggers

- End of a business process, contract, project, service provider access, or system.
- Expiry of a defined retention period or loss of a business purpose for use.
- Decommissioning, migration, tenant change, or retirement of devices and storage media.
- Data protection/legal requirement, data subject request, or internal deletion request with human review.
- Security event, unauthorized data stock, audit finding, or cleanup measure.
- Change in data classification, storage architecture, backup strategy, or cloud/SaaS use.
- Regular review of data repositories, shares, exports, logs, and legacy archives.

## Roles and responsibilities

- **Information Owner / Process Owner:** determines business purpose, retention need, and approval for deletion.
- **IT / Platform Owner:** implements deletion, secure decommissioning, media handling, and technical evidence.
- **Data Protection / Legal:** reviews deletion requests, retention obligations, personal data, and dispute/evidence situations.
- **Records / Document Owner:** coordinates retention and archive logic where present.
- **Supplier Management:** obtains deletion/return confirmations and contractual evidence.
- **ISMS Owner / Security Role:** defines minimum logic, evidence requirements, risk paths, and escalation paths.
- **Management:** decides on target conflicts between deletion, evidence needs, operational risk, costs, and residual risk.

## Implementation

### Minimum start

Goal: be able to delete critical data repositories and system decommissioning cases in a controlled way.

1. The organization identifies data repositories with high protection needs, old repositories, and systems in the ISMS scope.
2. Each repository has a business owner and a technical contact.
3. Deletion events are recorded in a simple deletion log or ticket: repository, trigger, owner, decision, method, date, evidence.
4. System decommissioning, device retirement, and contract termination receive a deletion/return checklist.
5. Exceptions are documented for a limited period, for example due to evidence needs, backup cycles, or ongoing clarification.
6. At least annually, spot checks verify whether legacy data and exports are still needed.

Minimum evidence:

- list of critical data repositories with owner,
- deletion or decommissioning ticket,
- approval by the business owner,
- technical deletion or destruction evidence,
- exception with rationale and follow-up date.

### Solid practice

Goal: deletion is connected with data lifecycle, retention, and service provider control.

1. Data classes receive deletion and retention logic that is reviewed from business and legal perspectives.
2. Systems, databases, file shares, SaaS services, logs, backups, and archives are linked to responsible owners.
3. Deletion methods are defined by context: logical deletion, secure overwriting, key destruction, media destruction, tenant cleanup, or service provider confirmation.
4. Migrations and decommissioning include mandatory steps for residual data, snapshots, test copies, and temporary exports.
5. Regular reviews identify orphaned repositories, legacy projects, uncontrolled exports, and overdue data repositories.
6. Deletion conflicts are decided: retention, evidence preservation, data protection, operations, costs, and risk.

Strong evidence:

- data repository/system list with deletion owner,
- reviewed deletion and retention rules,
- tickets with approval, execution, and validation,
- storage media destruction or deletion certificates,
- service provider confirmations,
- review minutes for legacy data,
- management decision on conflicts or residual risks.

### Advanced practice

Goal: deletion is automated, risk-based, and controllable across data flows.

1. Data classification, retention periods, DLP/discovery results, and system inventory are connected.
2. Deletion runs are technically logged and escalated when errors occur.
3. Key management supports controlled rendering inaccessible of encrypted data repositories where suitable and reviewed.
4. Cloud and SaaS services are regularly checked for export, recycle bin, snapshot, and tenant residual data.
5. Backup and archive concepts specify when deletion requests take effect immediately, with delay, or only through expiry cycles.
6. Metrics show overdue deletions, legacy data, exceptions, unassignable data repositories, and open service provider confirmations.

## Routine flow

1. **Deletion trigger arises:** retention period expiry, system decommissioning, contract termination, request, review finding, or incident.
2. **Clarify scope:** determine affected data repositories, copies, systems, backups, service providers, and storage media.
3. **Check approval:** business owner confirms end of use; Legal/Data Protection reviews retention or blocking reasons if relevant.
4. **Define method:** select suitable deletion, blocking, destruction, or key measure.
5. **Implement:** IT, business unit, or service provider performs deletion in a controlled way.
6. **Validate:** check sample, log, system status, certificate, or service provider confirmation.
7. **File evidence:** document decision, execution, residual data, and exceptions.
8. **Escalate:** send unclear retention, missing owner, technical non-deletability, or cost conflict to management or Legal/Data Protection.
9. **Improve:** feed causes of legacy data back into data retention, roles, system design, or procurement.

## Decisions

- Which data repositories and storage media are critical enough for the start?
- Who may approve deletion, suspend it, or accept an exception?
- How are backups, archives, logs, snapshots, and recycle bins handled?
- Which deletion methods are appropriate for which data class and platform?
- When is a service provider confirmation sufficient, and when is additional review needed?
- How are target conflicts between deletion, evidence obligations, operations, and forensics decided?

## Evidence

### Strong evidence

- current data/system scope with owners,
- deletion request with trigger, approval, and date,
- technical deletion log or storage media destruction evidence,
- documented handling of backups, archives, and residual copies,
- service provider confirmation for externally stored data,
- review evidence for legacy data and corrective measures,
- exception with duration, risk decision, and follow-up date.

### Weak evidence

- general deletion policy without concrete execution,
- verbal confirmation that “it was deleted”,
- screenshot of an empty folder without scope,
- ticket without business approval or validation,
- service provider contract without concrete deletion confirmation,
- retention plan without system reference.

### Evidence gaps

- unknown copies in test systems, exports, mailboxes, or shadow repositories,
- no rule for backups and snapshots,
- storage media retirement without evidence,
- service provider termination without return/deletion confirmation,
- permanent exceptions without decision,
- no owner for legacy archives.

## Effectiveness review

Review questions:

- Can critical data repositories be assigned to an owner and deletion logic?
- Are deletion triggers actually processed in tickets or logs?
- Are backups, archives, logs, exports, and test copies visible in the routine?
- Is there evidence that deletions were validated or service provider confirmations obtained?
- Are unclear retention or data protection questions escalated in time?
- Are legacy data stocks reduced and causes of new legacy stocks corrected?

Possible metrics:

- overdue deletion requests,
- share of critical data repositories with owner and deletion logic,
- open service provider confirmations,
- number of orphaned legacy data stocks,
- exception rate and overdue exceptions,
- time from deletion trigger to evidence.

## BSIG/NIS2 connection point

Controlled deletion is compatible as a connection point with NIS2-oriented risk management measures, cyber hygiene, access protection, handling of sensitive information, supplier control, and incident follow-up. For affected organizations, the concrete connection should be assessed in the requirements register and in data/system inventories.

This artifact does not replace legal or data protection review of deletion obligations, retention obligations, or data subject rights.

## Boundaries

- This artifact is not a legal or data protection opinion on deletion periods.
- It does not replace a forensic preservation decision or an archiving strategy.
- It does not guarantee that all technical residual data has been completely removed.
- It contains no ISO 27002 text and no certification assurance.
- Public examples must not contain real organizational, customer, personal, or secret data.

## Handoffs

- **Data Protection / Legal Handoff:** deletion requests, retention obligations, personal data, disputes, evidence preservation.
- **IT / Platform Handoff:** technical deletion, backups, snapshots, storage media, keys, validation.
- **Supplier Handoff:** contract termination, cloud/SaaS data, subprocessors, deletion/return confirmation.
- **Incident Handoff:** unauthorized data stock, data leakage, forensic preservation before deletion.
- **BCM Handoff:** deletion or key destruction can affect recoverability or emergency operations.
- **Management Handoff:** costs, technical non-deletability, residual risk, permanent exception.
- **Audit / Evidence Handoff:** missing evidence or deletion decisions that cannot be reviewed.

## Typical mistakes

- Deletion is understood as an IT task without business approval.
- Backups, logs, test data, and exports are forgotten.
- Decommissioned systems remain reachable as data graveyards.
- Service provider confirmations are not obtained after contract termination.
- Exceptions are not time-limited.
- Deletion periods are asserted generically without legal/data protection review.
- Data is deleted even though evidence preservation or retention is still unclear.

## Fictional mini example

A fictional mechanical engineering service provider shuts down an old project portal. The service owner confirms that the project data is no longer operationally needed. Legal reviews which documents still need to be retained. IT exports the approved archive portion, deletes the portal tenant, documents backup handling through regular expiry cycles, and has the hosting service provider confirm tenant deletion. An old test data copy is found during review and deleted separately.

Evidence:

- decommissioning ticket with business approval,
- Legal/Data Protection review note without legal advice in the artifact,
- technical deletion log,
- service provider confirmation,
- evidence of test data cleanup,
- exception note for backup expiry cycles.
