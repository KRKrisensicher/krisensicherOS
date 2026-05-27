
# A.8.13 — Datensicherung

## Zweck

Datensicherung sorgt dafür, dass Informationen und Systeme nach Fehlern, Angriffen, Fehlbedienung, Ausfall oder Datenverlust wiederhergestellt werden können. Der Wert liegt nicht im vorhandenen Backupjob, sondern in einer betriebenen Restore-Fähigkeit: Was muss in welcher Zeit, mit welchem Datenstand, von wem und unter welchen Bedingungen wiederherstellbar sein?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine für Planung, Durchführung, Schutz, Überwachung und Wiederherstellung von Backups. Die Routine verbindet Assetkritikalität, RTO/RPO, Backupumfang, Zugriffsschutz, Verschlüsselung, Offline-/Immutable-Schutz, Restore-Tests, Incident Response, BCM und Managemententscheidungen.

## Typische Risiken

- Wenn Backups zwar laufen, aber nie wiederhergestellt werden, bleibt die tatsächliche Recovery-Fähigkeit unbekannt.
- Wenn kritische Systeme nicht vollständig oder nicht häufig genug gesichert werden, entstehen nicht tragbare Datenverluste.
- Wenn Backups mit denselben Konten oder Netzpfaden erreichbar sind wie Produktivsysteme, können Ransomware oder Fehlbedienung auch Sicherungen zerstören.
- Wenn SaaS-, Cloud-, Datenbank- oder Konfigurationsdaten nicht im Scope sind, fehlen zentrale Wiederherstellungsbausteine.
- Wenn Restore-Ziele nicht mit Fachbereichen und BCM abgestimmt sind, passen technische Backups nicht zum Krisenbedarf.

## Trigger

- neues System, neue Datenbank, neue SaaS-Nutzung, neue Cloud-Ressource oder geänderter Service.
- Änderung von Kritikalität, RTO/RPO, Datenklasse, Architektur oder Betriebsmodell.
- Incident, Ransomware-Verdacht, Fehlbedienung, Datenverlust oder Restore-Anforderung.
- Backupfehler, Monitoring-Treffer, abgelaufene Jobs oder Kapazitätswarnung.
- Migration, Systemstilllegung, Release, Infrastrukturwechsel oder Lieferantenwechsel.
- BCM-/Notfallübung, Auditfinding, Managementfrage oder turnusmäßiger Restore-Test.
- Änderung von Verschlüsselung, Schlüsselmanagement, Zugriffen oder Aufbewahrungsdauer.

## Rollen und Verantwortung

- **Service Owner / Fachbereich:** legt Wiederanlaufbedarf, Datenverlusttoleranz und Priorität fest.
- **IT-/Plattform Owner:** plant, betreibt, überwacht und testet Backup- und Restoreverfahren.
- **Datenbank-/Application Owner:** stellt Konsistenz, Applikationsabhängigkeiten und Wiederherstellungsreihenfolge sicher.
- **BCM-Verantwortliche:** verbinden Backups mit Notbetrieb, Wiederanlaufplanung und Übungen.
- **ISMS-Owner / Security-Rolle:** definiert Schutzanforderungen, Evidenzlogik, Risiko- und Eskalationswege.
- **Datenschutz / Legal:** prüft personenbezogene Daten, Aufbewahrung, Löschung, Verschlüsselung und externe Speicherung.
- **Management:** entscheidet über Kosten, Recovery-Ziele, Restrisiken, Ausnahmen und Ressourcen.

## Implementierung

### Minimalstart

Ziel: kritische Daten wiederherstellbar machen und nicht nur Backupjobs betreiben.

1. Die wichtigsten Systeme und Datenbestände im ISMS-Scope werden mit Ownern benannt.
2. Für jedes kritische System werden gewünschter Datenstand und Wiederanlaufzeit grob festgelegt.
3. Backupjobs werden eingerichtet, überwacht und bei Fehlern nachverfolgt.
4. Mindestens ein Restore-Test pro kritischem Backupbereich wird geplant und dokumentiert.
5. Zugriffe auf Backups werden eingeschränkt und gesondert betrachtet.
6. Ausnahmen oder nicht gesicherte Systeme werden mit Risiko und Wiedervorlage dokumentiert.

Minimaler Nachweis:

- Liste kritischer Systeme mit Backupstatus,
- Backupjob- und Fehlerprotokolle,
- Restore-Testnachweis,
- Zugriffsliste für Backupadministration,
- Ausnahme- oder Risikoentscheidung.

### Solide Praxis

Ziel: Backups werden risikobasiert, geschützt und mit Wiederanlaufplanung verbunden.

