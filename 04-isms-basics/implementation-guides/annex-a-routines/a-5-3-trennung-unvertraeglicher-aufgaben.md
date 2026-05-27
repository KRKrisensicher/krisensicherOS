# A.5.3 — Separation of conflicting duties

## Purpose

Separation of conflicting duties prevents individual persons or roles from being able to plan, execute, approve and review critical actions without sufficient counter-control. The core is not distrust of people, but robust process design against mistakes, misuse, conflicts of interest and unnoticed concentration of power.

## Control objective in repository language

The organization operates a routine that identifies, assesses, separates or compensates critical combinations of tasks, rights and decisions. Where separation is not possible, exceptions are consciously decided, monitored and time-limited.

## Typical risks

- If one person controls change, approval and production release alone, mistakes or manipulation may remain undetected.
- If admin rights and business approval rights coincide, uncontrolled concentrations of power arise.
- If small teams do not define compensating measures, unavoidable role conflicts become invisible.
- If role changes are not reviewed, old and new rights can create dangerous combinations.
- If service providers perform implementation and control at the same time, independent steering is missing.
- If emergency rights are not reviewed afterwards, temporary exceptions become permanent.

## Triggers

- new or changed roles, permission groups, workflows or approval paths.
- role changes, onboarding, departure or deputy arrangements.
- new system, new process, new application or new service provider access.
- introduction of privileged rights, emergency access or technical accounts.
- audit finding, fraud indicator, security event or suspicion of an impermissible action chain.
- scheduled permission, role or process review.
- organizational bottlenecks where separation is practically not fully possible.

## Roles and responsibilities

- **Process owner:** identifies critical process steps and conflicting duties in the business process.
- **Asset / information owner:** assesses protection needs and risk in task combinations.
- **IT/platform owner:** provides role, group and permission information and implements technical separation.
- **ISMS owner / security role:** defines assessment logic, minimum requirements, review and escalation.
- **Manager:** is accountable for role design, deputies and implementation in the team.
- **Internal audit / audit role:** reviews critical combinations, evidence and compensating measures.
- **Management:** decides on non-resolvable conflicts, resources and risk acceptance.

## Implementation

### Minimum start

Objective: Make critical task conflicts visible in the most important processes.

1. The organization names especially critical processes: payments, production changes, access approval, procurement, customer data, security monitoring.
2. Process owners describe the critical steps for each process: request, approve, execute, review, log.
3. Obviously conflicting combinations are marked.
4. Existing roles and rights are checked against them.
5. Cases that cannot be separated receive a compensating measure, review or management decision.
6. A conflict check is triggered during role changes.

Minimum evidence:

- list of critical processes and tasks,
- simple conflict matrix,
- review of a sample of critical roles,
- documented exception with compensation,
- management decision for non-resolvable conflict.

### Solid practice

Objective: Separation of duties is built into the role model, access and process reviews.

1. Conflict rules are defined for central systems and processes.
2. Access requests check not only individual rights, but dangerous combinations.
3. Role reviews consider admin rights, approval rights, deputies, service providers and technical accounts.
4. Compensating measures are defined concretely: four-eyes approval, downstream review, logging, report, time limitation.
5. Exceptions are time-limited and maintained with a risk decision.
6. Findings from incident, audit or control flow back into conflict rules.

### Advanced practice

Objective: Conflicts are continuously identified and steered in a decision-ready way.

1. IAM, ticket, workflow or GRC data support conflict detection.
2. Critical combinations trigger alerts, additional approvals or mandatory reviews.
3. Emergency rights and just-in-time access are reviewed afterwards.
4. Service provider actions are connected with internal approval and independent control.
5. Management sees not only conflict numbers, but non-resolvable conflicts of objectives and resource needs.
6. Organizational design, role model and automation reduce recurring conflicts.

## Routine flow

