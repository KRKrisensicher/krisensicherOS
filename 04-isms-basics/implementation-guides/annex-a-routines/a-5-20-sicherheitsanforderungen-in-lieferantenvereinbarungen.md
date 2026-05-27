
# A.5.20 — Sicherheitsanforderungen in Lieferantenvereinbarungen

## Zweck

Sicherheitsanforderungen an Lieferanten müssen so früh und konkret in Vereinbarungen übersetzt werden, dass sie im Betrieb steuerbar sind. Ohne klare Vereinbarung bleiben Zugriffsschutz, Meldewege, Nachweise, Subdienstleister, Schwachstellenbehandlung, Datenrückgabe oder Exit-Fähigkeit oft unverbindliche Erwartungen.

Diese Routine sorgt dafür, dass Sicherheitsanforderungen aus Risiko, Schutzbedarf und Betriebsrealität abgeleitet, mit Einkauf/Legal verhandlungsfähig gemacht und während der Laufzeit überprüft werden.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der sicherheitsrelevante Anforderungen an Lieferanten vor Vertragsabschluss oder Änderung identifiziert, in geeignete Vereinbarungen eingebracht, bei Ausnahmen entschieden und im laufenden Betrieb nachverfolgt werden.

## Typische Risiken

- Wenn Sicherheitsanforderungen nicht vertraglich oder verbindlich vereinbart werden, fehlen Durchsetzung, Nachweise und Eskalationswege.
- Wenn Anforderungen zu generisch sind, passen sie nicht zum konkreten Service, Datenumfang oder Zugriff.
- Wenn Meldewege, Fristen und Ansprechpartner fehlen, verzögern sich Reaktionen auf Sicherheitsereignisse.
- Wenn Subdienstleister, Standorte oder technische Änderungen nicht geregelt sind, verändert sich das Risiko unbemerkt.
- Wenn Exit, Datenrückgabe, Löschung oder Zugangsentzug nicht vereinbart sind, entstehen Risiken am Ende der Zusammenarbeit.
- Wenn Lieferantenanforderungen nur von Security formuliert werden, aber nicht rechtlich, kommerziell und betrieblich anschlussfähig sind, bleiben sie wirkungslos.

## Trigger

- neuer Lieferant, neue Vereinbarung, Ausschreibung, Proof of Concept oder Vertragsverlängerung.
- Änderung von Datenarten, Schutzbedarf, Zugriffen, Subdienstleistern, Betriebsmodell oder Standorten.
- Sicherheitsereignis, Schwachstellenmeldung, Leistungsproblem oder Auditfinding mit Lieferantenbezug.
- neue interne Sicherheitsanforderung, Risikoentscheidung oder Managementvorgabe.
- Review kritischer Lieferantenvereinbarungen.
- geplanter Exit, Kündigung, Migration oder Dienstleisterwechsel.
- externe Kundenanforderung oder regulatorischer Mappingbedarf, der Human Review erfordert.

## Rollen und Verantwortung

- **Service Owner / Fachverantwortlicher:** beschreibt Leistung, Daten, Prozesse, Kritikalität und betriebliche Anforderungen.
- **Einkauf / Vendor Management:** koordiniert Verhandlung, Lieferantenkommunikation, Vertragsbestand und Wiedervorlagen.
- **Legal:** übersetzt Anforderungen in geeignete Vertrags- oder Vereinbarungslogik und bewertet rechtliche Risiken.
- **Datenschutz:** prüft personenbezogene Daten, Datenschutzrollen und erforderliche Datenschutzvereinbarungen.
- **ISMS-Owner / Security-Rolle:** definiert Sicherheitsanforderungen, Nachweiserwartungen, Ausnahmen und Reviewpunkte.
- **IT-/Plattform Owner:** bewertet technische Anforderungen zu Zugriff, Schnittstellen, Protokollierung, Schwachstellen und Betrieb.
- **BCM-/Krisenrolle:** ergänzt Anforderungen zu Verfügbarkeit, Wiederherstellung, Krisenkommunikation und Exit.
- **Management:** entscheidet bei Abweichungen von Mindestanforderungen, kritischen Restrisiken oder kommerziellen Zielkonflikten.

## Implementierung

### Minimalstart

Ziel: sicherheitsrelevante Vereinbarungen enthalten die wichtigsten betrieblichen Erwartungen.

