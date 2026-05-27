# A.5.14 — Information transfer between parties

## Purpose

Information transfer between parties ensures that information remains controlled when it is shared, sent, provided, or received. This covers internal and external transfers: email, data rooms, interfaces, portals, storage media, support access, messengers, file repositories, postal mail, and personal handovers.

The core is not “we sometimes encrypt,” but a clear decision routine: Which information is transferred to whom, through which channel, with which approval, protection, evidence, and feedback?

## Control objective in repository language

The organization operates a traceable routine for secure, purpose-bound, and reviewable information transfer. The routine connects classification, recipient checks, approvals, suitable channels, technical protection measures, contractual or business handoffs, logging, exception handling, and incident escalation.

## Typical risks

- If confidential information is transferred through unsuitable channels, it can be disclosed or changed without authorization.
- If recipient or purpose are not checked, misdirected sending, excessive sharing, or unclear responsibility arise.
- If interfaces and data exchanges are operated without owners, changes, errors, and security events remain unnoticed.
- If external parties do not know protection requirements, control ends at the organizational boundary.
- If transfer evidence is missing, approvals, delivery, integrity, or withdrawal cannot be traced.

## Triggers

- New external party, new service provider, new customer or authority communication.
- New interface, data room, portal, API, export, or regular data exchange.
- Transfer of confidential, personal, business-critical, or contractually protected information.
- Change of classification, recipient, purpose, channel, data scope, or frequency.
- Misdirected sending, delivery problem, data leakage, suspected manipulation, or incident.
- Audit finding, customer requirement, contract change, or risk decision.
- Periodic review of important data transfers.

## Roles and responsibilities

- **Information Owner / Process Owner:** decides purpose, scope, recipient, and business approval.
- **ISMS Owner / Security role:** defines minimum requirements, risk logic, exception handling, and review.
- **IT/Platform Owner:** provides suitable channels, encryption, data rooms, interfaces, and logs.
- **Data Protection / Legal:** reviews personal data, contracts, confidentiality, international or legally sensitive transfers.
- **Procurement / Supplier Management:** connects transfer with service provider contracts, subcontractors, and return rules.
- **Business units:** check recipient, purpose, data scope, and correct channel in daily work.
- **Incident Response:** takes over in case of misdirected sending, suspected disclosure, or compromise.
- **Management:** decides on high residual risks, resource conflicts, or unavoidable insecure transfer.

## Implementation

### Minimum start

Goal: Critical information transfers are consciously approved and performed with evidence.

1. The organization names permitted standard channels per information class, for example collaboration platform, data room, encrypted email, portal, or personal handover.
2. For confidential or critical information, recipient, purpose, and data scope are checked before transfer.
3. Recurring external transfers receive owner, frequency, and storage location for evidence.
4. Misdirected sending or wrong recipients are treated as security reports.
5. Exceptions from standard channels are justified, time-limited, and reviewed.
6. Business units receive a short decision aid for sending and sharing.

Minimum evidence:

- channel and handling matrix per information class,
- approval or ticket evidence for critical transfer,
- list of regular external data exchanges,
- communication or training evidence,
- incident or exception protocol in case of deviation.

### Solid practice

Goal: Information transfer is steered on a risk basis, repeatably, and with contractual connection points.

1. Data flows and regular transfers are maintained in an information or interface register.
2. Protection measures are based on classification, recipient, purpose, channel, integrity need, and evidence need.
3. External parties confirm handling requirements through contract, agreement, portal rules, or technical terms of use where appropriate.
4. Interfaces receive an owner, technical responsibility, monitoring, change process, and incident path.
5. Approval and four-eyes rules are defined for particularly critical transfers.
6. Samples check recipient, channel, scope, approval, and evidence.
7. Lessons learned from misdirected sending and interface problems feed into rules and training.

Strong evidence:

- data flow or transfer register,
- approvals with purpose, recipient, and scope,
- technical channel or encryption evidence,
- interface documentation with owner,
- supplier or contract evidence,
- sample and correction protocols,
- incident lessons learned.

### Advanced practice

Goal: Critical transfers are technically supported, monitored, and reported in a decision-ready way.

1. Data rooms, portals, APIs, managed file transfer, DLP, or rights management enforce or support suitable protection measures.
2. Regular data exchanges are connected with monitoring, error handling, integrity checks, and change approval.
3. Highly critical transfers use additional controls such as recipient confirmation, expiry date, watermarking, access revocation, or log review where appropriate.
4. Deviations from DLP, mail gateways, interface monitoring, or support processes are triaged.
5. Metrics show critical transfers, exceptions, misdirected sending, overdue reviews, and open supplier feedback.
6. Management sees trade-offs between speed, collaboration, cost, and protection needs.

