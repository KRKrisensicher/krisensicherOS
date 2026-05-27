# A.6.5 — Security tasks during changes or termination

## Purpose

Security tasks during changes or termination ensure that role changes, internal transfers, contract endings and departures are handled in a controlled way. Access, devices, information, responsibilities and knowledge should be handed over or withdrawn in an orderly manner.

The core is a reliable mover/leaver process: do not react only on the last working day, but trigger tasks, owners, deadlines and evidence early.

## Control objective in repository language

The organisation operates a routine with which role changes and departures are recognised, assessed, implemented and evidenced from a security perspective. The routine connects HR/engagement events, access withdrawal, asset return, knowledge transfer, confidentiality/responsibility reminders, supplier context and review.

## Typical risks

- If departures are not reported to IT and business units in time, accounts, tokens or physical access remain active.
- If role changes are not cleaned up, permissions grow over time and segregation conflicts arise.
- If knowledge and responsibilities are not handed over, operational and crisis risks arise.
- If external staff or service provider endings are missing, third-party access remains uncontrolled.
- If devices, data carriers or documents are not returned, information can leak.

## Triggers

- Resignation, contract end, end of a project or planned last working day.
- Internal role change, team change, promotion, longer absence or change of tasks.
- End or change of a service provider engagement, subcontractor change or external access.
- Security event, suspected misuse or immediate withdrawal required.
- Change in protection need of a role or system.
- Periodic review of open mover/leaver cases.

## Roles and responsibilities

- **HR / people function:** triggers employee changes and departures in time and coordinates personal process steps.
- **Manager / client owner:** assesses role change, handover, knowledge retention and business access.
- **IT/IAM owner:** withdraws, changes or confirms accounts, groups, tokens, devices and technical access.
- **Asset owner / service owner:** confirms which business rights, responsibilities and data stores are affected.
- **ISMS owner / security role:** defines minimum tasks, risk criteria, escalation and sample review.
- **Procurement / supplier management:** manages external persons, contract endings and service provider access.
- **Legal / data protection:** reviews special cases, retention, communication, investigations or conflicts.
- **Management:** decides on high-risk departures, conflicts, exceptions or resource problems.

## Implementation

### Minimum start

Goal: critical changes and departures reliably trigger security tasks.

1. HR or the client owner reports changes and departures to IT, the manager and relevant owners.
2. A checklist covers at least accounts, groups, admin rights, external access, devices, keys/badges, data carriers, handover and open responsibilities.
3. Access is withdrawn or adjusted at the appropriate time.
4. Critical roles receive an additional check by the asset owner or ISMS owner.
5. Closure and exceptions are documented.

Minimum evidence:

- mover/leaver ticket,
- checklist with responsible persons and deadlines,
- evidence of withdrawn or changed access,
- asset/device return,
- handover or exception decision.

### Solid practice

Goal: changes and departures are connected with IAM, asset management and knowledge transfer.

1. Role changes trigger recertification of existing rights, not only new rights.
2. Critical accounts, service accounts, API tokens, shared secrets and admin rights are considered separately.
3. Devices, keys, badges, data carriers and document holdings are tracked through asset or facility processes.
4. Responsibilities for systems, risks, suppliers, emergency roles or open measures are handed over.
5. External staff are managed through engagement end, service provider contact and access list.
6. Samples check timely implementation and find legacy permissions.

Strong evidence:

- mover/leaver workflow,
- IAM change or withdrawal evidence,
- rights review during role change,
- asset return logs,
- handover record for critical responsibility,
- exception and escalation log,
- sample review.

### Advanced practice

Goal: change and departure control is largely integrated and monitored on a risk basis.

1. HR, supplier, IAM, asset and facility information generates automated or semi-automated tasks.
2. High-risk departures receive predefined escalation and protection measures.
3. Machine identities, secrets, certificates, tokens and shared accounts are systematically rotated or withdrawn.
4. Critical responsibilities are updated in BCM, incident, risk and service owner registers.
5. Metrics show overdue withdrawals, role changes without recertification, open assets and external access after contract end.
6. Management receives trends on process gaps, technical debt and resource needs.

## Routine flow

