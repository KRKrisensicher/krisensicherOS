# A.7.3 — Protecting rooms and buildings

## Purpose

Rooms and buildings protect information, systems, and operational capability not only through doors, locks, or reception areas. What matters is an operated routine that brings together protection needs, site usage, access, structural weaknesses, visitor routes, and responsibilities.

The core idea is: critical areas should not be protected by chance, but planned, operated, reviewed, and adjusted when changes occur in a traceable way.

## Control objective in repository language

The organization operates a site-related protection routine for buildings, floors, rooms, and zones in which information, IT systems, media containing information, or critical processes must be protected. The routine connects site scope, owners, protection needs, access logic, structural or organizational measures, review, and exception handling.

## Typical risks

- If server, technical, archive, or storage areas are not clearly separated, unauthorized persons may reach sensitive information or systems.
- If reception, visitor, and delivery routes are not controlled, unobserved movement in areas requiring protection may occur.
- If moves, conversions, or space changes take place without security review, old protective measures may no longer fit the new use.
- If keys, cards, or room permissions are not reviewed regularly, old or excessive access rights remain active.
- If building risks are not connected with information values, investments in protective measures are decided arbitrarily or too late.

## Triggers

- New site, move, conversion, area change, or change of room use.
- New critical systems, archives, laboratory, production, or operational areas.
- Change in protection needs, data classes, customer requirements, or process criticality.
- Security event, break-in, loss, unaccompanied visitor, or suspicious access attempt.
- Change of facility provider, landlord, security service, or cleaning service.
- Regular site or room review.
- Audit finding, risk analysis, BCM review, or management decision.

## Roles and responsibilities

- **Site / Facility Owner:** responsible for building and room logic, structural measures, key/card processes, and service provider coordination.
- **Asset Owner / Process Owner:** states the protection needs of information, systems, and processes in the room.
- **ISMS Owner / Security role:** defines the minimum logic for zones, reviews, exceptions, and risk handling.
- **IT / Platform Owner:** assesses technical rooms, network areas, racks, media storage, and operational dependencies.
- **Reception / Office Management:** operates visitor, supplier, and day-access processes.
- **Procurement / Vendor Management:** involves facility, security, maintenance, and cleaning service providers.
- **Management:** decides on investments, residual risks, site compromises, and permanent exceptions.

## Implementation

### Minimum start

Goal: make critical rooms and building areas visible, assigned, and reviewable.

1. The organization identifies sites and rooms in ISMS scope that have increased protection relevance.
2. A functional owner and a facility contact are defined for each critical area.
3. Groups authorized for access are documented at a coarse level: employees, service providers, visitors, emergency access.
4. Visitor and delivery routes are described so that areas requiring protection are not unintentionally left exposed.
5. A simple review checks at least annually or when changes occur whether room, use, and protective measures fit together.
6. Deviations are documented as a measure, exception, or management decision.

Minimum evidence:

- site/room list with owners,
- zone or room sketch at an appropriate level of detail,
- list of authorized roles or groups,
- review note with findings,
- exception or measure decision.

### Solid practice

Goal: building protection is risk-based, repeatable, and connected with access control.

1. Rooms are grouped by protection need: public areas, office space, internal areas, protected technical or archive areas.
2. Access rules, escort requirements, visitor registration, and service provider access are described per zone.
3. Keys, cards, codes, or mechanical permissions are managed with issue, return, loss reporting, and review.
4. Conversions, new use, or new critical assets trigger a security review.
5. Regular walkthroughs check doors, signage, storage, visitor routes, and technical protective measures.
6. Findings lead to measures with owner, deadline, and priority.
7. Residual risks and investment needs are fed into ISMS or management review.

### Advanced practice

Goal: building protection is integrated into site planning, BCM, access systems, and situational awareness.

1. Site and room data are connected with asset inventory, process criticality, and access control.
2. Critical areas have documented protection concepts with zones, responsibilities, escalation paths, and emergency access.
3. Access events, disruptions, and facility findings flow into security, BCM, and risk reviews.
4. Site decisions take account of security, availability, supply chain, and environmental aspects.
5. Service provider access is connected with contractual logic, identity checks, escorting, and review.
6. Management receives decision-ready information on site residual risks, investment needs, and recurring findings.

## Routine flow

