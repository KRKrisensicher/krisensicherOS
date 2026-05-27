
# A.8.11 — Datenmaskierung und Reduktion sensibler Anzeige

## Zweck

Datenmaskierung und reduzierte Anzeige sorgen dafür, dass Menschen, Systeme und Dienstleister nur die sensiblen Details sehen, die sie für ihre Aufgabe wirklich benötigen. Der Kern ist nicht „Daten irgendwie schwärzen“, sondern eine bewusst gestaltete Anzeige- und Verarbeitungsroutine: Welche Felder werden wem vollständig, teilweise, pseudonymisiert, aggregiert oder gar nicht gezeigt?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der sensible Informationen in Anwendungen, Reports, Testdaten, Supportfällen, Protokollen, Exporten und Schnittstellen gezielt minimiert oder maskiert werden. Die Routine verbindet Datenklassifizierung, Rollenbedarf, Zugriff, Entwicklung, Reporting, Datenschutz-/Legal-Handoff und technische Validierung.

## Typische Risiken

- Wenn vollständige sensible Daten in Supportmasken, Reports oder Screenshots erscheinen, können sie unnötig kopiert, geteilt oder offengelegt werden.
- Wenn Produktionsdaten unverändert in Test- oder Schulungsumgebungen genutzt werden, entstehen unnötige Vertraulichkeits- und Datenschutzrisiken.
- Wenn Rollen nur Zugriff auf eine Anwendung erhalten, aber Feldsichtbarkeit nicht differenziert wird, sehen Personen mehr Details als für ihre Aufgabe nötig.
- Wenn Logs, Fehlermeldungen oder Exporte sensible Werte enthalten, gelangen Daten in schwer kontrollierbare Nebenablagen.
- Wenn Maskierung nicht getestet wird, können Sonderfälle, APIs oder Adminansichten die Schutzlogik umgehen.

## Trigger

- neues System, neues Datenfeld, neuer Report, neue Schnittstelle oder neue Supportfunktion.
- Verarbeitung sensibler Daten in Test-, Entwicklungs-, Schulungs- oder Analyseumgebungen.
- Rollenänderung, neuer Dienstleisterzugriff oder neue externe Supportleistung.
- Datenschutz-/Legal-Prüfung, Datenklassifizierungsänderung oder neue Schutzbedarfsbewertung.
- Incident, Datenabfluss, Screenshot-/Exportfinding oder Auditfeststellung.
- Änderung von Logging, Monitoring, Debugging, BI, KI-/Analysefunktionen oder Data Warehouse.
- turnusmäßiger Review von Maskierungsregeln und Stichproben der tatsächlichen Anzeige.

## Rollen und Verantwortung

- **Information Owner / Fachbereich:** bewertet, welche Felder für welche Aufgabe sichtbar sein müssen.
- **Product Owner / Application Owner:** priorisiert Maskierung, Feldberechtigungen und UI-/API-Anforderungen.
- **Entwicklung / Plattformteam:** implementiert Maskierung, Tokenisierung, Pseudonymisierung, Aggregation oder Feldunterdrückung.
- **Datenschutz / Legal:** prüft personenbezogene Daten, Zweckbindung, Testdaten, Reporting und externe Offenlegung.
- **ISMS-Owner / Security-Rolle:** definiert Mindestanforderungen, Reviewlogik, Evidenz und Eskalation.
- **Support-/Operations Owner:** stellt sicher, dass Betriebs- und Supportprozesse mit reduzierter Anzeige arbeitsfähig bleiben.
- **Management:** entscheidet bei Zielkonflikten zwischen Arbeitsfähigkeit, Transparenz, Kosten und Restrisiko.

## Implementierung

### Minimalstart

Ziel: unnötige Anzeige besonders sensibler Felder in kritischen Prozessen reduzieren.

1. Kritische Datenfelder und Anzeigen im ISMS-Scope werden benannt: Identifikatoren, Finanzdaten, Gesundheitsdaten, Geheimnisse, Zugangsdaten, vertrauliche Geschäftsdetails.
2. Für jede kritische Anzeige wird festgelegt, welche Rollen vollständige, teilweise oder keine Sicht benötigen.
3. Mindestens Support-, Reporting-, Export- und Testdatenprozesse werden geprüft.
4. Einfache Maskierungen werden umgesetzt: Teilanzeige, Platzhalter, Aggregation, separate Freigabe für Vollsicht.
5. Ausnahmen werden mit Zweck, Dauer, Owner und Reviewdatum dokumentiert.
6. Eine Stichprobe prüft, ob Maskierung in Oberfläche, Export und Screenshot-Szenario tatsächlich wirkt.

Minimaler Nachweis:

- Liste sensibler Felder oder Datenklassen,
- Rollen-/Anzeigematrix,
- Ticket zur Maskierungsumsetzung,
- Test- oder Screenshotnachweis mit fiktiven Daten,
- Ausnahmeentscheidung mit Wiedervorlage.

### Solide Praxis

Ziel: Maskierung wird als Design- und Reviewroutine betrieben.

