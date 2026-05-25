<!-- kso:product-relevance
repo-scope: product
classification: product-governance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; product-safety; release-readiness
-->

# Contributing to krisensicherOS

Thank you for your interest in krisensicherOS.

This repo is intended to enable organizations to build security governance, NIS2 readiness, ISMS, BCMS, and crisis readiness in a way they can operate themselves.

## Principles

Contributions should:

- make concrete governance work easier,
- make roles, routines, evidence, and decisions clearer,
- enable user organizations instead of making them dependent,
- remain public-safe and portable,
- not create legal or certification promises.

## Good contributions

Suitable examples include:

- agent profiles with clear responsibility and boundaries,
- skills with inputs, process, outputs, and verification,
- templates with operating logic,
- workflows with handoffs and approval points,
- evals and quality gates,
- fictional examples,
- documentation that enables users to build their own setup.

## Not suitable

Do not submit:

- real customer data or personal data,
- confidential contract content,
- ISO or other licensed standard texts,
- unreviewed legal interpretations,
- statements such as “compliant,” “legally certain,” “ready for certification,” or similar guarantees,
- generic policy texts without roles, triggers, evidence, and review,
- tool-specific domain logic in canonical profiles.

## Artifact checklist

Before contributing, please check:

- What problem does the artifact solve?
- Who uses it?
- When is it triggered?
- What inputs does it need?
- What process is created?
- What output is created?
- What evidence is created?
- What boundaries and human review points exist?
- Which agents, skills, or templates are affected?

## Structure

- Agent profiles: `agents/`
- Public target-repo agents: `agents/public/`
- Skills: `skills/`
- Templates: `templates/`
- Playbooks: `playbooks/`
- Workflows: `workflows/`
- Quality gates: `evals/`
- Standards: `docs/standards/`

## Review expectation

Every contribution should be reviewed at least for public safety, claim safety, operating logic, portability, and empowerment.
