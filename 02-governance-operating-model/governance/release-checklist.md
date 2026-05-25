<!-- kso:product-relevance
repo-scope: product
classification: product-governance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; product-safety; release-readiness
-->

# Release Checklist

## Purpose

This checklist prepares a public release candidate of krisensicherOS. It does not trigger publication.

Push, tagging, release, public activation, or external communication always require explicit human approval.

## Release Candidate Gates

### 1. Product Scope

- [ ] README explains purpose, target groups, AI prerequisite, and boundaries.
- [ ] krisensicherOS is clearly positioned as an AI-assisted governance repo.
- [ ] There is no full product path without AI usage.
- [ ] Approval preparation for AI usage is only a side note / template, not an alternative operating mode.
- [ ] Central folders are present and linked.
- [ ] Agents, skills, templates, playbooks, workflows, and evals are findable.

### 2. Public Safety

- [ ] No real personal, customer, or organizational data.
- [ ] No phone numbers, email addresses, credentials, or secrets.
- [ ] No private runtime, chat, workspace, or tool metadata.
- [ ] No internal work, review, persona, briefing, roadmap, queue, or release notes.
- [ ] Examples are clearly fictional.

### 3. Source and License Boundaries

- [ ] Public sources are used only as reference anchors or as proprietary summaries.
- [ ] No ISO or other licensed standard texts.
- [ ] No confidential contract content.
- [ ] Compliance register separates public, internal, confidential, and licensed content.

### 4. Claim Safety

- [ ] Does not provide legal advice.
- [ ] Does not provide data protection advice.
- [ ] Does not provide compliance, certification, or security assurance.
- [ ] No management decision by agents.
- [ ] Human gates are visible.

### 5. Artifact Gates

- [ ] Agent profiles meet the public profile standard and manifest alignment.
- [ ] Skills meet `07-ai-governance-agents/standards/skill-standard-v1.0.md`.
- [ ] Templates include purpose, trigger, users, input, process, output, evidence, boundaries, and review.
- [ ] Playbooks include situation, objective, roles, process, decisions, escalation, outputs, follow-up, and lessons learned.
- [ ] Workflows include trigger, agents, skills, templates, steps, stop/approval points, outputs, and quality gates.
- [ ] Examples meet public safety, claim safety, and fiction gate.

### 6. Technical QA

Minimum command in the working state:

```bash
GitHub Actions `quality-check` or local review of the relevant quality rules
```

Also check:

- working tree and staging status,
- local links,
- manifest vs. agent profiles,
- no private files in the export,
- no secret, PII, standard text, or runtime markers,
- no deleted internal files accidentally still present in the product state.

### 7. Publication Approval

- [ ] Target repo / target organization confirmed.
- [ ] Release name or tag confirmed.
- [ ] QA result reviewed.
- [ ] Diff reviewed.
- [ ] Publication approved separately.

## Hard Blockers

Release or publication is blocked by:

- missing publication approval,
- missing target repo or target account,
- legally unresolved license/disclaimer change,
- real or confidential data,
- secrets,
- licensed standard texts,
- overstated compliance or security claims,
- unresolved scope break,
- internal work artifacts in the product state.

## Definition of Done

A release candidate is prepared when:

- all gates have been checked,
- open blockers are documented,
- no unintended private or confidential content is included,
- QA results are traceable,
- publication can be approved separately.