1. RTO/RPO werden mit Fachbereichen und BCM abgestimmt und je Service dokumentiert.
2. Backupumfang umfasst Daten, Konfigurationen, Schlüsselabhängigkeiten, Infrastrukturcode und relevante SaaS-/Cloud-Daten.
3. Backups werden gegen Manipulation, Verschlüsselung durch Angreifer und unbefugten Zugriff geschützt.
4. Restore-Tests prüfen nicht nur einzelne Dateien, sondern auch Datenbank-, Applikations- oder Service-Wiederherstellung.
5. Backupfehler lösen Tickets, Eskalationen und Ursachenanalyse aus.
6. Aufbewahrungsdauer, Löschlogik und Speicherorte werden mit Legal/Datenschutz geprüft, wenn relevant.
7. Ergebnisse fließen in ISMS-Review, BCM-Übungen und Management Review.

Starke Evidenz:

- Service-/Backupmatrix mit RTO/RPO,
- Backupkonfiguration und Jobhistorie,
- Fehlertickets und Korrekturmaßnahmen,
- Restore-Testprotokolle mit Ergebnis und Dauer,
- Nachweis geschützter Backupzugriffe,
- Dokumentation von Aufbewahrung und Speicherort,
- Managemententscheidung bei nicht erfüllten Recovery-Zielen.

### Fortgeschritten

Ziel: Recovery-Fähigkeit wird belastbar, getestet und in Krisenfähigkeit integriert.

1. Backup- und Restoreprozesse sind mit CMDB, Monitoring, SIEM, Ticketing und BCM-Plänen verbunden.
2. Kritische Sicherungen werden immutable, offline, getrennt administriert oder anderweitig gegen Kompromittierung geschützt.
3. Restore-Tests umfassen Abhängigkeiten, Reihenfolgen, Rollen, Kommunikationswege und realistische Ausfallannahmen.
4. Ransomware- und Disaster-Recovery-Szenarien werden in Übungen integriert.
5. Kennzahlen zeigen Backupabdeckung, Fehler, erfolgreiche Restores, getestete Systeme, Restore-Dauer und Lücken gegenüber RTO/RPO.
6. Schlüssel, Secrets, Konfigurationen und Identitätsdienste werden als Recovery-Abhängigkeiten gesondert behandelt.

## Ablauf als Routine

1. **Backupbedarf bestimmen:** Service, Datenklasse, Kritikalität, RTO/RPO, Abhängigkeiten und Owner klären.
2. **Backupdesign festlegen:** Umfang, Frequenz, Aufbewahrung, Speicherort, Schutz, Verschlüsselung und Zugriff definieren.
3. **Einrichten:** Jobs, Monitoring, Fehlerhandling und Dokumentation umsetzen.
4. **Überwachen:** Jobstatus, Kapazität, Manipulationsschutz und Zugriff regelmäßig prüfen.
5. **Restore testen:** Datei-, Datenbank-, Applikations- oder Service-Restore mit realistischem Ziel durchführen.
6. **Nachweis ablegen:** Ergebnis, Dauer, Abweichungen, offene Maßnahmen und Entscheidung dokumentieren.
7. **Eskalieren:** Backupfehler, nicht erreichbare RTO/RPO, ungeschützte Sicherungen oder Ressourcenlücken ins Management geben.
8. **Verbessern:** Findings aus Tests, Incidents und Übungen in Backupdesign, BCM und Architektur zurückspielen.

## Entscheidungen

- Welche Systeme und Daten sind kritisch genug für definierte Recovery-Ziele?
- Wie viel Datenverlust und Ausfallzeit ist fachlich tragbar?
- Welche Backups brauchen getrennte Administration, Immutable-/Offline-Schutz oder besondere Verschlüsselung?
- Welche SaaS- und Cloud-Daten werden durch Anbieterfunktionen ausreichend abgedeckt und wo braucht es eigene Sicherung?
- Wie oft werden Restore-Tests durchgeführt und wie realistisch müssen sie sein?
- Wer akzeptiert Abweichungen von RTO/RPO oder nicht gesicherte Systeme?

## Evidenz

### Starke Evidenz

- Backupscope mit Service Ownern und Kritikalität,
- dokumentierte RTO/RPO-Entscheidungen,
- Backupjob-Historie mit Fehlerbehandlung,
- Restore-Testprotokolle inklusive Ergebnis und Dauer,
- Nachweise zu Zugriffsschutz, Verschlüsselung oder Immutable-/Offline-Schutz,
- Maßnahmen aus fehlgeschlagenen Tests,
- BCM-/Managemententscheidung bei Recovery-Lücken.

### Schwache Evidenz

- Screenshot „Backup erfolgreich“ ohne Scope,
- Backupkonzept ohne Restore-Test,
- Jobliste ohne Owner oder Kritikalität,
- Restore-Test nur für eine unkritische Datei,
- Anbieterstatement ohne Prüfung eigener SaaS-Daten,
- unklare Aufbewahrungsdauer ohne Legal-/Datenschutz-Handoff.

### Evidenzlücken

