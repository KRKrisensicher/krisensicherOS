# Agent profiles

This folder contains the public agent profiles for krisensicherOS.

## Purpose

The agent profiles describe roles for AI-assisted security governance. They are not substitute accountable parties, but working roles for structuring, analysis, evidence flow, review, and handoff.

## Public user agents v1.0

The public user agents are located under `07-ai-governance-agents/agents/public/` (`public/`). They form a role model for organizations that want to build their own compliance and security governance agent system with krisensicherOS.

Orchestration:

- `compliance-operating-system-lead`
- `agent-quality-and-safety-reviewer`

Sources and registers:

- `regulatory-source-mapper`
- `compliance-register-curator`
- `third-party-requirements-analyst`
- `data-protection-interface-reviewer`

Management systems and governance:

- `security-governance-architect`
- `isms-operating-model-designer`
- `bcms-readiness-designer`
- `risk-and-obligation-prioritizer`

Evidence and reviews:

- `control-evidence-architect`
- `evidence-pack-reviewer`
- `policy-and-controls-drafter`
- `management-review-facilitator`

Readiness and exercises:

- `nis2-readiness-analyst`
- `incident-readiness-coach`

For getting started with a small number of roles, see `07-ai-governance-agents/agents/public/anwender-routing.md` (`public/anwender-routing.md`). The complete role model is in `07-ai-governance-agents/agents/public/role-model.md` (`public/role-model.md`), and the routing manifest is in `07-ai-governance-agents/agents/manifest.yaml` (`manifest.yaml`).

## Quality rule for all agents

Each agent must make visible:

- which decision or routine is supported,
- which input data is missing or uncertain,
- which assumptions were made,
- which human role must review or approve,
- which evidence or work artifact is created.

Agents relieve workload, structure, and review. They do not replace accountability.
