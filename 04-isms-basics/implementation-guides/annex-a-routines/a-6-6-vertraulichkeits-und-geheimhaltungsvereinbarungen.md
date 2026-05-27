# A.6.6 — Confidentiality and non-disclosure agreements

## Purpose

Confidentiality and non-disclosure agreements create a clear expectation of which information must be protected, who may speak about it or share it, and what continues to apply after role change, project end or contract end. The value is not in the signed form alone, but in the connection between protection need, role, understandable obligation, evidence and review.

## Control objective in repository language

The organisation operates a routine with which confidentiality obligations for employees, external staff, service providers, project partners and other involved roles are defined, communicated, tracked and reviewed when changes occur, in line with the information risk.

## Typical risks

- If people receive sensitive information without knowing their confidentiality obligations, data may be shared uncontrollably or used incorrectly.
- If agreements do not match the protection need of the information, especially critical projects, customer information, trade secrets or security details remain insufficiently protected.
- If external parties only receive technical access but no suitable contractual or organisational binding exists, a robust action framework is missing in cases of misconduct or contract end.
- If confidentiality rules are not reassessed after role change or departure, blind spots arise with former project members or service providers.
- If wording is copied without review, legal, employment-law or data-protection-related questions may remain unclear.

## Triggers

- Entry, role change, project start, project end or departure.
- Access to confidential, internal, protection-worthy or business-critical information.
- Engagement of service providers, freelancers, consultants, auditors or development partners.
- Introduction of new data classes, new information assets or new collaboration spaces.
- Security event, suspected information leakage or rule violation.
- Contract change, supplier change or end of collaboration.
- Periodic review of HR, procurement, project or ISMS documents.

## Roles and responsibilities

- **HR / people function:** integrates confidentiality into onboarding, role changes and departure.
- **Manager / project owner:** assesses which information the role or project touches and whether additional obligations are needed.
- **Information owner / asset owner:** defines protection need and expected handling rules for information assets.
- **Procurement / vendor management:** ensures that external parties are appropriately bound before access.
- **ISMS owner / security role:** defines minimum logic, data-class reference, evidence requirements and review points.
- **Legal / data protection:** reviews contractual, employment-law, non-disclosure and data protection questions.
- **Management:** decides on conflicts of objectives, exceptions, critical projects or residual risks.

## Implementation

### Minimum start

Goal: for people with access to protection-worthy information, it is traceable which confidentiality binding exists.

1. The organisation names data classes or information types for which confidentiality must be explicitly regulated.
2. For employees and external parties, it is defined when a confidentiality agreement or corresponding contractual component is required.
3. Onboarding and service provider approval include a check step before access is granted.
4. Evidence is kept centrally findable: person or organisation, date, scope, type of agreement, responsible function.
5. Exceptions are documented only with a time limit and owner.

Minimum evidence:

- data class or protection-need reference,
- onboarding/contract checklist,
- evidence of obligation or agreement,
- list of open exceptions,
- review note for critical roles or external access.

### Solid practice

Goal: confidentiality obligations are embedded into HR, project and supplier processes on a risk basis and repeatably.

1. Roles and participants are clustered by information access: standard role, privileged role, project role, external role, auditor role.
2. For elevated risks, additional notices or agreements are triggered, for example for trade secrets, security architecture, customer data or M&A/crisis topics.
3. Confidentiality is linked with access granting, data classification, training and departure.
4. Project end, supplier end and role change trigger a check of whether access, documents, devices and repositories have been cleaned up.
5. Legal and data protection review templates before they are used productively or substantially changed.
6. Findings from incidents, audits or supplier reviews flow back into templates and processes.

### Advanced practice

Goal: confidentiality is managed as ongoing governance across information assets, identities and external relationships.

1. Confidentiality status, roles, access and supplier relationship are linked in HR, IAM, contract or GRC processes.
2. Critical projects maintain a participant register with information scope, obligation status, access and offboarding check.
3. Exceptions and missing evidence generate escalations before access is granted.
4. Management receives reports on critical gaps, external parties without current evidence and recurring process errors.
5. Lessons learned from information leakage, misdirected sending or project changes improve training, classification and contract routines.

## Routine flow

