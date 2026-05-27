# A.7.13 — Maintenance of equipment

## Purpose

Maintenance ensures that in-scope equipment is maintained reliably, securely and traceably without unnecessarily exposing information, configurations or operating environments. This does not only mean repairs, but the managed routine around maintenance need, service provider access, spare parts, logging, return to operation and open residual risks.

## Control objective in repository language

The organisation operates a traceable maintenance routine for equipment with an information security connection. Maintenance is planned, authorised, accompanied, documented and followed up; specific risks from external technicians, replaced components, storage media, remote maintenance or unplanned repairs are visibly decided.

## Typical risks

- If equipment is maintained in an unplanned or informal way, configurations may be changed, protection measures disabled or data disclosed.
- If external maintenance personnel receive unsupervised access to equipment or rooms, unclear responsibility and opportunities for misuse arise.
- If defective components with data carriers or memory are removed, information may leave the organisation.
- If maintenance windows are not aligned with operations and change management, critical services may fail.
- If maintenance evidence is missing, deviations, exceptions and recurring defects remain invisible.

## Triggers

- Planned maintenance date, manufacturer requirement or service contract.
- Disruption, defect, security event or unusual equipment behaviour.
- Site change, equipment move, replacement procurement or decommissioning.
- External maintenance on site or remote access by manufacturer, service provider or managed service.
- Change in protection need, new risk assessment or audit finding.
- Recurring review of critical equipment, maintenance contracts and open repairs.

## Roles and responsibilities

- **Asset owner / equipment owner:** defines criticality, protection need and approval for maintenance.
- **IT / facility operations:** coordinates date, access, accompaniment, technical execution and return to operation.
- **ISMS owner / security role:** defines minimum requirements, exception handling and evidence logic.
- **Service provider / supplier management:** reviews contract, scope of services, contacts and escalation paths.
- **Data protection / Legal:** review personal data, contractual issues, remote access or data exfiltration risks.
- **Management:** decides in cases of resource shortages, critical exceptions or unacceptable residual risks.

## Implementation

### Minimum start

Goal: make maintenance of critical equipment controlled and evidenced.

1. Critical equipment in the ISMS scope is recorded with owner, location and maintenance responsibility.
2. Maintenance takes place only based on a ticket, order or documented approval.
3. External maintenance is accompanied or technically limited; remote access is limited in time and scope.
4. Removed components with possible information content are handled separately.
5. After maintenance, it is checked whether the device, protection measures and configuration are operational again.
6. Deviations and unfinished repairs are documented with follow-up date.

Minimum evidence:

- equipment list with owner and criticality,
- maintenance ticket or order,
- evidence of approval and execution,
- return-to-service / functional check,
- exception or deviation note.

### Solid practice

Goal: maintenance is connected with operations, supplier management and risk management.

1. Equipment is classified by criticality, location, data connection and maintenance model.
2. Maintenance windows are aligned with change management, service owners and operating times.
3. External accesses are controlled through visitor, access, remote-access or service provider processes.
4. Data carriers, memory modules and replaced components receive clear handling: return, deletion, destruction or retention.
5. Recurring defects lead to root-cause analysis, replacement planning or risk decision.
6. Maintenance contracts, contact channels and escalations are regularly reviewed.

Strong evidence:

- classified equipment / asset register,
- maintenance plan and maintenance records,
- change or service tickets,
- evidence of accompaniment or limitation of external access,
- component evidence when replaced,
- measure log for deviations and recurring errors.

### Advanced practice

Goal: maintenance is managed proactively and integrated into resilience, monitoring and supplier management.

1. Critical equipment provides condition, warranty, patch or maintenance indicators into a central operational picture.
2. Maintenance events are linked with configuration management, vulnerability management and spare-part strategy.
3. Remote maintenance uses approved access paths, logging and time-limited activation.
4. Critical maintenance dependencies feed into BCM, emergency planning and Management Review.
5. Supplier performance is assessed based on response time, quality, security requirements and open risks.
6. Metrics show overdue maintenance, unplanned repairs, recurring defects and exceptions.

## Routine flow

