# A.8.2 — Manage privileged rights

## Purpose

Privileged rights allow far-reaching changes to systems, data, identities and security functions. This routine ensures that such rights do not arise incidentally, but are specifically requested, justified, limited, monitored, reviewed and withdrawn when needed.

## Control objective in repository language

The organisation operates its own control process for privileged rights. Admin, root, superuser, cloud, database, security, network, CI/CD and emergency rights are managed with owner, purpose, approval, technical implementation, logging, review and exception handling.

## Typical risks

- If privileged rights are assigned permanently and broadly, a compromised account can cause major damage.
- If admin rights are not separated from everyday accounts, risk from phishing, malware or operating errors increases.
- If emergency or break-glass accounts are not reviewed, backdoors or undetected use remain possible.
- If service providers receive privileged access without limitation, control and accountability are missing.
- If logging or review are missing, misuse, misconfigurations and excessive rights are detected late.

## Triggers

- new admin need, new system, new platform, new cloud or SaaS administration.
- role change, onboarding, offboarding or end of a service provider engagement.
- security event, suspected account compromise or unusual admin activity.
- change to role model, permission groups, PAM/IAM tooling or emergency access.
- audit finding, vulnerability, penetration test or management question.
- periodic review of privileged rights.

## Roles and responsibilities

- **System / Service Owner:** confirms need, criticality and business justification.
- **IT / Platform Owner:** implements rights technically and provides logs or exports.
- **Security role / ISMS Owner:** defines minimum requirements, review frequency, escalation logic and exception handling.
- **Manager / Process Owner:** confirms role relevance and segregation of duties.
- **Supplier Management:** controls privileged access for external administrators.
- **Data Protection / Legal:** reviews personal logs, service provider and employee-related topics.
- **Management:** decides on permanent exceptions, missing segregation, lack of resources or accepted residual risk.

## Implementation

### Minimum start

Goal: make the most critical privileged rights visible and reviewable.

1. Critical admin rights are identified: identity platform, central servers, cloud, network, security tools, databases and core applications.
2. Each privileged account receives an owner, purpose, user/responsible person and validity.
3. New rights are granted only via request/ticket with business approval.
4. Admin rights are considered separately from everyday accounts and reviewed regularly at least for critical systems.
5. Offboarding, role changes and the end of service provider work trigger withdrawal or review.
6. Emergency accounts are inventoried and use is reviewed afterwards.

Minimum evidence:

- list of privileged accounts/groups in the critical scope,
- requests and approvals,
- review record with decisions,
- evidence of withdrawn rights,
- exception or break-glass documentation.

### Solid practice

Goal: privileged rights are limited, monitored and linked to risk decisions.

1. Privilege types are classified: permanent admin rights, time-limited rights, emergency rights, service/automation accounts, external admin access.
2. Strong authentication, role-based groups and separate accounts are used for critical activities.
3. Rights are reviewed according to least-privilege logic and segregation of duties, without blindly blocking operational capability.
4. Privileged activities are logged appropriately and triaged when anomalies occur.
5. External admin access is time-limited, contract-related and technically limited.
6. Exceptions receive an expiry date, compensating measure and risk decision.

Strong evidence:

- privilege register with type, owner, purpose and validity,
- role/group catalogue for admin rights,
- recertification records,
- evidence of MFA, separate accounts or PAM mechanisms,
- log review or unusual activity analysis,
- exception decisions with follow-up date.

### Advanced practice

Goal: privileged rights are controlled dynamically, verifiably and with detection capability.

1. Just-in-time or time-limited privileges replace permanent admin rights where useful.
2. PAM/IAM, ticketing, asset criticality and logging are connected.
3. Admin sessions for critical systems are recorded or controlled on a risk basis.
4. Risk indicators such as unusual times, new target systems or mass changes trigger triage.
5. Break-glass processes are tested and reviewed after use.
6. Management sees overdue reviews, permanent high-risk rights, external admin access and segregation conflicts that cannot be implemented.

## Routine flow

