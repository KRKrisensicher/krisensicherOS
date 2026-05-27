# A.8.21 — Security of network services

## Purpose

Network services such as internet access, site networking, DNS, VPN, proxy, WLAN, cloud connectivity, or managed network services are often prerequisites for operations. This routine ensures that such services are not only procured or technically activated, but controlled with security requirements, responsibilities, evidence, and review points.

## Control objective in repository language

The organization defines and operates security requirements for internal, external, and outsourced network services. Service scope, protection mechanisms, responsibilities, monitoring, change paths, incident communication, evidence, and exceptions are traceably regulated.

## Typical risks

- If network services are commissioned without security requirements, evidence, reporting paths, or technical protection options may be missing later.
- If provider and organizational responsibility remain unclear, incidents, vulnerabilities, or configuration errors are not handled in time.
- If DNS, VPN, proxy, or WLAN are treated as pure infrastructure, manipulation, misconfiguration, or outage can impair central services.
- If service provider access is not reviewed, uncontrolled paths into internal systems emerge.
- If performance and security metrics are missing, the organization notices deterioration only during disruption or attack.

## Triggers

- new network service, provider change, contract renewal, or tender.
- change to service scope, site, bandwidth, access technology, security options, or operating model.
- incident, disruption, vulnerability notification, provider notice, or audit finding.
- new cloud, remote access, WLAN, DNS, proxy, or site networking.
- changed protection needs, business continuity requirements, or management decision.
- periodic service and security review.

## Roles and responsibilities

- **Service owner:** responsible for business need, service scope, criticality, and review of the network service.
- **Network/platform owner:** assesses technical security requirements and operates internal configurations.
- **Procurement / supplier management:** anchors requirements, evidence, contacts, and escalation paths in the supplier process.
- **Security role / ISMS owner:** defines minimum requirements, risk logic, and evidence logic.
- **BCM responsible roles:** review dependencies, restart, fallback paths, and critical operational consequences.
- **Legal / data protection:** review contract, data protection, and communication questions where affected.
- **Management:** decides on critical dependencies, cost/security conflicts, or accepted residual risks.

## Implementation

### Minimum start

Goal: make critical network services visible with owner, security requirements, and contacts.

1. The organization lists the most important network services in scope: internet connectivity, VPN, DNS, WLAN, proxy, site networking, cloud connectivity, or managed services.
2. For each critical service, owner, provider, purpose, criticality, and affected sites or services are recorded.
3. Minimum requirements are documented: authentication, encryption, logging, availability, support path, incident contact, and change process.
4. Contracts, service descriptions, or operating documents are reviewed for security and escalation points.
5. Open gaps are managed as measures, exceptions, or management questions.

Minimum evidence:

- network service register with owners,
- service description or contract reference,
- documented minimum requirements,
- contact and escalation list,
- review note with gaps and measures.

### Solid practice

Goal: network services are procured, operated, and reviewed on a risk basis.

1. Security requirements are reviewed before procurement or change and transferred into selection, contract, or operating agreement.
2. Critical network services receive defined SLAs, security contacts, maintenance windows, reporting paths, and evidence formats.
3. Provider changes, maintenance, and disruptions are mirrored in internal change, incident, and BCM processes.
4. Service provider access is connected with access control, purpose, duration, and review.
5. Service reviews examine disruptions, security notifications, open risks, changes, and evidence.
6. Dependencies feed into risk analysis, contingency planning, and management review.

Strong evidence:

- requirements from tender, contract, or service description,
- service review records with security portion,
- evidence on availability, disruptions, security notifications, or maintenance,
- tickets for provider changes and internal follow-up changes,
- risk and BCM assessment of critical network services,
- documented exceptions with expiry date.

### Advanced practice

Goal: network services are controlled as critical supply and operating dependencies.

1. Service information, provider contacts, SLAs, disruptions, and security events are maintained centrally in an evaluable form.
2. Critical network services are integrated into monitoring, incident response, crisis communication, and BCM exercises.
3. Redundancy, alternative access paths, and dependencies are regularly tested or plausibility-checked.
4. Security metrics such as unresolved provider findings, SLA breaches, disruption duration, unchecked changes, and open exceptions are reported.
5. For particularly critical services, independent evidence, technical tests, or joint exercises with service providers are used.

## Routine flow