1. **Maintenance need arises:** planned date, disruption, manufacturer notice, monitoring or review.
2. **Review scope and criticality:** determine device, location, data connection, service impact and owner.
3. **Clarify approval and date:** define maintenance type, access, accompaniment, maintenance window and service provider.
4. **Perform:** implement maintenance in a controlled way, document changes and component replacement.
5. **Check return:** verify function, protection measures, configuration and operational release.
6. **File evidence:** secure ticket, record, deviation, component evidence and open points.
7. **Follow up:** handle defects, exceptions, recurring patterns or supplier problems.
8. **Escalate:** give critical outages, data risks or unfunded replacement needs to management.

## Decisions

- Which equipment is considered critical and needs managed maintenance?
- Which types of maintenance may be performed internally, externally, remotely or only when accompanied?
- How are removed components with possible information content handled?
- Which maintenance windows are compatible with service or BCM requirements?
- When is repair no longer appropriate and replacement required?
- Who may accept exceptions and for how long?

## Evidence

### Strong evidence

- current asset register with owner, location and criticality,
- approved maintenance orders or tickets,
- records with performed work and deviations,
- evidence of external access, accompaniment or remote approval,
- return-to-service check after maintenance,
- component or data carrier evidence,
- management decision for critical exceptions or replacement need.

### Weak evidence

- general maintenance contract without equipment and owner connection,
- individual invoices without security or return-to-service check,
- informal email agreements without status and deviations,
- asset list without maintenance history,
- statement “the service provider does it” without service evidence.

### Evidence gaps

- critical equipment without owner or maintenance plan,
- external maintenance without evidence of access, remote access or accompaniment,
- removed components without evidence of whereabouts,
- maintenance changes configuration without review,
- open defects without risk decision.

## Effectiveness review

Review questions:

- Are critical devices and their maintenance responsibilities known?
- Can it be traced for a sample when and by whom maintenance was performed?
- Are external and remote maintenance activities controlled and documented?
- Are data carriers or storage-capable components handled securely?
- Do maintenance deviations lead to measures, replacement planning or management decision?
- Are maintenance windows aligned with operational and emergency requirements?

Possible metrics:

- overdue maintenance of critical equipment,
- unplanned repairs per equipment category,
- open maintenance deviations,
- external maintenance without complete evidence,
- recurring defects,
- critical replacement needs without decision.

## BSIG/NIS2 connection point

Equipment maintenance is connectable to NIS2-oriented topics such as operational stability, resilience, physical security, supplier management, access protection and risk management for critical assets. The specific connection should be assessed in the requirements register, in the asset register and for critical maintenance dependencies in Management Review.

This artefact does not replace legal assessment and does not replace binding review of applicability or evidence obligations.

## Boundaries

- This artefact is not a technical maintenance manual and not a manufacturer specification.
- It does not replace contractual, data protection or occupational safety review.
- It makes no statement on certifiability or legal fulfilment.
- It contains no licensed standards texts and no confidential equipment details.
- It is not sufficient as evidence if maintenance is actually unmanaged.

## Handoffs

- **Facility / IT operations handoff:** planning, access, maintenance window, return to operation.
- **Supplier handoff:** external technicians, manufacturers, managed service, service-level problems.
- **Change handoff:** maintenance changes configuration, firmware, network connection or service availability.
- **Data protection / Legal handoff:** personal data, remote access, contractual or liability questions.
- **BCM handoff:** maintenance or defect affects critical services or emergency equipment.
- **Management handoff:** replacement investment, permanent exception, unacceptable residual risk.
- **Audit / evidence handoff:** missing evidence for maintenance, access or component whereabouts.

## Typical mistakes

- Maintenance is treated as a purely technical topic without owner and protection need.
- External maintenance receives broad access to rooms or equipment.
- Removed components are treated like normal spare material.
- After maintenance, no one checks whether protection measures are active again.
- Critical equipment has maintenance contracts but no internal review routine.
- Recurring defects are repaired but not escalated as a risk or replacement need.

## Fictional mini example

A fictional production site has maintenance performed on a network device that provides connectivity to a warehouse area. The IT owner creates a ticket, agrees a maintenance window with the service owner and accompanies the external technician. After replacement of a memory module, its whereabouts are documented. The return-to-service check shows a deviating configuration, which is corrected and tracked in the ticket. In the next review, a decision is made to include similar devices in spare-part planning.

Evidence:

- maintenance ticket with approval,
- accompaniment and access note,
- component evidence,
- return-to-service check,
- corrective measure,
- review decision on spare-part planning.
