# A.8.20 — Network security

## Purpose

Network security ensures that network connections, transitions, components, and operating paths are planned, protected, monitored, and changed in a traceable way. The core is not “firewall exists”, but an operated routine: Which network areas exist, which connections are allowed, who is responsible for changes, and how are deviations detected?

## Control objective in repository language

The organization operates networks as a controlled operating environment. Network architecture, access paths, firewall/routing rules, remote access, cloud networks, and critical network components are controlled with owners, change process, monitoring, review, and exception handling.

## Typical risks

- If network transitions grow without review, systems may become reachable that should never have been exposed.
- If firewall or routing rules have no owner, old approvals remain in place after a project ends.
- If network components remain insecurely configured or unpatched, attackers can manipulate central communication paths.
- If remote or administrative access is not controlled separately, a compromised account can have far-reaching impact.
- If cloud, site, and provider networks are not considered together, blind spots arise in reachability, logging, and responsibility.

## Triggers

- new network, new site, new cloud environment, new service provider access, or new interface.
- change to firewall rules, routing, VPN, DNS, proxy, WLAN, or management access.
- vulnerability, incident, unusual network traffic, or monitoring alert.
- introduction or change of critical systems and network components.
- audit finding, architecture review, or risk decision.
- periodic review of network rules, network plans, and admin access.

## Roles and responsibilities

- **Network owner / platform owner:** responsible for architecture, operations, changes, and technical evidence.
- **Service owner / asset owner:** describes business need, protection need, and required connections.
- **Security role / ISMS owner:** defines minimum logic for approvals, reviews, exceptions, and risk handling.
- **Change owner:** coordinates tests, rollback, maintenance windows, and documentation.
- **Incident response:** takes over when misuse, lateral movement, or network compromise is suspected.
- **Supplier management:** controls external network services, managed services, and service provider access.
- **Management:** decides on residual risks, lack of resources, architectural conflicts, or permanently necessary exceptions.

## Implementation

### Minimum start

Goal: make critical network areas and network changes visible and reviewable.

1. The most important network areas, internet transitions, remote access paths, cloud networks, and critical components are recorded with owners.
2. New or changed network approvals go through a ticket or change with purpose, source, destination, port/protocol, duration, and business owner.
3. Internet-exposed and administrative access paths are reviewed separately.
4. Open or broad rules receive a justification, compensating measure, or rollback plan.
5. At least critical rules and components are reviewed regularly.

Minimum evidence:

- network overview with critical transitions and owners,
- change/ticket evidence for rule changes,
- review record for critical firewall or routing rules,
- list of administrative and external network access paths,
- exception decisions with expiry date.

### Solid practice

Goal: network security is managed as a repeatable architecture and operating routine.

1. Network areas are organized by protection need, function, exposure, and operational responsibility.
2. Rule changes follow an approval process with business justification, security review, and technical validation.
3. Network components have a baseline configuration, patch/firmware routine, configuration backup, and access protection.
4. Logging and monitoring cover relevant transitions, denied connections, admin access, and configuration changes.
5. Old rules, temporary approvals, and project access paths are actively removed.
6. Network findings feed into vulnerability management, architecture review, and management review.

Strong evidence:

- current network and data flow overview,
- rule catalogue with owner, purpose, and review date,
- approved changes with test/rollback note,
- configuration and backup evidence for critical components,
- monitoring or log analyses,
- evidence of removal of rules no longer needed.

### Advanced practice

Goal: network control is risk-oriented, automated, and connected with detection.

1. Network rules, cloud security groups, VPNs, and zero-trust policies are centrally inventoried or regularly evaluated automatically.
2. Critical paths and unexpected reachability are made visible through tests, attack path analyses, or configuration checks.
3. Network changes are reviewed against architecture principles, data flows, and exposure risks.
4. Configuration deviations and unusual connections generate alerts for operations or incident triage.
5. Management receives decision-ready metrics on exposed services, old rules, exception rates, critical network findings, and resource needs.

## Routine flow

