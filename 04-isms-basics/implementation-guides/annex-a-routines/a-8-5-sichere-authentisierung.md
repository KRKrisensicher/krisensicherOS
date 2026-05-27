# A.8.5 — Secure authentication

## Purpose

Secure authentication ensures that people, services and machine identities must reliably prove who or what they are before access to systems, data or functions is created. The value is not in a password rule alone, but in an operated routine for authentication methods, MFA, exceptions, technical accounts, recovery and review.

## Control objective in repository language

The organisation operates a traceable authentication routine for user accounts, privileged accounts, external access, service accounts, interfaces and critical applications. Authentication is planned on a risk basis, implemented technically, reviewed regularly and improved when weaknesses or incidents occur.

## Typical risks

- If simple or reused secrets are sufficient for critical access, compromised credentials can directly lead to system access.
- If MFA is only partially introduced, privileged, external or cloud access remains attackable.
- If recovery and reset processes are weak, an attacker can bypass authentication through support.
- If service accounts, API keys or tokens run without owner, permanent hidden access emerges.
- If exceptions are not time-limited, weak authentication becomes normal.
- If authentication events are not monitored, brute force, credential stuffing or unusual logins remain unnoticed.

## Triggers

- new system, new cloud service, new application, new interface or new remote access.
- introduction or change of MFA, single sign-on, password manager, identity provider or privileged-access solution.
- new privileged role, external access, service provider account or service account.
- account compromise, suspicious logins, phishing wave or credential leak.
- reset, recovery or support process is changed.
- audit finding, vulnerability finding or monitoring hit.
- periodic review of critical authentication methods and exceptions.

## Roles and responsibilities

- **IAM / Identity Owner:** owns identity source, authentication methods, MFA logic and technical policies.
- **IT / Platform Owner:** implements authentication in systems, cloud services and applications.
- **Service Owner / Application Owner:** assesses protection need, user groups and exception need.
- **Security role / ISMS Owner:** defines minimum logic, review requirements, monitoring and escalation points.
- **Support / Service Desk:** operates reset and recovery processes with clear verification steps.
- **HR / Supplier Management:** provides onboarding, offboarding and contract events for accounts.
- **Data Protection / Legal:** reviews personal login analyses, employee data and contractual questions.
- **Management:** decides on costs, user acceptance, exception rates or unacceptable residual risks.

## Implementation

### Minimum start

Goal: do not make critical access dependent on weak secrets alone.

1. Critical systems, cloud services, remote access, admin access and external access are named in the scope.
2. MFA or an equivalently justified stronger method is planned and implemented for these accesses.
3. Password and secret rules are aligned with realistic use, lockout, reuse and secure storage.
4. Reset and recovery processes receive documented verification steps.
5. Service accounts, API keys and tokens receive owner, purpose and expiry or review date.
6. Exceptions are time-limited, justified and reviewed.

Minimum evidence:

- scope of critical authentication targets,
- MFA/authentication status by target group,
- documented reset or recovery flow,
- service account/token list with owner,
- exception decisions with follow-up.

### Solid practice

Goal: authentication is operated on a risk basis, repeatably and reviewably.

1. Authentication requirements are distinguished by access type: standard users, privileged users, external users, technical identities, API access.
2. MFA coverage, exceptions, recovery events and suspicious logins are analysed regularly.
3. Privileged accounts receive stronger methods, separated use or additional approvals.
4. Machine identities are inventoried, rotated and limited to minimum permissions.
5. New applications are checked against the authentication logic before production use.
6. Support processes prevent identity verification from being replaced by informal confirmation.
7. Findings feed into the action log, awareness, IAM improvements or management review.

### Advanced practice

Goal: authentication is controlled by context and risk.

1. Identity provider, device trust, network/location context and risk indicators are considered for critical access.
2. Privileged activities use time-limited permissions, stronger approvals or session monitoring where appropriate.
3. Anomalies such as impossible travel, unusual time, new devices or repeated failed attempts trigger triage.
4. Secrets, tokens and certificates are centrally managed, rotated and integrated into CI/CD or operations processes.
5. Authentication metrics are integrated into security monitoring, incident response and management reporting.
6. Recurring weaknesses lead to architecture, tool or process decisions.

## Routine flow

