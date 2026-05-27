
# A.8.17 — Zeitsynchronisation

## Zweck

Zeitsynchronisation sorgt dafür, dass Systeme, Anwendungen, Logquellen und Sicherheitswerkzeuge Ereignisse mit verlässlichem Zeitbezug erzeugen. Der praktische Nutzen liegt in nachvollziehbarer Incident-Analyse, korrekter Korrelation von Logs, stabilen Authentifizierungsverfahren und belastbarer Fehlerdiagnose.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der relevante Systeme eine definierte, vertrauenswürdige Zeitquelle nutzen, Abweichungen erkannt und behoben werden und der Zeitbezug für Protokollierung, Monitoring, Zugriffsschutz, Zertifikate, Backup und Incident Response nachvollziehbar bleibt.

## Typische Risiken

- Wenn Systeme unterschiedliche Zeiten verwenden, lassen sich Logereignisse nicht zuverlässig korrelieren.
- Wenn Zeitquellen ungeklärt oder manipuliert sind, können Untersuchungen, Zugriffsnachweise oder technische Prüfungen fehlerhaft werden.
- Wenn Authentifizierung, Zertifikate oder Token auf falsche Zeit angewiesen sind, entstehen Ausfälle oder Sicherheitslücken.
- Wenn Cloud-, SaaS- und lokale Systeme keine abgestimmte Zeitbasis haben, entstehen Lücken in Monitoring und Incident Response.
- Wenn Zeitabweichungen nicht erkannt werden, bleiben Fehler lange unbemerkt und erschweren Ursachenanalyse.
- Wenn kritische Sonderumgebungen isoliert sind, werden sie oft vom Standard ausgeschlossen, ohne Risikoentscheidung.

## Trigger

- neues System, neuer Server, neue Cloud-Umgebung, neues Netzwerksegment oder neue OT-/Sonderumgebung.
- Änderung an Domänencontrollern, Identitätsdiensten, NTP-/Zeitservern, Firewalls oder Routing.
- Incident, Forensikbedarf oder Logkorrelationsproblem.
- Zertifikats-, Token-, Backup-, Replikations- oder Authentifizierungsfehler mit möglichem Zeitbezug.
- Monitoring-Treffer zu Zeitabweichung oder nicht erreichbarer Zeitquelle.
- Lieferanten- oder SaaS-Änderung, die Zeitstempel, Logs oder Reports betrifft.
- regulärer Review kritischer Infrastruktur- und Logquellen.

## Rollen und Verantwortung

- **IT-/Plattform Owner:** definiert und betreibt Zeitquellen, Client-Konfigurationen, Monitoring und Störungsbehebung.
- **Netzwerk-/Infrastrukturteam:** stellt Erreichbarkeit, Segmentübergänge und technische Einschränkungen bereit.
- **Service Owner / Application Owner:** bewertet Auswirkungen auf Anwendung, Logs, Authentifizierung, Jobs und Schnittstellen.
- **Security-Rolle / ISMS-Owner:** verknüpft Zeitsynchronisation mit Logging, Monitoring, Incident Response und Evidenzanforderungen.
- **Incident-Response-Rolle:** nutzt Zeitbezug für Triage und Untersuchung und meldet Lücken zurück.
- **Lieferantenmanagement:** klärt Zeitstempelqualität und Zeitquellen bei externen Diensten oder Managed Services.
- **Management:** entscheidet bei strukturellen Lücken, Legacy-Systemen oder Investitionsbedarf.

## Implementierung

### Minimalstart

Ziel: Kritische Systeme nutzen eine definierte Zeitquelle und Zeitabweichungen sind sichtbar.

1. Kritische Systeme und Logquellen benennen: Identität, Server, Firewalls, Cloud-Plattform, SIEM/Logging, Backup, zentrale Anwendungen.
2. Pro Systemklasse festlegen, welche Zeitquelle genutzt wird und wer sie betreibt.
3. Eine einfache Prüfung durchführen: aktuelle Zeitquelle, Synchronisationsstatus und erkennbare Abweichung.
4. Abweichungen in einem Maßnahmenlog erfassen und priorisieren.
5. Für isolierte oder nicht synchronisierbare Systeme eine Ausnahme mit Risiko- und Reviewdatum dokumentieren.
6. Incident- und Logging-Routinen darauf hinweisen, welche Zeitbasis verwendet wird.

### Solide Praxis

Ziel: Zeitsynchronisation wird als Infrastrukturstandard betrieben und regelmäßig geprüft.

