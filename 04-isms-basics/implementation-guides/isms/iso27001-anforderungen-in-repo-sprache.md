<!-- kso:product-relevance
repo-scope: product
classification: implementation-guide
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->

# ISO/IEC 27001 Requirements in krisensicherOS Language

## Purpose

This artifact translates ISO/IEC 27001 reference points into krisensicherOS language. It makes visible which routine, decision, role, evidence, and review can result from a reference point.

It contains no standard texts, no control wording, and no binding interpretation of the standard. Section numbers serve only as reference anchors.

## Boundaries

This artifact does not replace legal advice, data protection advice, certification advice, audit assessment, or management decision. It does not confirm fulfillment of external requirements.

## Use

1. Select section reference.
2. Review existing routine and owner.
3. Enter gap, decision, and evidence trail.
4. Mark human gate.
5. Transfer result into scope canvas, risk register, action backlog, evidence pack, or decision log.

## Translation Logic

| Reference term | krisensicherOS language |
| --- | --- |
| Requirement | Routine / decision point |
| Control | Safeguard / way of working |
| Audit criterion | Review question / evidence trail |
| Documentation | Evidence flow |
| Responsibility | Role with decision authority |

## Section Map

### Section 4.1 — Context Review Routine

- **Operating question:** Which internal and external factors influence what security governance is needed and operable?
- **Role with decision authority:** Executive management or delegated governance responsibility.
- **Routine:** Collect influencing factors; derive impacts on objectives, resources, and risks; mark assumptions; feed changes into scope and risk review.
- **Minimum artifacts:** Context register, assumptions log, influencing factors list, review note.
- **Evidence trail:** Dated context assessment with reference to scope or risk decision.
- **Review point:** Annually and upon material organizational, technology, threat, or regulatory changes.
- **BSIG/NIS2 reference:** § 28 BSIG and annexes for applicability indicators; § 30 BSIG indirectly through risk-based action planning.
- **Human gate:** Management confirms which context factors are relevant for steering.

### Section 4.2 — Expectations and Obligations Radar

- **Operating question:** Which parties, requirements, and evidence expectations influence the ISMS?
- **Role with decision authority:** Governance owner with legal/compliance and business owners.
- **Routine:** Record relevant parties; sort expectation types; convert requirements into review questions, decisions, or handoffs; escalate conflicts.
- **Minimum artifacts:** Stakeholder register, expectations log, obligations register, open clarification list.
- **Evidence trail:** Mapping from expectation to owner, decision, evidence, or clarification status.
- **Review point:** Upon new customer requirements, contracts, regulatory changes, or management reviews.
- **BSIG/NIS2 reference:** § 28 BSIG for possible applicability; § 30 and § 38 BSIG for governance and management references.
- **Human gate:** Legal, contractual, and regulatory classification only by responsible humans.

### Section 4.3 — Scope Decision Canvas

- **Operating question:** Which organizational units, services, processes, locations, systems, and interfaces belong to the ISMS operating scope?
- **Role with decision authority:** Executive management or ISMS sponsor.
- **Routine:** Collect scope candidates; justify inclusions and exclusions; make interfaces visible; record scope risks; obtain scope approval.
- **Minimum artifacts:** ISMS scope canvas, non-scope list, interface map, scope decision note.
- **Evidence trail:** Approved scope version with date, owner, and open scope questions.
- **Review point:** Upon organizational change, new critical services, outsourcing, M&A, or possible new applicability.
- **BSIG/NIS2 reference:** § 28 BSIG and annexes for entity/sector review; § 38 BSIG for management decision.
- **Human gate:** Final scope approval by responsible management.

### Section 4.4 — ISMS Operating Model

- **Operating question:** How is security governance operated as a recurring steering process?
- **Role with decision authority:** ISMS owner with management sponsor.
- **Routine:** Define core routines; specify roles, inputs, outputs, and escalations; version registers; connect reviews with decisions.
- **Minimum artifacts:** ISMS operating model, roles matrix, routines calendar, register overview, handoff map.
- **Evidence trail:** Review minutes, action statuses, decision logs, evidence pack index.
- **Review point:** Quarterly operationally, at least annually strategically.
- **BSIG/NIS2 reference:** § 30 BSIG for action steering; § 38 BSIG for management responsibility; § 32 BSIG for notification paths.
- **Human gate:** Management confirms operating model, resources, and responsibilities.

