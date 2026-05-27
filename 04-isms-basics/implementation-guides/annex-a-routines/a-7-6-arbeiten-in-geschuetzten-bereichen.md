# A.7.6 — Working in protected areas

## Purpose

Protected areas lose their value when work in them is unplanned, unsupervised or carried out without clear rules. This routine ensures that activities in server rooms, archives, technical areas, laboratories, security zones or other areas requiring protection are prepared, performed, documented and followed up in a controlled way.

## Control objective in repository language

The organisation operates a work routine for protected areas that connects access authorisation, work order, escorting, rules of conduct, brought-in devices, evidence management, exception handling and handoffs to Facility, IT, Data Protection, Incident Response and Management.

## Typical risks

- If maintenance, cleaning or deliveries in protected areas take place without work order and escorting, systems, information or data media may be unintentionally put at risk.
- If work is not documented, later disruptions, tampering or losses cannot be traced.
- If tools, mobile devices or cameras are brought in without control, risks of leakage, tampering or mix-ups arise.
- If emergency access is used informally, protection rules are bypassed in everyday operations.
- If rules of conduct are not explained by role, employees and service providers make unsafe ad-hoc decisions on site.

## Triggers

- Planned access to server room, technical area, archive, laboratory, security zone or other protected area.
- Maintenance, cleaning, repair, delivery, inventory, conversion, audit walkthrough or emergency measure.
- New service provider, new activity or changed work instruction.
- Disruption, alarm, unaccompanied access, missing documentation or suspected rule violation.
- Change in protection need, room classification or access authorisation.
- Regular review of work rules, visitor/service provider access or access logs.

## Roles and responsibilities

- **Area / Room Owner:** decides which work is permitted and which rules apply in the area.
- **Requester / Service Owner:** describes purpose, period, scope and expected result of the work.
- **Facility / Office Management:** coordinates access, escorting, keys/cards and external service providers.
- **IT / Platform Owner:** assesses technical risks for work on infrastructure, racks, cabling or systems.
- **ISMS Owner / Security role:** defines minimum requirements, exception handling, review and escalation.
- **Service providers / Visitors:** work only within the approved scope and report deviations immediately.
- **Management:** decides on permanent exceptions, resource gaps or unacceptable operational risks.

## Implementation

### Minimum start

Goal: work in critical areas is commissioned, escorted and traceable.

1. Protected areas are identified and assigned to an owner.
2. Planned work has a simple work order: who, when, where, why, with which escorting.
3. External persons receive access only for a limited time and limited purpose.
4. Basic rules are communicated before access: no uncommissioned work, no photos, no open doors, no lone work without approval, report anomalies.
5. Access and completion are documented.
6. Deviations, damage or unexpected findings are treated as an incident, facility item or measure.

Minimum evidence:

- List of protected areas with owner,
- work order or visitor ticket,
- access/escort evidence,
- short work or completion note,
- deviation or measures log for problems.

### Solid practice

Goal: work is prepared, controlled and followed up in a risk-based way.

1. Types of work are classified: routine maintenance, cleaning, repair, installation, audit, emergency access.
2. For each work type, approvals, escorting, permitted devices, photo rules, bringing in/removing material and documentation are defined.
3. Service providers receive clear security requirements contractually or operationally.
4. Work on critical technology is connected with change, maintenance or emergency processes.
5. Access logs and work evidence are regularly checked by sample against work orders.
6. Recurring deviations lead to training, service provider discussion, process change or management handoff.
7. Emergency access is reviewed afterwards.

Strong evidence:

- Area and work-type matrix,
- approved work orders,
- visitor/service provider and escort evidence,
- change or maintenance tickets,
- completion/acceptance records,
- sample review of access against work order,
- measures from deviations.

### Advanced practice

Goal: work in protected areas is integrated with access, change, service provider management and incident capability.

1. Access permissions, work orders and change windows are reconciled in advance.
2. Critical activities use dual control, temporary permissions or documented approval by area and service owners.
3. Materials, data media and devices are handled traceably when brought in or removed.
4. Service provider performance, deviations and repeated errors flow into vendor reviews.
5. Emergency work is concluded with subsequent review, evidence and risk decision.
6. Metrics show unauthorised access, retrospective emergency access, missing completion notes and recurring findings.

## Routine flow

