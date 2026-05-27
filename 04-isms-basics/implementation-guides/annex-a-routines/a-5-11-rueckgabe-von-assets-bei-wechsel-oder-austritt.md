# A.5.11 — Return of assets during role change or exit

## Purpose

This routine ensures that organizational assets do not remain uncontrolled with individuals, teams, or service providers after role changes, exits, or contract end. This includes physical devices, access media, storage media, documents, software licenses, tokens, keys, mobile devices, and other means used to process or protect information.

The core is not the signature on a return checklist, but a reliable closure process: What was issued, what must be returned, who checks completeness, what risks arise if something is lost, and when are access revocation or compensating measures triggered?

## Control objective in repository language

The organization operates a traceable routine for returning, blocking, sanitizing, reusing, or securely disposing of assets during onboarding changes, role changes, exits, and external contract endings. The routine connects HR/people events, asset inventory, IT operations, facility, business units, supplier management, and evidence review.

## Typical risks

- If laptops, mobile devices, or storage media are not returned at exit, information can remain outside the organization's control.
- If access cards, keys, or tokens remain active, unauthorized physical or logical access may occur.
- If role changes are not treated as return events, special equipment, project documents, or elevated authorization media remain in the wrong area.
- If service provider devices or loan hardware are not tracked, accountability, cost control, and security decisions are missing.
- If returns rely only on manual reminders, absences, short-notice exits, or decentralized sites become blind spots.

## Triggers

- Exit, contract end, termination, retirement, or end of external work.
- Role change, team change, site change, or project end.
- Longer absence with increased risk or unclear asset status.
- Loss report, theft, damage, or suspected tampering.
- Offboarding of a service provider, supplier change, or end of a managed service.
- Asset inventory, audit finding, or discrepancy between HR, asset, and IT data.
- Management decision on cost, replacement procurement, or risk acceptance.

## Roles and responsibilities

- **HR / People function:** reports change and exit events in time and initiates offboarding.
- **Manager / Process Owner:** confirms which project- or role-related assets must be returned.
- **Asset Owner / IT Asset Management:** maintains inventory, assignment, return status, and reuse.
- **IT Operations / Workplace Team:** receives devices, blocks, deletes, checks, and prepares reuse or disposal.
- **Facility / Site responsible:** manages keys, access cards, locking media, and physical items.
- **Procurement / Supplier Management:** tracks external assets, loan devices, and contractual returns.
- **ISMS Owner / Security role:** defines minimum requirements, escalation, and evidence logic.
- **Management:** decides on missing assets, residual risks, costs, or returns that cannot be enforced.

## Implementation

### Minimum start

Goal: Do not lose critical assets during role change or exit.

1. The organization defines which asset types fall within the return process: devices, storage media, access media, documents, tokens, special hardware.
2. For new issuances, at least person, asset, date, and owner are documented.
3. HR or manager events trigger a return checklist.
4. Critical assets are checked before or no later than the exit date.
5. Missing assets are recorded as exceptions with risk, measure, and follow-up date.
6. IT and Facility confirm return, blocking, deletion, or loss handling.

Minimum evidence:

- asset list or issuance register,
- offboarding or change checklist,
- return confirmation,
- ticket for blocking/deletion,
- exception or loss decision.

### Solid practice

Goal: Return is operated as a repeatable offboarding and change routine.

1. Asset issuance and asset return are connected to joiner/mover/leaver processes.
2. Asset classes receive minimum actions: return, remote lock, data deletion, refurbishment, disposal, replacement claim.
3. Managers check project- and business-unit-specific items, not only central IT devices.
4. Service providers and external workers are managed in the same return status.
5. Open returns are escalated and not closed as completed offboarding.
6. Samples compare HR exits, asset register, access media, and IT tickets.

Strong evidence:

- current asset register with assignment,
- offboarding tickets with return status,
- confirmation of technical sanitization or deletion,
- facility evidence for access media,
- exception decisions with deadline,
- sampling protocol with corrections.

### Advanced practice

Goal: Asset return is integrated into identity, access, procurement, and risk steering.

1. HR system, asset management, IAM, MDM, and access control systems provide aligned offboarding tasks.
2. Mobile devices can be blocked, located, or wiped on a risk basis in case of loss or non-return, where permissible and clarified.
3. Highly critical assets receive specific return deadlines and evidence requirements.
4. Exceptions feed into risk, cost, and management reporting.
5. Recurring return problems lead to process improvements in issuance, inventory, or contract design.
6. Metrics show overdue returns, unassigned assets, loss rates, and processing times.

