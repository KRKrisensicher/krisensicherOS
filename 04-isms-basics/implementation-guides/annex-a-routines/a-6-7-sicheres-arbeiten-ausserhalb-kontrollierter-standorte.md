
# A.6.7 — Sicheres Arbeiten außerhalb kontrollierter Standorte

## Zweck

Sicheres Arbeiten außerhalb kontrollierter Standorte sorgt dafür, dass Informationen, Geräte, Zugänge und Gespräche auch dann geschützt bleiben, wenn Menschen im Homeoffice, unterwegs, bei Kunden, in Co-Working-Flächen, im Zug oder an anderen nicht kontrollierten Orten arbeiten. Der Kern ist eine betreibbare Routine: klare Regeln, passende technische Ausstattung, Meldewege, Reviews und Entscheidungen bei Ausnahmen.

## Control-Ziel in Repo-Sprache

Die Organisation legt fest und betreibt, wie mobiles, hybrides und externes Arbeiten sicher ermöglicht wird. Die Routine verbindet Rollen, Datenklassen, Geräte, Netzwerkzugang, physische Umgebung, Verhalten, Support, Incident-Meldung und Managemententscheidungen.

## Typische Risiken

- Wenn schutzbedürftige Informationen in ungeeigneten Umgebungen bearbeitet werden, können Dritte Einblick in Bildschirme, Ausdrucke, Gespräche oder Unterlagen erhalten.
- Wenn private oder unverwaltete Geräte genutzt werden, fehlen Schutzmaßnahmen, Updates, Löschbarkeit und Nachweisfähigkeit.
- Wenn Verbindungen ohne angemessene Absicherung erfolgen, können Zugangsdaten, Sitzungen oder Datenflüsse gefährdet werden.
- Wenn mobile Geräte verloren gehen oder gestohlen werden, kann ohne Verschlüsselung, Sperre und Meldeweg ein Informationsabfluss entstehen.
- Wenn Führungskräfte und Beschäftigte Ausnahmen informell regeln, entstehen uneinheitliche Risiken und unklare Verantwortlichkeiten.

## Trigger

- Einführung oder Änderung von Homeoffice-, Mobile-Work- oder Reise-Regeln.
- Eintritt, Rollenwechsel oder Übernahme einer Rolle mit sensiblen Informationen.
- Ausgabe, Wechsel, Verlust oder Rückgabe mobiler Geräte.
- neues Tool, Cloud-Dienst, VPN-/Zero-Trust-Zugang oder Kollaborationsplattform.
- Arbeit bei Kunden, auf Reisen, in Co-Working-Umgebungen oder an öffentlichen Orten.
- Sicherheitsereignis, Gerätediebstahl, Fehlversand, Shoulder-Surfing-Hinweis oder Regelverstoß.
- turnusmäßiger Review von Remote-Work-Risiken, Gerätebestand und Ausnahmen.

## Rollen und Verantwortung

- **HR / People-Funktion:** verankert Arbeitsmodelle, Onboarding und Regelkommunikation.
- **Führungskräfte:** entscheiden im Rahmen definierter Regeln über Arbeitsorte, Aufgaben und Alltagstransfer.
- **ISMS-Owner / Security-Rolle:** definiert Mindestanforderungen, Risikologik, Meldewege und Reviews.
- **IT-/Plattform Owner:** stellt Geräte, Zugriffsschutz, Verschlüsselung, Updates, Remote-Löschung und Supportprozesse bereit.
- **Information Owner / Fachbereich:** legt fest, welche Daten oder Tätigkeiten außerhalb kontrollierter Standorte zulässig sind.
- **Datenschutz / Legal:** prüft Beschäftigtendaten, Arbeitsortregelungen, personenbezogene Verarbeitung und vertragliche Fragen.
- **Management:** entscheidet über Restrisiken, Ausstattung, Ausnahmen und Kultur-/Produktivitätszielkonflikte.

## Implementierung

### Minimalstart

