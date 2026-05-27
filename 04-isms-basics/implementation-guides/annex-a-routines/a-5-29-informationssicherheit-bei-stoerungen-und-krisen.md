# A.5.29 — Information security during disruptions and crises

## Purpose

Information security during disruptions and crises ensures that security requirements do not disappear as soon as time pressure, outage, emergency operations, or crisis communication begin. The goal is a workable crisis routine that appropriately considers availability, confidentiality, integrity, traceability, and decision capability.

## Control objective in repository language

The organization integrates information security into disruption, emergency, and crisis flows. Critical security roles, minimum controls, communication paths, exceptions, decisions, and evidence are prepared so that they can also be used under pressure.

## Typical risks

- If crisis plans ignore security questions, insecure emergency access, uncontrolled data transfers, or non-traceable decisions arise.
- If emergency operations are improvised, exceptions remain in place permanently.
- If communication channels fail or are chosen insecurely, false information, confidential data, or attack surfaces may arise.
- If roles are unclear, incident response, BCM, IT operations, management, and business functions compete over decisions.
- If restart is optimized only for availability, compromised systems may return too early.
- If crisis decisions are not documented, residual risks and lessons learned are no longer traceable later.

## Triggers

- major IT disruption, security incident, service outage, or crisis team activation.
- activation of an emergency, restart, or crisis communication plan.
- outage of critical security functions such as IAM, monitoring, backup, email, or network segmentation.
- planned emergency, crisis, or tabletop exercise.
- significant architecture, supplier, or process change affecting crisis capability.
- management decision on emergency operations, prioritization, residual risk, or external communication.
- review after disruption, crisis, or exercise.

## Roles and responsibilities

- **Crisis team lead / BCM role:** coordinates overall decision, priorities, and crisis routines.
- **ISMS owner / Security role:** keeps security minimum requirements, risk notes, and escalations visible.
- **Incident Owner:** steers security incidents and distinction from pure operational disruptions.
- **Service Owner / Business function:** assesses business impact, emergency operations, and business priorities.
- **IT operations / platform team:** provides recovery, technical emergency actions, and security functions.
- **Communication / HR / Legal / Data protection:** review internal and external communication, employee, and data protection questions.
- **Management:** decides on conflicting objectives, resources, risk acceptance, and public or authority communication.

## Implementation

### Minimum start

Goal: do not forget security decisions during disruption and crisis.

1. Name critical disruption and crisis scenarios: identity outage, ransomware suspicion, cloud outage, communication outage, suspected data leakage.
2. Include a security and ISMS role in existing emergency contacts.
3. Define minimum rules for emergency operations: emergency access, data transfer, communication channels, logging, later rollback.
4. Document crisis decisions in an event log: decision, time, role, rationale, residual risk.
5. After a disruption or exercise, conduct a short security follow-up review.
6. Return exceptions from emergency operations with deadline and owner.

Minimum evidence:

- crisis contact list with security role,
- security checklist for emergency operations,
- event or decision log,
- exception and rollback evidence,
- lessons-learned note.

### Solid practice

Goal: information security is firmly embedded in BCM, incident response, and crisis management.

1. Crisis plans contain security checkpoints for restart, emergency access, communication, data extraction, and service providers.
2. Roles and escalation paths between incident response, BCM, IT operations, and management are aligned.
3. Critical security functions have fallback or minimum operating procedures.
4. Crisis exercises contain security injects: compromised identity, insecure communication, untrusted backup, supplier outage.
5. Decisions on deviations from security rules are time-limited, justified, and reviewed.
6. Lessons learned flow back into ISMS, BCM, awareness, supplier management, and technical architecture.

### Advanced practice

Goal: the organization keeps security governance decision-capable even in complex crisis situations.

1. Security situation picture, operational status, and business impact are considered together in crisis decisions.
2. Restart criteria combine availability with trustworthiness, integrity, and monitoring capability.
3. Emergency communication is prepared with secure alternative channels, approvals, and information classification.
4. Crisis exercises test several parallel stressors, such as ransomware, cloud outage, and media inquiry.
5. Crisis decisions are evaluated structurally: Was the security role involved early enough? Was evidence available? Were exceptions withdrawn?
6. Management receives decision-capable metrics on crisis capability, open weaknesses, and restart residual risks.

## Routine flow

