<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Agentenprofile

Dieser Ordner enthält die öffentlichen Agentenprofile für krisensicherOS.

## Zweck

Die Agentenprofile beschreiben Rollen für KI-unterstützte Security Governance. Sie sind keine Ersatzverantwortlichen, sondern Arbeitsrollen für Strukturierung, Analyse, Evidenzfluss, Review und Handoff.

## Öffentliche Nutzeragenten v1.0

Die öffentlichen Nutzeragenten liegen unter [`07-ai-governance-agents/agents/public/`](public/). Sie bilden ein Rollenmodell für Organisationen, die mit krisensicherOS ein eigenes Compliance- und Security-Governance-Agentensystem aufbauen wollen.

Orchestrierung:

- `compliance-operating-system-lead`
- `agent-quality-and-safety-reviewer`

Quellen und Register:

- `regulatory-source-mapper`
- `compliance-register-curator`
- `third-party-requirements-analyst`
- `data-protection-interface-reviewer`

Managementsysteme und Governance:

- `security-governance-architect`
- `isms-operating-model-designer`
- `bcms-readiness-designer`
- `risk-and-obligation-prioritizer`

Evidenz und Reviews:

- `control-evidence-architect`
- `evidence-pack-reviewer`
- `policy-and-controls-drafter`
- `management-review-facilitator`

Readiness und Übungen:

- `nis2-readiness-analyst`
- `incident-readiness-coach`

Für den Einstieg mit wenigen Rollen siehe [`07-ai-governance-agents/agents/public/anwender-routing.md`](public/anwender-routing.md). Das vollständige Rollenmodell steht in [`07-ai-governance-agents/agents/public/role-model.md`](public/role-model.md) und das Routingmanifest in [`07-ai-governance-agents/agents/manifest.yaml`](manifest.yaml).

## Qualitätsregel für alle Agenten

Jeder Agent muss sichtbar machen:

- welche Entscheidung oder Routine unterstützt wird,
- welche Eingangsdaten fehlen oder unsicher sind,
- welche Annahmen getroffen wurden,
- welche menschliche Rolle prüfen oder freigeben muss,
- welche Evidenz oder welches Arbeitsartefakt entsteht.

Agenten entlasten, strukturieren und prüfen. Sie ersetzen keine Verantwortungsübernahme.
