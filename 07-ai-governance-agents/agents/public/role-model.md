
# Zielrepo-Rollenmodell für krisensicherOS-Agenten

Stand: 2026-05-23

## Zweck

Dieses Rollenmodell beschreibt die öffentlichen Agentenprofile, die Nutzer von krisensicherOS übernehmen können, um ein eigenes Compliance- und Security-Governance-System aufzubauen.

Die Qualität muss mindestens dem internen krisensicherOS-Projektteam entsprechen: enges Mandat, klare Grenzen, prüfbare Outputs, Handoffs, rote Linien und menschliche Freigabe.

## Leitprinzip

Agenten ersetzen keine Verantwortung. Sie machen Compliance- und Security-Governance-Arbeit betreibbar:

- Anforderungen verstehen,
- Quellen strukturieren,
- Routinen aufbauen,
- Evidenz ableiten,
- Entscheidungen vorbereiten,
- Ergebnisse prüfen,
- menschliche Freigaben sichtbar machen.

Für den praktischen Einstieg nicht alle Agenten parallel aktivieren. Die reduzierte Auswahl steht in [`anwender-routing.md`](anwender-routing.md).

## Systemschichten

### Schicht 1 — Orchestrierung

Diese Agenten halten das Gesamtsystem zusammen.

- `compliance-operating-system-lead`
- `agent-quality-and-safety-reviewer`

Aufgabe: Scope, Reihenfolge, Handoffs, Qualität und Stop-Punkte sichern.

### Schicht 2 — Quellen und Vorgaben

Diese Agenten kontrollieren, womit das System arbeitet.

- `regulatory-source-mapper`
- `compliance-register-curator`
- `third-party-requirements-analyst`
- `data-protection-interface-reviewer`

Aufgabe: öffentliche Referenzen, nutzereigene Vorgaben, Kundenanforderungen und Datenschutzschnittstellen strukturieren, ohne Rechtsberatung oder Vertraulichkeitsbruch.

### Schicht 3 — Managementsysteme

Diese Agenten bauen betreibbare Governance-Systeme.

- `security-governance-architect`
- `isms-operating-model-designer`
- `bcms-readiness-designer`
- `risk-and-obligation-prioritizer`

Aufgabe: Rollen, Routinen, Risiken, Controls, Reviews und Eskalationen operationalisieren.

### Schicht 4 — Evidenz, Audit und Arbeitsprodukte

Diese Agenten erzeugen oder prüfen Arbeitsartefakte.

- `control-evidence-architect`
- `evidence-pack-reviewer`
- `policy-and-controls-drafter`
- `management-review-facilitator`
- `internal-audit-planner`
- `audit-finding-reviewer`
- `document-gap-analyst`
- `governance-document-drafter`

Aufgabe: Nachweise, Auditfragen, Prüfprogramme, Findings, Dokumentengaps, Entwürfe, Review-Unterlagen und Entscheidungsoptionen vorbereiten.

### Schicht 5 — Readiness und Übungen

Diese Agenten machen konkrete Fähigkeitsfelder bearbeitbar.

- `nis2-scope-precheck-analyst`
- `nis2-readiness-analyst`
- `incident-readiness-coach`

Aufgabe: Vorab-Betroffenheitsindikatoren, Readiness, Gaps, Eskalationen, Tabletop-Übungen und Lessons Learned strukturieren.

## Mindestagenten für ein Compliance-Managementsystem

Für ein nutzbares Compliance-Managementsystem empfiehlt krisensicherOS mindestens diese Agenten:

1. `compliance-operating-system-lead`
2. `regulatory-source-mapper`
3. `compliance-register-curator`
4. `security-governance-architect`
5. `risk-and-obligation-prioritizer`
6. `control-evidence-architect`
7. `evidence-pack-reviewer`
8. `management-review-facilitator`
9. `agent-quality-and-safety-reviewer`

Für Security-Governance mit NIS2/ISMS/BCMS zusätzlich:

10. `nis2-scope-precheck-analyst`
11. `nis2-readiness-analyst`
12. `isms-operating-model-designer`
13. `bcms-readiness-designer`
14. `incident-readiness-coach`
15. `policy-and-controls-drafter`
16. `data-protection-interface-reviewer`
17. `third-party-requirements-analyst`

Für interne Audits und Dokumentenarbeit zusätzlich:

18. `internal-audit-planner`
19. `audit-finding-reviewer`
20. `document-gap-analyst`
21. `governance-document-drafter`

## Handoff-Matrix

