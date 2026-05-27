# A.5.15 — Access control as a governance routine

## Purpose

Access control ensures that people, services, and technical identities receive only the access they need for legitimate tasks — and that this access is requested, approved, changed, reviewed, and revoked in a traceable way.

The core is not “authorization list exists,” but a robust decision and review process: Who may access what, why, for how long, with which approval, and with which risk?

## Control objective in repository language

The organization operates a traceable routine for access to information, applications, systems, rooms, interfaces, and administrative functions. The routine connects roles, protection needs, business need, approval, technical implementation, review, and exception handling.

## Typical risks

- If former employees, service providers, or technical accounts remain active, information can be viewed, changed, or deleted without authorization.
- If permissions grow across role changes, unnoticed concentrations of power and segregation conflicts arise.
- If business units grant access informally, approval, traceability, and revocation are missing.
- If privileged rights are not considered separately, a single compromised account can cause significant damage.
- If access concepts exist only for central systems, cloud services, SaaS tools, data repositories, interfaces, or service accounts remain unmanaged.

## Triggers

- Onboarding, role change, team change, or exit.
- New system, new data repository, new cloud service, or new interface.
- Change in protection need, new risk decision, or new regulatory relevance.
- Supplier change, end of contract, or changed service provider access.
- Security event, suspected account compromise, or audit finding.
- Periodic access review.
- Introduction or change of role models, groups, admin rights, or technical accounts.

## Roles and responsibilities

- **Information Owner / Asset Owner:** defines who needs access from a business perspective and which restrictions apply.
- **Manager / Process Owner:** confirms business need and role connection.
- **IT/Platform Owner:** implements permissions technically and provides evaluations.
- **ISMS Owner / Security role:** defines minimum logic, review requirements, risk handling, and escalation.
- **HR / People function:** provides onboarding, change, and exit events.
- **Data Protection / Legal:** reviews personal evaluations, employee data, logging, and contractual questions.
- **Management:** decides on exceptions, residual risks, resources, and trade-offs.

## Implementation

### Minimum start

Goal: Make critical access visible and reviewable.

1. The organization names the most important systems, data repositories, and admin access in the ISMS scope.
2. An owner is defined for each critical target.
3. New access is granted only with a traceable request or ticket.
4. Exits and role changes trigger an access review.
5. A simple quarterly review checks at least privileged and external access.
6. Exceptions are documented with rationale, duration, and follow-up date.

Minimum evidence:

- system/data repository list with owner,
- ticket or approval evidence for access,
- exit/role-change review,
- review protocol for critical access,
- exception decision.

### Solid practice

Goal: Repeatable access control across roles and risks.

1. Access types are classified: standard access, elevated access, privileged access, external access, technical account.
2. Role models or authorization groups are described and connected with owners.
3. Approvals follow clear logic: business approval, technical implementation, security review for increased risk.
4. Access reviews are planned on a risk basis: critical systems more often, lower protection needs less often.
5. Recertification results lead to revocation, correction, exception, or management decision.
6. Joiner/mover/leaver processes are connected with HR or identity data.

Strong evidence:

- role/group catalog,
- approved access requests,
- technical authorization exports,
- review list with decisions,
- evidence of revoked or corrected access,
- exception and risk acceptance log.

### Advanced practice

Goal: Operate access as an ongoing governance and detection routine.

1. Identity source, role model, system groups, and recertification are integrated.
2. Critical rights are monitored with segregation-of-duties rules, risk indicators, or alerts.
3. Just-in-time or time-limited privileges are used for particularly critical activities.
4. Service accounts, API tokens, and machine identities are maintained with owner, purpose, rotation, and expiry date.
5. Unusual access patterns feed into monitoring, incident triage, and risk review.
6. Management receives decision-ready metrics: overdue reviews, exception rate, critical legacy permissions, external access, unassigned accounts.

## Routine flow

