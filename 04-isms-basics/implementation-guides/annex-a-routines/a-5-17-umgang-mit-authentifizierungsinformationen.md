# A.5.17 — Handling authentication information

## Purpose

Authentication information is anything that can be used to prove identities or trigger access: passwords, passphrases, MFA tokens, recovery codes, API keys, certificates, SSH keys, service account secrets, and comparable secrets.

This routine ensures that such information is not casually created, shared, stored, copied, or forgotten. The core is secure operating logic across the full lifecycle: issuance, use, storage, rotation, revocation, recovery, and handling of suspected cases.

## Control objective in repository language

The organization operates a traceable routine for authentication information of people, services, and machine identities. It defines which secrets are allowed, where they may be stored, who manages them, when they are changed or withdrawn, and how suspected cases are handled.

## Typical risks

- If passwords, tokens, or keys end up in chats, tickets, repositories, or spreadsheets, unauthorized persons may gain access to systems and data.
- If service account secrets have no owner, they remain active after project end and are not revoked during role changes.
- If recovery codes or break-glass access are stored without control, emergency access can become normal access.
- If credentials are shared between people, actions can no longer be assigned to a responsible identity.
- If compromised authentication information is not rotated quickly, a security event can be prolonged or worsened.
- If MFA, password managers, or secret management are used only informally, workaround paths without evidence arise.

## Triggers

- New account, new admin access, new service, new API, new certificate, or new key.
- Hiring, role change, departure, or end of service provider access.
- Suspected compromised credentials, phishing, token leak, repository finding, or incident.
- Introduction or change of MFA, password manager, secret management, certificate management, or IAM process.
- Expiry date, rotation deadline, or planned review of service accounts and machine identities.
- Audit finding, vulnerability finding, or technical change to authentication methods.
- Emergency access, account recovery, or use of a break-glass procedure.

## Roles and responsibilities

- **Identity/IAM owner:** defines technical authentication methods, account types, and withdrawal logic.
- **IT/platform owner:** technically implements password, MFA, secret, key, and certificate requirements.
- **Asset owner / Service owner:** is responsible for authentication information for applications, interfaces, and service accounts.
- **ISMS owner / Security role:** defines minimum logic, review requirements, exception handling, and incident handoff.
- **Manager / Process owner:** confirms business need for special access or shared function risks.
- **HR / Procurement:** provides hiring, change, departure, and contract-end triggers.
- **Data protection / Legal:** assesses personal-data analysis, employee reference, contractual and evidence requirements.
- **Management:** decides on permanent residual risk, non-implementable minimum requirements, or resource needs.

## Implementation

### Minimum start

Goal: make the most dangerous secrets visible and stop insecure storage locations.

1. The organization defines which authentication information is in scope: user passwords, MFA, admin access, service accounts, API keys, certificates, and recovery codes.
2. An owner is named for critical systems and service accounts.
3. Credentials must not be stored in chat, email, tickets, code repositories, or unprotected files.
4. A password manager or equivalently approved storage path is defined for people.
5. For technical secrets, there is at least a register with owner, purpose, storage location, expiry, or review date.
6. Suspected disclosure immediately triggers rotation, blocking, or incident triage.
7. Emergency access is documented separately and reviewed after use.

Minimum evidence:

- rule or short standard for handling authentication information,
- list of critical service accounts, keys, or certificates with owner,
- evidence of approved storage paths,
- ticket for rotation or blocking in case of suspicion,
- review note for emergency access.

### Solid practice

Goal: secrets are managed across their lifecycle.

1. Authentication information is classified by type and criticality: personal access, privileged access, technical secrets, certificates, recovery means.
2. MFA is introduced based on risk for critical access, external access, and privileged roles, or exceptions are justified.
3. Service accounts and machine identities receive owner, purpose, minimal rights, rotation logic, and deprovisioning trigger.
4. Secret scanning, repository rules, or manual controls check typical leakage locations.
5. Exceptions are time-limited, justified, and managed with compensating measures.
6. Joiner/mover/leaver processes trigger review or revocation of affected authentication information.
7. Recurring findings lead to improvements in tooling, training, or process design.

Strong evidence:

- secret/service account register,
- password manager or secret management use with scope,
- MFA coverage overview for critical access,
- rotation and revocation tickets,
- secret scanning results with measures,
- exception decisions with expiry date.

### Advanced practice

Goal: authentication information is technically monitored and closely connected with IAM, DevOps, and incident response.

1. Secret management, IAM, CI/CD, cloud platforms, and monitoring are integrated.
2. Short-lived tokens, just-in-time privileges, or automatic rotation reduce long-lived secrets.
3. Certificates, SSH keys, API keys, and service accounts are automatically inventoried and monitored for expiry.
4. Leaks in repositories, artifacts, logs, or tickets create alerts and predefined response steps.
5. Break-glass access is regularly tested, sealed, logged, and reviewed after every use.
6. Management receives decision-ready metrics on open risks, overdue rotations, non-assignable secrets, and exception rates.

## Routine flow

