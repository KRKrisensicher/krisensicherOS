
# ISO/IEC 27001-Anforderungen in krisensicherOS-Sprache

## Zweck

Dieses Artefakt übersetzt ISO/IEC-27001-Referenzpunkte in krisensicherOS-Sprache. Es macht sichtbar, welche Routine, Entscheidung, Rolle, Evidenz und welcher Review aus einem Referenzpunkt entstehen kann.

Es enthält keine Normtexte, keine Kontrollformulierungen und keine verbindliche Normauslegung. Abschnittsnummern dienen nur als Referenzanker.

## Grenzen

Dieses Artefakt ersetzt keine Rechtsberatung, Datenschutzberatung, Zertifizierungsberatung, Auditbewertung oder Managemententscheidung. Es bestätigt keine Erfüllung externer Anforderungen.

## Nutzung

1. Abschnittsreferenz auswählen.
2. Bestehende Routine und Owner prüfen.
3. Lücke, Entscheidung und Evidenzspur eintragen.
4. Human Gate markieren.
5. Ergebnis in Scope Canvas, Risikoregister, Maßnahmenbacklog, Evidence Pack oder Decision Log überführen.

## Übersetzungslogik

| Referenzbegriff | krisensicherOS-Sprache |
| --- | --- |
| Anforderung | Routine / Entscheidungspunkt |
| Control | Schutzmaßnahme / Arbeitsweise |
| Auditkriterium | Prüffrage / Evidenzspur |
| Dokumentation | Nachweisfluss |
| Verantwortlichkeit | Rolle mit Entscheidungskompetenz |

## Abschnittslandkarte

### Abschnitt 4.1 — Kontext-Review-Routine

- **Betriebsfrage:** Welche internen und externen Faktoren beeinflussen, welche Security-Governance nötig und betreibbar ist?
- **Rolle mit Entscheidungskompetenz:** Geschäftsleitung oder delegierte Governance-Verantwortung.
- **Routine:** Einflussfaktoren sammeln; Auswirkungen auf Ziele, Ressourcen und Risiken ableiten; Annahmen markieren; Änderungen in Scope- und Risiko-Review einspeisen.
- **Mindestartefakte:** Kontextregister, Annahmenlog, Einflussfaktorenliste, Reviewnotiz.
- **Evidenzspur:** datierte Kontextbewertung mit Verweis auf Scope- oder Risikoentscheidung.
- **Reviewpunkt:** jährlich und bei wesentlichen Organisations-, Technologie-, Bedrohungs- oder Regulierungsänderungen.
- **BSIG/NIS2-Bezug:** § 28 BSIG und Anlagen für Betroffenheitsindikatoren; § 30 BSIG indirekt über risikobasierte Maßnahmenplanung.
- **Human Gate:** Management bestätigt, welche Kontextfaktoren steuerungsrelevant sind.

### Abschnitt 4.2 — Erwartungs- und Verpflichtungsradar

- **Betriebsfrage:** Welche Parteien, Anforderungen und Nachweiserwartungen beeinflussen das ISMS?
- **Rolle mit Entscheidungskompetenz:** Governance Owner mit Legal/Compliance und Fachverantwortlichen.
- **Routine:** relevante Parteien erfassen; Erwartungstypen sortieren; Anforderungen in Prüffragen, Entscheidungen oder Handoffs überführen; Konflikte eskalieren.
- **Mindestartefakte:** Stakeholder-Register, Erwartungslog, Verpflichtungsregister, offene Klärungsliste.
- **Evidenzspur:** Zuordnung von Erwartung zu Owner, Entscheidung, Nachweis oder Klärstatus.
- **Reviewpunkt:** bei neuen Kundenanforderungen, Verträgen, regulatorischen Änderungen oder Management Reviews.
- **BSIG/NIS2-Bezug:** § 28 BSIG für mögliche Betroffenheit; § 30 und § 38 BSIG bei Governance- und Leitungsbezug.
- **Human Gate:** rechtliche, vertragliche und regulatorische Einordnung nur durch zuständige Menschen.

