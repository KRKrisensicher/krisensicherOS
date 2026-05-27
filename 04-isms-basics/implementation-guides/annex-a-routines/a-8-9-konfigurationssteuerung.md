
# A.8.9 — Konfigurationssteuerung

## Zweck

Konfigurationssteuerung sorgt dafür, dass sicherheitsrelevante Einstellungen von Systemen, Anwendungen, Cloud-Diensten, Netzkomponenten, Endgeräten und Plattformen bewusst festgelegt, geändert, geprüft und korrigiert werden. Der Kern ist nicht eine einmalige Baseline, sondern eine Routine gegen Konfigurationsdrift, Schattenänderungen und unsichere Defaults.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Routine für sichere und betrieblich tragfähige Konfigurationen. Baselines, Verantwortlichkeiten, Changes, Ausnahmen, Prüfungen, Drift-Behandlung und Managemententscheidungen sind so verbunden, dass Konfigurationen nicht zufällig, sondern gesteuert entstehen und erhalten bleiben.

## Typische Risiken

- Wenn Systeme mit unsicheren Standardkonfigurationen betrieben werden, entstehen vermeidbare Angriffsflächen.
- Wenn Änderungen ohne Review erfolgen, können Sicherheitsfunktionen deaktiviert, Ports geöffnet oder Daten ungeschützt bereitgestellt werden.
- Wenn Cloud-, SaaS- oder Netzwerk-Konfigurationen nicht überwacht werden, bleiben Fehlfreigaben und Exposition unbemerkt.
- Wenn Baselines nicht versioniert sind, ist unklar, welcher Zustand gewollt war.
- Wenn Ausnahmen nicht dokumentiert werden, wird Abweichung zur Normalität.
- Wenn Konfigurationen nicht mit Schwachstellen-, Change- und Incident-Prozessen verbunden sind, werden Ursachen wiederholt übersehen.

## Trigger

- neues System, neue Anwendung, neue Cloud-Ressource, neue Netzwerkkomponente oder neues SaaS-Feature.
- Änderung an Firewall, Identität, Logging, Verschlüsselung, Backup, Adminrechten oder Exposition.
- Schwachstellenfund, Fehlkonfiguration, Auditfinding, Incident oder Monitoring-Treffer.
- Hersteller- oder Plattformänderung, neues Default-Verhalten oder abgekündigte Funktion.
- Architektur-, Release-, Change- oder Migrationsentscheidung.
- Wiederherstellung, Neuinstallation oder Infrastruktur-als-Code-Änderung.
- turnusmäßiger Review von Baselines, Drift, Ausnahmen und kritischen Konfigurationen.

## Rollen und Verantwortung

- **System-/Platform Owner:** verantwortet technische Konfiguration, Baseline-Umsetzung und Korrekturen.
- **Service Owner / Application Owner:** bewertet fachliche Auswirkungen, Verfügbarkeit und Schutzbedarf.
- **Security-Rolle / ISMS-Owner:** definiert Mindestlogik, Prüfschwerpunkte, Ausnahmebehandlung und Reporting.
- **Change Owner:** stellt Review, Freigabe, Test und Rollback für relevante Änderungen sicher.
- **Cloud-/Network Owner:** steuert Cloud-, Netzwerk-, Firewall-, DNS- und Expositionskonfigurationen.
- **Entwicklung / DevOps:** pflegt Konfigurationen in Code, Deployments, Pipelines und Umgebungsvariablen.
- **Management:** entscheidet bei Zielkonflikten, dauerhaftem Abweichen, Ressourcenbedarf oder akzeptiertem Restrisiko.

## Implementierung

### Minimalstart

Ziel: kritische Konfigurationen sichtbar, verantwortlich und prüfbar machen.

1. Kritische Systeme, Cloud-Ressourcen, Netzwerkkomponenten, Endpunkte, Anwendungen und Sicherheitsfunktionen werden im Scope benannt.
2. Für jedes kritische Ziel wird ein Owner festgelegt.
3. Für die wichtigsten Konfigurationsbereiche wird ein gewünschter Mindestzustand beschrieben: Zugriff, Logging, Updates, Verschlüsselung, Exposition, Backup, Adminrechte.
4. Änderungen an kritischen Konfigurationen laufen über Ticket, Change oder nachvollziehbare Freigabe.
5. Abweichungen und Ausnahmen werden mit Begründung, Risiko, Kompensation und Ablaufdatum dokumentiert.
6. Mindestens stichprobenartig wird geprüft, ob Ist-Zustand und gewünschter Zustand zusammenpassen.

Minimaler Nachweis:

- Scope kritischer Konfigurationsobjekte mit Owner,
- einfache Baseline oder Mindestkonfiguration,
- Change-/Ticketnachweis,
- Konfigurationsauszug oder Prüfprotokoll,
- Ausnahmeentscheidung mit Wiedervorlage.

