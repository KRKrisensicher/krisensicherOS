
# Anwenderpfade für den ersten krisensicherOS-Durchstich

## Zweck

Diese Pfade helfen, vorhandene Artefakte gezielt zu nutzen. Sie ersetzen keine Rechtsberatung, Datenschutzberatung, Konformitätsbewertung, Zertifizierungszusage oder Managemententscheidung.

Vor jedem Pfad: KI-Freigabe, Datenklasse, erlaubte Umgebung und Human Gates prüfen. Wenn keine Freigabe vorliegt, nur die Freigabe mit [`../../templates/ki-nutzungsfreigabe-matrix.md`](../../../08-templates-playbooks/templates/ki-nutzungsfreigabe-matrix.md) vorbereiten.

## Pfad 1: NIS2 starten

**Wann nutzen:** Wenn Management, CISO/ISB oder GRC eine erste NIS2-Arbeitsannahme, Gap-Sicht und Entscheidungsfrage brauchen.

**Vorhandene Artefakte:**

- [`minimaler-nis2-start-in-5-artefakten.md`](minimaler-nis2-start-in-5-artefakten.md)
- [`../../templates/nis2-vorab-betroffenheitspruefung-fragebogen.md`](../../../08-templates-playbooks/templates/nis2-vorab-betroffenheitspruefung-fragebogen.md)
- [`../../templates/compliance-source-register.md`](../../../08-templates-playbooks/templates/compliance-source-register.md)
- [`../../templates/nis2-gap-worksheet.md`](../../../08-templates-playbooks/templates/nis2-gap-worksheet.md)
- [`../../templates/evidence-request-list.md`](../../../08-templates-playbooks/templates/evidence-request-list.md)
- [`../../workflows/nis2-readiness-gap.yaml`](../../../08-templates-playbooks/workflows/nis2-readiness-gap.yaml)
- [`../../playbooks/nis2-readiness-startworkshop.md`](../../../08-templates-playbooks/playbooks/nis2-readiness-startworkshop.md)

**Startagenten:** `nis2-scope-precheck-analyst`, danach `nis2-readiness-analyst`; bei Orchestrierung `compliance-operating-system-lead`.

**Nach 15 Minuten solltest du haben:** geklärte KI-Freigabe/Datenklasse, eine Managementfrage und einen markierten Human-Gate-Punkt.

**60–90-Minuten-Ergebnis:** Eine Arbeitsannahme zum Scope, ein Registereintrag, ein NIS2-Gap, maximal drei Evidence Requests und ein Decision-Log-Handoff.

**Human Gates:** Rechtsauslegung, Betroffenheit, Risikoakzeptanz, Managemententscheidung, externe Kommunikation.

**Nächster Schritt:** Evidence Requests mit Ownern klären oder in [`../../workflows/evidence-management-review.yaml`](../../../08-templates-playbooks/workflows/evidence-management-review.yaml) überführen.

## Pfad 2: ISMS starten

**Wann nutzen:** Wenn ein kleines, betreibbares ISMS-Grundsystem aufgebaut werden soll, ohne sofort vollständige Dokumentenlandschaften zu erzeugen.

**Vorhandene Artefakte:**

- [`../../implementierungsleitfaeden/isms/README.md`](../../../04-isms-basics/implementation-guides/README.md)
- [`../../implementierungsleitfaeden/isms/01-kontext-scope-und-betroffenheit.md`](../../../04-isms-basics/implementation-guides/01-kontext-scope-und-betroffenheit.md)
- [`../../implementierungsleitfaeden/isms/02-rollen-verantwortung-und-managementauftrag.md`](../../../04-isms-basics/implementation-guides/02-rollen-verantwortung-und-managementauftrag.md)
- [`../../implementierungsleitfaeden/isms/03-risikosteuerung-und-massnahmenplanung.md`](../../../04-isms-basics/implementation-guides/03-risikosteuerung-und-massnahmenplanung.md)
- [`../../templates/isms-scope-canvas.md`](../../../08-templates-playbooks/templates/isms-scope-canvas.md)
- [`../../templates/risikoregister-starter.md`](../../../08-templates-playbooks/templates/risikoregister-starter.md)
- [`../../templates/soa-risk-control-map.md`](../../../08-templates-playbooks/templates/soa-risk-control-map.md)
- [`../../workflows/minimum-viable-isms.yaml`](../../../08-templates-playbooks/workflows/minimum-viable-isms.yaml)
- [`../../playbooks/minimum-viable-isms-setup.md`](../../../08-templates-playbooks/playbooks/minimum-viable-isms-setup.md)

