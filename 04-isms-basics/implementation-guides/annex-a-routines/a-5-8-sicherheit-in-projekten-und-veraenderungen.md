
# A.5.8 — Sicherheit in Projekten und Veränderungen

## Zweck

Sicherheit in Projekten und Veränderungen sorgt dafür, dass Informationssicherheit nicht erst nach Go-live oder nach einem Incident betrachtet wird. Neue Vorhaben, Prozessänderungen, technische Changes, organisatorische Umbauten und Lieferantenwechsel werden früh genug auf Sicherheitsrisiken, Verantwortlichkeiten, Evidenz und offene Entscheidungen geprüft.

Der Kern ist kein schweres Freigabeformular, sondern ein praktikabler Sicherheits-Checkpoint: Was ändert sich, welche Risiken entstehen, wer entscheidet und welche Mindestanforderungen müssen vor Umsetzung erfüllt sein?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der Projekte und wesentliche Änderungen nach Risiko und Schutzbedarf in Sicherheitsarbeit überführt werden. Security-Anforderungen, Handoffs, Tests, Ausnahmen und Managemententscheidungen werden in Projekt-, Change- und Beschaffungsabläufe eingebaut.

## Typische Risiken

- Wenn Sicherheit zu spät eingebunden wird, sind Architektur, Lieferanten, Datenflüsse oder Berechtigungen bereits faktisch entschieden.
- Wenn Projekte keine Sicherheits-Owner haben, bleiben Anforderungen, Tests und Abnahmen unklar.
- Wenn Änderungen ohne Risiko- und Schutzbedarfsblick umgesetzt werden, entstehen neue Angriffsflächen, Datenabflüsse oder Betriebsstörungen.
- Wenn Sicherheitsanforderungen generisch bleiben, werden sie im Projektalltag nicht umgesetzt.
- Wenn Ausnahmen nicht entschieden werden, gehen nicht erfüllte Anforderungen unbemerkt in den Betrieb.
- Wenn Changes nicht mit Asset-, Zugriffs-, Lieferanten- oder BCM-Routinen verbunden sind, fehlen Nachweise und Folgearbeiten.

## Trigger

- neues Projekt, Produkt, Service, Prozess, Standort, Tool, Schnittstelle oder Datenverarbeitung.
- wesentliche Änderung an Architektur, Berechtigungen, Datenflüssen, Betriebsmodell, Lieferant oder Cloud-/SaaS-Nutzung.
- geplanter technischer Change mit Sicherheits-, Verfügbarkeits- oder Datenschutzbezug.
- Einführung neuer Technologie, Automatisierung, KI-Funktion, Drittkomponente oder externer Zugriff.
- Sicherheitsereignis, Auditfinding, Schwachstelle oder Lessons Learned mit Änderungsbedarf.
- Projekt-Gate, Architekturreview, Beschaffungsentscheidung, Releasefreigabe oder Managemententscheidung.
- Rückbau, Migration, Stilllegung oder Übergabe in den Betrieb.

## Rollen und Verantwortung

- **Projekt Owner / Product Owner:** verantwortet, dass Sicherheitsanforderungen und Entscheidungen im Vorhaben geplant und nachgehalten werden.
- **Change Owner:** bewertet technische und betriebliche Änderungsrisiken, Tests, Rollback und Freigabe.
- **ISMS-Owner / Security-Rolle:** definiert Sicherheits-Checkpoints, Mindestfragen, Handoffs und Ausnahmebehandlung.
- **Asset Owner / Service Owner:** bewertet Schutzbedarf, Betriebsrisiko und Abnahmefähigkeit.
- **IT-/Plattform- oder Entwicklungsteam:** setzt Sicherheitsmaßnahmen, Tests und technische Nachweise um.
- **Einkauf / Vendor Management:** bindet Sicherheitsanforderungen bei Lieferanten, SaaS und externen Leistungen ein.
- **Datenschutz / Legal:** prüft personenbezogene Daten, Vertragsfragen, Rechtsgrundlagen und externe Kommunikation.
- **Management:** entscheidet über Restrisiken, Budget, Termin-/Sicherheitskonflikte und Ausnahmen.