### Section 5.1 — Management Mandate Routine

- **Operating question:** How can it be recognized that management actively carries responsibility, priorities, and resources?
- **Role with decision authority:** Executive management.
- **Routine:** Connect security objectives with organizational objectives; decide resources; address top risks; decide effectiveness and improvement needs in the review.
- **Minimum artifacts:** Management mandate, decision log, resource decision, review agenda.
- **Evidence trail:** Decisions, priority decisions, management review minutes.
- **Review point:** During management review and for critical risks or resource blockers.
- **BSIG/NIS2 reference:** § 38 BSIG in case of possible applicability.
- **Human gate:** Management decides risk acceptance, budget, and escalations.

### Section 5.2 — Security Policy as Decision Framework

- **Operating question:** Which guardrails apply to decisions, priorities, and behavior in the ISMS?
- **Role with decision authority:** Executive management with ISMS owner.
- **Routine:** Formulate decision guardrails; communicate roles and expectations; link policy to routines; plan review and update.
- **Minimum artifacts:** Policy summary, communication evidence, review note, decision guardrails.
- **Evidence trail:** Approved policy version, announcement, change log.
- **Review point:** Annually and upon scope, strategy, or risk changes.
- **BSIG/NIS2 reference:** § 30 and § 38 BSIG indirectly through governance and action framework.
- **Human gate:** Management approves guardrails.

### Section 5.3 — Roles and Decision Rights Matrix

- **Operating question:** Who decides, who executes, who reviews, and who escalates?
- **Role with decision authority:** Executive management / ISMS sponsor.
- **Routine:** Identify roles; define decision rights and deputies; define escalation paths; review roles regularly.
- **Minimum artifacts:** Roles matrix, RACI-like work matrix, escalation map, deputy rule.
- **Evidence trail:** Approved roles list, changes, review minutes.
- **Review point:** Upon personnel changes, reorganization, incidents, or review findings.
- **BSIG/NIS2 reference:** § 38 BSIG for management and training reference.
- **Human gate:** Management confirms mandates and resources.

### Section 6.1.1 — Risk and Opportunity Working Mode

- **Operating question:** How does the ISMS identify relevant uncertainties and derive decisions from them?
- **Role with decision authority:** ISMS owner with risk owners.
- **Routine:** Collect relevant uncertainties; prioritize risks/opportunities; assign responsible parties; derive actions or decisions.
- **Minimum artifacts:** Risk log, opportunities/improvement list, prioritization, decision log.
- **Evidence trail:** Traceable assessment and follow-up decision.
- **Review point:** Regularly and upon context, scope, or incident changes.
- **BSIG/NIS2 reference:** § 30 BSIG as reference anchor for risk-related security measures.
- **Human gate:** Risk acceptance remains a management decision.

### Section 6.1.2 — Risk Assessment Routine

- **Operating question:** How are security risks described, assessed, and made comparable consistently?
- **Role with decision authority:** Risk owner, confirmed by ISMS owner.
- **Routine:** Describe risk scenario; map affected assets/services; record existing measures; document assessment and rationale; set review date.
- **Minimum artifacts:** Risk analysis register, assessment methodology, risk scenario, review calendar.
- **Evidence trail:** Dated assessment with rationale, owner, and change history.
- **Review point:** Upon new threats, vulnerabilities, incidents, scope changes, or due cadence.
- **BSIG/NIS2 reference:** § 30 BSIG for risk management measures.
- **Human gate:** Professionally approve methodology and assessment assumptions.

### Section 6.1.3 — Risk Treatment and SoA Working Logic

- **Operating question:** How are risks converted into actions, exceptions, acceptances, and evidence?
- **Role with decision authority:** Risk owner; management for residual risk and resources.
- **Routine:** Select treatment option; formulate action or acceptance decision; maintain safeguard references; define evidence and effectiveness review; document decision.
- **Minimum artifacts:** Risk-control map, action backlog, SoA extension, exception/acceptance log.
- **Evidence trail:** Connection between risk, action, owner, status, rationale, and review.
- **Review point:** Upon action completion, exception expiry, new risks, or management review.
- **BSIG/NIS2 reference:** § 30 BSIG for action planning and evidence capability.
- **Human gate:** Risk acceptance and action prioritization by responsible humans.

