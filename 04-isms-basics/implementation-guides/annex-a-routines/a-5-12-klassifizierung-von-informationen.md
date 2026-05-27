# A.5.12 — Classification of information

## Purpose

Classification of information makes visible how critical information is for confidentiality, integrity, availability, and traceability. It helps people and systems decide which protection measures, approvals, storage locations, transfer paths, and review routines are appropriate.

The value is not in having as many labels as possible, but in an understandable decision aid: Which information needs which handling, who may define the classification, when is it reviewed, and what consequences does it have in operations?

## Control objective in repository language

The organization operates a consistent, role-understandable classification routine for information in the ISMS scope. The routine connects information assets, business processes, protection needs, data classes, owner decisions, tooling, training, access, transfer, retention, and deletion.

## Typical risks

- If critical information is not recognized, it is processed in unsuitable repositories, tools, or communication channels.
- If everything is marked highly critical, labels lose their steering effect and teams bypass the rules.
- If business units do not understand the classification, inconsistent decisions and wrong protection measures arise.
- If classification is not connected to access, sharing, retention, and deletion, it remains a paper label without effect.
- If data protection, contractual, or confidentiality requirements are not considered, legal and business risks arise that require human review.

## Triggers

- New business process, new information asset, new system, or new data repository.
- Introduction or change of data classes, protection needs, or information types.
- New product, new service provider, new interface, or new transfer to third parties.
- Security event, misdirected sending, data leakage, audit finding, or customer requirement.
- Change in contracts, legal framework, or internal risk decisions.
- Periodic review of asset inventory, data flows, or protection needs.
- Migration to cloud, collaboration, or AI-supported work environments.

## Roles and responsibilities

- **Information Owner / Process Owner:** defines the business classification and protection need for information types.
- **ISMS Owner / Security role:** defines classification model, minimum logic, review, and escalation.
- **Data Protection / Legal:** reviews personal data, contractual obligations, confidentiality commitments, and legal questions.
- **IT/Platform Owner:** translates classification into repositories, access, labels, DLP, backup, or technical controls.
- **Business units:** apply classifications in daily work and report unclear information types.
- **Procurement / Supplier Management:** connects classification with service provider requirements and data sharing.
- **Management:** decides trade-offs, tolerances, and resources for protection measures.

## Implementation

### Minimum start

Goal: Introduce a few understandable classes with clear operational effect.

1. The organization defines three to four information classes in its own language, for example public, internal, confidential, strictly confidential.
2. For each class, typical examples and minimum actions are described: repository, access, sharing, sending, retention, disposal.
3. Critical information types in the ISMS scope receive an owner and a classification.
4. New or changed information types are checked through process, system, or supplier changes.
5. Unclear classifications are escalated to the Information Owner or ISMS Owner.
6. Application is checked through sampling.

Minimum evidence:

- classification model with examples,
- list of critical information types with owner and class,
- decision note for classifications,
- training or communication evidence,
- sample or review note.

### Solid practice

Goal: Classification steers concrete protection measures and reviews.

1. The classification model is connected to asset inventory, data flows, access control, information transfer, and retention.
2. Owners review classifications for new systems, process changes, service provider involvement, and material risks.
3. Each class has minimum protection: approval, encryption, storage location, external sharing, printing, disposal, backup, and logging, where appropriate.
4. Data Protection and Legal handoffs are triggered when personal data, confidentiality commitments, or contractual requirements are affected.
5. Misclassification, missing labels, or unclear data flows are handled as findings.
6. Classification is integrated into onboarding and role-based training.

Strong evidence:

- classification policy in the organization's own language,
- information asset register with classification,
- protection measures matrix per class,
- owner review decisions,
- evidence from samples or corrective actions,
- management decision on protection/usability conflicts.

### Advanced practice

Goal: Classification is integrated into data and tool governance.

1. Classification can be supported in collaboration tools, document management, email, DLP, or cloud platforms.
2. Data flows, interfaces, and AI use are steered based on information class.
3. Automated or assisted labels are safeguarded through owner reviews and misclassification processes.
4. Metrics show coverage of critical information types, label quality, exceptions, and corrections.
5. Classification feeds into supplier assessment, incident triage, BCM, access, cryptography, and deletion concepts.
6. Management receives a decision-ready view of particularly sensitive information holdings and open trade-offs.

## Routine flow

