
# A.8.34 — Schutz von Informationssystemen während Prüfungen

## Zweck

Prüfungen, Audits, Penetrationstests, Schwachstellenscans und technische Reviews sollen Risiken sichtbar machen, dürfen aber selbst keine unnötigen Risiken für Verfügbarkeit, Vertraulichkeit oder Integrität erzeugen. Diese Routine sorgt dafür, dass Prüfaktivitäten geplant, autorisiert, begrenzt, überwacht und nachbereitet werden.

Der Kern ist nicht „Prüfung erlaubt“, sondern eine sichere Durchführung: Was wird geprüft? Mit welchen Methoden? Wann? Wer ist informiert? Welche Grenzen gelten? Wie wird reagiert, wenn die Prüfung Störungen, Datenzugriff oder Sicherheitsereignisse auslöst?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der Prüfungen an Informationssystemen sicher vorbereitet, genehmigt, durchgeführt, begleitet und nachbereitet werden. Sie verbindet Prüfziel, Systemkritikalität, Betriebsfenster, Zugriff, Datennutzung, Monitoring, Notfallabbruch, Evidenz und Maßnahmenverfolgung.

## Typische Risiken

- Wenn aktive Tests ohne Betriebsabstimmung laufen, können Systeme überlastet, gestört oder unbeabsichtigt verändert werden.
- Wenn Prüfende zu breite Zugriffe erhalten, können vertrauliche Daten oder produktive Funktionen unnötig exponiert werden.
- Wenn Testmethoden, Umfang oder Zeitfenster unklar sind, kann Security Monitoring echte Angriffe und autorisierte Tests nicht unterscheiden.
- Wenn Prüfungen in kritischen Zeiten stattfinden, erhöhen sie Betriebs- und Krisenrisiken.
- Wenn Findings vertrauliche technische Details enthalten und unsicher geteilt werden, entstehen neue Angriffsflächen.
- Wenn Abbruchkriterien fehlen, wird bei Störungen zu spät reagiert.

## Trigger

- interner oder externer Audit mit technischer Systemprüfung.
- Penetrationstest, Red-Team-Übung, Schwachstellenscan, Konfigurationsreview oder Last-/Sicherheitstest.
- Kunden-, Lieferanten- oder regulatorische Anfrage mit Prüfaktivitäten.
- neue kritische Anwendung, größere Architekturänderung oder Go-live-Prüfung.
- Incident Lessons Learned, Schwachstellenwelle oder Managementauftrag.
- wiederkehrender Prüfplan für kritische Systeme.
- Änderung des Prüfumfangs, der Methode, des Dienstleisters oder des Zeitfensters.

## Rollen und Verantwortung

- **Prüfungsauftraggeber / Audit Owner:** definiert Prüfziel, Scope, Erwartungen und Ergebnisverwendung.
- **Asset Owner / Service Owner:** bewertet Betriebsrisiko, Freigabe, Zeitfenster und Abbruchkriterien.
- **IT-/Plattform Owner:** bereitet technische Zugänge, Monitoring, Backup-/Rollback-Bereitschaft und Begleitung vor.
- **Security-Rolle / ISMS-Owner:** koordiniert Prüfgrenzen, Rules of Engagement, Finding-Triage und Maßnahmenverfolgung.
- **Prüfende / externer Dienstleister:** halten Scope, Methode, Meldewege, Geheimhaltung und Abbruchregeln ein.
- **Datenschutz / Legal:** prüft personenbezogene Daten, Protokollierung, Vertraulichkeit, Vertrags- und Haftungsfragen.
- **Management:** entscheidet über Prüfungen an besonders kritischen Systemen, Restrisiken, Ressourcen und Veröffentlichung von Ergebnissen.

## Implementierung

### Minimalstart

Ziel: technische Prüfungen laufen nur mit klarem Auftrag, Scope und Betriebsabsicherung.

