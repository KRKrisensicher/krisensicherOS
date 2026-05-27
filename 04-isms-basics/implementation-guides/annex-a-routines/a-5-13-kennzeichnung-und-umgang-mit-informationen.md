# A.5.13 — Labeling and handling of information

## Purpose

Labeling and handling of information translate classification into visible behavior. People, teams, and systems should be able to recognize how information must be handled: where it is stored, who may share it, which channels are permitted, and how it is printed, transported, archived, or disposed of.

The core is not an attractive label on documents, but a practical handling routine that reduces misdirected sending, wrong storage, unsuitable tools, and unclear responsibilities.

## Control objective in repository language

The organization operates a traceable routine for labeling and handling classified information. The routine connects information classes, concrete handling rules, tool support, training, sampling, exception handling, and handoffs to Data Protection, Legal, IT, Supplier Management, and Incident Response.

## Typical risks

- If confidential information is not visibly labeled, it may accidentally be shared through wrong channels.
- If labels have no handling consequences, employees treat all information the same.
- If handling rules are too complicated, workarounds arise, such as private repositories, shadow IT, or uncontrolled copies.
- If physical documents, printouts, or meeting notes are forgotten, protection measures remain limited to digital documents.
- If external parties do not understand labels, information can be processed incorrectly despite internal rules.

## Triggers

- Introduction or change of a classification model.
- New document templates, collaboration tools, data rooms, DMS, email, or cloud platforms.
- New information type, data repository, process documentation, or external sharing.
- Misdirected sending, wrong storage, discovery of paper documents, data leakage, or incident.
- Audit finding, customer requirement, or supplier requirement.
- Migration, archiving, disposal, or larger clean-up action.
- Periodic sample of label and handling quality.

## Roles and responsibilities

- **Information Owner / Process Owner:** defines how information in the relevant class is labeled and handled.
- **ISMS Owner / Security role:** defines minimum logic, training, samples, and escalation.
- **IT/Platform Owner:** supports labels, permissions, approvals, DLP, printing, or sharing settings.
- **Business units:** apply labeling and handling rules in documents, tickets, repositories, meetings, and communication.
- **Data Protection / Legal:** reviews personal data, confidentiality obligations, external notices, and disputes.
- **Procurement / Supplier Management:** ensures that external parties understand and confirm handling requirements.
- **Management:** decides trade-offs between usability, cost, tooling, and protection needs.

## Implementation

### Minimum start

Goal: Make critical information recognizable and manageable in daily work.

1. The organization defines simple handling rules for each information class: repository, sharing, sending, printing, meeting, disposal.
2. Critical document types or information types receive clear labeling examples.
3. Templates or headers/footers are adapted for frequently used documents where useful.
4. Business units receive a short decision aid: “If this information has this classification, then use this handling.”
5. Missing or wrong labeling is recorded and corrected in samples.
6. Exceptions are justified and time-limited.

Minimum evidence:

- handling matrix per information class,
- labeling examples or templates,
- communication or training evidence,
- sample list with corrections,
- exception decision for different handling.

### Solid practice

Goal: Labeling and handling are systematically built into processes and tools.

1. Labels are connected to concrete tool rules: sharing, download, external approval, encryption, DLP, or storage location.
2. Physical information is considered: printouts, whiteboards, meeting documents, shipping, records destruction.
3. External sharing includes clear notices, expected handling, and contractual or business approvals where needed.
4. Incorrectly labeled or incorrectly handled information is treated as a finding with cause and measure.
5. Awareness and onboarding include practical examples from business units.
6. Reviews check not only labels, but actual handling.

Strong evidence:

- handling rules with handling consequences,
- configured tool or platform rules,
- templates and examples,
- sample protocols with corrections,
- evidence of physical disposal or secure shipping,
- external approval or contract evidence.

### Advanced practice

Goal: Handling rules are technically supported and continuously improved.

1. Sensitivity labels, DLP, data rooms, rights management, or encryption support handling where they create value.
2. Automatic notices or blocks are connected with exception processes and owner decisions.
3. External collaboration spaces are preconfigured by information class.
4. Misdirected-sending and DLP events feed into incident triage, training, and process improvement.
5. Metrics show label coverage, mislabeling, blocked or approved exceptions, and recurring error patterns.
6. Management receives decisions on tool investments, usability conflicts, and accepted residual risks.

## Routine flow