### Abschnitt 4.3 — Scope-Entscheidungscanvas

- **Betriebsfrage:** Welche Organisationsteile, Services, Prozesse, Standorte, Systeme und Schnittstellen gehören zum ISMS-Betriebsbereich?
- **Rolle mit Entscheidungskompetenz:** Geschäftsleitung oder ISMS-Sponsor.
- **Routine:** Scope-Kandidaten sammeln; Ein- und Ausschlüsse begründen; Schnittstellen sichtbar machen; Scope-Risiken festhalten; Scope freigeben lassen.
- **Mindestartefakte:** ISMS-Scope-Canvas, Nicht-Scope-Liste, Schnittstellenkarte, Scope-Entscheidungsnotiz.
- **Evidenzspur:** freigegebene Scope-Version mit Datum, Owner und offenen Scope-Fragen.
- **Reviewpunkt:** bei Organisationsänderung, neuen kritischen Services, Outsourcing, M&A oder möglicher neuer Betroffenheit.
- **BSIG/NIS2-Bezug:** § 28 BSIG und Anlagen für Einrichtungs-/Sektorprüfung; § 38 BSIG bei Leitungsentscheidung.
- **Human Gate:** finale Scope-Freigabe durch verantwortliche Leitung.

### Abschnitt 4.4 — ISMS-Betriebsmodell

- **Betriebsfrage:** Wie wird Security Governance als wiederkehrender Steuerungsprozess betrieben?
- **Rolle mit Entscheidungskompetenz:** ISMS Owner mit Management-Sponsor.
- **Routine:** Kernroutinen definieren; Rollen, Inputs, Outputs und Eskalationen festlegen; Register versionieren; Reviews mit Entscheidungen verbinden.
- **Mindestartefakte:** ISMS-Operating-Model, Rollenmatrix, Routinenkalender, Registerübersicht, Handoff-Landkarte.
- **Evidenzspur:** Reviewprotokolle, Maßnahmenstände, Entscheidungslogs, Evidence-Pack-Index.
- **Reviewpunkt:** quartalsweise operativ, mindestens jährlich strategisch.
- **BSIG/NIS2-Bezug:** § 30 BSIG für Maßnahmensteuerung; § 38 BSIG für Leitungsverantwortung; § 32 BSIG bei Meldewegen.
- **Human Gate:** Management bestätigt Betriebsmodell, Ressourcen und Verantwortlichkeiten.

### Abschnitt 5.1 — Leitungsmandat-Routine

- **Betriebsfrage:** Woran erkennt man, dass Leitung Verantwortung, Prioritäten und Ressourcen aktiv trägt?
- **Rolle mit Entscheidungskompetenz:** Geschäftsleitung.
- **Routine:** Sicherheitsziele mit Organisationszielen verbinden; Ressourcen entscheiden; Top-Risiken behandeln; Wirksamkeit und Verbesserungsbedarf im Review entscheiden.
- **Mindestartefakte:** Management-Mandat, Entscheidungslog, Ressourcenbeschluss, Reviewagenda.
- **Evidenzspur:** Beschlüsse, Prioritätsentscheidungen, Management-Review-Protokolle.
- **Reviewpunkt:** bei Management Review und bei kritischen Risiken oder Ressourcenblockern.
- **BSIG/NIS2-Bezug:** § 38 BSIG bei möglicher Betroffenheit.
- **Human Gate:** Leitung entscheidet Risikoakzeptanz, Budget und Eskalationen.

### Abschnitt 5.2 — Security-Policy als Entscheidungsrahmen

