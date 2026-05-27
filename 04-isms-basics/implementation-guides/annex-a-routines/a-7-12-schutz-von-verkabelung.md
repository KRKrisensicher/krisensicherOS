# A.7.12 — Protection of cabling

## Purpose

Cabling connects systems, rooms, sites, network segments, sensors, and utility infrastructure. Unprotected or unclear cable routes can cause outages, manipulation, incorrect connections, unauthorized interception, sabotage, or difficult recovery. This routine ensures that critical cable routes, patch panels, cable paths, and network outlets are not treated as invisible infrastructure.

The core is not “lay cables neatly”, but an operated protection logic: Which connections are critical, where do they run, who may make changes, how are manipulation and mispatching prevented, and how is it evidenced that the state remains controlled?

## Control objective in repository language

The organization operates a routine with which critical data, network, communication, and relevant utility cabling is planned, documented, protected against accidental or unauthorized impact, changed, and reviewed.

## Typical risks

- If patch panels or network outlets are freely accessible, unauthorized devices can be connected or connections changed.
- If cable routes are not documented, disruptions, relocations, and recovery measures delay operations.
- If critical lines run through public or unprotected areas, damage, manipulation, or interception can become more likely.
- If cabling changes are made informally, mispatching, network segmentation errors, or shadow connections arise.
- If data and utility cabling are changed without coordination, outages or security gaps can arise.
- If temporary cables for projects become permanent, they bypass protection and documentation logic.

## Triggers

- New construction, renovation, refurbishment, relocation, or space change.
- New or changed network, telephony, production, building, or security cabling.
- Patch change, new network outlet, carrier/WAN change, or technical room change.
- Disruption, outage, suspected manipulation, unclear port, or unknown device.
- New service provider, maintenance, building work, or facility measure.
- Audit finding, location review, or security event.
- Regular review of technical rooms, patch panels, cable routes, and documentation.

## Roles and responsibilities

- **Network / IT Infrastructure Owner:** is responsible for technical cabling logic, patch panels, network outlets, documentation, and change approvals.
- **Facility / Location Owner:** is responsible for structural cable routes, shafts, rooms, service provider access, and protection against environmental impact.
- **Service Owner / Asset Owner:** assesses criticality of affected connections and impact of changes.
- **ISMS Owner / Security Role:** defines protection, review, and exception requirements for critical cable routes.
- **Service provider / installation partner:** implements changes only according to order, approval, and documentation requirement.
- **BCM Owner / Crisis Role:** considers critical connections in recovery and alternate-site planning.
- **Management:** decides on structural protection needs, redundancy costs, residual risks, or permanent exceptions.

## Implementation

### Minimum start

Goal: Critical cabling and patch points are visible, protected, and change-controlled.

1. The organization identifies critical cable areas: technical rooms, patch panels, carrier handover points, connections to critical systems, branch offices, production or building technology.
2. Owners and contact paths are named for these areas.
3. Changes to critical patching or cable routes are made only by ticket or documented work order.
4. Open patch panels, unclear ports, loose or temporary cables are recorded in the location review.
5. Critical areas are protected against simple unauthorized access, for example through lockable rooms, cabinets, or clear access rules.
6. Exceptions are time-limited and documented with risk or service reference.

Minimum evidence:

- list of critical cable areas or patch points,
- owner and contact assignment,
- simple cabling or patch documentation,
- change ticket or work order,
- review note with findings and measures,
- exception with deadline.

### Solid practice

Goal: Cabling protection is integrated into facility, network, and change processes.

1. Cable routes and patch panels are classified by criticality and accessibility.
2. Minimum protection is defined: access, labeling, documentation, separation of relevant lines, protection against damage, service provider escort.
3. Patch and cable changes are controlled through change management, work order, or maintenance window.
4. Network outlets and ports are connected with inventory, room, segment, or purpose.
5. Unknown or unused ports are checked and deactivated or documented where needed.
6. Renovations and refurbishments include an IT/security check for cable routes.
7. Regular spot checks compare documentation and actual state.

Strong evidence:

- patch and cabling documentation with date,
- change/work orders with approval and closure note,
- location review of technical rooms and patch panels,
- port/outlet inventory or network plan data,
- evidence of remediated mispatches or open cabling deficiencies,
- service provider records and acceptance documents.

### Advanced practice

Goal: Critical connections are connected with segmentation, monitoring, redundancy, and resilience planning.

1. Critical cable routes and carrier handovers are linked in network architecture, CMDB, BIA, and recovery plans.
2. Redundant line routes are deliberately planned, documented, and checked for shared weaknesses.
3. Port security, NAC, link monitoring, or comparable controls detect unexpected devices or connection changes.
4. Structural cable routes, shafts, and technical rooms are connected with facility risk reviews.
5. Critical patch or line changes trigger automatic or semi-automatic service and security checks.
6. Management receives information on single points of failure, structural protection gaps, and investment needs.

## Routine flow

