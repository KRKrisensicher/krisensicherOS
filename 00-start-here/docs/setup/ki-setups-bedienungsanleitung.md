# Practical Guide: AI Setups for krisensicherOS

Status: 2026-05-23

## Purpose

This guide is the summary overview for the krisensicherOS setups. Separate setup documents are available for practical use:

- `README.md` (`README.md`) — entry point and setup selection,
- `chatgpt-lokale-ide.md` (`chatgpt-lokale-ide.md`) — ChatGPT with local IDE,
- `m365-copilot.md` (`m365-copilot.md`) — Microsoft 365 Copilot,
- `claude-code.md` (`claude-code.md`) — Claude Code App, VS Code, and CLI,
- `lokale-ki.md` (`lokale-ki.md`) — local AI without cloud.

krisensicherOS requires approved AI use. Without AI usage approval, only the approval is prepared; productive use starts only with an allowed AI environment and clear human gates.

The setup descriptions are primarily written Windows-first. macOS/Linux are mentioned only where relevant for developer or local AI setups.

The goal is not to “turn on AI and hope,” but a controlled way of working with data rules, human gates, prompts, and verifiable artifacts.

## If you only have 15 minutes: secure setup decision

| Situation | Secure start | Next step |
| --- | --- | --- |
| No AI usage approval | Stop | Use `templates/ki-nutzungsfreigabe-matrix.md` as approval template; no productive use |
| Approved cloud AI available | AI only with allowed data classes | Complete `templates/ki-nutzungsfreigabe-matrix.md` |
| Microsoft 365 Copilot is approved at tenant level | M365 path with SharePoint/permission check | Clarify data access, sensitivity labels, and owners |
| Local AI planned | Pilot with operations owner | Complete operating checklist for local AI and redaction tools |
| Confidential, personal, or licensed content | Stop / handoff | legal/data protection handoff; no processing in unclear AI environments |

## Mandatory gate before any AI use

Before ChatGPT, Microsoft 365 Copilot, Claude Code, local AI, or redaction tools are used, AI use must be approved.

Use `templates/ki-nutzungsfreigabe-matrix.md` or an equivalent internal organizational rule for this.

Minimum decision:

- data class: public, internal, confidential, personal, or licensed,
- allowed AI environment: approved cloud AI, M365 Copilot, local AI, or isolated environment,
- prohibited content: personal data, secrets, customer data, contract details, licensed standard texts,
- optional redaction step, e.g., OpenAI Privacy Filter or comparable tools,
- human gate for review and approval.

Redaction is not an anonymization guarantee and does not replace a data protection assessment.

## Research basis

Publicly available vendor and project documentation was reviewed for this guide:

- OpenAI Help: ChatGPT Work with Apps / VS Code Extension — ChatGPT can work with supported apps and VS Code via the macOS app; VS Code uses the `openai.chatgpt` extension.
- Microsoft Learn: Microsoft 365 Copilot Admin/Scenarios — Copilot scenarios are controlled via Microsoft 365 Admin Center / Copilot Control System and roles such as AI Administrator.
- Claude Code Docs: VS Code Extension — Claude Code offers a VS Code extension and CLI, with plan review, diffs, file context, and project work.
- Ollama — local execution of open models, optional cloud extension.
- LM Studio — local models, GUI, OpenAI-compatible API, SDK/CLI.
- Jan — free open-source desktop tool as a local ChatGPT replacement.
- GPT4All — local/private chatbot focus.
- Open WebUI — self-hosted, offline-capable web interface, supports Ollama and OpenAI-compatible APIs.
- Continue — AI-assisted development/review workflows and checks in the repo context.

## Basic decision: which setup for whom?

| Setup | Suitable for | Not ideal for |
| --- | --- | --- |
| ChatGPT + local IDE | Individuals, fast document/code work, low entry barrier | Strictly confidential data without an approval rule |
| Microsoft 365 Copilot | Organizations with M365, Word/Excel/Teams/SharePoint work | Repo-focused agent work without M365 governance |
| Claude Code | Repo work, structured changes, coding agents, docs-as-code | Pure Office users without Git/IDE |
| Local AI with LM Studio/Jan/GPT4All | Simple local chat/document work, data protection sensitivity | Complex repo agents without additional tools |
| Ollama + Open WebUI | Local team operations, API, RAG, self-hosting | Users without technical support |
| Ollama/LM Studio + Continue | Local or hybrid developer workflows | Pure Office processes |

## Common security rules

Define before every setup:

