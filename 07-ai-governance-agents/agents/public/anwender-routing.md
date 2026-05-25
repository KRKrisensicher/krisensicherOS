<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# User Routing: maximum 8 start agents

## Purpose

This selection helps you get started. Do not use all agents at the same time. Choose the agent that prepares the next concrete work step. Agents do not replace legal review, data protection review, compliance assessment, certification decision, or management responsibility.

## For skeptical or highly regulated teams

Use the same paths first via templates, playbooks, and guides. Start at [`../../01-orientation/getting-started/anwenderpfade.md`](../../../01-orientation/getting-started/anwenderpfade.md) and open only the artifacts from “Required in 15 minutes”. Agents accelerate structuring and review, but do not replace internal responsibility.

For EU AI Act readiness, do not start with a new specialized agent. Start with `compliance-operating-system-lead` for sequence and handoffs; data protection, legal, and management questions remain human gates.

| Start agent | When to use | Input | Output | Handoff |
| --- | --- | --- | --- | --- |
| `compliance-operating-system-lead` | When sequence, scope, or overall path is unclear | Objective, data class, AI usage approval, desired result | Work plan, suitable artifacts, stop points | to specialist agents; final review to `agent-quality-and-safety-reviewer` |
| `nis2-scope-precheck-analyst` | When NIS2 applicability should only be preliminarily checked | public/approved organizational assumptions, questionnaire | Preliminary check working assumption, open legal questions | mandatory to legal/legal review; if continuing, to `nis2-readiness-analyst` |
| `nis2-readiness-analyst` | When NIS2 gaps and evidence requests are being built | Register entry, scope, management question | Gap worksheet, evidence needs, owner questions | to `control-evidence-architect` or `management-review-facilitator` |
| `isms-operating-model-designer` | When a minimum viable ISMS is being started | Scope, risks, role assumptions, approval limits | ISMS start model with routines, reviews, and evidence | to `risk-and-obligation-prioritizer` or `security-governance-architect` |
| `security-governance-architect` | When roles, triggers, routines, or escalations are missing | Target routine, existing way of working, owner assumptions | Operating logic with role, process, evidence, and review | to `control-evidence-architect` for evidence |
| `risk-and-obligation-prioritizer` | When too many risks, gaps, or requirements are open | Risk/gap list, impact, effort, deadlines | Prioritized work list and decision needs | to `management-review-facilitator` for management decision |
| `control-evidence-architect` | When controls/routines need to be translated into evidence | Routine, control assumption, existing evidence | Control-evidence map, evidence requests | to `evidence-pack-reviewer` |
| `incident-readiness-coach` | When escalation, notification triage, or tabletop exercises should be practiced | Scenario, roles, escalation path, approval limits | Escalation card, triage draft, exercise questions | to legal/data protection/notification owners and `management-review-facilitator` |

## Quality rule

If a result sounds too certain, touches confidential content, or could have external impact: stop, mark the human gate, and use `agent-quality-and-safety-reviewer` for claim safety and boundaries.
