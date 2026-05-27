# A.8.17 — Time synchronization

## Purpose

Time synchronization ensures that systems, applications, log sources and security tools generate events with a reliable time reference. The practical value lies in traceable incident analysis, correct correlation of logs, stable authentication processes and reliable error diagnosis.

## Control objective in repository language

The organization operates a routine through which relevant systems use a defined, trusted time source, deviations are detected and remediated, and the time reference for logging, monitoring, access protection, certificates, backup and incident response remains traceable.

## Typical risks

- If systems use different times, log events cannot be reliably correlated.
- If time sources are unclear or manipulated, investigations, access evidence or technical checks may become faulty.
- If authentication, certificates or tokens depend on incorrect time, outages or security gaps arise.
- If cloud, SaaS and local systems do not have an aligned time basis, gaps arise in monitoring and incident response.
- If time deviations are not detected, errors remain unnoticed for a long time and complicate root cause analysis.
- If critical special environments are isolated, they are often excluded from the standard without a risk decision.

## Triggers

- New system, new server, new cloud environment, new network segment or new OT/special environment.
- Change to domain controllers, identity services, NTP/time servers, firewalls or routing.
- Incident, forensic need or log correlation problem.
- Certificate, token, backup, replication or authentication error with possible time reference.
- Monitoring hit on time deviation or unreachable time source.
- Supplier or SaaS change affecting timestamps, logs or reports.
- Regular review of critical infrastructure and log sources.

## Roles and responsibilities

- **IT/platform owner:** defines and operates time sources, client configurations, monitoring and incident remediation.
- **Network/infrastructure team:** provides reachability, segment transitions and technical restrictions.
- **Service owner / application owner:** assesses impacts on application, logs, authentication, jobs and interfaces.
- **Security role / ISMS owner:** links time synchronization with logging, monitoring, incident response and evidence requirements.
- **Incident response role:** uses time reference for triage and investigation and reports gaps back.
- **Supplier management:** clarifies timestamp quality and time sources for external services or managed services.
- **Management:** decides on structural gaps, legacy systems or investment needs.

## Implementation

### Minimum start

Goal: Critical systems use a defined time source and time deviations are visible.

1. Name critical systems and log sources: identity, servers, firewalls, cloud platform, SIEM/logging, backup, central applications.
2. For each system class, define which time source is used and who operates it.
3. Perform a simple check: current time source, synchronization status and detectable deviation.
4. Record deviations in an action log and prioritize them.
5. For isolated or non-synchronizable systems, document an exception with risk and review date.
6. Inform incident and logging routines which time basis is used.

### Solid practice

Goal: Time synchronization is operated as an infrastructure standard and checked regularly.

1. Standard configurations for servers, clients, network devices, cloud resources and virtual platforms are documented.
2. Time sources are redundant or resilient enough for the criticality of the environment.
3. Monitoring detects relevant time deviations and unreachable time sources.
4. New systems receive time synchronization through build, deployment or configuration management.
5. Logging and monitoring reviews check whether timestamps between sources can be correlated.
6. Special cases such as isolated networks, appliances, OT, lab environments or SaaS reports are explicitly decided.
7. Changes to time sources run through change and communication channels.

### Advanced practice

Goal: The time reference is reliable organization-wide, automatically checked and integrated into security processes.

1. Time configurations are maintained as a baseline in endpoint, server, cloud and network management.
2. Deviations create tickets or alerts with criticality according to system class.
3. Time sources, stratum/hierarchy, redundancy and dependencies are visible in architecture and operations documentation.
4. Incident and forensic playbooks contain assumptions and checks on the time basis.
5. Correlation between local, cloud and SaaS logs is tested regularly.
6. Critical time infrastructure is included in availability, backup and restart considerations.
7. Management sees open gaps, legacy exceptions and impacts on traceability.

## Routine flow

1. **Take system into scope:** include new or critical systems in the time configuration logic.
2. **Assign time source:** define standard source or justified exception.
3. **Check configuration:** check synchronization status and deviation.
4. **Enable monitoring:** capture relevant deviations, outages or unreachable sources.
5. **Treat deviation:** document owner, cause, action and deadline.
6. **Check log correlation:** test during reviews or incidents whether timestamps match.
7. **Review exceptions:** regularly reassess isolated, old or external systems.
8. **Build in lessons learned:** investigations with time problems lead to standard or tool adjustments.

