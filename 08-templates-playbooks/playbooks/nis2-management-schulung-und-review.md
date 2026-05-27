# NIS2 Executive Management Training and Management Review

## Situation / Trigger

Use when an organization wants to translate NIS2 readiness into management capability: training, decision routine, resource approval, risk acceptance, evidence capability, and follow-up.

This playbook does not replace legal advice, data protection assessment, or a management decision. It prepares decisions.

## Goal

Executive management should be able to make regular and traceable decisions on:

- whether NIS2 applicability indicators exist and have been legally reviewed,
- which material risks and services are relevant,
- which measures are prioritized,
- which resources, owners, and deadlines are needed,
- which evidence is available in the management review,
- which training and knowledge evidence is created.

## Roles

| Role | Task |
| --- | --- |
| Management / executive management | decides priorities, resources, risk acceptance, escalations |
| Management review facilitator | prepares agenda, decision questions, minutes, and follow-up |
| information security officer/CISO | provides risk situation, measure status, incident readiness, and escalations |
| Legal/lawyer | reviews applicability, obligations, and external statements |
| Data protection | reviews data protection interfaces |
| Risk Owner | is responsible for risks and residual risk templates |
| Measure owner | reports progress, blockers, evidence, and resource needs |
| Evidence Reviewer | checks whether evidence is findable, current, and decision-ready |

## Source anchors

- BSIG § 38 — implementation, monitoring, and training obligation for executive management: <https://www.gesetze-im-internet.de/bsig_2025/__38.html>
- BSIG § 30 — risk management measures: <https://www.gesetze-im-internet.de/bsig_2025/__30.html>
- BSIG § 32 — notification obligations: <https://www.gesetze-im-internet.de/bsig_2025/__32.html>
- EnWG § 5e for energy relevance: <https://www.gesetze-im-internet.de/enwg_2005/__5e.html>
- NIS2 Directive: <https://eur-lex.europa.eu/eli/dir/2022/2555/oj?locale=de>

## Training routine for executive management

### Training objective

The training should not create slide knowledge, but decision readiness:

- understand the NIS2/BSIG context as a management task,
- identify and assess risks and risk management practices,
- assess impacts on services, operations, customers, and supply chain,
- understand incident and notification triage,
- document own decisions, approvals, and follow-ups cleanly.

### Minimum modules

| Module | Core question | Output / evidence |
| --- | --- | --- |
| Applicability and legal review | What working assumption exists and what has Legal reviewed? | Legal review handoff / decision log |
| Risk and service logic | Which services, systems, and dependencies are material? | Risk register / service mapping |
| Risk management measures | Which measures have been decided, blocked, or underfunded? | Measures backlog |
| Incident and notification capability | Who decides for 24h/72h/final logic? | Incident triage exercise note |
| Supply chain and service providers | Which providers are critical or cannot provide evidence? | Supplier/MSP review note |
| Evidence and supervisory readiness | Which evidence is available and which is missing? | Evidence pack index |
| Risk acceptance and resources | What is accepted, funded, postponed, or escalated? | Management decision |

### Training evidence

| Field | Entry |
| --- | --- |
| Training date |  |
| Participating roles |  |
| Modules |  |
| Open questions |  |
| Decisions / conditions |  |
| Follow-up owner |  |
| Next review date |  |

## Management review routine

### Cadence

Recommended as operating logic:

- initial NIS2 management review after preliminary applicability check,
- then monthly during the build-up phase,
- quarterly in regular operation,
- additionally after significant incidents, relevant findings, scope changes, or regulatory changes.

### Agenda

| Agenda item | Decision question | Input | Output |
| --- | --- | --- | --- |
| 1. Applicability / legal review | Has the preliminary classification been legally reviewed or is it open? | Questionnaire, legal handoff | Legal review status |
| 2. Scope and material services | Which services/units are in scope? | Service/sector mapping | confirmed scope / open scope questions |
| 3. Top risks | Which risks require a management decision? | Risk register | priority / acceptance / measure |
| 4. Measure status | What is overdue, blocked, or ready for decision? | Backlog | decision, owner, deadline |
| 5. Incident readiness | Has notification/triage capability been exercised and is it decision-ready? | Triage playbook, exercise note | approval / exercise assignment |
| 6. Supply chain | Which service provider/MSP/MSSP risks are open? | Supplier register | evidence/contract/exit assignment |
| 7. Evidence pack | Is evidence sufficient for review and supervisory readiness? | Evidence pack index | evidence gaps and owners |
| 8. Resources | Which capacity, budget, or external support is needed? | Options | management decision |
| 9. Training status | Is executive management trained and able to follow up? | Training evidence | next training / refresher |
| 10. Follow-up | What will be reviewed by when? | Decision log | updated follow-up |

## Decision logic

Each decision is recorded as one of the following forms:

- **Decision:** measure is implemented; owner, deadline, and evidence output are clear.
- **Condition:** decision postponed, but specific additional information is requested.
- **Risk acceptance:** residual risk is consciously accepted; rationale and review date required.
- **Escalation:** topic goes to Legal, data protection, crisis team, supervisory preparation, or budget committee.
- **Stop:** no sufficient basis for decision; evidence or legal review is missing.

## Evidence Pack for Management Review

| Evidence | Purpose | Owner |
| --- | --- | --- |
| Preliminary applicability questionnaire | working assumption and open legal review | NIS2 Scope Precheck Analyst / Legal |
| Legal review handoff | legal clarification of applicability and obligations | Legal/lawyer |
| Risk register | top risks and residual risk | information security officer/CISO / Risk Owner |
| Measures backlog | implementation status and blockers | Measure owner |
| Incident triage exercise note | notification and escalation capability | Incident Owner |
| Supplier/MSP review note | third-party risks | Service Owner / Procurement |
| Evidence pack index | evidence capability | Evidence Reviewer |
| Executive management training evidence | knowledge and review routine | Management review facilitator |
| Decision Log | decisions, conditions, deadlines | Management review facilitator |

## Agent support

| Agent | Use | Boundary |
| --- | --- | --- |
| `management-review-facilitator` | agenda, decision brief, follow-up | no management decision |
| `nis2-scope-precheck-analyst` | applicability indicators and legal handoff | no legal decision |
| `nis2-readiness-analyst` | gaps, measures, evidence needs | no compliance assurance |
| `risk-and-obligation-prioritizer` | prioritization of risks/measures | no risk acceptance |
| `incident-readiness-coach` | triage exercise and escalation logic | no live crisis leadership |
| `control-evidence-architect` | evidence packs | no effectiveness guarantee |
| `agent-quality-and-safety-reviewer` | claim safety and human gates | no technical approval |

## Stop points

Stop and clarify with humans when there is:

- missing legal review of applicability,
- unclear risk acceptance,
- missing management owner,
- budget or resource decision,
- personal data,
- external communication,
- regulatory or contractual interpretation,
- false assurance without evidence.

## Output

- training agenda,
- training evidence,
- management review agenda,
- decision log,
- measures and evidence follow-up,
- next review cadence.