### Section 6.2 — Objective and Implementation Plan Routine

- **Operating question:** Which measurable work objectives drive the ISMS in the next period?
- **Role with decision authority:** ISMS owner with management sponsor.
- **Routine:** Derive objectives from risks and priorities; set owners and deadlines; define measurement or review criterion; report progress.
- **Minimum artifacts:** Objective register, action plan, progress report, review note.
- **Evidence trail:** Objective status, decisions on deviations, evidence of progress.
- **Review point:** Monthly operationally or according to agreed management cadence.
- **BSIG/NIS2 reference:** § 30 and § 38 BSIG indirectly through steering and management responsibility.
- **Human gate:** Objectives, priorities, and resources confirmed by management.

### Section 6.3 — Change Control for the ISMS

- **Operating question:** How are planned changes to the ISMS prepared and tracked in a controlled way?
- **Role with decision authority:** ISMS owner; management for scope/resource impact.
- **Routine:** Describe change; assess impact on scope, risks, roles, and evidence; define handoffs; approve and track change.
- **Minimum artifacts:** ISMS change log, impact note, approval, follow-up control.
- **Evidence trail:** Change decision, implementation status, review after implementation.
- **Review point:** After every major change and in the management review.
- **BSIG/NIS2 reference:** Relevant if the change influences applicability, notification paths, or risk management.
- **Human gate:** Human review of scope, obligation, or resource consequences.

### Section 7.1 — Resource Decision Routine

- **Operating question:** Which resources does the ISMS need to operate agreed routines realistically?
- **Role with decision authority:** Executive management / budget owners.
- **Routine:** Derive resource needs from objectives, risks, and backlog; mark bottlenecks; prepare options; document decision.
- **Minimum artifacts:** Resource need, capacity note, priority list, management decision.
- **Evidence trail:** Decision, budget/capacity allocation, open blockers.
- **Review point:** During management review, budget planning, and overdue actions.
- **BSIG/NIS2 reference:** § 38 BSIG for management and oversight reference.
- **Human gate:** Resource approval by responsible management.

### Section 7.2 — Competence Routine

- **Operating question:** Can the roles actually execute and decide their ISMS tasks?
- **Role with decision authority:** ISMS owner with HR/training and line managers.
- **Routine:** Define role-based capabilities; identify gaps; plan training or coaching; maintain evidence.
- **Minimum artifacts:** Competence matrix, training plan, participation/briefing evidence, role briefing.
- **Evidence trail:** Training evidence, enablement status, open gaps.
- **Review point:** Upon role changes, new routines, incidents, or annual training planning.
- **BSIG/NIS2 reference:** § 38 BSIG in case of possible executive management and training obligation.
- **Human gate:** Training needs and suitability reviewed by responsible roles.

### Section 7.3 — Awareness and Understanding of Responsibility

- **Operating question:** Do affected persons understand what security responsibility they have in daily work?
- **Role with decision authority:** ISMS owner with communications/HR role.
- **Routine:** Define target groups; derive core messages from roles and risks; conduct awareness formats; evaluate impact and questions.
- **Minimum artifacts:** Awareness plan, target group list, communication evidence, feedback note.
- **Evidence trail:** Completed actions, participation or alternative evidence, improvement log.
- **Review point:** Annually, upon new risks, or after relevant events.
- **BSIG/NIS2 reference:** Indirectly through security culture, management responsibility, and risk management.
- **Human gate:** Approve content for target groups and data classes.

### Section 7.4 — Communication Routine

- **Operating question:** Who communicates which security information to whom, when, and with which approval?
- **Role with decision authority:** Communications role with ISMS owner; legal/management for external communication.
- **Routine:** Define communication types; define internal and external recipients; clarify approvals; maintain communication evidence.
- **Minimum artifacts:** Communication matrix, approval log, distribution/recipient list, communication note.
- **Evidence trail:** Dated communication, approval, recipient group, follow-up action.
- **Review point:** Upon incidents, regulatory changes, management review, or communication failures.
- **BSIG/NIS2 reference:** § 32 BSIG for notification and communication paths; § 38 BSIG for management communication.
- **Human gate:** Have external statements, customer/authority communication, and legal assessment approved.