- kritische Systeme ohne Backupstatus,
- keine getestete Wiederherstellung,
- Backupadministration mit normalen Produktivkonten,
- keine Sicherung von Konfigurationen, Schlüsseln oder Identitätsdiensten,
- Backupfehler ohne Ticket oder Eskalation,
- RTO/RPO nicht mit Fachbereichen abgestimmt.

## Wirksamkeitsprüfung

Prüffragen:

- Sind kritische Systeme und Datenbestände im Backupscope vollständig sichtbar?
- Wurden Wiederanlaufzeit und Datenverlusttoleranz mit den Ownern abgestimmt?
- Werden Backupfehler erkannt, bearbeitet und eskaliert?
- Sind Backups gegen Manipulation, Ransomware und unbefugten Zugriff geschützt?
- Wurden Restore-Tests durchgeführt und führten sie zu belastbaren Ergebnissen?
- Stimmen Backupfähigkeit, BCM-Annahmen und Managemententscheidungen überein?

Mögliche Kennzahlen:

- Backupabdeckung kritischer Systeme,
- fehlgeschlagene oder überfällige Backupjobs,
- Anteil getesteter kritischer Restores,
- tatsächliche Restore-Dauer gegenüber RTO,
- erreichter Datenstand gegenüber RPO,
- offene Recovery-Lücken und akzeptierte Ausnahmen.

## BSIG-/NIS2-Anschluss

Datensicherung ist anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Business Continuity, Incident Handling, Krisenfähigkeit, Cyberhygiene und Aufrechterhaltung kritischer Dienste. Der konkrete Bezug sollte im Anforderungsregister, BCM-Kontext und Management Review organisationsspezifisch geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Prüfung von Aufbewahrung, Datenschutz, Meldepflichten oder branchenspezifischen Anforderungen.

## Grenzen

- Ein Backup ist kein Nachweis für Wiederherstellbarkeit, solange Restore nicht getestet wurde.
- Dieses Artefakt ist kein vollständiges Disaster-Recovery-Design.
- Es ersetzt keine Datenschutzprüfung zu Aufbewahrung, Speicherort oder Löschung.
- Es garantiert keine Verfügbarkeit und keine Zertifizierungsfähigkeit.
- Es enthält keine ISO-27002-Texte und keine vertraulichen Architekturdetails.

## Handoffs

- **BCM-Handoff:** RTO/RPO, Wiederanlaufreihenfolge, Notbetrieb, Übungen und Krisenentscheidungen.
- **Incident-Handoff:** Ransomware, Datenverlust, Manipulation, Restore im laufenden Vorfall.
- **IT-/Plattform-Handoff:** Backupdesign, Monitoring, Restore, Zugriffsschutz, Schlüssel und Speicherorte.
- **Datenschutz-/Legal-Handoff:** personenbezogene Daten, Aufbewahrung, Löschung, externe Speicherung, Verschlüsselung.
- **Lieferanten-Handoff:** SaaS-/Cloud-Backupfähigkeit, Restore-SLAs, Provider-Nachweise.
- **Management-Handoff:** nicht erfüllte Recovery-Ziele, Kosten, technische Grenzen, akzeptierte Ausnahmen.
- **Audit-/Evidence-Handoff:** fehlende Restore-Nachweise oder unklare Backupabdeckung.

## Typische Fehler

- Backups werden mit Wiederherstellbarkeit verwechselt.
- Restore-Tests werden nur theoretisch oder nur für unkritische Dateien durchgeführt.
- SaaS-Daten werden als „vom Anbieter gesichert“ angenommen, ohne eigene Recovery-Anforderung zu prüfen.
- Backupkonten und Produktivadminrechte sind nicht getrennt.
- Konfigurationen, Secrets, Schlüssel oder Identitätsdienste fehlen im Recovery-Plan.
- Backupfehler werden im Monitoring gesehen, aber nicht nachverfolgt.
- RTO/RPO werden technisch geschätzt, ohne Fachbereich und BCM einzubeziehen.

## Fiktives Mini-Beispiel

Ein fiktiver Onlinehändler bewertet sein Shopsystem als kritisch. Der Service Owner legt mit BCM fest, dass Bestellungen nur mit begrenztem Datenverlust wiederherstellbar sein müssen. IT sichert Datenbank, Konfiguration und relevante Schlüssel getrennt und testet quartalsweise einen Restore in einer isolierten Umgebung. Beim ersten Test fehlt eine Konfigurationsdatei; das Finding wird behoben und im Management Review wird Budget für immutable Backup-Speicher freigegeben.

Evidenz:

- Service-/Backupmatrix mit RTO/RPO,
- Backupjob-Historie,
- Restore-Testprotokoll mit fehlender Konfiguration,
- Korrekturticket,
- Managemententscheidung zum Backupschutz,
- aktualisierte Wiederherstellungsanleitung.
