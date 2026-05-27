
# A.5.37 — Dokumentierte Betriebsregeln für Informationsverarbeitung

## Zweck

Dokumentierte Betriebsregeln sorgen dafür, dass Informationsverarbeitung nicht von stillschweigendem Erfahrungswissen, einzelnen Schlüsselpersonen oder improvisierten Arbeitsweisen abhängt. Sie beschreiben, wie Systeme, Daten, Dienste und wiederkehrende Betriebsaufgaben sicher und nachvollziehbar betrieben werden.

Der Kern ist nicht ein Handbuch im Regal, sondern eine nutzbare Betriebslogik: Welche Tätigkeiten müssen wie ausgeführt werden, wer darf abweichen, wann wird eskaliert und welche Nachweise entstehen im Alltag?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine aktuelle, verständliche und rollenbezogene Sammlung von Betriebsregeln für relevante Informationsverarbeitung. Diese Regeln verbinden technische Abläufe, Verantwortlichkeiten, Schutzbedarf, Änderungen, Ausnahmen, Notfallbezug und Review.

## Typische Risiken

- Wenn kritische Betriebsabläufe nur einzelne Personen kennen, entstehen Ausfälle, Fehlbedienung und Abhängigkeiten bei Abwesenheit.
- Wenn Betriebsregeln veraltet sind, werden Systeme nach alten Annahmen betrieben und Schutzmaßnahmen laufen ins Leere.
- Wenn Ausnahmen informell entstehen, werden unsichere Arbeitsweisen dauerhaft und unsichtbar.
- Wenn Betriebs- und Sicherheitsregeln getrennt gepflegt werden, fehlen klare Stop-Punkte bei riskanten Änderungen.
- Wenn Dienstleister nach eigenen Routinen arbeiten, ohne abgestimmte Regeln und Nachweise zu liefern, bleiben Verantwortlichkeiten unklar.

## Trigger

- neuer oder wesentlich geänderter Service, Prozess, Standort, System, Cloud-Dienst oder Dienstleister.
- Änderung von Architektur, Betriebsmodell, Datenklasse, Schutzbedarf oder Verfügbarkeitsanforderung.
- Sicherheitsereignis, Betriebsstörung, Auditfinding, Schwachstelle oder Lessons Learned.
- Rollenwechsel im Betriebsteam oder Übergabe an einen anderen Betreiber.
- neue oder geänderte Vorgaben aus Risikoanalyse, Managemententscheidung, Vertrag oder Anforderungsregister.
- turnusmäßiger Review der Betriebsdokumentation.

## Rollen und Verantwortung

- **Service Owner / Prozess Owner:** legt fest, welche Betriebsregeln für den Dienst notwendig sind und entscheidet fachliche Zielkonflikte.
- **IT-/Plattform Owner:** beschreibt technische Betriebsabläufe, Wartung, Monitoring, Backup, Wiederherstellung und sichere Standardhandlungen.
- **ISMS-Owner / Security-Rolle:** definiert Mindestlogik für Sicherheitsbezug, Review, Ausnahmen und Evidenz.
- **Betriebsteam / Administratoren:** nutzen die Regeln im Alltag und melden Unklarheiten, Abweichungen oder veraltete Inhalte.
- **Change Owner:** stellt sicher, dass Änderungen an Systemen auch Betriebsregeln aktualisieren.
- **Lieferantenmanagement:** bindet externe Betriebsanteile, Nachweise und Eskalationswege ein.
- **Management:** entscheidet über nicht tragbare Restrisiken, Ressourcenlücken und akzeptierte Abweichungen.

## Implementierung

### Minimalstart

Ziel: Kritische Betriebsabläufe sind auffindbar, verantwortet und reviewfähig.

1. Die Organisation benennt die wichtigsten Dienste, Systeme oder Datenverarbeitungsprozesse im ISMS-Scope.
2. Für jedes kritische Objekt wird ein Owner festgelegt.
3. Pro Objekt werden die wichtigsten Betriebsregeln knapp dokumentiert: Start/Stop, Änderung, Zugriff, Backup, Monitoring, Störung, Eskalation.
4. Regeln werden dort abgelegt, wo das Betriebsteam sie tatsächlich findet und nutzt.
5. Änderungen oder Störungen lösen eine Prüfung aus, ob die Regel noch passt.
6. Ausnahmen werden mit Grund, Laufzeit und Wiedervorlage dokumentiert.

Minimaler Nachweis:

- Liste kritischer Dienste oder Systeme mit Owner,
- Betriebsregel oder Runbook für priorisierte Objekte,
- Reviewdatum und Änderungsverlauf,
- Ticket oder Protokoll zu Abweichung, Störung oder Aktualisierung,
- dokumentierte Ausnahmeentscheidung.