1. **Access need arises:** new role, task, service provider, system function, or exception.
2. **Record request:** who, to what, why, for how long, with which role/risk connection.
3. **Make business decision:** owner checks business need and protection need.
4. **Check security logic:** elevated rights, external access, segregation conflicts, or personal evaluations are considered separately.
5. **Implement technically:** IT implements permission according to approval.
6. **File evidence:** request, decision, and implementation remain traceable.
7. **Perform review:** owner confirms, revokes, corrects, or escalates.
8. **Steer exceptions:** time-limited, justified, risk-assessed, with follow-up date.
9. **Improve:** findings and patterns feed back into role model, process, or tooling.

## Decisions

- Which systems and data repositories are critical enough for the start?
- Which access requires business approval, security approval, or management decision?
- How often are which access types reviewed?
- Which exceptions are tolerable and which are not?
- How are external access, admin rights, and technical accounts prioritized?
- Which trade-offs exist between rapid ability to work and restrictive permission assignment?

## Evidence

### Strong evidence

- current asset/system scope with owners,
- access requests with rationale and approval,
- authorization exports or system evidence at review time,
- review protocols with decision per conspicuous access,
- evidence of revoked rights,
- documented exceptions with expiry date,
- management decision for accepted residual risks.

### Weak evidence

- general access policy without concrete execution,
- screenshot of individual groups without owner or review date,
- incomplete lists without system scope,
- “handled by IT” without evidence of the decision,
- old role matrix without recertification.

### Evidence gaps

- no connection between HR events and access revocation,
- external accounts without contract or owner connection,
- technical accounts without responsible person,
- admin rights without separate review,
- permanent exceptions without risk acceptance.

## Effectiveness review

Review questions:

- Can it be traced for a critical system who has access and why?
- Are role changes and exits processed within defined deadlines?
- Is there evidence that reviews led to corrections?
- Are privileged, external, and technical access considered specifically?
- Are exceptions time-limited and documented in a decision-ready way?
- Does management recognize where resource or objective conflicts exist?

Possible metrics:

- share of critical systems with current owner,
- overdue access reviews,
- number of critical legacy permissions,
- time to revocation after exit,
- exception rate and overdue exceptions,
- unassigned accounts.

## BSIG/NIS2 connection point

Access control is a central connection point to NIS2-oriented risk management measures, especially cyber hygiene, access protection, handling of critical systems, incident prevention, and information security governance.

For BSIG/NIS2 applicability, the organization should assess in the requirements register which services, systems, roles, and evidence are relevant. This artifact does not replace legal interpretation and does not provide a binding assessment of applicability.

## Boundaries

- This artifact is not an identity and access management tool design.
- It does not replace data protection review for employee evaluations, logging, or monitoring.
- It makes no binding statement on legal obligations.
- It contains no ISO 27002 text or certification commitment.
- It must not be treated as sufficient evidence if actual access practice remains unchecked.

## Handoffs

- **HR handoff:** onboarding, role change, exit, longer absence, or function change.
- **Data Protection handoff:** personal access evaluations, monitoring, risk of behavior or performance control.
- **Legal/Procurement handoff:** external access, service providers, contract end, access obligations in agreements.
- **Incident handoff:** suspected compromised account, unauthorized use, unexplained permission.
- **Management handoff:** permanent exceptions, resource conflicts, segregation that cannot be implemented, accepted residual risks.
- **Audit/Evidence handoff:** missing review evidence or incomplete system scope.

## Typical mistakes

- Access is granted cleanly at onboarding, but not cleaned up during role changes.
- Admin rights are treated like normal user rights.
- Access reviews are sent out, but decisions are not tracked.
- Business units approve all existing rights in bulk because the list is incomprehensible.
- Service accounts and API tokens are missing from the review.
- Exceptions become permanent because no expiry date was set.
- The organization confuses an IAM tool with functioning governance.

## Fictional mini example

A fictional mid-sized company operates a customer portal. During the review, it becomes apparent that three former project members still have access to the administration group. The IT Owner creates an authorization export, the Product Owner confirms the missing business need, IT revokes the rights and documents the change in the ticket. In the management review, it is decided that admin rights will be reviewed monthly and normal business access quarterly in the future.

Evidence:

- export of the admin group at review time,
- Product Owner decision,
- ticket with rights revocation,
- updated review frequency,
- management decision on prioritization.
