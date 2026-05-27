# A.8.24 — Using cryptographic procedures

## Purpose

Cryptographic procedures protect information and communication paths from unauthorized reading, modification, or impersonation. The routine ensures that encryption, signatures, certificates, keys, and secrets are not solved randomly per system, but operated with clear responsibility, lifecycle, and review.

## Control objective in repository language

The organization defines where cryptographic procedures are needed, which minimum requirements apply, who is responsible for keys and certificates, how generation, storage, use, rotation, revocation, and expiry are controlled, and which evidence makes secure operation plausible.

## Typical risks

- If data is transmitted or stored unencrypted, it may be disclosed through misrouting, loss, or third-party access.
- If outdated or weak procedures are used, apparent protection exists despite enabled encryption.
- If certificates or keys expire, are lost, or are copied in an uncontrolled way, services may fail or be misused.
- If secrets end up in code, tickets, or configuration files, attackers may gain access to systems and data.
- If responsibility for key material remains unclear, rotation, revocation, and emergency recovery cannot be controlled.

## Triggers

- new system, new interface, new data storage, new mobile use, or new cloud/SaaS connection.
- processing or transmission of information requiring protection.
- certificate expiry, key rotation, suspected compromise, or secret leak.
- architecture, development, procurement, or data protection review.
- vulnerability notification relating to protocol, library, certificate, key management, or crypto configuration.
- incident, audit finding, or management question about protection need and encryption coverage.

## Roles and responsibilities

- **Asset owner / service owner:** determines protection need, business requirements, and accepts or escalates residual risks.
- **IT/platform owner:** operates certificates, key management, configurations, and technical evidence.
- **Development / product owner:** integrates cryptography securely into applications, interfaces, CI/CD, and secrets management.
- **Security architecture / ISMS owner:** defines minimum requirements, procedures, exception process, and review logic.
- **Data protection / legal:** review requirements for personal data, contracts, export/legal questions, or evidence obligations where affected.
- **Incident response:** takes over for key compromise, secret leak, or suspected cryptographic failure.
- **Management:** decides on legacy exceptions, investment need, risk acceptance, or conflicts with operating objectives.

## Implementation

### Minimum start

Goal: make critical encryption and key topics visible and controllable.

1. The organization names critical use cases: transport encryption, storage media encryption, backups, cloud storage, administrative access, API communication, email or file exchange.
2. For critical certificates, keys, and secrets, owner, purpose, storage location, expiry date, and emergency contact are recorded.
3. Minimum requirements are defined: no known weak procedures, no plaintext secrets in code or tickets, regulated certificate renewal.
4. New systems and interfaces must name encryption needs in the architecture or change process.
5. Exceptions are time-limited, justified, and managed with a risk decision.

Minimum evidence:

- cryptography/certificate register for critical use cases,
- technical configuration evidence for selected critical services,
- expiry or rotation dates,
- secret leak prevention rule for code and configuration,
- exception decisions with follow-up date.

### Solid practice

Goal: cryptographic procedures are operated repeatably through lifecycle, roles, and technical standards.

1. Cryptographic minimum requirements are described by use case: transport, storage, backup, mobile devices, APIs, signatures, and secrets.
2. Certificate and key management covers generation, storage, access, rotation, backup, revocation, and expiry monitoring.
3. Secrets are maintained in suitable secret management mechanisms and not stored in repositories, images, tickets, or documents.
4. Development and platform teams review crypto configurations before go-live and during relevant changes.
5. Outdated protocols, expiring certificates, and weak configurations are handled through vulnerability or measures management.
6. Critical exceptions are decided in ISMS or management review.

Strong evidence:

- documented minimum requirements per use case,
- register of critical certificates, keys, and secrets with owners,
- technical scan or configuration evidence,
- tickets for certificate renewal, rotation, or secret cleanup,
- review records for exceptions and legacy procedures,
- incident or lessons learned evidence for secret leaks.

### Advanced practice

Goal: cryptography is controlled as an integrated security building block in architecture, development, and operations.

1. Certificate expiries, weak TLS/SSH/API configurations, and secret findings are monitored automatically.
2. Key material is managed role-based, audit-capable, and separate from applications; especially critical keys use stronger protection mechanisms.
3. CI/CD, containers, infrastructure as code, and cloud environments contain checks against hardcoded secrets and insecure crypto configurations.
4. Cryptographic procedures are considered in architecture decisions, data classification, supplier assessment, and contingency planning.
5. Management receives metrics on coverage, exceptions, expiring certificates, secret findings, and legacy risks.

## Routine flow

