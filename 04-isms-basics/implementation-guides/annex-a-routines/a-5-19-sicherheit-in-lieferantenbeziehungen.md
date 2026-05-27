# A.5.19 — Security in supplier relationships

## Purpose

Supplier relationships create security dependencies: external services process information, operate systems, deliver software, have access to environments, or influence the availability of critical processes. This routine ensures that such relationships are not only procured, but selected, operated, reviewed, and ended based on risk.

The core is supplier governance that keeps security risks visible before, during, and after collaboration: who is critical? Which access, data, and services are affected? Which evidence exists? Which issues are escalated?

## Control objective in repository language

The organization operates a traceable routine for security steering of suppliers and service providers. It connects procurement, business responsibility, information security, data protection, legal, operations, and management into a shared handling of supplier risks.

## Typical risks

- If a service provider receives access to systems or data without risk-based assessment, unrecognized attack and dependency surfaces arise.
- If critical suppliers are not inventoried, owners, review dates, and escalation paths are missing.
- If security requirements are clarified only after contract signing, renegotiation is difficult or expensive.
- If performance or security issues do not feed into reviews, the actual supplier situation remains invisible.
- If subcontractors or cloud dependencies are not considered, blind spots arise in the supply chain.
- If offboarding is missing, access, data copies, or interfaces remain active after contract end.

## Triggers

- New supplier, new service, proof of concept, tender, or contract renewal.
- Change to service scope, data types, system access, location, subcontractor, or operating model.
- Security event, vulnerability, outage, service issue, or audit finding at the supplier.
- Periodic supplier review or management question on critical dependencies.
- Changed risk situation, new regulatory affectedness, or new protection need.
- Termination, cancellation, migration, or supplier change.
- External request, customer requirement, or internal review of supplier steering.

## Roles and responsibilities

- **Service owner / Business responsible role:** assesses business need, criticality, and performance expectation.
- **Procurement / Vendor management:** steers selection, register, commercial coordination, and supplier communication.
- **ISMS owner / Security role:** defines security assessment, minimum evidence, review logic, and risk handling.
- **IT/platform owner:** assesses technical integration, access, interfaces, operations, and offboarding.
- **Data protection / Legal:** assesses personal data, contractual questions, data protection roles, clauses, and legal risks.
- **BCM/crisis role:** assesses dependencies for critical processes and emergency capability.
- **Management:** decides on critical suppliers, accepted residual risks, budget, alternatives, and escalations.

## Implementation

### Minimum start

Goal: make critical suppliers visible, owned, and reviewable.

1. The organization creates a supplier register for security-relevant services: name, service, owner, data/system reference, criticality, review date.
2. New suppliers are briefly assessed before approval: which data, access, services, locations, and dependencies are affected?
3. Critical suppliers receive a named service owner and a security contact.
4. Minimum evidence is requested or replaced with justification: security description, certificate/audit evidence, questionnaire, contractual annex, or technical description.
5. Open risks are managed in the action or risk register.
6. Contract end or service provider change triggers offboarding of access, data, and interfaces.

Minimum evidence:

- supplier register with criticality and owner,
- simple security assessment before use,
- evidence of requested or assessed security information,
- risk or action log,
- offboarding check at the end of the relationship.

### Solid practice

Goal: supplier steering is integrated into procurement and operations based on risk.

1. Suppliers are classified by criticality: access to information, system access, availability relevance, subcontractors, recoverability.
2. Procurement starts security, data protection, and legal handoffs early enough before contract signing.
3. Critical suppliers are reviewed regularly: performance, security events, evidence, open actions, subcontractor changes, exit capability.
4. Security requirements are transferred into supplier agreements with A.5.20.
5. IT supply chain risks such as software, cloud, managed services, or updates are connected with A.5.21.
6. Supplier events feed into incident response, vulnerability management, BCM, and management review.
7. Exceptions receive duration, compensating measures, and a decision by the appropriate role.

Strong evidence:

- risk-based supplier register,
- assessment form or due diligence note,
- review records for critical suppliers,
- open actions and escalations,
- offboarding or exit evidence,
- management decision for critical dependency or residual risk.

### Advanced practice

Goal: supplier relationships are operated as ongoing dependency and risk management.

1. Supplier register, asset register, contract management, BCM, and risk analysis are connected.
2. Critical suppliers receive defined security and resilience metrics, review calendars, and escalation paths.
3. Subcontractors, concentration risks, regional dependencies, and exit scenarios are reviewed regularly.
4. Security events, vulnerability reports, and performance issues are transferred into joint improvement plans.
5. Management sees decision-ready information: critical dependencies, unmet requirements, exit risks, open exceptions, and resource needs.
6. Supplier change, emergency operation, or exit is exercised for critical services or at least tested in tabletop form.

## Routine flow

