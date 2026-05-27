# A.5.20 — Security requirements in supplier agreements

## Purpose

Security requirements for suppliers must be translated into agreements early and concretely enough that they can be steered in operations. Without a clear agreement, access protection, reporting paths, evidence, subcontractors, vulnerability handling, data return, or exit capability often remain non-binding expectations.

This routine ensures that security requirements are derived from risk, protection need, and operational reality, made negotiable with procurement/legal, and reviewed during the contract term.

## Control objective in repository language

The organization operates a routine by which security-relevant requirements for suppliers are identified before contract conclusion or change, introduced into suitable agreements, decided in case of exceptions, and followed up during ongoing operations.

## Typical risks

- If security requirements are not contractually or bindingly agreed, enforcement, evidence, and escalation paths are missing.
- If requirements are too generic, they do not fit the concrete service, data scope, or access.
- If reporting paths, deadlines, and contacts are missing, responses to security events are delayed.
- If subcontractors, locations, or technical changes are not regulated, the risk changes unnoticed.
- If exit, data return, deletion, or access withdrawal are not agreed, risks arise at the end of collaboration.
- If supplier requirements are formulated only by security but are not connectable legally, commercially, and operationally, they remain ineffective.

## Triggers

- New supplier, new agreement, tender, proof of concept, or contract renewal.
- Change to data types, protection need, access, subcontractors, operating model, or locations.
- Security event, vulnerability report, performance issue, or audit finding with supplier reference.
- New internal security requirement, risk decision, or management requirement.
- Review of critical supplier agreements.
- Planned exit, cancellation, migration, or service provider change.
- External customer requirement or regulatory mapping need that requires human review.

## Roles and responsibilities

- **Service owner / Business responsible role:** describes service, data, processes, criticality, and operational requirements.
- **Procurement / Vendor management:** coordinates negotiation, supplier communication, contract portfolio, and follow-ups.
- **Legal:** translates requirements into suitable contract or agreement logic and assesses legal risks.
- **Data protection:** assesses personal data, data protection roles, and required data protection agreements.
- **ISMS owner / Security role:** defines security requirements, evidence expectations, exceptions, and review points.
- **IT/platform owner:** assesses technical requirements for access, interfaces, logging, vulnerabilities, and operations.
- **BCM/crisis role:** adds requirements for availability, recovery, crisis communication, and exit.
- **Management:** decides on deviations from minimum requirements, critical residual risks, or commercial target conflicts.

## Implementation

### Minimum start

Goal: security-relevant agreements contain the most important operational expectations.

1. Before contract conclusion or material change, the supplier is classified by criticality and security relevance.
2. For security-relevant suppliers, a short requirements list is created: data, access, evidence, reporting path, subcontractors, exit.
3. Procurement, legal, data protection, and security review the requirements before approval.
4. Unmet requirements are documented as exceptions with risk, runtime, and decision-maker.
5. Agreed security requirements are referenced in the supplier register.
6. Contract end triggers review of access withdrawal, data return/deletion, and interface deactivation.

Minimum evidence:

- security requirements list for each critical supplier,
- handoff evidence to procurement/legal/data protection/security,
- agreement reference or contractual annex,
- exception decision in case of deviation,
- offboarding or exit requirement.

### Solid practice

Goal: requirements are risk-based, negotiable, and verifiable.

1. The organization uses requirement catalogs by supplier type: SaaS, managed service, software supplier, consultant with access, hosting, maintenance, hardware/IT components.
2. Requirements are derived from risk analysis, protection need, data class, access type, availability need, and supply chain dependency.
3. Agreements address at least: security contact, incident communication, access protection, evidence, vulnerabilities, changes, subcontractors, availability, data handling, offboarding, and audit/review capability in appropriate form.
4. Deviations are not accepted informally, but documented as a risk decision.
5. Review dates check whether evidence, reports, changes, and open actions fit the agreement.
6. Requirements from A.5.19 and A.5.21 are connected consistently with supplier steering and the IT supply chain.

Strong evidence:

- risk-based requirements catalog,
- contract or agreement reference with security connection,
- documented deviations and risk decisions,
- review records on evidence and open obligations,
- change or subcontractor notices with assessment,
- exit checklist or offboarding evidence.

### Advanced practice

Goal: security requirements are steered across portfolio, contract lifecycle, and management decisions.

1. Contract management, supplier register, risk register, and review calendar are connected.
2. Critical requirements have owner, evidence frequency, escalation path, and measurable status.
3. Contract changes, subcontractor changes, security events, and material technical changes create automatic or binding review triggers.
4. Standard clauses and playbooks are regularly improved based on incidents, audits, exit experience, and market changes.
5. Management sees deviations from minimum requirements, critical suppliers without suitable agreements, and cost/risk conflicts.
6. For critical services, exit, emergency, and communication requirements are tested together with BCM and the crisis team, or reviewed in tabletop form.

## Routine flow

