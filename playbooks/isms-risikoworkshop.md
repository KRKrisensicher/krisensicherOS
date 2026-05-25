<!-- kso:product-relevance
repo-scope: product
classification: playbook
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->

# Playbook: ISMS Risk Workshop

## Purpose

This playbook guides a compact risk workshop that identifies risks, assesses them using a gross/net methodology, derives measures, and prepares control/SoA mappings.

The workshop produces operable decisions and evidence. It does not replace a risk tool or a management decision.

## Trigger

- quarterly ISMS risk workshop,
- significant changes to assets, processes, service providers, or the threat situation,
- incident, audit finding, or nonconformity,
- preparation for management review,
- control/SoA review or measure prioritization.

## Participants

- information security officer / CISO / ISMS owner as moderator,
- affected asset owners and process owners,
- control owners / measure owners,
- data protection, legal, procurement, IT operations, or management representative as needed,
- optional agent support for structuring, mapping, and draft minutes.

## Preparation

SoA optional: If no dedicated ISO 27001 SoA exists yet, the workshop initially uses an internal risk-control map. Later SoA creation is performed separately based on license-compliant ISO 27001 use.

1. Define scope and out-of-scope.
2. Open the current risk analysis register.
3. Open the current risk-control map / SoA extension.
4. Collect new triggers: incidents, audits, changes, vulnerabilities, service provider changes, management questions.
5. Mark open measures and overdue reviews.
6. Prepare decision points: acceptance, resources, avoidance, transfer, scope questions.

## Dialog-Based Risk Wizard

For individual risks or small workshops, the risk process can be carried out as a guided wizard. The wizard uses the skill [`isms-risk-analysis`](../skills/isms-risk-analysis/SKILL.md) and records the status in [`templates/risikoanalyse-session-state.md`](../templates/risikoanalyse-session-state.md).

Working rules:

- The moderator asks a maximum of 1-3 questions at a time.
- Each answer is assigned to a field in the session state.
- Missing mandatory fields are clarified before the next phase.
- Unclear statements are marked as assumptions and later confirmed or rejected.
- Each phase ends with a short summary: completed, open, assumptions, human gates, next question.

Phases:

1. Start or continue session.
2. Describe risk as vulnerability + asset + threat.
3. Capture the current measure situation.
4. Assess gross risk.
5. Select a strategy or prepare it as a decision.
6. Plan measures and control/SoA mapping.
7. Assess net/residual risk.
8. Generate reporting.

## Procedure

### 1. Confirm Entry Point and Scope

- Which assets, processes, or services are we considering?
- What intentionally remains outside today’s scope?
- Which decisions can be prepared in the workshop but not made final?

### 2. Formulate Risks

For each risk, check:

```text
Risk = vulnerability + asset + threat
```

Mandatory sentence:

```text
If [threat] exploits the vulnerability [vulnerability] on the asset [asset],
then [impact] may occur.
```

Unclear entries are marked as hypotheses and are not assessed as reliable.

### 3. Capture the Current Measure Situation

Before the assessment, the current situation is made visible. This can be prepared using [`templates/risikoanalyse-fragebogen.md`](../templates/risikoanalyse-fragebogen.md) and AI-assisted structuring.

- Which organizational, technical, and procedural measures already exist?
- Which incident response, crisis management, or BCMS capabilities limit the damage?
- Which measures are actually operated?
- Which evidence shows implementation and operation?
- Which control/SoA references belong to them?
- Which gaps or unverified assumptions remain?

The measure situation is confirmed by the asset owner or information security officer from a subject-matter perspective. AI results remain preparatory work.

### 4. Assess Gross Risk

- Assess detectability, exploitability, and concealment.
- Determine the probability factor as the maximum value.
- Assess material damage, personal injury, financial loss, and intangible damage.
- Determine the damage factor as the maximum value.
- Calculate the gross risk value.

The current measure situation is context. It must not automatically reduce the gross value.

### 5. Decide or Prepare Strategy

From a risk value of 7 onward, a strategy is prepared:

- acceptance,
- avoidance,
- transfer, e.g., insurance, outsourcing, or handover of certain response elements to crisis management / BCMS,
- minimization through measures.

Risk acceptance, resource approvals, transfer, and avoidance are marked as human gates and prepared in the decision log.

### 6. Derive and Plan Measures

Define the following for each measure:

- measure ID,
- risk reference,
- control/SoA reference,
- owner,
- effect on likelihood of occurrence, extent of damage, or both,
- due date,
- evidence source,
- effectiveness check,
- net/residual risk effect as planned value,
- later effectiveness check point.

### 7. Assess Net/Residual Risk

- Perform the assessment according to the selected strategy and planned measures.
- Use the same criteria as for gross risk.
- Plausibly explain which factors should change and why.
- Mark whether the assessment is a planned value or already confirmed.
- Report confirmed net risk only after implementation and effectiveness check.

### 8. Generate Reporting and Management Input

At the end, record:

- top risks by net risk,
- new or changed risk acceptances,
- overdue measures,
- control/SoA gaps,
- resource or scope decisions,
- next reviews.

## Output

- updated risk analysis register,
- updated risk-control map / SoA extension,
- measures list or backlog entries,
- decision log entries,
- workshop note as evidence,
- management review input,
- optional risk report as Markdown or HTML.

## Quality Check

- No risk without asset, vulnerability, and threat.
- Current measure situation documented before the gross assessment.
- Gross and net/residual risk documented in the correct order.
- Confirmed net risk reported only after implementation and effectiveness check.
- Measures have owner, due date, evidence, and effectiveness check.
- Control/SoA reference is maintained or marked as a gap.
- Human decisions are visible and not replaced by agents.

## Boundaries

Does not provide legal advice, does not provide data protection advice, does not provide certification assurance, no risk acceptance by agents. Real organizational data belongs only in approved internal working environments.
