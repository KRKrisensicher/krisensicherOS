
# A.8.32 — Änderungssteuerung

## Zweck

Änderungssteuerung sorgt dafür, dass Änderungen an Systemen, Anwendungen, Plattformen, Konfigurationen, Prozessen und Sicherheitsmaßnahmen geplant, bewertet, freigegeben, umgesetzt und überprüft werden. Sie schützt vor unbeabsichtigten Ausfällen, Sicherheitslücken, Datenverlusten und nicht nachvollziehbaren Betriebszuständen.

Der Kern ist nicht ein schweres Change-Board für jede Kleinigkeit, sondern eine risikogerechte Routine: Welche Änderungen brauchen welche Prüfung? Wer entscheidet? Wie werden Notfälle behandelt? Wo entsteht Evidenz?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Änderungsroutine für informationssicherheitsrelevante Systeme und Prozesse. Die Routine verbindet Bedarf, Risiko- und Auswirkungsbewertung, Freigabe, Test, Umsetzung, Rollback, Kommunikation, Nachweis und Lessons Learned.

## Typische Risiken

- Wenn Änderungen ohne Bewertung umgesetzt werden, können Dienste ausfallen oder Schutzmaßnahmen unbeabsichtigt abgeschaltet werden.
- Wenn Sicherheitsauswirkungen nicht geprüft werden, entstehen neue Schwachstellen, Fehlkonfigurationen oder Berechtigungslücken.
- Wenn Notfalländerungen nicht nachträglich reviewed werden, werden Abkürzungen zur Normalpraxis.
- Wenn Rollback und Tests fehlen, verlängern sich Störungen und Incidents.
- Wenn Änderungen nicht dokumentiert werden, können Ursachen bei Vorfällen oder Audits nicht nachvollzogen werden.
- Wenn Change-Prozesse zu schwergewichtig sind, umgehen Teams sie und verlieren dadurch Steuerbarkeit.

## Trigger

- neues Release, Patch, Konfigurationsänderung, Infrastrukturänderung oder Cloud-Anpassung.
- Änderung an Identitäten, Netzwerk, Logging, Backup, Monitoring, Kryptografie oder Sicherheitswerkzeugen.
- Einführung, Wechsel oder Abschaltung eines Systems, Dienstes oder Lieferanten.
- Schwachstelle, Incident, Notfall, Hotfix oder dringender Workaround.
- Änderung an Prozessen, Rollen, Datenflüssen oder Schnittstellen.
- Auditfinding, Kundenanforderung, Risikoentscheidung oder Managementauftrag.
- turnusmäßiger Review von Änderungen, Fehlern und Notfallchanges.

## Rollen und Verantwortung

- **Change Requester:** beschreibt Änderung, Grund, Scope, Risiko, Test- und Rollbackidee.
- **Service Owner / Asset Owner:** bewertet fachliche Auswirkung, Schutzbedarf und Betriebsrisiko.
- **IT-/Plattform Owner:** plant technische Umsetzung, Test, Rollback und Betriebskommunikation.
- **Security-Rolle / ISMS-Owner:** prüft sicherheitsrelevante Änderungen, Ausnahmen und Risikobezug.
- **Change-/Release Owner:** koordiniert Freigabe, Zeitfenster, Abhängigkeiten und Nachverfolgung.
- **Datenschutz / Legal:** prüft Änderungen mit personenbezogenen Daten, Protokollierung, Verträgen oder rechtlichen Zusagen.
- **Management:** entscheidet über hohe Restrisiken, Ressourcen, kritische Go-/No-Go-Fragen oder dauerhafte Abweichungen.

## Implementierung

### Minimalstart

Ziel: kritische Änderungen werden sichtbar, bewertet und nachvollziehbar freigegeben.