1. **Privilege need arises:** system operation, project, incident, service provider or emergency.
2. **Record request:** document person/account, target system, purpose, time period, scope of rights and risk.
3. **Review from business and technical perspective:** owner, task relevance, segregation conflict, alternatives and safeguards.
4. **Approve and implement:** limit, authenticate, log and document rights.
5. **Use and monitor:** review activities, deviations and emergency use.
6. **Perform review:** confirm, reduce, withdraw or escalate.
7. **Control exceptions:** time-limited, justified, with compensation and follow-up.
8. **Improve:** feed patterns back into role model, tooling, training or architecture.

## Decisions

- Which rights count as privileged and critical enough for special control?
- Which rights may be permanent, and which only time-limited?
- When are separate admin accounts, MFA, PAM or session control required?
- Who may use emergency accounts, and who reviews the use?
- Which segregation conflicts are unacceptable, and which need a management decision?
- How is external admin access limited and ended?

## Evidence

### Strong evidence

- current privilege register or group export with owners,
- approved requests with purpose and duration,
- technical evidence of implementation, MFA or separate accounts,
- review records with withdrawal/correction,
- log analyses or session evidence for critical activities,
- break-glass test or usage review,
- management decision for permanent exceptions.

### Weak evidence

- general admin policy without concrete rights overview,
- screenshot of an admin group without owner or review date,
- tool claim “PAM in place” without use and review,
- logs without analysis,
- generic service provider accounts without contractual or personal reference.

### Evidence gaps

- privileged accounts without an assignable responsible person,
- former employees or service providers with admin rights,
- break-glass accounts without test and usage review,
- service accounts with excessive rights,
- exceptions without expiry date or risk decision.

## Effectiveness review

Review questions:

- Are privileged rights for critical systems fully visible?
- Can it be explained why an admin right exists and who approved it?
- Are role changes, offboarding and the end of service provider work processed promptly?
- Are emergency and external admin accesses reviewed separately?
- Do reviews lead to actual withdrawal or reduction?
- Are unusual admin activities triaged and escalated?

Possible metrics:

- number of privileged accounts per critical system,
- overdue privilege reviews,
- permanent high-risk rights,
- external admin access without expiry date,
- break-glass uses and reviews,
- withdrawn or reduced rights per review.

## BSIG/NIS2 connection point

Control of privileged rights is compatible with NIS2-oriented topics such as access protection, cyber hygiene, incident prevention, secure administration, service provider control and risk management. The concrete connection should be assessed in the requirements register, access concept and management review.

This artefact does not replace legal review or data protection assessment of logging or employee data.

## Boundaries

- This artefact is not a complete IAM or PAM design.
- It does not replace technical architecture review or data protection review for logging.
- It does not promise certification readiness or legal fulfilment.
- It contains no confidential admin lists or production system details.
- A PAM tool alone is not an effective governance routine.

## Handoffs

- **Access / IAM handoff:** role model, joiner-mover-leaver, groups and technical accounts.
- **Incident handoff:** compromised account, suspicious admin activity or emergency use.
- **Supplier handoff:** external admin rights, contract end, managed service access.
- **Data protection / Legal handoff:** personal logs, session recording, employment-law questions.
- **Change / Operations handoff:** privileged changes to critical systems.
- **Management handoff:** segregation of duties that cannot be implemented, permanent exceptions, resource needs.
- **Audit / Evidence handoff:** missing owners, incomplete reviews or unclear break-glass use.

## Typical mistakes

- Admin rights are hidden in the general access review.
- Everyday accounts and admin roles are not separated.
- Emergency accounts exist but are never tested or reviewed.
- Service provider access remains active after project end.
- Logging is enabled, but nobody reviews anomalies.
- Exceptions for legacy systems become permanent and invisible.
- Service accounts are forgotten even though they have high privileges.

## Fictional mini example

A fictional SaaS team reviews its cloud administrators. The export shows eight owner rights, two of them for former project roles and one permanent service provider account. The Service Owner confirms only five active needs. Two rights are withdrawn, and the service provider account is converted to time-limited access. A test and monthly usage review are introduced for one break-glass account.

Evidence:

- cloud admin export,
- review decision by the Service Owner,
- tickets for rights withdrawal,
- new approval for service provider access,
- break-glass test record,
- management review item on permanent privilege reduction.
