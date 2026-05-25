<!-- kso:product-relevance
repo-scope: product
classification: tool-adapter
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Microsoft 365 Copilot Adapter

## Purpose

This adapter describes how krisensicherOS can be used in Microsoft 365 Copilot, SharePoint Agents, and Copilot Studio.

It is not a replacement for tenant governance, permission review, sensitivity labels, DLP, or human review.

## Research basis

As of: 2026-05-25.

Reviewed public Microsoft documentation:

- Microsoft Support: Microsoft 365 Copilot in SharePoint Help & Learning.
- Microsoft Support: Get started with agents in SharePoint.
- Microsoft Learn: Knowledge sources summary — Microsoft Copilot Studio.

Relevant points:

- SharePoint Agents can answer questions about site, page, and file content for which the user has permissions.
- There are ready-made agents per SharePoint site and custom-built agents with customized scope, identity, and behavior.
- Interaction requires a Microsoft 365 Copilot license or a shared pay-as-you-go service for SharePoint Agents.
- Editing a SharePoint Agent also requires appropriate editing permissions on the site.
- Custom agents can use knowledge sources, sites, pages, files, and customized prompts.
- Copilot Studio knowledge sources can use enterprise data, websites, and external systems for generative answers.

## Adapter principle

Microsoft 365 Copilot operates close to permissions and the tenant. Therefore:

- upload krisensicherOS artifacts only to reviewed SharePoint/Teams structures,
- do not bring unreviewed evidence packs, customer data, personal data, contract details, or standard texts into Copilot scope,
- clean up permissions before prompting,
- always transfer Copilot outputs back into decision logs, review notes, or templates,
- decisions remain with accountable humans.

## Recommended M365 structure

```text
krisensicherOS/
├── 01 Orientation
├── 02 Approved Product Artifacts
├── 03 Compliance Register
├── 04 Audit and Evidence
├── 05 Management Review
├── 06 Review and Approval
└── 99 Archive
```

Only `02 Approved Product Artifacts` is used as the knowledge base for an initial Copilot/SharePoint Agent pilot.

## Preconditions

Clarify before use:

- Microsoft 365 Copilot license or approved SharePoint Agent service,
- tenant approval by responsible admin/owner roles,
- site owner and business owner,
- reviewed SharePoint/Teams permissions,
- no broad groups such as “Everyone except external users” on sensitive libraries,
- sensitivity labels and DLP/retention/audit rules,
- data class per artifact group,
- human gates for output review.

## Suitable product artifacts for the pilot

Suitable:

- `README.md`,
- `01-orientation/getting-started/*`,
- `01-orientation/setup/README.md`,
- `07-ai-governance-agents/agents/public/role-model.md`,
- selected `templates/*.md`,
- selected `playbooks/*.md`,
- `02-governance-operating-model/governance/disclaimer.md`,
- `02-governance-operating-model/governance/quality-rules.md`.

Not suitable for the first Copilot pilot:

- real evidence packs,
- confidential customer data,
- personal data,
- contract details,
- secrets,
- licensed standard texts,
- workrepo artifacts with `repo-scope: workrepo`.

## SharePoint Agent setup

1. Create an approved SharePoint site or library.
2. Limit permissions to the pilot group.
3. Document sensitivity label and DLP/audit rules.
4. Upload only approved krisensicherOS product artifacts.
5. Use a ready-made agent only if the site scope is clean.
6. For a production pilot, preferably create a custom agent with limited knowledge sources.
7. Adopt agent purpose and prompts from `sharepoint-agent-instructions.md`.
8. Ask test questions only with fictional or approved content.
9. Transfer answers back into `templates/decision-log.md`, `templates/evidence-request-list.md`, or a review note.

## Copilot Studio setup

If Copilot Studio is used:

- limit knowledge sources to approved SharePoint libraries or reviewed websites,
- use generative answers only with a clear purpose description,
- secure authentication and access through Microsoft/tenant rules,
- do not use confidential sources as a global knowledge source without business approval,
- document test cases with fictional examples.

## Standard prompt for M365 Copilot

```text
You are supporting me with krisensicherOS.
Use only the approved files in this SharePoint library.
Do not provide legal advice, data protection advice, compliance assurance, certification assurance, or security assurance.
Do not make a management decision and do not accept risk.
Mark assumptions, gaps, evidence needs, and human gates.
If content could be personal, confidential, customer-specific, contractual, licensed, or credential-like: stop and request approval.

Task:
<specific task>

Output:
1. Brief finding.
2. Required evidence.
3. Open decisions.
4. Human gates.
5. Suitable krisensicherOS template.
```

## Human gates

| Point in time | Gate |
| --- | --- |
| Before upload | Data class, owner, sensitivity label, and permitted AI environment reviewed |
| Before agent creation | Knowledge sources and permissions reviewed |
| Before use with internal data | DLP, audit logging, retention, and access reviewed |
| Before sharing | Output reviewed by the relevant business owner |
| Before decision | Management or responsible role decides |
| Before external communication | Explicit approval documented |

## Adapter quality gate

Before completing an M365 Copilot work step, check:

- Were only `repo-scope: product` artifacts used?
- Are SharePoint/Teams permissions limited?
- Have sensitivity labels and DLP/audit rules been clarified?
- Have no workrepo, customer, personal, contract, incident, system, or secret data been introduced?
- Have no licensed standard texts been processed?
- Are assumptions, gaps, evidence needs, and human gates marked?
- Was output transferred into a krisensicherOS template or review artifact?