### Solide Praxis

Ziel: Betriebsregeln werden als wiederholbare Governance-Routine geführt.

1. Betriebsregeln folgen einer einheitlichen Mindeststruktur: Scope, Owner, Normalbetrieb, Wartung, Zugriff, Monitoring, Backup, Wiederanlauf, Eskalation, Nachweise.
2. Änderungen an Systemen oder Prozessen enthalten einen Check, ob Runbooks und Betriebsregeln angepasst wurden.
3. Kritische Betriebsaufgaben werden mit Checklisten, Vier-Augen-Punkten oder Freigaben unterstützt.
4. Dienstleisterregeln und interne Betriebsregeln werden aufeinander abgestimmt.
5. Störungen, Incidents und Auditfindings führen zu gezielten Verbesserungen.
6. Reviews prüfen nicht nur Existenz, sondern Nutzung, Aktualität und Verständlichkeit.

Starke Evidenz:

- aktueller Runbook-/Betriebsregelindex,
- Change-Tickets mit Dokumentationsprüfung,
- Betriebschecklisten oder Wartungsnachweise,
- Incident- oder Störungs-Lessons-Learned mit Regelanpassung,
- Dienstleisterabstimmung und Eskalationskontakte,
- Ausnahme- und Reviewlog.

### Fortgeschritten

Ziel: Betriebsregeln sind in Tooling, Monitoring und Resilienzroutinen integriert.

1. Runbooks sind mit Ticketing, Monitoring, On-Call-Prozessen und Wissensdatenbank verbunden.
2. Wiederkehrende Betriebsaufgaben werden teilautomatisiert, aber mit klaren menschlichen Freigabepunkten bei Risiko.
3. Notfall-, Wiederanlauf- und Krisenprozesse referenzieren die relevanten Betriebsregeln.
4. Regeländerungen werden versioniert und bei kritischen Diensten durch Peer Review geprüft.
5. Kennzahlen zeigen überfällige Reviews, offene Ausnahmen, Dokumentationslücken und wiederkehrende Betriebsfehler.
6. Management erhält entscheidungsfähige Sicht auf technische Schulden, Wissensabhängigkeiten und Resilienzrisiken.

## Ablauf als Routine

1. **Betriebsbedarf erkennen:** neuer Dienst, Änderung, Störung, Review oder Übergabe.
2. **Scope festlegen:** betroffene Systeme, Daten, Rollen, Schnittstellen und Dienstleister bestimmen.
3. **Regel schreiben oder aktualisieren:** konkrete Arbeitsweise, Zuständigkeit, Stop-Punkte und Nachweise beschreiben.
4. **Praxistauglichkeit prüfen:** Betriebsteam testet Verständlichkeit an einer realistischen Aufgabe.
5. **Freigeben und veröffentlichen:** Owner bestätigt Nutzung und Ablageort.
6. **Im Betrieb nutzen:** Wartung, Störung, Änderung oder Wiederanlauf erzeugt natürliche Evidenz.
7. **Reviewen:** Aktualität, Abweichungen, Lessons Learned und Ausnahmen prüfen.
8. **Eskalieren:** fehlende Ressourcen, nicht betreibbare Regeln oder akzeptierte Abweichungen ins Management geben.

## Entscheidungen

- Für welche Dienste und Prozesse werden zuerst Betriebsregeln benötigt?
- Welche Tätigkeiten brauchen Freigabe, Vier-Augen-Prinzip oder Eskalation?
- Welche Regeln müssen intern geführt werden, welche beim Dienstleister?
- Wie werden veraltete Regeln erkannt und aus dem Betrieb entfernt?
- Wann ist eine Abweichung eine zulässige Ausnahme und wann ein Risikoakzeptanzthema?
- Welche Betriebsrisiken gehören ins Management Review?

## Evidenz

### Starke Evidenz

- Runbooks oder Betriebsregeln mit Owner, Scope, Version und Reviewdatum,
- Nachweise, dass Regeln bei Changes, Wartungen oder Störungen genutzt wurden,
- Aktualisierungen nach Incidents, Tests oder Lessons Learned,
- dokumentierte Ausnahmen mit Laufzeit und Entscheidung,
- Dienstleister-Nachweise zu betriebenen Aufgaben,
- Managemententscheidungen zu Ressourcen, technischen Schulden oder Restrisiken.

### Schwache Evidenz

- altes Betriebshandbuch ohne Owner und Reviewdatum,
- generische Prozessbeschreibung ohne Bezug zu konkreten Diensten,
- Ablage in einem Wiki, das im Betrieb niemand nutzt,
- Change-Nachweis ohne Prüfung der Betriebsdokumentation,
- Dienstleistervertrag ohne operative Nachweise.