- **Betriebsfrage:** Welche Leitplanken gelten für Entscheidungen, Prioritäten und Verhalten im ISMS?
- **Rolle mit Entscheidungskompetenz:** Geschäftsleitung mit ISMS Owner.
- **Routine:** Entscheidungsleitplanken formulieren; Rollen und Erwartungen kommunizieren; Policy an Routinen koppeln; Review und Aktualisierung planen.
- **Mindestartefakte:** Policy-Kurzfassung, Kommunikationsnachweis, Reviewnotiz, Entscheidungsleitplanken.
- **Evidenzspur:** freigegebene Policy-Version, Bekanntmachung, Änderungslog.
- **Reviewpunkt:** jährlich und bei Scope-, Strategie- oder Risikowechsel.
- **BSIG/NIS2-Bezug:** § 30 und § 38 BSIG indirekt über Governance- und Maßnahmenrahmen.
- **Human Gate:** Management gibt Leitplanken frei.

### Abschnitt 5.3 — Rollen- und Entscheidungsrechte-Matrix

- **Betriebsfrage:** Wer entscheidet, wer führt aus, wer prüft und wer eskaliert?
- **Rolle mit Entscheidungskompetenz:** Geschäftsleitung / ISMS Sponsor.
- **Routine:** Rollen identifizieren; Entscheidungsrechte und Stellvertretung festlegen; Eskalationswege definieren; Rollen regelmäßig prüfen.
- **Mindestartefakte:** Rollenmatrix, RACI-ähnliche Arbeitsmatrix, Eskalationskarte, Stellvertretungsregel.
- **Evidenzspur:** freigegebene Rollenliste, Änderungen, Reviewprotokolle.
- **Reviewpunkt:** bei Personalwechsel, Reorganisation, Incidents oder Review-Findings.
- **BSIG/NIS2-Bezug:** § 38 BSIG bei Leitungs- und Schulungsbezug.
- **Human Gate:** Management bestätigt Mandate und Ressourcen.

### Abschnitt 6.1.1 — Risiko- und Chancenarbeitsmodus

- **Betriebsfrage:** Wie erkennt das ISMS relevante Unsicherheiten und leitet daraus Entscheidungen ab?
- **Rolle mit Entscheidungskompetenz:** ISMS Owner mit Risk Ownern.
- **Routine:** relevante Unsicherheiten sammeln; Risiken/Chancen priorisieren; Verantwortliche festlegen; Maßnahmen oder Entscheidungen ableiten.
- **Mindestartefakte:** Risikolog, Chancen-/Verbesserungsliste, Priorisierung, Decision Log.
- **Evidenzspur:** nachvollziehbare Bewertung und Folgeentscheidung.
- **Reviewpunkt:** regelmäßig und bei Kontext-, Scope- oder Incident-Änderungen.
- **BSIG/NIS2-Bezug:** § 30 BSIG als Referenzanker für risikobezogene Sicherheitsmaßnahmen.
- **Human Gate:** Risikoakzeptanz bleibt Managemententscheidung.

### Abschnitt 6.1.2 — Risikobewertungsroutine

- **Betriebsfrage:** Wie werden Sicherheitsrisiken einheitlich beschrieben, bewertet und vergleichbar gemacht?
- **Rolle mit Entscheidungskompetenz:** Risk Owner, bestätigt durch ISMS Owner.
- **Routine:** Risikoszenario beschreiben; betroffene Assets/Services zuordnen; bestehende Maßnahmen erfassen; Bewertung und Begründung dokumentieren; Reviewtermin setzen.
- **Mindestartefakte:** Risikoanalyse-Register, Bewertungsmethodik, Risikoszenario, Reviewkalender.
- **Evidenzspur:** datierte Bewertung mit Begründung, Owner und Änderungsverlauf.
- **Reviewpunkt:** bei neuen Bedrohungen, Schwachstellen, Incidents, Scope-Änderungen oder fälliger Kadenz.
- **BSIG/NIS2-Bezug:** § 30 BSIG für Risikomanagementmaßnahmen.
- **Human Gate:** Methodik und Bewertungsannahmen fachlich freigeben.

### Abschnitt 6.1.3 — Risikobehandlungs- und SoA-Arbeitslogik