1. **Protection need or change arises:** new system, interface, data storage, certificate, secret, or finding.
2. **Classify use case:** determine transport, storage, signature, authentication, backup, API, mobile use, or data exchange.
3. **Define requirement:** define procedure, key length/parameters, certificate source, storage location, rotation, and responsible roles without creating a product or standard substitute.
4. **Implement technically:** set up configuration, certificate, key storage, secret management, and access protection.
5. **Validate:** perform scan, configuration test, code/repo check, or operational evidence.
6. **Control lifecycle:** monitor expiry, rotation, revocation, backup, and emergency access.
7. **Handle exceptions:** decide legacy, technical limitation, or supplier dependency with time limit.
8. **Escalate:** hand over secret leak, key compromise, critical legacy procedures, or resource conflicts.

## Decisions

- Which data, systems, and interfaces need cryptographic protection?
- Which minimum requirements apply to transport, storage, backups, APIs, and mobile use?
- Who may generate, use, rotate, revoke, or recover keys?
- Which certificates and secrets are critical enough for central monitoring?
- How are legacy systems handled if they do not meet current requirements?
- When is a cryptographic finding an incident, a change, or a management decision?

## Evidence

### Strong evidence

- cryptography or minimum requirements concept with use cases and owners,
- certificate/key/secret register with expiry and rotation dates,
- technical evidence for encryption in critical services,
- repo/CI check evidence against plaintext secrets,
- tickets for rotation, revocation, renewal, or configuration correction,
- exception decisions with expiry date and compensating measure,
- incident and lessons learned evidence for secret or key events.

### Weak evidence

- general statement “data is encrypted” without scope or evidence,
- certificate list without owner or expiry monitoring,
- screenshot of a TLS connection without review logic,
- password-protected file as a substitute for key management,
- policy without technical sample.

### Evidence gaps

- unknown certificates or keys in critical services,
- secrets in code, scripts, images, tickets, or documentation,
- no rotation or revocation process,
- expired or weak configurations without measures,
- supplier cryptography without evidence or contact person,
- exceptions without risk decision.

## Effectiveness review

Review questions:

- Are critical cryptography use cases and owners known?
- Are certificates, keys, and secrets controlled across their lifecycle?
- Can critical services provide technical encryption evidence?
- Are weak or outdated procedures found and handled?
- Are secrets removed from or prevented in code, tickets, and plaintext configurations?
- Is there a routine for expiry, rotation, revocation, and suspected compromise?

Possible metrics:

- critical certificates with expiry monitoring,
- certificates close to expiry or expired,
- open cryptography findings by risk class,
- secret findings in repositories or artifacts,
- overdue key rotations,
- number and age of cryptographic exceptions.

## BSIG/NIS2 connection point

The use of cryptographic procedures is a connection point for NIS2-oriented topics such as risk management, cyber hygiene, access protection, secure communication, data protection, incident prevention, secure development, and supply chain security. The specific classification should be assessed organization-specifically in the requirements register, risk analyses, and technical architecture reviews.

This artifact does not replace legal assessment, data protection review, or binding statement on legal requirements.

## Boundaries

- This artifact is not a cryptography library recommendation and not a technical parameter list for every use case.
- It does not replace specialist review for high-security, payment, health, KRITIS, cloud, or product requirements.
- Cryptography does not protect against incorrect permissions, compromised endpoints, or poor key management.
- Data protection, contract, or export questions may require human review.
- No certification promise and no adoption of licensed standard text.

## Handoffs

- **Architecture handoff:** new systems, interfaces, data flows, cloud designs, or legacy exceptions.
- **Development handoff:** API security, libraries, secrets in code, CI/CD checks, signatures.
- **Change handoff:** certificate renewal, key rotation, protocol shutdown, or configuration change.
- **Incident handoff:** secret leak, key compromise, certificate misuse, or suspected cryptographic failure.
- **Data protection/legal handoff:** personal data, contractual encryption requirements, legal or export questions.
- **Supplier handoff:** SaaS/provider encryption, key custody, evidence, support paths.
- **Management handoff:** legacy procedures, investment need, operational risk, accepted residual risk.

## Typical mistakes

- Encryption is treated as a checkbox without operating the key and certificate lifecycle.
- Certificates expire because expiry dates belong to nobody.
- Secrets are stored in repositories, scripts, tickets, or wiki pages.
- Legacy protocols remain active because shutdown is not decided.
- Supplier promises are not connected with evidence or responsibilities.
- Backups or exports are forgotten although they contain the same data.
- Management sees technical detail findings, but no decision on legacy risks and resources.

## Fictional mini example

A fictional SaaS provider discovers an API key in an old deployment script during a repository check. The development team blocks the key, creates a new secret management entry, and removes the script. The platform owner additionally reviews the certificate list and finds two certificates expiring soon. In the ISMS review, it is decided to make expiry warnings and secret scans mandatory in the release process.

Evidence:

- secret finding and cleanup ticket,
- evidence of key revocation and new creation in secret management,
- updated certificate list,
- tickets for certificate renewal,
- review decision on CI/CD checking.