1. Jede aktive Prüfung erhält einen Prüfsteckbrief: Ziel, Scope, Systeme, Methode, Zeitraum, Prüfende, Kontakte und Abbruchkriterien.
2. Asset Owner und IT-/Plattform Owner bestätigen, dass Zeitpunkt und Methode zum Betriebsrisiko passen.
3. Zugriffe für Prüfende werden zweckgebunden, befristet und nachvollziehbar eingerichtet.
4. Monitoring, Service Desk oder Incident-Rolle werden informiert, damit Testaktivitäten eingeordnet werden können.
5. Kritische oder produktive Systeme erhalten klare Grenzen: keine destruktiven Tests ohne Sonderfreigabe, keine Datenextraktion ohne Klärung.
6. Findings werden sicher übergeben, priorisiert und in Maßnahmen nachverfolgt.

Minimaler Nachweis:

- Prüfsteckbrief oder Rules of Engagement,
- Freigabe durch Asset-/Service Owner,
- Zugriffsnachweise für Prüfende,
- Information an Betrieb/SOC/Service Desk,
- Finding-Liste mit Ownern,
- Abschluss- oder Nachbereitungsnotiz.

### Solide Praxis

Ziel: Prüfungen sind Teil eines risikobasierten Test- und Verbesserungsprozesses.

1. Prüfarten werden unterschieden: passiver Review, authentifizierter Scan, aktiver Penetrationstest, Social/Physical-Anteil, Red-Team-Übung, Lasttest.
2. Für jede Prüfart gibt es Mindestanforderungen an Scope, Freigabe, Methode, Zeitfenster, Datenumgang und Abbruch.
3. Kritische Systeme werden mit Betriebsfenstern, Kommunikationsplan und Bereitschaft zur Störungsreaktion geprüft.
4. Testkonten, IP-Adressen, Tools und erlaubte Techniken werden dokumentiert.
5. Sensible Findings und technische Details werden in geschützten Kanälen und mit begrenztem Empfängerkreis geteilt.
6. Nach Abschluss werden Zugänge entzogen, Logs geprüft, Findings priorisiert und Maßnahmen verfolgt.
7. Wiederkehrende Findings fließen in Architektur, Schwachstellenmanagement, Secure Development oder Betrieb zurück.

Starke Evidenz:

- genehmigter Prüfplan,
- Rules of Engagement,
- Betriebsfreigabe und Kommunikationsnachweis,
- Zugriff- und Testkontenprotokoll,
- Monitoring-/Abbruchbereitschaft,
- Findings mit Risiko, Owner und Frist,
- Nachweis des Zugriffsentzugs nach Prüfung.

### Fortgeschritten

Ziel: Prüfungen verbessern Sicherheit messbar, ohne den Betrieb unkontrolliert zu gefährden.

1. Prüfplanung ist mit Assetkritikalität, Bedrohungslage, Schwachstellenmanagement und Releaseplanung verbunden.
2. Technische Testumgebungen, Staging oder kontrollierte Produktionsfenster werden risikogerecht gewählt.
3. SOC/Monitoring kann Prüfaktivitäten markieren und gleichzeitig echte Auffälligkeiten erkennen.
4. Prüfende erhalten temporäre Identitäten, kontrollierte Zugriffswege und sichere Ergebnisablagen.
5. Findings werden automatisch oder strukturiert in Risiko-, Ticket- und Maßnahmenmanagement überführt.
6. Lessons Learned prüfen nicht nur Findings, sondern auch Prüfungsdurchführung: Störungen, falsche Alarme, Kommunikationslücken, zu breite Zugriffe.
7. Management erhält entscheidungsfähige Sicht auf kritische Findings, Behebungsrückstände, Testabdeckung und akzeptierte Restrisiken.

## Ablauf als Routine

