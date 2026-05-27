# A.8.1 — Securing user endpoint devices

## Purpose

User endpoint devices are everyday work tools and, at the same time, frequent entry points. This routine ensures that laptops, desktops, smartphones, tablets and comparable work devices are not only procured and issued, but securely configured, operated, monitored, updated, returned and decided upon when deviations occur.

## Control objective in repository language

The organisation operates a traceable security routine for in-scope user endpoint devices. Every relevant device has an owner, management status, baseline configuration, protection measures, update and return process; exceptions are time-limited, justified and risk-assessed.

## Typical risks

- If endpoints remain unpatched or unmanaged, known vulnerabilities can be exploited.
- If local data is stored unencrypted, loss or theft quickly leads to information leakage.
- If private or non-approved devices are used productively, control, support and evidence are missing.
- If protection functions are disabled or not monitored, tool installation creates false assurance.
- If local admin rights, insecure software or shadow IT arise, the attack surface increases.
- If return and offboarding do not work, data, tokens and access remain on devices.

## Triggers

- New device, replacement device, BYOD/COPE/loan device or rollout.
- Joining, role change, departure or longer absence.
- New operating system, new standard software, new data class or new work model.
- Vulnerability, malware finding, EDR/MDM alert or security event.
- Loss, theft, defect or return of a device.
- Regular endpoint compliance review or audit finding.

## Roles and responsibilities

- **IT / workplace owner:** operates device management, baseline, rollout, updates and support.
- **Asset owner / manager:** confirms business need and special requirements.
- **ISMS owner / security role:** defines security minimum logic, exceptions, review and escalation.
- **Users:** report loss, anomalies and deviations; do not bypass protection measures.
- **HR / people function:** provides joining, change and departure events.
- **Data protection / Legal:** review personal device and monitoring data, BYOD questions and employee connection.
- **Management:** decides on exceptions, resource conflicts or unacceptable residual risks.

## Implementation

### Minimum start

Goal: inventory, manage and operate critical endpoint devices with baseline protection.

1. In-scope devices are recorded with asset ID, user/assignment, owner and management status.
2. A minimum standard defines: encryption, screen lock, update capability, malware/endpoint protection, central management and return path.
3. New devices are issued only with standard build or approved configuration.
4. Loss, theft and malware finding have a reporting and blocking process.
5. Offboarding triggers return, blocking and data treatment.
6. Exceptions are documented with a time limit.

Minimum evidence:

- device inventory with management status,
- standard-build or baseline evidence,
- update/protection status for sample,
- loss/incident and return process,
- exception decisions.

### Solid practice

Goal: endpoint security is repeatable, risk-based and reviewable.

1. Device groups are distinguished by use, data access and risk profile.
2. MDM/endpoint management enforces or checks central settings and security status.
3. Patch and update processes have deadlines, monitoring and escalation.
4. Local admin rights, non-approved software and devices without management status are regularly reviewed.
5. Remote work, external staff and special devices receive their own rules.
6. Loss, theft, malware or compliance deviations are connected with Incident Response.
7. Metrics and open risks feed into ISMS and Management Review.

Strong evidence:

- endpoint inventory with management and compliance status,
- baseline/configuration evidence,
- patch and update reports,
- tickets for deviations and remediation,
- evidence of loss/remote wipe/blocking,
- review records on exceptions and admin rights.

### Advanced practice

Goal: endpoints are operated as an active part of detection, zero-trust logic and resilience.

1. Device health influences access to applications or data.
2. EDR/XDR signals, vulnerability status and identity data are incorporated into triage and Incident Response.
3. Role and risk profiles steer hardening, software catalogue and update frequency.
4. Automation remediates standard deviations or isolates compromised devices.
5. Device lifecycle, procurement, return, disposal and reuse are integrated.
6. Management receives decision-ready metrics: unmanaged devices, critical patch gaps, exceptions, local admin rights and incident patterns.

## Routine flow

