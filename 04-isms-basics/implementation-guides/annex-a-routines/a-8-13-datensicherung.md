# A.8.13 — Backup

## Purpose

Backup ensures that information and systems can be restored after errors, attacks, user mistakes, outages, or data loss. The value is not in the existence of a backup job, but in an operated restore capability: what must be restorable within what time, to what data state, by whom, and under which conditions?

## Control objective in repository language

The organization operates a routine for planning, execution, protection, monitoring, and restoration of backups. The routine connects asset criticality, RTO/RPO, backup scope, access protection, encryption, offline/immutable protection, restore tests, incident response, BCM, and management decisions.

## Typical risks

- If backups run but are never restored, the actual recovery capability remains unknown.
- If critical systems are not backed up completely or frequently enough, unacceptable data loss arises.
- If backups are reachable with the same accounts or network paths as production systems, ransomware or user error can also destroy backups.
- If SaaS, cloud, database, or configuration data is not in scope, central recovery components are missing.
- If restore targets are not coordinated with business units and BCM, technical backups do not match crisis needs.

## Triggers

- New system, new database, new SaaS use, new cloud resource, or changed service.
- Change in criticality, RTO/RPO, data class, architecture, or operating model.
- Incident, suspected ransomware, user error, data loss, or restore request.
- Backup error, monitoring hit, expired jobs, or capacity warning.
- Migration, system decommissioning, release, infrastructure change, or supplier change.
- BCM/emergency exercise, audit finding, management question, or regular restore test.
- Change in encryption, key management, access, or retention period.

## Roles and responsibilities

- **Service Owner / Business Unit:** defines restart needs, data loss tolerance, and priority.
- **IT / Platform Owner:** plans, operates, monitors, and tests backup and restore procedures.
- **Database / Application Owner:** ensures consistency, application dependencies, and restoration sequence.
- **BCM Responsible:** connect backups with emergency operations, restart planning, and exercises.
- **ISMS Owner / Security Role:** defines protection requirements, evidence logic, risk paths, and escalation paths.
- **Data Protection / Legal:** reviews personal data, retention, deletion, encryption, and external storage.
- **Management:** decides on costs, recovery targets, residual risks, exceptions, and resources.

## Implementation

### Minimum start

Goal: make critical data restorable and not only operate backup jobs.

1. The most important systems and data repositories in the ISMS scope are identified with owners.
2. For each critical system, the desired data state and restart time are roughly defined.
3. Backup jobs are configured, monitored, and followed up when errors occur.
4. At least one restore test per critical backup area is planned and documented.
5. Access to backups is restricted and considered separately.
6. Exceptions or systems without backup are documented with risk and follow-up date.

Minimum evidence:

- list of critical systems with backup status,
- backup job and error logs,
- restore test evidence,
- access list for backup administration,
- exception or risk decision.

### Solid practice

Goal: backups are risk-based, protected, and connected with restart planning.

1. RTO/RPO are coordinated with business units and BCM and documented per service.
2. Backup scope includes data, configurations, key dependencies, infrastructure code, and relevant SaaS/cloud data.
3. Backups are protected against manipulation, encryption by attackers, and unauthorized access.
4. Restore tests check not only individual files, but also database, application, or service restoration.
5. Backup errors trigger tickets, escalations, and root cause analysis.
6. Retention period, deletion logic, and storage locations are reviewed with Legal/Data Protection where relevant.
7. Results flow into ISMS review, BCM exercises, and management review.

Strong evidence:

- service/backup matrix with RTO/RPO,
- backup configuration and job history,
- error tickets and corrective measures,
- restore test logs with result and duration,
- evidence of protected backup access,
- documentation of retention and storage location,
- management decision on unmet recovery targets.

### Advanced practice

Goal: recovery capability is robust, tested, and integrated into crisis capability.

1. Backup and restore processes are connected with CMDB, monitoring, SIEM, ticketing, and BCM plans.
2. Critical backups are immutable, offline, separately administered, or otherwise protected against compromise.
3. Restore tests include dependencies, sequences, roles, communication paths, and realistic outage assumptions.
4. Ransomware and disaster recovery scenarios are integrated into exercises.
5. Metrics show backup coverage, errors, successful restores, tested systems, restore duration, and gaps against RTO/RPO.
6. Keys, secrets, configurations, and identity services are treated separately as recovery dependencies.

## Routine flow

