# 07 — Suppliers and Dependencies

## Purpose

This module makes suppliers, service providers, platforms, and other dependencies manageable as part of the ISMS.

## Reference Framework

- ISO/IEC 27001:2022 — sections 4.3, 6.1, 8.1, 9, and Annex A as reference anchors.
- BSIG § 30 and § 32 where applicability is possible.
- EnWG § 5c to § 5e where energy is relevant.

## Users and Roles

- Service owner,
- procurement / vendor management,
- ISMS owner,
- risk owner,
- legal,
- data protection,
- incident owner.

## Triggers

- new supplier,
- critical service provider,
- outsourcing or cloud/MSP/MSSP use,
- contract change,
- supplier incident,
- missing evidence.

## Process

1. Maintain supplier and dependency register.
2. Determine criticality: service, data class, outage impact, replaceability.
3. Formulate security and evidence requirements as separate working questions.
4. Hand over contractual, data protection, and notification obligations to legal/data protection.
5. Define evidence and review date.
6. Check exit, emergency, or replacement logic if critical.

## Decisions

| Decision | Options | Human Gate |
| --- | --- | --- |
| Criticality | critical / relevant / low / unclear | Service owner |
| Evidence sufficient? | yes / partially / no | Evidence owner |
| Accept contract gap? | no / time-limited / management decision | Legal + management |
| Escalation for supplier incident | internal / customer / authority review | Incident owner + legal |

## Evidence

- supplier register,
- criticality assessment,
- evidence and contract references,
- risk decision,
- review minutes,
- incident or escalation notes.

## Review

At least upon contract renewal, scope change, new service, incident, evidence gap, or annual supplier review.

## BSIG/NIS2 Reference

Organizations close to NIS2/BSIG must steer supply chain risks particularly cleanly. This module prepares risk, evidence, and notification hygiene without interpreting obligations in a binding way.

## Boundaries

No contract review, no data protection review, no assessment of a supplier as “secure.”

## Handoffs

- to procurement/vendor management,
- to legal/data protection,
- to incident triage,
- to management for critical dependencies.
