
# A.5.2 — Rollen und Zuständigkeiten für Informationssicherheit

## Zweck

Rollen und Zuständigkeiten sorgen dafür, dass Informationssicherheit nicht zwischen Management, IT, Fachbereichen und Dienstleistern liegen bleibt. Jede relevante Sicherheitsaufgabe braucht eine verantwortliche Rolle, klare Entscheidungsrechte, Stellvertretung und einen Weg zur Eskalation.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Rollenroutine für Informationssicherheit. Für zentrale Sicherheitsaufgaben ist klar, wer verantwortet, wer mitwirkt, wer prüft, wer entscheidet und wann Management oder Spezialrollen einbezogen werden.

## Typische Risiken

- Wenn Rollen nur auf Papier benannt sind, bleiben Maßnahmen, Reviews und Ausnahmen unbearbeitet.
- Wenn Owner keine Entscheidungskompetenz haben, werden Risiken informell akzeptiert.
- Wenn IT als allein verantwortlich gilt, fehlen fachliche Entscheidungen zu Schutzbedarf, Daten und Prozessen.
- Wenn Stellvertretungen fehlen, bleiben Incidents, Reviews oder Freigaben bei Abwesenheit liegen.
- Wenn Dienstleisterzuständigkeiten unklar sind, entstehen Lücken zwischen Vertrag, Betrieb und Nachweis.
- Wenn mehrere Rollen dieselbe Aufgabe „irgendwie“ verantworten, wird niemand rechenschaftsfähig.

## Trigger

- Aufbau oder Änderung des ISMS, neuer Scope oder neue Sicherheitsroutine.
- neue Systeme, Prozesse, Datenklassen, Standorte oder Lieferanten.
- Rollenwechsel, Reorganisation, Eintritt oder Austritt relevanter Verantwortungsträger.
- Sicherheitsereignis, Auditfinding, überfällige Maßnahme oder Eskalation.
- Managemententscheidung zu Risiko, Budget, Priorität oder Ressourcenkonflikt.
- regelmäßiger Rollen- und Verantwortlichkeitsreview.

## Rollen und Verantwortung

- **Management:** bestätigt Verantwortungsmodell, Entscheidungsrechte, Eskalationswege und Ressourcen.
- **ISMS-Owner / Security-Rolle:** pflegt Rollenmatrix, Mindestzuständigkeiten, Reviewrhythmus und Evidenzlogik.
- **Risk Owner:** verantwortet konkrete Risiken, Maßnahmen, Akzeptanzen und Eskalationen.
- **Asset Owner / Information Owner:** entscheidet fachlich über Schutzbedarf, Nutzung und Zugriff.
- **Prozess Owner:** integriert Sicherheitsanforderungen in Arbeitsabläufe und Kontrollen.
- **IT-/Plattform Owner:** verantwortet technische Umsetzung, Betriebsnachweise und technische Risiken im eigenen Bereich.
- **HR / People-Funktion:** unterstützt Rollenwechsel, Stellenprofile, Onboarding und Stellvertretungen.
- **Dienstleister-/Vendor Owner:** steuert externe Verantwortlichkeiten, Nachweise und Eskalationskontakte.

## Implementierung

### Minimalstart

Ziel: Für die wichtigsten Sicherheitsaufgaben gibt es einen benannten Owner und Eskalationspunkt.

1. Die Organisation listet zentrale Sicherheitsroutinen: Risiko, Zugriff, Incident, Lieferanten, Awareness, Schwachstellen, Backup, BCM, Policies.
2. Für jede Routine wird ein primärer Owner benannt.
3. Stellvertretung und Eskalationspunkt werden mindestens für kritische Routinen festgelegt.
4. Owner bestätigen ihren Verantwortungsbereich und offene Entscheidungsgrenzen.
5. Unklare oder nicht besetzte Rollen werden als Managementthema dokumentiert.
6. Ein Reviewtermin prüft Aktualität nach Reorganisation oder Rollenwechseln.

Minimaler Nachweis:

- Rollen-/Zuständigkeitsmatrix,
- Owner-Bestätigung oder Managementfreigabe,
- Liste offener Rollenlücken,
- Eskalationspfad,
- Reviewdatum.

### Solide Praxis

Ziel: Rollen sind mit Aufgaben, Entscheidungen, Evidenz und Stellvertretungen verbunden.