## Decisions

- Which time sources apply to which system classes and environments?
- Which maximum time deviation is tolerable for logging, authentication and operations?
- Who operates central time sources and who may change them?
- How are isolated systems, appliances, OT or lab environments treated?
- Which time deviations trigger an alert, ticket or incident triage?
- How is timestamp quality assessed for SaaS, supplier reports and managed services?
- When does a technical gap need a management decision?

## Evidence

### Strong evidence

- Documented time sources and responsibilities by system class,
- configuration evidence for critical systems,
- monitoring or test reports on time deviations,
- tickets for remediating synchronization problems,
- evidence that new systems receive standard configurations,
- incident or exercise evidence using correlatable timestamps,
- exception decisions for special environments with review date.

### Weak evidence

- General statement “NTP is enabled” without scope and check,
- screenshot of a single server without coverage,
- standard image document without evidence of productive implementation,
- log correlation is assumed but never tested,
- service provider report with timestamps without clarification of the time basis,
- exceptions for isolated systems without risk decision.

### Evidence gaps

- No known time sources or owners,
- unknown deviations on critical systems,
- central log sources use different time bases,
- no treatment of time server outages,
- new systems are configured manually and inconsistently,
- external services provide timestamps that are not traceable,
- incident analysis fails due to unclear sequence of events.

## Effectiveness review

Review questions:

- Do critical systems use defined and reachable time sources?
- Are relevant time deviations detected and remediated?
- Can timestamps from identity, network, cloud, servers and applications be correlated?
- Are new systems automatically or bindingly included in the time routine?
- Are there documented decisions for isolated or non-standard-capable systems?
- Was the time basis checked in incident exercises or log reviews?
- Are changes to time sources traceable and controlled?

Possible metrics:

- Coverage of critical systems with defined time source,
- open time deviations by criticality,
- number of unreachable time sources,
- time to remediate relevant deviations,
- share of new systems with standard configuration,
- number of unchecked special exceptions.

## BSIG/NIS2 connection point

Time synchronization can connect to NIS2-oriented topics such as logging, monitoring, incident handling, access protection, operational stability and traceability of technical events. The concrete connection should be assessed organization-specifically in the requirements register, operating standards and incident response reviews.

This artifact does not replace legal assessment of evidence obligations, reporting obligations or technical evidentiary questions.

## Boundaries

- This artifact is not a detailed NTP/PTP architecture and not a product configuration.
- It does not replace forensic assessment if timestamps have already been manipulated or are inconsistent.
- High-precision special environments need their own technical assessment.
- No certification, conformity or security guarantee.
- No adoption of licensed standard texts.

## Handoffs

- **Logging/monitoring handoff:** inconsistent timestamps prevent correlation or alerting.
- **Incident handoff:** time deviation affects investigation, event sequence or suspicion of manipulation.
- **Platform/network handoff:** time source, firewall rule, segmentation or client configuration is faulty.
- **Supplier handoff:** SaaS, appliance or managed service timestamps are unclear or cannot be correlated.
- **BCM/operations handoff:** outage of central time sources endangers critical services.
- **Management handoff:** legacy or special environments remain permanently outside the standard.
- **Audit/evidence handoff:** evidence on the time basis is missing or not reviewable.

## Typical mistakes

- Time synchronization is treated as a one-time system setting.
- Critical network devices, appliances or cloud resources are forgotten.
- Monitoring checks availability but not relevant time deviation.
- Isolated systems are exempted without a risk decision.
- Time servers are changed without checking impacts on logging and authentication.
- Incident teams discover time problems only during the investigation.
- Supplier reports are compared with local logs although the time basis is unclear.

## Fictional mini example

A fictional company investigates several failed VPN sign-ins. The firewall logs and identity logs do not align in time. The platform owner checks the time source and finds an outdated configuration on two network devices. The devices are switched to the defined internal time source, monitoring for time deviations is enabled and a sample confirms correlatable events. An isolated lab environment remains exempt for now; the service owner documents the exception with a review date.
