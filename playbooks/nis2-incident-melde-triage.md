<!-- kso:product-relevance
repo-scope: product
classification: playbook
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->

# NIS2 Incident and Notification Triage

## Situation / Trigger

Use when a security event, technical signal, provider notice, vulnerability finding, or outage may potentially be relevant under NIS2.

This playbook is intended for readiness, exercises, and initial structuring. It does not replace live incident response, legal advice, data protection assessment, or an official notification decision.

## Goal

Within the first situation points, it should become clear:

- what is known,
- what is only an assumption,
- which services, systems, data classes, and organizational units may be affected,
- whether a NIS2/BSIG/special-regime notification assessment is required,
- who must decide legally, operationally, and communicatively,
- which evidence must be prepared for 24h/72h/final logic.

## Roles

| Role | Task | Decision? |
| --- | --- | --- |
| Incident Owner | leads triage, coordinates situation points, keeps the decision log current | internal escalation yes, external notification no without approval |
| Technical specialist role | provides facts on systems, logs, timeframe, affected services | no legal decision |
| Service Owner | assesses impact on service, users, customers, operations | operational impact assessment |
| ISB/CISO | assesses security severity, priority, and need for action | security escalation |
| Legal/lawyer | reviews notification obligations, applicability, external communication | legal approval |
| Data protection | reviews personal data and GDPR notification path | data protection approval |
| Communication | prepares internal/external communication | sending only after approval |
| Management/crisis team | decides resources, risk acceptance, customer/authority communication | management decision |

## Source Anchors

- NIS2 Directive: <https://eur-lex.europa.eu/eli/dir/2022/2555/oj?locale=de>
- BSIG: <https://www.gesetze-im-internet.de/bsig_2025/>
- BSIG § 32 notification obligations: <https://www.gesetze-im-internet.de/bsig_2025/__32.html>
- BSIG § 36 feedback from the Federal Office: <https://www.gesetze-im-internet.de/bsig_2025/__36.html>
- EnWG § 5d for energy context: <https://www.gesetze-im-internet.de/enwg_2005/__5d.html>
- Implementing Regulation (EU) 2024/2690: <https://eur-lex.europa.eu/eli/reg_impl/2024/2690/oj?locale=de>
- BSI NIS2 for IT/TK and Implementing Regulation: <https://www.bsi.bund.de/DE/Themen/Regulierte-Wirtschaft/NIS-2-regulierte-Unternehmen/Sektorspezifische-NIS-2-Informationen/NIS-2-fuer-IT-und-TK/NIS-2-fuer-IT-und-TK_node.html>

## Triage Principles

1. Separate facts and assumptions.
2. Document the time at which awareness was obtained.
3. No external communication without approval.
4. Involve legal/data protection/sector assessment early.
5. Prepare notification readiness without asserting a notification obligation.
6. Secure evidence, but do not claim forensic assessment by agents.
7. Update the decision log after each situation point.

## Process: First 0 to 30 Minutes

| Step | Question | Output | Owner |
| --- | --- | --- | --- |
| Capture signal | What was detected when and by whom? | incident signal note | Incident Owner |
| Mark time of awareness | When did internal awareness begin? | time anchor for notification assessment | Incident Owner + Legal |
| Separate facts/assumptions | Which observations are confirmed? | fact list / assumption list | Technical specialist role |
| Set preliminary scope | Which services/systems/locations/data classes are affected? | preliminary scope | Service Owner |
| Check immediate escalation | Is there a risk to critical services, operations, confidentiality, integrity, or availability? | internal escalation decision | ISB/CISO |

## Process: First 30 to 90 Minutes