1. Die Organisation definiert, welche Änderungen mindestens steuerungspflichtig sind: produktive Systeme, kritische Dienste, Sicherheitskonfigurationen, Zugriffe, Datenflüsse, externe Schnittstellen.
2. Änderungen werden in Ticket, Change-Log oder Maßnahmenregister erfasst.
3. Jeder Change enthält Grund, betroffenes System, Owner, Umsetzungszeitpunkt, Testidee, Rollbackidee und Freigabe.
4. Sicherheitsrelevante oder kritische Änderungen erhalten eine zusätzliche Risiko- oder Security-Prüfung.
5. Notfalländerungen dürfen schnell umgesetzt werden, müssen aber nachträglich dokumentiert und reviewed werden.
6. Fehlgeschlagene Änderungen und wiederholte Notfallchanges werden in Lessons Learned überführt.

Minimaler Nachweis:

- Change- oder Ticketliste,
- Freigabe durch Owner,
- Risiko-/Auswirkungsnotiz,
- Test- oder Rollbacknachweis,
- Nachreview bei Notfalländerungen,
- Maßnahmen bei Fehlern.

### Solide Praxis

Ziel: Änderungen werden nach Risiko klassifiziert und in Betrieb, Entwicklung und ISMS integriert.

1. Changes werden in Kategorien geführt: Standard, normal, kritisch, Notfall, Sicherheitschange.
2. Bewertungslogik berücksichtigt Verfügbarkeit, Vertraulichkeit, Integrität, Datenklassen, Exposition, Abhängigkeiten und Kunden-/Nutzerwirkung.
3. Change-Freigaben sind risikogerecht: kleine Standardänderungen vereinfacht, kritische Änderungen mit Review und Go-/No-Go.
4. Tests, Monitoring, Kommunikationsbedarf und Rollback werden vor Umsetzung geplant.
5. Umsetzung und Ergebnis werden dokumentiert: erfolgreich, rückgerollt, teilweise umgesetzt, offen.
6. Change-Fehler, Incidents und Schwachstellen führen zu Prozessverbesserungen.
7. Management erhält entscheidungsfähige Informationen zu riskanten Changes, technischen Schulden und Ressourcenengpässen.

Starke Evidenz:

- Change-Klassifizierung und Bewertungslogik,
- Tickets mit Risiko, Freigabe, Test und Rollback,
- Release- und Deploymentnachweise,
- Nachreview von Notfalländerungen,
- Lessons-Learned-Maßnahmen,
- Managemententscheidungen bei hohen Restrisiken.

### Fortgeschritten

Ziel: Änderungssteuerung ist automatisiert, risikobasiert und eng mit Entwicklung, Betrieb, Security und Monitoring verbunden.

1. CI/CD, Infrastructure-as-Code, Konfigurationsmanagement und Ticketing sind so verbunden, dass produktive Änderungen nachvollziehbar bleiben.
2. Automatisierte Prüfungen erkennen kritische Änderungen an Sicherheitsgruppen, Identitäten, Logging, Verschlüsselung, Backup oder externen Schnittstellen.
3. Change-Risiko wird durch Assetkritikalität, Exposition, Incident-Historie und Abhängigkeiten unterstützt.
4. Standardchanges werden vorab qualifiziert und regelmäßig überprüft, um Geschwindigkeit ohne Kontrollverlust zu ermöglichen.
5. Monitoring, Telemetrie und Post-Deployment-Checks bestätigen, ob Änderungen wie erwartet wirken.
6. Change-Kennzahlen zeigen nicht nur Anzahl und Geschwindigkeit, sondern Fehlerrate, Notfallanteil, Rollbacks, Sicherheitsauswirkungen und überfällige Reviews.

## Ablauf als Routine