1. **Recognize disruption or crisis:** event is classified as operational disruption, security incident, or combined situation.
2. **Activate roles:** involve crisis team, Incident Owner, ISMS/Security, Service Owner, and communication.
3. **Clarify security situation:** assess affected assets, data, access, integrity, monitoring, service providers, and communication channels.
4. **Decide emergency operations:** define minimum controls, exceptions, manual workarounds, and logging.
5. **Control restart:** check not only availability, but trustworthiness and control capability.
6. **Approve communication:** aligned internally and externally, with Legal/data protection handoff for sensitive content.
7. **Document decisions:** record time, role, rationale, risk, duration, and review date.
8. **Return to normal operations:** withdraw emergency access, workarounds, and exceptions or deliberately extend them.
9. **Follow up:** derive security lessons learned and actions.

## Decisions

- Which security minimum requirements also apply in emergency operations?
- When may availability be prioritized over security, and who accepts the residual risk?
- Which systems may go online again after a security suspicion?
- Which communication channels are permissible for crisis information?
- Which emergency access is allowed, logged, and reviewed afterward?
- When does a disruption become a security incident or a reporting/communication-relevant situation?
- Which service providers must be involved in crisis decisions?

## Evidence

### Strong evidence

- crisis or emergency plan with security roles and security checkpoints,
- event and decision log,
- documented emergency access and its rollback,
- restart check with integrity and security assessment,
- exercise protocol with security scenarios,
- actions from lessons learned,
- management decision on residual risks or resources.

### Weak evidence

- general crisis plan without security role,
- chat history as the only decision basis,
- restart note without integrity or access assessment,
- communication draft without approval and classification logic,
- exercise without evaluation or actions.

### Evidence gaps

- emergency access is not logged or withdrawn,
- exceptions from the crisis remain permanently active,
- security is involved only after restart,
- no secure alternative communication,
- no distinction between disruption, security incident, and crisis,
- missing documentation of risk decisions under time pressure.

## Effectiveness review

Review questions:

- Is information security visibly included in crisis roles, checklists, and exercises?
- Are security exceptions in emergency operations documented, time-limited, and rolled back?
- Are restart decisions also measured against integrity and control capability?
- Do communication and escalation paths work under outage conditions?
- Are crisis decisions later evaluated traceably?
- Do findings flow back into ISMS, BCM, incident response, and architecture?

Possible metrics:

- share of crisis exercises with security scenario,
- open actions from crisis lessons learned,
- overdue withdrawal of emergency access,
- time until security/ISMS involvement in critical situation,
- critical services with restart security check,
- undocumented crisis decisions from sample.

## BSIG/NIS2 connection point

This routine is compatible with NIS2-oriented topics such as business continuity, crisis management, incident handling, maintenance of essential services, secure communication, and governance under exceptional conditions.

For affected organizations, the concrete connection point should be assessed in the requirements register, in the BCM context, and in management review. This artifact does not replace legal assessment of reporting obligations, affectedness, or communication obligations.

## Boundaries

- This artifact is not a complete BCM or crisis team plan.
- It does not replace legal, data protection, communication, or occupational safety review.
- It does not guarantee availability, security, or conformity in crisis situations.
- It describes no binding reporting obligations.
- It uses only fictional, public-safe examples.

## Handoffs

- **BCM handoff:** activation of emergency plans, restart, prioritization of critical processes.
- **Incident handoff:** suspicion of compromise, data leakage, manipulation, or attack indicators.
- **IT operations handoff:** emergency access, recovery, monitoring, backup, technical workarounds.
- **Communication handoff:** internal situation communication, customer information, media inquiries, or stakeholder communication.
- **Legal/data protection handoff:** suspected reporting obligation, personal data, contractual questions, external statements.
- **Management handoff:** conflicting objectives, risk acceptance, resources, external communication, and prioritization.
- **Evidence handoff:** event log, decision evidence, exercise and lessons-learned records.

## Typical mistakes

- Crisis management focuses only on availability.
- Emergency access is set up, but not reviewed or withdrawn.
- Communication uses fast but unsuitable channels for confidential information.
- Systems go online again without checking integrity or suspicion of compromise.
- Security is seen as a blocker and therefore involved too late.
- Exercises end with a good feeling, but without an action log.
- Management decisions under time pressure are not documented.

## Fictional mini example

A fictional production service provider loses access to the central identity system during a major disruption. The crisis team activates an emergency procedure for two administration accounts, limited to four hours and with manual logging. The ISMS owner adds a security check for restart: review logs, withdraw emergency access, confirm monitoring. After the exercise, it is decided to introduce a secure alternative channel for crisis communication.

Evidence:

- crisis decision log,
- emergency access approval with duration,
- rollback protocol,
- restart security check,
- exercise lessons learned,
- management decision on the alternative channel.
