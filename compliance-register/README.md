<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Compliance Register

This folder is the template for an organization-specific compliance register.

## Purpose

krisensicherOS contains hard-wired public reference sources under [`../knowledge/`](../knowledge/). In addition, organizations need space for their own requirements:

- licensed standards, e.g., ISO/IEC 27001,
- customer contracts,
- supplier requirements,
- internal policies,
- sector-specific requirements,
- audit findings,
- insurance requirements,
- regulatory conditions,
- corporate group requirements.

This register provides a structure for this, but no real organizational data.

## Important Rule

No real compliance requirements of an organization belong in the public krisensicherOS repo.

Users should copy this structure into their own private working repo and populate it there.

## What may be placed here in the public repo?

Allowed:

- empty templates,
- fictional examples,
- metadata schemas,
- mapping fields,
- guidance for agent work.

Not allowed:

- real contracts,
- real customer requirements,
- real audit reports,
- ISO standard texts,
- confidential control catalogs,
- personal data,
- access credentials or internal URLs.

## Recommended Register Structure for Users

```text
compliance-register/
├── README.md
├── sources.yaml
├── mappings/
│   ├── requirements-to-controls.yaml
│   ├── requirements-to-evidence.yaml
│   └── requirements-to-routines.yaml
├── notes/
│   └── README.md
└── private-sources/
    └── README.md
```

`private-sources/` usually belongs in `.gitignore` in user environments if confidential or licensed content is stored there.

## Register Fields

Each source should contain at least:

- `id`
- `title`
- `type`
- `owner`
- `source_location`
- `license_or_confidentiality`
- `applicability`
- `obligations_summary`
- `mapping_status`
- `review_frequency`
- `human_owner`
- `agent_usage_allowed`
- `notes`

## Agent Rule

Agents may derive working structures from register entries:

- question lists,
- mapping suggestions,
- control references,
- evidence needs,
- review routines,
- decision templates.

Agents must not:

- publish confidential content,
- reproduce licensed standard texts,
- claim binding legal or contractual interpretation,
- replace human approvals.

## Files

- [`sources.example.yaml`](sources.example.yaml) — fictional example for register entries.
- [`../templates/compliance-source-register.md`](../templates/compliance-source-register.md) — Markdown template for individual sources.
