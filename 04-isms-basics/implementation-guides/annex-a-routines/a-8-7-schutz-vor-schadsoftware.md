# A.8.7 — Protection against malware

## Purpose

Protection against malware reduces the likelihood that malicious code is executed on endpoints, servers, cloud workloads, email systems, storage, mobile devices, or development environments and causes damage unnoticed. The core is not “an antivirus scanner is installed”, but an operated protection, monitoring, and response routine.

## Control objective in repository language

The organization operates a traceable routine for prevention, detection, handling, and improvement in dealing with malware. Protection mechanisms, responsibilities, coverage, alerts, exceptions, incident handoffs, and lessons learned are connected in such a way that technical warnings become actionable decisions.

## Typical risks

- If endpoints, servers, or cloud workloads are not covered, malware can be executed unnoticed.
- If protection signatures, sensors, or policies are outdated, protection becomes superficial.
- If alerts are not assigned to anyone, infections or suspicious activities remain untreated.
- If exceptions for performance or compatibility become permanent, blind spots arise.
- If email, web, USB, or download paths are not considered, malware reaches users and systems more easily.
- If recovery and incident response are not integrated, containment takes too long.

## Triggers

- new endpoint, server, cloud workload, mobile device, development environment, or storage location.
- new protection solution, policy change, exception, or deactivation of a protection mechanism.
- malware alert, suspicious behavior, phishing wave, compromised account, or incident.
- vulnerability notice, new attack wave, or vendor advisory.
- audit finding, missing coverage, outdated signatures, or sensor failure.
- new data transfer paths such as email gateway, web proxy, file exchange, external media, or SaaS storage.
- periodic review of coverage, alerts, exceptions, and effectiveness.

## Roles and responsibilities

- **Endpoint / platform owner:** operates protection agents, policies, updates, and technical coverage.
- **Security operations / security role:** triages alerts, defines detection logic, and manages escalations.
- **IT operations / service desk:** supports containment, reinstallation, user communication, and recovery.
- **Service owner / asset owner:** assesses impacts on service, data, and business process.
- **ISMS owner:** ensures review logic, exception handling, evidence, and management handoff.
- **Awareness / HR function:** supports user enablement for phishing, downloads, and reporting paths.
- **Data protection / legal:** reviews personal-data analyses, possible data protection incidents, and external communication.
- **Management:** decides on residual risks, resource needs, tooling, exception rates, or operational interruptions.

## Implementation

### Minimum start

Goal: cover important systems, handle alerts, and make exceptions visible.

1. Critical endpoints, servers, cloud workloads, email systems, and file storage in the ISMS scope are named.
2. For these targets, it is defined which protection mechanism is active and who handles alerts.
3. Protection status, update/signature status, and sensor availability are checked regularly.
4. Malware alerts are recorded as a ticket or incident pre-assessment.
5. Exceptions, deactivations, and uncovered systems receive a justification, expiry date, and review.
6. Users know a reporting path for suspicious files, emails, or system behavior.

Minimum evidence:

- coverage list with owner,
- protection status or agent export,
- alert/ticket evidence,
- exception or deactivation log,
- communication evidence for the reporting path.

### Solid practice

Goal: malware protection is operated on a risk-based basis and connected to incident response.

1. Protection mechanisms are differentiated by asset type and risk: client, server, cloud, email, web, mobile devices, development environments.
2. Alerts are prioritized by criticality, spread, affected data, behavior, and possible exploitation.
3. Containment steps are prepared: isolate, check account, block file, clean systems, rebuild, initiate recovery.
4. Exceptions are regularly reviewed for necessity, compensation, and expiry.
5. Repeated findings feed into awareness, hardening, patch management, and email/web protection.
6. Protection status and top risks are addressed in the ISMS review and, where needed, in the management review.

### Advanced practice

Goal: malware protection is operated as an integrated detection and response capability.

1. Endpoint, server, cloud, email, and identity signals are brought together in security monitoring or incident triage.
2. Behavior-based detection, controlled execution, application control, or sandboxing are used on a risk-based basis.
3. Automated containment is used for clearly defined scenarios without losing human escalation for critical impacts.
4. Threat intelligence and incident lessons learned update detection rules, blocklists, and user communication.
5. Protection gaps are reconciled with asset inventory, vulnerability management, backup, and BCM.
6. Management receives metrics on coverage, alert quality, containment time, exception rate, and recurring causes.

## Routine flow