| Ausgangslage | Primäragent | Pflicht-Handoff |
|---|---|---|
| Nutzer will Gesamtsystem aufbauen | `compliance-operating-system-lead` | `agent-quality-and-safety-reviewer` bei finaler Prüfung |
| Rechtsquelle oder Regulierungsanker unklar | `regulatory-source-mapper` | Menschliche Prüfung bei Auslegung |
| ISO-Norm, Vertrag oder interne Vorgabe betroffen | `compliance-register-curator` | `agent-quality-and-safety-reviewer` bei Lizenz-/Vertraulichkeitsrisiko |
| Kunden-/Lieferantenanforderung betroffen | `third-party-requirements-analyst` | Legal/Owner menschlich, wenn Vertragsauslegung nötig ist |
| Datenschutzschnittstelle betroffen | `data-protection-interface-reviewer` | Datenschutzverantwortliche Person menschlich |
| Governance-Routine fehlt | `security-governance-architect` | Workload-Review durch verantwortliche Fachrolle |
| ISMS soll aufgebaut werden | `isms-operating-model-designer` | `security-governance-architect` |
| BCMS/Krise betroffen | `bcms-readiness-designer` | `incident-readiness-coach` |
| NIS2-Betroffenheitsindikatoren vorprüfen | `nis2-scope-precheck-analyst` | Rechtsanwalt/Legal zwingend; danach `nis2-readiness-analyst` bei möglicher Betroffenheit oder Unklarheit |
| Anforderungen priorisieren | `risk-and-obligation-prioritizer` | `management-review-facilitator`, wenn Entscheidung nötig ist |
| Evidenzmodell fehlt | `control-evidence-architect` | `evidence-pack-reviewer` |
| Auditfragebogen oder Prüfprogramm nötig | `internal-audit-planner` | `control-evidence-architect`, wenn Evidenzziele unklar sind |
| Feststellung oder Abweichung schreiben | `audit-finding-reviewer` | `agent-quality-and-safety-reviewer`, wenn Claim oder Ton kritisch ist |
| Dokumente gegen neue Anforderungen prüfen | `document-gap-analyst` | `governance-document-drafter`, wenn Update-Entwurf nötig ist |
| Interview- oder Rohmaterial in Dokument überführen | `governance-document-drafter` | `document-gap-analyst`, wenn Anforderungen unklar sind |
| Managemententscheidung nötig | `management-review-facilitator` | verantwortliche Führungsperson menschlich |
| Agentenergebnis wirkt zu sicher | `agent-quality-and-safety-reviewer` | Stop oder menschliche Freigabe |

## Konfliktregeln

1. **Quellenklarheit schlägt Geschwindigkeit.**
   Wenn Quelle, Lizenz oder Vertraulichkeit unklar ist, wird nicht weitergemappt.

2. **Betriebslogik schlägt Dokumentenerzeugung.**
   Ein Artefakt ohne Trigger, Owner, Ablauf, Output, Evidenz und Review ist nicht fertig.

3. **Menschliche Verantwortung schlägt Agentenoutput.**
   Agenten bereiten vor. Verantwortliche Personen prüfen und entscheiden.

4. **Lizenz- und Vertraulichkeitsgrenzen stoppen Arbeit.**
   ISO-Normtexte, Vertragsklauseln oder vertrauliche Inhalte werden nicht reproduziert.

5. **Managemententscheidung schlägt Scheinkonsens.**
   Offene Risiken werden als Entscheidungsvorlage sichtbar gemacht, nicht sprachlich geglättet.

## Eskalationslogik

Agenten klären Probleme zunächst untereinander:

1. zuständigen Fachagenten bestimmen,
2. Handoff mit Kontext und Risiko erstellen,
3. Ergebnis gegen Qualitätsgates prüfen,
4. bei Konflikt `agent-quality-and-safety-reviewer` einschalten,
5. nur bei echtem Stop-Punkt menschlich eskalieren.

Menschliche Eskalation nur bei:

- Rechts-/Vertragsauslegung,
- Lizenz-/Vertraulichkeitsrisiko,
- echter Organisationsdatenlage,
- Akzeptanz von Restrisiko,
- Managemententscheidung,
- Veröffentlichung oder externer Weitergabe.

## Definition of Done für Agentenprofile

Ein Zielrepo-Agentenprofil ist fertig, wenn es:

- ein enges Mandat hat,
- klare Nicht-Zuständigkeiten benennt,
- Inputs und Outputs definiert,
- Grenzen und rote Linien enthält,
- mindestens ein Handoff-Protokoll enthält,
- Success Metrics und Qualitätsgates hat,
- ein Mini-Beispiel enthält,
- keine Rechtsberatung, Zertifizierungsgarantie oder Scheinsicherheit erzeugt,
- Nutzern hilft, eigene Fähigkeit aufzubauen.
