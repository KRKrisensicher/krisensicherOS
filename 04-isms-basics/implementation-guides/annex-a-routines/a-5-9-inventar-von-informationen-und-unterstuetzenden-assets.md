# A.5.9 — Inventory of information and supporting assets

## Purpose

An inventory of information and supporting assets makes visible which information, systems, services, devices, data repositories, interfaces, and external dependencies are relevant for security and operations. Without this picture, risks, access, protection needs, vulnerabilities, emergency planning, and responsibilities can only be steered by chance.

The core is not a perfect CMDB, but a current, usable inventory with owners, criticality, protection needs, and connection to routines.

## Control objective in repository language

The organization operates an inventory routine that identifies, assigns responsibility for, classifies, updates, and connects relevant information and supporting assets in the ISMS scope with risk, access, vulnerability, supplier, change, and BCM processes.

## Typical risks

- If critical assets are unknown, they are not protected, patched, backed up, or prioritized in an emergency.
- If information is not assigned, owners, protection needs, and usage requirements are missing.
- If inventories become outdated, risk analyses and reviews are based on false assumptions.
- If SaaS services, interfaces, or data repositories are missing, shadow IT and uncontrolled data flows arise.
- If technical assets are maintained without business connection, vulnerabilities and access cannot be prioritized.
- If supporting assets such as service providers, keys, certificates, backups, or documentation locations are missing, dependencies surface only during an event.

## Triggers

- new or changed service, process, site, data set, system, SaaS service, interface, or service provider.
- project start, change, migration, decommissioning, procurement, or operational handover.
- vulnerability finding, incident, audit finding, or BCM exercise with unknown asset connection.
- change in protection need, data class, criticality, or owner.
- periodic inventory review.
- role change among asset owners or technical responsible parties.
- management decision on scope, prioritization, budget, or risk acceptance.

## Roles and responsibilities

- **Asset owner / information owner:** is responsible for business assignment, protection need, criticality, and usage context.
- **IT/platform owner:** maintains technical asset data, lifecycle, configurations, and operational status.
- **ISMS owner / security role:** defines minimum fields, review logic, risk and evidence connection.
- **Business unit / process owner:** names information, data repositories, processes, and dependencies.
- **Procurement / vendor management:** provides service provider, SaaS, and contract connections.
- **BCM role:** uses inventory data for criticality, recovery, dependencies, and emergency planning.
- **Management:** decides scope, resources, tolerated inventory gaps, and prioritization.

## Implementation

### Minimum start

Goal: make the most important information and assets in the ISMS scope visible and assigned.

1. The organization defines a starting scope: core services, critical processes, most important data sets, central systems, and relevant SaaS services.
2. Minimum fields are maintained for each entry: name, type, owner, purpose, criticality, data/protection need, location or service, technical responsible party, review date.
3. New projects and changes must check whether inventory entries need to be created or changed.
4. Critical assets are linked with access, backup, vulnerability management, and emergency planning.
5. At least quarterly or semi-annually, the organization checks whether critical entries are current.
6. Known gaps are documented with owner and follow-up date.

Minimum evidence:

- inventory list for critical information and assets,
- owner and review date for each critical entry,
- protection-need or criticality classification,
- change evidence from project/change,
- list of open inventory gaps.

### Solid practice

Goal: the inventory is used as a steering basis for ISMS routines.

1. Asset types are distinguished: information, applications, infrastructure, endpoints, cloud/SaaS services, interfaces, identities, service providers, keys/certificates, backups.
2. Minimum fields and maintenance responsibility are defined for each asset type.
3. Inventory entries are connected with risks, controls, data classes, access reviews, vulnerability sources, suppliers, and BCM criticality.
4. Lifecycle states are maintained: planned, productive, restricted, in migration, out of service, archived.
5. Samples and reconciliations check completeness: procurement, cloud console, network, endpoint management, SaaS list, project portfolio.
6. Unknown or unassignable assets are triaged and escalated.
7. Inventory quality is reported in the ISMS review.

Strong evidence:

- asset and information register with defined minimum fields,
- owner confirmation of critical entries,
- reconciliation records against technical or commercial sources,
- change and decommissioning evidence,
- links to risks, access, vulnerabilities, and BCM,
- measure log for inventory gaps.

### Advanced practice

Goal: inventory data is current, integrated, and decision-capable.

1. Technical discovery, cloud inventories, endpoint management, CMDB, SaaS register, and contract data are merged or regularly reconciled.
2. Criticality, exposure, data class, and dependencies influence prioritization in vulnerability, access, backup, and incident processes.
3. Changes create automatic or semi-automatic inventory updates.
4. Dependencies between services, interfaces, service providers, and recovery objectives are visible.
5. Management receives metrics on coverage, unknown assets, critical gaps, outdated entries, and technical debt.
6. Inventory quality is treated as a prerequisite for relevant security decisions.

## Routine flow