## Implementierung

### Minimalstart

Ziel: sicherheitsrelevante Projekte und Änderungen früh erkennen und nicht ungeprüft in Betrieb nehmen.

1. Die Organisation definiert einfache Security-Fragen für Projektstart und Change-Antrag: Daten, Nutzer, externe Zugriffe, Internet-Exposition, Lieferanten, Kritikalität, Betriebsabhängigkeiten.
2. Vorhaben mit Sicherheitsbezug erhalten einen Security-Checkpoint und einen verantwortlichen Owner.
3. Mindestanforderungen werden in Aufgaben übersetzt: Zugriff, Logging, Backup, Schwachstellenprüfung, Datenschutz-/Legal-Handoff, Betriebsübergabe.
4. Offene Sicherheitsrisiken werden vor Go-live dokumentiert und entschieden.
5. Änderungen mit hohem Risiko brauchen Freigabe, Testnachweis und Rollback- oder Kompensationsplan.
6. Die Übergabe in den Betrieb aktualisiert Assetinventar, Zugriffsliste, Lieferantenregister und Supportzuständigkeit.

Minimaler Nachweis:

- Security-Checkliste für Projekt oder Change,
- Risikoeinschätzung mit Owner,
- Maßnahmen- oder Handoff-Liste,
- Freigabe oder Ausnahmeentscheidung,
- Betriebsübergabe mit aktualisierten Registern.

### Solide Praxis

Ziel: Security by Design wird in Projekt- und Change-Gates eingebettet.

1. Projekte werden nach Risikoklassen oder Schutzbedarf eingestuft.
2. Je Risikoklasse gibt es passende Sicherheitsaktivitäten: Architekturreview, Datenschutz-Handoff, Lieferantenprüfung, Threat Modeling, Testnachweise, Abnahme.
3. Security-Anforderungen werden als Projekt-Backlog oder Change-Aufgaben geführt, nicht als separates Papier.
4. Abweichungen erhalten Begründung, Laufzeit, Kompensation und Entscheidung.
5. Go-live- oder Releaseentscheidungen enthalten Sicherheitsstatus und offene Restrisiken.
6. Lessons Learned aus Incidents, Audits und Schwachstellen passen Projektstandards an.
7. Projektabschluss aktualisiert Asset-, Daten-, Zugriffs-, Lieferanten- und Notfallinformationen.

Starke Evidenz:

- risikobasierte Projekteinordnung,
- Architektur- oder Sicherheitsreview,
- Sicherheitsanforderungen im Backlog,
- Test-, Scan-, Abnahme- oder Change-Nachweise,
- Ausnahme- und Restrisikoentscheidungen,
- aktualisierte Betriebs- und Registereinträge,
- Projektabschluss mit Lessons Learned.

### Fortgeschritten

Ziel: Sicherheitsentscheidungen sind integraler Bestandteil von Portfolio, Architektur und Change Governance.

1. Projektportfolio und Change-Kalender zeigen sicherheitsrelevante Vorhaben, Risiken, Abhängigkeiten und Ressourcenbedarf.
2. Standard-Controls und technische Baselines werden als wiederverwendbare Bausteine bereitgestellt.
3. Kritische Vorhaben nutzen strukturierte Methoden wie Threat Modeling, Security Acceptance Criteria, Pre-Production-Checks und risikobasierte Tests.
4. Automatisierte Gates in CI/CD, Cloud- oder Change-Prozessen liefern Evidenz, ohne manuelle Bürokratie zu erhöhen.
5. Management erhält entscheidungsfähige Sicht auf nicht erfüllte Anforderungen, akzeptierte Restrisiken, Termin-/Budgetkonflikte und technische Schulden.
6. Wiederkehrende Findings führen zu Architekturentscheidungen, Schulung oder Prozessverbesserung.