1. **Need or change arises:** new service, contract change, provider notice, disruption, or review.
2. **Classify service:** determine purpose, criticality, affected services, data flows, sites, and dependencies.
3. **Define requirements:** define security, availability, monitoring, incident communication, evidence, and access protection.
4. **Perform supplier/contract check:** clarify responsibilities, contacts, and escalation paths.
5. **Implement technically and organizationally:** set up configuration, monitoring, contacts, operating documentation, and change paths.
6. **Record evidence:** store contract, service description, review, disruption, change, or provider confirmation.
7. **Review:** regularly examine performance, security, findings, exceptions, and dependencies.
8. **Escalate:** give critical gaps, unclear responsibilities, or unacceptable dependencies to management.

## Decisions

- Which network services are critical for business, security, or availability?
- Which security requirements are mandatory before commissioning, and which are risk-based?
- Which evidence must a provider deliver regularly?
- Which disruptions or security notifications trigger incident, BCM, or management handoff?
- Which dependencies need redundancy or fallback procedures?
- Who may accept exceptions to provider requirements and for how long?

## Evidence

### Strong evidence

- current network service register with owner, provider, criticality, and review date,
- documented security requirements and service descriptions,
- contract or supplier evidence on responsibilities, reporting paths, and support,
- service review records with decisions,
- incident/disruption and change tickets with provider reference,
- BCM or risk analysis of critical network services,
- management decision for accepted dependencies or gaps.

### Weak evidence

- provider contract without security evaluation,
- technical product description without internal owners,
- SLA values without review or measures,
- contact list without test or currency date,
- broad statement “provider is responsible” without responsibility matrix.

### Evidence gaps

- critical services without owner or escalation contact,
- unclear separation between provider and internal responsibility,
- no evidence on security notifications or disruptions,
- service provider access without access routine,
- missing BCM reference for central network dependencies,
- exceptions without duration or risk decision.

## Effectiveness review

Review questions:

- Are all critical network services known with owner, provider, and criticality?
- Were security requirements reviewed before procurement or change?
- Can disruptions and security notifications be assigned to an internal process?
- Are provider changes and service provider access controlled traceably?
- Are escalation contacts current and have they been plausibility-checked?
- Are critical dependencies visible in the risk and BCM context?

Possible metrics:

- share of critical network services with current review,
- open provider findings by criticality,
- SLA breaches or recurring disruptions,
- unresolved provider changes,
- overdue exceptions,
- critical services without tested escalation path.

## BSIG/NIS2 connection point

Secure network services are a connection point for NIS2-oriented topics such as risk management, supply chain security, operational security, incident handling, business continuity, and secure communication. The specific connection should be assessed organization-specifically in the requirements register, supplier management, and management review.

This artifact does not replace legal assessment of applicability, contract design, or evidence obligations.

## Boundaries

- This artifact is not a contract template and not legal advice.
- It does not replace technical provider assessment or network architecture review.
- SLAs alone do not demonstrate security or effectiveness.
- Data protection questions may arise when network services process logs, user references, or content data.
- No certification promise and no adoption of licensed standard text.

## Handoffs

- **Procurement/supplier handoff:** new services, contract changes, provider changes, missing security evidence.
- **Change handoff:** technical migration, maintenance, routing, DNS, VPN, proxy, or cloud connectivity change.
- **Incident handoff:** provider security notification, service disruption with security impact, suspected misuse.
- **BCM handoff:** critical dependency, outage risk, redundancy need, or emergency exercise.
- **Data protection/legal handoff:** personal logs, content filtering, contract questions, or reporting obligation questions.
- **Management handoff:** cost/security conflict, unmet minimum requirement, accepted residual risk.
- **Audit/evidence handoff:** missing reviews, unclear responsibility matrix, or outdated evidence.

## Typical mistakes

- Network services are procured as technical commodities without clarifying security requirements.
- Provider responsibility is overestimated; internal owners are missing.
- Escalation contacts exist but are never tested or updated.
- Disruptions are resolved operationally but not used for risk and BCM reviews.
- Service provider access remains outside the access routine.
- Security evidence is searched for only during an audit.
- Redundancy is assumed but not reviewed with dependencies and restart.

## Fictional mini example

A fictional retail company changes internet provider for two sites. The service owner records the service in the network service register, procurement adds security and escalation contacts to the contract file, and the network owner reviews DNS, firewall, and monitoring adjustments. The first service review reveals a gap: maintenance notifications reach only one individual. Management decides to switch the escalation path to a group mailbox and an on-call contact.

Evidence:

- updated network service register,
- contract/service description with contacts,
- change tickets for technical migration,
- service review record,
- management decision on escalation path.