1. **Select critical process:** based on risk, protection need, financial impact, data class or incident history.
2. **Break down tasks:** request, approve, execute, review, monitor, change.
3. **Define conflicts:** Which combination must not sit with one role without control?
4. **Review roles and rights:** include persons, groups, service providers, technical accounts and deputies.
5. **Treat:** separate, change rights, add a second approval or define compensation.
6. **Decide exceptions:** time-limited, justified, risk-assessed and with follow-up date.
7. **Perform review:** check role changes, new systems and regular samples.
8. **Improve:** adjust conflict rules, role model or processes.

## Decisions

- Which processes and systems are critical for separation of duties?
- Which combinations are not acceptable, and which are acceptable only with compensation?
- When is the four-eyes principle sufficient, and when is technical separation needed?
- Who may accept an exception and for how long?
- How is separation implemented realistically in small teams?
- Which service provider actions require independent internal control?

## Evidence

### Strong evidence

- conflict matrix for critical processes or systems,
- role and permission exports at the review point,
- review minutes with decision for each conflict,
- evidence of implemented rights changes or process adjustments,
- documented compensating measures with owner,
- exception decisions with expiry date,
- management decision for structurally non-separable tasks.

### Weak evidence

- general statement “four-eyes principle applies” without process connection,
- organization chart without rights or task analysis,
- access list without conflict assessment,
- verbal deputy rule without evidence,
- tool rule without review of hits.

### Evidence gaps

- no defined critical combinations,
- admin and approval rights not reviewed together,
- emergency rights without downstream review,
- small teams without documented compensation,
- service provider executes and controls itself,
- exceptions without duration or risk acceptance.

## Effectiveness review

Review questions:

- Are the most important conflicting duties defined for each critical process?
- Are role changes and new rights checked for conflicts?
- Do reviews lead to rights removal, process change or decision?
- Are compensating measures concrete and evidenced?
- Are emergency and service provider accesses considered specifically?
- Does management see structural conflicts that cannot be solved operationally?

Possible metrics:

- number of critical conflicts per process or system,
- overdue conflict reviews,
- open exceptions without follow-up date,
- time to remediate critical role conflicts,
- share of emergency rights with downstream review,
- recurring conflicts caused by role model or team design.

## BSIG/NIS2 connection point

Separation of duties is connectable to NIS2-oriented governance, risk management, access protection, secure operating processes, incident prevention and management oversight. The concrete connection should be assessed organization-specifically in the requirements register, risk register and for critical processes.

This artifact does not replace legal assessment, data protection review or a statement on statutory fulfillment.

## Boundaries

- No blanket specification of which functions must be separated in every organization.
- No legal advice on fraud, liability, employment law or co-determination.
- No certification or conformity assurance.
- No complete IAM or process design specification.
- Small organizations often need compensation; the artifact does not create a false sense of security through unrealistic separation.

## Handoffs

- **Access/IAM handoff:** roles, groups, privileged rights, technical accounts, recertification.
- **Process owner handoff:** critical process steps, four-eyes rules, approval and control points.
- **HR handoff:** role changes, deputies, job design and absences.
- **Vendor handoff:** service provider rights, external approvals, control evidence.
- **Incident handoff:** suspicion of misuse, manipulation or control circumvention.
- **Management handoff:** non-separable tasks, resource bottleneck, accepted residual risk.
- **Audit/evidence handoff:** missing conflict rules, incomplete reviews or weak compensation.

## Typical mistakes

- Separation of duties is considered only in the financial process, not in IT and data processes.
- Conflicts are defined but not checked against real permissions.
- Small teams hide conflicts instead of documenting compensation.
- Emergency rights are not reviewed after use.
- Service providers receive broad rights without independent acceptance.
- Reviews produce lists but no decisions.
- Exceptions remain permanent because no expiry date was set.

## Fictional mini example

A fictional online retailer reviews the release process. Until now, the same person can merge code, approve deployment and use production access. The product owner and platform owner define a conflict rule: deployment approval and production admin access are separated. For a small on-call team, a time-limited exception with downstream log review is established.

Evidence:

- conflict rule for the release process,
- permission export of the deployment group,
- ticket for the rights change,
- exception for on-call duty with expiry date,
- log review evidence after emergency use.
