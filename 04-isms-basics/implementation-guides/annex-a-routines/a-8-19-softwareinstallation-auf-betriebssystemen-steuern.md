# A.8.19 — Control software installation on operating systems

## Purpose

Controlled software installation prevents unreviewed, outdated or unnecessary software on endpoints, servers and platforms from creating attack surface, license/operational risks or support problems. What matters is an operable routine for approval, provision, exception and removal.

## Control objective in repository language

The organization defines which software may be installed on which operating systems, through which paths installation takes place, who is responsible for approvals and exceptions, and how unapproved or risky software is detected and treated. The routine connects endpoint/server management, procurement, license view, vulnerability management and access protection.

## Typical risks

- If users or administrators install arbitrary software, malware, vulnerability and data leakage risks arise.
- If software is obtained from unreviewed sources, manipulated packages or unwanted additional components may be installed.
- If outdated or no longer needed software remains installed, the attack surface grows unnoticed.
- If servers and production systems are changed manually, the operational state is no longer reproducible.
- If business units install shadow tools, data, support and supplier risks arise outside governance.
- If exceptions are not time-limited, temporary installations become permanent.

## Triggers

- New workstation, server, operating system build, standard image or platform service.
- Request to install new software or extend existing software.
- New vulnerability, vendor end of life, license change or software discontinuation.
- Malware finding, unusual process execution or unapproved software in the inventory.
- Change of software distribution, endpoint management, package source or cloud base image.
- New service provider, business-unit tool or SaaS/client component.
- Regular review of software inventory, allow/deny lists, exceptions and legacy software.

## Roles and responsibilities

- **Endpoint/client owner:** steers software catalog, standard images, packaging and installation on workstations.
- **Server/platform owner:** steers installations, images, repositories and configuration management on servers and platforms.
- **Service owner / business unit:** justifies need, functional criticality and purpose of use.
- **Security role / ISMS owner:** defines risk criteria, source requirements, exception and review logic.
- **Procurement / license management:** checks source of supply, license, support and contractual questions without replacing legal assessment through this artifact.
- **Data protection/legal role:** checks organization-specific requirements where personal processing, contracts or terms of use are involved.
- **Management:** decides on residual risks, shadow IT, budget needs or conflicts between business need and security requirement.

## Implementation

### Minimum start

Goal: Critical systems and workstations receive software through traceable, approved paths.

1. Determine scope: managed endpoints, servers, admin workstations, production systems and critical business applications.
2. Define permitted installation paths: software distribution, package managers, approved repositories, images or IT service process.
3. Define simple approval logic: purpose, owner, source, criticality, data reference, support status and security review.
4. Track unapproved software findings in an action log.
5. Limit local installation rights where practicable and document exceptions.
6. Remove outdated or unnecessary software with priority.

### Solid practice

Goal: Software installation is standardized, inventoried and connected with risk and operational processes.

1. Software catalogs distinguish standard software, approved additional software, restricted software and prohibited software.
2. Installations take place through central distribution, package sources, build pipelines or infrastructure as code instead of manual individual changes.
3. Software inventory is regularly reconciled with approvals, licenses, vulnerabilities and support status.
4. New software is reviewed risk-based before approval: source, vendor, permissions, auto-update, data flows, dependencies.
5. Exceptions have owner, justification, duration, compensating measure and follow-up date.
6. Server and production system changes are connected with change management.
7. Shadow IT findings lead to a business-unit conversation, risk assessment and decision instead of only deletion.

### Advanced practice

Goal: Software installation is automatically controlled, reproducible and integrated into security operations.

1. Endpoint and server management enforce permitted installation paths and block unapproved sources or executions.
2. Application control, package signatures, repository governance and baseline images reduce manipulation and sprawl risks.
3. Software inventory is connected with vulnerability management, asset management, license view and EDR/monitoring.
4. Golden images, container base images and server builds are versioned, tested and reviewable.
5. Installation on production systems occurs through change, pipeline or configuration management with rollback capability.
6. Detection of unapproved software creates tickets or security triage.
7. Management reports show legacy software, shadow IT, exception rate, technical debt and resource needs.

## Routine flow

1. **Need or finding arises:** software request, new build, inventory finding, vulnerability or business-unit need.
2. **Assess:** check purpose, source, affected systems, data reference, permissions, support status and risks.
3. **Decide:** approve, reject, permit temporarily, replace or remove.
4. **Provide:** controlled installation path with version, source and owner.
5. **Evidence:** document installation, approval, exception or removal.
6. **Monitor:** check inventory, vulnerabilities, unapproved findings and end-of-life status.
7. **Escalate:** hand unclear shadow IT, high risks or business conflicts to management or suitable handoffs.
8. **Improve:** adjust software catalog, package sources, rights and build processes.

