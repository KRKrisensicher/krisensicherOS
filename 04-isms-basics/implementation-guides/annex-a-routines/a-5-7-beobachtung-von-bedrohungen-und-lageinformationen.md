# A.5.7 — Monitoring threats and situation information

## Purpose

Threat and situation monitoring ensures that relevant developments are not noticed by chance. The organization identifies warnings, attack patterns, vulnerability situations, supplier notifications, and industry-specific developments early enough to adjust risks, priorities, and measures.

The core is not as much threat intelligence as possible, but a usable situation routine: Which information is monitored, how is it assessed, who acts, and when is it escalated?

## Control objective in repository language

The organization operates a repeatable routine by which threat and situation information from defined sources is collected, filtered, assessed, and transferred into concrete decisions. Relevant findings flow into risk analysis, vulnerability management, incident response, awareness, supplier management, BCM, and management review.

## Typical risks

- If threats are not monitored, attack movements, active exploitation, or industry incidents remain unconsidered for too long.
- If too much unassessed information arrives, teams overlook the few truly relevant signals.
- If situation information is not connected with assets and services, no concrete measures result.
- If warnings are viewed only technically, business risks, supply-chain consequences, or crisis relevance remain invisible.
- If no escalation logic exists, critical notifications reach incident response or management too late.
- If sources are used without review, false alarms, rumors, or interest-driven information can distort decisions.

## Triggers

- new warning from CERT, CSIRT, vendor, service provider, industry, authority, or trusted specialist source.
- indication of active exploitation, new attack campaign, critical vulnerability, or industry-specific incident.
- security event, near miss, customer or supplier notification.
- new critical asset, new service provider, new technology, or new exposure.
- risk review, management review, BCM exercise, or incident lessons learned.
- significant change in the geopolitical, regulatory, technical, or industry-specific situation.
- periodic review of sources, search profiles, and assessment logic.

## Roles and responsibilities

- **Security role / ISMS owner:** defines sources, assessment logic, triage, internal distribution, and review.
- **IT/platform owner:** assesses technical affectedness, exposure, and treatment need.
- **Asset owner / service owner:** assesses business relevance and prioritizes measures.
- **Incident response role:** takes over notifications with possible active exploitation or compromise.
- **Supplier management:** tracks threat and situation notifications related to external services, products, or managed services.
- **BCM/crisis role:** assesses situation information with potential impact on availability, delivery capability, or crisis organization.
- **Management:** decides resources, prioritization, risk acceptance, and communication during an elevated situation.

## Implementation

### Minimum start

Goal: reliably identify critical situation notifications and translate them into measures.

1. The organization defines a few relevant sources: national warning channels, vendor advisories, service provider notifications, industry information, and internal incident findings.
2. For each source, an owner and review interval are defined.
3. Incoming notifications are checked for affectedness: asset, technology, service provider, process, industry, data class.
4. Relevant notifications are recorded in a ticket, measure log, or risk register.
5. Critical notifications trigger defined handoffs: incident response, vulnerability management, supplier management, or management.
6. Non-relevant notifications are briefly rejected with a rationale so decisions remain traceable.

Minimum evidence:

- source list with owner and review interval,
- triage note for relevant warnings,
- affectedness check for critical assets,
- measure or risk entry,
- escalation evidence for critical situation.

### Solid practice

Goal: situation monitoring becomes risk-oriented, repeatable, and decision-capable.

1. Monitoring profiles are derived from the ISMS scope: critical technologies, core services, service providers, data types, industry.
2. Sources are assessed by reliability, timeliness, relevance, and actionability.
3. Notifications are classified: monitor, check, treat, escalate, communicate, or close.
4. Situation information is connected with the asset inventory, vulnerability log, risk register, and incident routine.
5. Regular situation reviews condense top topics, open measures, and possible management decisions.
6. False positives and information overload are actively reduced.
7. Lessons learned from incidents adjust search profiles and sources.

Strong evidence:

- monitoring profile for critical services and technologies,
- source assessment,
- triage and decision log,
- tickets or measures from situation information,
- situation review with top risks and open decisions,
- update of risk analysis, awareness, or BCM scenarios.

### Advanced practice

Goal: the threat situation becomes part of security operations, risk steering, and crisis steering.

1. Situation information is semi-automatically correlated with asset data, vulnerabilities, exposure, and supplier information.
2. Critical warnings create predefined playbooks or prioritization rules.
3. The organization uses scenario analyses to assess possible impacts on core services, supply chains, and crisis capability.
4. Management receives short situation briefings with decision needs, not only technical warning lists.
5. Threat intelligence feeds, SIEM/SOC, incident response, and vulnerability management are aligned.
6. The quality of situation monitoring is reviewed using response time, hit rate, and measure effect.

