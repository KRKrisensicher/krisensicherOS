<!-- kso:product-relevance
repo-scope: product
classification: tool-adapter
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Orgavision MCP Adapter

This adapter describes how krisensicherOS artifacts can be used with the Orgavision MCP interface as an organizational distribution and knowledge-access path.

## Positioning

krisensicherOS does not create finished governance for a specific organization. It helps prepare roles, routines, evidence, reviews, and decisions. After professional review, this can become approved organizational information: process descriptions, role clarifications, decision logic, evidence routines, management review templates, or training content.

Orgavision can serve as an operational knowledge and distribution channel for this. The publicly described MCP interface connects QM/organizational knowledge stored in Orgavision with AI tools that support the Model Context Protocol. According to Orgavision, connected AI systems can access approved content, respect read permissions, and return relevant text excerpts with source references.

Source: <https://www.orgavision.com/loesungen/zusatzmodule/mcp-schnittstelle>

## Usage model

1. krisensicherOS supports creating or revising a governance artifact.
2. Professionally accountable people review content, data class, audience, owner, review cycle, and human gates.
3. Only approved content is published in Orgavision or a comparable management-system/QM knowledge system.
4. Orgavision makes this content available through roles, read permissions, handbook structures, and optionally MCP-supported AI queries.
5. Employees can find and use approved information in their work context instead of searching for documents in isolated repositories.

## Suitable content

Suitable content includes:

- approved role and responsibility descriptions,
- process and routine descriptions,
- management review and evidence routines,
- approved FAQ and training content,
- decision logic and escalation paths,
- references to public regulatory sources and internal register entries.

Not suitable:

- unreviewed AI drafts,
- real personal, customer, contract, incident, or secret content without appropriate approval,
- licensed standard texts or near-equivalent substitutes,
- legal, data protection, certification, or compliance assurances,
- content without an owner, review cycle, or target audience.

## Human gates before publication

Before publication in Orgavision or availability through MCP, check:

1. **Owner:** Who is professionally accountable?
2. **Audience:** Who may see and use the information?
3. **Data class:** Which content may enter Orgavision and connected AI queries?
4. **Approval:** Who approves content, language, and distribution?
5. **Review cycle:** When is the content reviewed?
6. **Boundaries:** Is it clear that the information does not replace legal advice, data protection advice, or compliance assurance?
7. **Read permissions:** Are Orgavision roles and permissions set appropriately?

## Starter prompt

```text
Use krisensicherOS to prepare an approved Orgavision/MCP-ready artifact.

Context:
- Topic: <NIS2 / ISMS / evidence review / incident readiness / management review>
- Target audience in the organization: <role/team>
- Planned storage location or handbook area in Orgavision: <area>
- Data class: <public / internal / confidential after approval>

Work in three steps:
1. First ask clarification questions about owner, target audience, read permissions, human gates, and review cycle.
2. Then create a public-safe or approval-ready draft with clear operating logic.
3. Mark all points that require human review before publication in Orgavision.

No legal advice, no data protection advice, no compliance or certification assurance. Do not include real personal, customer, contract, incident, secret, or licensed standard content.
```

## Adapter boundary

This adapter documents an integration and operating approach. It does not replace Orgavision configuration, permission review, data protection assessment, or professional approval. The concrete MCP setup must be performed in the respective Orgavision and AI environment by authorized administrators.