1. **Record event:** role change, departure, project end, service provider end or special case.
2. **Classify risk:** assess role, access, data, privileges, conflict situation and criticality.
3. **Create tasks:** assign access, devices, physical access, handovers, responsibilities and communication.
4. **Implement:** adjust or withdraw rights, return assets, rotate secrets, transfer responsibility.
5. **Confirm:** technical and business owners confirm closure or justify open points.
6. **Manage exceptions:** time-limit, compensate and document them in a decision-ready way.
7. **Review:** check samples, legacy permissions and lessons learned.
8. **Escalate:** bring overdue high-risk tasks or conflicts to management.

## Decisions

- Which role changes require a full rights review?
- When must access be withdrawn immediately, on the last day or after handover?
- Which roles count as high-risk departures?
- Who may approve temporary residual access and for how long?
- Which secrets, tokens or shared access paths must be rotated?
- How is external access demonstrably ended after project or contract end?

## Evidence

### Strong evidence

- complete mover/leaver ticket with date, owners and status,
- IAM logs or tickets for withdrawal or adjustment of rights,
- review of existing permissions during role change,
- return of asset, badge or key,
- handover record for critical responsibilities,
- evidence of ended external access,
- exception decision with expiry date and management handoff where risk exists.

### Weak evidence

- HR departure notice without technical closure confirmation,
- checklist without system scope,
- manual email “everything done” without evidence,
- withdrawal of the main account, but no check of SaaS, tokens or groups,
- device overview without return or deletion status.

### Evidence gaps

- role changes without permission clean-up,
- external accounts active after contract end,
- admin rights or service access not checked,
- assets or data carriers unclear,
- critical responsibility without successor,
- exceptions without deadline or risk decision.

## Effectiveness review

Review questions:

- Are changes and departures triggered in time to all relevant owners?
- Is access adjusted or withdrawn on schedule?
- Are role changes used as clean-up events?
- Are external persons and service provider endings fully covered?
- Are assets, physical access and secrets considered?
- Is there evidence for handover of critical responsibilities?
- Are overdue high-risk cases escalated?

Possible metrics:

- time to access withdrawal after departure,
- role changes with completed rights review,
- open mover/leaver tasks,
- external accounts after contract end,
- overdue asset returns,
- exceptions and overdue residual access,
- findings from samples.

## BSIG/NIS2 connection point

Mover/leaver routines are compatible with NIS2-oriented governance, access protection, cyber hygiene, supply chain management, incident prevention and business continuity. The concrete connection should be assessed organisation-specifically in the requirements register, role model and management review.

This artefact does not replace legal review of employment, contract, data protection or reporting questions.

## Boundaries

- No complete HR offboarding or IAM tool design.
- No legal or data protection advice on departure, conflict cases or retention.
- No guarantee that a documented withdrawal covers all shadow access.
- No certification, conformity or security assurance.
- No ISO 27002 texts or real personal/organisational data.

## Handoffs

- **HR handoff:** employee changes, departure, timing, communication and special cases.
- **Access/IAM handoff:** accounts, groups, admin rights, SaaS, tokens, certificates and service accounts.
- **Asset/facility handoff:** devices, data carriers, keys, badges, physical access and return.
- **Business unit handoff:** knowledge transfer, process responsibility, open measures and data stores.
- **Supplier handoff:** external persons, project end, contract end and subcontractor access.
- **Legal/data protection handoff:** conflict cases, investigations, retention, personal data and communication.
- **Management handoff:** high-risk departures, overdue withdrawals, exceptions or resource gaps.

## Typical mistakes

- Only departures are considered, but role changes are not.
- The main account is disabled, but SaaS, tokens and external access remain active.
- Managers report changes too late.
- External project staff disappear from view as soon as the project ends.
- Knowledge and responsibility handover is not understood as a security task.
- Exceptions for residual access are not time-limited.
- Samples find legacy permissions, but the process is not improved.

## Fictional mini example

A fictional employee moves from support to sales. HR triggers a mover ticket. The support lead confirms that access to customer tickets is no longer needed, while sales access is newly requested. IT removes support groups, checks a shared reporting account and documents the change. The service owner takes over two open measures from the old role profile. A later sample shows that one SaaS access was forgotten; the mover process is expanded to include this service.

Evidence:

- mover ticket,
- rights review support/sales,
- IAM change evidence,
- handover of open measures,
- sample finding,
- process adjustment for the SaaS service.
