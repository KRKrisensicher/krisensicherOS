# A.7.2 — Physical access

## Purpose

Physical access controls who may enter buildings, rooms and security areas — and how permissions are requested, granted, reviewed, withdrawn and handled when anomalies occur. The decisive element is not the door system alone, but the traceable connection of role, need, approval, badge/key, visitor logic, review and withdrawal.

## Control objective in repository language

The organisation operates a routine for physical access to sites and protected areas. The routine connects HR events, Facility, asset owners, visitor management, service provider access, logging, incident reporting and management decisions.

## Typical risks

- If access rights remain active after departure or role change, former or unauthorised persons can enter protected areas.
- If keys, cards or codes are not issued and returned in a controlled way, non-traceable access arises.
- If visitors, suppliers or maintenance providers receive unsupervised access, information can be viewed, devices manipulated or operations disrupted.
- If access rights are granted broadly, physical access does not match actual work need.
- If logging or video is used without clarification, data protection and employee-related issues arise.

## Triggers

- Joining, role change, site change, project change or departure.
- New site, new security area, conversion or change of the locking/access system.
- Loss of badge, key, token or access code.
- Visit, maintenance, delivery, external company or emergency access.
- Security event, unauthorised access attempt, tailgating, suspicious observation or theft.
- Regular access review or site inspection.
- Supplier change, cleaning/security guard service change or contract end.

## Roles and responsibilities

- **Site / facility owner:** operates access system, key/badge management, visitor process and site rules.
- **HR / people function:** provides joining, role-change, site-change and departure events.
- **Manager / area owner:** confirms business need for access.
- **Asset owner / security area owner:** decides on access to critical rooms or areas.
- **ISMS owner / security role:** defines minimum logic, review requirements, risk connection and escalation.
- **Data protection / Legal:** review access logs, video, visitor lists, security guard and employee data.
- **Management:** decides on critical exceptions, investments, conflicts of objectives and residual risks.

## Implementation

### Minimum start

Goal: access to critical areas is traceably granted, reviewable and withdrawable.

1. Critical rooms and areas are named and connected with owners.
2. Access is granted only with traceable approval: person/role, area, reason, duration, approving role.
3. Keys, cards, codes or badges are managed in a simple issue and return list.
4. Departure, role change, loss and contract end trigger withdrawal or blocking.
5. Visitors and maintenance providers are registered and, where necessary, accompanied.
6. Exceptions and emergency accesses are documented and subsequently reviewed.

Minimum evidence:

- list of critical areas and owners,
- access requests or approvals,
- issue/return list for badges, keys or codes,
- visitor or maintenance evidence,
- withdrawal or blocking evidence,
- exception or incident tickets.

### Solid practice

Goal: physical access is role-based, event-driven and regularly reviewed.

1. Access groups are connected with roles, areas and protection need.
2. Joiner/mover/leaver events from HR are linked with facility processes.
3. Critical areas receive more frequent reviews than general office areas.
4. Visitor, supplier and maintenance processes define registration, identity check, accompaniment, permitted area and evidence.
5. Lost badges, keys or codes have a fast blocking and replacement process.
6. Access anomalies are handed over to Security, Facility or Incident Response.
7. Data protection and Legal review logging, video, retention and inspection rights.

### Advanced practice

Goal: access control is integrated into identity, facility, incident and risk management.

1. HR system, access system, visitor management and security area register are organisationally or technically connected.
2. Access reviews use role, area and risk information instead of pure name lists.
3. Anomalies such as repeated failed attempts, access outside usual times or unreturned badges are reviewed based on risk.
4. Service provider access is connected with contracts, service times, contacts and offboarding.
5. Management receives metrics on overdue withdrawals, open badges, critical exceptions and investment needs.

## Routine flow

1. **Access need arises:** new person, new role, visit, maintenance, project or emergency.
2. **Review area and protection need:** general site, security area or particularly critical room.
3. **Obtain approval:** manager, Facility or area/asset owner confirms need and duration.
4. **Issue access:** badge, key, code or visitor badge is documented and explained.
5. **Operate use:** visitors are accompanied, service providers controlled and anomalies reported.
6. **Process change:** role change, departure, loss or contract end leads to blocking, return or code change.
7. **Perform review:** owners review whether access is still necessary and appropriate.
8. **Handle deviations:** unclear rights, lost media, unreturned keys or anomalies are escalated.
9. **Improve:** findings lead to changed roles, processes, systems or training.

