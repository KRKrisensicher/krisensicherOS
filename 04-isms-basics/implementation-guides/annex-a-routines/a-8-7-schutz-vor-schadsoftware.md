
# A.8.7 — Schutz vor Schadsoftware

## Zweck

Schutz vor Schadsoftware reduziert die Wahrscheinlichkeit, dass schädlicher Code auf Endgeräten, Servern, Cloud-Workloads, E-Mail-Systemen, Speichern, mobilen Geräten oder Entwicklungsumgebungen ausgeführt wird und unbemerkt Schaden verursacht. Der Kern ist nicht „ein Virenscanner ist installiert“, sondern eine betriebene Schutz-, Überwachungs- und Reaktionsroutine.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Routine zur Prävention, Erkennung, Behandlung und Verbesserung im Umgang mit Schadsoftware. Schutzmechanismen, Verantwortlichkeiten, Abdeckung, Alarme, Ausnahmen, Incident-Handoffs und Lessons Learned sind so verbunden, dass aus technischen Warnungen handlungsfähige Entscheidungen entstehen.

## Typische Risiken

- Wenn Endpunkte, Server oder Cloud-Workloads nicht abgedeckt sind, kann Schadsoftware unbemerkt ausgeführt werden.
- Wenn Schutzsignaturen, Sensoren oder Policies veraltet sind, entsteht Scheinschutz.
- Wenn Alarme niemandem zugeordnet sind, bleiben Infektionen oder verdächtige Aktivitäten unbehandelt.
- Wenn Ausnahmen für Performance oder Kompatibilität dauerhaft werden, entstehen blinde Flecken.
- Wenn E-Mail-, Web-, USB- oder Download-Wege nicht betrachtet werden, erreichen Schadprogramme Nutzer und Systeme leichter.
- Wenn Wiederherstellung und Incident Response nicht eingebunden sind, dauert Eindämmung zu lange.

## Trigger

- neues Endgerät, Server, Cloud-Workload, mobiles Gerät, Entwicklungsumgebung oder Speicherort.
- neue Schutzlösung, Policyänderung, Ausnahme oder Deaktivierung eines Schutzmechanismus.
- Malware-Alarm, verdächtiges Verhalten, Phishing-Welle, kompromittierter Account oder Incident.
- Schwachstellenmeldung, neue Angriffswelle oder Herstellerhinweis.
- Auditfinding, fehlende Abdeckung, veraltete Signaturen oder Sensor-Ausfall.
- neue Datenübertragungswege wie E-Mail-Gateway, Webproxy, Dateiaustausch, externe Datenträger oder SaaS-Speicher.
- turnusmäßiger Review der Abdeckung, Alarme, Ausnahmen und Wirksamkeit.

## Rollen und Verantwortung

- **Endpoint-/Platform Owner:** betreibt Schutzagenten, Policies, Updates und technische Abdeckung.
- **Security Operations / Security-Rolle:** triagiert Alarme, definiert Erkennungslogik und steuert Eskalationen.
- **IT-Betrieb / Service Desk:** unterstützt Eindämmung, Neuinstallation, Nutzerkommunikation und Wiederherstellung.
- **Service Owner / Asset Owner:** bewertet Auswirkungen auf Service, Daten und Geschäftsprozess.
- **ISMS-Owner:** stellt Reviewlogik, Ausnahmebehandlung, Evidenz und Management-Handoff sicher.
- **Awareness-/HR-Funktion:** unterstützt Nutzerbefähigung zu Phishing, Downloads und Meldewegen.
- **Datenschutz / Legal:** prüft personenbezogene Auswertungen, mögliche Datenschutzvorfälle und externe Kommunikation.
- **Management:** entscheidet bei Restrisiken, Ressourcenbedarf, Tooling, Ausnahmequoten oder Betriebsunterbrechungen.

## Implementierung

### Minimalstart

Ziel: wichtige Systeme abdecken, Alarme behandeln und Ausnahmen sichtbar machen.

1. Kritische Endpunkte, Server, Cloud-Workloads, E-Mail-Systeme und Dateispeicher im ISMS-Scope werden benannt.
2. Für diese Ziele wird festgelegt, welcher Schutzmechanismus aktiv ist und wer Alarme behandelt.
3. Schutzstatus, Update-/Signaturstatus und Sensorverfügbarkeit werden regelmäßig geprüft.
4. Malware-Alarme werden als Ticket oder Incident-Vorprüfung erfasst.
5. Ausnahmen, Deaktivierungen und nicht abgedeckte Systeme erhalten Begründung, Ablaufdatum und Review.
6. Nutzer kennen einen Meldeweg für verdächtige Dateien, E-Mails oder Systemverhalten.

Minimaler Nachweis:

- Abdeckungsliste mit Owner,
- Schutzstatus- oder Agentenexport,
- Alarm-/Ticketnachweise,
- Ausnahme- oder Deaktivierungslog,
- Kommunikationsnachweis zum Meldeweg.

### Solide Praxis