## Routine flow

1. **Event occurs:** role change, exit, contract end, project end, or loss report.
2. **Determine asset scope:** check central asset list, manager, project owner, facility, and service provider status.
3. **Plan return:** define deadline, location, responsible persons, and special cases.
4. **Perform return:** document physical receipt, shipping, collection, or secure handover.
5. **Handle technically:** block, back up or delete data, check devices, deactivate tokens, decide on reuse or disposal.
6. **Track status:** complete, open, lost, damaged, exception, or management decision.
7. **Escalate:** pass on missing critical assets, sensitive data, legal questions, or cost conflicts.
8. **Improve:** correct deviations in asset issuance, inventory, offboarding, or contracts.

## Decisions

- Which asset types must be returned and which only need to be documented?
- Which return deadline applies to critical devices, access media, or storage media?
- When is remote blocking or deletion performed, and what data protection/legal clarification is needed?
- Who decides on loss, damage, non-return, or cost reimbursement?
- When is offboarding completed despite a missing asset, and when does a risk remain open?
- Which external parties must be contractually required to return or destroy assets?

## Evidence

### Strong evidence

- asset register with person, owner, issuance and return status,
- offboarding ticket with confirmed subtasks,
- evidence of device receipt or shipping return,
- technical blocking, deletion, or refurbishment evidence,
- facility confirmation for access media,
- exception with risk decision, deadline, and follow-up date,
- management decision for critical non-return.

### Weak evidence

- generic exit checklist without specific assets,
- email saying “everything returned” without asset reference,
- outdated inventory list without assignment,
- verbal confirmation by the manager,
- device photo without return, deletion, or blocking status.

### Evidence gaps

- no reconciliation between HR exits and asset register,
- external persons without asset status,
- access media outside the offboarding process,
- loss without risk decision,
- device reuse without sanitization evidence.

## Effectiveness review

Review questions:

- Can all critical assets be assigned to an active or former person?
- Do role changes and project endings trigger return checks?
- Are missing assets handled and escalated on a risk basis?
- Is technical sanitization before reuse evidenced?
- Are external workers and service providers included?
- Does the routine lead to corrections in the asset register?

Possible metrics:

- overdue returns,
- open returns by criticality,
- unassigned assets,
- processing time from exit to closure,
- loss rate by asset class,
- share of offboardings with complete asset reconciliation.

## BSIG/NIS2 connection point

Asset return has a connection point to NIS2-oriented topics such as risk management, access protection, cyber hygiene, supply chain security, physical security, and maintaining controlled operating environments. The concrete relevance should be assessed in the requirements register and in organization-specific risk decisions.

This artifact does not replace legal review of employment, ownership, data protection, or contract-law questions.

## Boundaries

- No legal or data protection advice on surrender, cost reimbursement, locating, or remote deletion.
- No guarantee that a return list alone evidences security or conformity.
- No technical specifications for device forensics, data deletion, or disposal depth.
- No ISO 27002 text or certification commitment.
- No real personal, customer, or device data in public examples.

## Handoffs

- **HR handoff:** exit, role change, contract end, absence with return relevance.
- **IT/Workplace handoff:** device receipt, blocking, MDM action, data deletion, refurbishment.
- **Facility handoff:** keys, access cards, cabinets, locking media, site items.
- **Legal/Data Protection handoff:** remote deletion, locating, dispute, personal data, employment- or contract-law questions.
- **Supplier handoff:** external devices, loan hardware, subcontractors, return or destruction evidence.
- **Incident handoff:** suspected misuse, missing storage medium, compromised device.
- **Management handoff:** critical non-return, cost conflict, accepted residual risk.

## Typical mistakes

- Return is checked only at exit, not during role changes.
- Asset register and actual issuance do not match.
- Access media and tokens are forgotten because IT only looks at laptops.
- Offboarding is closed although critical assets remain open.
- External workers fall through the cracks.
- Devices are reissued without evidence of sanitization.
- Loss is recorded administratively but not assessed for risk.

## Fictional mini example

A fictional project manager moves to another department. The manager initiates a role-change check. The asset register shows a laptop, a test phone, an access card for a project room, and a hardware token. The test phone and project-room access are returned; the laptop remains assigned because of the new role. The hardware token cannot be found; IT blocks it, documents the loss, and the ISMS Owner includes the case in the next sample.

Evidence:

- role-change ticket,
- asset register with updated assignment,
- return confirmation for test phone and access card,
- blocking evidence for token,
- exception/loss note with review point.
