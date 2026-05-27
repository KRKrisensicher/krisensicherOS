# Artifact packages for getting started

## Purpose

These packages bundle existing templates, playbooks, workflows, and guides for small initial implementation passes. They are not complete compliance programs and do not provide legal advice, data protection advice, compliance assurance, or certification assurance.

If you do not yet know which package fits, start with the `user paths` (`anwenderpfade.md`).

## Reading rule

Each package is sorted by effort:

- **Required in 15 minutes:** open only these artifacts if you want to start quickly.
- **After that:** use once the first output exists.
- **Only if needed:** add when scope, risk, or a management question requires it.

## Package 1: NIS2 minimal start

**Goal:** Derive an initial NIS2 gap, evidence need, and decision point from a management question.

**Required in 15 minutes:**

1. `minimaler-nis2-start-in-5-artefakten.md` (`minimaler-nis2-start-in-5-artefakten.md`)
2. `../../templates/ki-nutzungsfreigabe-matrix.md` (`../../07-ai-governance-agents/templates/ki-nutzungsfreigabe-matrix.md`)
3. `../../templates/nis2-gap-worksheet.md` (`../../03-nis2-readiness/templates/nis2-gap-worksheet.md`)
4. `../../templates/decision-log.md` (`../../02-governance-operating-model/templates/decision-log.md`)

**After that:**

- `../../templates/evidence-request-list.md` (`../../06-evidence-management-review/templates/evidence-request-list.md`)
- `../../workflows/nis2-readiness-gap.yaml` (`../../03-nis2-readiness/workflows/nis2-readiness-gap.yaml`)

**Only if needed:**

- `../../templates/compliance-source-register.md` (`../../08-templates-playbooks/templates/compliance-source-register.md`)
- `../../playbooks/nis2-readiness-startworkshop.md` (`../../03-nis2-readiness/playbooks/nis2-readiness-startworkshop.md`)

**Suitable agents:** `nis2-scope-precheck-analyst`, `nis2-readiness-analyst`, `compliance-operating-system-lead`.

**Minimal output:** Management question, one source/reference, one gap, up to three evidence requests, one human gate handoff.

**Stop points:** Applicability or legal interpretation, external communication, real customer data, confidential contract content, management decision.

## Package 2: ISMS minimal start

**Goal:** Start a minimum viable ISMS as a role, risk, measure, and review routine.

**Required in 15 minutes:**

1. `../../09-implementation-roadmaps/examples/fiktiver-mittelstand/isms-90-minuten-durchstich.md` (`../../09-implementation-roadmaps/examples/fiktiver-mittelstand/isms-90-minuten-durchstich.md`)
2. `../../templates/isms-scope-canvas.md` (`../../04-isms-basics/templates/isms-scope-canvas.md`)
3. `../../templates/rollenmatrix.md` (`../../02-governance-operating-model/templates/rollenmatrix.md`)
4. `../../templates/risikoregister-starter.md` (`../../04-isms-basics/templates/risikoregister-starter.md`)

**After that:**

- `../../04-isms-basics/implementation-guides/isms/01-kontext-scope-und-betroffenheit.md` (`../../04-isms-basics/implementation-guides/isms/01-kontext-scope-und-betroffenheit.md`)
- `../../04-isms-basics/implementation-guides/isms/02-rollen-verantwortung-und-managementauftrag.md` (`../../04-isms-basics/implementation-guides/isms/02-rollen-verantwortung-und-managementauftrag.md`)
- `../../04-isms-basics/implementation-guides/isms/03-risikosteuerung-und-massnahmenplanung.md` (`../../04-isms-basics/implementation-guides/isms/03-risikosteuerung-und-massnahmenplanung.md`)
- `../../templates/soa-risk-control-map.md` (`../../04-isms-basics/templates/soa-risk-control-map.md`)

**Only if needed:**

- `../../04-isms-basics/implementation-guides/isms/00-nutzung-und-grenzen.md` (`../../04-isms-basics/implementation-guides/isms/00-nutzung-und-grenzen.md`)
- `../../workflows/minimum-viable-isms.yaml` (`../../04-isms-basics/workflows/minimum-viable-isms.yaml`)
- `../../playbooks/minimum-viable-isms-setup.md` (`../../04-isms-basics/playbooks/minimum-viable-isms-setup.md`)