- **Betriebsfrage:** Wie werden Risiken in Maßnahmen, Ausnahmen, Akzeptanzen und Nachweise überführt?
- **Rolle mit Entscheidungskompetenz:** Risk Owner; Management bei Restrisiko und Ressourcen.
- **Routine:** Behandlungsoption wählen; Maßnahme oder Akzeptanzentscheidung formulieren; Schutzmaßnahmen-Referenzen pflegen; Evidenz und Wirksamkeitsprüfung festlegen; Entscheidung dokumentieren.
- **Mindestartefakte:** Risk-Control Map, Maßnahmenbacklog, SoA-Erweiterung, Ausnahme-/Akzeptanzlog.
- **Evidenzspur:** Verbindung von Risiko, Maßnahme, Owner, Status, Begründung und Review.
- **Reviewpunkt:** bei Maßnahmenabschluss, Ausnahmeablauf, neuen Risiken oder Management Review.
- **BSIG/NIS2-Bezug:** § 30 BSIG für Maßnahmenplanung und Nachweisfähigkeit.
- **Human Gate:** Risikoakzeptanz und Maßnahmenpriorisierung durch verantwortliche Menschen.

### Abschnitt 6.2 — Ziel- und Umsetzungsplan-Routine

- **Betriebsfrage:** Welche messbaren Arbeitsziele treiben das ISMS im nächsten Zeitraum?
- **Rolle mit Entscheidungskompetenz:** ISMS Owner mit Management-Sponsor.
- **Routine:** Ziele aus Risiken und Prioritäten ableiten; Owner und Fristen setzen; Mess- oder Reviewkriterium festlegen; Fortschritt berichten.
- **Mindestartefakte:** Zielregister, Maßnahmenplan, Fortschrittsbericht, Reviewnotiz.
- **Evidenzspur:** Zielstatus, Entscheidungen bei Abweichung, Nachweise zum Fortschritt.
- **Reviewpunkt:** monatlich operativ oder nach vereinbarter Management-Kadenz.
- **BSIG/NIS2-Bezug:** § 30 und § 38 BSIG indirekt über Steuerung und Leitungsverantwortung.
- **Human Gate:** Ziele, Prioritäten und Ressourcen durch Leitung bestätigen.

### Abschnitt 6.3 — Änderungssteuerung für das ISMS

- **Betriebsfrage:** Wie werden geplante Änderungen am ISMS kontrolliert vorbereitet und nachverfolgt?
- **Rolle mit Entscheidungskompetenz:** ISMS Owner; Management bei Scope-/Ressourcenwirkung.
- **Routine:** Änderung beschreiben; Auswirkung auf Scope, Risiken, Rollen und Evidenz prüfen; Handoffs festlegen; Änderung freigeben und nachhalten.
- **Mindestartefakte:** ISMS-Change-Log, Auswirkungsnotiz, Freigabe, Nachkontrolle.
- **Evidenzspur:** Änderungsentscheidung, Umsetzungsstatus, Review nach Umsetzung.
- **Reviewpunkt:** nach jeder größeren Änderung und im Management Review.
- **BSIG/NIS2-Bezug:** relevant, wenn Änderung Betroffenheit, Meldewege oder Risikomanagement beeinflusst.
- **Human Gate:** Scope-, Pflicht- oder Ressourcenfolgen menschlich prüfen.

### Abschnitt 7.1 — Ressourcenentscheidungsroutine

- **Betriebsfrage:** Welche Ressourcen braucht das ISMS, um vereinbarte Routinen realistisch zu betreiben?
- **Rolle mit Entscheidungskompetenz:** Geschäftsleitung / Budgetverantwortliche.
- **Routine:** Ressourcenbedarf aus Zielen, Risiken und Backlog ableiten; Engpässe markieren; Optionen vorbereiten; Entscheidung dokumentieren.
- **Mindestartefakte:** Ressourcenbedarf, Kapazitätsnotiz, Prioritätenliste, Managemententscheidung.
- **Evidenzspur:** Beschluss, Budget-/Kapazitätszuordnung, offene Blocker.
- **Reviewpunkt:** bei Management Review, Budgetplanung und überfälligen Maßnahmen.
- **BSIG/NIS2-Bezug:** § 38 BSIG bei Leitungs- und Überwachungsbezug.
- **Human Gate:** Ressourcenfreigabe durch zuständige Leitung.