### Section 7.5.1 to 7.5.3 — Evidence Flow and Document Control

- **Operating question:** Which information must be findable, current, protected, and decision-ready?
- **Role with decision authority:** Evidence owner with ISMS owner.
- **Routine:** Define required evidence; specify storage, access, and versioning; determine protection needs; conduct regular evidence reviews.
- **Minimum artifacts:** Evidence pack index, document register, storage rule, review minutes.
- **Evidence trail:** Current versions, access clarification, change log, review status.
- **Review point:** Quarterly and before management review or internal reviews.
- **BSIG/NIS2 reference:** Evidence capability for § 30, § 32, and § 38 BSIG depending on context.
- **Human gate:** Review confidential, personal, or licensed content separately.

### Section 8.1 — Operational Planning and Control

- **Operating question:** How are ISMS routines planned, executed, monitored, and adapted when changes occur?
- **Role with decision authority:** ISMS owner with process and service owners.
- **Routine:** Maintain routines calendar; plan work packages; control changes; integrate outsourced services; track results.
- **Minimum artifacts:** Operating plan, action backlog, change note, outsourcing/interface list.
- **Evidence trail:** Completed routines, status reports, deviations, approvals.
- **Review point:** Monthly operationally, quarterly with risks and evidence.
- **BSIG/NIS2 reference:** § 30 BSIG for action operation; § 32 BSIG for incident/notification paths.
- **Human gate:** Approve material operational changes and outsourcing.

### Section 8.2 — Risk Analysis in Operation

- **Operating question:** How is it ensured that risk analyses do not remain one-time activities?
- **Role with decision authority:** Risk owner with ISMS owner.
- **Routine:** Conduct risk analysis according to cadence; capture new triggers; update assessment; adapt affected actions and decisions.
- **Minimum artifacts:** Updated risk register, review note, change log, open decisions.
- **Evidence trail:** Assessment history, owner, review date, follow-up actions.
- **Review point:** According to calendar and upon incidents, changes, supplier changes, or findings.
- **BSIG/NIS2 reference:** § 30 BSIG as reference anchor for ongoing risk steering.
- **Human gate:** Have assessment methodology and risk acceptance reviewed.

### Section 8.3 — Risk Treatment in Operation

- **Operating question:** Are agreed actions, exceptions, and acceptances actually implemented and reviewed?
- **Role with decision authority:** Risk owner / control owner; management for residual risk.
- **Routine:** Review action status; escalate blockers; update evidence; conduct effectiveness review; renew decisions.
- **Minimum artifacts:** Action backlog, risk-control map, exception log, effectiveness review.
- **Evidence trail:** Status, evidence, review decision, open residual risks.
- **Review point:** Monthly for actions, quarterly for risk/control effect.
- **BSIG/NIS2 reference:** § 30 BSIG for action operation and evidence capability.
- **Human gate:** Humans decide residual risk, exceptions, and resources.

### Section 9.1 — Monitoring and Assessment Routine

- **Operating question:** How does the organization recognize whether the ISMS works or needs adjustment?
- **Role with decision authority:** ISMS owner with management review facilitator.
- **Routine:** Define metrics and review questions; define data sources; assess results; prepare decisions.
- **Minimum artifacts:** Review indicators, monitoring note, evaluation report, decision questions.
- **Evidence trail:** Data basis, evaluation, management handoff.
- **Review point:** According to defined cadence and before management review.
- **BSIG/NIS2 reference:** Supports evidence capability for § 30 and management involvement under § 38 BSIG.
- **Human gate:** Professionally approve assessment and conclusions.

### Section 9.2.1 and 9.2.2 — Internal Review Planning and Execution

