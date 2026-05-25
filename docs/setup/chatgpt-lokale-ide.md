<!-- kso:product-relevance
repo-scope: product
classification: setup-guidance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Setup: ChatGPT with Local IDE

Status: 2026-05-23

## Purpose

This setup is for individuals or small teams that want to use krisensicherOS with ChatGPT and a local working environment.

ChatGPT may only be used if the organization has approved its use for the affected data classes.

## Windows-first Toolkit

- Windows 10/11,
- VS Code or compatible editor,
- Git for Windows,
- local krisensicherOS checkout or ZIP download,
- ChatGPT account aligned with organizational approval,
- optionally ChatGPT Desktop App or VS Code integration, if approved.

## Step by Step on Windows

1. Install Git for Windows or download the repo as a ZIP.
2. Create a working folder, e.g., `C:\\Users\\<Name>\\Documents\\krisensicherOS`.
3. Open the repo:

   ```powershell
   git clone <repo-url> krisensicherOS
   cd krisensicherOS
   code .
   ```

4. Open starting files:
   - `README.md`
   - `docs/getting-started/minimaler-nis2-start-in-5-artefakten.md`
   - `docs/setup/README.md`
   - `templates/ki-nutzungsfreigabe-matrix.md`

5. Check AI usage approval: the matrix and ChatGPT-specific check table must be clarified before the first prompt.
6. Enter only approved, suitable content into ChatGPT.
7. Treat outputs as drafts and check them against human gates.

## Hard Approval Gate Before the First Prompt

Without a completed [`../../templates/ki-nutzungsfreigabe-matrix.md`](../../templates/ki-nutzungsfreigabe-matrix.md) **and** without the following ChatGPT-specific check table, this path is not used. In that case, only the approval is prepared; productive use stops.

Before the first ChatGPT use, document:

| Check Field | Minimum Clarification |
| --- | --- |
| Account/workspace type | Personal, Team, Enterprise, or approved internally by the organization? |
| Contract/admin approval | Who approved use and data classes? |
| Data use | Are training/data-use settings, history, and memory clarified? |
| Uploads | Are file uploads allowed or only copy/paste of approved excerpts? |
| IDE context | May ChatGPT read project files or editor context? |
| Connectors | Are external connectors disabled or approved? |
| Logging/deletion | Who knows the storage, export, and deletion rules? |
| Prohibited content | Secrets, personal data, customer data, contract details, and licensed standard texts excluded? |

If the data class, account type, or data use is unclear: stop and clarify approval.

## Safe First Prompt

Stop: Use this prompt only after the approval matrix and ChatGPT-specific check table have been completed.

```text
You are supporting me with krisensicherOS.

Context:
- I am working in a local Windows working copy.
- Use only the files I provide to you or explicitly describe.
- Do not create legal advice, data protection advice, compliance assurance, or certification assurance.
- Mark assumptions, gaps, evidence needs, and human approvals.
- Process only content whose data class is approved for this ChatGPT environment. Ask me to stop if input could be confidential, personal, customer-specific, contractual, licensed, or a secret.

Task:
Guide me step by step through the first NIS2/ISMS/audit walkthrough.

Desired output:
1. Which repo files I should open.
2. Which questions I need to answer.
3. Which template I fill out first.
4. Which human gates I need to observe.
5. What I should check afterward.
```

## Do Not Use For

- unclear confidential content,
- personal data without approval,
- customer data, contract details, or secrets,
- licensed standard texts,
- final legal, data protection, risk, or management decisions.

## Windows Start Clarified

If no specific repo URL is available yet, use a ZIP working copy or an internally provided copy.

PowerShell example with Git:

```powershell
cd $HOME\Documents
git clone <freigegebene-repo-url> krisensicherOS
cd krisensicherOS
code .
```

`<freigegebene-repo-url>` must be replaced with the internal or public approved repo address.

## Human Gates for ChatGPT Outputs

| Output / Topic | Human Gate |
| --- | --- |
| Legal/regulatory reference | Legal or responsible specialist role reviews |
| personal data | Data protection role reviews |
| risk acceptance | Management decides |
| technical evidence | IT/system owner reviews |
| publication or external sharing | specialist approval in advance |
| unclear data class | Stop and clarify approval/handoff |
