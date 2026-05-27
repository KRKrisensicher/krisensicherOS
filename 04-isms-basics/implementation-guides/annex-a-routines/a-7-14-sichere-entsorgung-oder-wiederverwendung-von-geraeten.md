# A.7.14 — Secure disposal or reuse of equipment

## Purpose

Secure disposal or reuse prevents information from leaking through old, defective, returned or reassigned equipment. The core is a controlled handover routine: identify equipment, clarify data and protection needs, trigger deletion or destruction, review the result and evidence the whereabouts.

## Control objective in repository language

The organisation operates a traceable routine for equipment, data carriers and storage-capable components that are disposed of, sold, repaired, returned, donated or reused internally. No one relies on assumptions such as “it was probably empty”, but on owner, approval, deletion/destruction evidence and sampling.

## Typical risks

- If equipment with local data is passed on without review, confidential information can be disclosed.
- If data carriers in defective equipment are overlooked, information leaves the organisation uncontrolled.
- If returns from home office, leasing or service provider operation are not recorded, evidence of whereabouts is missing.
- If deletion is not validated, false assurance arises from incomplete or unsuitable procedures.
- If disposal service providers are not managed, chain, responsibility and evidence quality remain unclear.

## Triggers

- Equipment retirement, lease return, sale, donation or scrapping.
- Internal reuse, reinstallation, role change or return from project/home office.
- Defect, repair, component replacement or warranty case with equipment transport.
- Departure of employees or end of a service provider assignment.
- Change of data class, audit finding, security event or suspected data leakage.
- Regular review of storage, old equipment, returns and disposal evidence.

## Roles and responsibilities

- **Asset owner / equipment owner:** decides on retirement, reuse and protection need.
- **IT operations / workplace team:** performs return, inventory check, deletion, reinstallation or handover.
- **Facility / storage / procurement:** manages physical storage, disposal, lease return or onward transfer.
- **ISMS owner / security role:** defines minimum logic, samples, exception handling and evidence requirements.
- **Data protection / Legal:** review personal data, contractual and evidence requirements as well as service provider questions.
- **Management:** decides on costs, exceptions, high residual risk or missing disposal capability.

## Implementation

### Minimum start

Goal: no equipment leaves the scope without a documented data decision.

1. Return and retirement cases are recorded in a ticket or register.
2. Equipment is identified: type, serial number/asset ID, owner, last user or area of use.
3. It is checked whether data carriers, memory, SIM/memory cards or configuration data may be present.
4. Deletion, reinstallation or destruction is documented; in case of uncertainty, destruction or separate approval is chosen.
5. Reuse takes place only after reset and approval.
6. External disposal or return receives handover and result evidence.

Minimum evidence:

- return/retirement ticket,
- asset ID or serial number,
- deletion, reinstallation or destruction evidence,
- handover evidence to disposal provider/lessor,
- exception decision if evidence is missing.

### Solid practice

Goal: disposal and reuse are operated as a repeatable asset lifecycle process.

1. Equipment categories are distinguished by data and storage risk: clients, smartphones, servers, network devices, printers, removable media, IoT/OT components.
2. Approved procedures for deletion, reset, cryptographic erasure or destruction are described for each category.
3. Returns are stored securely until processing and protected against unauthorised removal.
4. Disposal service providers and leasing processes provide traceable evidence.
5. Samples check whether deletion, inventory status and whereabouts match.
6. Missing devices or evidence trigger incident, risk or management review.

Strong evidence:

- asset lifecycle register,
- equipment categories with procedures,
- deletion/destruction records,
- protected storage or handover evidence,
- sampling results,
- measure log for deviations.

### Advanced practice

Goal: equipment departures are integrated into identity, asset, endpoint and supplier processes.

1. Asset management, endpoint management, HR/leaver process and procurement provide departure and return events.
2. Encryption status, device management status and remote-wipe results are considered on return.
3. Disposal service providers are assessed based on evidence quality, chain, response time and deviations.
4. Storage stocks, old equipment and unassignable devices are regularly reconciled automatically or semi-automatically.
5. Metrics show open returns, disposal duration, missing evidence and deviation rate.
6. Reuse is connected with standard builds, hardening and role approval.

## Routine flow

