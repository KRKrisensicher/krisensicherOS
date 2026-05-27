# A.8.8 — Handling technical vulnerabilities

## Purpose

Vulnerability handling ensures that known technical vulnerabilities are identified, assessed, prioritized, treated, and tracked. The value is not in the scan report, but in the ability to turn technical findings into risk-based decisions and effective measures.

## Control objective in repository language

The organization operates a routine that transfers vulnerabilities from scans, vendor advisories, threat intelligence, penetration tests, bug reports, incident lessons learned, or supplier notifications into prioritized measure and decision management.

## Typical risks

- If known vulnerabilities are not identified or assessed, exploitable attack surfaces remain open.
- If scan reports are not prioritized, teams drown in findings and critical gaps remain untreated.
- If asset owners are missing, vulnerabilities cannot be assigned to a risk, system, or service.
- If patches are deployed without change and availability assessment, operational disruptions arise.
- If exceptions are not documented, “not patched” becomes invisible.
- If supplier notifications are not processed, third-party components and SaaS dependencies remain blind spots.

## Triggers

- new vulnerability scan or penetration test.
- vendor advisory, CVE notice, CERT/CSIRT advisory, or threat-intelligence hit.
- new or changed systems, applications, containers, libraries, or cloud resources.
- security event or suspected exploitation.
- supplier notification about product or service vulnerabilities.
- regular patch or vulnerability review.
- audit finding, customer requirement, or management question on the technical risk situation.

## Roles and responsibilities

- **Asset owner / service owner:** assesses business criticality and accepts or escalates residual risks.
- **IT / platform owner:** operates scans, patches, configurations, and technical measures.
- **Development / product owner:** assesses application code, libraries, images, and release dependencies.
- **Security role / ISMS owner:** defines assessment logic, deadlines, escalation paths, and reporting.
- **Change owner:** coordinates tests, rollout, and operational risks.
- **Supplier management:** tracks vulnerabilities in external products or services.
- **Management:** decides on unacceptable residual risks, lack of resources, or accepted exceptions.

## Implementation

### Minimum start

Goal: make critical vulnerabilities visible, assigned, and trackably handled.

1. Critical assets in the ISMS scope are named: internet-exposed systems, central identity services, core applications, production servers, important SaaS services.
2. These assets have owners and technical responsible persons.
3. Vulnerability sources are defined: at minimum vendor advisories, central scans, or service provider notifications.
4. Findings are recorded in a measure log: asset, vulnerability, assessment, owner, decision, deadline, status.
5. Critical findings are triaged promptly and escalated if needed.
6. Unresolved findings receive an exception, compensating measure, or risk decision.

Minimum evidence:

- asset list in scope,
- vulnerability log or ticket list,
- assessment and prioritization decision,
- evidence of remediated findings,
- exception or risk acceptance for open critical findings.

### Solid practice

Goal: vulnerability handling is risk-based, repeatable, and connected to change management.

1. Vulnerabilities are assessed by technical criticality, exposure, asset criticality, exploitability, and existing compensating measures.
2. Treatment deadlines are defined by risk class.
3. Patches and configuration changes run through an appropriate change process.
4. False positives, accepted risks, and technically non-remediable findings are documented traceably.
5. Repeated findings lead to root cause analysis: missing patch process, outdated platform, insecure architecture, unclear responsibility.
6. Supplier and SaaS vulnerabilities are tracked via contract/service contacts.
7. Status and top risks flow into ISMS review and management review.

Strong evidence:

- defined assessment and deadline logic,
- regular scan or notification evidence,
- tickets with owner, deadline, and status,
- patch/change evidence,
- re-scan or validation evidence,
- exception decisions with expiry date,
- management decision for persistent residual risks.

### Advanced practice

Goal: vulnerability management is integrated into architecture, development, operations, and the situational picture.

1. Asset inventory, CMDB, cloud inventory, container/dependency scanning, and ticketing are connected.
2. Exposure and business criticality influence prioritization automatically or semi-automatically.
3. Critical vulnerabilities are linked with threat intelligence, active exploitation, and incident triage.
4. Patch and remediation SLAs are monitored and reported.
5. Secure development, baseline configurations, and architecture decisions reduce recurring findings.
6. Lessons learned from incidents and penetration tests lead to structural improvements.
7. Management sees not only the number of findings, but risk development, overdue critical gaps, technical debt, and resource needs.

## Routine flow

