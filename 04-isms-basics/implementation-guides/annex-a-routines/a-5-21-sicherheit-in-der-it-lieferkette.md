# A.5.21 — Security in the IT supply chain

## Purpose

IT supply chains consist of software, hardware, cloud services, managed services, libraries, images, updates, integrations, support access, and subcontractors. Security problems do not arise only at the direct supplier, but also through upstream components, build and update paths, or hidden dependencies.

This routine ensures that IT supply chain risks are visible, assessed, contractually and technically managed, and tracked when changes or incidents occur.

## Control objective in repository language

The organization operates a routine for managing security-relevant IT supply chains. It identifies critical IT dependencies, assesses components and providers, tracks vulnerabilities and changes, defines evidence, and connects supplier management, architecture, operations, development, BCM, and incident response.

## Typical risks

- If software components, libraries, or container images are unknown, vulnerabilities cannot be assigned and treated.
- If updates or artifacts are obtained from insecure sources, manipulated components may enter production systems.
- If managed service or cloud dependencies are not understood, subcontractors, support access, and operating locations remain blind spots.
- If hardware, firmware, or appliances are procured without considering security and updates, long-lived technical risks arise.
- If supplier vulnerability notifications are not processed, affected products or services remain unpatched.
- If exit and substitution capability are missing, a supply chain disruption quickly becomes an availability or crisis issue.

## Triggers

- new software, library, platform, cloud service, hardware, appliance, managed service, or integration component.
- change to version, source, build pipeline, update channel, subcontractor, or operating model.
- vulnerability notification, manufacturer notice, security advisory, compromised provider, or incident.
- procurement, architecture decision, make-or-buy decision, or contract renewal.
- release, deployment, larger migration, or technical standardization.
- audit finding, penetration test, dependency scan, or SBOM/inventory finding.
- BCM review, crisis exercise, or management question about critical IT dependencies.

## Roles and responsibilities

- **IT/platform owner:** is responsible for platforms, components, update channels, and technical operating risks in use.
- **Development / Product Owner:** is responsible for software dependencies, libraries, containers, CI/CD, and release decisions.
- **Architecture role:** assesses strategic dependencies, standardization, substitution capability, and technical debt.
- **Procurement / Vendor Management:** connects IT supply chain requirements with the supplier register and agreements.
- **ISMS owner / Security role:** defines assessment logic, vulnerability handoff, evidence, exceptions, and reporting.
- **BCM/crisis role:** assesses availability and recovery risks of critical IT dependencies.
- **Data protection / Legal:** reviews personal data, contractual issues, subcontractors, and legal risks.
- **Management:** decides on critical dependencies, non-substitutable components, resource needs, or accepted residual risk.

## Implementation

### Minimum start

Goal: make the most critical IT supply chain dependencies visible and response-capable.

1. The organization identifies critical IT services, central software products, cloud/managed services, and internet-facing components in scope.
2. For each critical dependency, owner, supplier, purpose, data/system reference, update path, and contact are recorded.
3. Vulnerability and manufacturer notifications for critical components are subscribed to or required via service providers.
4. New critical components are briefly assessed before use: source, support status, update capability, access, subcontractors, and exit relevance.
5. Open vulnerabilities, insecure update paths, or non-substitutable components are maintained in the action or risk register.
6. In supply chain incidents, there is an incident handoff and a list of potentially affected services.

Minimum evidence:

- register of critical IT dependencies,
- owner and contact per dependency,
- evidence of vulnerability/manufacturer information,
- assessment note for new critical components,
- action or risk entry for open supply chain risks.

### Solid practice

Goal: IT supply chain risks are integrated into architecture, procurement, development, and operations.

1. IT dependencies are classified by criticality: production-critical, internet-exposed, identity-related, data-intensive, hard to replace, or privileged.
2. Software and component inventories are built risk-based: products, versions, libraries, containers, images, appliances, firmware, and SaaS services.
3. Source and update paths are defined: trusted sources, signatures, repositories, approvals, test and rollback procedures.
4. Vulnerability management connects supplier notifications, dependency scans, manufacturer notices, and asset references.
5. Agreements with suppliers address security requirements from A.5.20: notifications, evidence, subcontractors, changes, support, and exit.
6. Critical dependencies are made visible in BCM, emergency planning, and management review.
7. Exceptions such as unsupported software, unpatchable appliances, or missing SBOM are time-limited and risk-assessed.

Strong evidence:

- IT dependency or component register,
- assessment logic for criticality and supply chain risks,
- evidence for update and source paths,
- vulnerability and advisory tickets with asset reference,
- supplier requirements or contract references,
- BCM/exit consideration for critical dependencies,
- exception decisions with expiry date.

### Advanced practice

Goal: IT supply chains are continuously monitored and embedded in secure development, platform operations, and resilience management.

1. SBOM, dependency scanning, container scanning, artifact repositories, CMDB, and ticketing are integrated.
2. Build and release pipelines check origin, integrity, signatures, policies, and known vulnerabilities automatically or semi-automatically.
3. Critical cloud, SaaS, and managed service dependencies are tracked with subcontractor, location, support, and exit information.
4. Supply chain events create situation pictures: affected assets, services, customer processes, vulnerability status, and communication needs.
5. Technical standards reduce dependencies on unsupported components, uncontrolled repositories, or individual exceptions.
6. Management sees concentration risks, non-substitutable components, supplier dependencies, technical debt, and investment needs.

## Routine flow

