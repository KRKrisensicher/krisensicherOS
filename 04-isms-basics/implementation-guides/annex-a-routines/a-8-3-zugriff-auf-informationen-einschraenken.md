# A.8.3 — Restrict access to information

## Purpose

Information must be accessible where it is needed for legitimate tasks — and limited where access is unnecessary, risky or undecided. This routine connects information classification, roles, storage locations, applications and technical access controls into a reviewable way of working.

## Control objective in repository language

The organisation operates a routine that restricts access to information according to business need, protection need, roles, data storage location and risk. Business owners decide, IT implements in a controlled way, reviews check actual access, and exceptions are handled with time limits and traceability.

## Typical risks

- If sensitive information is stored in open locations, too many people can read, copy or change it.
- If roles and protection needs are not connected, permissions become too broad or permanent.
- If data ends up in shadow storage, exports or collaboration tools, it bypasses the intended access control.
- If external or project-related access is not time-limited, information remains open after the need ends.
- If reviews only check group lists but do not understand data stores and information assets, pseudo-controls emerge.

## Triggers

- new data storage location, application, share, database, report, interface or collaboration space.
- new data class, new project, new role or changed protection-need assessment.
- onboarding, role change, offboarding or end of external work.
- data migration, cloud/SaaS introduction, new interface or reporting export.
- security event, mistaken sharing, audit finding or data protection question.
- periodic review of critical information assets and access groups.

## Roles and responsibilities

- **Information Owner / Data Owner:** defines protection need, permitted roles and approval logic.
- **Process / Business Unit Owner:** confirms business need and project-related access.
- **IT / Platform Owner:** implements technical access restrictions, groups and storage locations.
- **ISMS Owner / Security role:** defines minimum logic, review frequencies, exceptions and evidence requirements.
- **Data Protection / Legal:** reviews personal, confidential or contractually bound information and analyses.
- **Management:** decides on conflicts between operational capability, transparency, protection need and resources.

## Implementation

### Minimum start

Goal: do not operate critical information in open or unreviewed storage locations.

1. The most important information assets in scope are named: data stores, applications, reports, interfaces or project areas.
2. Each critical asset has an Information Owner.
3. The owner defines permitted roles or groups and justifies deviations.
4. New access is granted via ticket or documented approval.
5. External, project-related and elevated access is time-limited.
6. Critical storage locations are regularly checked for open groups, old access and unclear owners.

Minimum evidence:

- list of critical information assets with owner,
- access model or role/group assignment,
- approval tickets,
- review record for critical storage locations,
- exception decisions with expiry date.

### Solid practice

Goal: access restriction is connected to data classification, role model and review.

1. Information assets are described by protection need, process, data class and storage location.
2. Role or group models represent standard access; special access requires additional approval.
3. Data stores and collaboration tools receive clear rules for ownership, approval, external links and sharing.
4. Access reviews consider actual content, external access, project durations and role changes.
5. Data exports, reports and interfaces are treated as separate access paths.
6. Findings lead to clean-up, role model adjustment, training or management decision.

Strong evidence:

- information register or data storage overview,
- protection-need and role logic,
- group/permission exports at the review date,
- review decisions with corrections,
- evidence of removed open links or external access,
- exception and action log.

### Advanced practice

Goal: information access is continuously controlled from data context, identity and usage signals.

1. Data classification, IAM, DLP/CASB/SaaS reports and asset register provide a shared situational picture.
2. Access to sensitive information is limited on a risk basis through device, location, role or context signals.
3. Open shares, mass exfiltration, unusual exports or external links trigger triage.
4. Projects and data rooms have automatic expiry or recertification logic.
5. Interfaces and technical accounts are reviewed with data scope, purpose and owner.
6. Management sees decision-ready metrics on open storage locations, external shares, old access and data movements.

## Routine flow

