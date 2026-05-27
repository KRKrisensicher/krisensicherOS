# A.5.8 — Security in projects and changes

## Purpose

Security in projects and changes ensures that information security is not considered only after go-live or after an incident. New initiatives, process changes, technical changes, organizational restructuring, and supplier changes are reviewed early enough for security risks, responsibilities, evidence, and open decisions.

The core is not a heavy approval form, but a practical security checkpoint: What is changing, which risks arise, who decides, and which minimum requirements must be met before implementation?

## Control objective in repository language

The organization operates a routine by which projects and significant changes are transferred into security work according to risk and protection need. Security requirements, handoffs, tests, exceptions, and management decisions are built into project, change, and procurement processes.

## Typical risks

- If security is involved too late, architecture, suppliers, data flows, or permissions have already effectively been decided.
- If projects have no security owners, requirements, tests, and acceptances remain unclear.
- If changes are implemented without a risk and protection-need view, new attack surfaces, data leaks, or operational disruptions arise.
- If security requirements remain generic, they are not implemented in day-to-day project work.
- If exceptions are not decided, unmet requirements enter operations unnoticed.
- If changes are not connected with asset, access, supplier, or BCM routines, evidence and follow-up work are missing.

## Triggers

- new project, product, service, process, site, tool, interface, or data processing.
- significant change to architecture, permissions, data flows, operating model, supplier, or cloud/SaaS use.
- planned technical change with security, availability, or data protection relevance.
- introduction of new technology, automation, AI function, third-party component, or external access.
- security event, audit finding, vulnerability, or lessons learned requiring change.
- project gate, architecture review, procurement decision, release approval, or management decision.
- decommissioning, migration, retirement, or handover into operations.

## Roles and responsibilities

- **Project owner / product owner:** is responsible for planning and tracking security requirements and decisions in the initiative.
- **Change owner:** assesses technical and operational change risks, tests, rollback, and approval.
- **ISMS owner / security role:** defines security checkpoints, minimum questions, handoffs, and exception handling.
- **Asset owner / service owner:** assesses protection need, operational risk, and acceptability.
- **IT/platform or development team:** implements security measures, tests, and technical evidence.
- **Procurement / vendor management:** embeds security requirements for suppliers, SaaS, and external services.
- **Data protection / legal:** reviews personal data, contractual questions, legal bases, and external communication.
- **Management:** decides residual risks, budget, schedule/security conflicts, and exceptions.

## Implementation

### Minimum start

Goal: recognize security-relevant projects and changes early and not put them into operation without review.

1. The organization defines simple security questions for project start and change request: data, users, external access, internet exposure, suppliers, criticality, operational dependencies.
2. Initiatives with security relevance receive a security checkpoint and a responsible owner.
3. Minimum requirements are translated into tasks: access, logging, backup, vulnerability check, data protection/legal handoff, operational handover.
4. Open security risks are documented and decided before go-live.
5. High-risk changes require approval, test evidence, and a rollback or compensation plan.
6. The handover into operations updates asset inventory, access list, supplier register, and support responsibility.

Minimum evidence:

- security checklist for project or change,
- risk assessment with owner,
- measure or handoff list,
- approval or exception decision,
- operational handover with updated registers.

### Solid practice

Goal: security by design is embedded in project and change gates.

1. Projects are classified by risk classes or protection need.
2. Suitable security activities exist for each risk class: architecture review, data protection handoff, supplier review, threat modeling, test evidence, acceptance.
3. Security requirements are managed as project backlog or change tasks, not as separate paper.
4. Deviations receive rationale, duration, compensation, and decision.
5. Go-live or release decisions include security status and open residual risks.
6. Lessons learned from incidents, audits, and vulnerabilities adjust project standards.
7. Project closure updates asset, data, access, supplier, and emergency information.

Strong evidence:

- risk-based project classification,
- architecture or security review,
- security requirements in the backlog,
- test, scan, acceptance, or change evidence,
- exception and residual-risk decisions,
- updated operational and register entries,
- project closure with lessons learned.

### Advanced practice

Goal: security decisions are an integral part of portfolio, architecture, and change governance.

1. Project portfolio and change calendar show security-relevant initiatives, risks, dependencies, and resource needs.
2. Standard controls and technical baselines are provided as reusable building blocks.
3. Critical initiatives use structured methods such as threat modeling, security acceptance criteria, pre-production checks, and risk-based tests.
4. Automated gates in CI/CD, cloud, or change processes provide evidence without increasing manual bureaucracy.
5. Management receives a decision-ready view of unmet requirements, accepted residual risks, schedule/budget conflicts, and technical debt.
6. Recurring findings lead to architecture decisions, training, or process improvement.

## Routine flow

