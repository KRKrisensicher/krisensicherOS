# A.5.18 — Review of access rights

## Purpose

Access rights change faster than responsibilities are documented: new tasks, project roles, substitutions, service provider access, and technical groups create rights that are often not removed later. This routine ensures that existing access is regularly reviewed by the business, corrected, withdrawn, or consciously decided as an exception.

The review is not a list exercise. It is a governance moment: owners confirm whether access is still needed, whether it fits the protection need, and whether notable rights trigger a risk or management decision.

## Control objective in repository language

The organization operates a risk-based review routine for user, admin, external, and technical access. Reviews have clear scope, understandable decision criteria, responsible owners, documented results, and follow-up through to implementation.

## Typical risks

- If rights remain after role changes, excessive or incompatible permissions arise.
- If former service providers, project members, or external accounts are not reviewed, unnoticed access paths remain open.
- If owners approve incomprehensible group lists, a pseudo-review without business decision emerges.
- If admin rights are treated like normal access, especially powerful rights remain active for too long.
- If technical accounts and API access are missing, the review is limited to people only.
- If review results are not implemented, the risk remains unchanged despite the record.

## Triggers

- Planned monthly, quarterly, semi-annual, or annual permission review.
- Hiring, role change, team change, departure, project end, or service provider end.
- New system, new data repository, new privileged role, or changed role model.
- Security event, compromised account, unusual use, or audit finding.
- Change in protection need, business process, data class, or regulatory affectedness.
- Migration, cleanup, system replacement, or introduction of an IAM/recertification tool.
- Management question about critical legacy permissions, external access, or segregation conflicts.

## Roles and responsibilities

- **Information owner / Asset owner:** decides whether access is still needed from a business perspective.
- **Process owner / Manager:** confirms role reference, business need, and organizational changes.
- **IT/platform owner:** creates permission exports, explains group logic, and implements withdrawal or correction.
- **IAM/access owner:** defines review procedure, frequencies, criticality classes, and recertification logic.
- **ISMS owner / Security role:** checks risk reference, exception handling, and escalation.
- **HR / Procurement:** provides role change, departure, project-end, and service-provider information.
- **Data protection / Legal:** assesses personal-data analysis, employee reference, and contractual questions.
- **Management:** decides on accepted residual risks, resource conflicts, and non-resolvable segregation conflicts.

## Implementation

### Minimum start

Goal: critical and privileged access is reviewed visibly on a regular basis.

1. The organization names the most important systems, data repositories, admin roles, and external access in scope.
2. Each review object has a business owner and a technical contact.
3. IT provides understandable permission extracts: person or account, role/group, purpose, last known reference.
4. Owners decide for each notable access: confirm, withdraw, change, clarify, or exempt for a limited time.
5. Withdrawal and correction are tracked as tickets.
6. Open or disputed items receive deadline, escalation path, and follow-up.

Minimum evidence:

- review scope with systems and owners,
- permission export at review time,
- review record with decisions,
- tickets for withdrawal or adjustment,
- exceptions with justification and expiry date.

### Solid practice

Goal: access reviews are risk-based, understandable, and repeatable.

1. Access types are considered separately: standard access, privileged access, external access, technical accounts, function accounts.
2. Review frequencies are based on protection need, exposure, and permission power.
3. Review lists are prepared understandably for owners: descriptive roles, system purpose, criticality, last change, external marker.
4. HR, project, and supplier events are reconciled with the review.
5. Recertification results lead to measurable actions: withdrawal, role cleanup, exception, risk decision, or process improvement.
6. Recurring notable cases are fed back into role model, joiner/mover/leaver process, or training.
7. Critical overdue reviews go into ISMS or management review.

Strong evidence:

- risk-based review plan,
- current owner matrix,
- understandably prepared review lists,
- decisions per access or access group,
- implementation evidence for withdrawal and correction,
- exception and escalation log.

### Advanced practice

Goal: reviews are integrated with identity data, risk indicators, and management steering.

1. IAM, HR source, system groups, service accounts, and ticketing are connected.
2. High-risk access is recertified more frequently or event-based.
3. Segregation-of-duties conflicts, unusual combinations, orphaned accounts, and old external access are marked automatically.
4. Reviews create structured tasks and evidence in the ticket or GRC system.
5. Metrics show overdue reviews, withdrawal duration, exception rate, non-assignable accounts, and recurring role problems.
6. Management receives not only list status, but decision-ready residual risks and resource needs.

## Routine flow