Ziel: Außerhalb kontrollierter Standorte wird nicht improvisiert, sondern mit klaren Mindestregeln gearbeitet.

1. Die Organisation definiert, für welche Rollen und Tätigkeiten mobiles oder externes Arbeiten zulässig ist.
2. Mindestregeln werden verständlich kommuniziert: Bildschirm schützen, Gespräche beachten, Geräte sperren, Unterlagen sichern, Verlust sofort melden.
3. Kritische Datenklassen oder Tätigkeiten werden benannt, die nur unter zusätzlichen Bedingungen oder nicht außerhalb kontrollierter Standorte bearbeitet werden dürfen.
4. Verwaltete Geräte, starke Authentisierung, Geräteverschlüsselung und sichere Verbindung werden als Standard festgelegt, soweit im Scope erforderlich.
5. Ausnahmen werden mit Begründung, Laufzeit und verantwortlicher Entscheidung dokumentiert.
6. Verlust, Diebstahl oder Verdacht auf Einsichtnahme haben einen sichtbaren Meldeweg.

Minimaler Nachweis:

- Remote-/Mobile-Work-Regel oder kompakte Arbeitsanweisung,
- Zielgruppen- und Tätigkeitsumfang,
- Nachweis Geräteausgabe oder Schutzkonfiguration,
- Kommunikationsnachweis zum Meldeweg,
- Ausnahme- und Incident-Tickets.

### Solide Praxis

Ziel: Sicheres Arbeiten außerhalb kontrollierter Standorte wird risikobasiert und wiederholbar betrieben.

1. Tätigkeiten werden nach Informationsrisiko und Umgebung eingeordnet: Homeoffice, Reise, Kunde, öffentlich, Ausland, Hochrisikoprojekt.
2. Technische Mindestmaßnahmen werden mit Rollen und Datenklassen verbunden: MDM, Festplattenverschlüsselung, MFA, sichere Verbindung, automatische Sperre, Backup, Remote-Löschung.
3. Führungskräfte erhalten Entscheidungsleitlinien, wann Aufgaben außerhalb kontrollierter Standorte ungeeignet sind.
4. Onboarding, Geräteausgabe, Awareness und Incident-Meldung sind miteinander verknüpft.
5. Ausnahmen wie private Geräte, lokale Ausdrucke, Reisen mit sensiblen Daten oder temporäre Sonderzugriffe werden gesondert entschieden.
6. Reviews prüfen Gerätebestand, offene Ausnahmen, gemeldete Vorfälle und wiederkehrende Regelprobleme.

### Fortgeschritten

Ziel: Mobile und hybride Arbeit wird als kontrollierte Betriebsfähigkeit mit Monitoring, Support und Lernschleifen gesteuert.

1. Geräte-Compliance, Zugriffskontext, Patchstand und Verschlüsselungsstatus fließen in Zugriffsentscheidungen ein.
2. Risikoindikatoren wie ungewöhnliche Zugriffe, verlorene Geräte, häufige Ausnahmen oder unsichere Reiseumgebungen werden ausgewertet.
3. Hochrisikorollen erhalten zusätzliche Briefings, Schutzfolien, Reisehinweise, sichere Kommunikationswege oder alternative Arbeitsmodi.
4. Krisen-, BCM- und Remote-Work-Szenarien werden zusammen betrachtet, damit Notbetrieb nicht unsichere Workarounds erzwingt.
5. Management erhält entscheidungsfähige Kennzahlen zu Ausstattungslücken, Ausnahmequote, Incident-Mustern und Investitionsbedarf.

## Ablauf als Routine

