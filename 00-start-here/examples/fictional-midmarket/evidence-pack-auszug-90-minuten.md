# Evidence-Pack-Auszug nach 90 Minuten: fiktiver Mittelstand

## Fiktivität

Dieses Beispiel ist vollständig fiktiv. Es enthält keine echten Organisations-, Kunden-, Personen-, Vertrags-, Incident-, System-, Netz- oder Kontaktdaten.

## Aus dem Repo erarbeitet

Dieser Auszug ist kein freier Marketing-Screenshot. Er wurde aus bestehenden krisensicherOS-Bausteinen abgeleitet:

- `examples/fiktiver-mittelstand/nis2-minidurchstich.md` — fiktiver Case Backup-/Restore-Routine für digitalen Kundenservice,
- `templates/nis2-gap-worksheet.md` — Logik für Referenz, Routine, Evidenz, Gap, Maßnahme, Priorität und Managemententscheidung,
- `templates/evidence-request-list.md` — maximal drei entscheidungsrelevante Evidence Requests im ersten Durchstich,
- `templates/evidence-pack-index.md` — Bündelung von Nachweisen für Review, Managemententscheidung und Follow-up,
- `templates/decision-log.md` — Human Gate, Entscheidung, Evidenzbezug und Review-Kadenz.

## Ausgangslage

Die fiktive Organisation **Musterwerk GmbH** betreibt einen digitalen Kundenservice. Im 90-Minuten-Durchstich wird nicht „NIS2-Konformität“ bestätigt, sondern konkrete Arbeit sichtbar gemacht: Scope, Gap, Evidenzbedarf, Owner, nächste Entscheidung.

## Auszug aus dem Evidence Pack

| Feld | Beispielinhalt | Repo-Herkunft |
| --- | --- | --- |
| Arbeitspaket | NIS2-Readiness: Backup-/Restore-Routine für digitalen Kundenservice | `examples/fiktiver-mittelstand/nis2-minidurchstich.md` |
| Ergebnis nach 90 Minuten | Ein priorisierter Gap, drei Evidence Requests, ein Management-Entscheidungspunkt | `templates/nis2-gap-worksheet.md`, `templates/evidence-request-list.md`, `templates/decision-log.md` |
| Human Gate | CISO/ISB prüft fachlich; Management entscheidet Review-Kadenz und Restrisiko | `templates/decision-log.md` |
| Grenze | Keine Rechtsberatung, keine Zertifizierungsaussage, keine Sicherheitsgarantie | Template-Grenzen und Repo-Guardrails |

## Beispielhafte NIS2-Gap-Zeile

| Arbeitsfeld | Referenzanker | bestehende Routine | vorhandene Evidenz | Gap | Maßnahme | Owner-Vorschlag | Priorität | Managemententscheidung |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Backup / Restore | interner Registerverweis Business Continuity / Incident Readiness | Backups laufen; Restore-Test wird technisch durchgeführt | Restore-Testnotizen liegen verstreut; Reviewvermerk fehlt | Evidenz- und Review-Gap | Restore-Testnotiz, Maßnahmenlog und Reviewvermerk in Evidence Pack bündeln | Service Owner + CISO/ISB | hoch für ersten Durchstich | Review-Kadenz und Eskalationsschwelle festlegen |

## Drei Evidence Requests

| ID | Kriterium / Referenz | Benötigte Evidenz | Zweck der Evidenz | Warum für Entscheidung nötig? | Aufwand | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ER-001 | Backup-/Restore-Readiness | letzte Restore-Testnotiz | Testpraxis sichtbar machen | Management kann Review-Kadenz nur festlegen, wenn Testpraxis bekannt ist. | niedrig | Service Owner | offen |
| ER-002 | Backup-/Restore-Readiness | Maßnahmenlog aus Restore-Test | offene Punkte priorisieren | Priorisierung hängt davon ab, ob offene Punkte kritisch oder Routinearbeit sind. | niedrig | Betriebsteam | offen |
| ER-003 | Backup-/Restore-Readiness | vorhandener Review- oder Freigabevermerk | Owner-/Management-Review prüfen | Eskalationsschwelle braucht vorhandene Reviewpraxis oder deren belegte Lücke. | mittel | CISO/ISB | offen |

## Evidence-Pack-Index-Ausschnitt

| Evidence Item | Scope / Control | Owner | Status | Zweck | Qualitätsnotiz | Lücke / Follow-up | Review durch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| letzte Restore-Testnotiz | digitaler Kundenservice / Restore-Routine | Service Owner | angefragt | Testdurchführung nachvollziehen | vorhandene Notiz zuerst wiederverwenden | Ablage und Aktualität prüfen | CISO/ISB |
| Maßnahmenlog | Restore-Test | Betriebsteam | angefragt | offene Punkte priorisieren | keine neue Dokumentation verlangen, wenn Log existiert | Maßnahmenstatus fehlt ggf. | CISO/ISB + Service Owner |
| Reviewvermerk | Management Review / Service Review | CISO/ISB | offen | Review-Kadenz und Eskalation bewerten | fehlender Vermerk ist selbst ein Gap | Managemententscheidung vorbereiten | Management |

## Was daraus konkret entsteht

- ein prüfbarer nächster Arbeitsschritt statt allgemeiner Compliance-Diskussion,
- eine kurze Evidenzliste, die vorhandene Nachweise zuerst nutzt,
- ein klarer Owner-Handoff,
- ein Managementpunkt für Kadenz, Priorität und Restrisiko.

## Grenzen

Dieses Beispiel bestätigt keine regulatorische Erfüllung, keine Zertifizierungsfähigkeit und keine Sicherheit. Rechtliche Prüfung, Datenschutzbewertung, Risikoakzeptanz und Managemententscheidungen bleiben menschlich.