1. Standardkonfigurationen für Server, Clients, Netzwerkgeräte, Cloud-Ressourcen und virtuelle Plattformen sind dokumentiert.
2. Zeitquellen sind redundant oder ausfallsicher genug für die Kritikalität der Umgebung.
3. Monitoring erkennt relevante Zeitabweichungen und nicht erreichbare Zeitquellen.
4. Neue Systeme erhalten Zeitsynchronisation über Build-, Deployment- oder Konfigurationsmanagement.
5. Logging- und Monitoring-Reviews prüfen, ob Zeitstempel zwischen Quellen korrelierbar sind.
6. Sonderfälle wie isolierte Netze, Appliances, OT, Laborumgebungen oder SaaS-Berichte werden explizit entschieden.
7. Änderungen an Zeitquellen laufen über Change- und Kommunikationswege.

### Fortgeschritten

Ziel: Der Zeitbezug ist organisationsweit belastbar, automatisiert überprüft und in Sicherheitsprozesse integriert.

1. Zeitkonfigurationen werden als Baseline in Endpoint-, Server-, Cloud- und Netzwerkmanagement geführt.
2. Abweichungen erzeugen Tickets oder Alarme mit Kritikalität nach Systemklasse.
3. Zeitquellen, Stratum-/Hierarchie, Redundanz und Abhängigkeiten sind in Architektur- und Betriebsdokumentation sichtbar.
4. Incident- und Forensik-Playbooks enthalten Annahmen und Prüfungen zur Zeitbasis.
5. Korrelation zwischen lokalen, Cloud- und SaaS-Logs wird regelmäßig getestet.
6. Kritische Zeitinfrastruktur wird in Verfügbarkeits-, Backup- und Wiederanlaufüberlegungen einbezogen.
7. Management sieht offene Lücken, Legacy-Ausnahmen und Auswirkungen auf Nachvollziehbarkeit.

## Ablauf als Routine

1. **System in Scope nehmen:** neue oder kritische Systeme in die Zeitkonfigurationslogik aufnehmen.
2. **Zeitquelle zuweisen:** Standardquelle oder begründete Ausnahme festlegen.
3. **Konfiguration prüfen:** Synchronisationsstatus und Abweichung kontrollieren.
4. **Monitoring aktivieren:** relevante Abweichungen, Ausfälle oder nicht erreichbare Quellen erfassen.
5. **Abweichung behandeln:** Owner, Ursache, Maßnahme und Frist dokumentieren.
6. **Logkorrelation prüfen:** bei Reviews oder Incidents testen, ob Zeitstempel zusammenpassen.
7. **Ausnahmen reviewen:** isolierte, alte oder externe Systeme regelmäßig neu bewerten.
8. **Lessons Learned einbauen:** Untersuchungen mit Zeitproblemen führen zu Standard- oder Toolanpassungen.

## Entscheidungen

- Welche Zeitquellen gelten für welche Systemklassen und Umgebungen?
- Welche maximale Zeitabweichung ist für Logging, Authentifizierung und Betrieb tolerierbar?
- Wer betreibt zentrale Zeitquellen und wer darf sie ändern?
- Wie werden isolierte Systeme, Appliances, OT oder Laborumgebungen behandelt?
- Welche Zeitabweichungen lösen Alarm, Ticket oder Incident-Triage aus?
- Wie wird Zeitstempelqualität bei SaaS, Lieferantenreports und Managed Services bewertet?
- Wann braucht eine technische Lücke eine Managemententscheidung?

## Evidenz

### Starke Evidenz

- dokumentierte Zeitquellen und Zuständigkeiten je Systemklasse,
- Konfigurationsnachweise für kritische Systeme,
- Monitoring- oder Prüfberichte zu Zeitabweichungen,
- Tickets zur Behebung von Synchronisationsproblemen,
- Nachweis, dass neue Systeme Standardkonfigurationen erhalten,
- Incident- oder Übungsnachweis, der korrelierbare Zeitstempel nutzt,
- Ausnahmeentscheidungen für Sonderumgebungen mit Reviewdatum.

### Schwache Evidenz

- allgemeine Aussage „NTP ist aktiviert“ ohne Scope und Prüfung,
- Screenshot eines einzelnen Servers ohne Abdeckung,
- Standardimage-Dokument ohne Nachweis produktiver Umsetzung,
- Logkorrelation wird angenommen, aber nie getestet,
- Dienstleisterreport mit Zeitstempeln ohne Klärung der Zeitbasis,
- Ausnahmen für isolierte Systeme ohne Risikoentscheidung.

### Evidenzlücken

- keine bekannten Zeitquellen oder Owner,
- unbekannte Abweichungen auf kritischen Systemen,
- zentrale Logquellen nutzen unterschiedliche Zeitbasis,
- keine Behandlung von Zeitserver-Ausfällen,
- neue Systeme werden manuell und uneinheitlich konfiguriert,
- externe Dienste liefern nicht nachvollziehbare Zeitstempel,
- Incident-Analyse scheitert an unklarer Reihenfolge von Ereignissen.