1. Datenklassifizierung und Schutzbedarf steuern Anzeige-, Export-, Logging- und Testdatenregeln.
2. Anforderungen an Maskierung werden in Entwicklung, Beschaffung und Änderungsprozesse aufgenommen.
3. Produktiv-, Test-, Schulungs- und Analyseumgebungen werden getrennt betrachtet.
4. APIs, Reports, Suchfunktionen, Adminansichten und Massendownloads werden in die Prüfung einbezogen.
5. Rollenspezifische Vollsicht wird begründet, freigegeben und regelmäßig reviewed.
6. Maskierungsfehler lösen Korrekturtickets, Ursachenanalyse und bei Bedarf Incident-Triage aus.
7. Datenschutz-/Legal-Handoffs werden ausgelöst, wenn personenbezogene oder besonders sensible Daten betroffen sind.

Starke Evidenz:

- Datenfeld-/Schutzbedarfskatalog,
- Rollen- und Anzeigekonzept,
- Entwicklungs- oder Change-Tickets mit Akzeptanzkriterien,
- Testfälle für UI, API, Export, Report und Logs,
- Reviewnachweise zu Vollsicht-Rollen,
- Freigaben und Ausnahmen mit Ablaufdatum,
- Managemententscheidung bei nicht umsetzbarer Reduktion.

### Fortgeschritten

Ziel: sensible Anzeige wird systematisch minimiert und technisch überwacht.

1. Maskierungsregeln werden zentral oder wiederverwendbar über Plattform-, API- oder Datenzugriffsschichten umgesetzt.
2. Testdaten werden synthetisch erzeugt oder kontrolliert anonymisiert/pseudonymisiert, soweit geeignet und geprüft.
3. Data-Loss-Prevention-, Discovery- oder Logging-Prüfungen erkennen sensible Felder in Exporten, Reports und Nebenablagen.
4. Berechtigungen für Vollsicht werden zeitlich begrenzt, fallbezogen oder mit zusätzlicher Freigabe vergeben.
5. Architektur- und Datenschutzprüfungen betrachten Re-Identifizierungsrisiken, Kombination von Datenquellen und Analysezwecke.
6. Kennzahlen zeigen Vollsicht-Rollen, Maskierungsabdeckung, Findings in Logs/Exporten und überfällige Ausnahmen.

## Ablauf als Routine

1. **Anzeige- oder Verarbeitungsbedarf entsteht:** neues Feature, Report, Supportfall, Testumgebung, Export oder Schnittstelle.
2. **Datenfelder klassifizieren:** sensible Felder, Zweck, Rollenbedarf und mögliche Nebenablagen bestimmen.
3. **Sichtbarkeit entscheiden:** vollständig, teilweise, aggregiert, pseudonymisiert, anonymisiert, synthetisch oder gar nicht anzeigen.
4. **Human Gates prüfen:** Datenschutz/Legal einbeziehen, wenn personenbezogene, arbeitsrechtliche oder vertragliche Fragen berührt sind.
5. **Technisch umsetzen:** UI, API, Export, Log, Report und Testdatenregel anpassen.
6. **Testen:** mit fiktiven oder freigegebenen Testdaten prüfen, ob Maskierung in Haupt- und Nebenpfaden wirkt.
7. **Nachweis ablegen:** Entscheidung, Umsetzung, Test und Ausnahmen dokumentieren.
8. **Reviewen:** Rollen mit Vollsicht und kritische Anzeigen regelmäßig prüfen.
9. **Verbessern:** Findings aus Incidents, Audits und Supportpraxis in Designregeln zurückführen.

## Entscheidungen

- Welche Datenfelder sind so sensibel, dass Vollsicht begründet werden muss?
- Welche Rollen benötigen vollständige Werte, welche nur Teilwerte oder aggregierte Informationen?
- Wie werden Exporte, Screenshots, Logs, Suchergebnisse und Reports begrenzt?
- Welche Testdatenstrategie ist für die Organisation realistisch?
- Wann ist Maskierung ausreichend, wann braucht es Zugriffsentzug, Verschlüsselung oder Prozessänderung?
- Wer darf zeitlich begrenzte Vollsicht genehmigen?

## Evidenz

### Starke Evidenz

- aktueller Katalog sensibler Felder und Anzeigen,
- Rollen-/Feldsichtbarkeitsmatrix,
- dokumentierte Design- oder Change-Entscheidungen,
- Testnachweise für Oberfläche, API, Export, Report und Logs,
- Review von Vollsicht- und Ausnahmeberechtigungen,
- Nachweise bereinigter Testdaten oder synthetischer Daten,
- Datenschutz-/Legal-Handoff bei relevanten Datenkategorien.

### Schwache Evidenz

- allgemeine Aussage „Daten werden maskiert“ ohne Feld- und Rollenbezug,
- Screenshot einer einzelnen Maske ohne API-/Exportprüfung,
- Testdatenbank mit unbekannter Herkunft,
- Policy zur Datenminimierung ohne technische Akzeptanzkriterien,
- Rollenliste ohne Prüfung der tatsächlichen Anzeige.

