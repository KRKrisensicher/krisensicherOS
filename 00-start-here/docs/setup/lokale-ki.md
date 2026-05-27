# Setup: Local AI without cloud

As of: 2026-05-23

## Purpose

This setup is for organizations or individuals who want to operate or test AI locally without sending content to cloud AI.

Local AI is not automatically secure. It is an operable system with an owner, access control, model approval, logging, evaluation, and offboarding.

## Windows-first candidates

| Tool | Suitable for |
| --- | --- |
| LM Studio | GUI, local model tests, OpenAI-compatible local API |
| Jan | simple local desktop chat |
| GPT4All | low-threshold local chat/document use |
| Ollama | local model API, developer workflows, combination with Open WebUI/Continue |
| Open WebUI | self-hosted team interface, usually with Ollama |
| Continue | IDE/repo assistant with local or hybrid model connection |

## Getting started for Windows users

Basic rule: **first document model/checkpoint approval, then download, install, or run `ollama pull`.**

1. Start with LM Studio or Jan if a simple GUI is needed.
2. Start with Ollama if local APIs or developer workflows are needed.
3. For team use, deploy Open WebUI only with an operating owner and an access concept.
4. For repo work, review Continue with Ollama or LM Studio.

## Example: LM Studio

1. Install LM Studio.
2. Document model/checkpoint approval.
3. Download a suitable approved model.
4. Test local chat.
5. Optionally activate the local server.
6. Use only approved data classes.
7. Check outputs against human gates.

## Example: Ollama

```powershell
# only after model/checkpoint approval
ollama pull <approved-model:version>
ollama run <approved-model:version>
```

Before `pull`, document: source, model name, version, checkpoint/hash, license, storage location, purpose, and owner approval.

Recommendation:

- simple governance texts: 7B–14B instruct model,
- code/repo: coder model,
- longer documents: model with a larger context window.

## Operating checklist

| Check field | Minimum clarification |
| --- | --- |
| System owner | Who operates local AI, model servers, or redaction components? |
| Purpose / scope | For which tasks may the system be used? |
| Data classes | Which data may be processed? Which are prohibited? |
| Access | Who may use, administer, and view logs? |
| Model approval | Which models/checkpoints are allowed? Who approves changes? |
| Patch / update | Who updates the app, runtime, container, models, and dependencies? |
| Logging | Which inputs, outputs, metadata, or error logs are stored? |
| Storage locations | Where are models, prompts, uploads, vector databases, exports, and backups stored? |
| Evaluation | How are false positives, false negatives, and domain suitability checked? |
| Offboarding | How are users, models, data, and logs removed or archived? |
| Human review | Who reviews critical outputs before forwarding or decision-making? |

## Redaction tools

OpenAI Privacy Filter or comparable tools can be reviewed as an auxiliary layer. In a local “without cloud” setup, such tools may only be used if they are actually operated locally or if explicit approval exists for a cloud-based data flow for the affected data class.

Clarify before use:

- Where are model weights and checkpoints stored?
- Are inputs or redaction results stored?
- Which label categories are detected and which are not?
- Are there tests with German, domain-specific, and organization-near examples?
- Who decides whether redaction results are sufficient for the specific purpose?

Redaction does not replace data classification, data protection assessment, or human approval.

## Model/checkpoint approval

Before downloading or changing a model, document:

| Check field | Minimum clarification |
| --- | --- |
| Source / registry | Where does the model come from? |
| Model name / version | Which specific version is used? |
| Checkpoint / hash / quantization | Which file/variant was approved? |
| License | May the model be used for the intended purpose? |
| Storage location | Where are the model, cache, and configuration stored? |
| Purpose | For which tasks is the model approved? |
| Owner approval | Who approved use and changes? |

Model changes, new quantization, or a new checkpoint count as a new approval.

## Windows pilot checklist

Before local use on Windows, check:

- Does a local server run only on `127.0.0.1`, or is it reachable on the network?
- Where are the model cache, chat histories, uploads, exports, vector databases, and backups stored?
- Are admin rights required for installation or operation?
- Are local app logs, error logs, or telemetry data written?
- Is network access blocked, restricted, or deliberately approved?
- Are work data stored in the user profile, in OneDrive, in a central repository, or in a project folder?
- Is it clear who may delete, export, or back up data?

Unclear storage locations or unclear network binding lead to stop; productive use starts only after operational approval or exclusively with public/fictional test data.

## Minimum decision on logging and storage locations

Before pilot start, at minimum, storage locations for models, prompts, uploads, chat histories, exports, vector databases, logs, and backups must be documented.

If it is not clear what is stored or who has access to logs, testing may only be performed with public or fictional data.

## Team use / Open WebUI gate

Use team interfaces such as Open WebUI only once the following has been clarified:

- role model: users, admins, owners, log access,
- authentication and access removal,
- separation of projects and data spaces,
- deletion and export rights,
- handling of shared chats,
- handling of RAG data and vector databases,
- review process for new users, models, and knowledge collections.

Without this clarification, local AI remains limited to a single-user pilot with fictional or public data.

## Redaction in the local setup

Redaction tools may only be used in the local setup if operating mode, data flow, storage locations, logging, and model/checkpoint storage are demonstrably clarified.

A cloud-based redaction tool is not part of a “without cloud” setup unless explicit approval exists for this data class.

## Minimum evaluation before productive use

Before productive use, check at least 5–10 fictional or domain-typical test cases:

- summary without invented facts,
- hallucination with incomplete inputs,
- incorrect security or compliance statement,
- legal/data protection claim,
- secret detection,
- redaction false negative,
- German technical terms and abbreviations,
- handling of contradictory documents,
- clear marking of assumptions and human gates.