| Step | Question | Output | Owner |
| --- | --- | --- | --- |
| Check applicability context | Is the organization possibly an important/particularly important entity or subject to a special regime? | reference to preliminary applicability check | NIS2 Scope Precheck Analyst + Legal |
| Check notification path | Are BSIG, EnWG, DORA, GDPR, contract, or customer affected? | notification path matrix | Legal/Data protection |
| Assess severity preliminarily | Are there significant impacts, critical services, user impact, downtime, data/system compromise? | severity working assumption | ISB/CISO + Service Owner |
| Check Implementing Regulation | Are DNS/TLD/cloud/data center/CDN/MSP/MSSP/online marketplace/search engine/social network/trust service affected? | 2024/2690 review note | Legal + business owner |
| Set communication situation | Who may say what internally/externally? | communication approval or stop | Management/Communication |

## Prepare 24h/72h/Final Logic

The specific notification obligation and deadline must be legally reviewed. This playbook only prepares the information logic.

| Situation point | Purpose | Minimum content as working logic | Approval |
| --- | --- | --- | --- |
| Early initial notification / 24h logic | quick orientation on whether a significant security incident may exist | time of awareness, affected services, suspicion of malicious/unlawful act, possible cross-border impacts, immediate measures | Legal/Management |
| 72h logic | confirmed or updated assessment | severity level, impacts, compromise factors, ongoing measures, open assumptions | Legal/Management |
| Interim notification | status update in case of new situation or request | new facts, measure status, impact change | Incident Owner + Legal |
| Final logic | summary after stabilization | description, severity/impact, likely cause, completed and ongoing remedial measures, cross-border impacts if relevant | Management/Legal |

## Notification Path Matrix

| Path | Review question | Handoff | Status |
| --- | --- | --- | --- |
| BSIG/NIS2 | Possible important/particularly important entity and significant security incident? | Legal/lawyer, ISB/CISO | open |
| EnWG energy | Energy supply network, energy facility, or digital energy service under EnWG § 5c? | Legal, energy business owner | open |
| Implementing Regulation 2024/2690 | addressed type of digital entity and criteria for significant incident? | Legal, Service Owner | open |
| GDPR | personal data affected? | Data protection | open |
| Contract/customer | contractual notification obligations or customer communication? | Legal, Account/Communication | open |
| Authorities/public | external notification or press communication? | Management/crisis team | open |

## Evidence Pack for Incident Triage

| Evidence | Purpose | Internal storage location | Owner |
| --- | --- | --- | --- |
| Timeline | awareness, situation points, decisions |  | Incident Owner |
| Fact/assumption list | separation of reliable information |  | Technical specialist role |
| Scope note | affected services/systems/data classes |  | Service Owner |
| Log/alert references | technical basis |  | Technical specialist role |
| Decision log | who decided what and when |  | Incident Owner |
| Notification path review note | legal/data protection/sector assessment |  | Legal/Data protection |
| Communication approvals | internal/external statements |  | Communication/Management |
| Measures list | immediate measures and follow-up |  | ISB/CISO |

## Agent Support

| Agent | Use | Boundary |
| --- | --- | --- |
| `incident-readiness-coach` | triage questions, escalation map, exercise logic | no live crisis management |
| `nis2-scope-precheck-analyst` | structure applicability indicators and special regimes | no legal decision |
| `control-evidence-architect` | evidence pack and evidence logic | no effectiveness guarantee |
| `management-review-facilitator` | decisions, options, resource needs | does not decide itself |
| `agent-quality-and-safety-reviewer` | claim safety, human gates, stop points | no subject-matter approval |

## Stop Points

Escalate to humans immediately in case of:

- possible notification obligation,
- personal data,
- critical service impacts,
- cross-border impacts,
- customer/authority/press communication,
- unclear owner,
- risk acceptance or operational continuation decision,
- legal or data protection interpretation.

## Output

- completed incident triage note,
- notification path matrix,
- decision log,
- evidence pack list,
- handoff to Legal/Data protection/Management,
- lessons-learned backlog.

## Boundaries

- does not provide legal advice,
- does not provide data protection advice,
- no determination of a notification obligation,
- no live incident response,
- no external communication without approval,
- no real incident, customer, personal, or system data in public examples.