1. **Information access arises:** new asset, project, role, report, interface or sharing.
2. **Classify information:** clarify owner, protection need, data class, storage location and business need.
3. **Define access model:** standard roles, special access, external access, technical access and expiry date.
4. **Approve and implement:** document business decision; IT implements groups or controls.
5. **Review use:** identify open links, broad groups, external access, exports and old permissions.
6. **Perform review:** confirm, restrict, withdraw, time-limit or escalate.
7. **Control exceptions:** justified, risk-assessed, with follow-up and compensation.
8. **Improve:** adjust role model, storage structure, training or tooling.

## Decisions

- Which information is critical enough for a prioritised start?
- Who decides on data access when process owner and system owner differ?
- Which data may be placed in collaboration tools, exports or external shares?
- Which accesses are standardised, and which require individual approval?
- How long are project, external or special accesses valid?
- When is operational capability weighted higher than strict restriction — and who accepts the risk?

## Evidence

### Strong evidence

- information or data storage register with owner and protection need,
- defined role/group models,
- approved access requests with purpose and duration,
- technical permission exports or SaaS reports,
- review records with withdrawal, restriction or confirmation,
- evidence of remediated open links, old access or external shares,
- management decision for conflicts or permanent exceptions.

### Weak evidence

- general access policy without information reference,
- permission list without explanation of data or roles,
- screenshots of individual shares without date and owner,
- statement “only the business unit has access” without export or review,
- data classification without technical implementation.

### Evidence gaps

- critical data stores without Information Owner,
- open groups such as “all employees” without justified need,
- external links without expiry date,
- reports and exports outside the review scope,
- technical accounts with data access without purpose and owner.

## Effectiveness review

Review questions:

- Are critical information assets and owners known?
- Can it be explained who may access a sensitive storage location and why?
- Are external, project-related and technical accesses time-limited and reviewed?
- Do reviews lead to actual clean-up of open or old access?
- Are data exports, reports and interfaces visible as access paths?
- Are conflicts between collaboration and protection need decided instead of solved informally?

Possible metrics:

- critical information assets with owner and review date,
- open or very broad shares,
- external access without expiry date,
- overdue access reviews,
- removed old permissions,
- exceptions by data class or business unit.

## BSIG/NIS2 connection point

Restricted information access is compatible with NIS2-oriented topics such as access protection, risk management, cyber hygiene, protection of critical information, incident prevention and secure supply chain/service provider access. The concrete connection should be assessed in the requirements register, data classification and access concept.

This artefact does not replace legal or data protection assessment of data processing, employee analyses or disclosure obligations.

## Boundaries

- This artefact is not a complete role model or DLP architecture.
- It does not replace data protection, secrecy, contract or legal review.
- It makes no certification or conformity commitment.
- It contains no real data stores, customer information or internal permission lists.
- A policy without technical implementation and review is not an effective access restriction.

## Handoffs

- **Access / IAM handoff:** roles, groups, joiner-mover-leaver, technical accounts.
- **Data protection / Legal handoff:** personal data, confidential information, external sharing, contractual binding.
- **Business unit handoff:** owner decision, business need, project duration and data quality.
- **DLP / Monitoring handoff:** open links, unusual exports, mass movements or external forwarding.
- **Incident handoff:** mistaken sharing, unauthorised access, suspected data leakage.
- **Management handoff:** broad sharing for operational reasons, resource or tooling conflicts, accepted residual risks.
- **Audit / Evidence handoff:** missing owners, missing review or unclear exception handling.

## Typical mistakes

- Access is reviewed system-centrically even though data exists in several places.
- Open collaboration spaces are treated as a culture question instead of a protection-need decision.
- External links and project rooms continue after project end.
- Data exports and BI reports bypass the actual permission concept.
- Business units confirm permissions generically because roles are hard to understand.
- Data classification is maintained but not connected to access controls.
- Technical accounts and interfaces are forgotten during review.

## Fictional mini example

A fictional manufacturer introduces a new project room for product data. The Information Owner classifies the data as internally critical and defines three roles: core team, read access for support and time-limited external access for a service provider. During the first review, a public sharing link for an export is found. The link is removed, the export process is adjusted, and external access receives an expiry date in future.

Evidence:

- entry in the information register,
- role and approval decision,
- permission export for the review,
- ticket to remove the sharing link,
- adjustment of the export process,
- review note on expiry dates for external access.