1. **Änderungsbedarf entsteht:** Fachbedarf, Patch, Schwachstelle, Incident, Release, technische Schuld oder Prozessanpassung.
2. **Change erfassen:** Zweck, Scope, betroffenes Asset, Owner, geplantes Zeitfenster und Abhängigkeiten dokumentieren.
3. **Auswirkung bewerten:** Sicherheit, Verfügbarkeit, Daten, Schnittstellen, Nutzer, Lieferanten und Compliance-Anforderungen betrachten, ohne Rechtsbewertung zu behaupten.
4. **Freigabe einholen:** risikogerechte Entscheidung durch Owner, Change-Rolle, Security oder Management.
5. **Umsetzung vorbereiten:** Test, Backup, Rollback, Kommunikation, Monitoring und Verantwortliche klären.
6. **Änderung durchführen:** kontrolliert umsetzen und Abweichungen dokumentieren.
7. **Ergebnis prüfen:** Funktion, Sicherheit, Monitoring, Fehler und offene Punkte bewerten.
8. **Nachweise ablegen:** Ticket, Freigabe, Test, Rollback, Ergebnis und Entscheidungen sichern.
9. **Lernen und eskalieren:** Fehler, Notfallchanges und wiederkehrende Ursachen in Verbesserungen oder Managemententscheidungen überführen.

## Entscheidungen

- Welche Änderungen sind steuerungspflichtig und welche dürfen als Standardchange laufen?
- Welche Änderungen brauchen Security-, Datenschutz-, Architektur- oder Managementprüfung?
- Welche Risiken blockieren eine Umsetzung oder einen Go-live?
- Welche Tests und Rollback-Anforderungen sind für kritische Systeme Mindeststandard?
- Wie werden Notfalländerungen erlaubt, begrenzt und nachträglich reviewed?
- Wann ist Geschwindigkeit wichtiger als vollständige Vorabprüfung und wer trägt die Entscheidung?
- Welche wiederkehrenden Change-Probleme benötigen strukturelle Investitionen?

## Evidenz

### Starke Evidenz

- Change-Tickets mit Scope, Owner, Risiko, Freigabe und Umsetzungsergebnis,
- definierte Change-Kategorien und Freigaberegeln,
- Test-, Deployment-, Backup- oder Rollbacknachweise,
- Security-Review bei sicherheitsrelevanten Änderungen,
- Post-Implementation-Review für kritische oder fehlgeschlagene Changes,
- Notfallchange-Protokolle mit Nachfreigabe,
- Managemententscheidungen bei Restrisiken oder Zielkonflikten.

### Schwache Evidenz

- allgemeine Change-Policy ohne Ticket- oder Reviewnachweise,
- Releasekalender ohne Risiko- oder Freigabeinformationen,
- Chat-Freigaben ohne Bezug zu Scope und Owner,
- automatisierte Deployments ohne nachvollziehbare Genehmigung,
- Notfalländerungen ohne Nachreview,
- Change-Statistik ohne Aussage zu Fehlern oder Sicherheitsauswirkungen.

### Evidenzlücken

- produktive Änderungen außerhalb des Change-Logs,
- fehlende Owner oder betroffene Assets,
- keine Sicherheitsbewertung bei kritischen Konfigurationsänderungen,
- kein Rollbackplan für hohe Risiken,
- wiederholte Notfallchanges ohne Ursachenanalyse,
- fehlende Verbindung zu Incidents, Schwachstellen oder Risikoregister.

## Wirksamkeitsprüfung

Prüffragen:

- Sind kritische produktive Änderungen vollständig und nachvollziehbar erfasst?
- Wird die Tiefe der Prüfung nach Risiko und Kritikalität gesteuert?
- Gibt es Nachweise für Freigabe, Test, Umsetzung und Ergebnisprüfung?
- Werden Notfalländerungen nachträglich reviewed und begrenzt?
- Führen fehlgeschlagene Changes zu Verbesserungen?
- Sind sicherheitsrelevante Änderungen an Zugriff, Logging, Backup, Netzwerk oder Kryptografie gesondert sichtbar?
- Erkennt das Management wiederkehrende Zielkonflikte zwischen Geschwindigkeit, Stabilität und Sicherheit?

Mögliche Kennzahlen:

