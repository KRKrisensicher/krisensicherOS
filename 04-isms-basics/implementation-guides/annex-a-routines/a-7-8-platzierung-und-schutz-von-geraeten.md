# A.7.8 — Placement and protection of equipment

## Purpose

Placement and protection of equipment ensures that servers, network components, workstations, printers, kiosk systems, sensors, or other technical devices are not unnecessarily exposed to physical access, manipulation, environmental influences, or observation.

The core is not “the device is somewhere in the office”, but a traceable decision: Which device is critical, where may it be placed, what environment does it need, who may work on it, and how is it checked whether protection holds up in day-to-day operation?

## Control objective in repository language

The organization operates a routine for placing, protecting, reviewing, and reassessing equipment according to criticality, location, access possibilities, and environmental risks when changes occur.

## Typical risks

- If critical network equipment is freely accessible, unauthorized persons can pull cables, restart devices, use ports, or change configurations.
- If screens, printers, or multifunction devices are placed in open areas, information can be read, taken away, or collected incorrectly.
- If devices are operated in unsuitable environments, heat, humidity, dust, vibration, or power problems can cause outages.
- If temporary devices in projects, events, or relocations are not assessed, unprotected transitional solutions emerge.
- If protection requirements are considered only during initial setup, later renovations, new teams, or changed use remain unnoticed.

## Triggers

- new device, new device class, or changed location.
- office, warehouse, technical room, or data center relocation.
- renovation, refurbishment, space change, or new visitor/service provider routes.
- new service that requires local devices or edge components.
- security event, loss, suspected manipulation, outage, or near miss.
- maintenance, device replacement, decommissioning, or inventory.
- regular location, asset, or facility review.

## Roles and responsibilities

- **Asset Owner / Service Owner:** assesses criticality, protection needs, and business impact of a device.
- **IT / Platform Owner:** defines technical minimum requirements, operates devices, and documents changes.
- **Facility / Location Owner:** is responsible for rooms, furniture, physical protection measures, and location changes.
- **ISMS Owner / Security Role:** defines assessment logic, review frequency, exception handling, and escalation paths.
- **Business unit / Process Owner:** reports changes in use and specific privacy-screening or availability requirements.
- **Procurement / Supplier Management:** considers equipment placement, maintenance access, and service provider involvement in procurement and contracts.
- **Management:** decides in conflicts between cost, ergonomics, availability, security, and space use.

## Implementation

### Minimum start

Goal: Critical devices are not placed by chance, but with an owner, location decision, and simple check.

1. The organization identifies critical device classes in scope: network devices, servers, backup hardware, central printers, reception/kiosk systems, production or building technology with IT relevance.
2. An owner is named for each critical device class.
3. Locations are assessed using simple protection logic: publicly accessible, supervised, lockable, climatically suitable, susceptible to manipulation.
4. Obvious risks are treated: lockable room or cabinet, privacy screening, port protection, separated visitor areas, clear maintenance rule.
5. Changes to location or use trigger a short reassessment.
6. Exceptions are documented with rationale, duration, and follow-up date.

Minimum evidence:

- list of critical device classes or devices with owner,
- location/room assignment,
- simple protection assessment or checklist,
- ticket or review note for relocation/change,
- documented exception with follow-up date.

### Solid practice

Goal: Equipment placement is embedded in asset, location, and change processes.

1. Devices are classified by criticality and location type: technical room, office area, publicly accessible area, production area, branch office, mobile/temporary setup.
2. Minimum protection per class is defined: access restriction, environmental conditions, privacy screening, cable protection, port use, maintenance access, inventory labeling.
3. Procurement, relocation, and change management check location requirements before commissioning.
4. Facility and IT conduct joint spot checks.
5. Findings lead to a measure, exception, or management decision.
6. Protection requirements for service provider maintenance and temporary installations are visible in tickets or work orders.

Strong evidence:

- equipment/asset inventory with location and owner,
- minimum protection logic per location or device class,
- change or relocation tickets with location check,
- spot-check records with measures,
- evidence of remediated deficiencies,
- exception decisions with deadline.

### Advanced practice

Goal: Equipment protection is connected with monitoring, facility management, and resilience planning.

1. Critical rooms and devices are connected to access, environmental, or availability monitoring.
2. Asset inventory, CMDB, location plans, and maintenance contracts are reconciled regularly.
3. Critical devices have defined requirements for redundancy, spare parts, maintenance windows, and escalation.
4. Manipulation, temperature, power, or location alarms feed into incident triage or operational monitoring.
5. Location decisions are considered in BCM, crisis, and architecture reviews.
6. Management receives decision-ready information on residual location risks, investment needs, and recurring deficiencies.

