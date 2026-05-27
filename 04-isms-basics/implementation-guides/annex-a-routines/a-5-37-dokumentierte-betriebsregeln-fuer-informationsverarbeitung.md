# A.5.37 — Documented operating rules for information processing

## Purpose

Documented operating rules ensure that information processing does not depend on tacit experiential knowledge, individual key people, or improvised ways of working. They describe how systems, data, services, and recurring operating tasks are run securely and traceably.

The core is not a manual on a shelf, but usable operating logic: Which activities must be carried out how, who may deviate, when is escalation required, and which evidence emerges in everyday work?

## Control objective in repository language

The organisation operates a current, understandable, and role-based set of operating rules for relevant information processing. These rules connect technical processes, responsibilities, protection needs, changes, exceptions, emergency relevance, and review.

## Typical risks

- If critical operating processes are known only to individual people, outages, user errors, and absence-related dependencies arise.
- If operating rules are outdated, systems are run based on old assumptions and safeguards miss their purpose.
- If exceptions emerge informally, insecure ways of working become permanent and invisible.
- If operating rules and security rules are maintained separately, clear stop points for risky changes are missing.
- If providers work according to their own routines without aligned rules and evidence, responsibilities remain unclear.

## Triggers

- new or materially changed service, process, site, system, cloud service, or provider.
- change in architecture, operating model, data class, protection need, or availability requirement.
- security event, operational disruption, audit finding, vulnerability, or lessons learned.
- role change in the operations team or handover to another operator.
- new or changed requirements from risk analysis, management decision, contract, or requirements register.
- periodic review of operating documentation.

## Roles and responsibilities

- **Service Owner / Process Owner:** determines which operating rules are necessary for the service and decides business-related conflicting objectives.
- **IT / Platform Owner:** describes technical operating processes, maintenance, monitoring, backup, recovery, and secure standard actions.
- **ISMS Owner / Security role:** defines minimum logic for security relevance, review, exceptions, and evidence.
- **Operations team / Administrators:** use the rules in everyday work and report unclear points, deviations, or outdated content.
- **Change Owner:** ensures that changes to systems also update operating rules.
- **Supplier management:** integrates external operating parts, evidence, and escalation paths.
- **Management:** decides on unacceptable residual risks, resource gaps, and accepted deviations.

## Implementation

### Minimum start

Goal: Critical operating processes are findable, owned, and review-ready.

1. The organisation names the most important services, systems, or data-processing processes in ISMS scope.
2. An owner is assigned for each critical object.
3. The most important operating rules are documented briefly for each object: start/stop, change, access, backup, monitoring, disruption, escalation.
4. Rules are stored where the operations team actually finds and uses them.
5. Changes or disruptions trigger a check whether the rule still fits.
6. Exceptions are documented with reason, duration, and review date.

Minimum evidence:

- list of critical services or systems with owner,
- operating rule or runbook for prioritised objects,
- review date and change history,
- ticket or record for deviation, disruption, or update,
- documented exception decision.

### Solid practice

Goal: Operating rules are maintained as a repeatable governance routine.

1. Operating rules follow a uniform minimum structure: scope, owner, normal operation, maintenance, access, monitoring, backup, restart, escalation, evidence.
2. Changes to systems or processes include a check whether runbooks and operating rules were updated.
3. Critical operating tasks are supported with checklists, four-eyes points, or approvals.
4. Provider rules and internal operating rules are aligned with each other.
5. Disruptions, incidents, and audit findings lead to targeted improvements.
6. Reviews check not only existence, but use, currency, and understandability.

Strong evidence:

- current runbook/operating-rule index,
- change tickets with documentation check,
- operating checklists or maintenance evidence,
- incident or disruption lessons learned with rule adjustment,
- provider alignment and escalation contacts,
- exception and review log.

### Advanced practice

Goal: Operating rules are integrated into tooling, monitoring, and resilience routines.

1. Runbooks are connected with ticketing, monitoring, on-call processes, and the knowledge base.
2. Recurring operating tasks are partially automated, but with clear human approval points where risk is present.
3. Emergency, restart, and crisis processes reference the relevant operating rules.
4. Rule changes are versioned and reviewed by peers for critical services.
5. Metrics show overdue reviews, open exceptions, documentation gaps, and recurring operating errors.
6. Management receives a decision-ready view of technical debt, knowledge dependencies, and resilience risks.

