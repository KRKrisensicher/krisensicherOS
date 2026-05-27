
# A.8.20 — Netzwerksicherheit

## Zweck

Netzwerksicherheit sorgt dafür, dass Netzwerkverbindungen, Übergänge, Komponenten und Betriebswege geplant, geschützt, überwacht und nachvollziehbar geändert werden. Der Kern ist nicht „Firewall vorhanden“, sondern eine betriebene Routine: Welche Netzbereiche gibt es, welche Verbindungen sind erlaubt, wer verantwortet Änderungen und wie werden Abweichungen erkannt?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt Netzwerke als kontrollierte Betriebsumgebung. Netzwerkarchitektur, Zugänge, Firewall-/Routing-Regeln, Remote-Zugriffe, Cloud-Netzwerke und kritische Netzwerkkomponenten werden mit Ownern, Änderungsprozess, Monitoring, Review und Ausnahmebehandlung gesteuert.

## Typische Risiken

- Wenn Netzwerkübergänge ohne Review wachsen, können Systeme erreichbar werden, die nie exponiert sein sollten.
- Wenn Firewall- oder Routing-Regeln keinen Owner haben, bleiben Altfreigaben nach Projektende bestehen.
- Wenn Netzwerkkomponenten unsicher konfiguriert oder ungepatcht bleiben, können Angreifer zentrale Kommunikationswege manipulieren.
- Wenn Remote- oder Administrationszugänge nicht gesondert gesteuert werden, kann ein kompromittiertes Konto weitreichende Wirkung entfalten.
- Wenn Cloud-, Standort- und Dienstleisternetze nicht gemeinsam betrachtet werden, entstehen blinde Flecken in Erreichbarkeit, Logging und Verantwortung.

## Trigger

- neues Netzwerk, neuer Standort, neue Cloud-Umgebung, neuer Dienstleisterzugang oder neue Schnittstelle.
- Änderung von Firewall-Regeln, Routing, VPN, DNS, Proxy, WLAN oder Managementzugängen.
- Schwachstelle, Incident, ungewöhnlicher Netzwerkverkehr oder Monitoring-Alarm.
- Einführung oder Änderung kritischer Systeme und Netzwerkkomponenten.
- Auditfinding, Architekturreview oder Risikoentscheidung.
- turnusmäßiger Review von Netzwerkregeln, Netzwerkplänen und Adminzugängen.

## Rollen und Verantwortung

- **Netzwerk Owner / Plattform Owner:** verantwortet Architektur, Betrieb, Änderungen und technische Nachweise.
- **Service Owner / Asset Owner:** beschreibt Geschäftsbedarf, Schutzbedarf und benötigte Verbindungen.
- **Security-Rolle / ISMS-Owner:** definiert Mindestlogik für Freigaben, Reviews, Ausnahmen und Risikohandling.
- **Change Owner:** koordiniert Tests, Rollback, Wartungsfenster und Dokumentation.
- **Incident Response:** übernimmt bei Verdacht auf Missbrauch, laterale Bewegung oder Netzwerkkompromittierung.
- **Lieferantenmanagement:** steuert externe Netzwerkdienste, Managed Services und Dienstleisterzugänge.
- **Management:** entscheidet bei Restrisiken, Ressourcenmangel, Architekturzielkonflikten oder dauerhaft notwendigen Ausnahmen.

## Implementierung

### Minimalstart

Ziel: kritische Netzbereiche und Netzwerkänderungen sichtbar und reviewfähig machen.

1. Die wichtigsten Netzbereiche, Internetübergänge, Remote-Zugänge, Cloud-Netze und kritischen Komponenten werden mit Owner erfasst.
2. Neue oder geänderte Netzwerkfreigaben laufen über Ticket oder Change mit Zweck, Quelle, Ziel, Port/Protokoll, Laufzeit und fachlichem Owner.
3. Internet-exponierte und administrative Zugänge werden gesondert geprüft.
4. Offene oder pauschale Regeln erhalten Begründung, Kompensationsmaßnahme oder Rückbauplan.
5. Mindestens kritische Regeln und Komponenten werden regelmäßig reviewed.

Minimaler Nachweis:

- Netzwerkübersicht mit kritischen Übergängen und Ownern,
- Change-/Ticketnachweise für Regeländerungen,
- Reviewprotokoll kritischer Firewall- oder Routing-Regeln,
- Liste administrativer und externer Netzwerkzugänge,
- Ausnahmeentscheidungen mit Ablaufdatum.

### Solide Praxis

Ziel: Netzwerksicherheit wird als wiederholbare Architektur- und Betriebsroutine geführt.