1. **Supplier need arises:** new service, contract change, renewal, or new access.
2. **Create security profile:** capture service, data, access, criticality, availability, subcontractors, and exit relevance.
3. **Derive requirements:** select suitable security, evidence, reporting, change, offboarding, and BCM requirements.
4. **Check handoffs:** involve procurement, legal, data protection, security, IT, and BCM depending on profile.
5. **Negotiate or document agreement:** transfer requirements into contract, annex, statement of work, security concept, or binding operating rule.
6. **Decide deviations:** assess unmet points, compensate, time-limit, or escalate to management.
7. **Monitor operations:** track evidence, reports, changes, and measures in supplier review.
8. **Assess changes:** new subcontractors, locations, access paths, or data types trigger renewed review.
9. **End:** evidence exit, deletion, return, interface, and access withdrawal requirements.

## Decisions

- Which suppliers need which security requirements?
- Which minimum requirements are non-negotiable and which can be adjusted based on risk?
- Which evidence is sufficient and how often must it be updated?
- Who accepts deviations from requirements?
- Which events must the supplier report and through which channel?
- Which subcontractor or change information must be assessed in advance?
- Which exit and data-handling requirements are necessary for critical services?

## Evidence

### Strong evidence

- supplier security profile with data, access, and criticality reference,
- requirements catalog or contract checklist,
- contractual annex, statement of work, or agreement reference with security connection,
- documented legal/data protection/security review,
- deviation and exception decisions with runtime,
- evidence from ongoing reviews,
- exit and offboarding evidence.

### Weak evidence

- blanket security clause without service reference,
- standard contract without review of the concrete data or access scope,
- supplier certificate without connection to the agreement,
- oral supplier assurance without evidence,
- checklist without decision in case of deviations.

### Evidence gaps

- critical supplier without documented security requirements,
- contract change without security review,
- no rule for security events or contacts,
- subcontractors or locations unknown,
- deviations not risk-assessed,
- contract end without data, access, or interface evidence.

## Effectiveness review

Review questions:

- Were security requirements introduced before contract conclusion or change?
- Do requirements fit the concrete service, protection need, and access?
- Are deviations visible, time-limited, and decided?
- Are agreed evidence and reports checked during operations?
- Are subcontractor, change, and incident communication sufficiently steerable?
- Are exit, data return/deletion, and access withdrawal regulated with evidence?
- Does management recognize critical agreement gaps and target conflicts?

Possible metrics:

- share of critical suppliers with documented security requirements,
- open contract gaps by criticality,
- overdue evidence or reviews,
- number and age of deviations,
- supplier changes with security review,
- offboarding evidence at contract end,
- critical suppliers without exit regulation.

## BSIG/NIS2 connection point

Security requirements in supplier agreements are compatible with NIS2-oriented topics such as supply chain security, service provider steering, risk management, incident communication, business continuity, access protection, and evidence capability.

For BSIG/NIS2 affectedness, the organization should assess in the requirements register which agreements, supplier classes, and evidence are relevant. This artifact does not replace legal advice, contract review, or binding interpretation of applicability.

## Boundaries

- This artifact is not a contract template and does not replace legal review.
- It defines no universal mandatory clauses; requirements must be derived in relation to the organization and service.
- It does not replace a data protection review or data processing agreement.
- No certification, conformity, or security guarantee.
- No ISO 27002 text and no real contract, supplier, or customer data in examples.

## Handoffs

- **Procurement/vendor management handoff:** negotiation, contract reference, supplier communication, deadlines, and renewals.
- **Legal handoff:** contract design, liability/evidence mechanics, termination, audit/review rights, and legal risks.
- **Data protection handoff:** personal data, role clarification, data processing, deletion, transfer, and data-subject risks.
- **Security/ISMS handoff:** security requirements, evidence, exceptions, risk register, and review frequency.
- **IT/access handoff:** technical access, interfaces, logging, vulnerabilities, certificates, and offboarding.
- **BCM/crisis handoff:** availability, restart, emergency communication, exit, and replacement operation.
- **Management handoff:** material deviations, residual risk, budget conflicts, or decision against minimum requirements.
- **Audit/evidence handoff:** missing agreement reference, unreviewed deviations, or incomplete review evidence.

## Typical mistakes

- Security is involved only when the contract is already ready for signature.
- Requirements are copied from a generic clause collection and not related to the service.
- Deviations are accepted commercially, but not documented as a risk decision.
- Agreements contain reporting obligations, but no contacts or processes.
- Subcontractor changes are not tracked.
- Exit is considered only at termination.
- Evidence is collected annually, but not assessed or linked with measures.

## Fictional mini example

A fictional IT operation awards operation of a monitoring service to a managed service provider. The preliminary check shows access to infrastructure metadata and alerting paths. Security and IT formulate requirements for admin access, MFA, security contact, vulnerability reports, and offboarding. Legal transfers them into a contractual annex. The provider cannot meet one evidence frequency; the service owner documents a time-limited exception with an additional quarterly meeting. After contract start, evidence status is checked in the supplier review.

Evidence:

- security profile of the managed service,
- requirements list,
- contractual annex reference,
- legal/security handoff,
- exception decision,
- review record on evidence status.
