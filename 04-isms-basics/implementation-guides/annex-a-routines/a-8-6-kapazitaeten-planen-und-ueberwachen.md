# A.8.6 — Plan and monitor capacity

## Purpose

Capacity planning and monitoring ensure that important services do not fail because of foreseeable bottlenecks, growth, misconfigurations or undetected utilisation. The core is not a single monitoring dashboard, but a routine that connects technical metrics with service criticality, business planning, change management and management decisions.

## Control objective in repository language

The organisation operates a traceable routine for capacities of critical systems, platforms, networks, storage, applications, licences, cloud resources and operational resources. It detects trends, defines thresholds, plans expansions and escalates conflicts before availability, security or service quality tip over.

## Typical risks

- If capacity limits are reached unnoticed, services can fail or security functions may stop working.
- If growth, campaigns or new customers are not included in planning, bottlenecks only become visible in operations.
- If log, backup or monitoring storage fills up, security and recovery evidence is lost.
- If cloud resources grow without control, cost risks or shutdowns due to limits can arise.
- If licence, staffing or support capacities are forgotten, technical measures cannot be operated.
- If alerts run without owner, thresholds are ignored or handled too late.

## Triggers

- new or changed service, new platform, new data volume or new user group.
- business event such as campaign, migration, site expansion, product launch or customer growth.
- monitoring alert, trend threshold breach, repeated performance problems or incident.
- change to backup, logging, security monitoring or retention requirements.
- cloud limit, licence limit, contract change or supplier notice.
- architecture, change or release decision with capacity impact.
- periodic review of critical services and capacity metrics.

## Roles and responsibilities

- **Service Owner / Application Owner:** assesses criticality, user need, service objectives and business planning.
- **IT / Platform Owner:** measures technical capacities, sets thresholds and plans expansions.
- **Cloud / Infrastructure Owner:** controls resource limits, scaling, costs and technical reserves.
- **Security role / ISMS Owner:** pays attention to capacities for logging, monitoring, backup, protection systems and incident response.
- **BCM / Emergency responsible persons:** assess impacts on critical processes and recovery objectives.
- **Finance / Procurement:** clarifies budget, licences, contracts and procurement lead times.
- **Management:** decides on resource needs, acceptance of bottlenecks, prioritisation and availability targets.

## Implementation

### Minimum start

Goal: make critical capacity risks visible and do not discover them only during an incident.

1. The most important services, platforms, storage locations, network connections, log/backup systems and cloud limits are named.
2. Each critical target has an owner and a simple metric.
3. Thresholds are defined: warning, critical range, escalation.
4. Regular review of metrics is defined, at least for productive critical services.
5. Foreseeable expansions, costs or procurements are tracked in the action log.
6. Bottlenecks with risk to availability or security are taken to management review.

Minimum evidence:

- list of critical capacity objects with owner,
- monitoring or metric extract,
- defined thresholds,
- action or capacity log,
- decision on expansion, workaround or accepted residual risk.

### Solid practice

Goal: capacity control becomes plannable, trend-based and connected to change management.

1. Capacity is considered per service along relevant dimensions: CPU, memory, network, storage, database, queue, licences, cloud limits, log/backup volume.
2. Trends are assessed regularly and aligned with business planning, roadmap and changes.
3. Capacity impact becomes part of architecture, release and change reviews.
4. Alerts have owner, response path and escalation threshold.
5. Security-relevant capacities such as logging, EDR, SIEM, backup and update distribution are considered separately.
6. Measures distinguish short-term relief, permanent expansion, architecture change and accepted limitation.
7. Management receives decision-ready information on costs, availability and residual risk.

### Advanced practice

Goal: capacity is controlled proactively and service-oriented.

1. Automated dashboards, forecasts or SLO/SLA references connect technical trends with service criticality.
2. Cloud and platform limits are controlled through IaC, policies or budget alerts.
3. Load tests, resilience tests and growth assumptions feed into roadmaps and BCM planning.
4. Capacity data supports incident triage, problem management and technical debt control.
5. Critical resources are reviewed for single points of capacity: specialist staff, maintenance windows, licences, delivery times.
6. Management decisions are based on scenarios: invest, limit, defer, accept or change architecture.

## Routine flow

