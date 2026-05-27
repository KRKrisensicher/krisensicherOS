# A.7.11 — Utility and infrastructure services

## Purpose

Utility and infrastructure services such as power, cooling, network/carrier connectivity, water, fire protection, building management systems, access technology, or external data center services can directly influence the availability and security of information processing. This routine ensures that such dependencies are not treated only as a facility topic, but as managed operational and resilience dependencies.

The core is not “UPS exists”, but the question: Which services depend on what, which outages are tolerable, who monitors the dependency, who decides on redundancy, maintenance, escalation, and residual risk?

## Control objective in repository language

The organization operates a routine that maps critical information processing and business processes to their relevant utility and infrastructure dependencies, protects, monitors, tests, and reviews them when changes occur.

## Typical risks

- If power, cooling, or network supply for critical systems has not been assessed, individual outages can interrupt entire services.
- If maintenance on building or infrastructure technology is not coordinated with IT operations, unplanned outages arise.
- If redundancies are only assumed but not tested, they fail during an event.
- If external infrastructure or carrier dependencies are unknown, escalation paths and restart plans are missing.
- If environmental or building technology alarms do not feed into operational processes, critical early signs are overlooked.
- If conflicts between cost, sustainability, security, and availability are not decided, risks remain hidden.

## Triggers

- new or changed site, technical room, data center, carrier, cloud/housing service, or production area.
- introduction or change of a critical service.
- maintenance, renovation, refurbishment, power shutdown, cooling change, or network work.
- outage, near outage, alarm, incident, or BCM exercise.
- supplier change, contract change, or SLA review.
- risk analysis, business impact analysis, asset review, or management question.
- regular infrastructure, facility, or resilience review.

## Roles and responsibilities

- **Service Owner / Process Owner:** assesses business criticality, tolerable downtimes, and impacts.
- **IT / Platform Owner:** names technical dependencies, monitoring needs, failover, and restart requirements.
- **Facility / Location Owner:** is responsible for power, climate, rooms, technical building infrastructure, and maintenance coordination.
- **BCM Owner / Crisis Role:** connects infrastructure dependencies with BIA, emergency plans, exercises, and restart.
- **ISMS Owner / Security Role:** defines assessment logic, risk, and evidence requirements.
- **Procurement / Supplier Management:** manages contracts, SLAs, escalation contacts, and service provider reviews.
- **Management:** decides on redundancy, investments, residual risks, priorities, and service objectives.

## Implementation

### Minimum start

Goal: Critical infrastructure dependencies are visible and have owners.

1. The organization identifies the most important services, sites, or technical areas in ISMS scope.
2. Relevant dependencies are recorded for them: power, cooling, network/internet, access, fire protection, water/leakage, external data center or carrier services.
3. Owners and escalation contacts are documented.
4. For critical dependencies, it is checked whether minimum protection exists: UPS, climate monitoring, alternative path, maintenance contract, alerting, or manual workaround routine.
5. Maintenance and changes to infrastructure are coordinated with IT/service owners.
6. Open gaps are managed as a risk, measure, or management decision.

Minimum evidence:

- dependency list of critical services/sites,
- owner and contact list,
- maintenance or change ticket,
- evidence of existing protection or monitoring measure,
- risk/measure log for gaps.

### Solid practice

Goal: Infrastructure dependencies are managed, tested, and reviewed in a risk-based way.

1. Services are connected with tolerable downtimes, restart priority, and infrastructure dependencies.
2. Minimum requirements per criticality class are defined: redundancy, UPS runtime, cooling, network path, alerting, maintenance window, escalation.
3. Maintenance is controlled through change or facility processes with risk and communication check.
4. Monitoring and alarm paths are checked regularly.
5. Redundancies, emergency power, failover, or workaround procedures are tested appropriately.
6. Service provider SLAs and escalation contacts are reviewed.
7. Findings feed into BCM, ISMS review, and management review.

Strong evidence:

- service dependency matrix,
- maintenance and change evidence,
- monitoring or alarm test records,
- test evidence for UPS, failover, alternative line, or restart,
- SLA/service provider review,
- risk and measure decisions.

### Advanced practice

Goal: Infrastructure resilience is integrated with architecture, monitoring, BCM, and management steering.

1. Infrastructure dependencies are maintained consistently in CMDB, service catalog, BIA, and crisis plans.
2. Critical infrastructure has defined thresholds, alarms, escalation chains, and on-call logic.
3. Capacity, lifecycle, maintenance condition, and single points of failure are assessed regularly.
4. Exercises test combined scenarios: power outage, cooling outage, carrier disruption, access system failure, or site loss.
5. Investment decisions are justified with risk reduction, service criticality, and BCM objectives.
6. Management receives metrics on dependencies, test status, open single points of failure, and overdue infrastructure measures.

## Routine flow