### Evidenzlücken

- sensible Werte in Logs, Fehlermeldungen, BI-Exports oder Tickets,
- Admin- oder Supportansichten ohne Reduktion,
- Produktionsdaten in Testsystemen ohne Prüfung,
- Vollsicht-Rollen ohne Owner oder Review,
- keine Betrachtung von APIs und Massendownloads,
- Ausnahmen ohne Ablaufdatum.

## Wirksamkeitsprüfung

Prüffragen:

- Sind sensible Felder und kritische Anzeigen bekannt?
- Kann begründet werden, welche Rolle welche Details sieht?
- Wirkt Maskierung auch in Exporten, APIs, Logs, Reports und Supportprozessen?
- Werden Test- und Schulungsdaten ohne unnötige Produktionsdetails genutzt?
- Werden Vollsicht-Rollen regelmäßig reviewed und bei Rollenwechseln angepasst?
- Führen Findings zu Korrekturen im Design- oder Entwicklungsprozess?

Mögliche Kennzahlen:

- Anteil kritischer Anwendungen mit Rollen-/Anzeigematrix,
- Anzahl Rollen mit Vollsicht auf sensible Felder,
- Findings sensibler Daten in Logs oder Exporten,
- überfällige Maskierungsmaßnahmen,
- Ausnahmen und abgelaufene Ausnahmen,
- Testabdeckung für UI/API/Export/Log.

## BSIG-/NIS2-Anschluss

Datenmaskierung und reduzierte Anzeige sind anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Zugriffsschutz, sichere Entwicklung, Cyberhygiene, Schutz sensibler Informationen und Incident-Prävention. Für betroffene Organisationen sollte der konkrete Bezug im Anforderungsregister, Datenschutzkonzept und Secure-Development-Prozess geprüft werden.

Dieses Artefakt ersetzt keine Datenschutzbewertung, keine Rechtsberatung und keine verbindliche Prüfung von Anwendbarkeit oder Pflichten.

## Grenzen

- Maskierung ist kein Ersatz für Zugriffskontrolle, Verschlüsselung oder Löschroutine.
- Teilmaskierung kann bei Kombination mit anderen Daten re-identifizierbar sein; dies braucht Human Review.
- Dieses Artefakt definiert keine verbindliche Anonymisierung nach Datenschutzrecht.
- Es enthält keine ISO-27002-Texte und keine Zertifizierungszusage.
- Öffentliche Beispiele verwenden nur fiktive, nicht-sensitive Daten.

## Handoffs

- **Datenschutz-/Legal-Handoff:** personenbezogene Daten, besondere Schutzbedarfe, Testdaten, Re-Identifizierungsrisiko, externe Offenlegung.
- **Entwicklungs-Handoff:** UI, API, Export, Logging, Testdaten, Akzeptanzkriterien.
- **Access-/IAM-Handoff:** Vollsicht-Rollen, privilegierte Ansichten, zeitlich begrenzte Freigaben.
- **Support-/Operations-Handoff:** Arbeitsfähigkeit bei reduzierter Anzeige, Freigabeprozess für Vollsicht im Einzelfall.
- **Incident-Handoff:** sensible Daten in Tickets, Logs, Screenshots oder ungewollten Exporten.
- **Management-Handoff:** Kosten, technische Grenzen, Zielkonflikte mit Fachprozessen, akzeptierte Ausnahmen.
- **Audit-/Evidence-Handoff:** fehlende Testnachweise oder nicht prüfbare Maskierungsregeln.

## Typische Fehler

- Nur die Oberfläche wird maskiert, API und Export bleiben vollständig.
- Support erhält pauschale Vollsicht, weil Einzelfallfreigaben fehlen.
- Produktionsdaten werden für Tests kopiert, ohne Reduktion oder Freigabe.
- Logs enthalten sensible Werte, obwohl die Anwendungsmasken reduziert sind.
- Maskierung wird einmal umgesetzt, aber bei neuen Feldern nicht reviewed.
- Teilmaskierung wird mit Anonymisierung verwechselt.
- Ausnahmen für Vollsicht werden nicht befristet.

## Fiktives Mini-Beispiel

Ein fiktiver Zahlungsdienstleister zeigt im Kundenservice bisher vollständige Kontodaten. Nach einem Review legt der Information Owner fest, dass Support nur die letzten vier Stellen sieht; vollständige Sicht ist nur für einen begründeten Klärfall mit Teamlead-Freigabe möglich. Entwicklung passt Oberfläche, Export und API-Antworten an. Ein Test mit fiktiven Kundendaten zeigt, dass ein CSV-Export noch vollständige Werte enthält; das Finding wird vor Freigabe behoben.

Evidenz:

- Rollen-/Anzeigematrix,
- Change-Ticket mit Akzeptanzkriterien,
- Testnachweis für Maske, API und CSV-Export,
- Freigabeprozess für Vollsicht,
- Reviewnotiz zur behobenen Exportlücke.