## Ablauf als Routine

1. **Vorhaben oder Änderung wird angemeldet:** Projektidee, Change, Release, Migration, Beschaffung oder Stilllegung.
2. **Security-Relevanz prüfen:** Daten, Kritikalität, Exposition, externe Parteien, Berechtigungen, Abhängigkeiten und Betriebswirkung bewerten.
3. **Risikoklasse festlegen:** minimale, normale oder erhöhte Security-Begleitung bestimmen.
4. **Anforderungen ableiten:** konkrete Aufgaben, Handoffs, Tests, Nachweise und Abnahmekriterien festlegen.
5. **Umsetzung begleiten:** offene Punkte in Projekt- oder Change-Backlog verfolgen.
6. **Vor Freigabe prüfen:** erledigte Anforderungen, Ausnahmen, Restrisiken, Rollback und Betriebsübergabe betrachten.
7. **Entscheiden:** Go-live, Verschiebung, Ausnahme, Kompensation oder Management-Handoff.
8. **Nachbereiten:** Register aktualisieren, Lessons Learned erfassen, Routinen verbessern.

## Entscheidungen

- Welche Projekte und Changes brauchen Security-Beteiligung, welche nicht?
- Welche Mindestfragen gelten für jedes Vorhaben?
- Welche Risikoklasse löst Architekturreview, Tests, Datenschutz-/Legal- oder Management-Handoff aus?
- Wer darf mit offenen Sicherheitsmaßnahmen live gehen?
- Welche Zielkonflikte zwischen Termin, Budget, Funktion und Sicherheit müssen entschieden werden?
- Welche Nachweise müssen vor Betriebsübergabe vorliegen?

## Evidenz

### Starke Evidenz

- Projekt- oder Change-Security-Check mit Risikoklasse,
- Security-Anforderungen im Backlog oder Change-Ticket,
- Architektur-, Datenschutz-, Lieferanten- oder Betriebsreview,
- Test-, Scan-, Abnahme- oder Rollback-Nachweise,
- Go-live-Entscheidung mit offenen Risiken,
- Ausnahme mit Kompensation, Ablaufdatum und Owner,
- aktualisierte Asset-, Zugriffs-, Lieferanten- und Betriebsdokumentation.

### Schwache Evidenz

- allgemeine Projektmethodik ohne Security-Fragen,
- einmalige Freigabemail ohne Risikobezug,
- Checkliste mit überall „nicht relevant“ ohne Begründung,
- Sicherheitshinweise außerhalb des Projektbacklogs,
- technische Tests ohne Verbindung zu Schutzbedarf oder Abnahme,
- Go-live-Protokoll ohne offene Restrisiken.

### Evidenzlücken

- keine frühe Security-Prüfung,
- keine Owner für Sicherheitsanforderungen,
- keine Dokumentation von Ausnahmen,
- kein Update von Asset- oder Zugriffsregistern,
- keine Lieferanten- oder Datenschutzprüfung bei relevanten Vorhaben,
- keine Nachweise für Tests, Abnahme oder Betriebsübergabe,
- keine Managemententscheidung bei Termin-/Sicherheitskonflikt.

## Wirksamkeitsprüfung

Prüffragen:

- Werden sicherheitsrelevante Projekte und Changes früh erkannt?
- Sind Sicherheitsanforderungen konkret genug, um umgesetzt und geprüft zu werden?
- Gibt es Nachweise, dass offene Risiken vor Go-live entschieden wurden?
- Werden Register und Betriebsroutinen nach Änderungen aktualisiert?
- Werden Ausnahmen befristet und nachverfolgt?
- Lernen Projekt- und Change-Prozesse aus Incidents, Audits und Findings?

Mögliche Kennzahlen:

- Anteil relevanter Vorhaben mit Security-Check,
- Anzahl offener Security-Anforderungen vor Go-live,
- überfällige Ausnahmen aus Projekten,
- wiederkehrende Findings nach Changes,
- Nacharbeitsaufwand durch zu späte Security-Einbindung,
- Anteil aktualisierter Register nach Betriebsübergabe.

## BSIG-/NIS2-Anschluss

Sicherheit in Projekten und Veränderungen ist anschlussfähig an NIS2-orientiertes Risikomanagement, sichere Beschaffung und Entwicklung, Incident-Prävention, Business Continuity, Lieferkettensicherheit und Managementverantwortung. Für betroffene Organisationen sollte der konkrete Bezug über Anforderungsregister, Projektportfolio, Risikoanalyse und Management Review geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung, Datenschutz-Folgenprüfung oder verbindliche Prüfung regulatorischer Anwendbarkeit.

## Grenzen

- Dieses Artefakt ist keine vollständige Projektmanagement- oder Change-Management-Methode.
- Es ersetzt keine Datenschutz-, Rechts-, Architektur- oder Penetrationstestbewertung.
- Es gibt keine Zertifizierungs-, Konformitäts- oder Sicherheitsgarantie.
- Es enthält keine lizenzpflichtigen Normtexte.
- Es darf nicht als bürokratisches Gate genutzt werden, das Entscheidungen verzögert, ohne Risiken zu klären.

## Handoffs

- **Architektur-Handoff:** neue Plattformen, Schnittstellen, Datenflüsse, Cloud-/SaaS-Modelle oder technische Schulden.
- **Datenschutz-/Legal-Handoff:** personenbezogene Daten, neue Verarbeitung, Verträge, externe Kommunikation oder regulatorische Fragen.
- **Lieferanten-Handoff:** neue oder geänderte Drittleistungen, SaaS, Managed Services oder Supportzugriffe.
- **Incident-/Schwachstellen-Handoff:** Findings, aktive Ausnutzung, Sicherheitsereignis oder remedierende Änderung.
- **BCM-Handoff:** Änderungen an kritischen Services, Wiederanlauf, Abhängigkeiten oder Krisenrollen.
- **Management-Handoff:** Restrisiko, Termin-/Budgetkonflikt, nicht erfüllte Mindestanforderung oder Ausnahme außerhalb Toleranz.
- **Audit-/Evidence-Handoff:** fehlende Nachweise, unklare Freigabe oder lückenhafte Betriebsübergabe.

## Typische Fehler

- Security wird erst kurz vor Go-live gefragt.
- Checklisten werden ausgefüllt, aber Anforderungen landen nicht im Projektbacklog.
- Jede Änderung wird gleich schwer behandelt und blockiert dadurch den Betrieb.
- Ausnahmen werden mündlich akzeptiert und nie wieder geprüft.
- Nach Go-live werden Asset-, Zugriff- und Lieferantenregister nicht aktualisiert.
- Projektteams optimieren Termine, ohne Management über Restrisiken entscheiden zu lassen.
- Technische Tests werden durchgeführt, aber Findings nicht mit Abnahme und Betrieb verbunden.

## Fiktives Mini-Beispiel

Ein fiktiver Fachbereich möchte ein neues SaaS-Tool für Kundenkommunikation einführen. Der Projekt Owner füllt den Security-Check aus: externe Nutzer, personenbezogene Inhalte und API-Anbindung sind relevant. ISMS, Datenschutz, Einkauf und IT werden eingebunden. Vor Go-live werden Rollen, MFA, Datenexport, Lieferantenkontakt und Incident-Meldeweg geklärt. Eine offene Logging-Anforderung wird als befristete Ausnahme mit Management-Wiedervorlage dokumentiert.

Evidenz:

- Security-Check mit Risikoklasse,
- Aufgaben im Projektbacklog,
- Datenschutz- und Lieferanten-Handoff,
- technische Abnahmen zu Zugriff und MFA,
- befristete Ausnahme zur Logging-Anforderung,
- aktualisiertes Asset- und Lieferantenregister.