1. **Define scope:** determine critical services, platforms, security functions and resources.
2. **Define metrics:** select technical and organisational capacities per service.
3. **Set thresholds:** describe warning, critical range, escalation and target state.
4. **Review data:** analyse monitoring, costs, licences, tickets, incidents and business planning.
5. **Assess:** estimate trend, service impact, security impact and time to bottleneck.
6. **Plan measure:** plan scaling, clean-up, optimisation, procurement, architecture change or accepted limitation.
7. **Implement and evidence:** document change, ticket, budget decision or configuration change.
8. **Review:** check effectiveness and adjust thresholds, forecasts or responsibilities.
9. **Escalate:** take bottlenecks with availability, security or cost impact to management review.

## Decisions

- Which services and security functions are capacity-critical?
- Which thresholds trigger technical response, Service Owner review or management decision?
- Which growth assumptions are realistic and who confirms them?
- When is scaling, optimisation, limitation or conscious risk acceptance chosen?
- Which capacities depend on budget, suppliers or personnel?
- How are cost risks controlled in cloud and licence models?

## Evidence

### Strong evidence

- scope of critical services and capacity objects with owners,
- monitoring or trend reports with date and thresholds,
- alert and escalation rules,
- capacity measures with ticket, change or budget decision,
- evidence for log, backup, security-monitoring and cloud limits,
- review record with assessment and decision,
- management decision for resource or availability conflict.

### Weak evidence

- dashboard without owner or review routine,
- technical utilisation values without service reference,
- generic statement “cloud scales automatically” without limit check,
- capacity planning only for servers, but not for logs, backups or licences,
- alert list without response path,
- budget request without risk reference.

### Evidence gaps

- critical services without capacity measurement,
- no thresholds or escalation points,
- no connection to business planning,
- full log or backup storage without decision,
- cloud limits or licence boundaries unknown,
- repeated performance incidents without root cause analysis.

## Effectiveness review

Review questions:

- Are critical services and security functions in scope from a capacity perspective?
- Can owners recognise when a bottleneck becomes a service or security risk?
- Are trends assessed and handled before an incident?
- Is there evidence that alerts lead to decisions or measures?
- Are log, backup, monitoring and cloud capacities considered?
- Are resource and budget conflicts taken to management in time?

Possible metrics:

- share of critical services with defined capacity thresholds,
- overdue capacity measures,
- number of critical threshold breaches,
- time to bottleneck according to forecast,
- capacity-related incidents,
- log/backup storage reach,
- cloud limit or licence boundaries with escalation status.

## BSIG/NIS2 connection point

Capacity planning and monitoring are compatible with NIS2-oriented topics such as operational security, maintenance of critical services, business continuity, incident prevention, monitoring and risk management. The concrete connection should be assessed organisation-specifically in the requirements register, BCM documentation and management review.

This artefact does not replace legal assessment or any availability or conformity commitment.

## Boundaries

- This artefact is not a performance engineering handbook.
- It does not replace technical architecture, load test or cloud cost analysis.
- It does not guarantee availability or fulfilment of external service objectives.
- It makes no legal statement on concrete obligations.
- No confidential operational, cost or customer data in public examples.

## Handoffs

- **Change handoff:** scaling, architecture change, maintenance window, test and rollback needs.
- **BCM handoff:** capacity bottleneck affects a critical business process or recovery objective.
- **Security handoff:** logging, monitoring, backup, EDR, SIEM or protection systems reach capacity limits.
- **Finance / Procurement handoff:** budget, licence limits, cloud costs, procurement lead times or contract limits.
- **Management handoff:** residual risk, prioritisation, cost/availability conflict or deliberate performance limitation.
- **Incident / Problem handoff:** repeated performance or availability disruptions caused by bottlenecks.
- **Audit / Evidence handoff:** missing thresholds, non-traceable capacity decisions or incomplete scope.

## Typical mistakes

- Monitoring exists, but nobody assesses trends.
- Capacity is considered only for production servers, not for logging, backup or licences.
- Cloud scaling is assumed even though limits, costs or architecture restrict it.
- Alerts create noise and no decision.
- Business growth reaches IT only after the bottleneck.
- Capacity measures are treated as purely technical tickets and not prioritised.
- Management receives utilisation charts without a decision question.

## Fictional mini example

A fictional online service plans a marketing campaign. The Service Owner informs the platform team about expected user growth. A trend report shows that database storage and log storage will become critical in six weeks. The platform team creates two changes: storage expansion and adjustment of log retention. Finance approves budget; the ISMS Owner documents that security logs are not shortened, but moved to lower-cost storage.

Evidence:

- capacity scope for the service,
- trend report with thresholds,
- change tickets,
- budget decision,
- review note on log retention.