1. **Initiative or change is registered:** project idea, change, release, migration, procurement, or decommissioning.
2. **Check security relevance:** assess data, criticality, exposure, external parties, permissions, dependencies, and operational impact.
3. **Define risk class:** determine minimal, normal, or elevated security involvement.
4. **Derive requirements:** define concrete tasks, handoffs, tests, evidence, and acceptance criteria.
5. **Support implementation:** track open items in the project or change backlog.
6. **Review before approval:** consider completed requirements, exceptions, residual risks, rollback, and operational handover.
7. **Decide:** go-live, postponement, exception, compensation, or management handoff.
8. **Follow up:** update registers, record lessons learned, improve routines.

## Decisions

- Which projects and changes need security involvement, and which do not?
- Which minimum questions apply to every initiative?
- Which risk class triggers architecture review, tests, data protection/legal handoff, or management handoff?
- Who may go live with open security measures?
- Which target conflicts between schedule, budget, function, and security must be decided?
- Which evidence must exist before operational handover?

## Evidence

### Strong evidence

- project or change security check with risk class,
- security requirements in the backlog or change ticket,
- architecture, data protection, supplier, or operational review,
- test, scan, acceptance, or rollback evidence,
- go-live decision with open risks,
- exception with compensation, expiry date, and owner,
- updated asset, access, supplier, and operational documentation.

### Weak evidence

- general project methodology without security questions,
- one-off approval email without risk connection,
- checklist with “not relevant” everywhere and no rationale,
- security notes outside the project backlog,
- technical tests without connection to protection need or acceptance,
- go-live record without open residual risks.

### Evidence gaps

- no early security review,
- no owners for security requirements,
- no documentation of exceptions,
- no update of asset or access registers,
- no supplier or data protection review for relevant initiatives,
- no evidence for tests, acceptance, or operational handover,
- no management decision in a schedule/security conflict.

## Effectiveness review

Review questions:

- Are security-relevant projects and changes identified early?
- Are security requirements concrete enough to be implemented and checked?
- Is there evidence that open risks were decided before go-live?
- Are registers and operational routines updated after changes?
- Are exceptions time-limited and tracked?
- Do project and change processes learn from incidents, audits, and findings?

Possible metrics:

- share of relevant initiatives with security check,
- number of open security requirements before go-live,
- overdue exceptions from projects,
- recurring findings after changes,
- rework effort due to late security involvement,
- share of updated registers after operational handover.

## BSIG/NIS2 connection point

Security in projects and changes is connectable to NIS2-oriented risk management, secure procurement and development, incident prevention, business continuity, supply-chain security, and management responsibility. For affected organizations, the concrete connection should be assessed through the requirements register, project portfolio, risk analysis, and management review.

This artifact does not replace legal assessment, data protection impact assessment, or binding review of regulatory applicability.

## Boundaries

- This artifact is not a complete project management or change management method.
- It does not replace data protection, legal, architecture, or penetration-test assessment.
- It provides no certification, conformity, or security guarantee.
- It contains no licensed standards text.
- It must not be used as a bureaucratic gate that delays decisions without clarifying risks.

## Handoffs

- **Architecture handoff:** new platforms, interfaces, data flows, cloud/SaaS models, or technical debt.
- **Data protection/legal handoff:** personal data, new processing, contracts, external communication, or regulatory questions.
- **Supplier handoff:** new or changed third-party services, SaaS, managed services, or support access.
- **Incident/vulnerability handoff:** findings, active exploitation, security event, or remediating change.
- **BCM handoff:** changes to critical services, recovery, dependencies, or crisis roles.
- **Management handoff:** residual risk, schedule/budget conflict, unmet minimum requirement, or exception outside tolerance.
- **Audit/evidence handoff:** missing evidence, unclear approval, or incomplete operational handover.

## Typical mistakes

- Security is asked only shortly before go-live.
- Checklists are filled out, but requirements do not land in the project backlog.
- Every change is treated with the same weight and thereby blocks operations.
- Exceptions are accepted verbally and never reviewed again.
- After go-live, asset, access, and supplier registers are not updated.
- Project teams optimize schedules without letting management decide on residual risks.
- Technical tests are performed, but findings are not connected with acceptance and operations.

## Fictional mini example

A fictional business unit wants to introduce a new SaaS tool for customer communication. The project owner completes the security check: external users, personal data content, and API integration are relevant. ISMS, data protection, procurement, and IT are involved. Before go-live, roles, MFA, data export, supplier contact, and incident reporting path are clarified. An open logging requirement is documented as a time-limited exception with a management follow-up.

Evidence:

- security check with risk class,
- tasks in the project backlog,
- data protection and supplier handoff,
- technical acceptances for access and MFA,
- time-limited exception for the logging requirement,
- updated asset and supplier register.
