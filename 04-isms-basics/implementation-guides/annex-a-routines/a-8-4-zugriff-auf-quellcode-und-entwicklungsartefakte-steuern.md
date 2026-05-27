# A.8.4 — Control access to source code and development artefacts

## Purpose

Source code, build scripts, repositories, artefact stores, container images, CI/CD configurations and development documentation are not only technical work materials. They can contain business logic, vulnerabilities, fragments of credentials, architecture knowledge and opportunities for manipulation.

This routine ensures that access to development artefacts is intentionally granted, separated, reviewed and withdrawn. The core is not “repository private”, but traceable control: who may read, change, merge, build, publish or retrieve code and artefacts — and why?

## Control objective in repository language

The organisation operates an access routine for source code and development artefacts. It connects repository scope, roles, protection need, approvals, technical permissions, review, exceptions and handoffs to secure development, IAM, supplier management and incident response.

## Typical risks

- If former employees or service providers retain repository access, code, secrets or architecture knowledge can leak.
- If write, merge or release rights are granted too broadly, faulty or manipulated changes can enter production artefacts.
- If CI/CD tokens, deploy keys or artefact access are not controlled, hidden privileged access emerges.
- If external developers work without clear separation, tenant, customer or product boundaries can be violated.
- If open-source, fork or mirror workflows are unclear, confidential development states can be shared publicly or without control.
- If rights are not reviewed, permissions grow beyond role changes and project end.

## Triggers

- new repository, new build pipeline, new artefact store or new development service.
- new product, new project team, external development engagement or open-source publication.
- onboarding, role change, project end or offboarding of developers, admins or service providers.
- change to branching, review, release or deployment processes.
- security event, compromised developer account, suspicious commit or secret leak.
- audit finding, vulnerability finding or supplier change.
- periodic review of critical repositories, admin rights and machine identities.

## Roles and responsibilities

- **Product Owner / Service Owner:** assesses business need and criticality of the code or artefact.
- **Repository Owner / Tech Lead:** owns permission model, branch protection, review rules and team access.
- **Platform / DevOps Owner:** operates repository platform, CI/CD, artefact store, tokens and technical controls.
- **Security role / ISMS Owner:** defines minimum requirements, review logic, exception handling and escalation.
- **Development team:** requests access traceably and reports anomalies or incorrect permissions.
- **HR / Project Management:** provides onboarding, role change, project end and offboarding events.
- **Procurement / Supplier Management:** controls external development access and contract end.
- **Management:** decides on residual risks, resource conflicts or permanently inseparable rights.

## Implementation

### Minimum start

Goal: operate critical repositories and development artefacts visibly and with access control.

1. Critical repositories, CI/CD projects and artefact stores are named with owners.
2. Access is distinguished into read rights, write rights, merge/admin rights, release rights and technical identities.
3. New access is granted via ticket or traceable approval.
4. External access and admin rights are marked separately.
5. Project end, role change and offboarding trigger a rights review.
6. Critical repositories, admin rights, deploy keys and tokens are reviewed at least quarterly.

Minimum evidence:

- list of critical repositories and artefact stores with owner,
- access request or approval,
- permission export at the review date,
- evidence of withdrawn or corrected rights,
- exception with expiry date.

### Solid practice

Goal: access to development artefacts is controlled by role and risk.

1. Repository and artefact classes are distinguished by criticality, exposure and product relevance.
2. Standard roles are defined: Reader, Contributor, Maintainer, Release Owner, Admin, CI/CD service account.
3. Branch protection, review obligations, merge rules and release approvals are connected to permissions.
4. Service provider access is time-limited and linked to engagement, project or contract.
5. Machine identities receive owner, purpose, permission scope, rotation and expiry date.
6. Secret scanning, commit signature or protection mechanisms are used where risk and tooling justify it.
7. Review findings lead to withdrawal, correction, exception or management decision.

### Advanced practice

Goal: source code access is integrated into secure development, IAM and the supply chain.

1. Repository platform, identity source, project portfolio and offboarding process are connected.
2. Critical rights are analysed automatically: admins, external users, inactive users, unassignable tokens, public repositories.
3. CI/CD rights follow least-privilege logic and are controlled through protected environments, separated secrets and approval paths.
4. Unusual repository activities feed into security monitoring and incident triage.
5. Open-source publications and code sharing go through their own approval routine.
6. Management receives decision-ready metrics on review coverage, overdue external access, admin rights and exception rate.

## Routine flow