1. **Prüfbedarf entsteht:** Auditplan, Penetrationstest, Go-live, Incident Lesson Learned, Kundenfrage oder Managementauftrag.
2. **Scope definieren:** Systeme, Schnittstellen, Umgebungen, Daten, Methoden, Ausschlüsse und Testtiefe klären.
3. **Risiko bewerten:** Betriebswirkung, Datenzugriff, Kritikalität, Zeitfenster, Abhängigkeiten und Notfallfähigkeit prüfen.
4. **Freigabe einholen:** Asset Owner, Plattform Owner, Security und bei Bedarf Management, Datenschutz oder Legal einbinden.
5. **Durchführung vorbereiten:** Testkonten, IPs, Kontakte, Kommunikationsplan, Monitoring, Abbruchkriterien und sichere Ablage festlegen.
6. **Prüfung begleiten:** Aktivitäten beobachten, Störungen melden, Scope-Abweichungen stoppen oder neu freigeben.
7. **Ergebnisse sichern:** Findings geschützt übergeben, priorisieren und Maßnahmen zuordnen.
8. **Nachbereiten:** Zugänge entziehen, Logs prüfen, Prüfung bewerten und Lessons Learned dokumentieren.
9. **Verbessern:** Findings und Durchführungsprobleme in Betrieb, Entwicklung, Architektur und Risikomanagement zurückspielen.

## Entscheidungen

- Welche Prüfmethoden sind für produktive Systeme zulässig?
- Wann muss in Test/Staging statt Produktion geprüft werden?
- Wer darf destruktive, invasive oder datenintensive Prüfungen freigeben?
- Welche Systeme, Zeitfenster oder Funktionen sind aus Betriebsgründen ausgeschlossen?
- Welche Daten dürfen Prüfende sehen, speichern oder exportieren?
- Welche Findings müssen sofort als Incident oder Managementthema eskaliert werden?
- Wann werden Prüfungsrisiken höher bewertet als der Nutzen der Prüfung?

## Evidenz

### Starke Evidenz

- Prüfauftrag mit Ziel, Scope, Methode, Zeitraum und Verantwortlichen,
- genehmigte Rules of Engagement,
- Betriebs- und Security-Freigabe,
- Kommunikationsnachweis an SOC, Service Desk oder Betrieb,
- Testkonten-/Zugriffsnachweise mit Befristung,
- geschützte Finding-Übergabe,
- Maßnahmenlog mit Ownern und Fristen,
- Abschlussnotiz inklusive Zugriffsentzug und Lessons Learned.

### Schwache Evidenz

- Prüfbericht ohne vorherige Freigabe oder Scope,
- Kalendereintrag „Pentest“ ohne Methoden- und Kontaktangaben,
- pauschale Adminzugänge für Prüfende,
- Findings per ungeschütztem Verteiler,
- Scanprotokoll ohne Betriebsabstimmung,
- Abschlussbericht ohne Maßnahmenverfolgung.

### Evidenzlücken

- unbekannte Prüfaktivitäten im Produktivnetz,
- keine Abbruchkriterien oder Notfallkontakte,
- keine Klärung des Datenzugriffs,
- Prüfkonten bleiben nach Abschluss aktiv,
- kritische Findings ohne Owner oder Frist,
- Monitoring kann Testaktivitäten nicht von Angriffen unterscheiden,
- keine Nachbereitung von durch Prüfungen verursachten Störungen.

## Wirksamkeitsprüfung

Prüffragen:

- Gibt es für aktive Prüfungen einen genehmigten Scope und klare Grenzen?
- Sind Asset Owner, Betrieb und Security vor Prüfungsbeginn informiert und entscheidungsfähig?
- Werden Prüfzugänge befristet und nach Abschluss entzogen?
- Sind Abbruchkriterien und Notfallkontakte bekannt?
- Werden sensible Findings geschützt geteilt und nachverfolgt?
- Haben Prüfungen zu Verbesserungen geführt, nicht nur zu Berichten?
- Wurden Störungen, Fehlalarme oder Scope-Abweichungen nachbereitet?

Mögliche Kennzahlen:

- Anteil aktiver Prüfungen mit vollständigem Prüfsteckbrief,
- Prüfkonten nach Abschluss noch aktiv,
- kritische Findings ohne Owner oder Frist,
- prüfungsbedingte Störungen,
- überfällige Maßnahmen aus Prüfungen,
- wiederkehrende Findings,
- Prüfungen ohne Nachbereitung.

