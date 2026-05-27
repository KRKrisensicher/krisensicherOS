# A.7.9 — Protection of assets outside the site

## Purpose

Assets outside the site — such as laptops, mobile storage media, spare devices, project equipment, documents, test devices, or devices at service providers — leave the organization’s controlled environment. This routine ensures that such assets do not become invisible, but are managed with owner, protection need, usage context, return or deletion logic, and evidence.

The core is not “home office is allowed”, but the question: Which assets may go where, under which conditions, with which protection, and how does the organization detect loss, misuse, or forgotten returns?

## Control objective in repository language

The organization operates a traceable routine for assets outside its own sites. It connects asset inventory, approval, technical and organizational protection measures, usage rules, loss reporting, return, and review.

## Typical risks

- If mobile devices are used without encryption, lock, or inventory reference, loss can lead to information leakage and operational interruption.
- If documents, storage media, or spare devices outside the site are not recorded, return, deletion, and accountability are missing.
- If employees or service providers take assets informally, protection needs and usage context remain unclear.
- If assets are left unattended in vehicles, hotels, events, or private environments, theft and viewing risks increase.
- If return is not checked during role changes, departure, or project end, devices, data, or accesses remain outside control.
- If loss reporting is unclear, incident response, data protection review, and replacement measures are delayed.

## Triggers

- Issuing, taking away, or shipping an asset outside a controlled site.
- Home office, mobile work, travel, event, customer project, or field service.
- Provision of spare devices, test devices, or loan hardware.
- Service provider access, repair, maintenance, or return shipment.
- Role change, departure, project end, or contract end.
- Loss, theft, damage, suspected manipulation, or late return.
- Regular inventory or review of mobile and external assets.

## Roles and responsibilities

- **Asset Owner / Service Owner:** defines protection needs, permitted use, and return requirements.
- **IT / Endpoint Owner:** provides technical protection measures, management, blocking, deletion, and tracking.
- **User / Business unit:** protects the asset in daily use, reports loss or deviation, and follows return rules.
- **Manager / Project Owner:** confirms business need and ensures return at role or project end.
- **ISMS Owner / Security Role:** defines minimum protection, exception handling, review, and escalation logic.
- **HR / People function:** triggers return and access checks on departure or role change.
- **Procurement / Supplier Management:** manages assets at service providers, repairs, shipping, and contract end.
- **Data Protection / Legal:** reviews personal data, consequences of loss, contractual and reporting obligation questions in human review.

## Implementation

### Minimum start

Goal: Mobile and external assets are visible, protected, and recoverable.

1. The organization names asset types that may be used outside the site: laptops, smartphones, storage media, documents, test devices, keys, tokens, or spare hardware.
2. Owners and minimum protection are defined for these asset types: inventory entry, screen lock, encryption, secure storage, loss reporting, return.
3. Issuing or taking away is documented traceably.
4. Departure, role change, and project end trigger a return check.
5. Loss or theft triggers an incident and data protection/legal handoff according to a defined threshold.
6. Exceptions are time-limited and documented with rationale.

Minimum evidence:

- asset list or issue log with owner,
- minimum protection rule for external use,
- return evidence or offboarding check,
- loss/incident ticket in case of deviation,
- exception with deadline.

### Solid practice

Goal: External asset use is managed in a risk-based and repeatable way.

1. Assets are classified by data class, device control, location type, and user group.
2. Technical baselines for mobile devices are operated: encryption, device lock, patch level, remote lock or wipe, central management, backup or sync rule.
3. Paper documents, storage media, and special devices receive their own transport, storage, and return rules.
4. Service providers, repairs, and shipping are tracked through tickets, delivery notes, or contractual contacts.
5. Regular inventory reconciles issued assets with persons, projects, and service providers.
6. Assets that are not returned or not reachable are escalated.
7. Lessons learned from losses feed into training, endpoint management, or travel/home-office rules.

Strong evidence:

- asset inventory with external use, person/project, and owner,
- technical compliance evaluation of mobile devices,
- issue, shipping, repair, or return records,
- offboarding checklists with asset return,
- incident and lessons-learned evidence,
- exception and risk decisions.

### Advanced practice

Goal: External assets are integrated with identity, endpoint, supplier, and incident processes.

1. Asset inventory, MDM/endpoint management, HR events, and ticketing are connected.
2. Non-compliant, long-offline, or missing devices generate alerts.
3. Mobile use is coupled with data classification, conditional access, backup, DLP, or remote-wipe capability.
4. Service provider assets and repair paths are reconciled with contract and supplier reviews.
5. Management receives metrics on missing assets, non-compliance, losses, return times, and exception rates.
6. Scenarios such as trade fair, field service, emergency work, or crisis operations are exercised with BCM and incident response.