1. Netzbereiche werden nach Schutzbedarf, Funktion, Exposition und Betriebsverantwortung geordnet.
2. Regeländerungen folgen einem Freigabeprozess mit fachlicher Begründung, Sicherheitsprüfung und technischer Validierung.
3. Netzwerkkomponenten haben Basiskonfiguration, Patch-/Firmware-Routine, Backup der Konfiguration und Zugriffsschutz.
4. Logging und Monitoring erfassen relevante Übergänge, verweigerte Verbindungen, Adminzugriffe und Konfigurationsänderungen.
5. Alte Regeln, temporäre Freigaben und Projektzugänge werden aktiv zurückgebaut.
6. Netzwerkfindings fließen in Schwachstellenmanagement, Architekturreview und Management Review.

Starke Evidenz:

- aktuelle Netzwerk- und Datenflussübersicht,
- Regelkatalog mit Owner, Zweck und Reviewdatum,
- genehmigte Changes mit Test-/Rollback-Hinweis,
- Konfigurations- und Backupnachweise kritischer Komponenten,
- Monitoring- oder Logauswertungen,
- Nachweis über Rückbau nicht mehr benötigter Regeln.

### Fortgeschritten

Ziel: Netzwerksteuerung wird risikoorientiert, automatisiert und mit Detektion verbunden.

1. Netzwerkregeln, Cloud Security Groups, VPNs und Zero-Trust-Policies werden zentral inventarisiert oder regelmäßig automatisiert ausgewertet.
2. Kritische Pfade und unerwartete Erreichbarkeiten werden durch Tests, Attack-Path-Analysen oder Konfigurationsprüfungen sichtbar gemacht.
3. Netzwerkänderungen werden gegen Architekturprinzipien, Datenflüsse und Expositionsrisiken geprüft.
4. Konfigurationsabweichungen und unübliche Verbindungen erzeugen Alerts für Betrieb oder Incident Triage.
5. Management erhält entscheidungsfähige Kennzahlen zu exponierten Diensten, Altregeln, Ausnahmequoten, kritischen Netzwerkfindings und Ressourcenbedarf.

## Ablauf als Routine

1. **Bedarf entsteht:** neuer Service, Änderung, Standort, Cloud-Ressource, Dienstleister oder Incident-Maßnahme.
2. **Verbindung beschreiben:** Quelle, Ziel, Zweck, Protokoll, Datenart, Laufzeit und Owner erfassen.
3. **Risiko prüfen:** Exposition, Schutzbedarf, administrative Funktion, Drittzugriff und Segmentgrenzen bewerten.
4. **Entscheiden:** freigeben, ablehnen, befristen, kompensieren oder Management-Handoff auslösen.
5. **Umsetzen:** Regel oder Konfiguration technisch ändern und testen.
6. **Nachweis sichern:** Change, Konfiguration, Reviewdatum und Owner nachvollziehbar ablegen.
7. **Überwachen:** Logs, Alarme und Konfigurationsänderungen prüfen.
8. **Reviewen:** Altregeln, Ausnahmen und kritische Komponenten regelmäßig bereinigen.
9. **Verbessern:** Findings in Architektur, Segmentierung, Schwachstellenbehandlung oder Betriebsstandards zurückspielen.

## Entscheidungen

- Welche Netzbereiche und Übergänge sind kritisch genug für priorisierten Review?
- Welche Regeltypen brauchen Sicherheitsfreigabe oder Managemententscheidung?
- Wie lange dürfen temporäre Netzwerkfreigaben bestehen?
- Welche Netzwerkkomponenten benötigen besondere Härtung, Monitoring und Patchfrequenz?
- Wann wird ein Netzwerkfinding zum Incident oder Architekturthema?
- Welche Zielkonflikte bestehen zwischen schneller Konnektivität, Verfügbarkeit und Angriffsflächenreduktion?

## Evidenz

### Starke Evidenz

- Netzwerkübersicht mit Ownern, Schutzbedarf und kritischen Übergängen,
- genehmigte Regel- und Konfigurationsänderungen,
- Firewall-/Routing-/Cloud-Regellisten mit Reviewentscheidungen,
- technische Nachweise für Härtung, Backup, Patch oder Konfigurationsänderung,
- Monitoring- und Alertnachweise relevanter Übergänge,
- dokumentierte Ausnahmen mit Ablaufdatum und Risikoentscheidung,
- Managemententscheidung bei dauerhaft offenen Risiken.

### Schwache Evidenz

- veralteter Netzwerkplan ohne Owner oder Datum,
- Firewall-Export ohne Zweck, Entscheidung oder Review,
- pauschale Aussage „Netzwerk ist durch Dienstleister abgesichert“,
- Change-Ticket ohne fachliche Begründung,
- Tool-Dashboard ohne Ableitung von Maßnahmen.

### Evidenzlücken