### Abschnitt 7.2 — Kompetenzroutine

- **Betriebsfrage:** Können die Rollen ihre ISMS-Aufgaben tatsächlich ausführen und entscheiden?
- **Rolle mit Entscheidungskompetenz:** ISMS Owner mit HR/Training und Linienverantwortlichen.
- **Routine:** rollenbezogene Fähigkeiten definieren; Lücken feststellen; Schulung oder Coaching planen; Nachweise pflegen.
- **Mindestartefakte:** Kompetenzmatrix, Schulungsplan, Teilnahme-/Briefingnachweis, Rollenbriefing.
- **Evidenzspur:** Schulungsnachweise, Befähigungsstatus, offene Lücken.
- **Reviewpunkt:** bei Rollenwechsel, neuen Routinen, Incidents oder jährlicher Schulungsplanung.
- **BSIG/NIS2-Bezug:** § 38 BSIG bei möglicher Geschäftsleitungs- und Schulungspflicht.
- **Human Gate:** Schulungsbedarf und Eignung durch zuständige Rollen prüfen.

### Abschnitt 7.3 — Awareness- und Verantwortungsverständnis

- **Betriebsfrage:** Verstehen betroffene Personen, welche Sicherheitsverantwortung sie im Alltag haben?
- **Rolle mit Entscheidungskompetenz:** ISMS Owner mit Kommunikations-/HR-Rolle.
- **Routine:** Zielgruppen definieren; Kernbotschaften aus Rollen und Risiken ableiten; Awareness-Formate durchführen; Wirkung und Rückfragen auswerten.
- **Mindestartefakte:** Awareness-Plan, Zielgruppenliste, Kommunikationsnachweis, Feedbacknotiz.
- **Evidenzspur:** durchgeführte Maßnahmen, Teilnahme oder alternative Nachweise, Verbesserungslog.
- **Reviewpunkt:** jährlich, bei neuen Risiken oder nach relevanten Vorfällen.
- **BSIG/NIS2-Bezug:** indirekt über Sicherheitskultur, Leitungsverantwortung und Risikomanagement.
- **Human Gate:** Inhalte für Zielgruppen und Datenklassen freigeben.

### Abschnitt 7.4 — Kommunikationsroutine

- **Betriebsfrage:** Wer kommuniziert welche Sicherheitsinformation an wen, wann und mit welcher Freigabe?
- **Rolle mit Entscheidungskompetenz:** Kommunikationsrolle mit ISMS Owner; Legal/Management bei externer Kommunikation.
- **Routine:** Kommunikationsarten festlegen; interne und externe Empfänger definieren; Freigaben klären; Kommunikationsnachweise pflegen.
- **Mindestartefakte:** Kommunikationsmatrix, Freigabelog, Verteiler-/Empfängerliste, Kommunikationsnotiz.
- **Evidenzspur:** datierte Kommunikation, Freigabe, Empfängerkreis, Folgeaktion.
- **Reviewpunkt:** bei Incidents, regulatorischen Änderungen, Management Review oder Kommunikationspannen.
- **BSIG/NIS2-Bezug:** § 32 BSIG bei Melde- und Kommunikationspfaden; § 38 BSIG bei Leitungskommunikation.
- **Human Gate:** externe Aussagen, Kunden-/Behördenkommunikation und rechtliche Bewertung freigeben lassen.

### Abschnitt 7.5.1 bis 7.5.3 — Nachweisfluss und Dokumentensteuerung