1. **Access need arises:** new team member, service provider, project, tool, pipeline or release responsibility.
2. **Record request:** document repository or artefact, role, purpose, duration, project relevance and external status.
3. **Business review:** owner confirms need, protection need and suitable role.
4. **Review security logic:** assess admin, release, CI/CD, external or public access separately.
5. **Technical implementation:** platform team implements rights, groups, branch protection or token permissions.
6. **Store evidence:** request, decision, implementation and expiry date remain traceable.
7. **Perform review:** owner reviews critical rights, external access, technical identities and anomalies.
8. **Correct or escalate:** withdraw unnecessary rights, time-limit exceptions, have residual risks decided.
9. **Learn:** feed findings back into role model, CI/CD design, onboarding or supplier control.

## Decisions

- Which repositories, pipelines and artefact stores are critical enough for tighter control?
- Who may read, write, merge, release, manage secrets or hold admin rights?
- Which external accesses are permissible with time limits?
- How are technical identities, deploy keys and CI/CD tokens limited?
- Which code or artefact releases need Security, Legal or Management handoff?
- When does an access event become an incident?

## Evidence

### Strong evidence

- current repository/artefact scope with owners,
- role and group model for development access,
- access requests with justification and approval,
- permission exports for critical repositories and CI/CD projects,
- review records with decisions and corrections,
- evidence of withdrawn external or privileged rights,
- token/deploy-key register with owner, purpose and expiry date,
- management decision for accepted exceptions.

### Weak evidence

- general statement “repositories are private” without review,
- screenshot of individual team members without owner or date,
- repository policy without technical implementation,
- admin list without justification,
- external access without project or contract reference,
- secret-scanning report without treatment of findings.

### Evidence gaps

- no overview of critical repositories or artefact stores,
- no assignment of technical identities,
- no review after project end or offboarding,
- no separation between read, write, merge and release rights,
- permanently public or external access without decision,
- no review evidence for CI/CD and artefact access.

## Effectiveness review

Review questions:

- Can critical repositories be assigned to an owner and a permission model?
- Are external, privileged and technical accesses especially visible?
- Are rights withdrawn promptly after project end, role change and offboarding?
- Is there evidence that reviews led to corrections?
- Are branch, merge and release rules consistent with permissions?
- Are secret leaks or suspicious repository activities handed over to incident or vulnerability processes?

Possible metrics:

- share of critical repositories with owner,
- overdue access reviews,
- number of external and privileged accesses,
- inactive users with access,
- technical identities without expiry date,
- corrected rights per review,
- open exceptions.

## BSIG/NIS2 connection point

Control of access to source code and development artefacts is compatible with NIS2-oriented topics such as secure development, access protection, supply chain security, vulnerability management, cyber hygiene and incident prevention. The concrete connection should be assessed organisation-specifically in the requirements register and risk analysis.

This artefact does not replace legal assessment, data protection review or any statement on the applicability of individual obligations.

## Boundaries

- This artefact is not a complete secure-development framework.
- It does not replace code analysis, architecture review or licence review.
- It provides no binding specification for concrete repository tools.
- No certification, conformity or security guarantee.
- No ISO 27002 text and no confidential repository or product details in public examples.

## Handoffs

- **IAM handoff:** role change, offboarding, group model, privileged and technical identities.
- **Secure development handoff:** branch protection, reviews, secrets, build and release rules.
- **Incident handoff:** suspicious commits, compromised accounts, secret leak, unauthorised access.
- **Supplier handoff:** external developers, project end, contractual binding, managed development.
- **Legal / Data protection handoff:** open-source publication, personal data in repositories, licence or confidentiality topics.
- **Management handoff:** permanent exceptions, inseparable release rights, resource needs.
- **Audit / Evidence handoff:** missing review evidence, unassignable tokens, incomplete repository scope.

## Typical mistakes

- Repository access is treated like normal file access.
- Admin rights remain active for former tech leads or service providers.
- CI/CD tokens are not treated as privileged access.
- Branch protection exists, but maintainers can bypass it without review.
- External developers are invited project by project, but not removed project by project.
- Public repositories, forks or mirrors are not included in the routine.
- Management sees only tool reports, but no decision-ready residual risks.

## Fictional mini example

A fictional software team ends a customer portal project with an external development partner. The Repository Owner pulls a permission export, marks external accounts and finds two active deploy keys without owner. The platform team removes the external accounts, replaces the deploy keys with a time-limited service account and documents the change in the ticket. In the next review, the Service Owner decides that release rights will be reviewed monthly in future.

Evidence:

- repository scope with owner,
- permission export,
- ticket for withdrawal of external access,
- new service account with purpose and expiry date,
- review decision on release-rights review.
