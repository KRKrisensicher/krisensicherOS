
# NIS2-Minidurchstich: fiktiver Mittelstand

## Fiktivität

Dieses Beispiel ist vollständig fiktiv. Es enthält keine echten Organisations-, Kunden-, Personen-, Vertrags-, Incident-, System-, Netz- oder Kontaktdaten.

## Ziel

Dieses Mini-Beispiel zeigt, wie ein skeptischer CISO/ISB mit fünf Artefakten startet:

1. Managementauftrag,
2. Compliance-Register-Eintrag,
3. NIS2-Gap,
4. Auditfrage und Evidence Request,
5. Management-Entscheidungspunkt.

Es bestätigt keine regulatorische Erfüllung, keine Konformität, keine Zertifizierungsfähigkeit und keine Sicherheit.

## Ausgangslage

Die fiktive Organisation betreibt einen digitalen Kundenservice. Der CISO/ISB möchte prüfen, ob die Backup-/Restore-Routine für den Kernservice ausreichend betreibbar und reviewfähig ist.

## 1. Managementauftrag

**Artefakt:** `templates/decision-log.md`

| Feld | Beispielinhalt |
| --- | --- |
| Entscheidungsfrage | Welche drei NIS2-relevanten Routinen prüfen wir im ersten 30-Tage-Durchstich? |
| Vorschlag für ersten Scope | Backup-/Restore-Routine für digitalen Kernservice |
| Managementbedarf | Priorität, Owner, Review-Kadenz und Ressourcen für Nachweisaufbereitung bestätigen |
| Human Gate | Geschäftsführung / verantwortliche Managementrolle entscheidet |

## 2. Compliance-Register-Eintrag

**Artefakt:** `templates/compliance-source-register.md`

| Feld | Beispielinhalt |
| --- | --- |
| Quelle / Referenz | NIS2-relevanter interner Arbeitsverweis auf Business Continuity / Incident Readiness |
| Eigene Zusammenfassung | Kritische Services brauchen belastbare Routinen, Nachweise und Entscheidungswege für Ausfälle und Wiederanlauf. |
| Betroffener Bereich | Digitaler Kernservice, Backup, Restore, Betriebsteam |
| Owner-Frage | Wer verantwortet Restore-Tests und Review der Nachweise? |
| Grenzen | Keine Rechtsauslegung; nur interne Arbeitszusammenfassung. |

## 3. NIS2-Gap

**Artefakt:** `templates/nis2-gap-worksheet.md`

| Feld | Beispielinhalt |
| --- | --- |
| Soll-Zustand | Restore-Routine ist beschrieben, getestet, nachgewiesen und reviewfähig. |
| Ist-Zustand | Backup läuft; Restore-Testnachweise liegen verstreut und ohne Management-Review vor. |
| Gap-Typ | Evidenz- und Review-Gap |
| Auswirkung | Management kann Belastbarkeit und Restrisiko nicht sauber bewerten. |
| Nächster Schritt | Evidence Request an Service Owner und Betriebsverantwortliche Rolle. |

## 4. Auditfrage und Evidence Request

**Artefakte:** `templates/audit-questionnaire.md`, `templates/evidence-request-list.md`

### Auditfrage

| Feld | Beispielinhalt |
| --- | --- |
| Kriterium / Referenz | Interner Registereintrag Backup-/Restore-Readiness |
| Leitfrage | Wann wurde der letzte Restore-Test für den digitalen Kernservice durchgeführt und wie wurde das Ergebnis bewertet? |
| Prüfmethode | Dokumentenprüfung und kurzes Owner-Interview |
| Erwartete Evidenz | Restore-Testnotiz, Fehler-/Maßnahmenlog, Reviewvermerk |
| Human Gate | Bewertung und Priorisierung durch CISO/ISB und Management |

### Evidence Request

| ID | Benötigte Evidenz | Zweck | Warum für Entscheidung nötig? | Reuse | Aufwand | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ER-001 | letzte Restore-Testnotiz | Nachweis, dass Test durchgeführt wurde | Management kann Review-Kadenz nur festlegen, wenn Testpraxis bekannt ist. | ja/offen | niedrig | Service Owner | offen |
| ER-002 | Maßnahmenlog aus Restore-Test | offene technische oder organisatorische Punkte erkennen | Priorisierung hängt davon ab, ob offene Punkte kritisch oder Routinearbeit sind. | ja/offen | niedrig | Betriebsteam | offen |
| ER-003 | vorhandener Review- oder Freigabevermerk | Management-/Owner-Review prüfen | Entscheidung über Eskalationsschwelle braucht vorhandene Reviewpraxis. | offen | mittel | CISO/ISB | offen |

Workload-Regel: Im ersten Durchstich maximal drei Requests. Keine neuen Dokumente verlangen, solange vorhandene Evidenz reicht.

## 5. Management-Entscheidungspunkt