- **Betriebsfrage:** Welche Informationen müssen auffindbar, aktuell, geschützt und entscheidungsfähig sein?
- **Rolle mit Entscheidungskompetenz:** Evidence Owner mit ISMS Owner.
- **Routine:** benötigte Nachweise definieren; Ablage, Zugriff und Versionierung festlegen; Schutzbedarf bestimmen; regelmäßige Evidence Reviews durchführen.
- **Mindestartefakte:** Evidence-Pack-Index, Dokumentenregister, Ablageregel, Reviewprotokoll.
- **Evidenzspur:** aktuelle Versionen, Zugriffsklärung, Änderungslog, Reviewstatus.
- **Reviewpunkt:** quartalsweise und vor Management Review oder internen Prüfungen.
- **BSIG/NIS2-Bezug:** Nachweisfähigkeit für § 30, § 32 und § 38 BSIG je nach Kontext.
- **Human Gate:** vertrauliche, personenbezogene oder lizenzpflichtige Inhalte getrennt prüfen.

### Abschnitt 8.1 — Betriebsplanung und Steuerung

- **Betriebsfrage:** Wie werden ISMS-Routinen geplant, ausgeführt, überwacht und bei Änderungen angepasst?
- **Rolle mit Entscheidungskompetenz:** ISMS Owner mit Prozess- und Service Ownern.
- **Routine:** Routinenkalender pflegen; Arbeitspakete planen; Änderungen kontrollieren; ausgelagerte Leistungen einbinden; Ergebnisse nachhalten.
- **Mindestartefakte:** Betriebsplan, Maßnahmenbacklog, Change-Notiz, Outsourcing-/Schnittstellenliste.
- **Evidenzspur:** durchgeführte Routinen, Statusberichte, Abweichungen, Freigaben.
- **Reviewpunkt:** monatlich operativ, quartalsweise mit Risiken und Evidenz.
- **BSIG/NIS2-Bezug:** § 30 BSIG bei Maßnahmenbetrieb; § 32 BSIG bei Incident-/Meldewegen.
- **Human Gate:** wesentliche Betriebsänderungen und Auslagerungen freigeben.

### Abschnitt 8.2 — Risikoanalyse im Betrieb

- **Betriebsfrage:** Wie wird sichergestellt, dass Risikoanalysen nicht einmalig bleiben?
- **Rolle mit Entscheidungskompetenz:** Risk Owner mit ISMS Owner.
- **Routine:** Risikoanalyse nach Kadenz durchführen; neue Trigger aufnehmen; Bewertung aktualisieren; betroffene Maßnahmen und Entscheidungen anpassen.
- **Mindestartefakte:** aktualisiertes Risikoregister, Reviewnotiz, Änderungslog, offene Entscheidungen.
- **Evidenzspur:** Bewertungsverlauf, Owner, Reviewdatum, Folgeaktionen.
- **Reviewpunkt:** nach Kalender und bei Incidents, Changes, Lieferantenänderungen oder Findings.
- **BSIG/NIS2-Bezug:** § 30 BSIG als Referenzanker für laufende Risikosteuerung.
- **Human Gate:** Bewertungsmethodik und Risikoakzeptanz prüfen lassen.

### Abschnitt 8.3 — Risikobehandlung im Betrieb

- **Betriebsfrage:** Werden beschlossene Maßnahmen, Ausnahmen und Akzeptanzen tatsächlich umgesetzt und überprüft?
- **Rolle mit Entscheidungskompetenz:** Risk Owner / Control Owner; Management bei Restrisiko.
- **Routine:** Maßnahmenstatus prüfen; Blocker eskalieren; Evidenz aktualisieren; Wirksamkeitsreview durchführen; Entscheidungen erneuern.
- **Mindestartefakte:** Maßnahmenbacklog, Risk-Control Map, Ausnahmeprotokoll, Wirksamkeitsreview.
- **Evidenzspur:** Status, Nachweis, Reviewentscheidung, offene Restrisiken.
- **Reviewpunkt:** monatlich für Maßnahmen, quartalsweise für Risiko-/Control-Wirkung.
- **BSIG/NIS2-Bezug:** § 30 BSIG für Maßnahmenbetrieb und Nachweisfähigkeit.
- **Human Gate:** Restrisiko, Ausnahmen und Ressourcen durch Menschen entscheiden.