## Decisions

- Which areas require formal access approval and which do not?
- Who may approve access to critical areas?
- How long do visitor, service provider or project accesses remain valid?
- Which access events are logged and how is data protection clarified?
- When is accompaniment sufficient, and when is permanent access needed?
- Which exceptions or emergency accesses are tolerable and who reviews them?
- How are physical access rights linked with HR and contract end?

## Evidence

### Strong evidence

- current area and access group list with owners,
- approved access requests with reason and duration,
- issue, blocking and return evidence for badges, keys or codes,
- visitor and maintenance logs with accompaniment rule,
- review records with withdrawal or correction decisions,
- incident or anomaly tickets,
- data protection / Legal review for logging or video,
- management decision for permanent exceptions or investment need.

### Weak evidence

- key board or card list without owner and review date,
- general house rules without specific access approvals,
- access system export without role or area connection,
- visitor book without evaluation or escalation logic,
- verbal approvals for service provider access.

### Evidence gaps

- unreturned keys or badges without follow-up,
- access rights of former employees or service providers,
- critical areas without separate review,
- emergency access without log or follow-up check,
- access logs or video without data protection clarification,
- codes that are shared and no longer connected to individuals.

## Effectiveness review

Review questions:

- Can access rights to critical areas be assigned to a role, approval and duration?
- Are departures, role changes and contract ends processed promptly?
- Are visitors and maintenance providers registered traceably and accompanied appropriately?
- Does the access review lead to withdrawal or correction of unnecessary rights?
- Are lost badges, keys or codes blocked or replaced quickly?
- Are data protection questions for logging and video clarified?
- Are access anomalies treated as security events?

Possible metrics:

- overdue access reviews,
- open returns of badges or keys,
- time to blocking after departure or loss,
- number of critical exceptions or emergency accesses,
- findings from visitor and maintenance processes,
- access rights without clear owner or business need.

## BSIG/NIS2 connection point

Physical access is connectable to NIS2-oriented topics such as risk management, protection of critical operating environments, incident prevention, supplier management, business continuity and cyber hygiene. The specific connection to services, sites and evidence should be assessed organisation-specifically.

This artefact does not replace legal or data protection assessment of access logging, video surveillance, employee data or external reporting obligations.

## Boundaries

- This artefact is not a complete building security or locking-system concept.
- It does not replace a data protection review for access logs, visitor lists or video.
- It does not confirm conformity, certifiability or physical security merely through an access system.
- It contains no ISO 27002 texts and no real site, personal or access data.
- It is not sufficient if access is granted but not withdrawn or reviewed.

## Handoffs

- **HR handoff:** joining, role change, site change, departure, longer absence.
- **Facility handoff:** badge/key management, locking system, visitor process, site inspection.
- **Asset / area owner handoff:** approval and review for critical rooms and security areas.
- **Data protection / Legal handoff:** access logs, video, visitor lists, retention, inspection rights, security guard contracts.
- **Vendor handoff:** service provider, maintenance, cleaning or security guard access and contract end.
- **Incident handoff:** unauthorised access, lost badge, tailgating, manipulation or theft.
- **Management handoff:** investment need, permanently unsolved access gaps, accepted residual risks.
- **Audit / evidence handoff:** missing approvals, unclear access groups or non-traceable reviews.

## Typical mistakes

- Physical access is granted on joining but not cleaned up after role change or departure.
- Master keys or shared codes are used without clear responsibility and review.
- Service providers receive permanent access although only temporary assignments take place.
- Visitor processes exist at reception but not for side entrances or delivery routes.
- Access system exports are reviewed without understanding area or business need.
- Data protection is only considered after logging or video is already used in production.
- Emergency access remains active after the emergency.

## Fictional mini example

A fictional office site introduces separate access for the server room. The IT owner approves access only for two administrators and Facility for maintenance cases. During the quarterly review, it becomes apparent that a former service provider still has an active card. Facility blocks the card, documents the correction and adds the supplier offboarding check. In parallel, data protection reviews retention of the access logs.

Evidence:

- server room access group with owner,
- approvals for authorised roles,
- review record with finding,
- blocking evidence for service provider card,
- updated offboarding check,
- data protection review of log retention.
