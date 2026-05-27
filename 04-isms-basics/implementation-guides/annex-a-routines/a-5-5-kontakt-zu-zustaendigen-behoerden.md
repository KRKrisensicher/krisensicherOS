# A.5.5 — Contact with competent authorities

## Purpose

Contact with competent authorities ensures that an organization does not have to look for relevant public bodies, supervisory authorities or reporting offices only during a serious event. The objective is a prepared, approved contact and escalation routine — without prematurely assessing legal reporting obligations itself.

## Control objective in repository language

The organization operates a routine with which competent authority contacts, communication paths, internal approvals and human gates for authority communication can be maintained, tested and activated during events.

## Typical risks

- If authority contacts are only researched during a security event, time and coordination capability are lost.
- If it is unclear who may communicate externally, contradictory or unapproved statements arise.
- If legal assessment, data protection and incident response are not connected, reports may be prioritized incorrectly or prepared late.
- If contact lists become outdated, urgent information reaches the wrong bodies or no one.
- If exercises exclude authority communication, the organization remains uncertain during a real event.
- If real incident data is shared without control, confidentiality, data protection or investigative interests may be impaired.

## Triggers

- security event, near miss, crisis situation or suspicion of a reportable matter.
- change in regulatory affectedness, sector, location, service or critical processes.
- new or changed official contact paths, portals, reporting formats or contacts.
- crisis exercise, incident tabletop or lessons learned.
- management decision on external communication or crisis organization.
- planned review of the contact list and approval routine.
- external request from an authority or public warning with organizational relevance.

## Roles and responsibilities

- **Incident manager / security role:** recognizes possible authority relevance and starts internal escalation.
- **ISMS owner:** maintains contact and routine logic, evidence and review dates.
- **Legal / compliance:** assesses legal reporting, information or communication questions.
- **Data protection role:** assesses personal-data aspects and possible data protection notifications.
- **Management / crisis team:** decides external communication, approvals, resources and escalation.
- **Communications / PR:** coordinates wording, timing and connected external communication.
- **Business or service owner:** provides robust facts on affected services, customers, data or impacts.

## Implementation

### Minimum start

Objective: The organization knows whom to involve internally during an event and where approved authority contacts are stored.

1. Relevant authority and reporting bodies are recorded as contact categories, not as a legal assessment.
2. For each category, it is defined who internally takes over assessment and approval.
3. A contact list contains official websites, portals, phone numbers or mailboxes as well as a review date.
4. The incident process contains a stop point: escalate possible authority relevance to legal, data protection and management.
5. External communication takes place only through approved roles.
6. The contact list is reviewed at least annually and after exercises or incidents.

Minimum evidence:

- authority contact list with source and review date,
- internal approval and escalation matrix,
- incident stop point for authority relevance,
- review note,
- exercise or incident record with lessons learned.

### Solid practice

Objective: Authority contact is integrated into incident, crisis management and governance.

1. Contact categories are connected with scenarios: cyberattack, data protection event, outage of critical services, suspicion of criminal relevance, sector-specific situation.
2. Reporting or information questions are managed as legal/data protection human gates.
3. Communication templates contain only structural questions, no unchecked statements or legal claims.
4. Exercises test whether internal approvals, facts and contact paths work.
5. Official information, warnings or feedback are fed back into risk, incident or measures routines.
6. Contact lists are versioned and maintained with deputies.

### Advanced practice

Objective: External interfaces are operated as part of the situation picture and crisis capability.

1. Authority contacts, CERT/CSIRT information, sector warnings and crisis communication are integrated into a situation picture.
2. In exercises under time pressure, roles can decide what must be assessed internally, approved and communicated externally.
3. Fact management separates confirmed information, assumptions, open questions and approved statements.
4. Management, legal, data protection, communications, incident response and BCM work with coordinated escalation levels.
5. After events, contact paths, response times, decision quality and documentation are reviewed.
6. Interfaces to service providers consider who supports authority contact and which information can be provided.

## Routine flow

