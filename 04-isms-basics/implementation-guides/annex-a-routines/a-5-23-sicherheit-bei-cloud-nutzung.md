# A.5.23 — Security in cloud use

## Purpose

Cloud use changes responsibilities, technical control, and dependencies. This routine helps not only to procure or technically set up cloud services, but to operate them securely: with a clear purpose, approved use, responsibility model, configuration control, monitoring, change assessment, and exit consideration.

## Control objective in repository language

The organization operates a traceable governance routine for cloud services. It knows which cloud services are used, what they are used for, which data and processes are affected, who remains internally responsible, and how risks, configurations, changes, evidence, and exceptions are managed.

## Typical risks

- If cloud services are used without approval or owner, shadow IT, unclear data stores, and unmanaged access arise.
- If the responsibility model is not understood, security tasks remain between provider and organization.
- If cloud configurations are not reviewed, data may unintentionally be public, too broadly accessible, or insufficiently logged.
- If SaaS services do not appear in asset and supplier management, risk and exit decisions are missing.
- If cloud changes by the provider are not assessed, safeguards change unnoticed.

## Triggers

- new cloud service, new tenant, new account, new subscription, or new SaaS use.
- change to data class, user group, interfaces, region, provider function, or admin model.
- cloud misconfiguration, security notification, vulnerability notice, incident, or audit finding.
- contract, architecture, operational, or supplier change.
- introduction of new cloud platform functions, automation, or external integrations.
- regular cloud service, permission, configuration, or cost review.

## Roles and responsibilities

- **Cloud Service Owner / Business function:** is responsible for purpose, business need, data reference, and use.
- **Cloud/platform team:** implements architecture, configuration, monitoring, and technical guardrails.
- **ISMS owner / Security role:** defines minimum requirements, risk logic, and review logic.
- **IT operations / Identity Owner:** manages identities, access, logging, and operational integration.
- **Procurement / Supplier management:** keeps contract, provider, and evidence information up to date.
- **Data protection / Legal:** reviews personal data, contractual, location, subcontractor, and legal issues.
- **Management:** decides on strategic cloud dependencies, residual risks, resources, and exceptions.

## Implementation

### Minimum start

Goal: make permitted cloud use visible, responsible, and reviewable.

1. Cloud services used in the ISMS scope are maintained in a simple cloud service list.
2. Each service receives owner, purpose, user group, data class, and criticality.
3. New cloud services require documented approval before production use.
4. Admin access, external access, and integrations are reviewed separately.
5. At least baseline controls are defined: MFA, role model, logging, backup/export capability, contract contact, review date.
6. Deviations are documented for a limited time and decided risk-based.

Minimum evidence:

- cloud service list with owners,
- approval or onboarding evidence,
- configuration or access evidence for critical services,
- documented exception,
- review note or action log.

### Solid practice

Goal: cloud security is integrated into procurement, architecture, operations, and review.

1. Cloud services are classified by use model, criticality, data reference, and responsibility model.
2. Minimum requirements are defined per service type: identity, access, encryption, logging, backup, interfaces, admin rights, monitoring, incident contact.
3. Cloud onboarding connects procurement, data protection, ISMS, IT, and business function.
4. Configuration reviews check critical settings, public shares, privileged roles, logging, and integrations.
5. Provider changes, new functions, and security notifications are assessed.
6. Results flow into the risk register, action log, supplier review, and management review.

Strong evidence:

- approved cloud service and risk classification,
- documented responsibility model,
- configuration and permission reviews,
- evidence for logging, backup, export, or recovery,
- supplier and contract evidence,
- actions and risk decisions for deviations.

### Advanced practice

Goal: cloud use is managed through guardrails, automation, and a situation picture.

1. Cloud governance is connected with identity management, asset inventory, ticketing, SIEM/monitoring, and vulnerability management.
2. Baselines, landing zones, policy-as-code, or comparable guardrails prevent frequent misconfigurations.
3. Critical deviations create alerts, tickets, or approval workflows.
4. Cloud risks are considered together with cost, dependency, resilience, data flows, and exit capability.
5. Management receives metrics on shadow IT, critical misconfigurations, open cloud exceptions, privileged access, and strategic dependencies.

## Routine flow