1. **Need arises:** account, API, service, certificate, emergency access, or technical integration is required.
2. **Determine type:** personal identity, privileged access, technical secret, recovery means, or machine identity.
3. **Define owner and purpose:** clarify business and technical owner, system reference, and runtime.
4. **Choose secure storage path:** use password manager, secret manager, certificate management, or approved alternative.
5. **Implement minimum protection:** define MFA, minimal rights, expiry date, rotation, access restriction, and logging as appropriate.
6. **Document use:** record not the secret itself, but owner, purpose, storage-location class, expiry, and review date.
7. **Perform review:** check active, expiring, shared, orphaned, or unusual authentication information.
8. **Act on suspicion:** block, rotate, check logs, trigger incident handoff, and document lessons learned.
9. **Improve:** feed repeated leaks or exceptions back into process, tooling, and training.

## Decisions

- Which authentication information is critical enough for the minimum start?
- Which storage paths are approved and which are explicitly prohibited?
- Where is MFA mandatory, and where are there time-limited exceptions?
- How long may technical secrets, certificates, or keys be valid?
- Who may store, use, and subsequently review emergency access?
- Which findings are treated as incidents and which as regular corrections?
- When does an exception need a management decision instead of a technical individual approval?

## Evidence

### Strong evidence

- current register of critical service accounts, API keys, certificates, or SSH keys with owner,
- evidence of approved secret and password storage,
- MFA coverage for critical and privileged access,
- rotation, blocking, or revocation evidence,
- secret scanning findings with documented handling,
- review records for emergency access,
- management decision for permanent residual risk.

### Weak evidence

- general password rule without evidence of use,
- screenshot of individual MFA settings without scope,
- outdated service account list without owner,
- ticket comment “password changed” without reference to the affected secret,
- policy that prohibits insecure storage without checking typical storage locations.

### Evidence gaps

- technical secrets without owner or expiry date,
- credentials in code, tickets, chat, or files without handling,
- shared accounts without exception decision,
- break-glass access without test or usage review,
- departed persons or service providers with known secrets,
- no incident triage when disclosure is suspected.

## Effectiveness review

Review questions:

- Are critical authentication information items inventoried, owned, and reviewable?
- Are insecure storage locations detected technically or organizationally?
- Can compromised secrets be blocked or rotated quickly?
- Are service accounts and machine identities managed with minimal rights and owner?
- Are MFA exceptions time-limited and decided traceably?
- Is every use of emergency access reviewed afterward?
- Do repeated leaks lead to process or tool improvements?

Possible metrics:

- share of critical service accounts with owner and review date,
- overdue rotations or certificate expiries,
- number of secret leaks by source,
- time to rotation after suspicion,
- MFA coverage for critical access,
- open and overdue exceptions.

## BSIG/NIS2 connection point

Secure handling of authentication information is compatible with NIS2-oriented risk management measures, cyber hygiene, access protection, incident prevention, and management oversight of critical technical dependencies.

For BSIG/NIS2 affectedness, the organization should assess in the requirements register which systems, roles, evidence, and handoffs are relevant. This artifact does not replace legal interpretation or a binding assessment of applicability.

## Boundaries

- This artifact is not a complete IAM, cryptography, or secret management design.
- It does not replace a data protection review for personal logs, MFA analysis, or employee data.
- It contains no requirements for concrete password lengths, algorithms, or vendor tools.
- No legal advice, no data protection advice, no certification commitment.
- No ISO 27002 text, no real credentials, and no confidential technical details in examples.

## Handoffs

- **IAM/access handoff:** new account types, role changes, withdrawal, recertification, and privileged rights.
- **Incident handoff:** suspected disclosure, phishing, token leak, unauthorized use, or unknown secret findings.
- **DevOps/development handoff:** secrets in code, CI/CD, artifacts, container images, logs, or build configurations.
- **HR/procurement handoff:** departure, service provider end, role change, or change of key persons.
- **Data protection/legal handoff:** personal-data logging, employee reference, contractual questions, or evidence requirements.
- **Management handoff:** permanent MFA exceptions, unfixable legacy methods, resource need, or accepted residual risk.
- **Audit/evidence handoff:** incomplete register, missing rotation evidence, or unreviewed emergency access.

## Typical mistakes

- The organization regulates passwords but forgets API keys, certificates, and service accounts.
- Secrets are shared in tickets or chats because the secure transfer path is impractical.
- MFA is introduced, but exceptions are never reviewed.
- Service accounts belong to former projects and nobody feels responsible.
- Break-glass access is tested, but use is not logged or reviewed.
- Rotation is required, but operated without owner, deadline, or evidence.
- Secret scanning reports findings, but nobody decides handling and risk.

## Fictional mini example

A fictional software service provider finds an API key for a test system during a repository scan. The product owner confirms the system reference, and the platform owner rotates the key and checks logs for use. The action log records that CI/CD secrets will in future be integrated only through the approved secret manager. A second finding concerns an old service account without owner; this item goes into the next access review with a deadline.

Evidence:

- scan finding without disclosure of the secret,
- rotation ticket,
- log review note,
- updated CI/CD instruction,
- action log for orphaned service account.