1. **Need arises:** business unit, IT, or project wants to use or change a supplier.
2. **Perform preliminary check:** capture data, access, criticality, subcontractors, availability, and exit relevance.
3. **Classify criticality:** standard supplier, security-relevant, critical, or strategically dependent.
4. **Trigger handoffs:** involve security, data protection, legal, IT, BCM, and procurement depending on risk.
5. **Assess evidence:** review questionnaire, certificates, security concept, technical description, audit report, or alternative evidence.
6. **Decide:** approve, sharpen requirements, time-limit exception, obtain management decision, or stop use.
7. **Operate and review:** regularly check performance, security events, changes, evidence, and open actions.
8. **Steer changes:** reassess new access, data types, subcontractors, or locations.
9. **End:** withdraw access, track data return/deletion, deactivate interfaces, and document lessons learned.

## Decisions

- Which suppliers are security-relevant or critical?
- Which minimum information must be available before use?
- When may a supplier start despite open security questions?
- Who accepts supplier risks and for what period?
- Which suppliers need regular reviews or management visibility?
- Which exit or replacement options are required for critical services?
- How are subcontractor changes and security events handled?

## Evidence

### Strong evidence

- current supplier register with owner, criticality, data/system reference, and review date,
- documented security assessment before use,
- reviewed supplier evidence or justified replacement assessment,
- review records with measures and decisions,
- evidence of offboarding, access withdrawal, and data/interface handling,
- escalations and management decisions for critical dependencies,
- link to risk, action, incident, or BCM register.

### Weak evidence

- pure creditor list without security reference,
- supplier certificate without scope check,
- questionnaire without assessment or measures,
- contract in the archive without responsible service owner,
- supplier review as procurement routine without security or availability questions.

### Evidence gaps

- critical SaaS or managed service suppliers missing from the register,
- no owner for supplier risk,
- no assessment before production use,
- subcontractors unknown or not tracked,
- contract end without evidence of access withdrawal and data handling,
- open security requirements without escalation.

## Effectiveness review

Review questions:

- Are security-relevant and critical suppliers identified completely enough?
- Is it clear for every critical supplier which service, data, and access are affected?
- Are security, data protection, legal, and BCM handoffs triggered before relevant decisions?
- Do reviews lead to measures, escalations, or conscious risk decisions?
- Are supplier changes and subcontractor changes reassessed?
- Is offboarding at contract end evidenced?
- Does management recognize critical dependencies and exit risks?

Possible metrics:

- share of critical suppliers with current review,
- suppliers without owner or criticality,
- open actions per critical supplier,
- overdue evidence or reviews,
- security events with supplier reference,
- open offboarding items after contract end,
- critical suppliers without documented exit consideration.

## BSIG/NIS2 connection point

Security in supplier relationships is compatible with NIS2-oriented topics such as supply chain security, risk management, service provider steering, business continuity, incident capability, and management oversight of essential dependencies.

For BSIG/NIS2 affectedness, the organization should assess in the requirements register which suppliers, services, evidence, and management decisions are relevant. This artifact does not replace legal interpretation, contract advice, or a binding assessment of applicability.

## Boundaries

- This artifact is not a contract template and not legal advice.
- It does not replace a data protection review, processor assessment, or negotiation by qualified roles.
- It does not state that a certificate or questionnaire proves sufficient security.
- No certification, conformity, or security guarantee.
- No ISO 27002 text and no real supplier, customer, or contract data in examples.

## Handoffs

- **Procurement/vendor management handoff:** selection, register, supplier communication, contract renewal, and termination.
- **Legal/data protection handoff:** contract design, personal data, data protection roles, reporting and information obligations.
- **Security/ISMS handoff:** security assessment, evidence, exceptions, risk register, and review logic.
- **IT/access handoff:** technical integration, interfaces, admin access, external accounts, and offboarding.
- **BCM/crisis handoff:** critical dependencies, outage risks, exit scenarios, and emergency operation.
- **Incident handoff:** security events, vulnerability reports, or outages with supplier reference.
- **Management handoff:** critical dependency, unmet requirements, residual risk, budget, or exit decision.
- **Audit/evidence handoff:** missing evidence, unclear scope check, or undocumented reviews.

## Typical mistakes

- Supplier steering starts only after the contract has been signed.
- A creditor list is confused with a security register.
- Certificates are collected, but their scope is not checked against the service used.
- Critical suppliers have no business owner.
- Subcontractors and cloud dependencies remain outside consideration.
- Security problems are treated as pure service quality and not transferred into risk management.
- Offboarding focuses on contract end but forgets access, data copies, and interfaces.

## Fictional mini example

A fictional mid-sized company wants to use a new SaaS tool for customer communication. The business unit reports the need to procurement and the ISMS owner. The preliminary check shows personal data, external accounts, and dependency in the support process. The supplier is classified as security-relevant. Before start, security information is assessed, data protection and legal are involved, and open points are transferred into a contractual annex. After six months, the service owner reviews use, open actions, and subcontractor notices.

Evidence:

- supplier register entry with criticality,
- security preliminary check,
- evidence and assessment note,
- data protection/legal handoff,
- action log,
- review record after six months.