## Routine flow

1. **Identify operating need:** new service, change, disruption, review, or handover.
2. **Define scope:** determine affected systems, data, roles, interfaces, and providers.
3. **Write or update rule:** describe concrete working method, responsibility, stop points, and evidence.
4. **Check practical usability:** the operations team tests understandability against a realistic task.
5. **Approve and publish:** owner confirms use and storage location.
6. **Use in operations:** maintenance, disruption, change, or restart generates natural evidence.
7. **Review:** check currency, deviations, lessons learned, and exceptions.
8. **Escalate:** route missing resources, non-operable rules, or accepted deviations to management.

## Decisions

- Which services and processes need operating rules first?
- Which activities require approval, four-eyes principle, or escalation?
- Which rules must be maintained internally, and which at the provider?
- How are outdated rules identified and removed from operations?
- When is a deviation a permissible exception, and when is it a risk acceptance topic?
- Which operating risks belong in management review?

## Evidence

### Strong evidence

- runbooks or operating rules with owner, scope, version, and review date,
- evidence that rules were used during changes, maintenance, or disruptions,
- updates after incidents, tests, or lessons learned,
- documented exceptions with duration and decision,
- provider evidence for operated tasks,
- management decisions on resources, technical debt, or residual risks.

### Weak evidence

- old operating manual without owner and review date,
- generic process description without reference to concrete services,
- storage in a wiki that nobody uses in operations,
- change evidence without review of operating documentation,
- provider contract without operational evidence.

### Evidence gaps

- critical services without runbook or deputy capability,
- no connection between changes and rule updates,
- exceptions without expiry date,
- disruptions repeat without rules being improved,
- external operating parts without aligned escalation paths.

## Effectiveness review

Review questions:

- Can operations teams perform critical tasks securely using the rules?
- Are owner, review date, and storage location clear for critical rules?
- Are operating rules updated after changes, disruptions, and incidents?
- Are exceptions time-limited and decided?
- Are provider parts connected with internal rules and evidence?
- Does management recognise recurring documentation or operating risks?

Possible metrics:

- share of critical services with current runbook,
- overdue reviews,
- open exceptions,
- recurring disruptions caused by unclear operating processes,
- changes with reviewed documentation update,
- critical services without deputy capability.

## BSIG/NIS2 connection point

Documented operating rules are a connection point for NIS2-oriented topics such as risk management, operational security, incident handling, business continuity, supply-chain control, and cyber hygiene. The specific connection should be assessed for the organisation in the requirements register and ISMS review.

This artefact does not replace legal assessment or binding review of applicability or evidence obligations.

## Boundaries

- This artefact is not a complete operating manual and not a technical hardening baseline.
- It does not replace architecture, data protection, contract, or emergency planning.
- It does not confirm conformity, certification readiness, or legal fulfilment.
- It does not adopt ISO 27002 text.
- A documented rule is only robust if it is used, reviewed, and improved in operations.

## Handoffs

- **Change handoff:** system, process, or architecture changes that alter operating rules.
- **Incident/Problem handoff:** disruptions, security events, or recurring errors caused by unclear processes.
- **BCM handoff:** restart, emergency operation, critical services, or dependencies.
- **Supplier handoff:** external operating tasks, evidence, escalation paths, and service boundaries.
- **Management handoff:** lack of resources, technical debt, non-operable rules, or accepted deviations.
- **Audit/Evidence handoff:** unclear owners, outdated rules, or missing evidence of use.

## Typical mistakes

- Rules are written once and never tested in operations.
- Runbooks describe desired processes instead of actually used workflows.
- Changes to systems do not update operating documentation.
- External providers operate critical parts without delivering aligned evidence.
- Operating rules contain no escalation or stop points.
- Management sees documentation rates, but no operating risks.

## Fictional mini example

A fictional mid-sized company operates a central ERP system. After a disruption, it becomes clear that only one person knows how to restart it. The Service Owner has a short runbook created with start sequence, contacts, backup check, and escalation. During the next maintenance window, another team member uses the runbook, documents two unclear points, and updates the rule. In management review, it is decided to build deputy capability for two additional critical services as well.

Evidence:

- ERP runbook with owner and version,
- maintenance ticket showing use of the runbook,
- update after test,
- list of further critical services,
- management decision on prioritisation.
