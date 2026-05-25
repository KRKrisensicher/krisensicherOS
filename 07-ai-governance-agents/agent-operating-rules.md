<!-- kso:product-relevance
repo-scope: product
classification: product-module
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Agent Operating Rules

## Zweck

Diese Regeln beschreiben, wie Organisationen die krisensicherOS-Agenten kontrolliert betreiben: toolneutral, public-safe, mit klaren Rollen, Handoffs und Qualitätsgates.

## 1. Agenten auswählen

Starte klein. Für einen ersten krisensicherOS-Betrieb genügen meist wenige Rollenprofile:

1. `compliance-operating-system-lead`
2. `regulatory-source-mapper`
3. `compliance-register-curator`
4. `security-governance-architect`
5. `risk-and-obligation-prioritizer`
6. `control-evidence-architect`
7. `evidence-pack-reviewer`
8. `management-review-facilitator`
9. `agent-quality-and-safety-reviewer`

Erweitere nur, wenn der Bedarf klar ist:

- NIS2: `nis2-readiness-analyst`
- ISMS: `isms-operating-model-designer`
- BCMS: `bcms-readiness-designer`
- Incident/Tabletop: `incident-readiness-coach`
- Policies/Controls: `policy-and-controls-drafter`
- Datenschutzschnittstellen: `data-protection-interface-reviewer`
- Dritte/Kunden/Lieferanten: `third-party-requirements-analyst`

## 2. Arbeitsauftrag formulieren

Jeder Agentenauftrag enthält:

- Ziel
- Scope und Nicht-Scope
- erlaubte Quellen und Daten
- erwarteter Output
- relevante Templates, Skills oder Workflows
- menschlicher Owner
- Stop-Punkte
- gewünschtes Quality Gate

## 3. Daten- und Quellenregel

Agenten dürfen nutzen:

- öffentliche Quellen als Referenzanker,
- eigene Zusammenfassungen,
- Metadaten aus Registern,
- fiktive Beispiele,
- redigierte interne Informationen in privaten Nutzerumgebungen.

Agenten dürfen nicht in öffentliche Artefakte übernehmen:

- echte Kundendaten,
- personenbezogene Daten,
- vertrauliche Vertragsinhalte,
- lizenzpflichtige Normtexte,
- Secrets oder Zugangsdaten,
- private Runtime- oder Workspace-Details.

## 4. Handoff-Regel

Ein Handoff ist nötig, wenn:

- eine andere Fachrolle zuständig ist,
- ein Ergebnis reviewed werden muss,
- eine Entscheidung vorbereitet wird,
- Grenzen oder Claims kritisch werden,
- Evidenz oder Quellen unklar sind.

Handoff-Format:

```text
Ausgangslage:
Scope:
Bisheriger Output:
Offene Frage:
Risiko / Grenze:
Benötigter nächster Agent oder menschliche Rolle:
Gewünschter Output:
```

## 5. Review-Regel

Jeder relevante Output wird gegen passende Gates geprüft:

- Public-Safety,
- Claim-Safety,
- Betriebslogik,
- Empowerment,
- Workload,
- Portabilität,
- artefaktspezifisches Gate aus `evals/quality-gates.md`.

## 6. Arbeitsweise in Tools

Die Fachlogik bleibt kanonisch in:

- `agents/public/`,
- `skills/`,
- `templates/`,
- `playbooks/`,
- `workflows/`,
- `evals/`.

Tooladapter für Claude, Codex, OpenClaw, Hermes oder andere Systeme sollen diese Fachlogik nur umsetzen, nicht verändern.

## 7. Eskalationsregel

Agenten lösen interne Fachfragen zuerst durch Handoffs und Quality Review. Menschen werden nur eingeschaltet, wenn ein echter Stop-Punkt erreicht ist:

- Rechts-/Datenschutzbewertung,
- Vertragsauslegung,
- Risikoakzeptanz,
- Managemententscheidung,
- externe Kommunikation,
- Veröffentlichung,
- Lizenz- oder Vertraulichkeitsfrage.

## Definition of Done

Agentenarbeit ist sauber betrieben, wenn:

- Auftrag und Scope klar sind,
- zulässige Quellen und Daten definiert sind,
- passender Agent, Skill, Template oder Workflow gewählt wurde,
- Human Gates sichtbar sind,
- Qualitätsgates bestanden oder Stop-Punkte markiert sind,
- Ergebnis und Handoff nachvollziehbar dokumentiert sind.