1. Data class: public, internal, confidential, personal, or licensed.
2. Allowed AI: cloud, local, M365 tenant, or project account.
3. Output limits: no legal advice, no data protection advice, no compliance or certification assurance.
4. Human gates: responsible person for review, decision, and approval.
5. Storage: location for documents, registers, evidence packs, and decision logs.
6. Standard texts: licensed content only as metadata, references, or own summaries.


## Setup A: ChatGPT with local IDE

### For whom?

For users who want to start without complex local AI infrastructure and use krisensicherOS as a repo, document base, or prompt library.

### Minimal toolkit

- ChatGPT account matching organizational approval.
- ChatGPT Desktop App if app/IDE integration is to be used.
- VS Code or compatible editor.
- Git.
- Local copy of the krisensicherOS repo.

### Step by step

1. **Store repo locally**

   ```bash
   git clone <repo-url> krisensicherOS
   cd krisensicherOS
   ```

2. **Open VS Code**

   ```bash
   code .
   ```

3. **Set up ChatGPT integration**

   - Open Extensions in VS Code.
   - Search for `ChatGPT` or `openai.chatgpt`.
   - Install extension if approved in the organization.
   - For VS Code forks, install VSIX according to OpenAI help if needed.

4. **Check working folders**

   Relevant start files:

   - `README.md`
   - `07-ai-governance-agents/README.md`
   - `07-ai-governance-agents/agents/public/role-model.md`
   - `07-ai-governance-agents/skills/README.md`
   - `templates/README.md`
   - `workflows/README.md`
   - `02-governance-operating-model/governance/review-process.md`

5. **Use first secure prompt**

   ```text
   You support me with krisensicherOS.

   Context:
   - I am working in a local repo.
   - Use only the files I provide to you or open in the project context.
   - Do not produce legal advice, data protection advice, compliance assurance, or certification assurance.
   - Mark assumptions, gaps, and human approvals.

   Task:
   Guide me step by step through the first NIS2/ISMS/audit walkthrough.

   Desired output:
   1. Which repo files I should open.
   2. Which questions I must answer.
   3. Which template I complete first.
   4. Which human gates I must observe.
   5. What I should check afterwards.
   ```

### Prompts for typical work

#### Start compliance register

```text
Use krisensicherOS as the working framework.

Goal: I want to create a first compliance register entry.

Use this structure:
- Source / reference
- Type of requirement
- Owner
- Confidentiality / license
- own summary
- possible governance routine
- evidence need
- human review

Limits:
No legal advice, no contract interpretation, no reproduction of standard text.
Ask for missing information instead of inventing it.
```

#### Document gap analysis

```text
Role: document-gap-analyst.

Compare the following document or the following summary with the requirements I provide.

Output:
- Document Gap Matrix
- missing content
- contradictory content
- outdated content
- statements that cannot support evidence
- need for change
- owner/review questions

Limits:
No final legal or compliance assessment. Mark assumptions and human gates.
```

#### Create audit questionnaire

```text
Role: internal-audit-planner.

Create an internal audit questionnaire from the following requirements.

For each requirement:
- Reference / criterion
- Audit guiding question
- expected evidence
- possible interview role
- suitable audit method
- evaluation note
- human gate

Do not use standard texts. Work only with my summaries and references.
```

## Setup B: Microsoft 365 Copilot

### For whom?

For organizations that already work with Word, Excel, PowerPoint, Teams, Outlook, SharePoint, and OneDrive and use Copilot administratively in the M365 tenant.

### Preconditions

- Microsoft 365 Copilot license or approved Copilot variant.
- Admin configuration in the Microsoft 365 Admin Center.
- Responsible roles, e.g., AI Administrator or corresponding admin role.
- Permissions, DLP, sensitivity labels, and SharePoint/OneDrive governance checked.

### Step by step for admin/owner

1. **Check license and tenant approval**

   - Is Microsoft 365 Copilot available for the organization?
   - Which apps/scenarios are activated?
   - Who may use Copilot?

2. **Check data access**

   - Clean up SharePoint/Teams permissions.
   - Check sensitivity labels and DLP rules.
   - Do not allow Copilot use on unchecked confidential areas.

3. **Create krisensicherOS working library**

   Recommended SharePoint structure:

   ```text
   krisensicherOS/
   ├── 01 Orientation
   ├── 02 Compliance Register
   ├── 03 Audit and Evidence
   ├── 04 Management Review
   ├── 05 Documents in Progress
   └── 99 Archive
   ```

4. **Upload core artifacts**

   - selected README files,
   - role model,
   - relevant templates,
   - quality gates,
   - review process.

5. **Document working rule in Teams/SharePoint**

   ```text
   Copilot may summarize krisensicherOS artifacts, derive questions, and prepare drafts.
   Copilot must not provide legal advice, data protection assessment, risk acceptance, or management decision.
   Confidential sources and licensed standards are used only as metadata or own summaries.
   ```