**Startagenten:** `isms-operating-model-designer`, bei Rollen-/Routinefragen `security-governance-architect`, bei Priorisierung `risk-and-obligation-prioritizer`.

**Nach 15 Minuten solltest du haben:** einen Scope-Satz, einen ISMS-Owner-Vorschlag und die drei wichtigsten offenen Entscheidungen.

**60–90-Minuten-Ergebnis:** Ein Scope-Satz, drei Start-Risiken, drei Maßnahmenroutinen, ein Owner-/Review-Modell und ein erster Managemententscheidungspunkt.

**Human Gates:** Scope-Freigabe, Risikoakzeptanz, Maßnahmenpriorisierung, Ressourcenentscheidung, ISO-/Audit-Auslegung.

**Nächster Schritt:** Beispiel [`../../examples/fiktiver-mittelstand/isms-90-minuten-durchstich.md`](../../examples/fictional-midmarket/isms-90-minuten-durchstich.md) als Muster nutzen und eigene Artefakte in Templates übertragen.

## Pfad 3: Evidence/Management Review aufbauen

**Wann nutzen:** Wenn Analyseergebnisse, Maßnahmen oder Nachweise in eine entscheidungsfähige Management-Review-Grundlage überführt werden müssen.

**Vorhandene Artefakte:**

- [`../../templates/evidence-pack-index.md`](../../../08-templates-playbooks/templates/evidence-pack-index.md)
- [`../../templates/management-review-agenda.md`](../../../08-templates-playbooks/templates/management-review-agenda.md)
- [`../../templates/decision-log.md`](../../../08-templates-playbooks/templates/decision-log.md)
- [`../../templates/control-evidence-map.md`](../../../08-templates-playbooks/templates/control-evidence-map.md)
- [`../../workflows/evidence-management-review.yaml`](../../../08-templates-playbooks/workflows/evidence-management-review.yaml)
- [`../../playbooks/evidence-pack-prep.md`](../../../08-templates-playbooks/playbooks/evidence-pack-prep.md)
- [`../../playbooks/management-review-prep.md`](../../../08-templates-playbooks/playbooks/management-review-prep.md)

**Startagenten:** `control-evidence-architect`, `evidence-pack-reviewer`, `management-review-facilitator`.

**Nach 15 Minuten solltest du haben:** eine Entscheidungsfrage, eine vorhandene Evidenzquelle und eine klare Evidenzlücke.

**60–90-Minuten-Ergebnis:** Evidence-Pack-Index, offene Nachweislücken, Review-Agenda, Decision-Log-Eintrag und klare Owner-Fragen.

**Human Gates:** Managemententscheidung, Restrisiko, Ressourcen, externe Zusagen, vertrauliche Evidenzfreigabe.

**Nächster Schritt:** Monatliche Routine mit [`../../playbooks/monthly-security-governance-review.md`](../../../08-templates-playbooks/playbooks/monthly-security-governance-review.md) starten.

## Pfad 4: Incident-/Melde-Readiness üben

**Wann nutzen:** Wenn Eskalation, Melde-Triage, Managementeinbindung oder Tabletop-Fähigkeit geübt werden soll.

**Vorhandene Artefakte:**

