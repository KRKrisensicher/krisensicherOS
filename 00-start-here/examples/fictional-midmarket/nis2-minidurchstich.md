# NIS2 mini walkthrough: fictional mid-sized organization

## Fictional nature

This example is entirely fictional. It contains no real organization, customer, person, contract, incident, system, network, or contact data.

## Goal

This mini example shows how a skeptical CISO/information security officer starts with five artifacts:

1. management mandate,
2. compliance register entry,
3. NIS2 gap,
4. audit question and evidence request,
5. management decision point.

It does not confirm regulatory fulfillment, compliance, certification capability, or security.

## Initial situation

The fictional organization operates a digital customer service. The CISO/information security officer wants to check whether the backup/restore routine for the core service is sufficiently operable and reviewable.

## 1. Management mandate

**Artifact:** `templates/decision-log.md`

| Field | Example content |
| --- | --- |
| Decision question | Which three NIS2-relevant routines do we check in the first 30-day walkthrough? |
| Proposal for initial scope | Backup/restore routine for digital core service |
| Management need | Confirm priority, owner, review cadence, and resources for evidence preparation |
| Human Gate | Executive management / responsible management role decides |

## 2. Compliance register entry

**Artifact:** `templates/compliance-source-register.md`

| Field | Example content |
| --- | --- |
| Source / reference | NIS2-relevant internal working reference to business continuity / incident readiness |
| Own summary | Critical services need robust routines, evidence, and decision paths for outages and restart. |
| Affected area | Digital core service, backup, restore, operations team |
| Owner question | Who is responsible for restore tests and review of evidence? |
| Boundaries | No legal interpretation; internal working summary only. |

## 3. NIS2 gap

**Artifact:** `templates/nis2-gap-worksheet.md`

| Field | Example content |
| --- | --- |
| Target state | Restore routine is described, tested, evidenced, and reviewable. |
| Current state | Backup is running; restore test evidence is scattered and available without management review. |
| Gap type | Evidence and review gap |
| Impact | Management cannot properly assess resilience and residual risk. |
| Next step | Evidence Request to service owner and responsible operations role. |

## 4. Audit question and Evidence Request

**Artifacts:** `templates/audit-questionnaire.md`, `templates/evidence-request-list.md`

### Audit question

| Field | Example content |
| --- | --- |
| Criterion / reference | Internal register entry backup/restore readiness |
| Guiding question | When was the last restore test for the digital core service performed and how was the result assessed? |
| Review method | Document review and short owner interview |
| Expected evidence | Restore test note, error/action log, review note |
| Human Gate | Assessment and prioritization by CISO/information security officer and management |

### Evidence Request

| ID | Required evidence | Purpose | Why needed for the decision? | Reuse | Effort | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ER-001 | latest restore test note | Evidence that the test was performed | Management can only define the review cadence if the test practice is known. | yes/open | low | Service Owner | open |
| ER-002 | action log from restore test | Identify open technical or organizational items | Prioritization depends on whether open items are critical or routine work. | yes/open | low | Operations team | open |
| ER-003 | existing review or approval note | Check management/owner review | Decision on escalation threshold needs existing review practice. | open | medium | CISO/ISB | open |

Workload rule: In the first walkthrough, no more than three requests. Do not request new documents as long as existing evidence is sufficient.

## 5. Management decision point

**Artifact:** `templates/decision-log.md`

| Field | Example content |
| --- | --- |
| Decision point | Should restore readiness for the core service appear monthly or quarterly in the management review? |
| Options | A: monthly operational review, B: quarterly management review, C: only after changes / incidents |
| Evidence status | Restore test note and action log requested; review note open |
| Open decision | Define review cadence, owner, and escalation threshold |
| Human Gate | Management decides; AI or agent only prepares. |

## 6. Derive action from gap

**Artifact:** `templates/corrective-action-plan.md`

| Field | Example content |
| --- | --- |
| Trigger | Evidence Request shows: restore test exists, but review and action tracking are missing. |
| Corrective action | In the future, document restore test note with result, open items, owner, and review note. |
| Cause / hypothesis | Routine was performed technically, but not operated as a process capable of management-grade evidence. |
| Owner | Service owner with support from CISO/information security officer |
| Due date | before next quarterly management review |
| Evidence | updated test note, action log, review note |
| Human Gate | Owner confirms feasibility; management decides review cadence and escalation threshold. |

## 7. Check effectiveness later

**Artifact:** `templates/remediation-effectiveness-review.md`

| Field | Example content |
| --- | --- |
| Review timing | after next restore test or no later than after the agreed review cadence |
| Effectiveness question | Does the new routine show whether restore test, open items, and management review are traceably connected? |
| Minimum evidence | Test note, action status, review note, decision on open items |
| Assessment | open; no effectiveness claim before evidence review |
| Handoff | Escalate to management review if evidence is repeatedly missing. |

## 8. Example: legal/data protection handoff

**Artifact:** `templates/legal-datenschutz-handoff.md`

The team uses this handoff only when legal, data protection, or confidential content is affected in the real project. In the fictional example, nobody assesses these questions; the handoff only prepares the transfer to data protection/legal.

| Field | Example content |
| --- | --- |
| Reason / trigger | Restore test note could contain real user, customer, or system references. |
| Specific question | May excerpts from the restore test note be used for AI-assisted summary or evidence pack preparation? |
| Data class | unclear; provisionally treat as internal/confidential |
| Planned processing / use | Summary for evidence pack and management review |
| AI use affected? | yes / unclear |
| Protective measures already applied | no real content in public examples; check redaction before AI use |
| Required decision / assessment | Data protection/legal clarify permitted processing and necessary minimization |
| Human Gate | Data protection/legal decides; CISO/information security officer uses the result only as working approval. |

Boundary: The handoff is not a data protection assessment. It prevents security governance work from silently making legal or data protection decisions.

## What deliberately remains open

- legal assessment of NIS2 applicability,
- data protection questions regarding real operational data,
- risk acceptance,
- final assessment of effectiveness,
- external communication or audit statement.

## Next step

When evidence is available:

1. fill in `templates/evidence-pack-index.md`,
2. use `templates/audit-finding-report.md` in case of deviations,
3. transfer actions into `templates/corrective-action-plan.md`,
4. check effectiveness later with `templates/remediation-effectiveness-review.md`,
5. track decision, review cadence, and open residual risks in the management review.
