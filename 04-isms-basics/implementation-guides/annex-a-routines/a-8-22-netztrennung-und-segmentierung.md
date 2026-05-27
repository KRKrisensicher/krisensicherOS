# A.8.22 — Network separation and segmentation

## Purpose

Network separation and segmentation limit which systems, user groups, services, and environments may communicate with each other. The routine reduces propagation paths, protects especially critical areas, and makes deliberate transitions visible.

## Control objective in repository language

The organization operates a traceable segmentation logic for networks, cloud environments, administration areas, development/test/production environments, critical systems, and external access paths. Segment boundaries, allowed connections, owners, exceptions, and reviews are documented and technically traceable.

## Typical risks

- If all systems are reachable in flat networks, a compromised device can quickly affect critical services.
- If production, test, and administration areas are not separated, errors or compromised accounts can reach sensitive systems.
- If third-party access or IoT/OT-adjacent systems are in the same network as core systems, propagation paths emerge that are hard to control.
- If segmentation rules are not reviewed, temporary connections remain permanently.
- If cloud and on-premises segmentation are controlled differently, inconsistent protection boundaries arise.

## Triggers

- new system, new environment, new site, new cloud landing zone, or new production/OT-adjacent component.
- introduction or change of admin access, service provider access, remote maintenance, or critical data flows.
- incident, malware finding, lateral movement, vulnerability finding, or penetration test result.
- architecture review, network review, risk analysis, or management decision.
- consolidation, migration, or decommissioning of networks and environments.
- periodic review of segments, transitions, and exceptions.

## Roles and responsibilities

- **Network/platform owner:** plans and operates segment boundaries, firewall rules, routing, cloud networks, and technical validation.
- **Service owner / asset owner:** describes protection need, data flows, and legitimate communication paths.
- **Security architecture / ISMS owner:** defines segmentation principles, risk logic, exceptions, and review requirements.
- **Change owner:** ensures that segmentation changes are tested, documented, and reversible.
- **Development / product owner:** clarifies requirements between development, test, and production environments.
- **Facility / OT responsible roles:** are involved when building, production, or special-purpose networks are affected.
- **Management:** decides on effort, availability conflicts, legacy dependency, or accepted residual risk.

## Implementation

### Minimum start

Goal: make the most important protection boundaries visible and review critical transitions.

1. The organization names critical segments: users, servers, administration, internet-exposed systems, guests/WLAN, development/test, production, backup, cloud, and service provider access.
2. Purpose, owner, and rough protection need are described for each segment.
3. Allowed connections between critical segments are recorded in a simple matrix or rule overview.
4. Particularly risky transitions such as admin access, third-party access, internet reference, or production data access are prioritized for review.
5. Temporary or broad connections are time-limited, justified, or removed.

Minimum evidence:

- segment overview with owners,
- communication matrix for critical transitions,
- tickets or changes for segment rules,
- review note on risky transitions,
- exceptions with expiry date and decision.

### Solid practice

Goal: segmentation is applied repeatably as an architecture and operating standard.

1. Segmentation principles are defined: protection need, function, exposure, environment, administration need, and trust boundary.
2. New systems receive a segment assignment during architecture or change review.
3. Connections between segments require purpose, owner, protocol, source/destination, duration, and review date.
4. Network, cloud, and identity controls are considered together so segmentation is not based only on IP rules.
5. Segmentation reviews examine old approvals, temporary rules, shadow connections, and bypass paths.
6. Findings from incidents, vulnerability management, and penetration tests lead to segmentation improvements.

Strong evidence:

- segmentation model or architecture principles,
- current segment and communication matrix,
- approved rule changes with purpose and owner,
- test results or validations of segment boundaries,
- review records with removal or correction decisions,
- risk decisions for legacy or exception connections.

### Advanced practice

Goal: segmentation becomes verifiable, dynamic, and connected with detection.

1. Segment boundaries are regularly validated through automated rule analyses, cloud posture checks, flow logs, or reachability tests.
2. Critical systems use additional controls such as separate admin paths, just-in-time access, or stronger identity checks.
3. Microsegmentation or software-defined policies are used where classic network boundaries are insufficient.
4. Segmentation violations, unexpected connections, or newly exposed paths generate alerts or review tickets.
5. Management sees risk development: critical transitions, legacy exceptions, flat networks, implementation effort, and technical debt.

## Routine flow