1. Vor Vertragsabschluss oder wesentlicher Änderung wird der Lieferant nach Kritikalität und Sicherheitsbezug eingestuft.
2. Für sicherheitsrelevante Lieferanten wird eine kurze Anforderungsliste erstellt: Daten, Zugriff, Nachweise, Meldeweg, Subdienstleister, Exit.
3. Einkauf, Legal, Datenschutz und Security prüfen die Anforderungen vor Freigabe.
4. Nicht erfüllte Anforderungen werden als Ausnahme mit Risiko, Laufzeit und Entscheider dokumentiert.
5. Vereinbarte Sicherheitsanforderungen werden im Lieferantenregister referenziert.
6. Vertragsende löst Prüfung von Zugangsentzug, Datenrückgabe/-löschung und Schnittstellendeaktivierung aus.

Minimaler Nachweis:

- Sicherheitsanforderungsliste je kritischem Lieferanten,
- Handoff-Nachweis an Einkauf/Legal/Datenschutz/Security,
- Vereinbarungsreferenz oder Vertragsanlage,
- Ausnahmeentscheidung bei Abweichung,
- Offboarding- oder Exit-Anforderung.

### Solide Praxis

Ziel: Anforderungen sind risikobasiert, verhandlungsfähig und prüfbar.

1. Die Organisation nutzt Anforderungskataloge nach Lieferantentyp: SaaS, Managed Service, Softwarelieferant, Berater mit Zugriff, Hosting, Wartung, Hardware/IT-Komponenten.
2. Anforderungen werden aus Risikoanalyse, Schutzbedarf, Datenklasse, Zugriffsart, Verfügbarkeitsbedarf und Lieferkettenabhängigkeit abgeleitet.
3. Vereinbarungen adressieren mindestens: Sicherheitskontakt, Incident-Kommunikation, Zugriffsschutz, Nachweise, Schwachstellen, Änderungen, Subdienstleister, Verfügbarkeit, Datenbehandlung, Offboarding und Audit-/Reviewfähigkeit in angemessener Form.
4. Abweichungen werden nicht informell akzeptiert, sondern als Risikoentscheidung dokumentiert.
5. Reviewtermine prüfen, ob Nachweise, Meldungen, Änderungen und offene Maßnahmen zur Vereinbarung passen.
6. Anforderungen aus A.5.19 und A.5.21 werden konsistent mit Lieferantensteuerung und IT-Lieferkette verbunden.

Starke Evidenz:

- risikobasierter Anforderungskatalog,
- Vertrags- oder Vereinbarungsreferenz mit Security-Bezug,
- dokumentierte Abweichungen und Risikoentscheidungen,
- Reviewprotokolle zu Nachweisen und offenen Pflichten,
- Änderungs- oder Subdienstleistermeldungen mit Bewertung,
- Exit-Checkliste oder Offboarding-Nachweis.

### Fortgeschritten

Ziel: Sicherheitsanforderungen werden über Portfolio, Vertragslebenszyklus und Managemententscheidungen gesteuert.

1. Vertragsmanagement, Lieferantenregister, Risikoregister und Reviewkalender sind verbunden.
2. Kritische Anforderungen haben Owner, Nachweisfrequenz, Eskalationspfad und messbaren Status.
3. Vertragsänderungen, Subdienstleisterwechsel, Sicherheitsereignisse und wesentliche technische Änderungen erzeugen automatische oder verbindliche Review-Trigger.
4. Standardklauseln und Playbooks werden regelmäßig aus Incidents, Audits, Exit-Erfahrungen und Marktänderungen verbessert.
5. Management sieht Abweichungen von Mindestanforderungen, kritische Lieferanten ohne passende Vereinbarungen und Kosten-/Risikokonflikte.
6. Für kritische Dienste werden Exit-, Notfall- und Kommunikationsanforderungen gemeinsam mit BCM und Krisenstab getestet oder tabletop-basiert geprüft.

## Ablauf als Routine

