# A.7.10 — Handling of storage media

## Purpose

Storage media can transport, duplicate, or continue to contain large amounts of information requiring protection after use. This routine ensures that USB sticks, external hard drives, backup media, memory cards, mobile data carriers, decommissioned drives, and comparable media do not arise informally, lie around, get passed on, or get disposed of without control.

The core is not “ban USB”, but an operated media logic: Which media are allowed, who is responsible for them, which data may be placed on them, and how are they protected, transported, erased, destroyed, and evidenced?

## Control objective in repository language

The organization operates a routine for storage media across the full lifecycle: need, approval, labeling or assignment, use, transport, storage, return, secure deletion, destruction, and exception handling.

## Typical risks

- If unencrypted media are lost, confidential or personal information can be disclosed.
- If media are used without inventory, owner, return, deletion, and accountability are missing.
- If old hard drives, backup tapes, or memory cards are not handled securely before disposal, data remains reconstructable.
- If external media are connected without checking, malware, data leakage, or uncontrolled copies can arise.
- If backup or export media are not stored securely, recoverability and confidentiality can both be at risk.
- If media go to service providers, authorities, customers, or repair sites, handover, return, and deletion can become unclear.

## Triggers

- Need for data transport, backup, export, migration, forensics, repair, or archiving.
- Issue, return, shipping, loss, or finding of a storage medium.
- Procurement or decommissioning of devices with built-in data carriers.
- Project end, system migration, service provider change, or contract end.
- Security event, malware suspicion, suspected data leakage, or data protection review.
- Change of data classification, encryption rule, or endpoint policy.
- Regular media inventory, backup, or disposal review.

## Roles and responsibilities

- **Information Owner / Asset Owner:** decides which data may be stored on media and which protection need applies.
- **IT / Endpoint / Backup Owner:** provides approved media, encryption, blocking rules, deletion, and technical control.
- **User / Business unit:** uses media only as approved, protects them, and reports loss or deviations.
- **ISMS Owner / Security Role:** defines media classes, minimum protection, exception, and review logic.
- **Data Protection / Legal:** reviews personal data, handovers, consequences of loss, and contractual questions in human review.
- **Procurement / Supplier Management:** manages media destruction, repair, shipping, external storage, or service provider handovers.
- **Management:** decides on residual risks, exceptions, resource needs, or non-recoverable media.

## Implementation

### Minimum start

Goal: Storage media with information requiring protection are limited, assigned, and protected.

1. The organization defines which media types are allowed in scope and which should generally not be used.
2. Media with information requiring protection are assigned to an owner, purpose, and return point.
3. Minimum requirements apply to permitted media: encryption, secure storage, no private use, loss reporting, secure deletion or destruction.
4. Built-in data carriers from decommissioned or repaired devices are assessed before handover.
5. Loss, finding, or unclear media status is treated as a security event.
6. Exceptions are time-limited and documented with a risk decision.

Minimum evidence:

- media rule or short standard,
- list of issued or critical media with owner,
- evidence of encryption or secure storage,
- deletion/destruction evidence,
- loss/incident ticket or exception decision.

### Solid practice

Goal: The media lifecycle is embedded in operations, backup, endpoint, disposal, and supplier management.

1. Media are classified by purpose and protection need: transport medium, backup medium, export medium, forensic medium, archive medium, device data carrier.
2. Technical policies regulate connection, write permissions, encryption, and logging where appropriate.
3. Issue, transport, external handover, and return are tracked through tickets or handover records.
4. Secure deletion and destruction are performed using a traceable method and evidence.
5. Backup and archive media are protected against loss, theft, damage, and unauthorized access.
6. Service providers for destruction, repair, or storage are managed through contracts, orders, and evidence.
7. Media events feed into incident response, data protection review, and lessons learned.

Strong evidence:

- media classification and permitted use,
- media inventory with owner, purpose, data class, and status,
- handover, shipping, or return records,
- technical policies or endpoint evaluations,
- deletion or destruction evidence,
- service provider confirmation,
- incident and exception decisions.

### Advanced practice

Goal: Media control is integrated with data classification, DLP, backup resilience, and disposal processes.

1. Endpoint and DLP rules restrict or monitor media use in a risk-based way.
2. Encryption and key management are regulated for media use and recovery.
3. Backup media are regularly checked for recoverability and secure storage.
4. Device retirement connects asset inventory, secure deletion, disposal, and evidence management.
5. Media losses or unusual export patterns trigger security or data protection triage.
6. Management receives decision-ready metrics on media exceptions, losses, destruction gaps, and backup/archive risks.

## Routine flow

