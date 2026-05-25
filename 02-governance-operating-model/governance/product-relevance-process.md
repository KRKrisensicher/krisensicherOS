<!-- kso:product-relevance
repo-scope: product
classification: product-governance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; reusable-governance-asset; human-gate-aware
-->

# Product Relevance Process

## Basic rule

The default is **workrepo**.

A file may remain in the product repo only if it is explicitly marked as product-relevant and meets the criteria below. When creating or changing a file, this classification must be checked again.

Workrepo files are not deleted just because they are not product-relevant. They are marked with `repo-scope: workrepo` and transferred to a dedicated workrepo on `git.kr.int`. Later, the product repo contains only `repo-scope: product` artifacts.

## Required tag

Every file in the working state must carry a `kso:product-relevance` tag in the file content.

- `repo-scope: product` means: may be included in the product repo export.
- `repo-scope: workrepo` means: remains in the workrepo, must not be included in the product repo export.

Minimum fields:

```text
kso:product-relevance
repo-scope: product | workrepo
classification: <artifact class>
decision: keep | move-to-workrepo | remove
review-required-on-change: true
criteria: <met criteria>
```

For Markdown, an HTML comment is used. For YAML, Shell and Gitignore, comment lines are used. For files without a comment format, the tag may be placed at the end as a plain-text metadata block.

## Decision criteria for `repo-scope: product`

A file is product-relevant only if it meets at least these criteria:

1. **Public-safe**
   - no internal workspace, runtime, chat, token, personal, customer or organizational data,
   - no private work notes or review traces.

2. **Product benefit**
   - directly helps user organizations with AI-assisted security governance,
   - or is necessary to keep the product repo usable, reviewable, secure or portable.

3. **AI-assisted governance fit**
   - supports agents, skills, templates, workflows, playbooks, governance routines, human gates or setup of approved AI usage,
   - is not a manual alternative path without AI product relevance.

4. **Reusability**
   - is generic enough for public use,
   - uses fictional examples,
   - contains no real customer specifics.

5. **Claim safety**
   - does not provide legal advice,
   - does not provide data protection advice,
   - does not provide compliance, certification or security assurance,
   - no management decision by agents.

6. **License and source clarity**
   - no licensed standard texts,
   - no confidential contract content,
   - public sources only as reference anchors or own summaries.

7. **Human gates**
   - human review, approval, risk acceptance and external communication remain visible with responsible roles.

## Typical decisions

### `repo-scope: product`

Examples:

- README, setup and getting-started documents,
- public agent profiles,
- skills,
- templates,
- workflows,
- playbooks,
- quality and governance rules,
- fictional examples,
- QA scripts that protect the product state.

### `repo-scope: workrepo`

Examples:

- internal brainstorms,
- personal notes,
- agent session memory,
- interim review and QA reports,
- roadmaps not intended for users,
- mirror/release technology,
- local test and repair scripts,
- files with private workspace details.

These files must not be included in the product repo export. They remain until repo separation and are transferred to the dedicated workrepo on `git.kr.int`.

## Required check when creating or changing files

Before completing any change:

1. Does every new or changed file have a `kso:product-relevance` tag?
2. Is `repo-scope: product` genuinely justified, or does the file belong in the workrepo?
3. Would a product file be understandable to users even without internal project context?
4. Does a product file contain no private, confidential, personal or licensed content?
5. Does a product file support AI-assisted governance and human gates?
6. Are `repo-scope: workrepo` files excluded from the product repo export?
7. Does the GitHub Actions quality gate run without tag or link errors?

## Escalation

If a file is not clearly product-relevant, it remains in the workrepo. Inclusion in the product occurs only after explicit justification and review.

## Target state for repo separation

- Product repo on `git.kr.int`: only product-relevant artifacts with `repo-scope: product`.
- Workrepo on `git.kr.int`: internal working states, reviews, roadmaps, release technology and provenance with `repo-scope: workrepo`.
- GitHub publication occurs exclusively from the reviewed product repo state, not from the workrepo.

Suggested workrepo name: `krisensicher/krisensicher-os-workrepo`.

Clarify before creating the workrepo:

1. Target namespace on `git.kr.int`.
2. Repo name.
3. Visibility and permissions.
4. Whether history is fully transferred or initially started as a new workrepo snapshot.
5. Which remotes are set locally.