1. **Information type arises or changes:** new process, data flow, system, report, contract, or dataset.
2. **Determine owner:** clarify business responsibility and decision authority.
3. **Assess protection need:** evaluate impacts of disclosure, alteration, loss, or unavailability.
4. **Define class:** decide using the organization model and typical examples.
5. **Derive handling consequences:** determine access, repository, sending, external sharing, retention, deletion, and technical measures.
6. **File evidence:** document classification, rationale, owner, and review date.
7. **Check application:** sample, tool evaluation, incident evaluation, or business-unit review.
8. **Correct:** remediate wrong classifications, missing owners, or unsuitable repositories.

## Decisions

- Which information classes are understandable and sufficient for the organization?
- Who may define or change classifications?
- Which information types are so critical that management or Legal/Data Protection must be involved?
- Which minimum measures apply per class?
- How are conflicts between easy collaboration and protection needs decided?
- How often are classifications reviewed?
- Which tools may process which information classes?

## Evidence

### Strong evidence

- current classification model with examples and handling consequences,
- information asset register with owner, class, and review date,
- documented classification decisions for new processes or systems,
- samples with corrective actions,
- training evidence for relevant roles,
- management decisions on protection-need conflicts,
- evidence that classification steers access, transfer, or repository.

### Weak evidence

- general policy without examples or operational consequences,
- labels in documents without owner or review,
- long class list that nobody uses in daily work,
- protection needs analysis without connection to repository and access,
- training slide without evidence of application.

### Evidence gaps

- critical information types without owner,
- classification not visible in the asset register,
- external sharing without classification decision,
- no review of misclassifications,
- personal or contractually protected information without handoff.

## Effectiveness review

Review questions:

- Can business units explain the classes and apply them to their own information?
- Are critical information types recorded with owner and review date?
- Does a higher class actually lead to different protection measures?
- Are new systems and service providers reviewed based on information class?
- Are misclassifications found and corrected?
- Are Legal/Data Protection questions for sensitive information types visibly escalated?

Possible metrics:

- share of critical information assets with current classification,
- number of unresolved information types,
- findings from classification samples,
- overdue reviews,
- exceptions from minimum protection measures,
- misdirected-sending or repository incidents related to classification.

## BSIG/NIS2 connection point

Information classification has a connection point to NIS2-oriented risk management measures, access protection, secure information processing, supply chain security, incident handling, business continuity, and governance. It helps make protection needs and evidence traceable, but does not replace organization-specific legal assessment.

The concrete relevance should be assessed in the requirements register, in risk analyses, and in relevant management decisions.

## Boundaries

- No legal or data protection advice and no binding classification of personal data.
- No certification, conformity, or security guarantee.
- No ISO 27002 text or replacement for the standard.
- Classification alone does not protect information; it must trigger measures.
- No real customer, personal, contract, or secret data in examples.

## Handoffs

- **Data Protection handoff:** personal data, special sensitivity, data subject rights, deletion, purpose limitation, or evaluations.
- **Legal handoff:** contractual secrets, confidentiality commitments, export/sector requirements, disputes.
- **IT/Platform handoff:** technical labels, DLP, storage locations, encryption, backup, access.
- **Supplier handoff:** sharing classified information with service providers or subcontractors.
- **Incident handoff:** misdirected sending, data leakage, wrong repository, or unauthorized access.
- **Management handoff:** high protection requirements, resource needs, usability conflicts, risk acceptance.
- **Audit/Evidence handoff:** missing owners, outdated classifications, or decisions that are not traceable.

## Typical mistakes

- Too many classes are defined and ignored in daily work.
- Classification is understood as a labeling project, not as a protection-decision routine.
- Business units have no examples for their information types.
- Confidential information can still be shared freely in technical terms.
- Classifications are never reviewed, even though processes and systems change.
- Data Protection and Legal are involved only after misdirected sending.
- Management receives no view of protection-need conflicts.

## Fictional mini example

A fictional business unit introduces a supplier portal. At project start, contracts, support tickets, and technical interface data are recorded as information types. The Process Owner classifies contracts as confidential and interface keys as strictly confidential. This leads to restricted storage locations, an approval process for external sharing, and a Data Protection/Legal handoff for personal support data. A sample after three months finds two documents stored incorrectly; the business unit corrects the repository and adds a short briefing.

Evidence:

- information asset entries with owner and class,
- classification decision in the project minutes,
- protection measures per class,
- sample result,
- corrective action and short briefing.
