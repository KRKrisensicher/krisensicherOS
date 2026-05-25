<!-- kso:product-relevance
repo-scope: product
classification: implementation-guide-module
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->

# 08 — Incidents, Deviations, and Improvement

## Purpose

This module connects security events, deviations, findings, and lessons learned with ISMS improvement.

## Reference framework

- ISO/IEC 27001:2022 — Sections 8, 9.1, and 10.
- BSIG § 32: <https://www.gesetze-im-internet.de/bsig_2025/__32.html>
- BSIG § 30 in case of possible applicability.

## Users and roles

- Incident owner,
- ISMS owner,
- information security officer/CISO,
- service owner,
- legal/data protection,
- management,
- corrective action owner.

## Triggers

- security event,
- confirmed incident,
- near miss,
- internal deviation,
- audit/review finding,
- notification assessment,
- lessons learned.

## Process

1. Capture the signal and separate facts from assumptions.
2. Classify the incident or deviation type.
3. Have the notification path checked: BSIG, GDPR, contract, customer, sector rule.
4. Define immediate measures and owners.
5. Review root-cause and impact perspectives after stabilization.
6. Add the improvement measure to the backlog.
7. Set a review date for effectiveness.

## Decisions

| Decision | Options | Human Gate |
| --- | --- | --- |
| Escalation needed? | yes / no / unclear | Incident owner |
| Notification assessment needed? | yes / no / unclear | Legal/data protection |
| Activate crisis team? | yes / no / prepare | Management |
| Improvement measure | immediate / planned / rejected | ISMS owner / management |

## Evidence

- incident or deviation note,
- timeline,
- notification path assessment note,
- action list,
- decision log,
- lessons-learned record,
- effectiveness review.

## Review

Check whether concrete improvements result from events: measure, owner, deadline, evidence, review.

## BSIG/NIS2 reference

§ 32 BSIG is an important reference anchor for notification assessments in case of possible applicability. This module does not determine any notification obligation; it prepares the assessment.

## Boundaries

No live crisis management, no determination of a notification obligation, no external communication without approval.

## Handoffs

- to incident escalation playbook,
- to legal/data protection,
- to management/crisis team,
- to corrective action planning.
