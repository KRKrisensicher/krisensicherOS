<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Evals and Quality Gates

This folder contains review routines for krisensicherOS artifacts.

The goal is not formal bureaucracy, but reliable quality: every artifact should be public-safe, professionally bounded, operable, portable, and empowerment-oriented.

## Review Levels

1. **Public Safety**  
   No real personal, customer, organizational, secret, or private workspace data.

2. **Claim Safety**  
   No legal advice, data protection advice, certification, compliance, or security guarantees.

3. **Operating Logic**  
   Roles, triggers, inputs, flow, outputs, evidence, decisions, and reviews are clear.

4. **Empowerment**  
   The artifact strengthens internal capabilities and does not create unnecessary consulting or agent dependency.

5. **Portability**  
   Canonical artifacts remain tool- and adapter-neutral.

6. **Handoff Capability**  
   Responsibilities, human review points, and agent handoffs are traceable.

## Usage

Before completing an artifact:

1. identify the appropriate artifact type,
2. apply gates from `quality-gates.md`,
3. mark stop points,
4. make corrections,
5. complete the result with brief review evidence.

## Minimal Review Evidence

```text
Artifact:
Gates reviewed:
Findings:
Corrections:
Open human review:
Result: pass / pass with notes / stop
```

## Stop Means

A stop is not an error, but a safety mechanism. Stop when an artifact touches human decision, legal review, data protection review, license review, real data, or publication.