- **Operating question:** How does the organization itself review whether routines run and evidence is robust?
- **Role with decision authority:** Internal review/audit role with ISMS owner.
- **Routine:** Define review objective and scope; formulate review questions; request evidence; assess results; transfer findings into actions.
- **Minimum artifacts:** Review plan, review questions, evidence request list, finding report, action handoff.
- **Evidence trail:** Review minutes, samples, observations, follow-up decisions.
- **Review point:** According to review program, after incidents, or before external reviews/customer requests.
- **BSIG/NIS2 reference:** Internal reviews can support evidence and management capability without replacing an external statement.
- **Human gate:** Review program, findings, and escalations confirmed by responsible roles.

### Section 9.3.1 to 9.3.3 — Management Review Routine

- **Operating question:** Which decisions must management make based on risks, actions, evidence, and changes?
- **Role with decision authority:** Executive management.
- **Routine:** Collect input from risks, incidents, actions, reviews, and changes; formulate decision questions; document decisions; steer follow-up.
- **Minimum artifacts:** Management review agenda, decision brief, decision log, follow-up list, training/involvement evidence.
- **Evidence trail:** Minutes, decisions, requirements, owners, deadlines.
- **Review point:** At least according to defined management cadence and event-driven upon material events.
- **BSIG/NIS2 reference:** § 38 BSIG for management responsibility; § 30 and § 32 BSIG as possible input fields.
- **Human gate:** Management decides priorities, resources, and risk acceptance.

### Section 10.1 — Improvement Routine

- **Operating question:** How are improvement opportunities identified, prioritized, and implemented?
- **Role with decision authority:** ISMS owner with management for larger changes.
- **Routine:** Collect improvement sources; estimate impact and effort; assign owner and deadline; track implementation and review.
- **Minimum artifacts:** Improvement backlog, prioritization, implementation evidence, review note.
- **Evidence trail:** Source, decision, implementation, effectiveness check.
- **Review point:** In operational review and management review.
- **BSIG/NIS2 reference:** Indirectly through ongoing improvement of risk management and evidence capability.
- **Human gate:** Have prioritization and resource allocation approved.

### Section 10.2 — Nonconformity and Corrective Action Routine

- **Operating question:** How does the organization respond to deviations so that causes are addressed and recurrence is reduced?
- **Role with decision authority:** Corrective action owner with ISMS owner.
- **Routine:** Record deviation; review impact and cause; define corrective and preventive action; verify effectiveness; escalate to management if needed.
- **Minimum artifacts:** Deviation note, root cause analysis, corrective action plan, effectiveness review, decision log.
- **Evidence trail:** Observation, action, owner, deadline, effectiveness evidence.
- **Review point:** After action deadline and in improvement review.
- **BSIG/NIS2 reference:** Have § 32 BSIG reviewed for events close to notification relevance; § 30 BSIG for risk actions.
- **Human gate:** Human review of notification obligation, external communication, and risk acceptance.

### Annex A — Safeguard Reference Logic

- **Operating question:** Which safeguards does the organization need based on its risks, scope, and decisions?
- **Role with decision authority:** Risk owner with control owner; management for exceptions or residual risks.
- **Routine:** Maintain safeguard references only as IDs or own short labels; connect each action to risk, owner, routine, evidence, and review; justify non-application or exception; review effectiveness.
- **Minimum artifacts:** Risk-control map, SoA extension, action routine, exception/non-application rationale, evidence pack.
- **Evidence trail:** Connection between risk, safeguard, status, rationale, evidence, and review.
- **Review point:** Upon risk change, scope change, incident, finding, and management review.
- **BSIG/NIS2 reference:** § 30 BSIG for risk management measures; § 32 BSIG for incident/notification reference; § 38 BSIG for management decision.
- **Human gate:** Selection, non-application, exception, and residual risk approved by responsible humans.

## Quality Checklist

Before using or publishing a derived working version, review:

- No standard texts, tables, or control wording adopted.
- Section numbers used only as reference anchors.
- Every reference is translated into routine, decision, role, evidence, and review.
- No external fulfillment, legal, or audit statement included.
- BSIG/NIS2 references are marked as public reference anchors and not formulated as legal interpretation.
- Human gates for management, risk acceptance, legal, data protection, and external communication are visible.
- Confidential, personal, or licensed content remains outside the public repo.
