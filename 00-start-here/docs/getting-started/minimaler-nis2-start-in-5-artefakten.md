# Minimal NIS2 Start in 5 Artifacts

## Purpose

This path reduces krisensicherOS to the smallest meaningful AI-assisted end-to-end pass.

It is intended for CISO/information security officer teams, security leads, and GRC roles that need to start NIS2 pragmatically without building a large compliance machinery.

## Preliminary gate: AI usage approval

krisensicherOS requires approved AI usage.

Before content is entered into an AI system:

1. Determine the data class: public, internal, confidential, personal, licensed.
2. Define the permitted AI environment: approved cloud AI, M365 Copilot, Claude Code, local AI, or isolated environment.
3. Exclude prohibited content: real customer data, personal data, secrets, contract details, licensed standard texts.
4. Set a human gate: AI output is a draft, not a decision.
5. Document approval in `../../templates/ki-nutzungsfreigabe-matrix.md` (`../../07-ai-governance-agents/templates/ki-nutzungsfreigabe-matrix.md`) or an equivalent internal rule.

If there is no AI usage approval: stop. Only the approval can then be prepared; krisensicherOS is not yet used productively.

## Where AI may help

AI may help with:

- structuring,
- summarizing approved content,
- drafting wording,
- generating questions,
- comparing with your own summaries,
- preparing evidence and decision logic.

AI must not:

- provide legal advice,
- make data protection assessments,
- confirm compliance,
- make management decisions,
- process confidential or licensed content in an uncontrolled way.

## The 5 artifacts

### 1. Management mandate and decision question

**File:** `templates/decision-log.md`

Clarify first:

- What should NIS2 concretely achieve in the next 30 days?
- Which management decision is needed?
- Which resources, priorities, or risk acceptances are open?
- Who is professionally responsible?

Minimal output:

```text
Decision question: Which three NIS2 action areas do we prioritize in the first end-to-end pass?
Owner: Executive management / CISO-information security officer / business unit
Required evidence: register entry, gap worksheet, first evidence requests
Deadline: <Date>
Human Gate: Management decision
```

### 2. Compliance register entry

**File:** `templates/compliance-source-register.md`

Record a source or requirement as a reference and your own summary.

Do not:

- copy standard texts,
- claim legal interpretation,
- transfer confidential contract content into public artifacts.

Minimal output:

```text
Source / reference: <public source or internal register reference>
Own summary: <short working summary>
Affected area: <process / control / role>
Owner question: Who is responsible for the routine?
```

### 3. NIS2 gap worksheet

**File:** `templates/nis2-gap-worksheet.md`

Translate the source into an initial gap.

Minimal output:

```text
Target state: <own summary>
Current state: <known status>
Gap: <missing role, routine, evidence, or decision>
Impact: <operational relevance>
Next step: <evidence request or management question>
```

### 4. Evidence request

**File:** `templates/evidence-request-list.md`

Request only evidence that is truly needed for the next decision.

Rule for the first end-to-end pass:

- maximum three requests per owner,
- existing evidence first,
- do not request new documents if existing evidence is sufficient,
- estimate effort,
- check confidentiality.

Minimal output:

```text
Required evidence: <specific evidence>
Purpose: <which question does the evidence answer?>
Owner: <role>
Effort: low / medium / high
Reuse: existing evidence usable? yes/no/open
```

### 5. Decision log and management review handoff

**File:** `templates/decision-log.md`

Feed the results back into a decision template.

Minimal output:

```text
Decision point: <prioritization / resources / risk acceptance>
Options: <Option A/B/C>
Evidence status: <what is available, what is missing?>
Recommendation for decision preparation: <no decision by AI>
Owner: <management role>
```

## 60-minute flow

1. 10 minutes: check AI usage approval.
2. 10 minutes: formulate management question.
3. 15 minutes: register one source / requirement.
4. 15 minutes: capture one gap.
5. 10 minutes: create a maximum of three evidence requests and one decision log entry.

## What deliberately does not happen

The minimal start does not:

- fully assess all NIS2 topics,
- write all policies,
- test all controls,
- ask all business units,
- claim compliance,
- decide data protection or legal questions.

## Definition of Done

The minimal start is complete when:

- AI usage is approved for the data and tools used,
- a management question is documented,
- a source or requirement is recorded,
- a gap is visible,
- a maximum of three concrete evidence requests are available,
- a decision log or management review handoff exists,
- human gates are marked.

## Next step

If the minimal start is viable, continue with:

- `01-orientation/getting-started/30-60-90-minuten-nutzungspfad.md`,
- `workflows/audit-evidence-remediation-chain.yaml`,
- `templates/legal-datenschutz-handoff.md` as soon as legal or data protection questions arise.
