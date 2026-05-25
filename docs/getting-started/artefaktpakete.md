<!-- kso:product-relevance
repo-scope: product
classification: getting-started-guidance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Artefaktpakete für den Einstieg

## Zweck

Diese Pakete bündeln vorhandene Templates, Playbooks, Workflows und Leitfäden für kleine Startdurchstiche. Sie sind keine vollständigen Compliance-Programme und erzeugen keine Rechts-, Datenschutz-, Konformitäts- oder Zertifizierungszusage.

Wenn du noch nicht weißt, welches Paket passt, starte mit den [`Anwenderpfaden`](anwenderpfade.md).

## Leseregel

Jedes Paket ist nach Aufwand sortiert:

- **Pflicht in 15 Minuten:** nur diese Artefakte öffnen, wenn du schnell starten willst.
- **Danach:** nutzen, wenn der erste Output steht.
- **Nur bei Bedarf:** ergänzen, wenn Scope, Risiko oder Managementfrage es verlangen.

## Paket 1: NIS2-Minimalstart

**Ziel:** Aus einer Managementfrage einen ersten NIS2-Gap, Evidenzbedarf und Entscheidungspunkt ableiten.

**Pflicht in 15 Minuten:**

1. [`minimaler-nis2-start-in-5-artefakten.md`](minimaler-nis2-start-in-5-artefakten.md)
2. [`../../templates/ki-nutzungsfreigabe-matrix.md`](../../templates/ki-nutzungsfreigabe-matrix.md)
3. [`../../templates/nis2-gap-worksheet.md`](../../templates/nis2-gap-worksheet.md)
4. [`../../templates/decision-log.md`](../../templates/decision-log.md)

**Danach:**

- [`../../templates/evidence-request-list.md`](../../templates/evidence-request-list.md)
- [`../../workflows/nis2-readiness-gap.yaml`](../../workflows/nis2-readiness-gap.yaml)

**Nur bei Bedarf:**

- [`../../templates/compliance-source-register.md`](../../templates/compliance-source-register.md)
- [`../../playbooks/nis2-readiness-startworkshop.md`](../../playbooks/nis2-readiness-startworkshop.md)

**Passende Agenten:** `nis2-scope-precheck-analyst`, `nis2-readiness-analyst`, `compliance-operating-system-lead`.

**Minimaler Output:** Managementfrage, eine Quelle/Referenz, ein Gap, bis zu drei Evidence Requests, ein Human-Gate-Handoff.

**Stop-Punkte:** Betroffenheits- oder Rechtsauslegung, externe Kommunikation, echte Kundendaten, vertrauliche Vertragsinhalte, Managemententscheidung.

## Paket 2: ISMS-Minimalstart

**Ziel:** Ein Minimum Viable ISMS als Rollen-, Risiko-, Maßnahmen- und Review-Routine starten.

**Pflicht in 15 Minuten:**

1. [`../../examples/fiktiver-mittelstand/isms-90-minuten-durchstich.md`](../../examples/fiktiver-mittelstand/isms-90-minuten-durchstich.md)
2. [`../../templates/isms-scope-canvas.md`](../../templates/isms-scope-canvas.md)
3. [`../../templates/rollenmatrix.md`](../../templates/rollenmatrix.md)
4. [`../../templates/risikoregister-starter.md`](../../templates/risikoregister-starter.md)

**Danach:**

- [`../../implementierungsleitfaeden/isms/01-kontext-scope-und-betroffenheit.md`](../../implementierungsleitfaeden/isms/01-kontext-scope-und-betroffenheit.md)
- [`../../implementierungsleitfaeden/isms/02-rollen-verantwortung-und-managementauftrag.md`](../../implementierungsleitfaeden/isms/02-rollen-verantwortung-und-managementauftrag.md)
- [`../../implementierungsleitfaeden/isms/03-risikosteuerung-und-massnahmenplanung.md`](../../implementierungsleitfaeden/isms/03-risikosteuerung-und-massnahmenplanung.md)
- [`../../templates/soa-risk-control-map.md`](../../templates/soa-risk-control-map.md)

**Nur bei Bedarf:**

- [`../../implementierungsleitfaeden/isms/00-nutzung-und-grenzen.md`](../../implementierungsleitfaeden/isms/00-nutzung-und-grenzen.md)
- [`../../workflows/minimum-viable-isms.yaml`](../../workflows/minimum-viable-isms.yaml)
- [`../../playbooks/minimum-viable-isms-setup.md`](../../playbooks/minimum-viable-isms-setup.md)

