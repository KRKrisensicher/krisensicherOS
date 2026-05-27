# A.7.5 — Protection against physical and environmental threats

## Purpose

Physical and environmental threats can affect information assets, IT operations and critical processes even without a cyberattack: fire, water, heat, power outage, dust, construction work, severe weather, vandalism or unsuitable storage. This routine ensures that such threats are not only generally known, but assessed, treated and reviewed in relation to sites and assets.

## Control objective in repository language

The organisation operates a routine for identifying, assessing and treating physical and environmental threats to sites, rooms, systems, data media and critical operating processes, and for transferring them into BCM, facility and ISMS reviews.

## Typical risks

- If technical rooms are not considered with regard to water, heat or power problems, a local event may cause central services to fail.
- If construction work, maintenance or external companies are not assessed from a security perspective, damage, interruptions or unnoticed exposure may arise.
- If data media, paper archives or devices are stored in unsuitable ways, information may be damaged, lost or disclosed.
- If environmental threats are not connected with business continuity requirements, fallback procedures and priorities are missing.
- If warnings, sensors or maintenance are not reviewed, gradual risks such as humidity, temperature or power instability remain invisible.

## Triggers

- New site, room, technical area, archive, warehouse or production environment.
- Conversion, construction work, maintenance, change to cooling, power, water or fire protection environment.
- New critical system, new process or changed availability requirement.
- Disruption, water damage, fire event, overheating, power outage, severe weather or near miss.
- Insurance, landlord, facility, BCM or risk review.
- Supplier change for facility, maintenance, energy supply, data centre or storage provider.
- Audit finding or management question on site and operational resilience.

## Roles and responsibilities

- **Site / Facility Owner:** responsible for threat identification, structural and technical protective measures, maintenance and service provider coordination.
- **Asset Owner / Service Owner:** assesses impacts on information, systems, processes and recovery priorities.
- **BCM Owner:** connects physical threats with emergency planning, recovery and fallback procedures.
- **IT / Platform Owner:** assesses technical rooms, power, cooling, backup media, network and operational dependencies.
- **ISMS Owner / Risk owners:** brings together risks, measures, exceptions and reviews.
- **Procurement / Vendor Management:** manages external facility, data centre, maintenance or storage service providers.
- **Management:** decides on investments, residual risks, priorities and accepted site dependencies.

## Implementation

### Minimum start

Goal: make obvious physical and environmental threats to critical areas visible and controllable.

1. Critical rooms, technical areas, archives, storage areas and work areas in ISMS scope are identified.
2. Typical threats are roughly checked for each area: fire, water, heat/cold, power, construction work, dust, access, storage.
3. Existing protective measures and dependencies are documented: detectors, maintenance, cooling, UPS, extinguishing agents, landlord, service providers.
4. Open gaps are managed as measures, time-limited exceptions or management decisions.
5. Disruptions and near misses are included in the review as lessons learned.
6. A BCM handoff is triggered if outage of an area affects critical services or recovery objectives.

Minimum evidence:

- List of critical areas with owner,
- simple overview of threats and measures,
- maintenance or inspection notes,
- disruption/near-miss note,
- measure or risk decision.

### Solid practice

Goal: physical and environmental threats are managed in a risk-based way with Facility, IT and BCM.

1. Threats are assessed systematically per site and room type.
2. Protective measures are maintained with owner, maintenance interval, test logic and escalation path.
3. Changes to construction, power, cooling, water, fire protection or storage trigger a security and BCM review.
4. Critical systems are connected with availability requirements, fallback procedures and recovery priorities.
5. Service provider and landlord dependencies are documented and reviewed.
6. Disruptions lead to root cause analysis and measure tracking.
7. Residual risks, investment needs and site dependencies that cannot be resolved are submitted to management review.

Strong evidence:

- Site-related threat analysis,
- measures and maintenance register,
- sensor, test, maintenance or inspection logs,
- change review for construction or technical infrastructure,
- lessons learned from disruptions,
- BCM linkage for critical services,
- management decision on residual risks or investments.

### Advanced practice

Goal: site resilience, environmental monitoring and recovery capability are operated in an integrated way.

1. Environmental and infrastructure data such as temperature, humidity, power, UPS, leakage or alarm status are monitored on a risk basis.
2. Critical site dependencies are connected with BIA, BCM plans, recovery exercises and supplier management.
3. Construction and maintenance work is controlled through approval, escort and acceptance processes.
4. Scenarios such as power outage, water ingress, fire, heatwave or site loss are considered in exercises.
5. Recurring disruptions lead to structural decisions: conversion, relocation, redundancy, service provider change or accepted residual risk.
6. Management receives metrics and decision papers on site and infrastructure resilience.

## Routine flow