## Routine flow

1. **Information arrives:** warning, advisory, industry notification, service provider notification, incident finding, or situation update.
2. **Check source:** assess reliability, timeliness, context, and possible relevance.
3. **Clarify affectedness:** assign asset, technology, service provider, location, process, or data class.
4. **Determine urgency:** classify active exploitation, exposure, business impact, and existing safeguards.
5. **Trigger handoff:** involve vulnerability management, incident response, supplier management, BCM, or management.
6. **Document measure or decision:** treat, monitor, communicate, adjust risk, or close with rationale.
7. **Track:** record deadline, owner, status, and effectiveness review.
8. **Update situation picture:** transfer patterns, trends, and open decisions into review formats.

## Decisions

- Which sources are truly relevant for scope, industry, and technology?
- Which notifications must be triaged immediately, and which are sufficient for the next review?
- When does a situation notification become a suspected incident?
- Which situation information justifies resource shifts, change freeze, patch prioritization, or crisis preparation?
- Who decides on internal or external communication?
- How is information overload limited without losing critical signals?

## Evidence

### Strong evidence

- defined source and monitoring profiles,
- documented triage of critical situation notifications,
- affectedness checks with asset or service connection,
- measure, incident, or vulnerability tickets,
- situation review with decisions and open risks,
- adjustments to risk register, playbooks, awareness, or BCM scenarios,
- management decision during elevated situation or resource need.

### Weak evidence

- unfiltered feed or newsletter list,
- screenshots of individual warnings without assessment,
- tool dashboard without owner and handoff,
- blanket statement “monitored by service provider” without feedback,
- situation report without connection to measures or decisions.

### Evidence gaps

- no defined sources,
- no affectedness check,
- no connection to asset inventory or risk register,
- no escalation criteria for critical warnings,
- no tracking of open measures,
- no deputy for situation monitoring,
- no review routine for source quality.

## Effectiveness review

Review questions:

- Can critical situation notifications be assigned to an owner, asset, and decision path?
- Are active exploitations or industry-specific warnings assessed in a timely manner?
- Does situation monitoring lead to concrete measures or deliberately documented non-action?
- Are sources current, relevant, and not overloaded?
- Are supplier and SaaS notifications visibly processed?
- Is situation information fed back into risk, incident, vulnerability, and BCM routines?

Possible metrics:

- time from warning receipt to triage,
- share of critical notifications with affectedness check,
- number of measures from situation information,
- overdue situation notifications without decision,
- hit rate of relevant sources,
- number of supplier notifications with feedback.

## BSIG/NIS2 connection point

Threat and situation monitoring is connectable to NIS2-oriented risk management measures, incident handling, vulnerability management, supply-chain security, business continuity, and management oversight. For affected organizations, the concrete connection should be assessed in the requirements register, risk register, and incident/situation processes.

This artifact does not replace legal assessment of reporting obligations, affectedness, or communication with authorities.

## Boundaries

- This artifact is not a SOC design and does not require specific commercial threat-intelligence feeds.
- It does not replace technical vulnerability assessment or incident forensics.
- Situation information supports decisions; it is not certainty about actual affectedness.
- No legal or data protection advice, no certification assurance.
- No confidential situation or customer data in public examples.

## Handoffs

- **Vulnerability handoff:** warning affects specific technology, CVE, configuration, or product version.
- **Incident handoff:** active exploitation, suspected compromise, or notable indicators.
- **Supplier handoff:** notification affects SaaS, managed service, product supplier, or third-party component.
- **BCM/crisis handoff:** situation may affect availability, delivery capability, site operation, or crisis organization.
- **Management handoff:** increased resource need, risk acceptance, priority shift, or communication decision.
- **Communications/legal handoff:** external statements, customer information, contractual or legal questions.
- **Audit/evidence handoff:** missing triage, unclear sources, or untracked notifications.

## Typical mistakes

- As many feeds as possible are subscribed to, but nobody triages them.
- Warnings are read only technically and not connected with business services.
- Critical notifications remain in individual mailboxes.
- Situation reports contain a lot of information but no decision points.
- Service providers are made responsible without a feedback or escalation path.
- Sources are never reviewed for relevance or false alarms.
- Management is informed only when operational teams are already blocked.

## Fictional mini example

A fictional software service provider receives a warning about actively exploited vulnerabilities in a widely used VPN component. The security role checks the reliability of the source, assigns the component to two locations, and creates tickets for the platform owner. Because one location is externally reachable, the notification is escalated to incident response and management. After review and patching, the situation log is updated and the source is marked as highly relevant.

Evidence:

- warning notification with source and date,
- affectedness check against asset list,
- patch and validation tickets,
- escalation note to incident response and management,
- updated situation and source review.