**Passende Agenten:** `isms-operating-model-designer`, `security-governance-architect`, `risk-and-obligation-prioritizer`.

**Minimaler Output:** Scope-Satz, Rollenannahme, drei Risiken, drei Maßnahmenroutinen, ein Reviewtermin, ein Entscheidungspunkt.

**Stop-Punkte:** Scope-Freigabe, Risikoakzeptanz, Zertifizierungs-/Audit-Auslegung, Ressourcenentscheidung, vertrauliche Inhalte ohne Freigabe.

## Paket 3: Incident-/Melde-Readiness

**Ziel:** Eskalation und Melde-Triage üben, ohne echte Vorfälle oder personenbezogene Daten in öffentliche Beispiele zu übernehmen.

**Pflicht in 15 Minuten:**

1. [`../../templates/incident-escalation-card.md`](../../templates/incident-escalation-card.md)
2. [`../../templates/nis2-incident-melde-triage.md`](../../templates/nis2-incident-melde-triage.md)
3. [`../../templates/legal-datenschutz-handoff.md`](../../templates/legal-datenschutz-handoff.md)

**Danach:**

- [`../../playbooks/incident-escalation-first-assessment.md`](../../playbooks/incident-escalation-first-assessment.md)
- [`../../playbooks/nis2-incident-melde-triage.md`](../../playbooks/nis2-incident-melde-triage.md)
- [`../../templates/corrective-action-plan.md`](../../templates/corrective-action-plan.md)

**Nur bei Bedarf:**

- [`../../workflows/nis2-incident-and-management-readiness.yaml`](../../workflows/nis2-incident-and-management-readiness.yaml)
- [`../../playbooks/tabletop-ransomware.md`](../../playbooks/tabletop-ransomware.md)

**Passende Agenten:** `incident-readiness-coach`, `management-review-facilitator`, `agent-quality-and-safety-reviewer`.

**Minimaler Output:** Eskalationskarte, Triage-Entwurf, Human-Gate-Liste, Übungsszenario, erste Korrekturmaßnahmen.

**Stop-Punkte:** Meldepflichtbewertung, Datenschutzbewertung, Rechtsauslegung, Kommunikation an Behörden/Kunden/Öffentlichkeit, Krisenstabsentscheidung.
## Paket 5: EU-AI-Act-Readiness-Starter

**Ziel:** KI-Systeme und KI-Use-Cases sichtbar machen, ohne eine finale rechtliche oder datenschutzrechtliche Bewertung zu behaupten.

**Pflicht in 15 Minuten:**

1. [`eu-ai-act-readiness-start.md`](eu-ai-act-readiness-start.md)
2. [`../../templates/ki-nutzungsfreigabe-matrix.md`](../../templates/ki-nutzungsfreigabe-matrix.md)
3. [`../../templates/ki-system-inventar-und-risikovorpruefung.md`](../../templates/ki-system-inventar-und-risikovorpruefung.md)
4. [`../../templates/decision-log.md`](../../templates/decision-log.md)

**Danach:**

- [`../../templates/legal-datenschutz-handoff.md`](../../templates/legal-datenschutz-handoff.md)
- [`../../workflows/eu-ai-act-readiness-precheck.yaml`](../../workflows/eu-ai-act-readiness-precheck.yaml)

**Nur bei Bedarf:**

- [`../../07-ai-governance-agents/human-in-the-loop.md`](../../07-ai-governance-agents/human-in-the-loop.md)
- [`../../07-ai-governance-agents/risk-and-limits.md`](../../07-ai-governance-agents/risk-and-limits.md)
- [`../../knowledge/hardwired-sources.yaml`](../../knowledge/hardwired-sources.yaml)

**Passende Agenten:** `compliance-operating-system-lead`, `data-protection-interface-reviewer`, `security-governance-architect`, `agent-quality-and-safety-reviewer`.

**Minimaler Output:** KI-Systemeintrag, Datenklassenannahme, menschliche Aufsicht, offene Handoff-Fragen, Decision-Log-Eintrag.

**Stop-Punkte:** finale EU-AI-Act-Einordnung, Datenschutzbewertung, personenbezogene oder vertrauliche Daten, externe Zusagen, Managementfreigabe.