1. **Dependency arises or changes:** new component, supplier, version, update path, cloud service, or build step.
2. **Classify:** assess criticality, data reference, exposure, privileges, support status, subcontractors, and substitutability.
3. **Define owner:** assign business, technical, and supplier responsibility.
4. **Review evidence and requirements:** assess security information, support, update capability, vulnerability communication, agreements, and source path.
5. **Decide approval or exception:** use, sharpen requirements, compensate, time-limit, escalate, or reject.
6. **Monitor operations:** track advisories, scans, versions, updates, subcontractor changes, and open actions.
7. **Treat vulnerabilities:** connect findings with A.8.8, prioritize, patch, compensate, or escalate.
8. **Trigger incident handoff:** for compromised supply chain, active exploitation, or possible impact on critical services.
9. **Improve:** adapt architecture standards, procurement criteria, CI/CD rules, supplier requirements, or exit plans.

## Decisions

- Which IT dependencies are critical enough for an in-depth supply chain review?
- Which components must be inventoried or supported with SBOM/dependency information?
- Which sources, repositories, and update paths are allowed?
- When may unsupported or hard-to-patch technology continue to operate?
- Which vulnerability or supplier notifications trigger incident triage?
- Which supplier requirements belong in agreements?
- Which dependencies need exit, substitution, or emergency planning?

## Evidence

### Strong evidence

- current register of critical IT dependencies with owner, version/service, supplier, and criticality,
- component, SBOM, dependency, or asset information for relevant systems,
- documented assessment of new critical components,
- evidence of approved source and update paths,
- advisory, scan, or vulnerability tickets with treatment,
- supplier agreements or requirement references,
- BCM/exit assessments for critical dependencies,
- management decision for unacceptable or not quickly remediable risks.

### Weak evidence

- software list without version, owner, or place of use,
- supplier certificate without reference to the concrete component,
- dependency scan without triage or asset reference,
- generic statement “updates come from the manufacturer” without process evidence,
- architecture decision without consideration of support, exit, or source path.

### Evidence gaps

- critical components without owner,
- unknown versions or build artifacts,
- no processing of manufacturer or supplier notifications,
- insecure or undocumented repositories,
- unsupported technology without risk decision,
- subcontractors and managed service dependencies unknown,
- no incident handoff in case of supply chain suspicion.

## Effectiveness review

Review questions:

- Are the most important IT supply chain dependencies known and owned?
- Can critical components be assigned to affected services and owners?
- Are new or changed components assessed before production use?
- Are source and update paths sufficiently managed?
- Are supplier and manufacturer notices transferred into vulnerability management?
- Are unsupported or hard-to-replace components visible as risks?
- Are critical dependencies included in BCM, exit planning, and management review?

Possible metrics:

- share of critical services with documented IT dependencies,
- components without owner or version,
- open supply chain vulnerabilities by criticality,
- unsupported components in scope,
- overdue updates or advisories,
- critical dependencies without exit assessment,
- supply chain events with completed impact analysis.

## BSIG/NIS2 connection point

Security in the IT supply chain is a connection point for NIS2-oriented topics such as supply chain security, secure procurement and development, vulnerability management, cyber hygiene, business continuity, incident capability, and governance over essential technical dependencies.

For BSIG/NIS2 impact, the organization should assess in the requirements register which IT dependencies, supplier classes, evidence, and management decisions are relevant. This artifact does not replace legal interpretation, contract review, or a binding assessment of applicability.

## Boundaries

- This artifact is not a complete secure supply chain architecture and not a tool recommendation.
- It does not replace technical product review, code analysis, hardware review, or cloud security assessment.
- SBOM, scanners, or certificates do not replace an organization-specific risk decision.
- No legal advice, no data protection advice, no certification commitment.
- No ISO 27002 texts and no real supplier, component, vulnerability, or customer data in examples.

## Handoffs

- **Procurement/vendor handoff:** new IT suppliers, support status, requirements, evidence, and contract references.
- **Architecture handoff:** platform decisions, standardization, substitution capability, technical debt, and concentration risks.
- **Development/DevOps handoff:** dependencies, SBOM, CI/CD, artifact sources, containers, build and release rules.
- **IT operations handoff:** updates, firmware, appliances, cloud services, managed services, and monitoring.
- **Vulnerability handoff:** advisories, dependency findings, manufacturer notices, and active exploitation.
- **Incident handoff:** compromised provider, manipulated component, suspicious update, or possible impact on critical services.
- **BCM/crisis handoff:** non-substitutable components, critical outages, exit scenarios, and emergency operation.
- **Data protection/legal handoff:** personal data, subcontractors, contractual issues, or information duties.
- **Management handoff:** unsupported technology, critical dependency, resource needs, accepted residual risk, or strategic change.

## Typical mistakes

- Supply chain is understood only as a supplier list, not as component, update, and build dependency.
- Dependency scans run, but findings are not assigned to a service owner.
- Critical appliances or firmware are forgotten in the vulnerability process.
- Updates are obtained from convenient sources without checking origin and integrity.
- Unsupported software remains in production because it is not visible in the business process.
- Subcontractors and managed service dependencies are kept only in data protection lists, but are not technically assessed.
- Management sees individual vulnerabilities, but no concentration or exit risks.

## Fictional mini example

A fictional platform operator uses an open-source library in a customer portal. A dependency scan reports a critical vulnerability. The Product Owner assigns the library to the portal, and the platform owner checks exposure and update capability. The update is tested and rolled out through the CI/CD pipeline. In parallel, the team notices that no owners are recorded in the component register for two other critical libraries. This gap becomes an action for the next architecture review.

Evidence:

- dependency finding with component reference,
- assignment to the customer portal,
- update and test ticket,
- release evidence,
- component register gap,
- action for architecture review.
