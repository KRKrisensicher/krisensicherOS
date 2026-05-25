<!-- kso:product-relevance
repo-scope: product
classification: public-example
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# ISMS 90-Minute Walkthrough: fictional mid-sized organization

## Purpose

This example shows, in a compact form, how a Minimum Viable ISMS can be started as an operating routine. It is entirely fictional and contains no real organizational, customer, personal, contract, incident, or system data.

Does not provide legal advice, data protection advice, compliance assessment, certification assurance, or security guarantee.

## Fictional Scope

**Organization:** fictional mid-sized service provider.

**Start scope:** digital customer service, internal operations team, change process, backup/restore routine, and one central SaaS provider.

**Not in start scope:** full corporate group, all sites, all suppliers, full audit or certification readiness.

**Template references:**

- [`../../templates/isms-scope-canvas.md`](../../../04-isms-basics/templates/isms-scope-canvas.md)
- [`../../templates/rollenmatrix.md`](../../../02-governance-operating-model/templates/rollenmatrix.md)
- [`../../templates/risikoregister-starter.md`](../../../04-isms-basics/templates/risikoregister-starter.md)
- [`../../templates/soa-risk-control-map.md`](../../../04-isms-basics/templates/soa-risk-control-map.md)

## 3 Risks

| Risk | Working hypothesis | Human Gate |
| --- | --- | --- |
| Restore capability cannot be demonstrated in a robust way | Restore tests exist informally, but are not bundled in a reviewable form | Management confirms review cadence and accepts/changes residual risk |
| Changes to the core service are not consistently traceable | Change decisions are distributed across tickets and chat histories | Service owner defines the binding evidence source |
| SaaS dependency is operationally critical, but not clearly steered | Outage and escalation paths are not clearly documented | Procurement/service owner/legal review contract and escalation questions |

## 3 Measure Routines

| Routine | Trigger | Proposed owner | Evidence |
| --- | --- | --- | --- |
| Monthly restore evidence | Monthly review or major change | Operations team lead | Test note, result, deviation, measure |
| Change review for core service | Release or emergency change | Service owner | Ticket link, approval, rollback assumption, post-test |
| Supplier escalation check | Quarterly review or service disruption | Vendor owner | Contact/escalation card, open points, decision need |

**Template references:**

- [`../../templates/control-evidence-map.md`](../../../06-evidence-management-review/templates/control-evidence-map.md)
- [`../../templates/corrective-action-plan.md`](../../../06-evidence-management-review/templates/corrective-action-plan.md)
- [`../../playbooks/monthly-security-governance-review.md`](../../../06-evidence-management-review/playbooks/monthly-security-governance-review.md)

## 1 Management Decision

**Decision point:** Will the start scope for the next 90 days be limited to restore capability, change traceability, and SaaS escalation?

**Options:**

- A: Limit scope and review monthly.
- B: Expand scope, but plan for more owner and evidence effort.
- C: Postpone start until roles and AI usage approval are clarified.

**Human Gate:** Management decides priority, resources, and the accepted residual risk framework. AI only prepares the template.

**Template:** [`../../templates/decision-log.md`](../../../02-governance-operating-model/templates/decision-log.md)

## 1 Evidence Pack

**Evidence Pack:** `ISMS-Start-Kernservice-Q1`.

Note: Do not include real ticket, chat, customer, personal, contract, incident, or system data in this public example. In real organizations, such evidence belongs only in approved internal repositories.

| Content | Purpose | Source |
| --- | --- | --- |
| Scope Canvas | Delineation of the start scope | `isms-scope-canvas.md` |
| Risk register extract | three start risks and owner questions | `risikoregister-starter.md` |
| Control Evidence Map | Connect routines with evidence | `control-evidence-map.md` |
| Decision Log | Document management decision | `decision-log.md` |
| Corrective Actions | Convert deviations into measures | `corrective-action-plan.md` |

**Template:** [`../../templates/evidence-pack-index.md`](../../../06-evidence-management-review/templates/evidence-pack-index.md)

## 1 Review Date

**Date:** first monthly security governance review, fictionally at the end of next month.

**Agenda:**

1. Scope remains suitable or must be adjusted.
2. Review three risks: status, owner, evidence, decision point.
3. Confirm or simplify measure routines.
4. Check Evidence Pack for gaps.
5. Prepare management decision for the next 30 days.

**Templates and playbooks:**

- [`../../templates/management-review-agenda.md`](../../../06-evidence-management-review/templates/management-review-agenda.md)
- [`../../playbooks/management-review-prep.md`](../../../06-evidence-management-review/playbooks/management-review-prep.md)
- [`../../04-isms-basics/implementation-guides/isms/09-monitoring-management-review-und-entscheidungen.md`](../../../04-isms-basics/implementation-guides/isms/09-monitoring-management-review-und-entscheidungen.md)

## Definition of Done after 90 Minutes

The walkthrough is complete when scope, three risks, three routines, one decision log entry, one evidence pack index, and one review date are available as a draft and all human gates are marked.