### Abschnitt 9.1 — Monitoring- und Bewertungsroutine

- **Betriebsfrage:** Woran erkennt die Organisation, ob das ISMS funktioniert oder nachsteuern muss?
- **Rolle mit Entscheidungskompetenz:** ISMS Owner mit Management-Review-Facilitator.
- **Routine:** Kennzahlen und Reviewfragen definieren; Datenquellen festlegen; Ergebnisse bewerten; Entscheidungen vorbereiten.
- **Mindestartefakte:** Reviewindikatoren, Monitoringnotiz, Auswertungsbericht, Entscheidungsfragen.
- **Evidenzspur:** Datengrundlage, Auswertung, Management-Handoff.
- **Reviewpunkt:** nach festgelegter Kadenz und vor Management Review.
- **BSIG/NIS2-Bezug:** unterstützt Nachweisfähigkeit zu § 30 und Leitungsbefassung nach § 38 BSIG.
- **Human Gate:** Bewertung und Schlussfolgerungen fachlich freigeben.

### Abschnitt 9.2.1 und 9.2.2 — Interne Prüfplanung und Durchführung

- **Betriebsfrage:** Wie prüft die Organisation selbst, ob Routinen laufen und Nachweise tragfähig sind?
- **Rolle mit Entscheidungskompetenz:** interne Review-/Auditrolle mit ISMS Owner.
- **Routine:** Prüfziel und Scope festlegen; Prüffragen formulieren; Evidenz anfordern; Ergebnisse bewerten; Findings in Maßnahmen überführen.
- **Mindestartefakte:** Prüfplan, Prüffragen, Evidence Request List, Finding Report, Maßnahmen-Handoff.
- **Evidenzspur:** Prüfprotokoll, Stichproben, Feststellungen, Folgeentscheidungen.
- **Reviewpunkt:** nach Prüfprogramm, nach Incidents oder vor externen Prüfungen/Kundenanfragen.
- **BSIG/NIS2-Bezug:** interne Prüfungen können Nachweis- und Managementfähigkeit unterstützen, ohne externe Aussage zu ersetzen.
- **Human Gate:** Prüfprogramm, Findings und Eskalationen durch verantwortliche Rollen bestätigen.

### Abschnitt 9.3.1 bis 9.3.3 — Management-Review-Routine

- **Betriebsfrage:** Welche Entscheidungen muss die Leitung auf Basis von Risiken, Maßnahmen, Evidenz und Veränderungen treffen?
- **Rolle mit Entscheidungskompetenz:** Geschäftsleitung.
- **Routine:** Input aus Risiken, Incidents, Maßnahmen, Prüfungen und Veränderungen sammeln; Entscheidungsfragen formulieren; Beschlüsse dokumentieren; Follow-up steuern.
- **Mindestartefakte:** Management-Review-Agenda, Decision Brief, Decision Log, Follow-up-Liste, Schulungs-/Befassungsnachweis.
- **Evidenzspur:** Protokoll, Beschlüsse, Auflagen, Owner, Fristen.
- **Reviewpunkt:** mindestens in festgelegter Management-Kadenz und anlassbezogen bei wesentlichen Ereignissen.
- **BSIG/NIS2-Bezug:** § 38 BSIG bei Leitungsverantwortung; § 30 und § 32 BSIG als mögliche Inputfelder.
- **Human Gate:** Management entscheidet Prioritäten, Ressourcen und Risikoakzeptanz.

### Abschnitt 10.1 — Verbesserungsroutine

- **Betriebsfrage:** Wie werden Verbesserungschancen erkannt, priorisiert und umgesetzt?
- **Rolle mit Entscheidungskompetenz:** ISMS Owner mit Management bei größeren Änderungen.
- **Routine:** Verbesserungsquellen sammeln; Wirkung und Aufwand einschätzen; Owner und Frist festlegen; Umsetzung und Review nachhalten.
- **Mindestartefakte:** Verbesserungsbacklog, Priorisierung, Umsetzungsnachweis, Reviewnotiz.
- **Evidenzspur:** Quelle, Entscheidung, Umsetzung, Wirkungskontrolle.
- **Reviewpunkt:** im operativen Review und Management Review.
- **BSIG/NIS2-Bezug:** indirekt über laufende Verbesserung von Risikomanagement und Nachweisfähigkeit.
- **Human Gate:** Priorisierung und Ressourcenzuteilung freigeben lassen.