1. **Maintain contact basis:** update relevant official contact sources, portals and internal approval roles.
2. **Recognize event:** incident, outage, request or warning may have authority relevance.
3. **Trigger human gate:** involve legal, data protection, management and communications before external statements are made.
4. **Secure facts:** structure affected services, times, impacts, data types, measures and uncertainties.
5. **Decide:** whether, when, through which channel and with which approved content communication takes place.
6. **Communicate:** only through authorized roles and traceable channels.
7. **Document:** record contact attempt, content, approvals, times and feedback.
8. **Follow up:** transfer lessons learned into contact list, incident process, exercises and management review.

## Decisions

- Which categories of authorities or reporting offices are relevant for the organization to assess?
- Who may approve and perform external authority communication?
- Which events trigger legal, data protection, management or crisis team handoff?
- Which facts must be at least robust before external communication?
- How are assumptions, uncertainties and not-yet-reviewed information handled?
- How is official feedback transferred into measures and risk work?

## Evidence

### Strong evidence

- current contact list with official sources, owner and review date,
- escalation matrix for authority relevance and external approvals,
- incident or crisis process with authority human gate,
- exercise record with tested contact and approval routine,
- incident file with times, approvals, contact paths and feedback,
- lessons learned with process or contact list changes,
- management decision on external communication.

### Weak evidence

- uncommented link list without owner or review date,
- general sentence “authorities are informed” without approval path,
- outdated phone numbers in an emergency folder,
- communication templates without legal/data protection review,
- exercise without external communication decision.

### Evidence gaps

- no internal approval role for authority contact,
- no connection to the incident or crisis process,
- unclear separation between facts, assumptions and approved statements,
- contact list not traceable to official sources,
- service providers cannot deliver relevant facts in time,
- external request is answered without documentation.

## Effectiveness review

Review questions:

- Is it clear which role recognizes and escalates possible authority relevance?
- Are contact sources current and traceable to official bodies?
- Are legal, data protection, management and communications involved in time?
- Can the organization document facts and approvals traceably?
- Has the contact and communication routine been exercised?
- Do feedback or warnings flow into risk and measures work?

Possible metrics:

- currency of the contact list,
- share of exercises with an authority communication scenario,
- time until internal escalation when authority relevance is possible,
- open lessons learned from communication exercises,
- external requests with complete documentation,
- service provider contacts with defined fact delivery path.

## BSIG/NIS2 connection point

Authority contact is connectable to NIS2-oriented incident capability, crisis communication, management oversight, situation picture and possible reporting or information processes. The concrete connection must be assessed organization-specifically by legal, data protection and responsible roles.

This artifact does not make a binding assessment of any reporting obligation, deadline or authority responsibility.

## Boundaries

- No legal advice and no binding assessment of reporting obligations.
- No data protection advice or assessment of personal data breaches.
- No template for real authority reports with organizational data.
- No certification or conformity assurance.
- No disclosure of confidential, personal or investigation-relevant information without human review.

## Handoffs

- **Incident handoff:** possible authority relevance, suspicion of criminal relevance, significant security incident or external request.
- **Legal handoff:** reporting obligations, information duties, criminal complaint, contractual or regulatory questions.
- **Data protection handoff:** personal data, possible personal data breach, communication with affected persons.
- **Management/crisis team handoff:** external communication, resources, situation decision, reputational or operational impact.
- **Communications handoff:** coordinated statements, connected media or customer communication.
- **Vendor handoff:** facts from service provider operation, managed service, cloud or third-party product.
- **Audit/evidence handoff:** evidence on approvals, contact paths and lessons learned.

## Typical mistakes

- Authority contact is only researched during the incident.
- Security communicates externally without involving legal, data protection or management.
- Contact lists contain private notes instead of official sources.
- Reporting obligations are speculatively assessed in the technical team.
- Communication templates contain overly specific statements before facts are secured.
- Service providers do not deliver usable times or affectedness information.
- Exercises test technology, but not decision-making and external communication.

## Fictional mini example

A fictional cloud service provider exercises a ransomware suspicion. During the tabletop exercise, the incident manager recognizes possible authority relevance and triggers the internal stop point. Legal and data protection assess the situation, and management decides for the time being to collect facts only and not to submit any external report without further assessment. The contact list is updated because an official portal was linked out of date.

Evidence:

- exercise record with triggered authority handoff,
- updated contact list with official source,
- legal/data protection review assignment,
- management decision on communication approval,
- lessons-learned measure for fact management.