1. **Protection need emerges or changes:** site, room, asset, process, or service provider access changes.
2. **Clarify scope:** determine affected rooms, information, systems, processes, and people.
3. **Assess protection need:** classify criticality, exposure, visitor/service provider contact, and existing measures.
4. **Define zones and rules:** define access, escorting, keys/cards, visitor routes, and exceptions.
5. **Implement:** Facility, IT, Office Management, and affected owners implement measures.
6. **File evidence:** document room list, permission, walkthrough, finding, or decision.
7. **Perform review:** walkthrough, permission reconciliation, service provider review, or site review.
8. **Control deviations:** measure, time-limited exception, or management handoff.
9. **Improve:** feed findings back into construction planning, access process, service provider management, or BCM.

## Decisions

- Which rooms are considered to require protection and why?
- Which zones need escorting, separate authorization, or technical protection?
- Who may approve permanent room or access exceptions?
- Which structural gaps are accepted, compensated, or resolved through investment?
- How are shared buildings, co-working spaces, or landlord dependencies handled?
- Which site residual risks must enter management review?

## Evidence

### Strong evidence

- current site and room scope with owners,
- zone model or room classification,
- access/visitor/service provider process,
- key, card, or permission review,
- walkthrough record with measure status,
- evidence of resolved structural or organizational findings,
- management decision on residual risks or investments.

### Weak evidence

- general building rule without room or protection-need reference,
- outdated room plans without owners,
- key list without return or review date,
- blanket statement “access only for authorized persons” without process evidence,
- walkthrough photos without assessment or measure.

### Evidence gaps

- critical rooms without a named owner,
- service provider access without escort or approval logic,
- conversions without security review,
- lost keys or cards without documented response,
- permanent building gaps without risk decision.

## Effectiveness review

Review questions:

- Are critical rooms and building areas known and assigned to an owner?
- Do access rules fit actual use and protection needs?
- Are moves, conversions, and changes of use reviewed from a security perspective?
- Do walkthroughs lead to traceable measures?
- Are visitor, supplier, and service provider routes practically controllable?
- Are accepted structural residual risks documented in a decision-ready way?

Possible metrics:

- share of critical rooms with current owner,
- open findings from site walkthroughs,
- overdue access/key reviews,
- number of time-limited exceptions,
- time to respond to card/key loss,
- management items on site residual risks.

## BSIG/NIS2 connection point

Protection of rooms and buildings is a connection point for NIS2-oriented risk management measures, physical resilience, protection of critical services, business continuity, and supplier management. Affected organizations should assess in the requirements register which sites, evidence, and management decisions are relevant.

This artifact makes no legal statement on applicability and does not replace legal review or building law, occupational safety, data protection, or insurance-related assessment.

## Boundaries

- This artifact is not a complete building security concept and not construction planning.
- It does not replace legal, insurance-related, or occupational safety assessment.
- It does not guarantee protection against burglary, sabotage, or outage.
- It contains no ISO 27002 text and no certification promise.
- Public examples remain fictional and without sensitive site details.

## Handoffs

- **Facility handoff:** structural measures, keys/cards, doors, zones, maintenance, landlord coordination.
- **IT handoff:** technical rooms, racks, network areas, media storage, emergency access.
- **Procurement / Vendor handoff:** cleaning, security, maintenance, reception, or facility service providers.
- **BCM handoff:** site outage, alternative space, critical operating rooms, emergency access.
- **Data protection / Legal handoff:** visitor logs, ID data, video or access data, contract questions.
- **Management handoff:** investment needs, structural gaps that cannot be resolved, site residual risks.
- **Audit / Evidence handoff:** missing room list, missing reviews, or non-traceable exceptions.

## Typical mistakes

- Buildings are treated as a facility topic without connection to information values.
- Room plans are current, but protection needs and owners are missing.
- Keys or cards are issued but not reviewed regularly.
- Visitor processes work at reception, but not at side entrances, deliveries, or maintenance.
- Conversions change protection boundaries without involving ISMS or IT.
- Structural weaknesses remain known but without decision or compensation.

## Fictional mini example

A fictional software service provider moves into a new office floor. During the site review, it is found that a network cabinet is located in a generally accessible copy room. Facility and IT designate the area as a protected technical room, move printer use to another room, and restrict access to IT and Facility. Until structural adjustment is complete, a time-limited compensating measure with weekly visual inspection is documented.

Evidence:

- updated room list with owner,
- decision on room classification,
- ticket for access change,
- time-limited compensating measure,
- review note after structural adjustment.
