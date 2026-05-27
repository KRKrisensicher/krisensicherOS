# Using ISO standards with krisensicherOS in a license-compliant way

## Purpose

Many organizations want to connect krisensicherOS with ISO/IEC 27001 or other ISO standards. This is useful, but sensitive from a licensing perspective.

This guide describes how users can use ISO standards with krisensicherOS without impermissibly copying standard texts into the repo.

## Principle

ISO standards are generally protected by copyright and require a license.

krisensicherOS must therefore contain **no ISO standard texts, control texts, tables, annexes, or longer excerpts** in the public repo unless an explicit license exists for this.

## What is allowed

The following are typically permitted in the repo:

- references to standards as metadata,
- custom structure and mapping fields,
- custom summaries without reproducing protected wording,
- questions that support users when working with their licensed standard,
- templates for mapping and evidence,
- references to official sources,
- fictional examples without adopting standard text.

Example:

```yaml
source_id: iso-iec-27001-reference
source_type: standard-reference
source_location: internal licensed standards library
agent_usage: metadata_only
```

## What does not belong in the public repo

Do not include:

- copied ISO chapters,
- copied Annex A control texts,
- tables from standards,
- screenshots or scans from standard documents,
- purchased PDF files,
- standard excerpts taken from customer audits,
- paraphrased passages that effectively replace the standard text,
- standard texts in prompts, agent contexts, RAG systems, embeddings, vector databases, training data, or other AI systems without an explicit suitable license.

## Recommended approach for users

1. **Obtain the standard in a license-compliant way**
   - Via ISO, DIN, Beuth/DIN Media, or another permitted source.

2. **Do not copy the standard into the public repo**
   - Not even into `09-implementation-roadmaps/examples/`, `fixtures/`, prompts, or training data.

3. **Document the private storage location**
   - Reference only the storage location in your own non-public compliance register.

4. **Use your own mapping structure**
   - Requirements are mapped internally to controls, evidence, roles, and routines.

5. **Provide agents only with permitted context**
   - Use metadata, custom summaries, and organization-specific mappings.
   - Do not copy complete standard texts into agent prompts if the license does not explicitly allow this.
   - Do not load standard documents into RAG, embeddings, vector databases, training data, assistants, copilots, or local AI systems unless an explicit AI, text mining, multi-user, or platform license exists.

6. **Ensure human review**
   - Agents may prepare mappings, but must not confirm them as binding.

## Recommended repo structure for users

```text
02-governance-operating-model/compliance-register/
├── sources.yaml
├── mappings/
│   ├── iso27001-to-controls.yaml
│   ├── iso27001-to-evidence.yaml
│   └── iso27001-to-routines.yaml
└── private-sources/          # normally gitignored
    └── README.md             # no standard texts in the public repo
```

## Example of a license-compliant register entry

```yaml
id: iso-iec-27001-reference
title: ISO/IEC 27001
type: standard-reference
source_location: Internal licensed standards library
license_or_confidentiality: License required; do not copy standard texts into the repo
agent_usage_allowed: metadata_only
human_owner: information security officer/CISO
mapping_status: in_progress
```

## Agent rule

For ISO references, agents should always check:

- Is standard text being reproduced or effectively replaced here?
- Is the content only metadata, a custom summary, or mapping?
- Does the source require a license?
- Is AI, RAG, embedding, prompt, or text mining use explicitly licensed?
- Does a human need to approve the interpretation?

If there is doubt, the agent must stop and require human review.

## Provider and license note

Low-cost sources, single-seat, multi-user, intranet, subscription, or standards portal models can be useful. However, purchasing a standard does not automatically mean that the content may be transferred into a Git repo, an internal agent system, or an AI pipeline.

Each organization must clarify the following before use:

1. Who may read the document?
2. May it be stored internally on servers, the intranet, or a document management system?
3. May content be entered into prompts, RAG, embeddings, or other AI systems?
4. Are derived mappings without standard text allowed?
5. Does use apply only to the organization itself or also to consulting/customer contexts?

## No legal advice

This guide does not provide legal advice. Organizations must review their specific license situation, contract terms, and usage rights themselves or have them reviewed legally.