- unbekannte Internetexposition,
- Regeln ohne Owner oder Laufzeit,
- kritische Netzwerkkomponenten ohne Patch- und Backupnachweis,
- externe Zugänge ohne Vertrags- oder Servicebezug,
- keine Validierung nach Regeländerungen,
- dauerhafte Ausnahmen ohne Managemententscheidung.

## Wirksamkeitsprüfung

Prüffragen:

- Sind kritische Netzbereiche, Übergänge und Owner bekannt?
- Können Firewall- oder Cloud-Regeln einem Zweck und einer Entscheidung zugeordnet werden?
- Werden temporäre oder alte Netzwerkfreigaben entfernt?
- Sind administrative und externe Zugänge besonders kontrolliert?
- Werden Netzwerkkomponenten gepatcht, gesichert und überwacht?
- Haben Reviews zu konkreten Rückbauten, Korrekturen oder Risikoentscheidungen geführt?

Mögliche Kennzahlen:

- Anteil kritischer Übergänge mit aktuellem Owner,
- Anzahl Regeln ohne Zweck oder Reviewdatum,
- überfällige temporäre Freigaben,
- exponierte Dienste nach Kritikalität,
- offene Netzwerkfindings nach Risikoklasse,
- Zeit bis Rückbau nicht mehr benötigter Regeln.

## BSIG-/NIS2-Anschluss

Netzwerksicherheit ist anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Cyberhygiene, Zugriffsschutz, Incident-Prävention, Schwachstellenbehandlung, sichere Betriebsführung und Aufrechterhaltung kritischer Dienste. Der konkrete Bezug sollte im Anforderungsregister und in der organisationsspezifischen Risikoanalyse geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung der Anwendbarkeit oder Nachweispflichten.

## Grenzen

- Dieses Artefakt ist kein vollständiges Netzwerkdesign und keine technische Hardening-Baseline.
- Es ersetzt keine Architektur-, Cloud-, OT- oder Dienstleister-Sicherheitsanalyse.
- Es trifft keine verbindliche Aussage zu gesetzlichen Pflichten oder Zertifizierungsfähigkeit.
- Logging und Monitoring können Datenschutz- oder Beschäftigtenthemen berühren und benötigen geeignete Prüfung.
- Öffentliche Beispiele enthalten keine echten Netzpläne, IP-Adressen, Kundendaten oder geheimen Konfigurationen.

## Handoffs

- **Change-Handoff:** Regeländerungen, Routing, VPN, DNS, Proxy, WLAN, Cloud Security Groups.
- **Incident-Handoff:** verdächtiger Verkehr, laterale Bewegung, kompromittierte Netzwerkkomponente, unerklärte Erreichbarkeit.
- **Schwachstellen-Handoff:** ungepatchte Netzwerkgeräte, unsichere Dienste, exponierte Systeme.
- **Datenschutz-Handoff:** personenbezogene Logauswertungen, Nutzerbezug, Monitoring oder Inhaltsinspektion.
- **Lieferanten-Handoff:** Managed Network, Provider, externe Zugänge, Standortvernetzung.
- **Management-Handoff:** dauerhaft offene Verbindungen, Ressourcenbedarf, Architekturumbau, akzeptiertes Restrisiko.
- **Audit-/Evidence-Handoff:** fehlende Owner, unvollständige Reviews oder unklare Ausnahmeentscheidungen.

## Typische Fehler

- Firewall-Regeln werden ergänzt, aber nie zurückgebaut.
- Netzwerkpläne zeigen Soll-Architektur, aber nicht den betriebenen Ist-Zustand.
- Cloud-Netze werden getrennt vom klassischen Netzwerk betrachtet.
- Dienstleisterzugänge bleiben nach Projektende aktiv.
- Netzwerkkomponenten werden beim Schwachstellenmanagement vergessen.
- Monitoring erzeugt Alarme, aber keine Review- oder Incident-Routine.
- Management sieht technische Listen statt entscheidungsfähiger Risiken.

## Fiktives Mini-Beispiel

Ein fiktiver Maschinenbauer führt einen neuen Remote-Wartungszugang für eine Produktionsanlage ein. Der Service Owner beschreibt Zweck und Laufzeit, der Netzwerk Owner richtet eine befristete VPN-Regel ein, die Security-Rolle verlangt MFA und eingeschränkte Zielsysteme. Nach drei Monaten zeigt der Review, dass der Dienstleisterzugang nicht mehr benötigt wird. Die Regel wird entfernt und der Rückbau im Ticket dokumentiert.

Evidenz:

- genehmigtes Change-Ticket,
- Regelbeschreibung mit Zweck und Laufzeit,
- Nachweis MFA-/Zielsystembeschränkung,
- Reviewnotiz,
- Rückbauticket der VPN-Regel.