1. **Device need arises:** new hire, replacement, project, special role or defect.
2. **Prepare device:** asset ID, standard build, encryption, protection functions, management profile.
3. **Document issue:** assignment, user information, reporting path and return obligation.
4. **Monitor operation:** patch status, protection status, deviations, local admin rights and non-approved devices.
5. **Handle deviation:** ticket, remediation, blocking, exception or incident triage.
6. **Process role and departure events:** return, reinstallation, blocking and data treatment.
7. **Perform review:** check samples and metrics, improve patterns, escalate risks.

## Decisions

- Which device types and usage models are in scope?
- Which minimum configuration applies to which role and data class?
- When is BYOD or special hardware permitted and who accepts the risk?
- Which deviations lead to blocking, remediation or management decision?
- How quickly must critical updates and protection status deviations be handled?
- Which monitoring data may be evaluated and how?

## Evidence

### Strong evidence

- current device inventory with owner and management status,
- baseline and rollout evidence,
- patch/compliance reports with remediation status,
- tickets for deviations, malware, loss or theft,
- evidence of return, wipe or blocking,
- exception decisions with expiry date,
- management decision for systematic gaps.

### Weak evidence

- general endpoint policy without technical evidence,
- tool screenshot without scope and date,
- inventory list without management or patch status,
- statement “all devices are encrypted” without sample,
- single ticket without connection to review or measure log.

### Evidence gaps

- unknown or unmanaged devices accessing company data,
- no connection between HR events and device return,
- protection software installed but not monitored,
- local admin rights without review,
- BYOD or external devices without approval and data treatment.

## Effectiveness review

Review questions:

- Are all relevant endpoint devices inventoried and assigned to an owner?
- Is it visible which devices are managed, patched and encrypted?
- Are critical deviations handled within defined deadlines?
- Do loss, theft and offboarding routines work?
- Are special devices, external staff and BYOD consciously managed?
- Do recurring endpoint problems lead to structural improvements?

Possible metrics:

- share of managed devices in scope,
- devices with critical patch backlog,
- devices without encryption or protection status,
- local admin rights per risk group,
- overdue returns,
- open endpoint exceptions.

## BSIG/NIS2 connection point

Endpoint security is connectable to NIS2-oriented topics such as cyber hygiene, access protection, vulnerability management, incident prevention, secure remote work and protection of critical services. The specific connection should be assessed in the requirements register, in asset management and in risk management.

This artefact does not replace legal or data protection assessment of monitoring, BYOD or employee data.

## Boundaries

- This artefact is not a technical hardening baseline and not a product recommendation.
- It does not replace a data protection review for device or behavioural data.
- It makes no certification, conformity or security guarantee.
- It contains no confidential configuration details or real device data.
- An installed tool does not replace an operated review and decision routine.

## Handoffs

- **HR handoff:** joining, role change, departure, return and external staff.
- **Incident handoff:** malware, loss, theft, compromised device or EDR alert.
- **Vulnerability / patch handoff:** critical endpoint vulnerabilities, update deadlines, remediation.
- **Data protection / Legal handoff:** BYOD, monitoring, employee data, remote-wipe questions.
- **Asset / disposal handoff:** return, reuse, deletion or disposal.
- **Management handoff:** unmanaged devices, high exception rate, missing resources or risk acceptance.
- **Audit / evidence handoff:** incomplete scope, missing technical evidence or unresolved exceptions.

## Typical mistakes

- Endpoint security is confused with tool installation.
- Inventory, MDM and actual use do not match.
- Special devices and external devices remain outside the process.
- Local admin rights grow silently.
- Patch status is reported, but overdue devices are not followed up.
- Loss reports and offboarding are organisationally unclear.
- Data protection questions about monitoring or BYOD are clarified too late.

## Fictional mini example

A fictional service provider issues new laptops for a project team. The workplace team rolls out a standard build with encryption, endpoint protection and MDM profile. In the monthly review, two devices with disabled protection status appear. A support ticket is created for one; the other belongs to an external employee without the correct management profile. Access to project data is restricted until clarification and the external onboarding process is adjusted.

Evidence:

- device inventory with MDM status,
- baseline/rollout evidence,
- compliance report,
- support ticket,
- access decision for external device,
- measure in the onboarding process.
