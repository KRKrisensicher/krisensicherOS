# A.6.7 — Secure working outside controlled locations

## Purpose

Secure working outside controlled locations ensures that information, devices, access and conversations remain protected when people work from home, while travelling, at customer sites, in co-working spaces, on trains or in other uncontrolled places. The core is an operable routine: clear rules, suitable technical equipment, reporting paths, reviews and decisions on exceptions.

## Control objective in repository language

The organisation defines and operates how mobile, hybrid and external work is securely enabled. The routine connects roles, data classes, devices, network access, physical environment, behaviour, support, incident reporting and management decisions.

## Typical risks

- If protection-worthy information is processed in unsuitable environments, third parties can see screens, printouts, conversations or documents.
- If private or unmanaged devices are used, protection measures, updates, erasure capability and evidencability are missing.
- If connections are made without appropriate protection, credentials, sessions or data flows may be endangered.
- If mobile devices are lost or stolen, information leakage can occur without encryption, locking and a reporting path.
- If managers and employees handle exceptions informally, inconsistent risks and unclear responsibilities arise.

## Triggers

- Introduction or change of home office, mobile work or travel rules.
- Entry, role change or assumption of a role with sensitive information.
- Issue, change, loss or return of mobile devices.
- New tool, cloud service, VPN/zero-trust access or collaboration platform.
- Work at customer sites, while travelling, in co-working environments or public places.
- Security event, device theft, misdirected sending, shoulder-surfing indication or rule violation.
- Periodic review of remote-work risks, device inventory and exceptions.

## Roles and responsibilities

- **HR / people function:** anchors work models, onboarding and rule communication.
- **Managers:** decide within defined rules on work locations, tasks and everyday transfer.
- **ISMS owner / security role:** defines minimum requirements, risk logic, reporting paths and reviews.
- **IT/platform owner:** provides devices, access protection, encryption, updates, remote erasure and support processes.
- **Information owner / business unit:** defines which data or activities are permitted outside controlled locations.
- **Data protection / Legal:** reviews employee data, workplace rules, personal data processing and contractual questions.
- **Management:** decides on residual risks, equipment, exceptions and culture/productivity conflicts of objectives.

## Implementation

### Minimum start

Goal: outside controlled locations, work is not improvised but performed with clear minimum rules.

1. The organisation defines for which roles and activities mobile or external work is permitted.
2. Minimum rules are communicated understandably: protect screens, consider conversations, lock devices, secure documents, report loss immediately.
3. Critical data classes or activities are named that may only be processed under additional conditions or not outside controlled locations.
4. Managed devices, strong authentication, device encryption and secure connection are defined as standard where required in scope.
5. Exceptions are documented with justification, duration and responsible decision.
6. Loss, theft or suspected viewing has a visible reporting path.

Minimum evidence:

- remote/mobile work rule or compact work instruction,
- target group and activity scope,
- evidence of device issue or protection configuration,
- communication evidence for the reporting path,
- exception and incident tickets.

### Solid practice

Goal: secure working outside controlled locations is operated on a risk basis and repeatably.

1. Activities are classified by information risk and environment: home office, travel, customer, public, abroad, high-risk project.
2. Technical minimum measures are connected with roles and data classes: MDM, disk encryption, MFA, secure connection, automatic lock, backup, remote erasure.
3. Managers receive decision guidance on when tasks are unsuitable outside controlled locations.
4. Onboarding, device issue, awareness and incident reporting are linked.
5. Exceptions such as private devices, local printouts, travel with sensitive data or temporary special access are decided separately.
6. Reviews check device inventory, open exceptions, reported events and recurring rule problems.

### Advanced practice

Goal: mobile and hybrid work is managed as controlled operational capability with monitoring, support and learning loops.

1. Device compliance, access context, patch level and encryption status feed into access decisions.
2. Risk indicators such as unusual access, lost devices, frequent exceptions or unsafe travel environments are evaluated.
3. High-risk roles receive additional briefings, privacy filters, travel guidance, secure communication paths or alternative work modes.
4. Crisis, BCM and remote-work scenarios are considered together so emergency operation does not force unsafe workarounds.
5. Management receives decision-ready metrics on equipment gaps, exception rate, incident patterns and investment needs.

## Routine flow