1. **Need arises:** new service, change, site, cloud resource, service provider, or incident measure.
2. **Describe connection:** record source, destination, purpose, protocol, data type, duration, and owner.
3. **Review risk:** assess exposure, protection need, administrative function, third-party access, and segment boundaries.
4. **Decide:** approve, reject, time-limit, compensate, or trigger management handoff.
5. **Implement:** technically change and test rule or configuration.
6. **Secure evidence:** store change, configuration, review date, and owner in a traceable way.
7. **Monitor:** review logs, alerts, and configuration changes.
8. **Review:** regularly clean up old rules, exceptions, and critical components.
9. **Improve:** feed findings back into architecture, segmentation, vulnerability handling, or operating standards.

## Decisions

- Which network areas and transitions are critical enough for prioritized review?
- Which rule types require security approval or management decision?
- How long may temporary network approvals remain in place?
- Which network components need special hardening, monitoring, and patch frequency?
- When does a network finding become an incident or architecture topic?
- Which conflicts exist between fast connectivity, availability, and attack surface reduction?

## Evidence

### Strong evidence

- network overview with owners, protection need, and critical transitions,
- approved rule and configuration changes,
- firewall/routing/cloud rule lists with review decisions,
- technical evidence for hardening, backup, patching, or configuration change,
- monitoring and alert evidence for relevant transitions,
- documented exceptions with expiry date and risk decision,
- management decision for permanently open risks.

### Weak evidence

- outdated network plan without owner or date,
- firewall export without purpose, decision, or review,
- broad statement “network is secured by a service provider”,
- change ticket without business justification,
- tool dashboard without derived measures.

### Evidence gaps

- unknown internet exposure,
- rules without owner or duration,
- critical network components without patch and backup evidence,
- external access paths without contract or service reference,
- no validation after rule changes,
- permanent exceptions without management decision.

## Effectiveness review

Review questions:

- Are critical network areas, transitions, and owners known?
- Can firewall or cloud rules be assigned to a purpose and decision?
- Are temporary or old network approvals removed?
- Are administrative and external access paths controlled especially closely?
- Are network components patched, backed up, and monitored?
- Have reviews led to concrete removals, corrections, or risk decisions?

Possible metrics:

- share of critical transitions with current owner,
- number of rules without purpose or review date,
- overdue temporary approvals,
- exposed services by criticality,
- open network findings by risk class,
- time to remove rules no longer needed.

## BSIG/NIS2 connection point

Network security is a connection point for NIS2-oriented risk management measures, cyber hygiene, access protection, incident prevention, vulnerability handling, secure operations, and maintaining critical services. The specific connection should be assessed in the requirements register and in the organization-specific risk analysis.

This artifact does not replace legal assessment of applicability or evidence obligations.

## Boundaries

- This artifact is not a complete network design and not a technical hardening baseline.
- It does not replace architecture, cloud, OT, or service provider security analysis.
- It makes no binding statement on legal obligations or certification capability.
- Logging and monitoring may touch data protection or employee-related topics and require suitable review.
- Public examples contain no real network plans, IP addresses, customer data, or secret configurations.

## Handoffs

- **Change handoff:** rule changes, routing, VPN, DNS, proxy, WLAN, cloud security groups.
- **Incident handoff:** suspicious traffic, lateral movement, compromised network component, unexplained reachability.
- **Vulnerability handoff:** unpatched network devices, insecure services, exposed systems.
- **Data protection handoff:** personal log analyses, user reference, monitoring, or content inspection.
- **Supplier handoff:** managed network, provider, external access, site networking.
- **Management handoff:** permanently open connections, resource need, architecture redesign, accepted residual risk.
- **Audit/evidence handoff:** missing owners, incomplete reviews, or unclear exception decisions.

## Typical mistakes

- Firewall rules are added but never removed.
- Network plans show target architecture, but not the operated current state.
- Cloud networks are considered separately from the traditional network.
- Service provider access remains active after a project ends.
- Network components are forgotten in vulnerability management.
- Monitoring generates alerts but no review or incident routine.
- Management sees technical lists instead of decision-ready risks.

## Fictional mini example

A fictional machine builder introduces new remote maintenance access for a production system. The service owner describes purpose and duration, the network owner sets up a time-limited VPN rule, and the security role requires MFA and restricted target systems. After three months, the review shows that the service provider access is no longer needed. The rule is removed and the removal is documented in the ticket.

Evidence:

- approved change ticket,
- rule description with purpose and duration,
- evidence of MFA/target system restriction,
- review note,
- removal ticket for the VPN rule.