### Prompts for M365 Copilot

#### Word: structure document from raw material

```text
Create a structured governance document draft from these notes.

Use this structure:
1. Purpose
2. Scope and non-scope
3. Roles
4. Process / routine
5. Evidence
6. Review
7. Limits
8. open decisions

Mark assumptions and gaps. Do not produce legal advice or compliance assurance.
```

#### Excel: structure audit questions

```text
Create an audit questionnaire from this table.

Columns:
- Requirement / reference
- Control / topic
- Audit guiding question
- Audit method
- expected evidence
- Owner
- Evaluation note
- open human gate question

Use only the existing summaries; do not add standard texts.
```

#### Teams: summarize meeting

```text
Summarize this meeting as a governance review note.

Output:
- Decisions
- open questions
- risks
- measures with owner and deadline
- required evidence
- points for management review

Mark where human approval is required.
```

## Setup C: Claude Code

### For whom?

For repo-focused work: documentation, skills, templates, playbooks, workflows, checks, and structured changes in the Git repo.

### Minimal toolkit

- VS Code 1.98 or higher.
- Claude Code extension or Claude Code CLI.
- Anthropic account or approved provider.
- Git.
- Local krisensicherOS checkout.

### Step by step

1. **Install VS Code and open repo**

   ```bash
   git clone <repo-url> krisensicherOS
   cd krisensicherOS
   code .
   ```

2. **Install Claude Code**

   - Search for `Claude Code` in VS Code Extensions.
   - Install.
   - Sign in.
   - Alternatively, use CLI in the terminal if the extension is not available.

3. **Have project context read**

   First prompt:

   ```text
   Read README.md, AGENTS.md, 02-governance-operating-model/governance/review-process.md, and 06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md.

   Then explain to me:
   - how this repo works,
   - which stop points apply,
   - which files I should use for my first workflow.

   Do not make any changes before you have shown me the plan.
   ```

4. **Always make changes with plan and diff**

   Prompt:

   ```text
   Task: Add a new template for <topic>.

   Rules:
   - Follow templates/README.md and 06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md.
   - No legal advice, no data protection advice, no compliance assurance.
   - Use fictional examples.
   - Show the plan first.
   - Then change only the necessary files.
   - Afterwards, run a structure and claim-safety check.
   ```

### Typical Claude Code tasks

- new skills under `07-ai-governance-agents/skills/<name>/SKILL.md`,
- add templates,
- update workflows,
- link and structure checks,
- consolidate README,
- prepare release checklist.

## Setup D: Local AI without cloud

### For whom?

For organizations or individuals who do not want to send sensitive content to cloud AI or first want to experiment locally.

### Candidates

#### Ollama

Good for:

- developers,
- local API,
- fast model tests,
- combination with Open WebUI or Continue.

Typical start only after model/checkpoint approval:

```bash
ollama pull <approved-model:version>
ollama run <approved-model:version>
```

Before `pull`, document: source, model name, version, checkpoint/hash, license, storage location, purpose, and owner approval.

Recommendation:

- for simple governance texts: 7B–14B instruct model,
- for code/repo: coder model,
- for longer documents: model with a larger context window.

#### LM Studio

Good for:

- users who want a GUI instead of a terminal,
- local model management,
- OpenAI-compatible local API,
- tests with different models.

Procedure:

1. Install LM Studio.
2. Search for and download model.
3. Test chat.
4. Optionally activate local server / OpenAI-compatible API.
5. Connect with Continue, Open WebUI, or own tools.

#### Jan

Good for:

- simple local desktop chat,
- open-source approach,
- users who want “local ChatGPT” without much setup.

Procedure:

1. Install Jan.
2. Load local model.
3. Use governance prompts from this guide.
4. Do not include unchecked confidential data in exported examples.

#### GPT4All

Good for:

- simple local chat use,
- private 01-orientation/knowledge-sources/document questions,
- low entry barrier.

Not ideal for:

- complex repo agent work,
- larger team orchestration.

#### Open WebUI

Good for:

- self-hosted team interface,
- Ollama connection,
- RAG/knowledge collections,
- local or hybrid providers.

Typical start with Docker, only after version/digest approval:

```bash
docker run -d -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:<approved-version-or-digest>
```

Do not operate with `:main`. Image version or digest, update process, and restart behavior must be approved by the operations owner.

Then open in the browser:

```text
http://localhost:3000
```

#### Continue

Good for:

- VS Code/IDE-focused AI work,
- local or hybrid models,
- repo checks,
- coding and documentation workflows.