## Routine flow

1. **Transfer need arises:** request, project, interface, export, support case, or external collaboration.
2. **Classify information:** check class, protection need, personal or contractually protected content.
3. **Check recipient and purpose:** clarify authorization, identity, role, organization, and data minimization.
4. **Choose channel:** define standard channel or justified exception.
5. **Obtain approval:** involve owner, business unit, Legal/Data Protection, or Management depending on risk.
6. **Transfer:** apply protection measures and generate evidence.
7. **Confirm and monitor:** check delivery, access, interface run, error, or withdrawal.
8. **Handle deviation:** escalate misdirected sending, wrong channel, unclear recipients, or technical errors.
9. **Review:** update regular transfers, exceptions, and findings.

## Decisions

- Which channels are permitted per information class?
- Which transfers require owner approval, four-eyes principle, or management decision?
- When is encryption, data room, portal, or interface required?
- Which recipient check is needed before external transfer?
- How are recurring data exchanges registered and reviewed?
- When does misdirected sending become an incident?
- Which exceptions are permitted and for how long?

## Evidence

### Strong evidence

- transfer register with owner, recipient, purpose, channel, frequency, and class,
- approval protocol for critical transfers,
- technical evidence for channel, encryption, access, or integrity check,
- interface monitoring or run logs,
- supplier/contract evidence on handling and return,
- samples with corrective actions,
- incident and lessons-learned evidence for incorrect transfer.

### Weak evidence

- general note “encrypt confidential data” without channel decision,
- email thread without approval or recipient check,
- interface list without owner,
- tool screenshot without evidence of use,
- contract without connection to actual data flows.

### Evidence gaps

- regular external exports without register,
- confidential information through private or unchecked channels,
- no approval for particularly critical transfers,
- no handling of misdirected sending,
- unknown subcontractors or recipient chains,
- interface changes without review.

## Effectiveness review

Review questions:

- Are the most important external and internal data transfers known and owned?
- Can business units choose the right channel per information class?
- Are there approvals and evidence for critical transfers?
- Are misdirected sending and channel deviations reported and corrected?
- Do interfaces have owner, monitoring, and change process?
- Are Legal/Data Protection handoffs triggered in time?

Possible metrics:

- share of critical transfers with owner and register entry,
- number of channel deviations or misdirected-sending reports,
- overdue reviews of regular data exchanges,
- exceptions from standard channels,
- open supplier feedback,
- interface errors with security relevance.

## BSIG/NIS2 connection point

Controlled information transfer has a connection point to NIS2-oriented risk management measures, secure communication, supply chain security, incident handling, business continuity, access protection, and governance. The concrete relevance should be assessed organization-specifically in the requirements register, data flow overviews, and risk decisions.

This artifact does not replace legal assessment of data protection, reporting obligations, confidentiality, cross-border transfer, or contract questions.

## Boundaries

- No legal or data protection advice.
- No binding statement on which channel is permissible in every case.
- No certification, conformity, or security guarantee.
- No technical encryption baseline or product recommendation.
- No ISO 27002 text or confidential practice data.

## Handoffs

- **Classification handoff:** unclear information class or protection need.
- **Data Protection/Legal handoff:** personal data, confidentiality, contracts, international transfer, disputes.
- **IT/Platform handoff:** data rooms, email protection, interfaces, encryption, logging, monitoring.
- **Supplier handoff:** external parties, subcontractors, data return, deletion, security requirements.
- **Incident handoff:** misdirected sending, wrong recipient, data leakage, compromised channel.
- **BCM handoff:** critical transfer is necessary for business continuity or crisis communication.
- **Management handoff:** unavoidable insecure transfer, resource needs, accepted residual risk.

## Typical mistakes

- The channel is chosen for convenience, not based on information class.
- Recurring exports exist, but nobody knows the owner or recipient.
- Interfaces are treated as a purely technical topic without business approval.
- Confidential attachments are sent to distribution lists without recipient check.
- Misdirected sending is corrected but not used as a learning signal.
- External parties receive information without clear handling expectations.
- Encryption is mentioned, but key transfer or recipient check remains unclear.

## Fictional mini example

A fictional business unit wants to transfer support data monthly to an external maintenance service provider. The Process Owner records the data exchange in the transfer register: purpose, recipient, data scope, class, frequency, and channel. Data Protection and Legal review the contract and personal-data questions. IT sets up a data room with expiry date and access evidence. After two months, a sample shows that one export contained too many fields; the business unit reduces the dataset and documents the correction.

Evidence:

- transfer register entry,
- approval by Process Owner,
- Legal/Data Protection handoff note,
- data room and access evidence,
- sample result,
- correction of export scope.