## Routine flow

1. **External use arises:** issuing, taking away, shipping, repair, project, or travel need.
2. **Clarify protection need:** assess asset type, data class, criticality, user group, and destination.
3. **Approve:** business need and minimum protection are confirmed.
4. **Issue or ship:** document inventory, accountability, return date, and protection requirements.
5. **Operate:** ensure technical compliance, usage rules, and loss reporting path.
6. **Treat deviation:** handle loss, theft, late return, or non-compliance as ticket/incident.
7. **Return or delete:** evidence return, secure deletion, access withdrawal, and inventory update.
8. **Review:** handle inventory, pattern analysis, and measures in the ISMS review.

## Decisions

- Which asset types may be used outside controlled sites?
- Which data classes may be processed on mobile or external assets?
- Which minimum protection measures are mandatory before an asset is issued?
- When is external use too risky and needs a management decision?
- Who may approve exceptions and for how long?
- Which loss or theft scenarios trigger incident, legal, or data protection handoff?
- How are assets at service providers, in repairs, and in shipping tracked?

## Evidence

### Strong evidence

- current asset inventory with external assignment,
- issue and return evidence,
- technical compliance reports for mobile devices,
- offboarding or project-closure evidence,
- loss/theft tickets with decisions,
- shipping, repair, or service provider records,
- time-limited exceptions with review date,
- management decision for non-recoverable or high-risk assets.

### Weak evidence

- general home-office rule without asset reference,
- inventory list without person, project, or return status,
- device screenshot without date or compliance context,
- verbal assurance that devices are encrypted,
- loss report without follow-up decision.

### Evidence gaps

- issued assets without owner,
- external use without approval or protection need,
- return on departure not evidenced,
- non-compliant devices without escalation,
- repair or shipping without tracking,
- storage media or paper documents outside the site without rule.

## Effectiveness review

Review questions:

- Is it traceable who uses external assets, why, and until when?
- Are mobile devices technically protected and verifiably managed?
- Are departures, role changes, and project ends linked to return?
- Are loss and theft reported and treated quickly enough?
- Are service provider, repair, and shipping paths visible?
- Do inventory findings lead to measures or management decisions?

Possible metrics:

- share of external assets with owner and return status,
- number of overdue returns,
- devices outside technical compliance,
- time from loss report to blocking/deletion decision,
- open exceptions and overdue follow-ups,
- inventory differences by asset class.

## BSIG/NIS2 connection point

The protection of assets outside the site can connect to NIS2-oriented risk management measures, cyber hygiene, access protection, incident capability, supply chain security, and business continuity. The concrete connection should be assessed in the requirements register, in risk analyses, and in offboarding/asset processes.

This artifact does not replace legal review of reporting obligations, data protection consequences, or applicability.

## Boundaries

- This artifact is not a complete mobile device management architecture.
- It does not replace data protection review when personal data is lost.
- It does not replace employment-law, insurance-law, or contractual assessment.
- It makes no certification or conformity commitment.
- Public examples must not contain real personal, device, or location data.

## Handoffs

- **HR handoff:** departure, role change, longer absence, or return escalation.
- **IT/endpoint handoff:** encryption, blocking, deletion, compliance, backup, and device replacement.
- **Incident handoff:** loss, theft, suspected manipulation, unauthorized use, or unreachable device.
- **Data Protection/Legal handoff:** possible disclosure of personal data, contractual questions, reporting obligation review, or employment-law aspects.
- **Procurement/supplier handoff:** repair, shipping, service provider devices, loan devices, or contract end.
- **BCM handoff:** external assets are required for emergency work or critical operational capability.
- **Management handoff:** non-recoverable assets, high exception rate, investment need, or accepted residual risk.
- **Audit/evidence handoff:** unclear inventory data, missing return evidence, or incomplete loss handling.

## Typical mistakes

- Laptops are inventoried, but paper documents, storage media, and special devices are forgotten.
- Home-office rules do not replace an asset and return routine.
- Offboarding checks access, but not devices, tokens, keys, or documents.
- Loss reports reach IT, but not incident response or data protection review.
- Repairs and shipping run informally through individuals.
- Technical device protection measures exist, but are not verifiable.
- Exceptions for project devices continue without a time limit.

## Fictional mini example

A fictional consulting team issues five laptops and two test devices for a customer project. The project ticket contains asset numbers, users, return date, and minimum protection. At project close, one test device is missing. The Project Owner reports the deviation, IT blocks associated accesses, and management decides whether replacement procurement and risk acceptance are required. The return check is then added to the project closure checklist.

Evidence:

- project ticket with asset assignment,
- technical compliance evaluation of the laptops,
- return record,
- deviation ticket for the missing test device,
- management decision and updated closure checklist.
