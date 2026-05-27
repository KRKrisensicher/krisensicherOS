# User paths for the first krisensicherOS walkthrough

## Purpose

These paths help you use existing artifacts in a targeted way. They do not replace legal advice, data protection advice, compliance assessment, certification assurance, or a management decision.

Before each path: check AI usage approval, data class, permitted environment, and human gates. If no approval exists, prepare only the approval with `../../templates/ki-nutzungsfreigabe-matrix.md` (`../../07-ai-governance-agents/templates/ki-nutzungsfreigabe-matrix.md`).

## Path 1: Start NIS2

**When to use:** When management, CISO/information security officer, or GRC needs an initial NIS2 working assumption, gap view, and decision question.

**Existing artifacts:**

- `minimaler-nis2-start-in-5-artefakten.md` (`minimaler-nis2-start-in-5-artefakten.md`)
- `../../templates/nis2-vorab-betroffenheitspruefung-fragebogen.md` (`../../03-nis2-readiness/templates/nis2-vorab-betroffenheitspruefung-fragebogen.md`)
- `../../templates/compliance-source-register.md` (`../../08-templates-playbooks/templates/compliance-source-register.md`)
- `../../templates/nis2-gap-worksheet.md` (`../../03-nis2-readiness/templates/nis2-gap-worksheet.md`)
- `../../templates/evidence-request-list.md` (`../../06-evidence-management-review/templates/evidence-request-list.md`)
- `../../workflows/nis2-readiness-gap.yaml` (`../../03-nis2-readiness/workflows/nis2-readiness-gap.yaml`)
- `../../playbooks/nis2-readiness-startworkshop.md` (`../../03-nis2-readiness/playbooks/nis2-readiness-startworkshop.md`)

**Start agents:** `nis2-scope-precheck-analyst`, then `nis2-readiness-analyst`; for orchestration, `compliance-operating-system-lead`.

**After 15 minutes you should have:** clarified AI usage approval/data class, one management question, and a marked human gate point.

**60–90-minute result:** A working assumption on scope, one register entry, one NIS2 gap, no more than three evidence requests, and a decision log handoff.

**Human gates:** Legal interpretation, applicability, risk acceptance, management decision, external communication.

**Next step:** Clarify evidence requests with owners or transfer them into `../../workflows/evidence-management-review.yaml` (`../../06-evidence-management-review/workflows/evidence-management-review.yaml`).

## Path 2: Start ISMS

**When to use:** When a small, operable ISMS baseline should be built without immediately creating full document landscapes.

**Existing artifacts:**

- `../../04-isms-basics/implementation-guides/isms/README.md` (`../../04-isms-basics/implementation-guides/isms/README.md`)
- `../../04-isms-basics/implementation-guides/isms/01-kontext-scope-und-betroffenheit.md` (`../../04-isms-basics/implementation-guides/isms/01-kontext-scope-und-betroffenheit.md`)
- `../../04-isms-basics/implementation-guides/isms/02-rollen-verantwortung-und-managementauftrag.md` (`../../04-isms-basics/implementation-guides/isms/02-rollen-verantwortung-und-managementauftrag.md`)
- `../../04-isms-basics/implementation-guides/isms/03-risikosteuerung-und-massnahmenplanung.md` (`../../04-isms-basics/implementation-guides/isms/03-risikosteuerung-und-massnahmenplanung.md`)
- `../../templates/isms-scope-canvas.md` (`../../04-isms-basics/templates/isms-scope-canvas.md`)
- `../../templates/risikoregister-starter.md` (`../../04-isms-basics/templates/risikoregister-starter.md`)
- `../../templates/soa-risk-control-map.md` (`../../04-isms-basics/templates/soa-risk-control-map.md`)
- `../../workflows/minimum-viable-isms.yaml` (`../../04-isms-basics/workflows/minimum-viable-isms.yaml`)
- `../../playbooks/minimum-viable-isms-setup.md` (`../../04-isms-basics/playbooks/minimum-viable-isms-setup.md`)

**Start agents:** `isms-operating-model-designer`, for role/routine questions `security-governance-architect`, for prioritization `risk-and-obligation-prioritizer`.

**After 15 minutes you should have:** one scope statement, one proposed ISMS owner, and the three most important open decisions.

**60–90-minute result:** One scope statement, three starting risks, three control routines, an owner/review model, and a first management decision point.

**Human gates:** Scope approval, risk acceptance, control prioritization, resource decision, ISO/audit interpretation.

**Next step:** Use the example `../../09-implementation-roadmaps/examples/fiktiver-mittelstand/isms-90-minuten-durchstich.md` (`../../09-implementation-roadmaps/examples/fiktiver-mittelstand/isms-90-minuten-durchstich.md`) as a pattern and transfer your own artifacts into templates.

## Path 3: Build evidence/management review

**When to use:** When analysis results, controls, or evidence must be transferred into a management review basis that supports decision readiness.

**Existing artifacts:**

