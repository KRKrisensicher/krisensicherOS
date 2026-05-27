# A.5.30 — ICT readiness for continuity

## Purpose

ICT readiness for continuity ensures that digital services, infrastructure, data, identities, and operational capabilities are prepared for outages. The goal is not an attractive emergency manual, but a verifiable connection between business requirements, technical recovery capabilities, exercises, decisions, and improvements.

## Control objective in repository language

The organization operates a routine through which critical ICT services for continuity are planned, prepared, tested, reviewed, and improved. Requirements from business processes, BCM, risk analysis, supplier control, and IT operations are translated into concrete restart and minimum operating capabilities.

## Typical risks

- If critical services are not prioritized, the wrong systems are restored first during an outage.
- If recovery objectives are not aligned with technical capabilities, unrealistic expectations arise.
- If backups are never tested, recovery in a real case is uncertain.
- If dependencies on identity, network, cloud, DNS, suppliers, or key people are missing, restart fails because of secondary systems.
- If emergency exercises take place only on paper, technical and organizational gaps remain hidden.
- If security requirements are ignored during restart, compromised or incomplete systems can become productive.

## Triggers

- new or changed critical business processes, services, systems, or data stores.
- business impact analysis, risk analysis, BCM review, or management decision.
- major architecture, cloud, network, backup, or supplier change.
- outage, security incident, recovery test, or crisis exercise.
- audit finding or internal review on continuity, backup, or restart.
- new dependency on SaaS, managed service, platform, or location.
- periodic review of restart objectives and test evidence.

## Roles and responsibilities

- **BCM Owner / Process Owner:** defines critical business processes, priorities, and tolerable interruptions.
- **Service Owner / Asset Owner:** translates business requirements into service requirements and accepts open gaps or escalates them.
- **IT operations / platform team:** plans and operates backup, recovery, redundancy, monitoring, and technical emergency procedures.
- **ISMS owner / Security role:** reviews security requirements in emergency operations and restart.
- **Supplier management:** clarifies continuity commitments, contact paths, and dependencies of external services.
- **Management:** decides conflicting objectives between cost, restart time, residual risk, and service priority.
- **Business functions:** test work capability in emergency or restart operations.

## Implementation

### Minimum start

Goal: know the most important ICT services and check their recoverability at a basic level.

1. Name the most important business processes and associated ICT services in scope.
2. For each critical service, record owner, technical responsible persons, and central dependencies.
3. Document simple restart objectives: priority, tolerable interruption, required data currency, minimum operations.
4. Collect backup and recovery evidence for critical data or systems.
5. Conduct at least one recovery test or tabletop for a critical service.
6. Document gaps as actions with owner, deadline, and management handoff.

Minimum evidence:

- list of critical ICT services with owners,
- dependency overview,
- restart requirements,
- backup/restore test evidence,
- action log for continuity gaps.

### Solid practice

Goal: continuity requirements are aligned, tested, and embedded in operating routines.

1. Business impact requirements are aligned with technical recovery capabilities.
2. Critical dependencies are considered: identity, network, DNS, certificates, keys, monitoring, admin access, service providers, locations.
3. Recovery plans contain sequence, roles, communication paths, security checks, and fallback options.
4. Restore tests check not only individual files, but service capability and data integrity.
5. Suppliers are included in continuity reviews when they support critical services.
6. Deviations between requirement and capability lead to a risk decision, action, or management prioritization.

### Advanced practice

Goal: ICT continuity is resilient, exercised, and integrated into architecture decisions.

1. Critical services have graduated restart concepts with technical tests and business acceptance.
2. Scenarios such as ransomware, cloud outage, site loss, identity outage, and supplier outage are exercised.
3. Automated monitoring checks backup success, replication, key dependencies, and restart readiness.
4. Architecture decisions consider resilience, recoverability, portability, and security controls.
5. Continuity metrics flow into management review, investment planning, and risk treatment.
6. Lessons learned from disruptions and exercises improve technology, contracts, processes, and crisis routines.

## Routine flow