1. **Lieferantenbedarf entsteht:** neuer Dienst, Vertragsänderung, Verlängerung oder neuer Zugriff.
2. **Sicherheitsprofil erstellen:** Service, Daten, Zugriff, Kritikalität, Verfügbarkeit, Subdienstleister und Exit-Relevanz erfassen.
3. **Anforderungen ableiten:** passende Sicherheits-, Nachweis-, Melde-, Änderungs-, Offboarding- und BCM-Anforderungen auswählen.
4. **Handoffs prüfen:** Einkauf, Legal, Datenschutz, Security, IT und BCM je nach Profil einbinden.
5. **Vereinbarung verhandeln oder dokumentieren:** Anforderungen in Vertrag, Anlage, Leistungsbeschreibung, Sicherheitskonzept oder verbindliche Betriebsregel überführen.
6. **Abweichungen entscheiden:** nicht erfüllte Punkte bewerten, kompensieren, befristen oder ans Management eskalieren.
7. **Betrieb überwachen:** Nachweise, Meldungen, Änderungen und Maßnahmen im Lieferantenreview nachhalten.
8. **Änderungen bewerten:** neue Subdienstleister, Standorte, Zugriffspfade oder Datenarten lösen erneute Prüfung aus.
9. **Beenden:** Exit-, Lösch-, Rückgabe-, Schnittstellen- und Zugangsentzugsanforderungen nachweisen.

## Entscheidungen

- Welche Lieferanten benötigen welche Sicherheitsanforderungen?
- Welche Mindestanforderungen sind nicht verhandelbar und welche sind risikobasiert anpassbar?
- Welche Nachweise sind ausreichend und wie oft müssen sie aktualisiert werden?
- Wer akzeptiert Abweichungen von Anforderungen?
- Welche Ereignisse muss der Lieferant melden und über welchen Kanal?
- Welche Subdienstleister- oder Änderungsinformationen müssen vorab geprüft werden?
- Welche Exit- und Datenbehandlungsanforderungen sind für kritische Dienste notwendig?

## Evidenz

### Starke Evidenz

- Sicherheitsprofil des Lieferanten mit Daten-, Zugriffs- und Kritikalitätsbezug,
- Anforderungskatalog oder Vertragscheckliste,
- Vertragsanlage, Leistungsbeschreibung oder Vereinbarungsreferenz mit Security-Bezug,
- dokumentierte Legal-/Datenschutz-/Security-Prüfung,
- Abweichungs- und Ausnahmeentscheidungen mit Laufzeit,
- Nachweise aus laufenden Reviews,
- Exit- und Offboarding-Nachweise.

### Schwache Evidenz

- pauschale Sicherheitsklausel ohne Servicebezug,
- Standardvertrag ohne Prüfung des konkreten Daten- oder Zugriffsumfangs,
- Lieferantenzertifikat ohne Bezug zur Vereinbarung,
- mündliche Zusage des Lieferanten ohne Nachweis,
- Checkliste ohne Entscheidung bei Abweichungen.

### Evidenzlücken

- kritischer Lieferant ohne dokumentierte Sicherheitsanforderungen,
- Vertragsänderung ohne Security-Review,
- keine Regelung zu Sicherheitsereignissen oder Ansprechpartnern,
- Subdienstleister oder Standorte unbekannt,
- Abweichungen nicht risikobewertet,
- Vertragsende ohne Daten-, Zugangs- oder Schnittstellen-Nachweis.

## Wirksamkeitsprüfung

Prüffragen:

- Sind Sicherheitsanforderungen vor Vertragsabschluss oder Änderung eingebracht worden?
- Passen Anforderungen zum konkreten Service, Schutzbedarf und Zugriff?
- Sind Abweichungen sichtbar, befristet und entschieden?
- Werden vereinbarte Nachweise und Meldungen im Betrieb überprüft?
- Sind Subdienstleister-, Änderungs- und Incident-Kommunikation ausreichend steuerbar?
- Sind Exit, Datenrückgabe/-löschung und Zugangsentzug nachweisbar geregelt?
- Erkennt Management kritische Vereinbarungslücken und Zielkonflikte?

Mögliche Kennzahlen:

- Anteil kritischer Lieferanten mit dokumentierten Sicherheitsanforderungen,
- offene Vertragslücken nach Kritikalität,
- überfällige Nachweise oder Reviews,
- Anzahl und Alter von Abweichungen,
- Lieferantenänderungen mit Security-Review,
- Offboarding-Nachweise bei Vertragsende,
- kritische Lieferanten ohne Exit-Regelung.