1. Für zentrale Routinen wird beschrieben: verantwortlich, mitwirkend, prüfend, entscheidend, informiert.
2. Entscheidungsrechte werden geklärt: Risikoakzeptanz, Ausnahme, Budget, Priorität, externe Kommunikation.
3. Rollen werden in Onboarding, Stellenprofilen, Prozessbeschreibungen oder Betriebsdokumentation referenziert.
4. Dienstleisterrollen werden mit internen Ownern gekoppelt, damit Verantwortung nicht ausgelagert verschwindet.
5. Überfällige Maßnahmen, unklare Owner oder wiederkehrende Eskalationen fließen in Management Review.
6. Rollenänderungen werden mit HR-, Zugriff- und Wissensübergaberoutinen verbunden.

### Fortgeschritten

Ziel: Verantwortlichkeiten werden als aktives Governance-System betrieben.

1. Rollenmatrix, Assetinventar, Risikoregister, Maßnahmenlog und Evidence-Pack sind miteinander verbunden.
2. Workflows verhindern Tickets, Risiken oder Findings ohne Owner.
3. Stellvertretungen, Kompetenzanforderungen und Kapazitätsrisiken werden regelmäßig geprüft.
4. Management sieht Rollenengpässe, Single Points of Failure und nicht entscheidbare Konflikte.
5. Übungen oder Tabletop-Szenarien testen, ob Rollen im Incident- oder Krisenfall funktionieren.
6. Rollen werden bei Organisationsentwicklung und neuen Services frühzeitig angepasst.

## Ablauf als Routine

1. **Aufgabe oder Änderung erkennen:** neue Routine, neues Asset, Finding, Incident, Rollenwechsel oder Reorganisation.
2. **Verantwortungsbedarf bestimmen:** Welche Entscheidung, Umsetzung, Prüfung oder Eskalation ist nötig?
3. **Owner zuweisen:** primäre Rolle, Stellvertretung und beteiligte Rollen festlegen.
4. **Entscheidungsrechte klären:** Was darf die Rolle selbst entscheiden, was muss eskaliert werden?
5. **In Register übernehmen:** Rollenmatrix, Risikoregister, Prozessdokumentation oder Ticketing aktualisieren.
6. **Kommunizieren:** betroffene Personen und Schnittstellen informieren.
7. **Wirksamkeit prüfen:** offene Maßnahmen, Verzögerungen, Findings und Eskalationen auswerten.
8. **Anpassen:** Rollen, Kapazität, Schulung oder Managemententscheidung nachziehen.

## Entscheidungen

- Welche Sicherheitsaufgaben sind kritisch genug für explizite Owner und Stellvertretung?
- Wer darf Risiken, Ausnahmen und Fristverlängerungen akzeptieren?
- Welche Verantwortlichkeiten bleiben intern, auch wenn Dienstleister operative Aufgaben übernehmen?
- Welche Rollen brauchen besondere Befähigung oder Managementrückendeckung?
- Wann wird eine Rollenlücke zum Managementthema?
- Wie werden Verantwortlichkeiten bei Reorganisationen aktuell gehalten?

## Evidenz

### Starke Evidenz

- aktuelle Rollen- und Zuständigkeitsmatrix mit Scope,
- Owner-Bestätigungen für kritische Routinen oder Assets,
- dokumentierte Stellvertretungen und Eskalationswege,
- Maßnahmen-, Risiko- oder Finding-Listen mit klaren Ownern,
- Managemententscheidungen zu Rollenlücken oder Ressourcen,
- Nachweis, dass Rollenänderungen in Zugriffe und Routinen übertragen wurden.

### Schwache Evidenz

- Organigramm ohne Sicherheitsaufgaben,
- Policy mit Rollenbezeichnungen ohne Personen oder Funktionen,
- alte RACI-Tabelle ohne Reviewdatum,
- Tickets mit Teamnamen statt verantwortlichem Owner,
- Dienstleistervertrag ohne internen Gegenpart.

### Evidenzlücken

- Risiken oder Maßnahmen ohne Owner,
- keine Stellvertretung für kritische Sicherheitsrollen,
- unklare Risikoakzeptanzbefugnis,
- Rollenwechsel ohne Übergabe,
- externe Zuständigkeiten ohne interne Steuerung,
- wiederkehrende Findings wegen „niemand zuständig“.