## BSIG-/NIS2-Anschluss

Der Schutz von Informationssystemen während Prüfungen ist anschlussfähig an NIS2-orientierte Themen wie Risikomanagement, Sicherheitsprüfung, Schwachstellenbehandlung, Incident-Prävention, Cyberhygiene und sichere Betriebsführung. Der konkrete Bezug sollte im Anforderungsregister, Prüfplan und Management Review organisationsspezifisch geprüft werden.

Dieses Artefakt ersetzt keine rechtliche, datenschutzrechtliche oder vertragliche Bewertung von Prüfungen und Ergebnisweitergaben.

## Grenzen

- Dieses Artefakt ist kein vollständiger Penetrationstest-Standard und keine technische Testmethodik.
- Es ersetzt keine rechtliche Prüfung von Testfreigaben, Haftung, Datenschutz oder Kundenkommunikation.
- Es garantiert keine sichere oder störungsfreie Prüfung.
- Es enthält keine ISO-27002-Texte und keine vertraulichen System- oder Schwachstellendetails.
- Es darf nicht als Freigabe für destruktive Tests ohne menschliche Entscheidung genutzt werden.

## Handoffs

- **Betriebs-/Service-Handoff:** Produktivsysteme, Wartungsfenster, Monitoring, Störungsbereitschaft und Abbruchkriterien.
- **Security-/SOC-Handoff:** Testaktivitäten, Quell-IP-Adressen, Zeitfenster, erlaubte Techniken und Incident-Abgrenzung.
- **Datenschutz-/Legal-Handoff:** Zugriff auf personenbezogene Daten, Datenexporte, Verträge, Geheimhaltung, Haftung oder Ergebnisweitergabe.
- **Vendor-Handoff:** externe Prüfende, Unterauftragnehmer, Toolnutzung, Nachweise und sichere Ergebnisablage.
- **Incident-Handoff:** aktive Ausnutzung, unerwartete kritische Schwachstelle, Datenabflussverdacht oder prüfungsbedingte Störung.
- **Change-/Release-Handoff:** Prüfungen im Go-live-Kontext, Testfenster, Rollback und Maßnahmenumsetzung.
- **Management-Handoff:** Prüfung kritischer Systeme, hohe Restrisiken, nicht behebbare Findings oder Veröffentlichung von Ergebnissen.

## Typische Fehler

- Penetrationstests starten ohne Betriebskontakt und Abbruchregel.
- Prüfende erhalten breite Dauerzugänge, die nach Abschluss aktiv bleiben.
- Der Prüfbericht wird abgelegt, aber Findings werden nicht gesteuert.
- Kritische Tests laufen in Hochlast- oder Sperrzeiten.
- SOC/Monitoring wird nicht informiert und behandelt Tests entweder als Fehlalarm oder übersieht echte Angriffe.
- Sensible Findings werden zu breit verteilt.
- Aus Angst vor Störungen werden nur harmlose Prüfungen durchgeführt, sodass relevante Risiken unsichtbar bleiben.

## Fiktives Mini-Beispiel

Ein fiktiver Betreiber eines Kundenportals plant einen externen Penetrationstest. Der Security Owner erstellt Rules of Engagement mit Scope, Testfenster, erlaubten Methoden, Kontaktkette und Abbruchkriterien. Der Service Owner sperrt ein Hochlast-Zeitfenster aus. Das SOC erhält Quell-IP-Adressen und Testzeiten. Nach dem Test werden zwei kritische Findings in Tickets überführt, die Testkonten deaktiviert und eine kurze Nachbereitung dokumentiert. Ein Finding zu unsicherer Session-Konfiguration wird zusätzlich in den Secure-Development-Standard aufgenommen.

Evidenz:

- Prüfauftrag und Rules of Engagement,
- Betriebsfreigabe,
- SOC-Kommunikation,
- Testkontenprotokoll,
- Finding-Tickets,
- Zugriffsentzug,
- Lessons-Learned-Notiz.