1. **Trigger review:** schedule, event, incident, audit finding, or management question.
2. **Define scope:** determine systems, data repositories, roles, external accounts, admin rights, and technical accounts.
3. **Prepare data:** export permissions, assign owners, translate unclear groups, and mark notable cases.
4. **Review by business:** owners assess business need, role reference, protection need, and segregation conflicts.
5. **Decide:** confirm, withdraw, reduce, time-limit, escalate, or clarify further.
6. **Implement technically:** IT/IAM changes rights and documents implementation.
7. **Follow up:** manage open items, exceptions, and overdue decisions with deadlines.
8. **Check effectiveness:** sample, re-export, or validate whether agreed changes were implemented.
9. **Improve:** adjust role model, onboarding/offboarding, supplier process, or system groups.

## Decisions

- Which systems, roles, and access types are reviewed first?
- How often are standard, admin, external, and technical access reviewed?
- Which criteria make access notable or critical?
- Who may confirm access and who may accept exceptions?
- When is missing owner feedback escalated?
- Which segregation conflicts are not acceptable and which need management decision?
- How is it ensured that review results are actually implemented?

## Evidence

### Strong evidence

- review plan with risk-based frequency,
- system/asset scope with owners,
- permission export or recertification dataset at review time,
- business decisions with date and responsible role,
- withdrawal, change, or cleanup tickets,
- validation after implementation,
- time-limited exceptions with risk decision,
- management decision for permanent conflicts.

### Weak evidence

- signed list without recognizable individual decision,
- screenshot of groups without owner, date, or scope,
- review email without follow-up of changes,
- blanket confirmation “everything ok” by IT instead of business owner review,
- IAM tool status without evidence that open findings were handled.

### Evidence gaps

- no owners for critical systems or data repositories,
- admin rights, service accounts, or external accounts outside the review,
- review results without implementation tickets,
- permanently open clarification cases without escalation,
- role changes and departures not reconciled with review data,
- exceptions without deadline or risk acceptance.

## Effectiveness review

Review questions:

- Are the most critical access rights reviewed more often and more deeply than standard rights?
- Can owners understand and decide the review lists from a business perspective?
- Do reviews lead to actual withdrawal, reduction, or role cleanup?
- Are external, privileged, and technical access visibly included?
- Are overdue reviews and open clarification cases escalated?
- Is there validation that agreed changes were implemented?
- Are recurring notable cases fed back into the access process?

Possible metrics:

- share of critical systems with current review,
- overdue reviews by criticality,
- number of withdrawn or reduced access rights,
- open clarification cases older than defined deadline,
- withdrawal duration after review decision,
- exception rate and overdue exceptions,
- non-assignable accounts.

## BSIG/NIS2 connection point

Reviews of access rights are compatible with NIS2-oriented risk management measures, cyber hygiene, access protection, governance, incident prevention, and traceability of security-relevant decisions.

For BSIG/NIS2 affectedness, the organization should assess in the requirements register which systems, roles, review frequencies, and evidence are relevant. This artifact does not replace legal interpretation or a binding assessment of applicability.

## Boundaries

- This artifact does not replace a complete identity and access management concept.
- It is not a data protection assessment for employee analysis or log data.
- A review record does not replace technical implementation of agreed changes.
- No legal advice, no data protection advice, no certification commitment.
- No ISO 27002 text and no real personal, customer, or system data in examples.

## Handoffs

- **IAM/IT handoff:** permission exports, group logic, withdrawal, role model, and technical validation.
- **HR handoff:** hiring, departure, role change, organizational changes, and longer absences.
- **Procurement/supplier handoff:** external accounts, project end, contract end, or changed service provider scope.
- **Data protection/legal handoff:** personal-data analysis, employee reference, log data, or contractual questions.
- **Incident handoff:** suspicious rights, compromised accounts, or unauthorized use.
- **Management handoff:** permanent exceptions, segregation conflicts, resource shortages, or accepted residual risks.
- **Audit/evidence handoff:** missing review evidence, unclear decisions, or non-validated implementation.

## Typical mistakes

- Review lists are so technical that business units cannot assess them meaningfully.
- Owners blanket-confirm all rights because of time pressure.
- Admin, external, and technical accounts are not reviewed separately.
- Decisions are documented, but withdrawal or change is not followed up.
- Reviews take place annually even though critical access needs more frequent review.
- Exceptions receive no expiry date.
- The IAM tool is understood as the control even though owner decisions are missing.

## Fictional mini example

A fictional manufacturing company introduces a quarterly review of ERP admin rights. The IT owner provides a list with admin and support roles. The business owner identifies two former project roles that are no longer needed. IT withdraws the rights and confirms this by re-export. One external support access remains active for a limited time because an update window is pending; the exception receives an expiry date and follow-up in the next review.

Evidence:

- ERP review scope with owner,
- permission export at the reference date,
- business owner decisions,
- withdrawal ticket and re-export,
- time-limited exception for external support access.