### Solide Praxis

Ziel: Konfigurationen werden versioniert, regelmäßig geprüft und mit Change Management verbunden.

1. Baselines werden nach Assettyp oder Plattformklasse definiert: Server, Endpunkte, Netzwerk, Cloud, Datenbank, SaaS, Container, CI/CD.
2. Konfigurationen werden versioniert oder in nachvollziehbaren Templates geführt.
3. Kritische Änderungen werden vor Umsetzung auf Sicherheitswirkung, Betriebswirkung und Rollback geprüft.
4. Drift- oder Compliance-Prüfungen vergleichen Ist-Zustand und gewünschten Zustand.
5. Wiederkehrende Abweichungen führen zu Ursachenanalyse: fehlende Automatisierung, unklare Owner, Toolgrenzen, Legacy-Systeme.
6. Ausnahmen werden im Risiko- oder Maßnahmenlog geführt und regelmäßig reviewed.
7. Reviewresultate fließen in Schwachstellenmanagement, Incident Lessons Learned und Management Review.

### Fortgeschritten

Ziel: Konfigurationssteuerung wird automatisiert, risikobasiert und auditierbar betrieben.

1. Infrastructure as Code, Policy as Code oder zentrale Managementsysteme definieren und verteilen gewünschte Zustände.
2. Automatisierte Drift-Erkennung, Cloud-Security-Checks oder Baseline-Scans erzeugen Tickets mit Owner, Risiko und Frist.
3. Kritische Konfigurationen werden vor Deployment in CI/CD oder Change Gates geprüft.
4. Notfalländerungen werden zeitnah nachreviewed und in den Zielzustand zurückgeführt.
5. Konfigurationsdaten unterstützen Incident Response, Forensik, Schwachstellenbewertung und BCM.
6. Management sieht Risikoentwicklung, Ausnahmequote, überfällige Drift-Korrekturen und technische Schulden.

## Ablauf als Routine

1. **Konfigurationsobjekt bestimmen:** System, Plattform, Cloud-Ressource, Anwendung, Netzwerkkomponente oder Sicherheitsfunktion.
2. **Zielzustand festlegen:** Mindestkonfiguration, Owner, Schutzbedarf, Betriebsanforderungen und Abweichungstoleranz beschreiben.
3. **Änderung steuern:** Antrag, Review, Test, Freigabe, Umsetzung und Rollbackbedarf dokumentieren.
4. **Ist-Zustand prüfen:** Export, Scan, IaC-Review, Konsolenprüfung oder Stichprobe nutzen.
5. **Abweichung bewerten:** Sicherheitswirkung, Exposition, Datenbezug, Betriebsrisiko und Kompensation einschätzen.
6. **Behandeln:** korrigieren, Ausnahme befristen, Architektur ändern oder Risikoentscheidung einholen.
7. **Nachweisen:** Baseline, Change, Prüfung, Entscheidung und Korrektur ablegen.
8. **Reviewen:** Drift-Muster, Ausnahmen, Toolabdeckung und wiederkehrende Ursachen bewerten.
9. **Eskalieren:** nicht korrigierbare oder risikoreiche Abweichungen ins Management Review geben.

## Entscheidungen

- Welche Plattformen und Konfigurationsbereiche sind für den Start kritisch genug?
- Wer darf sicherheitsrelevante Konfigurationen ändern?
- Welche Änderungen brauchen Security-, Change- oder Management-Freigabe?
- Welche Abweichungen sind temporär akzeptabel und welche nicht?
- Wie werden Notfalländerungen nachträglich geprüft?
- Welche Konfigurationen gehören in Code, Templates oder zentrale Managementsysteme?

## Evidenz

### Starke Evidenz

- aktueller Scope kritischer Konfigurationsobjekte mit Ownern,
- versionierte Baselines, Templates oder IaC-Definitionen,
- Change-Tickets mit Review, Test und Freigabe,
- Konfigurationsscans, Exporte oder Drift-Reports,
- Korrekturtickets mit Nachweis der Umsetzung,
- Ausnahmeentscheidungen mit Risiko, Kompensation und Ablaufdatum,
- Managemententscheidung bei dauerhaftem Abweichen oder Ressourcenbedarf.

### Schwache Evidenz

- allgemeine Hardening-Policy ohne Systembezug,
- Screenshot einer Einstellung ohne Datum, Scope oder Owner,
- Toolreport ohne Triage,
- nicht versionierte Checkliste,
- Change-Freigabe ohne Sicherheitsbewertung,
- Aussage „Standardkonfiguration des Herstellers“ ohne Prüfung.

### Evidenzlücken

