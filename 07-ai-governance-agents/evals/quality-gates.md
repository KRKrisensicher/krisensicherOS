# krisensicherOS Quality Gates v1.0

Status: 2026-05-23

These gates apply to public repo artifacts: agent profiles, skills, templates, playbooks, workflows, examples, adapters, source registers, and documentation.

## 1. Universal Gates

### U1 — Public-Safe Gate

Check questions:

- Does the artifact contain real personal, customer, or organizational data?
- Does it contain private workspace, chat, runtime, or internal agent details?
- Does it contain secrets, tokens, credentials, or technical internals?
- Does it contain confidential contract content or licensed standard texts?

Pass criterion:

- Only fictional examples, public sources, metadata, own summaries, or empty user fields.

Stop criterion:

- Any real or confidential information that has not been explicitly approved for publication.

### U2 — Claim-Safety Gate

Check questions:

- Does the artifact claim legal advice, data protection advice, or binding interpretation?
- Does it claim NIS2 compliance, ISO certification capability, or a security guarantee?
- Does it sound as if an agent could take over human responsibility?

Pass criterion:

- Boundaries are visible; human review and decision remain explicit.

Stop criterion:

- Any compliance, certification, legal, or security guarantee.

### U3 — Operating Logic Gate

Check questions:

- Who uses the artifact?
- When is it triggered?
- What inputs does it need?
- What steps does it perform?
- What output is created?
- What evidence is created?
- Who reviews it and at what cadence?

Pass criterion:

- The artifact can be used in a real governance routine.

Stop criterion:

- Pure document template without role, trigger, decision, evidence, or review.

### U4 — Empowerment Gate

Check questions:

- Does the artifact help users build their own capabilities?
- Does it explain decisions, boundaries, and check points?
- Does it avoid consulting dependency or agent magic?

Pass criterion:

- Users can understand, adapt, and critically review the artifact.

Stop criterion:

- Black-box output without learning, review, or adaptation options.

### U5 — Workload Gate

Check questions:

- Does the artifact reduce work or increase decision readiness?
- Does it create unnecessary meetings, lists, or reviews?
- Are owner and benefit clear?

Pass criterion:

- Effort is justified and operationally useful.

Stop criterion:

- Bureaucracy without risk reduction, evidence value, or decision relevance.

### U6 — Portability Gate

Check questions:

- Is the canonical artifact tool-neutral?
- Are Claude, Codex, OpenClaw, Hermes, or other adapters only derivatives?
- Does the artifact avoid private paths, local accounts, or runtime details?

Pass criterion:

- Domain logic lives in the canonical artifact; adapters stay thin.

Stop criterion:

- Domain logic only in a tool adapter or with non-portable assumptions.

## 2. Artifact-Specific Gates

### A1 — Agent Profile Gate

Additionally check:

- YAML frontmatter complete,
- mandate clearly distinguishable,
- `When to use` and `When not to use` present,
- inputs/outputs concrete,
- success metrics verifiable,
- boundaries and red lines present,
- handoff protocol executable,
- human-in-the-loop visible,
- manifest entry present.

### A2 — Skill Gate

Additionally check:

- `SKILL.md` present,
- purpose and scope clear,
- inputs, process, outputs, and verification defined,
- human approvals named,
- example without real data,
- no replacement for legal, data protection, or management decision.

### A3 — Template Gate

Additionally check:

- trigger, users, input, process, output, evidence, and boundaries present,
- fields are operationally useful,
- no empty form graveyards,
- clear notes for adaptation and review.

### A4 — Playbook Gate

Additionally check:

- scenario and objective clear,
- roles and escalations defined,
- decision and communication points included,
- after-action/lessons-learned step present,
- no live-incident overreach.

### A5 — Workflow Gate

Additionally check:

- workflow connects agents, skills, templates, registers, and approvals,
- stop/escalation points included,
- inputs/outputs clear for each step,
- human decisions not automated,
- handoff protocol executable.

### A6 — Example Gate

Additionally check:

- example is fully fictional,
- no realistic customer names, phone numbers, domains, or individual data,
- assumptions are marked as assumptions,
- example shows good use, not perfect false assurance.

### A7 — Adapter Gate

Additionally check:

- adapter references the canonical source,
- no divergent domain logic,
- no private paths or local workspace assumptions,
- tool-specific notes are minimal and purely technical.

### A8 — Source/Register Gate

Additionally check:

- public sources are documented as reference anchors,
- licensed standards only as metadata/references/mappings,
- confidential requirements only as redacted summary or private user content,
- owner, status, review frequency, and permitted agent use are marked.

## 3. Result Levels

- **pass** — Artifact meets gates.
- **pass with notes** — Artifact is usable, but open human review or improvement is documented.
- **stop** — Artifact must not be published or used before the marked point is clarified.

## 4. Review Evidence Template

```text
Artifact:
Artifact type:
Reviewed gates:
Pass:
Pass with notes:
Stop points:
Corrections:
Human review required:
Result:
```

## 5. Hard Stop Points

Always stop for:

- real personal, customer, or organizational data,
- secrets or credentials,
- confidential contract content,
- licensed standard texts,
- legal or data protection advice,
- compliance, certification, or security guarantees,
- external publication without approval,
- license or disclaimer change without approval.