Ziel: Schadsoftwareschutz wird risikobasiert und mit Incident Response verbunden betrieben.

1. Schutzmechanismen werden nach Assettyp und Risiko unterschieden: Client, Server, Cloud, E-Mail, Web, mobile Geräte, Entwicklungsumgebungen.
2. Alarme werden priorisiert nach Kritikalität, Verbreitung, betroffenen Daten, Verhalten und möglicher Ausnutzung.
3. Eindämmungsschritte sind vorbereitet: isolieren, Konto prüfen, Datei sperren, Systeme bereinigen, neu aufsetzen, Wiederherstellung einleiten.
4. Ausnahmen werden regelmäßig auf Notwendigkeit, Kompensation und Ablauf geprüft.
5. Wiederholte Funde fließen in Awareness, Hardening, Patchmanagement und E-Mail-/Web-Schutz ein.
6. Schutzstatus und Top-Risiken werden im ISMS-Review und bei Bedarf im Management Review behandelt.

### Fortgeschritten

Ziel: Schadsoftwareschutz wird als integrierte Detektions- und Reaktionsfähigkeit betrieben.

1. Endpoint-, Server-, Cloud-, E-Mail- und Identitätssignale werden in Security Monitoring oder Incident Triage zusammengeführt.
2. Verhaltensbasierte Erkennung, kontrollierte Ausführung, Applikationskontrolle oder Sandboxing werden risikobasiert eingesetzt.
3. Automatisierte Eindämmung wird für klar definierte Szenarien genutzt, ohne menschliche Eskalation bei kritischen Auswirkungen zu verlieren.
4. Threat-Intelligence- und Incident-Lessons-Learned aktualisieren Erkennungsregeln, Blocklisten und Nutzerkommunikation.
5. Schutzlücken werden mit Assetinventar, Schwachstellenmanagement, Backup und BCM abgeglichen.
6. Management erhält Kennzahlen zu Abdeckung, Alarmqualität, Eindämmungszeit, Ausnahmequote und wiederkehrenden Ursachen.

## Ablauf als Routine

1. **Scope aktualisieren:** neue oder geänderte Assets, Datenwege und Plattformen aufnehmen.
2. **Schutzstatus prüfen:** Agenten, Policies, Signaturen, Sensoren, Gateways und Updates kontrollieren.
3. **Alarme triagieren:** betroffene Systeme, Nutzer, Daten, Verbreitung und Schwere bewerten.
4. **Eindämmen:** Netzwerkzugang, Konto, Datei, Prozess oder System je nach Lage begrenzen.
5. **Behandeln:** bereinigen, neu aufsetzen, patchen, blockieren, wiederherstellen oder Incident-Prozess starten.
6. **Nachweisen:** Alarm, Entscheidung, Maßnahme, Ergebnis und offene Risiken dokumentieren.
7. **Reviewen:** Abdeckung, Ausnahmen, Fehlalarme, Reaktionszeiten und wiederkehrende Muster prüfen.
8. **Verbessern:** Policies, Awareness, Hardening, Backup, Monitoring oder Beschaffung anpassen.
9. **Eskalieren:** größere Ausbreitung, Datenbezug, Betriebsunterbrechung oder Restrisiko an Management, Legal, Datenschutz oder BCM geben.

## Entscheidungen

- Welche Assettypen und Datenwege müssen zwingend geschützt und überwacht werden?
- Welche Alarme lösen Ticket, Incident-Vorprüfung oder formalen Incident aus?
- Wer darf Schutzmechanismen deaktivieren oder Ausnahmen genehmigen?
- Welche Kompensationsmaßnahmen gelten für nicht abdeckbare Systeme?
- Wann wird ein System bereinigt, isoliert, neu aufgesetzt oder wiederhergestellt?
- Welche personenbezogenen Auswertungen sind für Triage und Monitoring erforderlich und zu klären?

## Evidenz

### Starke Evidenz

- Abdeckung kritischer Assets mit Schutzstatus und Owner,
- Policy- und Update-/Signaturnachweise,
- Alarmtickets mit Triage, Entscheidung und Maßnahme,
- Nachweise zu Eindämmung, Bereinigung oder Wiederherstellung,
- Ausnahmeentscheidungen mit Ablaufdatum und Kompensation,
- Lessons Learned aus Malware-Incidents,
- Managemententscheidung bei Restrisiken oder Ressourcenbedarf.

### Schwache Evidenz

- Kaufnachweis einer Schutzlösung ohne Abdeckungsprüfung,
- Screenshot eines Agents ohne Scope,
- Alarmstatistik ohne Triage oder Maßnahmen,
- pauschale Aussage „wird vom Dienstleister gemacht“ ohne Rückmeldung,
- Ausnahmeliste ohne Ablaufdatum,
- Awareness-Kampagne ohne Verbindung zu Funden oder Meldeweg.

### Evidenzlücken