1. **Work need emerges:** maintenance, repair, delivery, audit, cleaning, emergency or change.
2. **Record work order:** area, purpose, persons, period, activity, devices/material, escort need.
3. **Check risk:** protection need, critical systems, data media, personal data, operational interruption.
4. **Approve:** area owner, service owner, Facility or Change Owner confirms the work frame.
5. **Control access:** check identity, organise escort, communicate rules, log access.
6. **Perform work:** only approved activity, report deviations immediately.
7. **Document completion:** result, anomalies, material movements, open items.
8. **Follow up:** close access, remove temporary rights, handle deviations, file review.
9. **Improve:** feed patterns from findings back into work rules, contracts, training or room concept.

## Decisions

- Which areas are considered protected and which work rules apply there?
- Which activities require escorting, dual control or change approval?
- Which devices, photos, data media or materials may be brought in or removed?
- When may emergency access temporarily override rules and who reviews this afterwards?
- Which service providers may work independently and which may not?
- Which deviations are an incident, contract problem or management topic?

## Evidence

### Strong evidence

- Current scope of protected areas with owner,
- work order with purpose, period, persons and approval,
- access, visitor or escort log,
- change/maintenance/acceptance ticket,
- evidence that temporary permissions were removed,
- deviation or incident documentation,
- review of emergency access and recurring findings.

### Weak evidence

- General house rules without area-specific work rules,
- visitor list without reference to the work order,
- service provider contract without operational evidence,
- access log without completion note,
- verbal approvals for critical activities.

### Evidence gaps

- Work in protected areas without work order,
- external persons without escort or identity evidence,
- emergency access without subsequent review,
- open doors, brought-in devices or photos without rule,
- temporary permissions remain active,
- damage or anomalies are not followed up.

## Effectiveness review

Review questions:

- Can samples show why a person worked in a protected area?
- Do work order, access time and completion note fit together?
- Are external persons appropriately escorted and briefed?
- Is emergency access rare, justified and reviewed afterwards?
- Are deviations treated as measures, incidents or service provider topics?
- Are temporary permissions and keys/cards removed or returned after completion?

Possible metrics:

- Work without complete work order,
- missing completion notes,
- retrospective emergency access,
- deviations by service provider or area,
- overdue temporary access rights,
- findings from sample reviews.

## BSIG/NIS2 connection point

Working in protected areas is a connection point for NIS2-oriented risk management measures, protection of critical operating environments, supplier management, incident prevention and business continuity. The concrete connection should be assessed in the requirements register, in site and service provider risks and in BCM reviews.

This artefact does not replace legal, data protection, labour, contract or occupational safety review.

## Boundaries

- This artefact is not a complete work, construction, maintenance or occupational safety instruction.
- It does not replace contract review for service providers or data protection assessment for logging.
- It does not guarantee freedom from tampering or sabotage.
- It contains no ISO 27002 text or certification promise.
- Public examples remain fictional and without real site details.

## Handoffs

- **Facility handoff:** access, escorting, keys/cards, cleaning, maintenance, structural work.
- **IT / Change handoff:** work on racks, network, servers, cabling, power, cooling or production infrastructure.
- **Procurement / Vendor handoff:** service provider rules, contract requirements, repeated deviations, performance review.
- **Incident handoff:** unauthorised access, suspected tampering, loss, damage, uncommissioned activity.
- **Data protection / Legal handoff:** visitor/access logs, employee data, photos, contract or liability questions.
- **BCM handoff:** work endangers critical services or requires emergency access.
- **Management handoff:** permanent exceptions, resource shortage, critical service provider problems or accepted residual risks.

## Typical mistakes

- Protected areas are defined, but work rules are missing.
- Visitors are registered but not connected with a concrete work order.
- Cleaning and maintenance are treated as low risk although they regularly have access to critical areas.
- Emergency access is not followed up.
- Temporary access remains active after completion.
- Deviations are resolved locally and do not reach ISMS, Facility or Vendor Management.

## Fictional mini example

A fictional IT service provider lets an air-conditioning service into the server room. Until now, access was only announced by phone. After a review, the organisation introduces a maintenance ticket: period, persons, escorting, permitted activities and completion note. During the first appointment, it becomes apparent that a service provider wants to take photos. The photo rule is added and discussed in the next vendor review.

Evidence:

- Maintenance ticket with approval,
- visitor and escort evidence,
- completion note by the Facility Owner,
- documented deviation regarding the photo rule,
- updated service provider instruction.