1. **Information is created or received:** document, dataset, ticket, export, printout, or meeting document.
2. **Check class:** use existing classification, information type, or owner decision.
3. **Apply label:** set label, metadata, template, folder rule, or accompanying notice.
4. **Choose handling:** perform storage, access, sending, printing, external approval, archiving, or disposal according to class.
5. **Check sharing:** verify recipient, purpose, channel, authorization, and external requirements.
6. **Generate evidence:** file approval, ticket, tool log, sample, or disposal evidence.
7. **Handle deviation:** report and correct wrong label, unsuitable channel, missing approval, or incident.
8. **Improve:** update examples, tool rules, or training based on findings.

## Decisions

- Which information classes need visible labels, and which are controlled through repository or system context?
- Which handling rules are mandatory, and which are recommended?
- Which channels are permitted for which information classes?
- Who may approve external sharing or deviations?
- When is mishandling treated as an incident?
- Which technical controls are helpful without blocking work disproportionately?
- How are physical documents and hybrid work practices covered?

## Evidence

### Strong evidence

- handling matrix with clear handling consequences,
- examples of correctly labeled document types,
- tool configurations for labels, sharing, or DLP,
- approvals for external sharing,
- samples with concrete corrections,
- evidence of secure disposal or shipping,
- lessons learned from misdirected sending or wrong storage.

### Weak evidence

- labeling policy without examples,
- documents with labels but without technical or organizational consequences,
- screenshot of a tool function without evidence of use,
- general training without reference to business-unit information,
- repository folder named “confidential” without access control.

### Evidence gaps

- no connection to classification,
- external sharing without approval or handling evidence,
- physical documents not considered,
- wrong labeling is not corrected,
- exceptions without owner, duration, or risk decision.

## Effectiveness review

Review questions:

- Can employees infer from a label what they must do or avoid?
- Are critical information types visibly steered in templates, tools, or repositories?
- Are mislabeling and mishandling detected and corrected?
- Are external recipients and collaboration spaces appropriately included?
- Are physical information, printouts, and disposal considered?
- Are exceptions traceable and time-limited?

Possible metrics:

- share of checked documents with appropriate label,
- number of mislabelings by area,
- misdirected-sending or wrong-storage events,
- overdue corrective actions,
- exception rate for external sharing,
- DLP/sharing events with confirmed assessment.

## BSIG/NIS2 connection point

Labeling and handling of information have a connection point to NIS2-oriented risk management measures, cyber hygiene, access protection, secure communication, supply chain security, incident handling, and governance. The concrete relevance should be assessed organization-specifically in risk analysis, requirements register, and management review.

This artifact does not replace legal or data protection assessment of information sharing, monitoring, or employee data.

## Boundaries

- No legal or data protection advice.
- No certification, conformity, or security guarantee.
- No ISO 27002 text or replacement for the standard.
- Labels alone are not a control if handling rules are not operated.
- No confidential or real organizational examples.

## Handoffs

- **Classification handoff:** unclear or missing classification of an information type.
- **IT/Platform handoff:** labels, DLP, sharing, encryption, templates, repository rules.
- **Data Protection/Legal handoff:** personal data, confidentiality obligations, external notices, monitoring, or disputes.
- **Supplier handoff:** external processing, data rooms, handling requirements, return or deletion.
- **Incident handoff:** misdirected sending, wrong publication, unauthorized sharing, or loss of physical documents.
- **Management handoff:** trade-offs, tool costs, accepted exceptions, or recurring error patterns.
- **Audit/Evidence handoff:** missing evidence for application, sampling, or correction.

## Typical mistakes

- Labels are introduced, but nobody knows the handling consequences.
- All confidential information can still be shared by standard email.
- Physical documents and printouts are not governed.
- External parties see internal labels but do not understand them.
- Tool blocks create shadow processes because exceptions are missing.
- Samples count only labels, not actual handling.
- Mislabeling is corrected, but causes are not addressed.

## Fictional mini example

A fictional sales team uses proposal templates with the label “confidential.” A sample shows that price lists are labeled correctly but are shared through open project folders. The Information Owner decides that price lists may only be stored in a restricted data room. IT adapts the template and folder permissions. A short team briefing explains when external approvals are permitted and when Legal must be involved.

Evidence:

- handling matrix for confidential sales documents,
- sample protocol,
- corrected folder permissions,
- updated template,
- team briefing evidence,
- open Legal handoff rule for external special cases.