1. **Vulnerability becomes known:** scan, notification, advisory, incident, supplier, or test.
2. **Assign:** determine affected asset, owner, service, data class, and exposure.
3. **Assess:** classify technical criticality, exploitability, business impact, and existing safeguards.
4. **Prioritize:** define deadline, treatment path, and escalation need.
5. **Treat:** patch, configuration, deactivation, segmentation, monitoring, workaround, or architecture measure.
6. **Validate:** re-scan, test, vendor confirmation, or technical evidence.
7. **Document:** record status, decision, evidence, and residual risk.
8. **Escalate:** bring overdue critical findings, non-remediable vulnerabilities, or resource problems into the management review.
9. **Learn:** feed causes and patterns back into architecture, operations, procurement, or development.

## Decisions

- Which assets are checked first and regularly?
- Which assessment logic connects technical severity with business risk?
- Which deadlines apply to critical, high, medium, and low findings?
- When is a workaround sufficient, and when is a patch or shutdown needed?
- Who may accept an exception and for how long?
- When does a vulnerability become an incident or management topic?
- How are supplier or SaaS vulnerabilities tracked?

## Evidence

### Strong evidence

- current scope of critical assets,
- vulnerability source with date and coverage,
- prioritized findings list with owners,
- tickets with treatment step and deadline,
- technical evidence for patch, configuration change, or compensation,
- re-scan or validation,
- exception with risk decision and expiry date,
- management decision for unremediated critical risks.

### Weak evidence

- scan report without triage,
- CVSS value without asset or exposure assessment,
- patch policy without evidence of implementation,
- ticket list without validation,
- monthly number of findings without risk context,
- blanket statement “managed by the service provider” without feedback or SLA.

### Evidence gaps

- unknown asset coverage,
- no owners for findings,
- no deadlines or escalation rules,
- no handling of exceptions,
- no supplier tracking,
- no validation after remediation,
- critical old findings without management decision.

## Effectiveness review

Review questions:

- Are the most important assets covered by the vulnerability process?
- Can critical findings be assigned to an owner and a deadline?
- Are vulnerabilities prioritized by business risk and exposure?
- Is there evidence that remediations were validated?
- Are overdue critical findings escalated?
- Are causes of recurring findings treated structurally?
- Are supplier and SaaS vulnerabilities visible in the process?

Possible metrics:

- coverage of critical assets,
- open critical findings,
- overdue findings by risk class,
- average remediation time by criticality,
- exception rate and overdue exceptions,
- reopen rate after validation,
- recurring findings per platform or team.

## BSIG/NIS2 connection point

Vulnerability handling is compatible with NIS2-oriented risk management measures, cyber hygiene, secure procurement and development, incident prevention, monitoring, and maintenance of secure services. For affected organizations, the specific connection point should be assessed in the requirements register, risk analyses, and management review.

This artifact does not replace legal review of reporting obligations, affectedness, or evidence obligations.

## Boundaries

- This artifact is not a technical scanner recommendation and not a hardening baseline.
- It does not replace product, cloud, network, or application security analysis.
- CVSS or tool severity levels do not replace organization-specific risk assessment.
- No legal advice, no data protection advice, no certification assurance.
- No ISO 27002 texts or confidential vulnerability details in public examples.

## Handoffs

- **Incident handoff:** active exploitation, suspicion of compromise, critical exposed vulnerability.
- **Change handoff:** patch, configuration change, testing need, rollback plan, maintenance window.
- **Development handoff:** code, dependency, container, or CI/CD findings.
- **Supplier handoff:** third-party product, SaaS, managed service, missing vendor information.
- **BCM handoff:** remediation endangers availability of critical services or requires emergency decision.
- **Management handoff:** lack of resources, overdue critical findings, accepted residual risk, technical debt.
- **Data protection handoff:** vulnerability affects personal data or possible breach of personal data protection.
- **Audit/evidence handoff:** missing coverage, missing validation, or unclear exception handling.

## Typical mistakes

- Scan reports are generated but not owned.
- Prioritization follows only the tool score, not asset criticality or exposure.
- Findings are closed without validating remediation.
- Exceptions run indefinitely.
- Critical legacy systems are excluded from the scan without a risk decision.
- Supplier risks remain outside the vulnerability process.
- Management sees volume metrics, but no decision-ready residual risks.
- Patching is decoupled from the change process and creates operational disruptions.

## Fictional mini example

A fictional operator of a customer portal receives a vendor advisory about an actively exploited vulnerability in a web component. The platform owner classifies the affected system as internet-exposed and critical. A high-priority ticket is created, a maintenance window is coordinated, and the patch is deployed. A re-scan confirms remediation. For a second internal system, the patch is not immediately possible; the service owner documents a time-limited exception with an additional network restriction and resubmission in the management review.

Evidence:

- vendor advisory as reference,
- affected asset list,
- prioritized tickets,
- change and patch evidence,
- re-scan,
- exception with compensating measure and expiry date,
- management review item for residual risk.
