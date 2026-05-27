# A.7.1 — Physical security areas

## Purpose

Physical security areas ensure that rooms, zones and sites with particular protection needs are not treated like normal office space. The aim is a traceable separation: where critical information, systems or operational processes are located, who is responsible, which protection logic applies and how it is reviewed.

## Control objective in repository language

The organisation operates a routine for classifying, separating, assigning responsibility for, documenting and reviewing physical areas according to protection needs. The routine connects site, asset criticality, access, visitor management, facility processes, incident reporting, BCM and management decisions.

## Typical risks

- If server rooms, archives, control rooms or technical areas are not clearly separated, unauthorised persons may view information, manipulate devices or cause operational disruptions.
- If protected areas are not connected with asset and process criticality, critical rooms may be protected too weakly or unimportant areas with too much effort.
- If structural, organisational and technical measures do not fit together, gaps arise despite existing doors, cards or cameras.
- If moves, conversions or new usage concepts are not reviewed, protection needs change unnoticed.
- If Facility and ISMS work separately, evidence, reviews and decisions on residual risks are missing.

## Triggers

- New site, move, conversion, area change or change of use.
- Establishment or change of server room, archive, laboratory, control room, warehouse, network technology area or crisis room.
- New critical assets, higher protection need or changed operational dependency.
- Security event, access anomaly, suspected manipulation or facility finding.
- Change of landlord, building service provider, security guard service or maintenance provider.
- BCM review, risk analysis, internal audit or management decision.
- Regular site or security area review.

## Roles and responsibilities

- **Site / facility owner:** is responsible for areas, structural measures, service provider coordination and site evidence.
- **Asset owner / service owner:** names critical systems, information and processes in the area.
- **ISMS owner / security role:** defines protection logic, review requirements, risk connection and escalation.
- **IT / operations role:** assesses technical rooms, network infrastructure, servers, media and operational dependencies.
- **Managers / area owners:** ensure everyday usability and implementation of rules.
- **Data protection / Legal:** review video, access logs, rental/service provider issues and personal data.
- **Management:** decides on investments, residual risks, exceptions and site priorities.

## Implementation

### Minimum start

Goal: critical physical areas are known, assigned to an owner and provided with minimum protection.

1. The organisation lists physical areas in the ISMS scope in which critical information, systems or processes are located.
2. For each area, an owner is named and the purpose is described.
3. Minimum rules are defined: who may enter, how visitors are accompanied, how doors/cabinets are secured and how anomalies are reported.
4. The connection to the asset list, risk analysis or BCM priority is documented.
5. Exceptions or structural weaknesses are managed with a risk decision and follow-up date.
6. At least annually or upon change, the organisation reviews whether area, protection need and use still fit together.

Minimum evidence:

- list of physical security areas with owners,
- area description with protection need,
- simple access and visitor rule,
- site or review record,
- measure or exception log.

### Solid practice

Goal: protected areas are managed consistently across sites and based on risk.

1. Areas are classified according to protection need or criticality without building unnecessary complexity.
2. Protection measures are documented for each area: structural separation, access control, visitor accompaniment, locking concept, environmental and operational risks, reporting paths.
3. Facility, IT, security and BCM reviews are aligned with each other.
4. Changes to areas, use, service providers or critical assets trigger a security area review.
5. Findings from inspections, incidents or maintenance are tracked as measures with owner and deadline.
6. Data protection and Legal are involved when logging, video, security guard services or landlord access are affected.

### Advanced practice

Goal: physical security areas are integrated into risk, BCM, access and facility management.

1. Area inventory, asset inventory, access groups, maintenance plans and risk register are connected.
2. Critical areas receive risk-based review frequencies and scenario assessments: outage, sabotage, water damage, fire, power, unauthorised access.
3. Access events, facility findings and maintenance activities are regularly reviewed for patterns.
4. Construction and move projects include an early security/BCM check.
5. Management receives decision-ready information on site gaps, investment needs, critical exceptions and operational dependencies.

## Routine flow

1. **Identify area:** site, room or zone contains critical assets, information or operational processes.
2. **Classify protection need:** asset owner, Facility and ISMS assess criticality, threats and dependencies.
3. **Separate area:** physical boundary, responsible persons, permitted roles and visitor logic are described.
4. **Define measures:** access, accompaniment, locking, labelling, maintenance, monitoring and reporting path are defined appropriately.
5. **Record evidence:** area inventory, sketch or description, owner, risks, measures and exceptions are filed.
6. **Review operation:** inspection, review, access check or facility check assesses the condition.
7. **Handle deviations:** structural gaps, changes of use or unclear access are tracked as measures.
8. **Escalate:** unacceptable residual risks, investments or site decisions go to Management Review.