- `../../templates/evidence-pack-index.md` (`../../06-evidence-management-review/templates/evidence-pack-index.md`)
- `../../templates/management-review-agenda.md` (`../../06-evidence-management-review/templates/management-review-agenda.md`)
- `../../templates/decision-log.md` (`../../02-governance-operating-model/templates/decision-log.md`)
- `../../templates/control-evidence-map.md` (`../../06-evidence-management-review/templates/control-evidence-map.md`)
- `../../workflows/evidence-management-review.yaml` (`../../06-evidence-management-review/workflows/evidence-management-review.yaml`)
- `../../playbooks/evidence-pack-prep.md` (`../../06-evidence-management-review/playbooks/evidence-pack-prep.md`)
- `../../playbooks/management-review-prep.md` (`../../06-evidence-management-review/playbooks/management-review-prep.md`)

**Start agents:** `control-evidence-architect`, `evidence-pack-reviewer`, `management-review-facilitator`.

**After 15 minutes you should have:** one decision question, one existing evidence source, and one clear evidence gap.

**60–90-minute result:** Evidence pack index, open evidence gaps, review agenda, decision log entry, and clear owner questions.

**Human gates:** Management decision, residual risk, resources, external commitments, confidential evidence approval.

**Next step:** Start a monthly routine with `../../playbooks/monthly-security-governance-review.md` (`../../06-evidence-management-review/playbooks/monthly-security-governance-review.md`).

## Path 4: Practice incident/notification readiness

**When to use:** When escalation, notification triage, management involvement, or tabletop capability should be practiced.

**Existing artifacts:**

- `../../templates/incident-escalation-card.md` (`../../05-incident-crisis-readiness/templates/incident-escalation-card.md`)
- `../../templates/nis2-incident-melde-triage.md` (`../../03-nis2-readiness/templates/nis2-incident-melde-triage.md`)
- `../../templates/legal-datenschutz-handoff.md` (`../../02-governance-operating-model/templates/legal-datenschutz-handoff.md`)
- `../../workflows/nis2-incident-and-management-readiness.yaml` (`../../05-incident-crisis-readiness/workflows/nis2-incident-and-management-readiness.yaml`)
- `../../playbooks/incident-escalation-first-assessment.md` (`../../05-incident-crisis-readiness/playbooks/incident-escalation-first-assessment.md`)
- `../../playbooks/nis2-incident-melde-triage.md` (`../../03-nis2-readiness/playbooks/nis2-incident-melde-triage.md`)
- `../../playbooks/tabletop-ransomware.md` (`../../05-incident-crisis-readiness/playbooks/tabletop-ransomware.md`)

**Start agents:** `incident-readiness-coach`, for management involvement `management-review-facilitator`, for quality/claim risk `agent-quality-and-safety-reviewer`.

**After 15 minutes you should have:** a fictional scenario, an incident owner, and marked legal/data protection handoffs.

**60–90-minute result:** Escalation card, notification triage draft, open legal/data protection handoffs, exercise assumptions, and lessons-learned logic.

**Human gates:** Notification obligation assessment, data protection assessment, legal interpretation, external communication, crisis team decision.

**Next step:** Schedule a tabletop exercise and transfer results into the decision log, corrective actions, and management review.
## Path 5: Start EU AI Act readiness

**When to use:** When AI systems, AI functions, or AI use cases should be made visible and prepared as a governance question.

**Existing artifacts:**

- `eu-ai-act-readiness-start.md` (`eu-ai-act-readiness-start.md`)
- `../../templates/ki-nutzungsfreigabe-matrix.md` (`../../07-ai-governance-agents/templates/ki-nutzungsfreigabe-matrix.md`)
- `../../templates/ki-system-inventar-und-risikovorpruefung.md` (`../../07-ai-governance-agents/templates/ki-system-inventar-und-risikovorpruefung.md`)
- `../../templates/legal-datenschutz-handoff.md` (`../../02-governance-operating-model/templates/legal-datenschutz-handoff.md`)
- `../../templates/decision-log.md` (`../../02-governance-operating-model/templates/decision-log.md`)
- `../../workflows/eu-ai-act-readiness-precheck.yaml` (`../../07-ai-governance-agents/workflows/eu-ai-act-readiness-precheck.yaml`)

**Start agents:** `compliance-operating-system-lead`, for data protection questions `data-protection-interface-reviewer`, for operating logic `security-governance-architect`, for quality `agent-quality-and-safety-reviewer`.

**After 15 minutes you should have:** an AI system or use case entry, data class assumption, owner, open legal/data protection/management questions, and a next review date.

**60–90-minute result:** AI system inventory, risk signals, oversight/logging assumptions, handoff package, and decision log entry.

**Human gates:** EU AI Act role or risk classification, data protection assessment, provider/contract questions, management approval, external commitments.

**Next step:** Clarify handoff questions with Legal, Data Protection, IT/Security, and Management; then document approval, restriction, or non-use.