1. **Departure or reuse is triggered:** return, defect, departure, lease end, redistribution or disposal.
2. **Identify equipment:** asset ID, serial number, owner, last use, possible data types.
3. **Assess data risk:** review local data, configuration, keys, tokens, data carriers or storage media.
4. **Choose treatment:** secure deletion, reinstallation, cryptographic erasure, data carrier removal, destruction or return path.
5. **Perform and review:** document result and validate by sample.
6. **Record whereabouts:** storage, reuse, disposal, lease return or service provider handover.
7. **Handle deviations:** escalate missing equipment, missing evidence, non-erasable data carrier or suspected data leakage.
8. **Improve:** feed patterns back into return process, procurement, device management or disposal provider management.

## Decisions

- Which equipment categories need deletion, destruction or separate review?
- When is reinstallation sufficient, and when is physical destruction required?
- Who may approve equipment for reuse?
- How are missing devices or missing evidence handled?
- Which disposal or leasing evidence is robust for internal management?
- Which cost and sustainability objectives conflict with protection needs?

## Evidence

### Strong evidence

- current asset register with departure status,
- return and retirement tickets,
- deletion, wipe, reinstallation or destruction records,
- handover evidence with asset connection,
- sampling records on effectiveness,
- exception or risk decisions where evidence is missing,
- management decision for systematic return or disposal problems.

### Weak evidence

- blanket disposal certificate without asset connection,
- Excel list without deletion or handover evidence,
- statement “equipment is always reinstalled” without review,
- invoice for disposal without chain or result,
- old policy without current returns.

### Evidence gaps

- equipment leaves storage without documented data treatment,
- returns from home office or service provider assignment are missing,
- data carriers in printers, network devices or servers are overlooked,
- disposal service provider does not provide usable evidence,
- reuse takes place without standard build or approval.

## Effectiveness review

Review questions:

- Can the whereabouts be traced for a sample of retired devices?
- Is there evidence that data treatment took place before onward transfer or disposal?
- Are equipment categories with hidden storage considered?
- Are missing devices, missing evidence and deletion errors escalated?
- Is reuse connected with secure reinstallation and approval?
- Are disposal provider or leasing records regularly assessed?

Possible metrics:

- open returns and overdue returns,
- devices with missing deletion/destruction evidence,
- duration from return to final whereabouts,
- deviations per equipment category,
- sample error rate,
- unclear old equipment in storage.

## BSIG/NIS2 connection point

Secure disposal and reuse are connectable to NIS2-oriented topics such as risk management, protection of information, cyber hygiene, supplier management and secure operating processes. The specific connection should be assessed through asset lifecycle, data classification, service provider management and requirements register.

This artefact does not replace legal, data protection or disposal-law assessment.

## Boundaries

- This artefact is not a technical deletion guide and not a product recommendation.
- It does not replace data protection, contractual, environmental or disposal review.
- It makes no binding statement on legal obligations or certifiability.
- Public examples contain no real equipment, personal or customer data.
- Deletion claims without evidence do not count as an effective routine.

## Handoffs

- **HR / leaver handoff:** return of equipment on departure, role change or longer absence.
- **IT / endpoint handoff:** remote wipe, reinstallation, encryption status, standard build.
- **Facility / storage handoff:** secured interim storage, pickup, handover and inventory reconciliation.
- **Procurement / supplier handoff:** lease return, disposal provider, service provider device, evidence quality.
- **Data protection / Legal handoff:** personal data, contractual issues, suspected data leakage or commissioned processing.
- **Incident handoff:** lost device, missing data carrier, unclear whereabouts or suspected disclosure.
- **Management handoff:** systematic return gaps, cost conflict, missing disposal capability.

## Typical mistakes

- Disposal is only considered at the end, not as part of the asset lifecycle.
- Only laptops are considered; printers, network devices or mobile data carriers are missing.
- Blanket disposal certificates are accepted although there is no asset connection.
- Reuse takes place after “reset” without reviewing the result.
- Old equipment is stored without protection because disposal costs or responsibility are unclear.
- Missing returns are administratively written off instead of reviewed as a risk.

## Fictional mini example

A fictional consulting company replaces twenty notebooks. The workplace team records each device by asset ID, checks encryption and management status and performs a documented reinstallation. Three devices cannot be reliably erased because of defects; the data carriers are removed and destroyed. The disposal provider confirms pickup of the remaining devices with an asset list. In a sample, one return from home office is missing; HR and IT trigger follow-up.

Evidence:

- asset list with departure status,
- reinstallation/wipe evidence,
- destruction evidence for data carriers,
- disposal provider handover record,
- sample note,
- follow-up ticket for missing return.