1. **Threat or change emerges:** site, room, technology, construction, weather situation, disruption or new service.
2. **Clarify affectedness:** which information, systems, processes, data media or people are affected?
3. **Assess risk:** classify likelihood, impact, existing protective measures and recovery dependency.
4. **Define measures:** avoidance, protection, monitoring, maintenance, fallback procedure or compensation.
5. **Implement and test:** Facility, IT, BCM and service providers carry out measures, tests or maintenance.
6. **Secure evidence:** document review, test, maintenance, disruption or decision in a traceable way.
7. **Control deviations:** escalate open gap, overdue maintenance or intolerable risk.
8. **Learn:** feed disruptions and near misses back into risk analysis, site planning and BCM.

## Decisions

- Which rooms, systems and processes are critical with regard to physical or environmental threats?
- Which threats are accepted, compensated or reduced through investment?
- Which maintenance, tests or sensors are appropriate for the protection need?
- When does a site gap lead to BCM measures or a relocation decision?
- Which dependencies on landlord, energy supply, data centre or facility service provider are tolerable?
- Who accepts residual risks when structural measures are not possible in the short term?

## Evidence

### Strong evidence

- Current scope of critical rooms and assets,
- site- or room-related threat analysis,
- measures register with owner, deadline and status,
- maintenance, sensor, inspection or test logs,
- change approvals for construction/infrastructure work,
- lessons learned from disruptions or near misses,
- BCM linkage and management decision for residual risks.

### Weak evidence

- General site description without threat reference,
- insurance or landlord documents without internal assessment,
- maintenance evidence without assignment to critical areas,
- old walkthrough without measure tracking,
- statement “the data centre is professional” without supplier or evidence review.

### Evidence gaps

- Critical rooms without threat assessment,
- no response to repeated temperature, power or humidity events,
- construction work without security or BCM review,
- external data centre or storage dependency without owner,
- accepted structural gaps without risk decision.

## Effectiveness review

Review questions:

- Are relevant physical and environmental threats to critical areas known?
- Are protective measures maintained, tested and followed up when faults occur?
- Do construction, maintenance and site changes trigger a review?
- Are critical systems connected with recovery and fallback logic?
- Are landlord and service provider dependencies actively managed?
- Are there management decisions on residual risks that cannot be resolved in the short term?

Possible metrics:

- Critical areas with current threat assessment,
- open measures from walkthroughs or disruptions,
- overdue maintenance or tests,
- number of relevant environmental alarms,
- time to resolve critical facility faults,
- BCM-relevant site residual risks.

## BSIG/NIS2 connection point

Protection against physical and environmental threats is a connection point for NIS2-oriented topics such as risk management, business continuity, crisis capability, protection of critical operating environments and supply chain/service provider dependencies. Concrete requirements should be assessed organisation-specifically in the requirements register and in risk and BCM artefacts.

This artefact does not replace legal, structural, occupational safety, insurance-related or authority-related assessment.

## Boundaries

- This artefact is not fire protection, construction, electrical or occupational safety advice.
- It does not replace technical planning for data centres, buildings or production environments.
- It provides no security, availability or conformity guarantee.
- It contains no ISO 27002 text or certification promise.
- Public examples remain fictional and without sensitive site details.

## Handoffs

- **Facility handoff:** buildings, maintenance, cooling, power, water, fire protection, construction work, landlord.
- **IT handoff:** technical rooms, networks, servers, backup media, UPS, monitoring.
- **BCM handoff:** outage of critical areas, alternative site, recovery, exercises.
- **Procurement / Vendor handoff:** data centre, storage, maintenance, energy, facility service providers.
- **Management handoff:** investments, site dependencies, accepted residual risks, prioritisation.
- **Legal / Data protection handoff:** contract questions, personal data in disruption/access logs, authority topics.
- **Audit / Evidence handoff:** missing maintenance, test, disruption or risk-decision evidence.

## Typical mistakes

- Environmental threats are considered only for data centres, not for archives, storage areas or office space.
- Maintenance evidence exists, but no one assesses its relevance for critical services.
- Construction work is treated as a facility topic and not coordinated with IT, ISMS or BCM.
- Near misses are resolved informally but not transferred into risk analysis and the measures log.
- Dependencies on landlord or service provider are not made decision-ready.
- Sensors alarm, but response paths and responsibilities are missing.

## Fictional mini example

A fictional specialist publisher stores contract archives and backup media in a basement room. After heavy rain, Facility discovers moisture on a wall. The ISMS Owner, Facility and IT assess the room as unsuitable for backup media. In the short term, the media are moved to a dry, locked room; in the medium term, management decides on external storage and better site separation.

Evidence:

- Disruption note on the humidity event,
- updated threat assessment of the basement room,
- ticket for moving the media,
- risk decision on the interim solution,
- management decision on future storage strategy.