1. **Arbeitsbedarf entsteht:** Person, Rolle oder Team will außerhalb kontrollierter Standorte arbeiten.
2. **Tätigkeit einordnen:** Führungskraft und Information Owner prüfen Datenklasse, Aufgabe, Ort und Risiko.
3. **Voraussetzungen prüfen:** Gerät, Authentisierung, Verbindung, Support, Awareness und Meldeweg sind vorhanden.
4. **Freigeben oder begrenzen:** Tätigkeit wird erlaubt, mit Auflagen versehen, an kontrollierten Standort gebunden oder eskaliert.
5. **Durchführen:** Beschäftigte halten Mindestregeln ein und melden Verlust, Fehlverhalten oder Verdachtsmomente.
6. **Nachweis erfassen:** Geräteausgabe, Regelkommunikation, Ausnahme, Incident oder Review werden dokumentiert.
7. **Reviewen:** wiederkehrende Probleme, Ausnahmen und technische Lücken werden geprüft.
8. **Verbessern:** Regeln, Ausstattung, Schulung oder Zugriffslogik werden angepasst.

## Entscheidungen

- Welche Tätigkeiten oder Datenklassen dürfen außerhalb kontrollierter Standorte bearbeitet werden?
- Welche technischen Mindestmaßnahmen sind für welche Rollen Pflicht?
- Sind private Geräte, Ausdrucke, lokale Speicherung oder öffentliche Arbeitsorte zulässig?
- Wer darf Ausnahmen genehmigen und wie lange gelten sie?
- Wie werden Reise-, Auslands- oder Kundenstandort-Situationen bewertet?
- Welche Investitionen sind nötig, damit sicheres Arbeiten nicht an Ausstattungslücken scheitert?

## Evidenz

### Starke Evidenz

- freigegebene Remote-/Mobile-Work-Regel mit Rollen- und Datenklassenbezug,
- Geräteinventar mit Schutzstatus für mobile Geräte,
- Nachweis zu MFA, Verschlüsselung, MDM oder sicherer Verbindung im Scope,
- Onboarding- oder Awareness-Nachweis zum externen Arbeiten,
- Ausnahmeentscheidungen mit Laufzeit,
- Tickets zu Verlust, Diebstahl, Remote-Löschung oder Incident-Triage,
- Reviewprotokoll zu Gerätebestand, Ausnahmen und Vorfällen.

### Schwache Evidenz

- allgemeine Homeoffice-Regel ohne Sicherheitsbezug,
- Tool-Screenshot ohne Zuordnung zu Rollen oder Geräten,
- mündliche Teamabsprachen ohne Nachweis,
- Gerätebestand ohne Schutzstatus,
- Teilnahmequote an Schulung ohne Praxis- oder Meldewegbezug.

### Evidenzlücken

- unverwaltete oder private Geräte im produktiven Zugriff ohne Entscheidung,
- keine Melderoutine für verlorene Geräte oder Einsichtnahme,
- keine Vorgaben für öffentliche Orte, Reisen oder Ausdrucke,
- Ausnahmen ohne Owner oder Ablaufdatum,
- kein Review von Vorfällen und wiederkehrenden Regelproblemen.

## Wirksamkeitsprüfung

Prüffragen:

- Wissen Beschäftigte, was sie außerhalb kontrollierter Standorte tun, lassen und melden müssen?
- Sind mobile Geräte im Scope verwaltet, verschlüsselt und nachvollziehbar zugeordnet?
- Werden Tätigkeiten mit hohem Schutzbedarf vor externer Bearbeitung geprüft?
- Können Verlust oder Diebstahl schnell gemeldet und behandelt werden?
- Sind Ausnahmen befristet und entscheidungsfähig dokumentiert?
- Haben Reviews zu besseren Regeln, Ausstattung oder Schulung geführt?

Mögliche Kennzahlen:

- Anteil mobiler Geräte mit aktuellem Schutzstatus,
- offene Geräte- oder Ausstattungslücken,
- Anzahl und Alter von Remote-Work-Ausnahmen,
- Meldezeit bei Verlust oder Diebstahl,
- Incident-Muster mit Bezug zu mobilem Arbeiten,
- Abdeckung kritischer Rollen durch Zusatzbriefings.

## BSIG-/NIS2-Anschluss