1. **Update scope:** include new or changed assets, data paths, and platforms.
2. **Check protection status:** check agents, policies, signatures, sensors, gateways, and updates.
3. **Triage alerts:** assess affected systems, users, data, spread, and severity.
4. **Contain:** limit network access, account, file, process, or system depending on the situation.
5. **Handle:** clean, rebuild, patch, block, restore, or start the incident process.
6. **Evidence:** document alert, decision, measure, result, and open risks.
7. **Review:** check coverage, exceptions, false positives, response times, and recurring patterns.
8. **Improve:** adjust policies, awareness, hardening, backup, monitoring, or procurement.
9. **Escalate:** hand larger spread, data relevance, operational interruption, or residual risk to management, legal, data protection, or BCM.

## Decisions

- Which asset types and data paths must be protected and monitored without exception?
- Which alerts trigger a ticket, incident pre-assessment, or formal incident?
- Who may deactivate protection mechanisms or approve exceptions?
- Which compensating measures apply to systems that cannot be covered?
- When is a system cleaned, isolated, rebuilt, or restored?
- Which personal-data analyses are required for triage and monitoring and need to be clarified?

## Evidence

### Strong evidence

- coverage of critical assets with protection status and owner,
- policy and update/signature evidence,
- alert tickets with triage, decision, and measure,
- evidence of containment, cleanup, or recovery,
- exception decisions with expiry date and compensation,
- lessons learned from malware incidents,
- management decision for residual risks or resource needs.

### Weak evidence

- proof of purchase of a protection solution without coverage review,
- screenshot of an agent without scope,
- alert statistics without triage or measures,
- blanket statement “handled by the service provider” without feedback,
- exception list without expiry date,
- awareness campaign without connection to findings or reporting path.

### Evidence gaps

- unknown systems without protection agent,
- outdated or deactivated sensors without decision,
- alerts without owner,
- repeated malware findings without root cause analysis,
- no integration of backup or incident response,
- no documentation of whether data or critical services were affected.

## Effectiveness review

Review questions:

- Are critical endpoints, servers, cloud workloads, and data paths covered?
- Are protection status and sensor availability checked regularly?
- Can alerts be assigned to an owner, a decision, and a measure?
- Are exceptions time-limited and operated with compensation?
- Do recurring findings flow back into patch management, hardening, or awareness?
- Is it clear when malware findings become an incident, data protection, or BCM topic?

Possible metrics:

- coverage of critical assets,
- systems with outdated or missing protection,
- malware alerts by severity and status,
- average triage and containment time,
- exception rate and overdue exceptions,
- recurring findings per asset group,
- share of alerts with documented decision.

## BSIG/NIS2 connection point

Protection against malware is compatible with NIS2-oriented topics such as cyber hygiene, incident prevention, detection, response, business continuity, vulnerability management, and secure operational processes. The specific connection point should be assessed in the requirements register, risk analyses, and incident/BCM documentation in an organization-specific way.

This artifact does not replace legal review of reporting obligations, data protection implications, or applicability.

## Boundaries

- This artifact is not a recommendation for a specific EDR, antivirus, or gateway product.
- It does not replace incident response planning, backup strategy, or technical forensics.
- Malware protection does not guarantee damage prevention.
- Personal monitoring and triage data require appropriate review.
- No ISO 27002 texts, no real malware details from confidential cases.

## Handoffs

- **Incident handoff:** confirmed infection, spread, data relevance, compromised accounts, or critical systems.
- **Backup/recovery handoff:** cleanup insufficient, restoration or rebuild required.
- **BCM handoff:** malware endangers critical services, production capability, or recovery objectives.
- **Data protection/legal handoff:** personal data affected, monitoring analysis, possible external communication.
- **Patch/hardening handoff:** recurring findings caused by vulnerabilities, macros, scripts, insecure configurations.
- **Awareness handoff:** phishing, downloads, reporting path problems, or user errors as cause.
- **Management handoff:** high residual risks, tooling gaps, exception rate, resource needs, or operational interruption.
- **Audit/evidence handoff:** missing coverage, unclear alert handling, or exceptions that are not traceable.

## Typical mistakes

- An installed protection solution is confused with effective operation.
- Uncovered systems are not made visible in the asset inventory.
- Alerts stay in the tool instead of reaching tickets or incident triage.
- Exceptions become permanent for performance reasons.
- Development, server, or cloud workloads are protected worse than office devices.
- Malware findings do not lead to lessons learned.
- Management receives alert volumes, but no risk assessment or decision question.

## Fictional mini example

A fictional service provider receives several malware alerts on two development workstations. Security operations creates tickets, isolates the devices, and checks whether repository access is affected. The workstations are rebuilt; an outdated browser plug-in is identified as the cause. The ISMS owner documents a measure to harden developer images and a short awareness briefing on suspicious downloads.

Evidence:

- alert tickets,
- isolation and rebuild evidence,
- review of affected access,
- measure for image hardening,
- awareness briefing and review note.