1. **Cloud need arises:** business function, IT, or project wants to use or extend a service.
2. **Capture onboarding:** document purpose, data, users, criticality, interfaces, and provider information.
3. **Clarify risk and responsibility:** assess internal tasks, provider services, data risks, and operational risks.
4. **Review minimum requirements:** identity, access, logging, backup, encryption, admin model, incident contact, and exit.
5. **Decide approval or conditions:** allow, limit, rework, or reject production use.
6. **Integrate operations:** include monitoring, review, support, changes, and supplier contact.
7. **Review regularly:** review configuration, access, provider changes, evidence, and open exceptions.
8. **Improve:** feed findings back into baselines, procurement, training, or technical guardrails.

## Decisions

- Which cloud services may be used without central review and which may not?
- Which data classes and processes are permitted for specific cloud services?
- Which security tasks are with the provider and which remain internal?
- Which minimum configurations are required for production use?
- Who may approve admin rights, external shares, or integrations?
- When is an exit plan, backup, second provider, or management decision needed?

## Evidence

### Strong evidence

- cloud service register with owner, purpose, data class, and criticality,
- documented approval with risk and responsibility assessment,
- configuration review of critical settings,
- permission review for admins and external access,
- logging/monitoring/backup evidence,
- action log with validated remediation,
- management decision on exceptions or strategic dependencies.

### Weak evidence

- cloud policy without list of actual services,
- provider certificate without reference to the used service and scope,
- screenshot of individual settings without review decision,
- cost list as a substitute for asset inventory,
- blanket trust in default settings.

### Evidence gaps

- cloud service without owner or approval,
- unknown data class or user group,
- no understanding of the responsibility model,
- missing logging or access evidence,
- open misconfiguration without action,
- no exit or recovery consideration for critical services.

## Effectiveness review

Review questions:

- Are all productively used cloud services in scope recorded?
- Can owners explain which internal security tasks remain despite cloud use?
- Are critical configurations and admin rights reviewed regularly?
- Are new cloud services assessed before use?
- Are provider changes, security notifications, and integrations tracked?
- Is there evidence for backup, export, or recovery where relevant to the service?
- Does management recognize critical cloud dependencies and exceptions?

Possible metrics:

- cloud services with current owner and review,
- unreviewed or unapproved cloud services,
- open critical misconfigurations,
- number of privileged cloud accounts,
- overdue cloud exceptions,
- critical services without exit or recovery evidence.

## BSIG/NIS2 connection point

Cloud security is a connection point for NIS2-oriented topics such as risk management, supply chain security, access protection, incident capability, business continuity, secure procurement, and technical cyber hygiene. The concrete connection should be assessed organization-specifically in the requirements register and risk register.

This artifact does not replace legal, data protection, or contract-law assessment of cloud use.

## Boundaries

- No cloud architecture specification, hardening baseline, or provider recommendation.
- No legal or data protection advice and no statement on the permissibility of concrete data processing.
- No certification, conformity, or security guarantee.
- No use of real tenant, customer, person, or contract data in public examples.
- No replacement for technical cloud security reviews, penetration tests, or incident response.

## Handoffs

- **Procurement/supplier handoff:** new provider, contract change, security evidence, subcontractor, service change.
- **Data protection/legal handoff:** personal data, international references, contractual issues, logging, proximity to data subject or reporting duties.
- **Identity/access handoff:** admin rights, external users, guest access, technical accounts, federation.
- **Architecture/platform handoff:** landing zone, network, encryption, backup, logging, interfaces.
- **Incident handoff:** cloud misconfiguration, compromised account, provider incident, suspected data leakage.
- **BCM handoff:** outage of critical cloud services, recovery, exit, concentration risk.
- **Management handoff:** strategic dependency, residual risk, budget, exception, or provider change.

## Typical mistakes

- Cloud is treated as a pure supplier question, although internal configuration is decisive.
- SaaS services are not maintained as assets and supplier services.
- Default configurations are adopted without review.
- Admin rights and integrations grow without review.
- Logging is activated, but no one evaluates critical events.
- Data protection or Legal are involved only after production use.
- Management sees cloud costs, but not cloud risks and dependencies.

## Fictional mini example

A fictional business function wants to use a new collaboration tool. Before rollout, cloud onboarding is completed: purpose, user group, data class, provider, admin model, and interfaces. The platform team reviews MFA, external shares, and logging. Data protection and Legal clarify points that require review. Use is approved with a condition: external shares only by named owners and review after three months.

Evidence:

- cloud onboarding form,
- approval decision with conditions,
- configuration evidence,
- review date,
- action log for open points.