**Artefakt:** `templates/decision-log.md`

| Feld | Beispielinhalt |
| --- | --- |
| Entscheidungspunkt | Soll Restore-Readiness für den Kernservice monatlich oder quartalsweise im Management Review erscheinen? |
| Optionen | A: monatlicher operativer Review, B: quartalsweiser Management Review, C: nur nach Änderungen / Incidents |
| Evidenzlage | Restore-Testnotiz und Maßnahmenlog angefragt; Reviewvermerk offen |
| Offene Entscheidung | Review-Kadenz, Owner und Eskalationsschwelle festlegen |
| Human Gate | Management entscheidet; KI oder Agent bereitet nur vor. |

## 6. Maßnahme aus Gap ableiten

**Artefakt:** `templates/corrective-action-plan.md`

| Feld | Beispielinhalt |
| --- | --- |
| Auslöser | Evidence Request zeigt: Restore-Test existiert, aber Review und Maßnahmenverfolgung fehlen. |
| Korrekturmaßnahme | Restore-Testnotiz künftig mit Ergebnis, offenen Punkten, Owner und Reviewvermerk dokumentieren. |
| Ursache / Hypothese | Routine wurde technisch durchgeführt, aber nicht als Management-evidenzfähiger Prozess betrieben. |
| Owner | Service Owner mit Unterstützung CISO/ISB |
| Fälligkeit | vor nächstem quartalsweisen Management Review |
| Evidenz | aktualisierte Testnotiz, Maßnahmenlog, Reviewvermerk |
| Human Gate | Owner bestätigt Umsetzbarkeit; Management entscheidet Review-Kadenz und Eskalationsschwelle. |

## 7. Wirksamkeit später prüfen

**Artefakt:** `templates/remediation-effectiveness-review.md`

| Feld | Beispielinhalt |
| --- | --- |
| Prüfzeitpunkt | nach nächstem Restore-Test oder spätestens nach vereinbarter Review-Kadenz |
| Wirksamkeitsfrage | Zeigt die neue Routine, ob Restore-Test, offene Punkte und Management-Review nachvollziehbar verbunden sind? |
| Mindestnachweis | Testnotiz, Maßnahmenstatus, Reviewvermerk, Entscheidung bei offenen Punkten |
| Bewertung | offen; keine Wirksamkeitsbehauptung vor Evidenzprüfung |
| Handoff | Bei wiederholtem Fehlen von Evidenz an Management Review eskalieren. |

## 8. Beispiel: Legal-/Datenschutz-Handoff

**Artefakt:** `templates/legal-datenschutz-handoff.md`

Das Team nutzt dieses Handoff nur, wenn im echten Projekt rechtliche, datenschutzrechtliche oder vertrauliche Inhalte betroffen sind. Im fiktiven Beispiel bewertet niemand diese Fragen; das Handoff bereitet nur die Übergabe an Datenschutz/Legal vor.

| Feld | Beispielinhalt |
| --- | --- |
| Anlass / Trigger | Restore-Testnotiz könnte echte Nutzer-, Kunden- oder Systembezüge enthalten. |
| Konkrete Frage | Dürfen Auszüge der Restore-Testnotiz für KI-gestützte Zusammenfassung oder Evidence-Pack-Aufbereitung genutzt werden? |
| Datenklasse | unklar; vorläufig intern/vertraulich behandeln |
| Geplante Verarbeitung / Nutzung | Zusammenfassung für Evidence Pack und Management Review |
| KI-Nutzung betroffen? | ja / unklar |
| Bereits angewandte Schutzmaßnahmen | keine echten Inhalte in öffentliche Beispiele; Redaction vor KI-Nutzung prüfen |
| Benötigte Entscheidung / Einschätzung | Datenschutz/Legal klären zulässige Verarbeitung und notwendige Minimierung |
| Human Gate | Datenschutz/Legal entscheidet; CISO/ISB nutzt Ergebnis nur als Arbeitsfreigabe. |

Grenze: Das Handoff ist keine Datenschutzbewertung. Es verhindert, dass Security-Governance-Arbeit heimlich rechtliche oder datenschutzrechtliche Entscheidungen trifft.

## Was bewusst offen bleibt

- rechtliche Bewertung der NIS2-Anwendbarkeit,
- Datenschutzfragen zu echten Betriebsdaten,
- Risikoakzeptanz,
- finale Bewertung der Wirksamkeit,
- externe Kommunikation oder Audit-Aussage.

## Nächster Schritt

Wenn Evidenz vorliegt:

1. `templates/evidence-pack-index.md` befüllen,
2. bei Abweichungen `templates/audit-finding-report.md` nutzen,
3. Maßnahmen in `templates/corrective-action-plan.md` überführen,
4. Wirksamkeit später mit `templates/remediation-effectiveness-review.md` prüfen,
5. Entscheidung, Review-Kadenz und offene Restrisiken im Management Review nachhalten.
