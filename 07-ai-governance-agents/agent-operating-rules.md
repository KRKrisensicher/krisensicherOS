<!-- kso:product-relevance
repo-scope: product
classification: product-module
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Agent Operating Rules

## Purpose

These rules describe how organizations operate the krisensicherOS agents in a controlled way: tool-neutral, public-safe, with clear roles, handoffs, and quality gates.

## 1. Select agents

Start small. For an initial krisensicherOS operation, a few role profiles are usually sufficient:

1. `compliance-operating-system-lead`
2. `regulatory-source-mapper`
3. `compliance-register-curator`
4. `security-governance-architect`
5. `risk-and-obligation-prioritizer`
6. `control-evidence-architect`
7. `evidence-pack-reviewer`
8. `management-review-facilitator`
9. `agent-quality-and-safety-reviewer`

Expand only when the need is clear:

- NIS2: `nis2-readiness-analyst`
- ISMS: `isms-operating-model-designer`
- BCMS: `bcms-readiness-designer`
- Incident/Tabletop: `incident-readiness-coach`
- Policies/Controls: `policy-and-controls-drafter`
- Data protection interfaces: `data-protection-interface-reviewer`
- Third parties/customers/suppliers: `third-party-requirements-analyst`

## 2. Formulate the work assignment

Each agent assignment contains:

- objective
- scope and non-scope
- permitted sources and data
- expected output
- relevant templates, skills, or workflows
- human owner
- stop points
- desired quality gate

## 3. Data and source rule

Agents may use:

- public sources as reference anchors,
- their own summaries,
- metadata from registers,
- fictional examples,
- redacted internal information in private user environments.

Agents must not include the following in public artifacts:

- real customer data,
- personal data,
- confidential contractual content,
- licensed standard texts,
- secrets or access credentials,
- private runtime or workspace details.

## 4. Handoff rule

A handoff is needed when:

- another specialist role is responsible,
- a result must be reviewed,
- a decision is being prepared,
- boundaries or claims become critical,
- evidence or sources are unclear.

Handoff format:

```text
Initial situation:
Scope:
Output so far:
Open question:
Risk / boundary:
Required next agent or human role:
Desired output:
```

## 5. Review rule

Each relevant output is checked against suitable gates:

- Public Safety,
- Claim Safety,
- operating logic,
- empowerment,
- workload,
- portability,
- artifact-specific gate from `evals/quality-gates.md`.

## 6. Working mode in tools

The specialist logic remains canonical in:

- `agents/public/`,
- `skills/`,
- `templates/`,
- `playbooks/`,
- `workflows/`,
- `evals/`.

Tool adapters for Claude, Codex, OpenClaw, Hermes, or other systems should only implement this specialist logic, not change it.

## 7. Escalation rule

Agents first resolve internal specialist questions through handoffs and quality review. Humans are involved only when a real stop point has been reached:

- legal/data protection assessment,
- contract interpretation,
- risk acceptance,
- management decision,
- external communication,
- publication,
- license or confidentiality question.

## Definition of Done

Agent work is operated cleanly when:

- assignment and scope are clear,
- permitted sources and data are defined,
- a suitable agent, skill, template, or workflow has been selected,
- human gates are visible,
- quality gates have been passed or stop points are marked,
- result and handoff are documented in a traceable way.