- unbekannte Systeme ohne Schutzagent,
- veraltete oder deaktivierte Sensoren ohne Entscheidung,
- Alarme ohne Owner,
- wiederholte Malware-Funde ohne Ursachenanalyse,
- keine Einbindung von Backup oder Incident Response,
- keine Dokumentation, ob Daten oder kritische Dienste betroffen waren.

## Wirksamkeitsprüfung

Prüffragen:

- Sind kritische Endpunkte, Server, Cloud-Workloads und Datenwege abgedeckt?
- Werden Schutzstatus und Sensorverfügbarkeit regelmäßig geprüft?
- Können Alarme einem Owner, einer Entscheidung und einer Maßnahme zugeordnet werden?
- Werden Ausnahmen befristet und mit Kompensation betrieben?
- Fließen wiederkehrende Funde in Patchmanagement, Hardening oder Awareness zurück?
- Ist klar, wann Malware-Funde zum Incident, Datenschutz- oder BCM-Thema werden?

Mögliche Kennzahlen:

- Abdeckung kritischer Assets,
- Systeme mit veraltetem oder fehlendem Schutz,
- Malware-Alarme nach Schwere und Status,
- mittlere Triage- und Eindämmungszeit,
- Ausnahmequote und überfällige Ausnahmen,
- wiederkehrende Funde pro Assetgruppe,
- Anteil Alarme mit dokumentierter Entscheidung.

## BSIG-/NIS2-Anschluss

Schutz vor Schadsoftware ist anschlussfähig an NIS2-orientierte Themen wie Cyberhygiene, Incident-Prävention, Erkennung, Reaktion, Business Continuity, Schwachstellenmanagement und sichere Betriebsprozesse. Der konkrete Bezug sollte im Anforderungsregister, in Risikoanalysen und in Incident-/BCM-Unterlagen organisationsspezifisch geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung von Meldepflichten, Datenschutzfolgen oder Anwendbarkeit.

## Grenzen

- Dieses Artefakt ist keine Empfehlung für ein konkretes EDR-, Antivirus- oder Gateway-Produkt.
- Es ersetzt keine Incident-Response-Planung, Backup-Strategie oder technische Forensik.
- Malware-Schutz garantiert keine Schadensvermeidung.
- Personenbezogene Monitoring- und Triage-Daten benötigen geeignete Prüfung.
- Keine ISO-27002-Texte, keine echten Schadsoftwaredetails aus vertraulichen Fällen.

## Handoffs

- **Incident-Handoff:** bestätigte Infektion, Ausbreitung, Datenbezug, kompromittierte Konten oder kritische Systeme.
- **Backup-/Recovery-Handoff:** Bereinigung nicht ausreichend, Wiederherstellung oder Neuaufbau erforderlich.
- **BCM-Handoff:** Malware gefährdet kritische Dienste, Produktionsfähigkeit oder Wiederanlaufziele.
- **Datenschutz-/Legal-Handoff:** personenbezogene Daten betroffen, Monitoring-Auswertung, mögliche externe Kommunikation.
- **Patch-/Hardening-Handoff:** wiederkehrende Funde durch Schwachstellen, Makros, Skripte, unsichere Konfigurationen.
- **Awareness-Handoff:** Phishing, Downloads, Meldewegprobleme oder Fehlbedienungen als Ursache.
- **Management-Handoff:** hohe Restrisiken, Tooling-Lücken, Ausnahmequote, Ressourcenbedarf oder Betriebsunterbrechung.
- **Audit-/Evidence-Handoff:** fehlende Abdeckung, unklare Alarmbehandlung oder nicht nachvollziehbare Ausnahmen.

## Typische Fehler

- Eine installierte Schutzlösung wird mit wirksamem Betrieb verwechselt.
- Nicht abgedeckte Systeme werden im Assetinventar nicht sichtbar.
- Alarme bleiben im Tool, statt in Tickets oder Incident Triage zu gelangen.
- Ausnahmen werden aus Performancegründen dauerhaft.
- Entwicklungs-, Server- oder Cloud-Workloads werden schlechter geschützt als Bürogeräte.
- Malware-Funde führen nicht zu Lessons Learned.
- Management erhält Alarmmengen, aber keine Risikoeinschätzung oder Entscheidungsfrage.

## Fiktives Mini-Beispiel

Ein fiktiver Dienstleister erhält mehrere Malware-Alarme auf zwei Entwicklungsrechnern. Security Operations erstellt Tickets, isoliert die Geräte und prüft, ob Repository-Zugänge betroffen sind. Die Rechner werden neu aufgesetzt; ein veraltetes Browser-Plugin wird als Ursache identifiziert. Der ISMS-Owner dokumentiert eine Maßnahme zur Härtung der Entwickler-Images und ein kurzes Awareness-Briefing zu verdächtigen Downloads.

Evidenz:

- Alarmtickets,
- Isolations- und Neuaufsetzungsnachweis,
- Prüfung betroffener Zugriffe,
- Maßnahme zur Image-Härtung,
- Awareness-Briefing und Reviewnotiz.
