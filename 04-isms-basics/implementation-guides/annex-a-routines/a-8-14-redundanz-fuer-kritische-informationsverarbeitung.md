# A.8.14 — Redundancy for critical information processing

## Purpose

Redundancy for critical information processing ensures that central services continue to run or can switch over in a controlled way when individual components, locations, providers, or dependencies fail. The core is not “duplicate everything”, but a deliberate decision: which processing is critical, which redundancy is needed, how is it tested, and which residual risk remains accepted?

## Control objective in repository language

The organization operates a routine to identify critical information processing, define redundancy requirements, decide technical and organizational implementation paths, test failover capability, and escalate deviations. The routine connects architecture, operations, BCM, monitoring, suppliers, costs, and management decisions.

## Typical risks

- If critical services depend on single servers, lines, locations, or people, a single failure can interrupt business operations.
- If redundancy has been built but never tested, switchover may fail during a real event due to configuration, data state, or unclear roles.
- If dependencies such as identity services, DNS, network, key management, or external providers are missing, redundancy only works on paper.
- If redundancy requirements are not coordinated with RTO/RPO and BCM, either too little is built or unnecessary cost is created.
- If active and redundant components can be compromised in the same way, redundancy does not protect against cyber or misconfiguration scenarios.

## Triggers

- New or changed critical service, process, location, provider, or architecture component.
- Change in RTO/RPO, criticality, customer requirement, BCM assumption, or risk assessment.
- Incident, outage, near outage, performance problem, or failover failure.
- Change to cloud/data center, network, power, identity, or supplier.
- New dependency through SaaS, API, platform service, database, messaging, or automation.
- BCM exercise, emergency test, audit finding, or management question about resilience.
- Regular architecture and redundancy review.

## Roles and responsibilities

- **Service Owner / Business Unit:** defines criticality, outage tolerance, and service priority.
- **Architecture / Platform Owner:** designs redundancy, dependencies, failover, and fallback paths.
- **IT Operations / Operations:** operates monitoring, switchover, tests, capacity, and operational documentation.
- **BCM Responsible:** connect redundancy with emergency operations, restart sequence, and crisis exercises.
- **Security Role / ISMS Owner:** reviews security risks, compromise scenarios, evidence, and escalation.
- **Supplier Management:** clarifies provider redundancy, SLAs, dependencies, and evidence.
- **Management:** decides on target conflicts between costs, resilience, complexity, and accepted residual risk.

## Implementation

### Minimum start

Goal: identify and deliberately treat critical single points of failure.

1. The organization identifies the most important critical services and information processing in the ISMS/BCM scope.
2. Central dependencies are documented for each service: application, database, identity, network, location, provider, keys, person role.
3. Single points of failure are marked and prioritized.
4. For the most critical dependencies, a decision is made: implement redundantly, bridge manually, accept, or replace.
5. A simple failover or restart test is planned and documented.
6. Unclosed redundancy gaps are recorded with risk, owner, and follow-up date.

Minimum evidence:

- list of critical services with owner,
- dependency and single-point-of-failure overview,
- decision per critical gap,
- test or exercise evidence,
- management or risk acceptance for open gaps.

### Solid practice

Goal: redundancy is controlled repeatably with architecture, operations, and BCM.

1. Critical services receive redundancy targets matching RTO/RPO, data consistency, and operational priority.
2. Architecture decisions describe active/active, active/passive, manual switchover, hot/warm/cold standby, or organizational substitute processes.
3. Redundant components are monitored, patched, configured, and checked for capacity like production components.
4. Failover tests check switchover, fallback, data state, roles, communication, and impact on users.
5. Provider and SaaS dependencies are reviewed for realistic redundancy and exit/workaround capability.
6. Findings from tests lead to measures, architecture improvements, or management decisions.
7. Redundancy is connected with backup, incident response, change management, and BCM exercises.

Strong evidence:

- service criticality and redundancy matrix,
- architecture decision with dependencies,
- monitoring and capacity evidence,
- failover/fallback test logs,
- measures from failed tests,
- supplier evidence or SLA assessments,
- management decision on non-redundant critical dependencies.

### Advanced practice

Goal: critical information processing is resilient, tested, and controllable in a decision-ready way.

1. Redundancy design considers locations, regions, providers, identity, DNS, keys, network, data replication, and operational roles.
2. Chaos, resilience, or emergency exercises check realistic failure and compromise scenarios in a controlled way.
3. Automated failover mechanisms are monitored, bounded, and regularly tested with a fallback plan.
4. Changes to critical components trigger a review of redundancy and failover capability.
5. Metrics show availability gaps, test coverage, failover time, data deviations, open single points of failure, and provider dependencies.
6. Management receives decision-ready scenarios: cost of redundancy, expected outage impact, technical debt, and accepted residual risk.

## Routine flow

