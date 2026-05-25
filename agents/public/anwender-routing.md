<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Anwender-Routing: maximal 8 Startagenten

## Zweck

Diese Auswahl hilft beim Einstieg. Nicht alle Agenten gleichzeitig nutzen. Wähle den Agenten, der den nächsten konkreten Arbeitsschritt vorbereitet. Agenten ersetzen keine rechtliche Prüfung, Datenschutzprüfung, Konformitätsbewertung, Zertifizierungsentscheidung oder Managementverantwortung.

## Für skeptische oder stark regulierte Teams

Nutze dieselben Pfade zunächst über Templates, Playbooks und Leitfäden. Beginne bei [`../../docs/getting-started/anwenderpfade.md`](../../docs/getting-started/anwenderpfade.md) und öffne nur die Artefakte aus „Pflicht in 15 Minuten“. Agenten beschleunigen Strukturierung und Review, ersetzen aber keine interne Verantwortung.

Für EU-AI-Act-Readiness starte nicht mit einem neuen Spezialagenten, sondern mit `compliance-operating-system-lead` für Reihenfolge und Handoffs; Datenschutz-, Legal- und Managementfragen bleiben Human Gates.

| Startagent | Wann nutzen | Input | Output | Handoff |
| --- | --- | --- | --- | --- |
| `compliance-operating-system-lead` | Wenn Reihenfolge, Scope oder Gesamtpfad unklar ist | Ziel, Datenklasse, KI-Freigabe, gewünschtes Ergebnis | Arbeitsplan, passende Artefakte, Stop-Punkte | an Fachagenten; finale Prüfung an `agent-quality-and-safety-reviewer` |
| `nis2-scope-precheck-analyst` | Wenn NIS2-Betroffenheit nur vorgeprüft werden soll | öffentliche/freigegebene Organisationsannahmen, Fragebogen | Vorprüfungs-Arbeitsannahme, offene Legal-Fragen | zwingend an Legal/Rechtsprüfung; bei weiterem Start an `nis2-readiness-analyst` |
| `nis2-readiness-analyst` | Wenn NIS2-Gaps und Evidence Requests aufgebaut werden | Registereintrag, Scope, Managementfrage | Gap-Worksheet, Evidenzbedarf, Owner-Fragen | an `control-evidence-architect` oder `management-review-facilitator` |
| `isms-operating-model-designer` | Wenn ein Minimum Viable ISMS gestartet wird | Scope, Risiken, Rollenannahmen, Freigabegrenzen | ISMS-Startmodell mit Routinen, Reviews und Evidenz | an `risk-and-obligation-prioritizer` oder `security-governance-architect` |
| `security-governance-architect` | Wenn Rollen, Trigger, Routinen oder Eskalationen fehlen | Zielroutine, bestehende Arbeitsweise, Owner-Annahmen | Betriebslogik mit Rolle, Ablauf, Evidenz und Review | an `control-evidence-architect` für Nachweise |
| `risk-and-obligation-prioritizer` | Wenn zu viele Risiken, Gaps oder Anforderungen offen sind | Risiko-/Gap-Liste, Wirkung, Aufwand, Fristen | priorisierte Arbeitsliste und Entscheidungsbedarf | an `management-review-facilitator` bei Managemententscheidung |
| `control-evidence-architect` | Wenn Controls/Routinen in Nachweise übersetzt werden müssen | Routine, Control-Annahme, vorhandene Evidenz | Control-Evidence-Map, Evidence Requests | an `evidence-pack-reviewer` |
| `incident-readiness-coach` | Wenn Eskalation, Melde-Triage oder Tabletop geübt werden soll | Szenario, Rollen, Eskalationspfad, Freigabegrenzen | Eskalationskarte, Triage-Entwurf, Übungsfragen | an Legal/Datenschutz/Meldeverantwortliche und `management-review-facilitator` |

## Qualitätsregel

Wenn ein Ergebnis zu sicher klingt, vertrauliche Inhalte berührt oder externe Wirkung entfalten könnte: stoppen, Human Gate markieren und `agent-quality-and-safety-reviewer` für Claim-Safety und Grenzen nutzen.
