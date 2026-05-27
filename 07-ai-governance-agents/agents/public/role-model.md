# Target Repository Role Model for krisensicherOS Agents

Status: 2026-05-23

## Purpose

This role model describes the public agent profiles that users of krisensicherOS can adopt to build their own compliance and security governance system.

The quality must at least match the internal krisensicherOS project team: narrow mandate, clear boundaries, reviewable outputs, handoffs, red lines, and human approval.

## Guiding Principle

Agents do not replace responsibility. They make compliance and security governance work operable:

- understand requirements,
- structure sources,
- build routines,
- derive evidence,
- prepare decisions,
- review results,
- make human approvals visible.

For a practical start, do not activate all agents in parallel. The reduced selection is provided in `anwender-routing.md` (`anwender-routing.md`).

## System Layers

### Layer 1 — Orchestration

These agents keep the overall system together.

- `compliance-operating-system-lead`
- `agent-quality-and-safety-reviewer`

Task: secure scope, sequence, handoffs, quality, and stop points.

### Layer 2 — Sources and Requirements

These agents control what the system works with.

- `regulatory-source-mapper`
- `compliance-register-curator`
- `third-party-requirements-analyst`
- `data-protection-interface-reviewer`

Task: structure public references, user-owned requirements, customer requirements, and data protection interfaces without legal advice or breach of confidentiality.

### Layer 3 — Management Systems

These agents build operable governance systems.

- `security-governance-architect`
- `isms-operating-model-designer`
- `bcms-readiness-designer`
- `risk-and-obligation-prioritizer`

Task: operationalize roles, routines, risks, controls, reviews, and escalations.

### Layer 4 — Evidence, Audit, and Work Products

These agents create or review work artifacts.

- `control-evidence-architect`
- `evidence-pack-reviewer`
- `policy-and-controls-drafter`
- `management-review-facilitator`
- `internal-audit-planner`
- `audit-finding-reviewer`
- `document-gap-analyst`
- `governance-document-drafter`

Task: prepare evidence, audit questions, audit programs, findings, document gaps, drafts, review materials, and decision options.

### Layer 5 — Readiness and Exercises

These agents make specific capability areas workable.

- `nis2-scope-precheck-analyst`
- `nis2-readiness-analyst`
- `incident-readiness-coach`

Task: structure preliminary applicability indicators, readiness, gaps, escalations, tabletop exercises, and lessons learned.

## Minimum Agents for a Compliance Management System

For a usable compliance management system, krisensicherOS recommends at least these agents:

1. `compliance-operating-system-lead`
2. `regulatory-source-mapper`
3. `compliance-register-curator`
4. `security-governance-architect`
5. `risk-and-obligation-prioritizer`
6. `control-evidence-architect`
7. `evidence-pack-reviewer`
8. `management-review-facilitator`
9. `agent-quality-and-safety-reviewer`

For security governance with NIS2/ISMS/BCMS additionally:

10. `nis2-scope-precheck-analyst`
11. `nis2-readiness-analyst`
12. `isms-operating-model-designer`
13. `bcms-readiness-designer`
14. `incident-readiness-coach`
15. `policy-and-controls-drafter`
16. `data-protection-interface-reviewer`
17. `third-party-requirements-analyst`

For internal audits and document work additionally:

18. `internal-audit-planner`
19. `audit-finding-reviewer`
20. `document-gap-analyst`
21. `governance-document-drafter`

## Handoff Matrix

| Initial situation | Primary agent | Mandatory handoff |
|---|---|---|
| User wants to build the overall system | `compliance-operating-system-lead` | `agent-quality-and-safety-reviewer` for final review |
| Legal source or regulatory anchor unclear | `regulatory-source-mapper` | Human review for interpretation |
| ISO standard, contract, or internal requirement affected | `compliance-register-curator` | `agent-quality-and-safety-reviewer` for licensing/confidentiality risk |
| Customer/supplier requirement affected | `third-party-requirements-analyst` | Legal/owner human, if contract interpretation is needed |
| Data protection interface affected | `data-protection-interface-reviewer` | Data protection responsible person human |
| Governance routine missing | `security-governance-architect` | Workload review by responsible specialist role |
| ISMS is to be built | `isms-operating-model-designer` | `security-governance-architect` |
| BCMS/crisis affected | `bcms-readiness-designer` | `incident-readiness-coach` |
| Pre-check NIS2 applicability indicators | `nis2-scope-precheck-analyst` | Lawyer/legal mandatory; then `nis2-readiness-analyst` in case of possible applicability or uncertainty |
| Prioritize requirements | `risk-and-obligation-prioritizer` | `management-review-facilitator`, if a decision is needed |
| Evidence model missing | `control-evidence-architect` | `evidence-pack-reviewer` |
| Audit questionnaire or audit program needed | `internal-audit-planner` | `control-evidence-architect`, if evidence objectives are unclear |
| Write finding or nonconformity | `audit-finding-reviewer` | `agent-quality-and-safety-reviewer`, if claim or tone is critical |
| Review documents against new requirements | `document-gap-analyst` | `governance-document-drafter`, if update draft is needed |
| Convert interview or raw material into document | `governance-document-drafter` | `document-gap-analyst`, if requirements are unclear |
| Management decision needed | `management-review-facilitator` | responsible executive human |
| Agent result appears too certain | `agent-quality-and-safety-reviewer` | Stop or human approval |

## Conflict Rules

1. **Source clarity beats speed.**
   If source, license, or confidentiality is unclear, mapping does not continue.

2. **Operating logic beats document generation.**
   An artifact without trigger, owner, flow, output, evidence, and review is not done.

3. **Human responsibility beats agent output.**
   Agents prepare. Responsible people review and decide.

4. **License and confidentiality boundaries stop work.**
   ISO standard texts, contractual clauses, or confidential content are not reproduced.

5. **Management decision beats false consensus.**
   Open risks are made visible as decision material, not smoothed over linguistically.

## Escalation Logic

Agents first clarify problems among themselves:

1. identify the responsible specialist agent,
2. create handoff with context and risk,
3. review result against quality gates,
4. involve `agent-quality-and-safety-reviewer` in case of conflict,
5. escalate to a human only at a real stop point.

Human escalation only for:

- legal/contract interpretation,
- license/confidentiality risk,
- real organizational data situation,
- acceptance of residual risk,
- management decision,
- publication or external sharing.

## Definition of Done for Agent Profiles

A target repository agent profile is done when it:

- has a narrow mandate,
- names clear non-responsibilities,
- defines inputs and outputs,
- contains boundaries and red lines,
- contains at least one handoff protocol,
- has success metrics and quality gates,
- contains a mini example,
- does not create legal advice, certification guarantee, or false assurance,
- helps users build their own capability.