### Abschnitt 10.2 — Abweichungs- und Korrekturmaßnahmenroutine

- **Betriebsfrage:** Wie reagiert die Organisation auf Abweichungen so, dass Ursachen bearbeitet und Wiederholungen reduziert werden?
- **Rolle mit Entscheidungskompetenz:** Corrective Action Owner mit ISMS Owner.
- **Routine:** Abweichung erfassen; Auswirkung und Ursache prüfen; Korrektur- und Vorbeugemaßnahme festlegen; Wirksamkeit überprüfen; Management eskalieren, wenn nötig.
- **Mindestartefakte:** Abweichungsnotiz, Ursachenanalyse, Corrective Action Plan, Wirksamkeitsreview, Decision Log.
- **Evidenzspur:** Feststellung, Maßnahme, Owner, Frist, Wirksamkeitsnachweis.
- **Reviewpunkt:** nach Maßnahmenfrist und im Verbesserungsreview.
- **BSIG/NIS2-Bezug:** § 32 BSIG bei meldepflichtnahen Ereignissen prüfen lassen; § 30 BSIG bei Risikomaßnahmen.
- **Human Gate:** Meldepflicht, externe Kommunikation und Risikoakzeptanz menschlich prüfen.

### Anhang A — Schutzmaßnahmen-Referenzlogik

- **Betriebsfrage:** Welche Schutzmaßnahmen braucht die Organisation aufgrund ihrer Risiken, ihres Scopes und ihrer Entscheidungen?
- **Rolle mit Entscheidungskompetenz:** Risk Owner mit Control Owner; Management bei Ausnahmen oder Restrisiken.
- **Routine:** Schutzmaßnahmen-Referenzen nur als IDs oder eigene Kurzlabels führen; jede Maßnahme an Risiko, Owner, Routine, Evidenz und Review koppeln; Nichtanwendung oder Ausnahme begründen; Wirksamkeit prüfen.
- **Mindestartefakte:** Risk-Control Map, SoA-Erweiterung, Maßnahmenroutine, Ausnahme-/Nichtanwendungsbegründung, Evidence Pack.
- **Evidenzspur:** Verbindung von Risiko, Schutzmaßnahme, Status, Begründung, Nachweis und Review.
- **Reviewpunkt:** bei Risikoänderung, Scope-Änderung, Incident, Finding und Management Review.
- **BSIG/NIS2-Bezug:** § 30 BSIG für Risikomanagementmaßnahmen; § 32 BSIG bei Incident-/Meldebezug; § 38 BSIG bei Leitungsentscheidung.
- **Human Gate:** Auswahl, Nichtanwendung, Ausnahme und Restrisiko durch verantwortliche Menschen freigeben.

## Qualitätscheckliste

Vor Nutzung oder Veröffentlichung einer abgeleiteten Arbeitsfassung prüfen:

- Keine Normtexte, Tabellen oder Kontrollformulierungen übernommen.
- Abschnittsnummern nur als Referenzanker genutzt.
- Jede Referenz ist in Routine, Entscheidung, Rolle, Evidenz und Review übersetzt.
- Keine externe Erfüllungs-, Rechts- oder Prüfaussage enthalten.
- BSIG-/NIS2-Bezüge sind als öffentliche Referenzanker markiert und nicht als Rechtsauslegung formuliert.
- Human Gates für Management, Risikoakzeptanz, Legal, Datenschutz und externe Kommunikation sind sichtbar.
- Vertrauliche, personenbezogene oder lizenzpflichtige Inhalte bleiben außerhalb des öffentlichen Repos.