## Wirksamkeitsprüfung

Prüffragen:

- Hat jede kritische Sicherheitsroutine einen Owner und eine Stellvertretung?
- Können Owner ihre Entscheidungen, Grenzen und Eskalationswege erklären?
- Werden Rollen bei Eintritt, Wechsel, Austritt und Reorganisation aktualisiert?
- Haben Risiken, Maßnahmen und Findings verantwortliche Personen oder Funktionen?
- Werden Dienstleisteraufgaben intern gesteuert?
- Erkennt Management Kapazitäts- und Kompetenzlücken?

Mögliche Kennzahlen:

- Anteil kritischer Routinen mit Owner und Stellvertretung,
- offene Maßnahmen ohne Owner,
- überfällige Reviews wegen fehlender Zuständigkeit,
- Rollenlücken im Management Review,
- Findings mit Ursache „unklare Verantwortung“,
- Zeit bis Owner-Zuweisung bei neuen Findings.

## BSIG-/NIS2-Anschluss

Klare Rollen und Zuständigkeiten sind anschlussfähig an NIS2-orientierte Governance, Managementaufsicht, Risikomanagement, Incident-Fähigkeit und Nachweisführung. Für betroffene Organisationen sollte im Anforderungsregister geprüft werden, welche Rollen, Entscheidungsrechte und Nachweise relevant sind.

Dieses Artefakt trifft keine verbindliche Aussage zur rechtlichen Anwendbarkeit oder zur persönlichen Verantwortlichkeit einzelner Personen.

## Grenzen

- Keine Rechtsberatung zu Organpflichten oder persönlicher Haftung.
- Keine Datenschutzberatung zu Rollen im Datenschutzrecht.
- Keine Zertifizierungs- oder Konformitätszusage.
- Keine Organisationsentscheidung durch Vorlagen oder Hilfsmittel.
- Keine wirksame Kontrolle, wenn Rollen ohne Zeit, Kompetenz oder Entscheidungsrecht benannt werden.

## Handoffs

- **Management-Handoff:** Rollenlücken, Kapazitätsprobleme, unklare Entscheidungsrechte, nicht akzeptierbare Single Points of Failure.
- **HR-Handoff:** Rollenwechsel, Stellenprofile, Onboarding, Austritt, Stellvertretung und Befähigung.
- **Risk-Handoff:** Risiken oder Maßnahmen ohne Owner, offene Risikoakzeptanz.
- **Vendor-Handoff:** externe Aufgaben, Dienstleisterkontakte, Nachweise und Eskalationspfade.
- **Incident-/BCM-Handoff:** Rollen für Meldewege, Krisenkommunikation, Wiederanlauf und Entscheidung im Ereignisfall.
- **Audit-/Evidence-Handoff:** Nachweise zu Rollen, Entscheidungen, Übergaben und dokumentiertem Prüfstand.

## Typische Fehler

- Rollen werden benannt, aber nicht mit Aufgaben oder Entscheidungen gefüllt.
- Eine zentrale Security-Rolle wird für alles verantwortlich gemacht.
- Fachbereiche liefern keine Owner für Informationen oder Prozesse.
- Stellvertretungen existieren nur informell.
- Dienstleister werden als Verantwortungsersatz verstanden.
- Rollenmatrix wird nach Reorganisationen nicht aktualisiert.
- Management bekommt Rollenlücken nicht als Entscheidungsfrage vorgelegt.

## Fiktives Mini-Beispiel

Ein fiktiver Softwareanbieter stellt fest, dass Schwachstellen-Tickets oft wochenlang ohne Entscheidung liegen. Der ISMS-Owner erstellt eine Rollenmatrix: Product Owner bewerten Geschäftsrisiko, Plattform Owner behandeln technische Findings, Management entscheidet über überfällige kritische Ausnahmen. HR ergänzt die Security-Rollen in das Onboarding neuer Führungskräfte.

Evidenz:

- Rollenmatrix für Schwachstellenroutine,
- Owner-Bestätigung der Product und Plattform Owner,
- Eskalationsregel für kritische Ausnahmen,
- aktualisierter Onboarding-Baustein,
- Reviewnotiz nach drei Monaten mit weniger ownerlosen Tickets.