1. **Asset or information emerges:** new system, data set, service, interface, contract, device, or key material.
2. **Create or update entry:** record type, purpose, owner, responsible parties, criticality, protection need, and status.
3. **Assign dependencies:** connect process, service, data class, access, supplier, backup, monitoring, vulnerability source, and BCM connection.
4. **Perform review:** owner confirms timeliness or reports corrections.
5. **Handle gaps:** triage unknown, duplicate, outdated, or unassignable assets.
6. **Track changes:** projects, changes, migrations, and decommissioning update the inventory.
7. **Secure evidence:** document review, reconciliation, correction, and management decisions.
8. **Improve:** adjust minimum fields, sources, and reconciliations to findings and operational needs.

## Decisions

- Which information and assets are critical enough for the starting scope?
- Which minimum fields are necessary without making the inventory unmaintainable?
- Who may change criticality, protection need, and owner?
- Which inventory gaps are tolerable, and which must be escalated?
- Which sources are authoritative: business unit, IT, procurement, cloud platform, CMDB?
- How are shadow IT, unknown SaaS services, or unassignable assets handled?

## Evidence

### Strong evidence

- current inventory with owners, criticality, protection need, and review date,
- evidence of owner reviews and corrections,
- reconciliation against technical, commercial, or project-related sources,
- linking of critical assets to risk, access, vulnerability, backup, and BCM routines,
- decommissioning or change evidence,
- measures and decisions on inventory gaps,
- management decision for unacceptable unknown assets or resource need.

### Weak evidence

- one-off Excel list without owner or review date,
- purely technical device list without business connection,
- CMDB extract without criticality and protection need,
- asset list only for on-premise systems without SaaS and cloud,
- inventory policy without evidence of maintenance,
- screenshots of individual tools without reconciliation or decision.

### Evidence gaps

- critical services without assigned assets,
- information without owner,
- unknown external services or data repositories,
- technical accounts, certificates, or interfaces without responsible party,
- no connection to vulnerability management or backup,
- outdated entries after migration or decommissioning,
- no review or reconciliation routine.

## Effectiveness review

Review questions:

- Are the most important information, systems, services, and dependencies in scope visible?
- Does every critical asset have a business and technical responsible party?
- Are new projects, changes, and procurements reflected in the inventory?
- Can vulnerabilities, access, and emergency planning build on inventory data?
- Are unknown or outdated assets found and treated?
- Does the inventory lead to decisions, prioritization, and measures rather than only filing?

Possible metrics:

- share of critical assets with owner and review date,
- number of unknown or unassignable assets,
- share of assets with criticality and protection need,
- overdue inventory reviews,
- deviations from technical or commercial reconciliations,
- share of critical assets with backup, vulnerability, and BCM connection.

## BSIG/NIS2 connection point

A reliable inventory is connectable to NIS2-oriented risk management, incident handling, vulnerability management, access protection, supply-chain security, business continuity, and management oversight. For affected organizations, the concrete connection should be assessed in the requirements register, risk analysis, and evidence pack.

This artifact does not replace legal assessment of applicability and does not make a binding determination of statutory evidence obligations.

## Boundaries

- This artifact is not a complete CMDB or ITAM tool design.
- It does not replace technical discovery, contract review, data protection inventories, or architecture modeling.
- It provides no certification, conformity, or security guarantee.
- It contains no licensed standards text.
- An inventory is only as reliable as its maintenance and review routine.

## Handoffs

- **Project/change handoff:** new, changed, or decommissioned assets and data sets.
- **Access handoff:** owners, critical data sets, admin access, and external access.
- **Vulnerability handoff:** technical assets, exposure, criticality, and patch responsibility.
- **BCM handoff:** critical services, dependencies, recovery, and emergency prioritization.
- **Supplier handoff:** SaaS, managed services, third-party products, support access, and contract connection.
- **Data protection/legal handoff:** personal data, retention, contractual or legal questions.
- **Management handoff:** unknown critical assets, resource need, unacceptable inventory gaps.
- **Audit/evidence handoff:** missing owners, missing reviews, or non-traceable coverage.

## Typical mistakes

- The inventory is built once and then not operated.
- Only servers are recorded, while information, SaaS, interfaces, and service providers are missing.
- Owners are entered but never check timeliness.
- Criticality is estimated technically and not connected with business processes.
- Decommissioned systems remain in the inventory, new cloud resources are missing.
- Inventory and vulnerability management use different asset names.
- Management receives lists, but no statement on gaps, priorities, and risks.

## Fictional mini example

A fictional medium-sized company adds a customer portal to the ISMS scope. The ISMS owner creates a minimum inventory with IT and the business unit: portal, database, identity service, backup storage, monitoring, external hosting service, and two interfaces. During review, an owner is missing for an old export repository. The business unit names the owner, reduces retention, and creates a change ticket for decommissioning.

Evidence:

- inventory entries with owners and criticality,
- review note on the export repository,
- decision on decommissioning,
- change ticket,
- updated connection to backup and vulnerability process.
