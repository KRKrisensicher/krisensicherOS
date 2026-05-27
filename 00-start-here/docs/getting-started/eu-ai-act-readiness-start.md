# Start EU AI Act readiness

## Purpose

This entry point helps make AI use in an organization visible and prepare it as a governance routine.

It does not provide legal advice, data protection advice, a binding EU AI Act classification, or a conformity assessment. The result is an inventory and handoff artifact for accountable humans.

## When to use?

Use this path if:

- AI systems, AI functions, or AI services are used in the organization,
- cloud AI, M365 Copilot, business applications with AI functions, or local AI are being introduced,
- it is unclear who is responsible from a business, technical, or legal perspective,
- data classes, personal data, or human oversight have not yet been clarified,
- legal, data protection, management, or IT/security need a structured preliminary check.

## 15-minute start

Open only these artifacts:

1. `../../templates/ki-nutzungsfreigabe-matrix.md` (`../../07-ai-governance-agents/templates/ki-nutzungsfreigabe-matrix.md`)
2. `../../templates/ki-system-inventar-und-risikovorpruefung.md` (`../../07-ai-governance-agents/templates/ki-system-inventar-und-risikovorpruefung.md`)
3. `../../templates/legal-datenschutz-handoff.md` (`../../02-governance-operating-model/templates/legal-datenschutz-handoff.md`)
4. `../../templates/decision-log.md` (`../../02-governance-operating-model/templates/decision-log.md`)

After 15 minutes, it should be clear:

- which AI system or AI use case is being considered,
- who the business owner is,
- which data class is affected,
- whether personal data, confidential content, or external providers play a role,
- which human review is required,
- which decision remains open.

## Guiding questions

### 1. What is the AI system or AI use case?

- name or working title,
- provider or internal solution,
- business purpose,
- affected process,
- user group.

### 2. What role does the organization have?

Capture only as a working assumption, not as a final assessment:

- does the organization procure or use an AI system?
- does it operate or configure it itself?
- does it integrate it into its own services?
- does it make it available to others?

Final assessment of roles and obligations is a legal/management handoff.

### 3. Which data and decisions are affected?

- data class: public, internal, confidential, personal, especially sensitive, or unclear,
- proximity to decision-making: assisting, recommending, prioritizing, automating,
- impact on people, customers, employees, security, availability, or critical processes,
- logging and traceability.

### 4. What human oversight exists?

- Who reviews inputs?
- Who reviews outputs?
- Who may adopt outputs?
- Who stops use in case of errors, bias, hallucinations, data protection risks, or security risks?
- Who decides on approval, restriction, or non-use?

## Minimal output

- one entry in the AI system inventory,
- one data class and approval assumption,
- one legal/data protection handoff for open questions,
- one decision log entry with owner, next step, and review date.

## Connection to krisensicherOS

- For approved AI environments: `../../templates/ki-nutzungsfreigabe-matrix.md` (`../../07-ai-governance-agents/templates/ki-nutzungsfreigabe-matrix.md`)
- For governance decisions: `../../templates/decision-log.md` (`../../02-governance-operating-model/templates/decision-log.md`)
- For legal or data protection questions: `../../templates/legal-datenschutz-handoff.md` (`../../02-governance-operating-model/templates/legal-datenschutz-handoff.md`)
- For workflow control: `../../workflows/eu-ai-act-readiness-precheck.yaml` (`../../07-ai-governance-agents/workflows/eu-ai-act-readiness-precheck.yaml`)
- For operating rules for agents: `../../07-ai-governance-agents/` (`../../07-ai-governance-agents/`)

## Stop points

Stop and obtain human approval for:

- final EU AI Act role or risk classification,
- legal or data protection assessment,
- use with personal, confidential, or especially sensitive data,
- AI outputs with an impact on people or essential business processes,
- external communication, customer commitment, or provider approval,
- management decision on introduction, restriction, or risk acceptance.

## Boundaries

This starter makes AI use visible and prepares questions that can be decided. It does not confirm EU AI Act conformity, permissibility, data protection conformity, or technical security.