Sicheres Arbeiten außerhalb kontrollierter Standorte ist anschlussfähig an NIS2-orientierte Themen wie Cyberhygiene, Zugriffsschutz, Schulung, Incident Handling, Business Continuity und Schutz kritischer Dienste. Der konkrete Bezug sollte organisationsspezifisch im Anforderungsregister und in Risikoanalysen geprüft werden.

Dieses Artefakt ersetzt keine rechtliche, datenschutzrechtliche oder arbeitsrechtliche Prüfung von Arbeitsmodellen, Monitoring oder Beschäftigtendaten.

## Grenzen

- Dieses Artefakt ist keine Homeoffice-Rechtsberatung und keine arbeitsrechtliche Vorlage.
- Es ersetzt keine Datenschutzprüfung für Monitoring, Geräteverwaltung oder Beschäftigtendaten.
- Es ist keine vollständige technische Mobile-Device-Management-Baseline.
- Es bestätigt keine Konformität oder Sicherheit allein durch eine Remote-Work-Policy.
- Es enthält keine ISO-27002-Texte und keine echten Personen- oder Standortdaten.

## Handoffs

- **HR-Handoff:** Arbeitsmodell, Onboarding, Rollenwechsel, Austritt, arbeitsbezogene Kommunikation.
- **IT-Handoff:** Geräteausgabe, Schutzkonfiguration, Support, Verlustprozess, Remote-Löschung.
- **Datenschutz-/Legal-Handoff:** Beschäftigtendaten, Monitoring, private Geräte, Auslandsarbeit, arbeitsrechtliche Fragen.
- **Access-Handoff:** Zugriff abhängig von Gerätestatus, Rolle, Ort oder Ausnahme.
- **Incident-Handoff:** Verlust, Diebstahl, Fehlversand, verdächtiger Zugriff, mögliche Einsichtnahme durch Dritte.
- **BCM-Handoff:** Notbetrieb, Pandemie-/Krisenarbeit, Ausweicharbeitsplätze und temporäre Workarounds.
- **Management-Handoff:** Ausstattungslücken, Zielkonflikte, dauerhafte Ausnahmen oder akzeptierte Restrisiken.
- **Audit-/Evidence-Handoff:** fehlende Nachweise zu Geräten, Regeln, Ausnahmen oder Vorfällen.

## Typische Fehler

- Homeoffice wird erlaubt, aber Sicherheitsvoraussetzungen werden nicht geprüft.
- Private Geräte werden geduldet, ohne Risikoentscheidung oder technische Mindestanforderung.
- Regelkommunikation erwähnt keine konkreten Meldewege für Verlust oder Verdacht.
- Führungskräfte entscheiden Arbeitsorte ohne Datenklassen- oder Tätigkeitsbezug.
- Ausdrucke, Gespräche und Sichtschutz werden gegenüber technischen Maßnahmen vergessen.
- Geräteinventar und tatsächlicher Nutzungsstatus passen nicht zusammen.
- Ausnahmen werden dauerhaft und verschwinden aus dem Review.

## Fiktives Mini-Beispiel

Ein fiktiver Beratungsbetrieb erlaubt hybrides Arbeiten. Für ein Projekt mit vertraulichen Ausschreibungsunterlagen entscheidet der Projekt Owner, dass Bearbeitung unterwegs nicht zulässig ist und Homeoffice nur mit verwaltetem Gerät, MFA und Sichtschutz erfolgen darf. Ein Mitarbeiter meldet später den Verlust eines Laptops im Zug. IT sperrt das Gerät, startet Remote-Löschung und dokumentiert den Vorgang. Im Review wird beschlossen, Reisebriefings für Projektrollen mit hohem Schutzbedarf einzuführen.

Evidenz:

- Projektbezogene Arbeitsortentscheidung,
- Geräte- und Schutzstatus,
- Kommunikationsnachweis zu Mindestregeln,
- Incident-Ticket zum Geräteverlust,
- Reviewmaßnahme für Reisebriefings.