## Decisions

- Which operating systems and system classes are in scope of installation control?
- Which installation sources are permitted and which are blocked?
- Which software needs security, data protection, license or architecture review before approval?
- Who may approve local installations or temporary exceptions?
- How are business-unit needs and security/operational risk decided against each other?
- When is software removed, replaced or transferred into managed provision?
- Which shadow IT risks are accepted, compensated for or escalated?

## Evidence

### Strong evidence

- Software catalog or allow/deny logic with owner and review date,
- approvals for new software with purpose, source, version and risk assessment,
- evidence from software distribution, package manager, MDM/endpoint management or configuration management,
- inventory reconciliation with unapproved findings and actions,
- exceptions with justification, duration and follow-up date,
- change evidence for installations on production systems,
- removal evidence for outdated or risky software.

### Weak evidence

- General IT policy without installation path and control,
- manual Excel list without inventory reconciliation,
- “admin rights only for IT” without checking actual installations,
- software distribution screenshot without approval or scope reference,
- license list without security and support status,
- exception by chat message without expiration date.

### Evidence gaps

- No overview of installed software on critical systems,
- unclear installation sources,
- local admin rights without limitation or review,
- no treatment of unapproved software,
- no process for end-of-life or outdated software,
- business-unit tools without owner, contract or data reference,
- production servers are changed manually without change evidence.

## Effectiveness review

Review questions:

- Are permitted installation paths for endpoints, servers and production systems defined?
- Is there a current software catalog or comparable approval logic?
- Are unapproved installations detected and treated?
- Are local installation rights limited and exceptions traceable?
- Are vulnerabilities, support end and no longer needed software included in decisions?
- Are production changes reproducible and connected with change management?
- Are business-unit needs decided instead of being pushed into shadow IT?

Possible metrics:

- Share of managed installations,
- number of unapproved software findings,
- open exceptions and overdue reviews,
- systems with outdated or unsupported software,
- time from software request to decision,
- risky software removed per review cycle,
- production installations without change reference.

## BSIG/NIS2 connection point

Controlled software installation can connect to NIS2-oriented topics such as cyber hygiene, vulnerability management, secure configuration, access protection, supply chain and service provider steering, and technical risk treatment. The concrete connection should be assessed organization-specifically in the requirements register, asset and software inventory, and change and risk management.

This artifact does not replace legal assessment of license, contract, data protection or evidence obligations.

## Boundaries

- This artifact is not license advice and not a complete endpoint hardening baseline.
- It does not replace technical analysis of individual software products, package sources or supply chain risks.
- Complete blocking of every user installation can be impractical for business; the goal is risk-based steering.
- No certification, conformity or security guarantee.
- No use of real inventories, customer data, license keys or secrets in public examples.

## Handoffs

- **Vulnerability management handoff:** installed software is vulnerable, outdated or no longer supported.
- **Change handoff:** installation or removal affects production systems, services or rollback capability.
- **Procurement/license handoff:** source of supply, contract, support, license or vendor relationship is unclear.
- **Data protection/legal handoff:** software processes personal data, sends telemetry or has unclear terms of use.
- **Incident handoff:** unapproved software, malware suspicion or manipulated packages are discovered.
- **Management handoff:** business unit needs risky software, shadow IT is widespread or tooling/resources are missing.
- **Audit/evidence handoff:** approvals, inventory or removal evidence are incomplete.

## Typical mistakes

- Software installation is viewed only through local admin rights, not through sources, approval and inventory.
- Servers are changed manually and lose their reproducible operational state.
- Standard software is approved but never checked for support end or vulnerabilities.
- Business-unit need is blocked without deciding on a secure alternative.
- Exceptions become permanent because no review date exists.
- Shadow IT is only deleted technically without clarifying cause and risk.
- Management sees license costs, but not security and operational risks from software sprawl.

## Fictional mini example

A fictional business unit wants to install a local analysis tool on several notebooks. The endpoint owner checks source, update path and required rights; the data protection role is involved because files with personal data could be processed. The software is initially provided for five users for a limited time through software distribution. EDR and inventory check the installation; after six weeks, the service owner assesses benefits and risks. An unapproved alternative software on two devices is removed and documented as a shadow IT finding in the action log.