1. **Media need arises:** transport, backup, export, repair, migration, forensics, or archiving.
2. **Clarify purpose and data class:** Which information should go onto the medium and why?
3. **Define approval and protection:** permitted media type, encryption, storage, transport, return, and deletion.
4. **Issue or use:** medium is assigned, labeled, or recorded in the register.
5. **Control transport or handover:** make recipient, handover path, and return point traceable.
6. **Close:** delete data, return, reuse, or destroy medium.
7. **Secure evidence:** file ticket, register, deletion/destruction evidence, or handover record.
8. **Treat deviation:** escalate loss, finding, malware suspicion, or unknown media status.
9. **Improve:** feed patterns from losses, exceptions, or shadow use back into rules and technology.

## Decisions

- Which storage media are generally allowed, restricted, or prohibited?
- Which data classes may be placed on transportable media?
- When is encryption, four-eyes handover, or special storage required?
- Which deletion or destruction method is appropriate for which media class?
- Who may accept media exceptions and for how long?
- When does media loss become an incident, data protection, or management topic?
- How are service providers for destruction, repair, and storage reviewed?

## Evidence

### Strong evidence

- current media standard with roles and triggers,
- media register with owner, purpose, data class, and status,
- evidence of encryption or technical media control,
- handover, shipping, return, and deletion records,
- destruction certificate or documented internal destruction evidence,
- incident ticket for loss or finding,
- time-limited exception with risk decision,
- management decision for unclear or critical media risks.

### Weak evidence

- blanket statement “USB is prohibited” without technical or organizational check,
- list of USB sticks without data class or owner,
- destruction invoice without reference to specific media,
- screenshot of an endpoint rule without review or exception handling,
- backup rule without storage or recovery evidence.

### Evidence gaps

- media with information requiring protection without assignment,
- decommissioned devices without deletion or destruction evidence,
- external handovers without recipient and return documentation,
- loss without incident or data protection review,
- backup media without protection or restore evidence,
- exceptions without expiry date.

## Effectiveness review

Review questions:

- Are permitted and non-permitted media types regulated understandably?
- Can critical media be assigned to an owner, purpose, and status?
- Is there evidence of secure deletion or destruction before handover?
- Are external handovers, shipping, and repairs controlled traceably?
- Are media losses reported and assessed quickly enough?
- Are backup and archive media both protected and recoverable?
- Do exceptions and findings lead to corrections?

Possible metrics:

- number of issued critical media,
- open or overdue returns,
- media exceptions by data class,
- deletion/destruction evidence per disposal wave,
- media losses and handling time,
- unauthorized media connections, where technically collected and clarified under data protection requirements.

## BSIG/NIS2 connection point

Handling storage media can connect to NIS2-oriented risk management measures, cyber hygiene, protection of information, incident handling, business continuity, and supply chain security in disposal or external storage. The concrete connection should be assessed in the requirements register and in data/asset processes.

This artifact does not replace legal review of data protection consequences, reporting obligations, retention obligations, or applicability.

## Boundaries

- This artifact is not a detailed cryptography, backup, or forensics guide.
- It does not replace data protection review for personal data on media.
- It does not replace contractual review of disposal, repair, or storage service providers.
- It makes no certification or conformity commitment.
- It must not contain real media numbers, location details, or confidential data in public examples.

## Handoffs

- **IT/endpoint handoff:** media approval, connection control, encryption, deletion, and technical evaluations.
- **Backup/BCM handoff:** backup media, recoverability, offsite storage, and emergency access.
- **Data Protection/Legal handoff:** personal data, loss, external handover, retention, and deletion obligation questions.
- **Incident handoff:** loss, finding, malware suspicion, unclear copy, or possible data leakage.
- **Procurement/supplier handoff:** destruction, repair, transport, external storage, or service provider confirmation.
- **Management handoff:** critical exception, unclear media status, investment need, or accepted residual risk.
- **Audit/evidence handoff:** missing deletion, destruction, handover, or return evidence.

## Typical mistakes

- Media are prohibited, but exceptions arise informally.
- Hard drives from old devices are treated as electronic waste, not as data carriers.
- Backup media are checked for availability, but not protected for confidentiality.
- Destruction evidence does not show which media were affected.
- External handovers to service providers run without return or deletion confirmation.
- Loss reports are treated as a procurement issue, not as a security event.
- Technical blocks are introduced without regulating justified special cases.

## Fictional mini example

A fictional business unit wants to hand over customer data for a migration to a service provider on an external SSD. The Information Owner requires encryption, a handover record, and return or deletion confirmation. IT provides an approved medium and documents the assignment in the ticket. After completion, the service provider confirms deletion, the Asset Owner closes the ticket, and the ISMS Owner includes the exception rate in the next review.

Evidence:

- approval ticket with purpose and data class,
- media register entry,
- evidence of encryption,
- handover record,
- deletion confirmation from the service provider,
- review note on the media exception.