## Routine flow

1. **Need arises:** new device, new location, relocation, maintenance, or change.
2. **Clarify criticality:** classify affected service, data, dependencies, and impact.
3. **Assess location:** check accessibility, visibility, manipulation possibility, environmental conditions, and maintenance needs.
4. **Define protection:** determine room, cabinet, position, labeling, privacy screening, port/cable protection, or organizational rule.
5. **Implement:** IT, Facility, or service providers implement the measure.
6. **Secure evidence:** file inventory, ticket, photo only if non-critical, checklist, or review note.
7. **Review:** spot check or location review checks whether devices are still placed appropriately.
8. **Escalate:** pass non-implementable protection measures, cost conflicts, or residual risks to management.

## Decisions

- Which devices are considered critical in the ISMS scope?
- Which locations are permitted for which device classes?
- When is organizational control sufficient, and when is structural or technical protection needed?
- Which devices may be placed in publicly accessible or unsupervised areas?
- How are temporary setups, test devices, and project areas handled?
- Who accepts residual risks if location or budget does not allow appropriate protection?

## Evidence

### Strong evidence

- current equipment inventory with location and owner,
- documented location and protection assessment,
- change/relocation tickets with approval,
- facility or IT spot checks with findings and measures,
- evidence of implemented protection measures,
- time-limited exception with risk decision,
- management decision for non-remediable location conflicts.

### Weak evidence

- general clean-desk or facility rule without equipment reference,
- outdated room plans without asset reconciliation,
- photos without date, owner, or assessment,
- statement “protected in the server room” without access or review evidence,
- inventory list without location quality.

### Evidence gaps

- critical devices without owner,
- devices in open areas without protection assessment,
- relocations without security check,
- temporary installations without expiry date,
- deficiencies without measure or exception decision.

## Effectiveness review

Review questions:

- Can critical devices be assigned to a location, owner, and protection need?
- Are location changes checked before commissioning?
- Are devices in open areas consciously assessed and protected?
- Do spot checks lead to corrections or decisions?
- Are environmental and manipulation risks for critical devices visible?
- Are exceptions time-limited and reviewed?

Possible metrics:

- share of critical devices with location and owner,
- open findings from location reviews,
- overdue exceptions,
- unplanned outages with location/environment relevance,
- number of non-inventoried devices in spot checks.

## BSIG/NIS2 connection point

The placement and protection of equipment can connect to NIS2-oriented risk management measures, physical security, cyber hygiene, maintenance of critical services, and business continuity. For affected organizations, the requirements register should be used to assess which locations, services, and evidence are relevant.

This artifact does not replace legal review, building-law assessment, or a binding statement on applicability.

## Boundaries

- This artifact is not a detailed building, data center, or fire protection standard.
- It does not replace occupational safety, data protection, insurance, or building security review.
- It makes no certification or conformity commitment.
- It contains no ISO 27002 text and no confidential location details.
- It is not sufficient as evidence if devices are actually operated unchecked or unprotected.

## Handoffs

- **Facility handoff:** room, cabinet, climate, access, renovation, furniture, or location deficiency.
- **IT operations handoff:** device setup, port protection, configuration, monitoring, maintenance, and inventory upkeep.
- **BCM handoff:** location or environmental risk may interrupt a critical service.
- **Incident handoff:** suspected manipulation, theft, unauthorized access, or unexplained outage.
- **Procurement/supplier handoff:** new devices, maintenance contracts, service provider access, or location requirements.
- **Management handoff:** structural investment, space conflict, accepted residual risk, or permanent exception.
- **Audit/evidence handoff:** missing owner, outdated location data, or non-traceable review evidence.

## Typical mistakes

- Devices are protected during setup, but not reassessed after relocations.
- Small network components are not treated as critical assets.
- Printers and multifunction devices are placed in open areas without information protection logic.
- Facility and IT work with different location lists.
- Temporary installations become permanent.
- Environmental conditions are considered only after outages.
- Management receives deficiency lists, but no decision-ready risk and investment options.

## Fictional mini example

A fictional service provider moves a team into a new office area. During the location check, it becomes apparent that a switch for the customer network is planned in an open sideboard. The IT Owner assesses the device as critical, Facility provides a lockable network cabinet, and the relocation ticket is closed only after the location has been documented. An exception remains for a temporary test device and is limited to four weeks.

Evidence:

- relocation ticket with location check,
- asset entry with owner and location,
- evidence of the lockable cabinet,
- time-limited exception for the test device,
- review date after project end.
