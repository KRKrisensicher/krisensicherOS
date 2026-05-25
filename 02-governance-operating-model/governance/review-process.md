<!-- kso:product-relevance
repo-scope: product
classification: product-governance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; product-safety; release-readiness
-->

# Review Process

## Purpose

The review process helps check whether krisensicherOS artifacts remain public-safe, operable, tool-neutral, and decision-oriented.

## Review Principles

1. Operating logic before document: Every artifact needs an owner, trigger, output, evidence, and review.
2. Human-in-the-loop: Legal assessment, data protection assessment, risk acceptance, management decision, and external communication remain with the responsible humans.
3. Public-safe by default: Public artifacts do not contain real customer, personal, contract, incident, system, or private workspace data.
4. Source clarity: Licensed standards and confidential content are maintained only as metadata, references, or own summaries.
5. Portability: Domain logic lives in canonical artifacts, not in tool adapters.

## Review Levels

### R1 — Self-check by Creator

Check before handoff:

- Purpose and scope clear?
- User role and trigger named?
- Inputs, process, outputs, and evidence visible?
- Boundaries and stop points included?
- No impermissible claims?
- No real or confidential data?

### R2 — Subject-matter Review

Suitable review by subject-matter role or agent profile:

- Agent profiles: `agent-quality-and-safety-reviewer`
- Governance/ISMS/NIS2: `security-governance-architect` or `nis2-readiness-analyst`
- BCMS/Incident: `bcms-readiness-designer` or `incident-readiness-coach`
- Evidence: `control-evidence-architect` or `evidence-pack-reviewer`
- Management decisions: `management-review-facilitator`

### R3 — Quality Gate Review

Check against `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md`:

- U1 Public-Safe Gate
- U2 Claim-Safety Gate
- U3 Operating Logic Gate
- U4 Empowerment Gate
- U5 Workload Gate
- U6 Portability Gate
- suitable artifact-specific gate

### R4 — Release Review

Before release candidate, additionally check:

- README and navigation consistent?
- Queue without open publication-relevant ready tasks?
- Blockers documented?
- License present?
- no private runtime/workspace content?
- no secrets or personal data?
- no standard texts or confidential content?
- no publication without approval?

## Review Evidence

```text
Artifact:
Reviewer:
Date:
Checked gates:
Pass:
Pass with notes:
Stop points:
Corrections:
Human review required:
Result:
```

## Stop Points

Review stops in case of:

- legal advice or data protection advice,
- management decision by agents,
- risk acceptance without a responsible role,
- compliance, certification, or security assurance,
- real or confidential data,
- licensed standard texts,
- external publication without approval,
- license/disclaimer change without approval.

## Definition of Done

An artifact is reviewable when:

- all relevant quality gates have been passed or notes are documented,
- stop points are either excluded or marked as blockers,
- human review points are visible,
- handoffs are clear,
- changes can be committed coherently.