1. **Change or review need arises:** renovation, patch change, disruption, new service, or location review.
2. **Determine criticality:** classify affected services, network segments, sites, data flows, and recovery relevance.
3. **Check cable route or patch point:** assess accessibility, documentation, labeling, protection, and dependencies.
4. **Approve change:** clarify owner, change window, service provider access, and rollback/recovery option.
5. **Implement:** patch, route, protect, remove, or deactivate according to order.
6. **Document:** update plans, port data, tickets, photos only if non-critical, acceptance, or test evidence.
7. **Validate:** check connection, segmentation, service function, and unexpected side effects.
8. **Review:** feed spot checks and findings back into measure log and risk analysis.
9. **Escalate:** pass structural deficiencies, single points of failure, or unacceptable temporary solutions to management.

## Decisions

- Which cable routes, patch panels, and handover points are critical?
- Which areas need structural or organizational access protection?
- Which changes may occur in the standard process, and which need change or management approval?
- How detailed must cabling be documented without making sensitive plans unnecessarily widely accessible?
- Which temporary cables or workarounds are permitted and for how long?
- When is redundancy, separate line routing, or additional protection needed?
- How are unknown ports, outlets, or devices handled?

## Evidence

### Strong evidence

- current patch, port, or cable-route documentation for critical areas,
- tickets or work orders for changes,
- acceptance and test evidence after cabling work,
- location review with findings, measures, and owners,
- evidence of deactivated or cleaned-up unknown ports,
- risk decision on temporary cables or unprotected line routes,
- management decision for redundancy or construction investments.

### Weak evidence

- outdated network plan without reconciliation with actual state,
- photos of patch panels without date, owner, or assessment,
- service provider invoice without documentation or acceptance reference,
- verbal statement “the electrician handles that” without order and approval,
- cable labeling without connection to service or inventory.

### Evidence gaps

- critical patch panels without access or change rule,
- unknown active ports,
- temporary cables without expiry date,
- renovations without IT/security check,
- redundancy assumptions without evidence of separate routes,
- cable changes without documentation update.

## Effectiveness review

Review questions:

- Are critical cable routes, patch points, and handovers known?
- Do documentation and actual state match in spot checks?
- Are cable and patch changes approved and documented in a controlled way?
- Are freely accessible patch panels or active ports assessed?
- Are temporary cables and workarounds removed or decided?
- Are single points of failure and redundancy assumptions checked?
- Do disruptions and mispatches feed into improvements?

Possible metrics:

- share of critical patch areas with current documentation,
- open findings from cable/patch reviews,
- unknown active ports,
- overdue temporary cabling,
- disruptions due to mispatching or cable damage,
- overdue documentation updates after changes.

## BSIG/NIS2 connection point

The protection of cabling can connect to NIS2-oriented risk management measures, operational security, physical security, maintenance of critical services, incident prevention, and business continuity. The concrete connection should be assessed in the requirements register, in architecture documents, and in location/BCM reviews.

This artifact does not replace legal review, specialist planning for electrical/network infrastructure, or a binding statement on applicability.

## Boundaries

- This artifact is not a technical cabling standard and not an installation standard.
- It does not replace building, electrical, fire protection, occupational safety, or insurance review.
- It does not replace network architecture or a segmentation baseline.
- It makes no certification or conformity commitment.
- Detailed cable and network plans can be confidential and do not belong in public examples.

## Handoffs

- **Facility handoff:** shafts, routes, rooms, structural protection, renovation, service provider access, and building work.
- **IT/network handoff:** patching, port approval, segmentation, documentation, monitoring, and disruption handling.
- **Change handoff:** critical line, patch, or carrier change with service impact.
- **BCM handoff:** single points of failure, redundant routes, recovery, and site outage.
- **Incident handoff:** suspected manipulation, unknown device, unexplained connection, cable damage, or suspected sabotage.
- **Supplier handoff:** installation partner, carrier, maintenance service provider, acceptance, and documentation obligations.
- **Management handoff:** structural protection need, redundancy investment, unacceptable residual risk, or permanent workarounds.
- **Audit/evidence handoff:** outdated plans, missing acceptances, or unclear change evidence.

## Typical mistakes

- Patch panels are physically open although they connect critical network segments.
- Cabling documentation is created during new construction and then never updated.
- Temporary cables become permanent.
- Facility commissions renovations without involving IT and Service Owners.
- Redundant lines run through the same shaft and share the same failure point.
- Unknown active ports remain active out of convenience.
- Detailed network and cabling plans are shared too broadly or stored without protection.

## Fictional mini example

A fictional site expands an office area. During the review, the Network Owner discovers several active outlets in a publicly accessible meeting area and a temporary cable to a printer. The active ports are checked, unneeded ports are deactivated, and the temporary cable is replaced by documented fixed cabling. Facility adds an IT checkpoint to the renovation process before acceptance.

Evidence:

- location review with found ports,
- change tickets for deactivation and new cabling,
- updated port documentation,
- acceptance record after cabling work,
- added IT checkpoint in the renovation process.