1. **Determine backup need:** clarify service, data class, criticality, RTO/RPO, dependencies, and owner.
2. **Define backup design:** define scope, frequency, retention, storage location, protection, encryption, and access.
3. **Set up:** implement jobs, monitoring, error handling, and documentation.
4. **Monitor:** regularly check job status, capacity, protection against manipulation, and access.
5. **Test restore:** perform file, database, application, or service restore with a realistic target.
6. **File evidence:** document result, duration, deviations, open measures, and decision.
7. **Escalate:** send backup errors, unreachable RTO/RPO, unprotected backups, or resource gaps to management.
8. **Improve:** feed findings from tests, incidents, and exercises back into backup design, BCM, and architecture.

## Decisions

- Which systems and data are critical enough for defined recovery targets?
- How much data loss and downtime is tolerable from a business perspective?
- Which backups need separate administration, immutable/offline protection, or special encryption?
- Which SaaS and cloud data are sufficiently covered by provider functions, and where is the organization’s own backup needed?
- How often are restore tests performed and how realistic do they need to be?
- Who accepts deviations from RTO/RPO or systems without backup?

## Evidence

### Strong evidence

- backup scope with service owners and criticality,
- documented RTO/RPO decisions,
- backup job history with error handling,
- restore test logs including result and duration,
- evidence of access protection, encryption, or immutable/offline protection,
- measures from failed tests,
- BCM/management decision on recovery gaps.

### Weak evidence

- screenshot “backup successful” without scope,
- backup concept without restore test,
- job list without owner or criticality,
- restore test only for a non-critical file,
- provider statement without review of the organization’s own SaaS data,
- unclear retention period without legal/data protection handoff.

### Evidence gaps

- critical systems without backup status,
- no tested restoration,
- backup administration with normal production accounts,
- no backup of configurations, keys, or identity services,
- backup errors without ticket or escalation,
- RTO/RPO not coordinated with business units.

## Effectiveness review

Review questions:

- Are critical systems and data repositories fully visible in the backup scope?
- Were restart time and data loss tolerance coordinated with the owners?
- Are backup errors detected, processed, and escalated?
- Are backups protected against manipulation, ransomware, and unauthorized access?
- Were restore tests performed and did they lead to robust results?
- Do backup capability, BCM assumptions, and management decisions align?

Possible metrics:

- backup coverage of critical systems,
- failed or overdue backup jobs,
- share of tested critical restores,
- actual restore duration compared with RTO,
- achieved data state compared with RPO,
- open recovery gaps and accepted exceptions.

## BSIG/NIS2 connection point

Backup is compatible as a connection point with NIS2-oriented risk management measures, business continuity, incident handling, crisis capability, cyber hygiene, and maintenance of critical services. The concrete connection should be assessed in an organization-specific way in the requirements register, BCM context, and management review.

This artifact does not replace legal review of retention, data protection, notification obligations, or sector-specific requirements.

## Boundaries

- A backup is not evidence of recoverability until restore has been tested.
- This artifact is not a complete disaster recovery design.
- It does not replace data protection review of retention, storage location, or deletion.
- It does not guarantee availability or certification capability.
- It contains no ISO 27002 text and no confidential architecture details.

## Handoffs

- **BCM Handoff:** RTO/RPO, restart sequence, emergency operations, exercises, and crisis decisions.
- **Incident Handoff:** ransomware, data loss, manipulation, restore during an ongoing incident.
- **IT / Platform Handoff:** backup design, monitoring, restore, access protection, keys, and storage locations.
- **Data Protection / Legal Handoff:** personal data, retention, deletion, external storage, encryption.
- **Supplier Handoff:** SaaS/cloud backup capability, restore SLAs, provider evidence.
- **Management Handoff:** unmet recovery targets, costs, technical limits, accepted exceptions.
- **Audit / Evidence Handoff:** missing restore evidence or unclear backup coverage.

## Typical mistakes

- Backups are confused with recoverability.
- Restore tests are performed only theoretically or only for non-critical files.
- SaaS data is assumed to be “backed up by the provider” without reviewing the organization’s own recovery requirement.
- Backup accounts and production admin rights are not separated.
- Configurations, secrets, keys, or identity services are missing from the recovery plan.
- Backup errors are seen in monitoring but not followed up.
- RTO/RPO are technically estimated without involving business units and BCM.

## Fictional mini example

A fictional online retailer assesses its shop system as critical. The service owner defines with BCM that orders must be restorable with only limited data loss. IT backs up the database, configuration, and relevant keys separately and tests a restore in an isolated environment every quarter. During the first test, a configuration file is missing; the finding is corrected and budget for immutable backup storage is approved in the management review.

Evidence:

- service/backup matrix with RTO/RPO,
- backup job history,
- restore test log with missing configuration,
- corrective ticket,
- management decision on backup protection,
- updated recovery instruction.