**Suitable agents:** `isms-operating-model-designer`, `security-governance-architect`, `risk-and-obligation-prioritizer`.

**Minimal output:** Scope statement, role assumption, three risks, three measure routines, one review date, one decision point.

**Stop points:** Scope approval, risk acceptance, certification/audit interpretation, resource decision, confidential content without approval.

## Package 3: Incident/notification readiness

**Goal:** Practice escalation and notification triage without transferring real incidents or personal data into public examples.

**Required in 15 minutes:**

1. `../../templates/incident-escalation-card.md` (`../../05-incident-crisis-readiness/templates/incident-escalation-card.md`)
2. `../../templates/nis2-incident-melde-triage.md` (`../../03-nis2-readiness/templates/nis2-incident-melde-triage.md`)
3. `../../templates/legal-datenschutz-handoff.md` (`../../02-governance-operating-model/templates/legal-datenschutz-handoff.md`)

**After that:**

- `../../playbooks/incident-escalation-first-assessment.md` (`../../05-incident-crisis-readiness/playbooks/incident-escalation-first-assessment.md`)
- `../../playbooks/nis2-incident-melde-triage.md` (`../../03-nis2-readiness/playbooks/nis2-incident-melde-triage.md`)
- `../../templates/corrective-action-plan.md` (`../../06-evidence-management-review/templates/corrective-action-plan.md`)

**Only if needed:**

- `../../workflows/nis2-incident-and-management-readiness.yaml` (`../../05-incident-crisis-readiness/workflows/nis2-incident-and-management-readiness.yaml`)
- `../../playbooks/tabletop-ransomware.md` (`../../05-incident-crisis-readiness/playbooks/tabletop-ransomware.md`)

**Suitable agents:** `incident-readiness-coach`, `management-review-facilitator`, `agent-quality-and-safety-reviewer`.

**Minimal output:** Escalation card, triage draft, human gate list, exercise scenario, initial corrective actions.

**Stop points:** Notification obligation assessment, data protection assessment, legal interpretation, communication to authorities/customers/public, crisis team decision.
## Package 4: EU AI Act readiness starter

**Goal:** Make AI systems and AI use cases visible without claiming a final legal or data protection assessment.

**Required in 15 minutes:**

1. `eu-ai-act-readiness-start.md` (`eu-ai-act-readiness-start.md`)
2. `../../templates/ki-nutzungsfreigabe-matrix.md` (`../../07-ai-governance-agents/templates/ki-nutzungsfreigabe-matrix.md`)
3. `../../templates/ki-system-inventar-und-risikovorpruefung.md` (`../../07-ai-governance-agents/templates/ki-system-inventar-und-risikovorpruefung.md`)
4. `../../templates/decision-log.md` (`../../02-governance-operating-model/templates/decision-log.md`)

**After that:**

- `../../templates/legal-datenschutz-handoff.md` (`../../02-governance-operating-model/templates/legal-datenschutz-handoff.md`)
- `../../workflows/eu-ai-act-readiness-precheck.yaml` (`../../07-ai-governance-agents/workflows/eu-ai-act-readiness-precheck.yaml`)

**Only if needed:**

- `../../07-ai-governance-agents/human-in-the-loop.md` (`../../07-ai-governance-agents/human-in-the-loop.md`)
- `../../07-ai-governance-agents/risk-and-limits.md` (`../../07-ai-governance-agents/risk-and-limits.md`)
- `../../01-orientation/knowledge-sources/hardwired-sources.yaml` (`../../01-orientation/knowledge-sources/hardwired-sources.yaml`)

**Suitable agents:** `compliance-operating-system-lead`, `data-protection-interface-reviewer`, `security-governance-architect`, `agent-quality-and-safety-reviewer`.

**Minimal output:** AI system entry, data class assumption, human oversight, open handoff questions, decision log entry.

**Stop points:** Final EU AI Act classification, data protection assessment, personal or confidential data, external assurances, management approval.