Recommendation:

- Connect Continue with Ollama or LM Studio.
- Define own checks for krisensicherOS: public safety, claim safety, secret scan, operating logic.


## Operating checklist for local AI and redaction tools

Local AI is not automatically secure. It is an operable system and needs owners, rules, and control.

Clarify before productive use:

| Check field | Minimum clarification |
| --- | --- |
| System owner | Who operates Ollama, LM Studio, Open WebUI, Continue, or redaction components? |
| Purpose / scope | For which tasks may the system be used? |
| Data classes | Which data may be processed? Which are prohibited? |
| Access | Who may use, administer, and see logs? |
| Model approval | Which models/checkpoints are allowed? Who approves changes? |
| Patch / update | Who updates app, runtime, container, models, and dependencies? |
| Logging | Which inputs, outputs, metadata, or error logs are stored? |
| Storage locations | Where are models, prompts, uploads, vector databases, exports, and backups located? |
| Redaction | Is a tool such as OpenAI Privacy Filter used? How is it evaluated? |
| Evaluation | How are false positives, false negatives, and domain suitability checked? |
| Offboarding | How are users, models, data, and logs removed or archived? |
| Human Review | Who reviews critical outputs before sharing or decision? |

For OpenAI Privacy Filter or comparable redaction components, additionally clarify:

- Where are model weights and checkpoints located?
- Are inputs or redaction results stored?
- Which label categories are detected and which are not?
- Are there tests with German, domain-specific, and organization-related examples?
- Who decides whether redaction results are sufficient for the specific purpose?

Redaction remains an auxiliary layer. It does not replace data classification, a data protection assessment, or human approval.

## Local AI: hardware rules of thumb

| Hardware | Useful start |
| --- | --- |
| 16 GB RAM, no strong GPU | small 3B–8B models, short tasks |
| 32 GB RAM | 7B–14B models, limited document work |
| 64 GB RAM or Apple Silicon with a lot of unified memory | larger models, longer documents |
| strong NVIDIA GPU | faster inference, larger models, team/API use |

Important: Local models are not automatically better or more secure. They reduce cloud outflow, but still need data classification, logging, access control, and human review.

## Recommended v1.0 setup by maturity level

### Level 1 — Simplest start

- ChatGPT or M365 Copilot
- krisensicherOS templates as files
- no confidential data
- manual human gates

### Level 2 — Repo work

- VS Code
- Claude Code or ChatGPT Work with Apps
- Git
- local checks
- work via 07-ai-governance-agents/skills/templates/workflows

### Level 3 — Data-protection-sensitive pilot

- LM Studio or Jan for local chat
- Ollama for local API
- no cloud data transfer
- manual quality assurance

### Level 4 — Team-capable operations

- Open WebUI + Ollama/LM Studio/API
- M365 Copilot for Office work
- Claude Code/Continue for repo work
- clear roles, logs, review process, release gates

## Universal prompt for krisensicherOS

```text
You are working with krisensicherOS.

Working rules:
- No legal advice.
- No data protection advice.
- No compliance, certification, or security assurance.
- No management decision.
- Use sources, standards, and contracts only as references, metadata, or own summaries.
- Mark assumptions, gaps, evidence needs, and human gates.
- Produce output with owner, trigger, process, evidence, review, and next step.

Task:
<insert specific task>

Input:
<insert scope, requirements, raw material, or documents>

Desired output:
<insert template, skill output, or review format>
```

## Which local AI is suitable?

Realistic options for krisensicherOS:

1. **Ollama** — best basis for local model API and developer workflows.
2. **LM Studio** — best GUI for local model tests and local OpenAI-compatible API.
3. **Jan** — simple open-source desktop chat.
4. **GPT4All** — simple private local chat, good for low-threshold use.
5. **Open WebUI** — self-hosted team interface for local/hybrid models.
6. **Continue** — IDE/repo assistant, especially with Ollama or LM Studio.
7. **AnythingLLM** — relevant for local knowledge bases/RAG when document collections are the focus.

Recommendation for v1.0:

- **Do not support everything at the same time.**
- Primarily document: ChatGPT, M365 Copilot, Claude Code.
- Document local as three paths:
  - simple: LM Studio or Jan,
  - technical: Ollama,
  - team-capable: Ollama + Open WebUI,
  - IDE: Continue + Ollama/LM Studio.

## Definition of Done for a setup

A setup is ready for use when:

- data classes and allowed AI are defined,
- users know where krisensicherOS artifacts are located,
- a universal prompt is available,
- at least one end-to-end workflow has been tested,
- human gates are documented,
- outputs are checked against quality gates,
- no publication or external sharing occurs without approval.
