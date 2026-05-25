<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Codex CLI Adapter

This adapter describes how krisensicherOS should be used with Codex CLI.

## Basic idea

Codex CLI primarily reads clear repo instructions and works well with precise Markdown profiles, verifiable working rules, and concrete quality gates.

## Usage

- Public-safe repo instructions belong in `AGENTS.md`.
- Agent roles are canonical under `agents/public/*.md`.
- The role manifest is under `agents/manifest.yaml`.
- Skills are under `skills/<skill-name>/SKILL.md`.
- Workflows will be added later under `workflows/*.yaml`.

## Working rule

When Codex simulates or uses a krisensicherOS agent:

1. Read the appropriate profile in `agents/public/*.md`.
2. Mark input data and missing information.
3. Follow the profile's standard workflow.
4. Deliver the result in the defined output format.
5. Check quality gates.
6. Make boundaries/disclaimers visible.

## Do not do

- Do not claim legal advice.
- Do not derive a certification guarantee.
- Do not publish private OpenClaw workspace files.
- Do not treat workrepo artifacts as product content.
- Do not treat vault files as operational truth.