1. **Segmentation need arises:** new system, change, finding, incident, or review.
2. **Determine protection need and function:** classify data, service criticality, user group, environment, and exposure.
3. **Assign segment:** use existing segment or justify a new protection boundary.
4. **Define communication:** record necessary sources, destinations, protocols, duration, and owner.
5. **Review risk:** assess propagation paths, admin access, third-party access, legacy dependency, and bypass paths.
6. **Implement technically:** change firewall, routing, cloud policy, identity control, or access path.
7. **Validate:** test reachability, blocking, logging, and operational impact.
8. **Review and clean up:** check old rules, temporary connections, and exceptions.
9. **Escalate:** give critical areas that cannot be separated or high effort to management review.

## Decisions

- Which segments are indispensable for the minimum start?
- Which systems may communicate directly with each other and why?
- Which transitions require additional authentication, monitoring, or approval?
- Which legacy connections are accepted, compensated, or removed?
- How is segmentation controlled consistently across cloud, development, and production environments?
- When does risk justify architecture redesign or investment?

## Evidence

### Strong evidence

- current segmentation model with owners and protection need,
- communication matrix with purpose, source, destination, protocol, and review date,
- changes for segmentation rules and cloud policies,
- test results for allowed and blocked connections,
- review records with removal decisions,
- incident or vulnerability lessons learned with segmentation measures,
- management decision where separation cannot be implemented.

### Weak evidence

- network diagram without data flows or rule reference,
- firewall export without segmentation logic,
- “VLAN exists” without review of allowed transitions,
- architecture slide without technical reconciliation,
- broad separation of production and test without access evidence.

### Evidence gaps

- no owners for segments,
- unknown connections between critical areas,
- admin paths not separated or not documented,
- third-party and remote access outside segmentation logic,
- temporary approvals without expiry,
- cloud security groups not included in review.

## Effectiveness review

Review questions:

- Are critical segments, protection boundaries, and owners known?
- Is there a traceable communication matrix for critical transitions?
- Are segmentation rules reviewed on a risk basis before implementation?
- Were segment boundaries technically validated, not only described?
- Are temporary and legacy connections reduced or decided on?
- Do incident and vulnerability findings flow into segmentation measures?

Possible metrics:

- share of critical segments with current communication matrix,
- number of transitions without owner or purpose,
- overdue temporary segment approvals,
- validated segment boundaries in the review period,
- open legacy exceptions,
- findings on unexpected reachability.

## BSIG/NIS2 connection point

Network separation and segmentation are a connection point for NIS2-oriented risk management measures, cyber hygiene, access protection, incident containment, secure architecture, business continuity, and protection of critical services. The specific classification should be performed organization-specifically in the requirements register, risk analyses, and architecture reviews.

This artifact does not replace legal assessment or binding review of applicability.

## Boundaries

- This artifact is not a complete network or cloud architecture design.
- Segmentation does not replace patch management, access protection, monitoring, or incident response.
- Technical separation can influence availability, operations, and support and needs change control.
- Data protection or employment law questions may arise if segmentation logs are evaluated with personal reference.
- No certification promise and no adoption of standard text.

## Handoffs

- **Architecture handoff:** new protection boundaries, cloud landing zones, zero-trust or microsegmentation decisions.
- **Change handoff:** rule changes, routing, security groups, VPN or admin paths.
- **Incident handoff:** lateral movement, malware propagation, unexpected segment permeability.
- **Vulnerability handoff:** critical systems that must be separated more strongly or compensated because of vulnerabilities.
- **Development handoff:** separation of development, test, production, and CI/CD access.
- **BCM handoff:** segmentation influences restart, emergency operations, or critical service dependencies.
- **Management handoff:** legacy exceptions, investment need, risk acceptance, or conflict with operating objectives.

## Typical mistakes

- Segmentation is confused with VLAN names and not controlled as allowed communication.
- Production and test environments are formally separate but share admin access or data paths.
- Cloud segmentation is not merged with on-premises rules.
- Exceptions arise for projects and remain permanently.
- Segment boundaries are never technically tested.
- Admin and backup networks are forgotten.
- Management receives no decision on expensive legacy separations.

## Fictional mini example

A fictional software company discovers that test systems have direct access to a production database. The product owner confirms that this access was needed only during a migration. The platform owner removes the rule, sets up anonymized data in a separate environment for future tests, and documents the change in the segmentation review. An open exception for legacy reporting is given to management review with a time limit.

Evidence:

- updated communication matrix,
- change ticket for removing the rule,
- test evidence for the blocked connection,
- review note on data provision,
- time-limited exception for legacy reporting.