- Anteil produktiver Changes mit vollständigem Ticket,
- fehlgeschlagene Changes und Rollbackquote,
- Anteil Notfallchanges,
- überfällige Post-Implementation-Reviews,
- sicherheitsrelevante Changes ohne Security-Review,
- Incidents mit Change-Ursache,
- offene technische Schulden aus Change-Reviews.

## BSIG-/NIS2-Anschluss

Änderungssteuerung ist anschlussfähig an NIS2-orientierte Themen wie Risikomanagement, sichere Entwicklung und Wartung, Schwachstellenbehandlung, Incident-Prävention, Cyberhygiene und Aufrechterhaltung kritischer Dienste. Der konkrete Bezug sollte im Anforderungsregister und in der Service-/Assetkritikalität geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung und keine verbindliche Prüfung gesetzlicher Pflichten.

## Grenzen

- Dieses Artefakt ist kein ITIL-Handbuch und kein vollständiges Release-Management-Modell.
- Es ersetzt keine technische Teststrategie, Architekturprüfung oder Betriebssicherheitsanalyse.
- Es garantiert keine Ausfallfreiheit, Sicherheit oder Konformität.
- Es enthält keine ISO-27002-Texte und keine geheimen Konfigurationsdetails.
- Es darf nicht dazu führen, dass kleine Teams durch unnötige Bürokratie zur Umgehung gedrängt werden.

## Handoffs

- **Security-Handoff:** Änderungen an Zugriffen, Netzwerk, Logging, Backup, Kryptografie, Exposition, Sicherheitswerkzeugen oder kritischen Konfigurationen.
- **Datenschutz-/Legal-Handoff:** neue Datenverarbeitung, geänderte Protokollierung, externe Schnittstellen, Vertrags- oder Zusageänderungen.
- **Release-/Development-Handoff:** Codeänderungen, Dependency-Updates, CI/CD, Feature Releases und Hotfixes.
- **Incident-Handoff:** Änderung verursacht Störung, Sicherheitsereignis oder Verdacht auf Kompromittierung.
- **BCM-Handoff:** Änderung betrifft kritische Dienste, Wiederanlauf, Backup, Notbetrieb oder Wartungsfenster.
- **Management-Handoff:** Go-live trotz Restrisiko, wiederholte Change-Fehler, Ressourcenmangel oder technische Schulden.
- **Audit-/Evidence-Handoff:** unvollständige Change-Nachweise, fehlende Nachreviews oder nicht erklärbare Produktivänderungen.

## Typische Fehler

- Jede Änderung wird gleich behandelt; dadurch sind kritische Changes zu leicht oder kleine Changes zu schwerfällig.
- Notfallchanges werden zur normalen Arbeitsweise.
- Security wird erst nach Umsetzung gefragt.
- Rollback wird als „wir spielen das Backup zurück“ behauptet, aber nicht geplant oder getestet.
- Automatisierte Deployments werden mit fehlender Kontrolle verwechselt.
- Changes werden abgeschlossen, obwohl Monitoring oder Nachprüfung fehlen.
- Management bekommt Durchsatzkennzahlen, aber keine Sicht auf Change-Risiken.

## Fiktives Mini-Beispiel

Ein fiktiver Plattformbetreiber möchte die Firewall-Regeln für eine neue Schnittstelle ändern. Der Plattform Owner erstellt ein Change-Ticket mit betroffenen Diensten, gewünschtem Zeitfenster und Rollback. Die Security-Rolle prüft Exposition und Logging. Nach Freigabe wird die Änderung umgesetzt, ein Verbindungstest durchgeführt und das Monitoring kontrolliert. Zwei Tage später zeigt ein Review, dass eine Regel breiter als geplant war. Sie wird korrigiert und als Lessons Learned in die Firewall-Change-Checkliste aufgenommen.

Evidenz:

- Change-Ticket mit Scope und Risiko,
- Security-Freigabe,
- Umsetzungs- und Testnachweis,
- Monitoringprüfung,
- Korrekturticket,
- aktualisierte Checkliste.