1. **Determine critical processing:** clarify service, process, data, user groups, dependencies, and BCM relevance.
2. **Define outage assumptions:** consider component, location, provider, network, identity, database, operating error, or cyber event.
3. **Decide redundancy need:** define target, architecture variant, organizational workaround, or risk acceptance.
4. **Implement:** prepare technical redundancy, substitute process, monitoring, documentation, and roles.
5. **Test:** check failover, fallback, data consistency, communication, permissions, and time required.
6. **File evidence:** document test flow, result, deviations, measures, and open risks.
7. **Review:** update dependencies after changes, incidents, exercises, and on a regular basis.
8. **Escalate:** send unmet targets, high costs, technical limits, or critical single points of failure to management.

## Decisions

- Which information processing is critical enough for technical redundancy?
- Which downtime and data loss are tolerable from a business perspective?
- Which architecture variant fits risk, costs, and operational capability?
- Which dependencies must also be redundant or bridgeable?
- How often and how realistically are failover and fallback tested?
- When is organizational emergency operation sufficient, and when is it not?
- Who accepts open single points of failure and for what period?

## Evidence

### Strong evidence

- current scope of critical services with owners,
- dependency model including single points of failure,
- redundancy and architecture decisions,
- monitoring and capacity evidence for primary and redundant components,
- failover/fallback test logs with result and duration,
- action log from tests or incidents,
- management decision on accepted redundancy gaps.

### Weak evidence

- architecture diagram without criticality or RTO/RPO reference,
- provider SLA without review of the organization’s own dependencies,
- statement “highly available” without test evidence,
- redundancy only for servers, but not for database, identity, or network,
- test log without result, time required, or measures.

### Evidence gaps

- unknown single points of failure,
- no owner for critical dependencies,
- redundant components are not patched or monitored,
- failover never tested,
- fallback unclear,
- SaaS or provider dependency without workaround,
- no management decision on redundancy that is not economically viable.

## Effectiveness review

Review questions:

- Are critical information processing activities and their dependencies currently known?
- Are there redundancy decisions matching RTO/RPO and BCM assumptions?
- Were failover and fallback tested realistically?
- Are redundant components monitored, maintained, and protected at an equivalent level?
- Are provider, identity, DNS, network, and key dependencies considered?
- Are open single points of failure risk-assessed and decided?

Possible metrics:

- share of critical services with redundancy decision,
- open single points of failure,
- failover test coverage,
- actual switchover time compared with target,
- failed or limited tests,
- overdue measures from resilience tests,
- critical provider dependencies without workaround.

## BSIG/NIS2 connection point

Redundancy of critical information processing is compatible as a connection point with NIS2-oriented risk management measures, business continuity, crisis capability, incident handling, supply chain risks, and maintenance of critical services. The concrete connection should be assessed in an organization-specific way through the requirements register, BCM analysis, risk analysis, and management review.

This artifact does not replace legal assessment of affectedness, an availability guarantee, or sector-specific obligation review.

## Boundaries

- Redundancy does not replace backups, incident response, or BCM.
- Highly available architecture can replicate cyber events or misconfigurations if protection logic is missing.
- This artifact is not a technical reference design for specific platforms.
- It does not guarantee availability, conformity, or certification capability.
- It contains no ISO 27002 text and no confidential architecture details.

## Handoffs

- **BCM Handoff:** criticality, RTO/RPO, emergency operations, restart sequence, and exercises.
- **IT / Architecture Handoff:** redundancy design, dependencies, failover, monitoring, capacity, and fallback.
- **Incident Handoff:** outage, compromise, failover during incident, technical restoration.
- **Change Handoff:** changes to critical components, provider change, network/identity changes.
- **Supplier Handoff:** provider redundancy, SLA, outage communication, exit or workaround capability.
- **Management Handoff:** costs, residual risk, non-redundant dependencies, target conflicts.
- **Audit / Evidence Handoff:** missing test evidence or unclear redundancy decisions.

## Typical mistakes

- Redundancy is built at server level, but central dependencies remain single.
- Failover is never exercised because tests are considered too risky.
- Redundant components are patched or monitored worse than primary systems.
- Provider SLAs are confused with the organization’s own restart capability.
- Active/active replication also carries over errors, encryption, or misconfiguration.
- Management sees the cost of redundancy, but not the outage impact of the gap.
- Fallback and communication paths are missing from the test.

## Fictional mini example

A fictional logistics service provider classifies its route planning system as critical. The dependency analysis shows that application and database run redundantly, but the central identity service is a single point of failure. IT tests a manual emergency access for crisis operations, BCM updates the emergency operations plan, and management decides on budget for a second identity instance. During the failover test, the switchover is documented; a missing DNS adjustment is recorded as an action.

Evidence:

- criticality and dependency overview,
- documented single point of failure,
- failover test log,
- BCM emergency operations adjustment,
- management decision on identity redundancy,
- action ticket for DNS correction.