## Decisions

- Which rooms or zones are physical security areas?
- Which protection level is appropriate for which area?
- Who may enter regularly, who only when accompanied and who not at all?
- Which structural or organisational gaps are accepted, compensated or remediated as a priority?
- How are landlords, cleaning, maintenance and external service providers involved?
- Which site or BCM risks require a management decision?

## Evidence

### Strong evidence

- current register of physical security areas with owners,
- protection-need or criticality connection per area,
- documented access and visitor logic,
- inspection or review records with findings,
- measure log with owner, deadline and status,
- risk or exception decision for structural gaps,
- management decision on investments or residual risks.

### Weak evidence

- building plan without protection need or owner,
- general house rules without critical areas,
- door lock or card as evidence without review logic,
- outdated room list after move or conversion,
- blanket statement “Facility takes care of it” without ISMS connection.

### Evidence gaps

- server, technical or archive rooms without owner,
- visitor or maintenance access not regulated,
- no connection to asset criticality or BCM,
- structural weaknesses without risk decision,
- no reviews after move, conversion or change of use,
- personal access or video data without clarification.

## Effectiveness review

Review questions:

- Are all critical physical areas in scope known and assigned to an owner?
- Does the protected area fit the criticality of the assets and processes it contains?
- Are visitors, maintenance and external service providers regulated traceably?
- Have inspections or reviews led to measures?
- Are conversions, moves and changes of use reviewed early?
- Are exceptions time-limited and provided with a risk decision?
- Does management recognise site gaps and investment needs?

Possible metrics:

- share of critical areas with current review,
- open findings from site inspections,
- overdue measures for structural or organisational gaps,
- number of unregulated service provider accesses,
- exceptions per site or area,
- time to review after conversion or change of use.

## BSIG/NIS2 connection point

Physical security areas are connectable to NIS2-oriented topics such as protection of critical operating environments, risk management, business continuity, supplier management and incident prevention. The specific connection to services, sites and evidence should be assessed organisation-specifically in the requirements register and in risk analyses.

This artefact does not replace building-law, occupational-safety, data-protection or other legal assessment.

## Boundaries

- This artefact is not a structural security concept and not a planning specification for building technology.
- It does not replace a data protection review for video, access logs or security guard services.
- It does not confirm conformity, certifiability or physical security merely through area definitions.
- It contains no ISO 27002 texts and no real site plans or confidential building data.
- It is not sufficient if protected areas are defined but not operated or reviewed.

## Handoffs

- **Facility handoff:** structural separation, locking systems, maintenance, service provider coordination, site inspection.
- **Asset / IT handoff:** critical systems, network technology, server rooms, technical operational dependencies.
- **BCM handoff:** outage of rooms, alternate sites, emergency operation, site resilience.
- **Data protection / Legal handoff:** video, access logs, security guard services, landlord rights, personal data.
- **Incident handoff:** suspected manipulation, unauthorised access, theft, sabotage or suspicious observation.
- **Management handoff:** investment need, site residual risks, permanent exceptions or strategic site decision.
- **Audit / evidence handoff:** missing area list, unclear owners, non-traceable reviews.

## Typical mistakes

- Physical security is treated only as a facility topic and not connected with information risks.
- Server rooms, archives or technical areas are known but not managed as protected areas.
- Visitor and maintenance access is regulated informally.
- After conversions, the old protected-area logic remains in place.
- Video or access logs are used without triggering a data protection handoff.
- Findings from inspections are not tracked as measures.
- Management sees costs, but not the associated operational risks.

## Fictional mini example

A fictional manufacturing company sets up a new network technology room. The IT owner reports the room to the ISMS, Facility adds it to the area register and defines access only for IT, Facility and accompanied maintenance providers. During an inspection, it becomes apparent that cleaning staff would have unsupervised access. Facility changes the cleaning schedule, and management approves a retrofit to the locking system.

Evidence:

- area register with owner and purpose,
- protection-need connection to network infrastructure,
- documented access and visitor rule,
- inspection finding,
- measure for the cleaning process,
- management decision on retrofit.