1. **Recognise information context:** role, project, supplier or collaboration requires access to protection-worthy information.
2. **Classify protection need:** information owner or project owner classifies data class, criticality and sharing risk.
3. **Check obligation need:** HR, procurement or project lead checks which agreement or contractual clause is required.
4. **Trigger human review:** Legal, data protection or employee representation are involved where wording, employee relation or personal data are affected.
5. **Record evidence:** obligation, date, scope and responsible function are documented.
6. **Release access:** access is granted only after the check step is fulfilled or an exception is documented.
7. **Check change:** role change, project end, departure or contract end triggers offboarding and evidence review.
8. **Improve:** gaps, violations or unclear agreements flow into process and template review.

## Decisions

- Which information types require explicit confidentiality binding?
- Which roles or external parties need additional agreements?
- May access occur before complete evidence exists, and who accepts the risk?
- How long is evidence retained and who may view it?
- Which changes to templates require Legal, data protection or management approval?
- How are legacy contracts or old employee documents without clear evidence handled?

## Evidence

### Strong evidence

- current data class or protection-need logic,
- onboarding, project or supplier check with confidentiality review,
- signed or otherwise traceably confirmed agreement,
- register of critical external participants with obligation status,
- offboarding evidence at role, project or contract end,
- exception decision with duration and risk acceptance,
- Legal/data protection review for new or changed templates.

### Weak evidence

- general policy without reference to roles or information assets,
- template repository without evidence of use,
- generic statement “it is in the employment contract” without verifiable assignment,
- supplier contract without access scope or owner,
- old signature list without currency, scope or responsible person.

### Evidence gaps

- external parties with access but without confidentiality evidence,
- critical projects without participant and offboarding overview,
- no check at role change or contract end,
- unclear responsibility for templates and evidence,
- exceptions without expiry date or management decision.

## Effectiveness review

Review questions:

- Can critical information access be assigned to suitable confidentiality binding?
- Is the check performed effectively before access granting and for external parties?
- Are role change, project end and contract end visible in the routine?
- Are templates and special cases reviewed by suitable human roles?
- Are there traceable exceptions with follow-up date?
- Have incidents or findings led to process improvements?

Possible metrics:

- share of critical roles with current evidence,
- external parties without complete evidence,
- open or overdue exceptions,
- evidence rate at project start and project end,
- findings from offboarding or supplier reviews.

## BSIG/NIS2 connection point

Confidentiality and non-disclosure routines are compatible with NIS2-oriented topics such as governance, risk management, supply chain security, access protection, training and incident prevention. The concrete connection should be assessed organisation-specifically in the requirements register.

This artefact does not replace legal review of employment contracts, non-disclosure agreements, data protection questions or statutory obligations.

## Boundaries

- This artefact is not a contract template and not legal advice.
- It does not replace data protection review or employment-law assessment.
- It does not confirm conformity, certification readiness or effectiveness through signatures alone.
- It contains no ISO 27002 texts and no confidential sample clauses.
- It is not sufficient if access practice and offboarding are not actually operated.

## Handoffs

- **HR handoff:** entry, role change, departure, personnel file or employee obligation.
- **Legal handoff:** contract templates, confidentiality scope, enforceability, special cases, legacy contracts.
- **Data protection handoff:** personal data in evidence, contract data, training or access evaluations.
- **Procurement/vendor handoff:** external parties, service provider access, project partners, contract end.
- **Access handoff:** access may occur only after clarified obligation status or documented exception.
- **Incident handoff:** suspected information leakage, misdirected sending, unauthorised sharing or rule violation.
- **Management handoff:** critical exceptions, legacy issues, conflicts of objectives or unacceptable residual risks.
- **Audit/evidence handoff:** missing evidence, unclear scopes or obligation logic that cannot be tested.

## Typical mistakes

- Confidentiality is treated as a one-off signature and not connected with access.
- External staff start in the project before contract or obligation status is clarified.
- Especially critical information types receive no additional consideration.
- Role changes and project end trigger no offboarding check.
- Templates are changed without Legal/data protection review.
- Evidence is distributed across HR, procurement and project teams and cannot be found during review.
- Exceptions become permanent because no follow-up date was set.

## Fictional mini example

A fictional software company starts a product development project with two external developers. The product owner classifies architecture documents and roadmap as confidential. Procurement checks the contract status before access is granted, Legal confirms the agreement used, and the ISMS owner adds the developers to the project participant register. At project end, the product owner confirms withdrawal of access and return of project-related documents.

Evidence:

- project participant register with information scope,
- contract or obligation evidence,
- Legal review of the template,
- access ticket after completed check step,
- offboarding evidence at project end.