1. **Work need arises:** person, role or team wants to work outside controlled locations.
2. **Classify activity:** manager and information owner check data class, task, location and risk.
3. **Check prerequisites:** device, authentication, connection, support, awareness and reporting path are available.
4. **Approve or limit:** activity is permitted, given conditions, bound to a controlled location or escalated.
5. **Perform:** employees comply with minimum rules and report loss, misconduct or suspicious circumstances.
6. **Record evidence:** device issue, rule communication, exception, incident or review are documented.
7. **Review:** recurring problems, exceptions and technical gaps are checked.
8. **Improve:** rules, equipment, training or access logic are adjusted.

## Decisions

- Which activities or data classes may be processed outside controlled locations?
- Which technical minimum measures are mandatory for which roles?
- Are private devices, printouts, local storage or public work locations permitted?
- Who may approve exceptions and how long do they apply?
- How are travel, foreign-country or customer-location situations assessed?
- Which investments are needed so secure work does not fail because of equipment gaps?

## Evidence

### Strong evidence

- approved remote/mobile work rule with role and data-class reference,
- device inventory with protection status for mobile devices,
- evidence of MFA, encryption, MDM or secure connection in scope,
- onboarding or awareness evidence for external work,
- exception decisions with duration,
- tickets for loss, theft, remote erasure or incident triage,
- review record on device inventory, exceptions and events.

### Weak evidence

- general home office rule without security reference,
- tool screenshot without assignment to roles or devices,
- verbal team agreements without evidence,
- device inventory without protection status,
- training attendance rate without practice or reporting-path reference.

### Evidence gaps

- unmanaged or private devices in productive access without decision,
- no reporting routine for lost devices or viewing by others,
- no requirements for public places, travel or printouts,
- exceptions without owner or expiry date,
- no review of events and recurring rule problems.

## Effectiveness review

Review questions:

- Do employees know what they must do, avoid and report outside controlled locations?
- Are mobile devices in scope managed, encrypted and traceably assigned?
- Are activities with high protection need checked before external processing?
- Can loss or theft be reported and handled quickly?
- Are exceptions time-limited and documented in a decision-ready way?
- Have reviews led to better rules, equipment or training?

Possible metrics:

- share of mobile devices with current protection status,
- open device or equipment gaps,
- number and age of remote-work exceptions,
- reporting time for loss or theft,
- incident patterns related to mobile work,
- coverage of critical roles by additional briefings.

## BSIG/NIS2 connection point

Secure working outside controlled locations is compatible with NIS2-oriented topics such as cyber hygiene, access protection, training, incident handling, business continuity and protection of critical services. The concrete connection should be assessed organisation-specifically in the requirements register and in risk analyses.

This artefact does not replace legal, data protection or employment-law review of work models, monitoring or employee data.

## Boundaries

- This artefact is not home-office legal advice and not an employment-law template.
- It does not replace data protection review for monitoring, device management or employee data.
- It is not a complete technical mobile device management baseline.
- It does not confirm conformity or security through a remote-work policy alone.
- It contains no ISO 27002 texts and no real personal or location data.

## Handoffs

- **HR handoff:** work model, onboarding, role change, departure, work-related communication.
- **IT handoff:** device issue, protection configuration, support, loss process, remote erasure.
- **Data protection/Legal handoff:** employee data, monitoring, private devices, work abroad, employment-law questions.
- **Access handoff:** access depends on device status, role, location or exception.
- **Incident handoff:** loss, theft, misdirected sending, suspicious access, possible viewing by third parties.
- **BCM handoff:** emergency operation, pandemic/crisis work, alternate workplaces and temporary workarounds.
- **Management handoff:** equipment gaps, conflicts of objectives, permanent exceptions or accepted residual risks.
- **Audit/evidence handoff:** missing evidence for devices, rules, exceptions or events.

## Typical mistakes

- Home office is allowed, but security prerequisites are not checked.
- Private devices are tolerated without risk decision or technical minimum requirement.
- Rule communication mentions no concrete reporting paths for loss or suspicion.
- Managers decide work locations without data-class or activity reference.
- Printouts, conversations and visual privacy are forgotten compared with technical measures.
- Device inventory and actual usage status do not match.
- Exceptions become permanent and disappear from review.

## Fictional mini example

A fictional consulting firm permits hybrid work. For a project with confidential tender documents, the project owner decides that processing while travelling is not permitted and home office may only take place with a managed device, MFA and privacy protection. An employee later reports the loss of a laptop on a train. IT locks the device, starts remote erasure and documents the process. In the review, it is decided to introduce travel briefings for project roles with high protection need.

Evidence:

- project-related work location decision,
- device and protection status,
- communication evidence for minimum rules,
- incident ticket for device loss,
- review measure for travel briefings.