## Wirksamkeitsprüfung

Prüffragen:

- Nutzen kritische Systeme definierte und erreichbare Zeitquellen?
- Werden relevante Zeitabweichungen erkannt und behoben?
- Sind Zeitstempel aus Identität, Netzwerk, Cloud, Servern und Anwendungen korrelierbar?
- Sind neue Systeme automatisch oder verbindlich in die Zeitroutine eingebunden?
- Gibt es dokumentierte Entscheidungen für isolierte oder nicht standardfähige Systeme?
- Wurde die Zeitbasis in Incident-Übungen oder Logreviews geprüft?
- Sind Änderungen an Zeitquellen nachvollziehbar und kontrolliert?

Mögliche Kennzahlen:

- Abdeckung kritischer Systeme mit definierter Zeitquelle,
- offene Zeitabweichungen nach Kritikalität,
- Anzahl nicht erreichbarer Zeitquellen,
- Zeit bis Behebung relevanter Abweichungen,
- Anteil neuer Systeme mit Standardkonfiguration,
- Anzahl ungeprüfter Sonderausnahmen.

## BSIG-/NIS2-Anschluss

Zeitsynchronisation ist anschlussfähig an NIS2-orientierte Themen wie Protokollierung, Monitoring, Incident Handling, Zugriffsschutz, Betriebsstabilität und Nachvollziehbarkeit technischer Ereignisse. Der konkrete Bezug sollte im Anforderungsregister, in Betriebsstandards und in Incident-Response-Reviews organisationsspezifisch geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung von Nachweispflichten, Meldepflichten oder technischen Beweisfragen.

## Grenzen

- Dieses Artefakt ist keine detaillierte NTP-/PTP-Architektur und keine Produktkonfiguration.
- Es ersetzt keine Forensikbewertung, wenn Zeitstempel bereits manipuliert oder inkonsistent sind.
- Hochpräzise Spezialumgebungen benötigen eigene technische Bewertung.
- Keine Zertifizierungs-, Konformitäts- oder Sicherheitsgarantie.
- Keine Übernahme lizenzpflichtiger Normtexte.

## Handoffs

- **Logging-/Monitoring-Handoff:** inkonsistente Zeitstempel verhindern Korrelation oder Alarmierung.
- **Incident-Handoff:** Zeitabweichung beeinflusst Untersuchung, Ereignisreihenfolge oder Verdacht auf Manipulation.
- **Plattform-/Netzwerk-Handoff:** Zeitquelle, Firewall-Regel, Segmentierung oder Client-Konfiguration ist fehlerhaft.
- **Lieferanten-Handoff:** SaaS-, Appliance- oder Managed-Service-Zeitstempel sind unklar oder nicht korrelierbar.
- **BCM-/Betriebs-Handoff:** Ausfall zentraler Zeitquellen gefährdet kritische Dienste.
- **Management-Handoff:** Legacy- oder Sonderumgebungen bleiben dauerhaft außerhalb des Standards.
- **Audit-/Evidence-Handoff:** Nachweise zur Zeitbasis fehlen oder sind nicht prüfbar.

## Typische Fehler

- Zeitsynchronisation wird als einmalige Systemeinstellung behandelt.
- Kritische Netzwerkgeräte, Appliances oder Cloud-Ressourcen werden vergessen.
- Monitoring prüft Verfügbarkeit, aber nicht relevante Zeitabweichung.
- Isolierte Systeme werden ausgenommen, ohne Risikoentscheidung.
- Zeitserver werden geändert, ohne Auswirkungen auf Logging und Authentifizierung zu prüfen.
- Incident-Teams entdecken Zeitprobleme erst während der Untersuchung.
- Lieferantenberichte werden mit lokalen Logs verglichen, obwohl die Zeitbasis ungeklärt ist.

## Fiktives Mini-Beispiel

Ein fiktives Unternehmen untersucht mehrere fehlgeschlagene VPN-Anmeldungen. Die Firewall-Logs und Identitätslogs passen zeitlich nicht zusammen. Der Plattform Owner prüft die Zeitquelle und findet eine veraltete Konfiguration auf zwei Netzwerkgeräten. Die Geräte werden auf die definierte interne Zeitquelle umgestellt, Monitoring für Zeitabweichungen wird aktiviert und eine Stichprobe bestätigt korrelierbare Ereignisse. Eine isolierte Laborumgebung bleibt vorerst ausgenommen; der Service Owner dokumentiert die Ausnahme mit Reviewdatum.