1. **Determine criticality:** classify business process, service, data, user groups, and impact.
2. **Define requirements:** describe restart priority, tolerable interruption, data currency, minimum operations, and security requirements.
3. **Record dependencies:** capture technical, organizational, and supplier-related prerequisites.
4. **Check capability:** assess backup, restore, redundancy, emergency access, monitoring, and staff availability.
5. **Update planning:** define recovery sequence, roles, checklists, contacts, and security checkpoints.
6. **Test or exercise:** technically, functionally, or as a tabletop; document result and gaps.
7. **Decide:** prioritize gaps, accept residual risks, or fund actions.
8. **Improve:** implement technical, contractual, or organizational actions and review again.

## Decisions

- Which ICT services are critical for business operations and security capability?
- Which restart objectives are realistic and financially viable?
- Which data losses or interruptions would not be acceptable?
- Which services need technical redundancy, and which can be restored manually or with a time delay?
- Which security checks are mandatory before recommissioning?
- Which supplier dependencies need contract adjustment or exit/fallback planning?
- Which continuity gaps does management consciously accept?

## Evidence

### Strong evidence

- critical service catalog with owners and dependencies,
- aligned restart requirements,
- recovery plan with roles and security checks,
- backup and restore test protocols,
- business acceptance of a recovery test,
- action log for continuity gaps,
- management decision on residual risk, investment, or prioritization.

### Weak evidence

- backup policy without restore evidence,
- system list without business process reference,
- emergency plan without test date,
- technical redundancy claim without outage or failover evidence,
- supplier commitment without service reference or review.

### Evidence gaps

- no owners for critical services,
- unclear dependency on identity, network, cloud, or service providers,
- restart objectives were never aligned with business functions,
- backups exist, but recovery was not tested,
- security review before restart is missing,
- continuity gaps without management decision.

## Effectiveness review

Review questions:

- Are critical ICT services and dependencies currently known?
- Do technical recovery capabilities fit business requirements?
- Are there current restore or restart tests for critical services?
- Are security requirements checked during restart?
- Are supplier dependencies considered in continuity planning and exercises?
- Do test gaps lead to actions, risk decisions, or investment decisions?

Possible metrics:

- share of critical services with current restart plan,
- share of critical services with successful restore test,
- open continuity gaps by criticality,
- deviation between required and tested restart,
- overdue tests or reviews,
- critical suppliers without reviewed continuity commitments.

## BSIG/NIS2 connection point

ICT readiness for continuity is compatible with NIS2-oriented topics such as business continuity, backup and recovery capability, crisis management, risk management, supply-chain security, and maintenance of essential services.

For affected organizations, the concrete connection point should be assessed in the requirements register, in BCM records, and in management review. This artifact does not replace legal assessment of affectedness, requirements, or evidence obligations.

## Boundaries

- This artifact is not a complete business continuity plan and not a technical high-availability design.
- It does not replace architecture, cloud, network, or backup specialist planning.
- It does not guarantee availability, recoverability, or conformity.
- It makes no legal or data protection assessment.
- Public examples use no real organizational or system data.

## Handoffs

- **BCM handoff:** business impact requirements, restart priorities, exercises, and crisis roles.
- **IT operations handoff:** backup, restore, redundancy, monitoring, emergency access, technical runbooks.
- **Security/ISMS handoff:** security checks, integrity, access protection, emergency operations, and risk acceptance.
- **Supplier handoff:** SaaS, managed services, cloud, support hours, continuity commitments, and exit/fallback questions.
- **Management handoff:** investments, conflicting objectives, unachievable restart objectives, and accepted residual risks.
- **Audit/evidence handoff:** test protocols, acceptances, actions, and review evidence.

## Typical mistakes

- Backups are confused with recovery capability.
- Critical dependencies such as IAM, DNS, certificates, or admin access are missing from plans.
- Business functions do not know restart objectives or have never confirmed them.
- Tests check only technology, but not business work capability.
- Security checks are skipped because of time pressure.
- Supplier promises are not aligned with own restart requirements.
- Management sees costs, but not the accepted outage and restart risk.

## Fictional mini example

A fictional logistics service provider identifies the shipping portal as a critical ICT service. The Service Owner documents dependencies on identity service, database, DNS, and a SaaS service. A restore test shows that the database can be recovered, but the identity service has no tested emergency procedure. Management decides to fund an emergency procedure for privileged access and an annual combined restart test.

Evidence:

- critical service entry with dependencies,
- restart requirements,
- restore test protocol,
- identified gap in the identity service,
- management decision on the action,
- date for combined restart test.