- unbekannte oder nicht verantwortete Konfigurationsobjekte,
- keine Baseline für kritische Plattformen,
- Änderungen außerhalb des Change-Prozesses,
- Drift ohne Ticket oder Entscheidung,
- Ausnahmen ohne Ablaufdatum,
- keine Verbindung zu Incident-, Schwachstellen- oder Risikoarbeit.

## Wirksamkeitsprüfung

Prüffragen:

- Gibt es für kritische Plattformen einen definierten und bekannten Zielzustand?
- Sind sicherheitsrelevante Konfigurationsänderungen nachvollziehbar freigegeben?
- Werden Ist-Zustand und Zielzustand regelmäßig verglichen?
- Führen Drift-Funde zu Korrektur, Ausnahme oder Managemententscheidung?
- Sind Notfalländerungen nachreviewed?
- Werden wiederkehrende Fehlkonfigurationen strukturell behandelt?

Mögliche Kennzahlen:

- Anteil kritischer Plattformen mit Baseline,
- Anzahl offener Drift-Funde nach Kritikalität,
- überfällige Konfigurationskorrekturen,
- Ausnahmequote und überfällige Ausnahmen,
- ungeplante oder Notfalländerungen mit Nachreview,
- wiederkehrende Fehlkonfigurationen pro Plattform,
- Zeit bis Korrektur kritischer Abweichungen.

## BSIG-/NIS2-Anschluss

Konfigurationssteuerung ist anschlussfähig an NIS2-orientierte Themen wie Cyberhygiene, sichere Betriebsprozesse, Schwachstellenmanagement, Incident-Prävention, Zugriffsschutz, Monitoring und Business Continuity. Der konkrete Bezug sollte organisationsspezifisch im Anforderungsregister, in Risikoanalysen und im Change-/Architekturprozess geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung, Datenschutzprüfung oder Zertifizierungszusage.

## Grenzen

- Dieses Artefakt ist keine technische Hardening-Baseline und kein Herstellerleitfaden.
- Es ersetzt keine Architekturprüfung, Penetrationstests oder Schwachstellenscans.
- Es garantiert keine sichere Konfiguration ohne tatsächliche Umsetzung und Review.
- Keine verbindliche Aussage zu gesetzlichen Pflichten oder Konformität.
- Keine vertraulichen Systemdetails, Secrets oder Kundendaten in öffentlichen Beispielen.

## Handoffs

- **Change-Handoff:** sicherheitsrelevante Änderung, Testbedarf, Rollback, Notfalländerung oder Release.
- **Schwachstellen-Handoff:** Fehlkonfiguration erhöht Ausnutzbarkeit oder wird als Finding gemeldet.
- **Incident-Handoff:** Konfigurationsänderung verursacht oder begünstigt Sicherheitsereignis.
- **Cloud-/Netzwerk-Handoff:** Exposition, Firewall, IAM, Speicherfreigaben, DNS oder Plattformpolicy betroffen.
- **Entwicklungs-/DevOps-Handoff:** IaC, CI/CD, Umgebungsvariablen, Container- und Deployment-Konfiguration.
- **BCM-Handoff:** Korrektur gefährdet Verfügbarkeit kritischer Dienste oder Wiederanlaufziele.
- **Management-Handoff:** dauerhafte Abweichung, Ressourcenbedarf, Legacy-Konflikt oder akzeptiertes Restrisiko.
- **Audit-/Evidence-Handoff:** fehlende Baselines, unvollständige Drift-Nachweise oder unklare Ausnahmebehandlung.

## Typische Fehler

- Eine Baseline wird erstellt, aber nie gegen echte Systeme geprüft.
- Änderungen werden technisch umgesetzt, ohne Sicherheitswirkung zu bewerten.
- Cloud- und SaaS-Konfigurationen fehlen im Scope.
- Notfalländerungen bleiben dauerhaft.
- Drift-Reports werden erzeugt, aber nicht priorisiert.
- Ausnahmen haben kein Ablaufdatum und keine Kompensation.
- Management bekommt technische Abweichungslisten ohne Entscheidungsvorlage.

## Fiktives Mini-Beispiel

Ein fiktiver Plattformbetreiber prüft monatlich die Konfiguration seiner Cloud-Speicher. Ein Drift-Report zeigt, dass ein Test-Bucket öffentlich lesbar ist. Der Cloud Owner sperrt den Zugriff, erstellt ein Ticket und prüft den Change-Verlauf. Ursache war eine Notfalländerung ohne Nachreview. Das Team ergänzt ein CI/CD-Gate für öffentliche Speicherfreigaben und dokumentiert eine Managemententscheidung, dass produktionsnahe Testdaten künftig nicht ohne Schutzklassifizierung genutzt werden.

Evidenz:

- Cloud-Konfigurationsbaseline,
- Drift-Report,
- Korrekturticket,
- Ursachenanalyse zur Notfalländerung,
- ergänztes CI/CD-Gate,
- Managemententscheidung zur Testdatennutzung.