## BSIG-/NIS2-Anschluss

Sicherheitsanforderungen in Lieferantenvereinbarungen sind anschlussfähig an NIS2-orientierte Themen wie Lieferkettensicherheit, Dienstleistersteuerung, Risikomanagement, Incident-Kommunikation, Business Continuity, Zugriffsschutz und Nachweisfähigkeit.

Für BSIG-/NIS2-Betroffenheit sollte die Organisation im Anforderungsregister prüfen, welche Vereinbarungen, Lieferantenklassen und Nachweise relevant sind. Dieses Artefakt ersetzt keine Rechtsberatung, Vertragsprüfung oder verbindliche Auslegung der Anwendbarkeit.

## Grenzen

- Dieses Artefakt ist kein Vertragsmuster und ersetzt keine juristische Prüfung.
- Es legt keine universellen Pflichtklauseln fest; Anforderungen müssen organisations- und servicebezogen abgeleitet werden.
- Es ersetzt keine Datenschutzprüfung oder Auftragsverarbeitungsvereinbarung.
- Keine Zertifizierungs-, Konformitäts- oder Sicherheitsgarantie.
- Keine ISO-27002-Texte und keine echten Vertrags-, Lieferanten- oder Kundendaten in Beispielen.

## Handoffs

- **Einkauf-/Vendor-Management-Handoff:** Verhandlung, Vertragsreferenz, Lieferantenkommunikation, Fristen und Verlängerungen.
- **Legal-Handoff:** Vertragsgestaltung, Haftungs-/Nachweismechanik, Kündigung, Audit-/Reviewrechte und rechtliche Risiken.
- **Datenschutz-Handoff:** personenbezogene Daten, Rollenklärung, Datenverarbeitung, Löschung, Übermittlung und Betroffenenrisiken.
- **Security-/ISMS-Handoff:** Sicherheitsanforderungen, Nachweise, Ausnahmen, Risikoregister und Reviewfrequenz.
- **IT-/Access-Handoff:** technische Zugänge, Schnittstellen, Protokollierung, Schwachstellen, Zertifikate und Offboarding.
- **BCM-/Krisen-Handoff:** Verfügbarkeit, Wiederanlauf, Notfallkommunikation, Exit und Ersatzbetrieb.
- **Management-Handoff:** wesentliche Abweichungen, Restrisiko, Budgetkonflikte oder Entscheidung gegen Mindestanforderungen.
- **Audit-/Evidence-Handoff:** fehlende Vereinbarungsreferenz, nicht geprüfte Abweichungen oder lückenhafte Reviewnachweise.

## Typische Fehler

- Security wird erst beteiligt, wenn der Vertrag bereits unterschriftsreif ist.
- Anforderungen werden aus einer generischen Klauselsammlung kopiert und nicht auf den Service bezogen.
- Abweichungen werden kommerziell akzeptiert, aber nicht als Risikoentscheidung dokumentiert.
- Vereinbarungen enthalten Meldepflichten, aber keine Ansprechpartner oder Prozesse.
- Subdienstleisteränderungen werden nicht nachgehalten.
- Exit wird erst bei Kündigung betrachtet.
- Nachweise werden jährlich eingesammelt, aber nicht bewertet oder mit Maßnahmen verknüpft.

## Fiktives Mini-Beispiel

Ein fiktiver IT-Betrieb vergibt den Betrieb eines Monitoring-Dienstes an einen Managed-Service-Anbieter. Die Vorprüfung zeigt Zugriff auf Infrastrukturmetadaten und Alarmierungswege. Security und IT formulieren Anforderungen zu Adminzugriff, MFA, Sicherheitskontakt, Schwachstellenmeldungen und Offboarding. Legal überführt sie in eine Vertragsanlage. Der Anbieter kann eine Nachweisfrequenz nicht erfüllen; der Service Owner dokumentiert eine befristete Ausnahme mit zusätzlichem Quartalsgespräch. Nach Vertragsstart wird der Nachweisstatus im Lieferantenreview geprüft.

Evidenz:

- Sicherheitsprofil des Managed Service,
- Anforderungsliste,
- Vertragsanlagenreferenz,
- Legal-/Security-Handoff,
- Ausnahmeentscheidung,
- Reviewprotokoll zum Nachweisstatus.