1. **Consider service or site:** critical process, technical room, data center, branch office, or new service.
2. **Record dependencies:** power, cooling, network, access, fire/water protection, external providers, and building management systems.
3. **Assess criticality:** impact, tolerable interruption, restart priority, and data/service reference.
4. **Define protection and monitoring:** redundancy, monitoring, maintenance, workaround procedure, escalation.
5. **Coordinate changes:** align maintenance and renovation with change, facility, and service calendars.
6. **Test and validate:** check alarm, UPS, failover, restart, or manual workaround routine.
7. **Secure evidence:** file matrix, ticket, test record, SLA review, or measure log.
8. **Escalate:** pass unacceptable single points of failure, investment needs, or overdue measures to management.
9. **Learn:** feed outages, tests, and near misses back into BCM, architecture, and operations.

## Decisions

- Which services and sites are critical enough for detailed infrastructure management?
- Which outage times and restart objectives are acceptable for the business?
- Which redundancies are necessary, and which residual risks are accepted?
- How are maintenance activities prioritized and communicated?
- Which infrastructure dependencies must be tested and how often?
- Which external service providers or carriers need SLA and escalation reviews?
- When does an infrastructure deficiency become a management or BCM topic?

## Evidence

### Strong evidence

- current dependency matrix for critical services,
- documented owners, escalation contacts, and SLAs,
- maintenance/change tickets with risk and communication check,
- monitoring and alarm test evidence,
- UPS, failover, emergency power, cooling, or restart test,
- findings with measures and responsible persons,
- management decision on redundancy, investment, or residual risk.

### Weak evidence

- general statement “Facility is responsible” without service reference,
- UPS or climate device inventory without test evidence,
- SLA document without escalation exercise or review,
- room plan without dependency to critical services,
- maintenance announcement without risk or communication assessment.

### Evidence gaps

- critical services without infrastructure dependency analysis,
- unknown single points of failure,
- alarms without recipient or response process,
- redundancies without test,
- maintenance without IT/service coordination,
- external dependencies without contact person or SLA review.

## Effectiveness review

Review questions:

- Are critical services assigned to their most important utility and infrastructure dependencies?
- Are owners and escalation contacts current?
- Are maintenance and changes coordinated before they endanger services?
- Have redundancies, alarms, or workaround procedures actually been tested?
- Are single points of failure known and decided?
- Do outages and near outages feed into measures and BCM planning?

Possible metrics:

- share of critical services with dependency matrix,
- open single points of failure,
- overdue infrastructure tests,
- unplanned outages with infrastructure cause,
- alarm response time,
- overdue SLA or supplier reviews,
- open measures from BCM exercises.

## BSIG/NIS2 connection point

Utility and infrastructure services can connect to NIS2-oriented risk management measures, business continuity, incident handling, supply chain security, operational security, and maintenance of essential services. The concrete connection should be assessed through the requirements register, risk analysis, BIA, and management review.

This artifact does not replace legal review, technical planning by specialist engineers, or a binding statement on applicability.

## Boundaries

- This artifact is not a building, electrical, climate, fire protection, or data center planning standard.
- It does not replace occupational safety, building, insurance, or operator obligation review.
- It does not replace a BCM strategy, but provides connection points for infrastructure dependencies.
- It makes no certification or conformity commitment.
- It contains no confidential location, network, or building plans.

## Handoffs

- **Facility handoff:** power, climate, building infrastructure, maintenance, alerting, access, and structural measures.
- **IT operations handoff:** monitoring, failover, restart, platform dependencies, and change coordination.
- **BCM/crisis handoff:** BIA, emergency strategy, restart priorities, exercises, and crisis decisions.
- **Supplier handoff:** carrier, data center, maintenance service provider, SLA, escalation contacts, and contract reviews.
- **Incident handoff:** infrastructure disruption, near outage, alarm, or security suspicion.
- **Management handoff:** redundancy investment, intolerable single point of failure, resource shortage, or residual risk acceptance.
- **Audit/evidence handoff:** missing tests, outdated contacts, or non-traceable dependency data.

## Typical mistakes

- Infrastructure is treated as a facility topic and not connected with critical services.
- Redundancy is assumed, but never tested.
- Maintenance on power, climate, or network is not coordinated with Service Owners.
- External carrier or data center dependencies are missing from the risk picture.
- Alarms go to individuals without deputy or response routine.
- UPS, cooling, or fire protection exist, but maintenance and test evidence is missing.
- Management sees investment wishes, but no risk-based options.

## Fictional mini example

A fictional mid-sized company operates a central ERP system in a local technical room. The BIA makes clear that power outage and cooling outage affect the same service. Facility and IT create a dependency matrix, test the UPS alarm, and find that notification goes to only one individual. The alarm chain is expanded; a second internet connection is prepared as a management decision with cost and risk assessment.

Evidence:

- service dependency matrix,
- UPS alarm test,
- updated escalation list,
- measure ticket for the alarm chain,
- management brief for the second connection.
