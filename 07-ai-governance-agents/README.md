# 07 AI Governance Agents

This module describes how user organizations use krisensicherOS agents in a controlled way to support security governance, NIS2 readiness, ISMS, BCMS, evidence work, and management reviews.

Agents are not substitute accountable owners. They structure work, prepare decisions, review quality, and make handoffs visible.

## Contents

- `human-in-the-loop.md` (`human-in-the-loop.md`) — human approval points, decisions, and stop points.
- `agent-operating-rules.md` (`agent-operating-rules.md`) — operating rules for assignments, data, sources, handoffs, and reviews.
- `risk-and-limits.md` (`risk-and-limits.md`) — typical risks of agentic governance work and countermeasures.
- `../01-orientation/getting-started/eu-ai-act-readiness-start.md` (`../01-orientation/getting-started/eu-ai-act-readiness-start.md`) — start AI systems as an inventory, pre-check, and handoff routine.
- `./agents/public/role-model.md` (`./agents/public/role-model.md`) — public role model of the target repo agents.
- `./agents/manifest.yaml` (`./agents/manifest.yaml`) — manifest for agent families, handoffs, and adapters.

## Recommended starting point

1. Define objective and scope.
2. Select the minimum required agents from the role model.
3. Define human gates.
4. Select suitable skills, templates, or workflows.
5. Review output against quality gates.
6. Make and document decisions by humans.

## Operating logic

An agent run is only useful if it is clear:

- who commissioned it,
- which data and sources are allowed,
- what output should be produced,
- who reviews it,
- which decision is being prepared,
- where it must be stopped or escalated.