1. **Authentication need arises:** new system, new role, external access, service account or change.
2. **Classify protection need:** assess data class, exposure, privilege level, user group and impact of misuse.
3. **Define method:** select MFA, SSO, certificate, token, password manager, machine identity or special process.
4. **Implement:** configure technical policy, groups, reset rules, token lifetime and logging.
5. **Capture evidence:** document scope, decision, technical implementation, exceptions and review date.
6. **Monitor:** review failed attempts, suspicious logins, recovery cases and exceptions.
7. **Review:** regularly assess MFA coverage, service accounts, tokens, privileged and external access.
8. **Improve or escalate:** send weak methods, high exception rate or resource needs to management or incident response.

## Decisions

- Which accesses mandatorily require stronger authentication?
- Which methods are practical and effective for which user groups?
- Who may approve exceptions and for how long?
- How are recovery and support protected against social engineering?
- Which technical identities need rotation, expiry date or stronger safeguards?
- Which login analyses are permissible and need data protection clarification?

## Evidence

### Strong evidence

- current scope of critical systems and access types,
- MFA or authentication coverage with date,
- technical policy exports or configuration evidence,
- documented reset and recovery verification steps,
- service account/token register with owner, purpose, rotation and expiry date,
- review records for exceptions and privileged access,
- incident or monitoring tickets for unusual login events,
- management decision for accepted residual risks.

### Weak evidence

- password policy without technical enforcement,
- MFA screenshot without scope or target-group reference,
- generic statement “SSO in place” without review,
- list of technical accounts without owner,
- reset process as informal service desk practice,
- metric on login errors without analysis or decision.

### Evidence gaps

- critical systems outside the identity provider,
- external or privileged accounts without MFA,
- service accounts without responsible persons and rotation,
- exceptions without expiry date,
- recovery process without identity verification,
- no triage of unusual authentication events.

## Effectiveness review

Review questions:

- Are critical, external and privileged accesses protected by appropriate authentication?
- Is it traceable which systems are not connected to the central method and why?
- Are exceptions reviewed with time limits and reduced?
- Are service accounts, API keys and tokens assigned to an owner?
- Has the reset/recovery process been reviewed for misuse?
- Are unusual login events transferred into monitoring or incident triage?

Possible metrics:

- MFA coverage of critical access,
- number and age of exceptions,
- privileged accounts without stronger method,
- service accounts without owner or expiry date,
- suspicious login events with triage,
- recovery cases by channel and result,
- overdue token rotations.

## BSIG/NIS2 connection point

Secure authentication is compatible with NIS2-oriented topics such as access protection, cyber hygiene, secure administration, incident prevention and protection of critical services. Organisations should define the concrete connection in the requirements register, risk analysis and technical architecture review.

This artefact does not replace legal advice, data protection review or binding assessment of applicability.

## Boundaries

- This artefact is not a product comparison for MFA, IAM or PAM solutions.
- It does not replace a complete access concept or technical architecture review.
- It makes no binding statement on legal obligations or certification readiness.
- Login and behaviour analyses require appropriate human review.
- No ISO 27002 text, no real credentials, no secret configuration details.

## Handoffs

- **IAM handoff:** role model, identity source, MFA, account lifecycle, technical identities.
- **Incident handoff:** compromised credentials, suspicious logins, MFA fatigue, credential stuffing.
- **Service desk handoff:** reset, recovery, identity verification and social-engineering protection.
- **Data protection / Legal handoff:** personal login analyses, employee monitoring, external identities.
- **Development / DevOps handoff:** API keys, secrets, certificates, CI/CD authentication.
- **Management handoff:** high exception rate, cost/usability conflicts, legacy systems that cannot be covered.
- **Audit / Evidence handoff:** missing scope coverage, missing exception reviews, incomplete token registers.

## Typical mistakes

- MFA is enabled only for some cloud services and then considered complete.
- Recovery processes are weaker than normal login.
- Service accounts are treated like normal users.
- Tokens and API keys run without limits.
- Exceptions become permanent for convenience reasons.
- Login alerts are generated, but nobody triages them.
- Password rules increase effort without reducing real attack paths.

## Fictional mini example

A fictional manufacturer introduces SSO for its customer portal. During the review, the Identity Owner finds that administrators use MFA, but three external support accounts and several API tokens exist without expiry date. The Service Owner confirms that two external accounts are no longer required. They are removed; MFA is enabled for the remaining accounts. API tokens receive owner, purpose, rotation date and an entry in the action log.

Evidence:

- scope of the customer portal,
- MFA coverage overview,
- ticket to withdraw external accounts,
- token register with rotation date,
- review decision by the Service Owner.
