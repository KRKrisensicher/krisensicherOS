<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Knowledge Sources

This folder describes the hardwired reference layer of krisensicherOS.

## Purpose

Agents should not freely assume “any compliance sources”, but work with clearly named source categories:

1. **Hardwired Sources** — public legal sources and primary regulatory sources that krisensicherOS recognizes as fixed reference anchors.
2. **Compliance Register** — organization-specific requirements that users add themselves, e.g., standards, customer contracts, internal policies, or sector-specific requirements.

## Basic Rule

krisensicherOS does not store copyrighted standard texts, confidential contract content, or personal data.

The repo may contain:

- source metadata,
- official reference locations,
- reference structures,
- mapping fields,
- evaluation and prompt logic,
- fictional examples.

The repo must not contain:

- ISO standard texts,
- paid standard excerpts,
- confidential customer contracts,
- real organization-specific compliance requirements,
- legal advice or binding interpretation.

## Files

- [`hardwired-sources.yaml`](hardwired-sources.yaml) — fixed public reference anchors.
- [`../compliance-register/README.md`](../compliance-register/README.md) — guidance for user-owned compliance registers.
- [`../docs/legal/iso-normen-lizenzkonform-nutzen.md`](../docs/legal/iso-normen-lizenzkonform-nutzen.md) — notes on using ISO standards in a license-compliant way.