- [`../../templates/incident-escalation-card.md`](../../../08-templates-playbooks/templates/incident-escalation-card.md)
- [`../../templates/nis2-incident-melde-triage.md`](../../../08-templates-playbooks/templates/nis2-incident-melde-triage.md)
- [`../../templates/legal-datenschutz-handoff.md`](../../../08-templates-playbooks/templates/legal-datenschutz-handoff.md)
- [`../../workflows/nis2-incident-and-management-readiness.yaml`](../../../08-templates-playbooks/workflows/nis2-incident-and-management-readiness.yaml)
- [`../../playbooks/incident-escalation-first-assessment.md`](../../../08-templates-playbooks/playbooks/incident-escalation-first-assessment.md)
- [`../../playbooks/nis2-incident-melde-triage.md`](../../../08-templates-playbooks/playbooks/nis2-incident-melde-triage.md)
- [`../../playbooks/tabletop-ransomware.md`](../../../08-templates-playbooks/playbooks/tabletop-ransomware.md)

**Startagenten:** `incident-readiness-coach`, bei Managementeinbindung `management-review-facilitator`, bei Qualitäts-/Claim-Risiko `agent-quality-and-safety-reviewer`.

**Nach 15 Minuten solltest du haben:** ein fiktives Szenario, einen Incident Owner und markierte Legal-/Datenschutz-Handoffs.

**60–90-Minuten-Ergebnis:** Eskalationskarte, Melde-Triage-Entwurf, offene Legal-/Datenschutz-Handoffs, Übungsannahmen und Lessons-Learned-Logik.

**Human Gates:** Meldepflichtbewertung, Datenschutzbewertung, Rechtsauslegung, externe Kommunikation, Krisenstabsentscheidung.

**Nächster Schritt:** Tabletop-Übung terminieren und Ergebnisse in Decision Log, Corrective Actions und Management Review überführen.
## Pfad 5: EU-AI-Act-Readiness starten

**Wann nutzen:** Wenn KI-Systeme, KI-Funktionen oder KI-Use-Cases sichtbar gemacht und als Governance-Frage vorbereitet werden sollen.

**Vorhandene Artefakte:**

- [`eu-ai-act-readiness-start.md`](eu-ai-act-readiness-start.md)
- [`../../templates/ki-nutzungsfreigabe-matrix.md`](../../../08-templates-playbooks/templates/ki-nutzungsfreigabe-matrix.md)
- [`../../templates/ki-system-inventar-und-risikovorpruefung.md`](../../../08-templates-playbooks/templates/ki-system-inventar-und-risikovorpruefung.md)
- [`../../templates/legal-datenschutz-handoff.md`](../../../08-templates-playbooks/templates/legal-datenschutz-handoff.md)
- [`../../templates/decision-log.md`](../../../08-templates-playbooks/templates/decision-log.md)
- [`../../workflows/eu-ai-act-readiness-precheck.yaml`](../../../08-templates-playbooks/workflows/eu-ai-act-readiness-precheck.yaml)

**Startagenten:** `compliance-operating-system-lead`, bei Datenschutzfragen `data-protection-interface-reviewer`, bei Betriebslogik `security-governance-architect`, bei Qualität `agent-quality-and-safety-reviewer`.

**Nach 15 Minuten solltest du haben:** einen KI-System- oder Use-Case-Eintrag, Datenklassenannahme, Owner, offene Legal-/Datenschutz-/Managementfragen und einen nächsten Reviewtermin.

**60–90-Minuten-Ergebnis:** KI-System-Inventar, Risikosignale, Aufsichts-/Logging-Annahmen, Handoff-Paket und Decision-Log-Eintrag.

**Human Gates:** EU-AI-Act-Rollen- oder Risikoklassifizierung, Datenschutzbewertung, Anbieter-/Vertragsfragen, Managementfreigabe, externe Zusagen.

**Nächster Schritt:** Handoff-Fragen mit Legal, Datenschutz, IT/Security und Management klären; danach Freigabe, Einschränkung oder Nichtnutzung dokumentieren.
