
# krisensicherOS in 30 / 60 / 90 Minuten nutzen

Stand: 2026-05-23

## Zweck

Dieser Nutzungspfad verbindet die vorhandenen Agenten, Skills, Templates und Workflows zu einem einfachen Einstieg. Er ist kein neues Fachmodul, sondern Benutzerführung für den ersten belastbaren Durchstich.

## Vor dem Start

Lege fest:

- welcher Bereich betrachtet wird,
- ob nur fiktive/öffentliche oder interne Daten genutzt werden,
- wer fachlich prüft,
- welche KI-Umgebung erlaubt ist,
- ob `templates/ki-nutzungsfreigabe-matrix.md` vollständig genug ist,
- wo Ergebnisse abgelegt werden.

Stop bei Rechtsauslegung, Datenschutzbewertung, Risikoakzeptanz, Managemententscheidung, externem Versand, vertraulichen Inhalten ohne Freigabe oder lizenzpflichtigen Normtexten.

## 30 Minuten: Orientierung und Scope

Ziel: Arbeitsrahmen verstehen und ersten Scope festlegen.

1. `README.md` lesen.
2. Managementfrage formulieren: Welche Entscheidung muss in den nächsten 30 Tagen vorbereitet werden?
2. `docs/setup/ki-setups-bedienungsanleitung.md` auswählen: ChatGPT, M365 Copilot, Claude Code oder lokale KI.
3. `07-ai-governance-agents/agents/public/role-model.md` lesen und passende Rolle wählen:
   - `compliance-operating-system-lead` für Orchestrierung,
   - `nis2-readiness-analyst` für NIS2-Start,
   - `isms-operating-model-designer` für ISMS,
   - `internal-audit-planner` für Audit,
   - `evidence-pack-reviewer` für Evidenz.
4. Erstes Template öffnen:
   - `templates/compliance-source-register.md`,
   - `templates/governance-operating-model-canvas.md`,
   - `templates/nis2-gap-worksheet.md`.

Output nach 30 Minuten:

- Managementfrage für die nächsten 30 Tage,
- Scope-Satz,
- gewählte Agentenrolle,
- erste Quelle / Anforderung / Registerzeile,
- offene Human-Gate-Fragen.

## 60 Minuten: erster NIS2-/ISMS-/Audit-Durchstich

Ziel: Aus einer Anforderung eine betreibbare Governance-Routine machen.

1. Quelle oder Anforderung als Referenz erfassen, nicht als Normtext kopieren.
2. Mit `governance-operating-model` ableiten:
   - Rolle,
   - Trigger,
   - Routine,
   - Entscheidungspunkt,
   - Evidenz.
3. Mit `nis2-gap-assessment` oder `minimum-viable-isms` den Gap dokumentieren.
4. Bei Auditbedarf:
   - `audit-questionnaire-builder`,
   - `audit-test-procedure-mapper`,
   - `evidence-request-list-builder`.
5. Passende Templates füllen:
   - `templates/nis2-gap-worksheet.md`,
   - `templates/audit-questionnaire.md`,
   - `templates/audit-test-program.md`,
   - `templates/evidence-request-list.md`.

Output nach 60 Minuten:

- Gap- oder Auditzeile,
- benötigte Evidenz,
- Owner-Fragen,
- erster Prüf- oder Maßnahmenansatz.

## 90 Minuten: Evidence Pack und Management Review vorbereiten

Ziel: Aus Analyse eine entscheidungsfähige Review-Grundlage machen.

1. Evidenz in `templates/evidence-pack-index.md` strukturieren.
2. Falls Findings entstehen:
   - `audit-finding-writer`,
   - `corrective-action-planner`,
   - `templates/audit-finding-report.md`,
   - `templates/corrective-action-plan.md`.
3. Falls Maßnahmen abgeschlossen sind:
   - `remediation-effectiveness-review`,
   - `templates/remediation-effectiveness-review.md`.
4. Management Review vorbereiten:
   - `management-review-prep`,
   - `templates/management-review-agenda.md`,
   - `templates/decision-log.md`.
5. Qualitätsgates prüfen:
   - Public-Safety,
   - Claim-Safety,
   - Betriebslogik,
   - Human Review,
   - Handoff.

Output nach 90 Minuten:

- Evidence-Pack-Index,
- Maßnahmen- oder Decision-Log-Eintrag,
- Reviewfragen für Management oder Owner,
- nächster Workflow-Schritt.

## Universal-Prompt

```text
Du unterstützt mich mit krisensicherOS.

Nutze nur bereitgestellte oder im Repo vorhandene Inhalte.
Keine Rechtsberatung, Datenschutzberatung, Konformitäts-, Zertifizierungs- oder Sicherheitszusage.
Keine Managemententscheidung.
Markiere Annahmen, Lücken, Evidenzbedarf und Human Gates.

Aufgabe:
Führe mich durch einen 30/60/90-Minuten-Durchstich für diesen Scope: <Scope>.

Output:
1. Welche Datei / welches Template ich öffnen soll.
2. Welche Agentenrolle oder welcher Skill passt.
3. Welche Fragen ich beantworten muss.
4. Welche Evidenz entsteht.
5. Welche Entscheidung beim Menschen bleibt.
```

## Definition of Done

Der erste Durchstich ist abgeschlossen, wenn:

- Scope und Quelle dokumentiert sind,
- mindestens ein Template befüllt ist,
- Evidenzbedarf und Owner sichtbar sind,
- Human Gates markiert sind,
- nächster Schritt in Audit, Evidence Pack oder Management Review klar ist.
