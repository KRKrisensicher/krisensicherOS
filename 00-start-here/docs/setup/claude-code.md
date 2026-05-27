# Setup: Claude Code for krisensicherOS

Status: 2026-05-23

## Purpose

This setup is for repo-adjacent work: documentation, templates, skills, playbooks, workflows, checks, and structured changes in the Git repo.

The guide is written **Windows-first**. macOS/Linux are possible, but they are not the primary entry point.

## Variants

| Variant | Suitable for |
| --- | --- |
| Claude Code App | Users who prefer a guided app experience for repo work |
| Claude Code in VS Code | Users who want to plan, change, and diff directly in the editor |
| Claude Code CLI | More technical users, automation, terminal workflows |

## Prerequisites

- Windows 10/11,
- Git for Windows,
- VS Code recommended,
- local krisensicherOS checkout,
- approved Anthropic/Claude access or approved provider,
- clarified data class and AI usage approval.

## Read-only first run and app security check

For AI-critical organizations, Claude Code always starts in read-only mode.

Before the first prompt, check:

- Is only the approved repo folder open?
- Was `C:\Users\<Name>`, the user profile, a root drive, all of OneDrive, or a confidential SharePoint sync folder not opened accidentally?
- Does the folder contain no real customer, personal, contract, incident, system, or secret data?
- Are additional folders, connectors, or integrations disabled or approved?
- Is it clear whether the app may change files or should initially only read?

Read-only first prompt:

```text
Work read-only for now.
Do not perform file changes, shell commands with write effects, Git actions, or external publications.
Read README.md, AGENTS.md, CLAUDE.md, 01-orientation/setup/README.md, and 06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md.
Read only the explicitly named files in the opened repo folder.
After that, explain the safe work plan and the stop points to me.
```

## Variant 1: Claude Code App on Windows

1. Install Claude Code App according to the vendor instructions.
2. Sign in with the approved organizational account.
3. Open the local working folder, for example:

   ```text
   C:\Users\<Name>\Documents\krisensicherOS
   ```

4. Ensure that the app accesses only the intended project folder.
5. Open the start files in the app or project context:
   - `README.md`
   - `AGENTS.md`
   - `CLAUDE.md`
   - `01-orientation/setup/README.md`
   - `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md`

6. Use the read-only first prompt from the section above. Do not start with change tasks.

## Variant 2: Claude Code in VS Code on Windows

1. Install Git for Windows.
2. Install VS Code.
3. Clone the repo:

   ```powershell
   git clone <repo-url> krisensicherOS
   cd krisensicherOS
   code .
   ```

4. Install the Claude Code Extension if approved by the organization.
5. In the project context, have the same start files read.
6. Have changes performed only after a plan and diff.

## Variant 3: Claude Code CLI on Windows

1. Open terminal: PowerShell or Windows Terminal.
2. Change into the repo:

   ```powershell
   cd C:\Users\<Name>\Documents\krisensicherOS
   ```

3. Start Claude Code CLI according to the vendor instructions.
4. Always request a plan before changes.
5. Check locally after changes:

   ```powershell
   git diff --check
   git status --short
   ```

## Change prompt with security boundaries

```text
Task: Add to or change <specific artifact>.

Rules:
- Follow AGENTS.md, CLAUDE.md, and 06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md.
- No legal advice, data protection advice, compliance assurance, or certification assurance.
- Use fictional examples.
- No real organizational, customer, personal, contract, incident, or system data.
- Show the plan first.
- Then change only the necessary files.
- Afterwards, show the diff and name the quality gates checked.
```

## Typical tasks

- consolidate README,
- add to setup documents,
- sharpen templates,
- create skills under `07-ai-governance-agents/skills/<name>/SKILL.md`,
- update workflows,
- prepare link and claim-safety checks.

## Stop points

Claude Code must not independently:

- publish, push, tag, or release,
- make license or disclaimer changes,
- write real organizational data into public examples,
- finalize legal or data protection assessments,
- make management decisions or risk acceptance.

## Windows self-test

Open PowerShell in the local krisensicherOS repo folder, for example:

```powershell
cd C:\Users\<Name>\Documents\krisensicherOS
```

Then check:

```powershell
git --version
code --version
git status --short
```

If `git status --short` shows unexpected changes: stop and clarify first whether these changes are intentional.

The recommended working location for the pilot is a local or internally approved working copy, not the entire user profile and not an unchecked sync of all company data.

## Branch, diff, and commit rules

Before changes:

```powershell
git status --short
git switch -c setup-pilot/<short-name>
```

Rules:

- work only on an approved working branch,
- no changes when the working tree is unclear,
- have the plan shown before changes,
- review the diff after changes,
- no commits without human approval,
- no pushes, tags, releases, or publications without explicit approval.

If local commits are allowed in the pilot, the responsible role must explicitly decide this beforehand. This stricter pilot rule takes precedence over general notes in `CLAUDE.md`.

## Minimum quality gate evidence after changes

After changes, Claude Code should report at least:

| Gate | Check question |
| --- | --- |
| U1 Public-Safe | Does the output contain real organizational, personal, customer, contract, or system data? |
| U2 Claim-Safety | Does the output contain legal, data protection, compliance, certification, or security assurances? |
| U3 Operating logic | Are owner, trigger, flow, evidence, and review clear? |
| U4 Empowerment | Does the artifact enable users or create unnecessary dependency? |
| U5 Workload | Is the effort realistic for a mid-sized organization? |
| U6 Portability | Does the artifact remain tool-neutral and adapter-ready? |
| A7 Adapter Gate | If tool-related: does the business logic remain in the source of truth and not hidden in the adapter? |