### Evidenzlücken

- kritische Dienste ohne Runbook oder Ersatzvertretung,
- keine Verbindung zwischen Changes und Regelaktualisierung,
- Ausnahmen ohne Ablaufdatum,
- Störungen wiederholen sich, ohne dass Regeln verbessert werden,
- externe Betriebsanteile ohne abgestimmte Eskalationswege.

## Wirksamkeitsprüfung

Prüffragen:

- Können Betriebsteams kritische Aufgaben anhand der Regeln sicher durchführen?
- Sind Owner, Reviewdatum und Ablageort für kritische Regeln klar?
- Werden Betriebsregeln nach Änderungen, Störungen und Incidents aktualisiert?
- Sind Ausnahmen befristet und entschieden?
- Sind Dienstleisteranteile mit internen Regeln und Nachweisen verbunden?
- Erkennt das Management wiederkehrende Dokumentations- oder Betriebsrisiken?

Mögliche Kennzahlen:

- Anteil kritischer Dienste mit aktuellem Runbook,
- überfällige Reviews,
- offene Ausnahmen,
- wiederkehrende Störungen durch unklare Betriebsabläufe,
- Changes mit geprüfter Dokumentationsaktualisierung,
- kritische Dienste ohne Vertretungsfähigkeit.

## BSIG-/NIS2-Anschluss

Dokumentierte Betriebsregeln sind anschlussfähig an NIS2-orientierte Themen wie Risikomanagement, Betriebssicherheit, Incident Handling, Business Continuity, Lieferkettensteuerung und Cyberhygiene. Der konkrete Bezug sollte im Anforderungsregister und im ISMS-Review organisationsspezifisch geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung und keine verbindliche Prüfung von Anwendbarkeit oder Nachweispflichten.

## Grenzen

- Dieses Artefakt ist kein vollständiges Betriebshandbuch und keine technische Hardening-Baseline.
- Es ersetzt keine Architektur-, Datenschutz-, Vertrags- oder Notfallplanung.
- Es bestätigt keine Konformität, Zertifizierungsfähigkeit oder gesetzliche Erfüllung.
- Es übernimmt keine ISO-27002-Texte.
- Eine dokumentierte Regel ist nur belastbar, wenn sie im Betrieb genutzt, geprüft und verbessert wird.

## Handoffs

- **Change-Handoff:** System-, Prozess- oder Architekturänderungen, die Betriebsregeln verändern.
- **Incident-/Problem-Handoff:** Störungen, Sicherheitsereignisse oder wiederkehrende Fehler durch unklare Abläufe.
- **BCM-Handoff:** Wiederanlauf, Notbetrieb, kritische Dienste oder Abhängigkeiten.
- **Lieferanten-Handoff:** externe Betriebsaufgaben, Nachweise, Eskalationswege und Servicegrenzen.
- **Management-Handoff:** Ressourcenmangel, technische Schulden, nicht betreibbare Regeln oder akzeptierte Abweichungen.
- **Audit-/Evidence-Handoff:** unklare Owner, veraltete Regeln oder fehlende Nutzungsnachweise.

## Typische Fehler

- Regeln werden einmal geschrieben und nie im Betrieb getestet.
- Runbooks beschreiben Wunschprozesse statt tatsächlich genutzter Abläufe.
- Änderungen an Systemen aktualisieren nicht die Betriebsdokumentation.
- Externe Dienstleister betreiben kritische Teile, ohne abgestimmte Nachweise zu liefern.
- Betriebsregeln enthalten keine Eskalations- oder Stop-Punkte.
- Management sieht Dokumentationsquoten, aber keine Betriebsrisiken.

## Fiktives Mini-Beispiel

Ein fiktiver Mittelständler betreibt ein zentrales ERP-System. Nach einer Störung fällt auf, dass der Wiederanlauf nur von einer Person beherrscht wird. Der Service Owner lässt ein kurzes Runbook mit Startreihenfolge, Ansprechpartnern, Backup-Prüfung und Eskalation erstellen. Beim nächsten Wartungsfenster nutzt ein anderes Teammitglied das Runbook, dokumentiert zwei Unklarheiten und aktualisiert die Regel. Im Management Review wird entschieden, für zwei weitere kritische Dienste ebenfalls Vertretungsfähigkeit aufzubauen.

Evidenz:

- ERP-Runbook mit Owner und Version,
- Wartungsticket mit Nutzung des Runbooks,
- Aktualisierung nach Test,
- Liste weiterer kritischer Dienste,
- Managemententscheidung zur Priorisierung.
