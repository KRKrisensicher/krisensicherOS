
# A.8.24 — Kryptografische Verfahren einsetzen

## Zweck

Kryptografische Verfahren schützen Informationen und Kommunikationswege vor unbefugtem Lesen, Verändern oder Vortäuschen von Identitäten. Die Routine sorgt dafür, dass Verschlüsselung, Signaturen, Zertifikate, Schlüssel und Geheimnisse nicht zufällig pro System gelöst werden, sondern mit klarer Zuständigkeit, Lebenszyklus und Review betrieben werden.

## Control-Ziel in Repo-Sprache

Die Organisation legt fest, wo kryptografische Verfahren benötigt werden, welche Mindestanforderungen gelten, wer Schlüssel und Zertifikate verantwortet, wie Erzeugung, Speicherung, Nutzung, Rotation, Widerruf und Ablauf gesteuert werden und welche Nachweise den sicheren Betrieb plausibel machen.

## Typische Risiken

- Wenn Daten unverschlüsselt übertragen oder gespeichert werden, können sie bei Fehlleitung, Verlust oder Zugriff durch Dritte offengelegt werden.
- Wenn veraltete oder schwache Verfahren genutzt werden, entsteht Scheinschutz trotz aktivierter Verschlüsselung.
- Wenn Zertifikate oder Schlüssel ablaufen, verloren gehen oder unkontrolliert kopiert werden, können Dienste ausfallen oder missbraucht werden.
- Wenn Secrets in Code, Tickets oder Konfigurationsdateien landen, können Angreifer Zugriff auf Systeme und Daten erhalten.
- Wenn Verantwortung für Schlüsselmaterial unklar bleibt, sind Rotation, Widerruf und Notfallwiederherstellung nicht beherrschbar.

## Trigger

- neues System, neue Schnittstelle, neue Datenablage, neue mobile Nutzung oder neue Cloud-/SaaS-Anbindung.
- Verarbeitung oder Übertragung schutzbedürftiger Informationen.
- Zertifikatsablauf, Schlüsselrotation, Kompromittierungsverdacht oder Secret-Leak.
- Architektur-, Entwicklungs-, Beschaffungs- oder Datenschutzreview.
- Schwachstellenmeldung zu Protokoll, Bibliothek, Zertifikat, Schlüsselverwaltung oder Kryptokonfiguration.
- Incident, Auditfinding oder Managementfrage zu Schutzbedarf und Verschlüsselungsabdeckung.

## Rollen und Verantwortung

- **Asset Owner / Service Owner:** bestimmt Schutzbedarf, fachliche Anforderungen und akzeptiert oder eskaliert Restrisiken.
- **IT-/Plattform Owner:** betreibt Zertifikate, Schlüsselverwaltung, Konfigurationen und technische Nachweise.
- **Entwicklung / Product Owner:** integriert Kryptografie sicher in Anwendungen, Schnittstellen, CI/CD und Secrets Management.
- **Security-Architektur / ISMS-Owner:** definiert Mindestanforderungen, Verfahren, Ausnahmeprozess und Reviewlogik.
- **Datenschutz / Legal:** prüfen Anforderungen bei personenbezogenen Daten, Verträgen, Export-/Rechtsfragen oder Nachweispflichten, soweit betroffen.
- **Incident Response:** übernimmt bei Schlüsselkompromittierung, Secret-Leak oder Verdacht auf kryptografisches Versagen.
- **Management:** entscheidet bei Legacy-Ausnahmen, Investitionsbedarf, Risikoakzeptanz oder Betriebszielkonflikten.

## Implementierung

### Minimalstart

Ziel: kritische Verschlüsselungs- und Schlüsselthemen sichtbar und steuerbar machen.

1. Die Organisation benennt kritische Einsatzfälle: Transportverschlüsselung, Datenträgerverschlüsselung, Backups, Cloud-Speicher, administrative Zugänge, API-Kommunikation, E-Mail- oder Dateiaustausch.
2. Für kritische Zertifikate, Schlüssel und Secrets werden Owner, Zweck, Speicherort, Ablaufdatum und Notfallkontakt erfasst.
3. Mindestanforderungen werden festgelegt: keine bekannten schwachen Verfahren, keine Secrets im Klartext in Code oder Tickets, geregelte Zertifikatserneuerung.
4. Neue Systeme und Schnittstellen müssen Verschlüsselungsbedarf im Architektur- oder Change-Prozess benennen.
5. Ausnahmen werden befristet, begründet und mit Risikoentscheidung geführt.

Minimaler Nachweis:

- Kryptografie-/Zertifikatsregister für kritische Einsatzfälle,
- technische Konfigurationsnachweise für ausgewählte kritische Dienste,
- Ablauf- oder Rotationstermine,
- Secret-Leak-Vermeidungsregel für Code und Konfiguration,
- Ausnahmeentscheidungen mit Wiedervorlage.

### Solide Praxis

Ziel: kryptografische Verfahren werden über Lebenszyklus, Rollen und technische Standards wiederholbar betrieben.

1. Kryptografische Mindestanforderungen werden nach Einsatzfall beschrieben: Transport, Speicherung, Backup, mobile Geräte, APIs, Signaturen und Secrets.
2. Zertifikats- und Schlüsselmanagement umfasst Erzeugung, Ablage, Zugriff, Rotation, Backup, Widerruf und Ablaufüberwachung.
3. Secrets werden in geeigneten Secret-Management-Mechanismen geführt und nicht in Repositories, Images, Tickets oder Dokumenten abgelegt.
4. Entwicklungs- und Plattformteams prüfen Kryptokonfigurationen vor Go-live und bei relevanten Änderungen.
5. Veraltete Protokolle, ablaufende Zertifikate und schwache Konfigurationen werden über Schwachstellen- oder Maßnahmenmanagement behandelt.
6. Kritische Ausnahmen werden im ISMS- oder Management Review entschieden.

Starke Evidenz:

- dokumentierte Mindestanforderungen je Einsatzfall,
- Register kritischer Zertifikate, Schlüssel und Secrets mit Ownern,
- technische Scan- oder Konfigurationsnachweise,
- Tickets zur Zertifikatserneuerung, Rotation oder Secret-Bereinigung,
- Reviewprotokolle zu Ausnahmen und Legacy-Verfahren,
- Incident- oder Lessons-Learned-Nachweise bei Secret-Leaks.

### Fortgeschritten

Ziel: Kryptografie wird als integrierter Sicherheitsbaustein in Architektur, Entwicklung und Betrieb gesteuert.

1. Zertifikatsabläufe, schwache TLS-/SSH-/API-Konfigurationen und Secret-Funde werden automatisiert überwacht.
2. Schlüsselmaterial wird rollenbasiert, revisionsfähig und getrennt von Anwendungen verwaltet; besonders kritische Schlüssel nutzen stärkere Schutzmechanismen.
3. CI/CD, Container, Infrastructure as Code und Cloud-Umgebungen enthalten Prüfungen gegen harte Secrets und unsichere Kryptokonfigurationen.
4. Kryptografische Verfahren werden bei Architekturentscheidungen, Datenklassifizierung, Lieferantenbewertung und Notfallplanung berücksichtigt.
5. Management erhält Kennzahlen zu Abdeckung, Ausnahmen, ablaufenden Zertifikaten, Secret-Funden und Legacy-Risiken.

## Ablauf als Routine

1. **Schutzbedarf oder Änderung entsteht:** neues System, Schnittstelle, Datenablage, Zertifikat, Secret oder Finding.
2. **Einsatzfall einordnen:** Transport, Speicherung, Signatur, Authentisierung, Backup, API, mobile Nutzung oder Datenaustausch bestimmen.
3. **Anforderung festlegen:** Verfahren, Schlüssellänge/Parameter, Zertifikatsquelle, Speicherort, Rotation und Verantwortliche definieren, ohne Produkt- oder Normersatz zu erzeugen.
4. **Technisch umsetzen:** Konfiguration, Zertifikat, Schlüsselablage, Secret-Management und Zugriffsschutz einrichten.
5. **Validieren:** Scan, Konfigurationstest, Code-/Repo-Prüfung oder Betriebsnachweis durchführen.
6. **Lebenszyklus steuern:** Ablauf, Rotation, Widerruf, Backup und Notfallzugriff überwachen.
7. **Ausnahmen behandeln:** Legacy, technische Einschränkung oder Lieferantenabhängigkeit befristet entscheiden.
8. **Eskalieren:** Secret-Leak, Schlüsselkompromittierung, kritische Legacy-Verfahren oder Ressourcenkonflikte weitergeben.

## Entscheidungen

- Welche Daten, Systeme und Schnittstellen benötigen kryptografischen Schutz?
- Welche Mindestanforderungen gelten für Transport, Speicherung, Backups, APIs und mobile Nutzung?
- Wer darf Schlüssel erzeugen, nutzen, rotieren, widerrufen oder wiederherstellen?
- Welche Zertifikate und Secrets sind kritisch genug für zentrale Überwachung?
- Wie werden Legacy-Systeme behandelt, die aktuelle Anforderungen nicht erfüllen?
- Wann ist ein kryptografisches Finding ein Incident, ein Change oder eine Managemententscheidung?

## Evidenz

### Starke Evidenz

- Kryptografie- oder Mindestanforderungskonzept mit Einsatzfällen und Ownern,
- Zertifikats-/Schlüssel-/Secret-Register mit Ablauf- und Rotationsterminen,
- technische Nachweise für Verschlüsselung bei kritischen Diensten,
- Repo-/CI-Prüfnachweise gegen Klartext-Secrets,
- Tickets für Rotation, Widerruf, Erneuerung oder Konfigurationskorrektur,
- Ausnahmeentscheidungen mit Ablaufdatum und Kompensationsmaßnahme,
- Incident- und Lessons-Learned-Nachweise bei Secret- oder Schlüsselereignissen.

### Schwache Evidenz

- allgemeine Aussage „Daten werden verschlüsselt“ ohne Scope oder Nachweis,
- Zertifikatsliste ohne Owner oder Ablaufüberwachung,
- Screenshot einer TLS-Verbindung ohne Reviewlogik,
- Passwortgeschützte Datei als Ersatz für Schlüsselmanagement,
- Policy ohne technische Stichprobe.

### Evidenzlücken

- unbekannte Zertifikate oder Schlüssel in kritischen Diensten,
- Secrets in Code, Skripten, Images, Tickets oder Dokumentationen,
- keine Rotation oder kein Widerrufsprozess,
- abgelaufene oder schwache Konfigurationen ohne Maßnahmen,
- Lieferantenkryptografie ohne Nachweis oder Ansprechpartner,
- Ausnahmen ohne Risikoentscheidung.

## Wirksamkeitsprüfung

Prüffragen:

- Sind kritische Kryptografie-Einsatzfälle und Owner bekannt?
- Werden Zertifikate, Schlüssel und Secrets über ihren Lebenszyklus gesteuert?
- Können kritische Dienste technische Verschlüsselungsnachweise vorlegen?
- Werden schwache oder veraltete Verfahren gefunden und behandelt?
- Sind Secrets aus Code, Tickets und Klartextkonfigurationen entfernt oder verhindert?
- Gibt es eine Routine für Ablauf, Rotation, Widerruf und Kompromittierungsverdacht?

Mögliche Kennzahlen:

- kritische Zertifikate mit Ablaufüberwachung,
- Zertifikate kurz vor Ablauf oder abgelaufen,
- offene Kryptografie-Findings nach Risikoklasse,
- Secret-Funde in Repositories oder Artefakten,
- überfällige Schlüsselrotationen,
- Anzahl und Alter kryptografischer Ausnahmen.

## BSIG-/NIS2-Anschluss

Der Einsatz kryptografischer Verfahren ist anschlussfähig an NIS2-orientierte Themen wie Risikomanagement, Cyberhygiene, Zugriffsschutz, sichere Kommunikation, Schutz von Daten, Incident-Prävention, sichere Entwicklung und Lieferkettensicherheit. Die konkrete Einordnung sollte organisationsspezifisch im Anforderungsregister, in Risikoanalysen und technischen Architekturreviews geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung, Datenschutzprüfung oder verbindliche Aussage zu gesetzlichen Anforderungen.

## Grenzen

- Dieses Artefakt ist keine Kryptografie-Bibliotheksempfehlung und keine technische Parameterliste für jeden Einsatzfall.
- Es ersetzt keine Spezialprüfung für Hochsicherheits-, Zahlungs-, Gesundheits-, KRITIS-, Cloud- oder Produktanforderungen.
- Kryptografie schützt nicht gegen falsche Berechtigungen, kompromittierte Endpunkte oder schlechte Schlüsselverwaltung.
- Datenschutz-, Vertrags- oder Exportfragen können menschliche Prüfung erfordern.
- Keine Zertifizierungszusage und keine Übernahme lizenzpflichtiger Normtexte.

## Handoffs

- **Architektur-Handoff:** neue Systeme, Schnittstellen, Datenflüsse, Cloud-Designs oder Legacy-Ausnahmen.
- **Entwicklungs-Handoff:** API-Sicherheit, Bibliotheken, Secrets im Code, CI/CD-Prüfungen, Signaturen.
- **Change-Handoff:** Zertifikatserneuerung, Schlüsselrotation, Protokollabschaltung oder Konfigurationsänderung.
- **Incident-Handoff:** Secret-Leak, Schlüsselkompromittierung, Zertifikatsmissbrauch oder Verdacht auf kryptografisches Versagen.
- **Datenschutz-/Legal-Handoff:** personenbezogene Daten, vertragliche Verschlüsselungsanforderungen, Rechts- oder Exportfragen.
- **Lieferanten-Handoff:** SaaS-/Provider-Verschlüsselung, Schlüsselhaltung, Nachweise, Supportwege.
- **Management-Handoff:** Legacy-Verfahren, Investitionsbedarf, Betriebsrisiko, akzeptiertes Restrisiko.

## Typische Fehler

- Verschlüsselung wird als Häkchen betrachtet, ohne Schlüssel- und Zertifikatslebenszyklus zu betreiben.
- Zertifikate laufen ab, weil Ablaufdaten niemandem gehören.
- Secrets werden in Repositories, Skripten, Tickets oder Wiki-Seiten abgelegt.
- Legacy-Protokolle bleiben aktiv, weil Abschaltung nicht entschieden wird.
- Lieferantenversprechen werden nicht mit Nachweisen oder Verantwortlichkeiten verbunden.
- Backups oder Exporte werden vergessen, obwohl sie dieselben Daten enthalten.
- Management sieht technische Detailfindings, aber keine Entscheidung zu Legacy-Risiken und Ressourcen.

## Fiktives Mini-Beispiel

Ein fiktiver SaaS-Anbieter entdeckt bei einer Repo-Prüfung einen API-Schlüssel in einem alten Deployment-Skript. Das Entwicklungsteam sperrt den Schlüssel, erzeugt einen neuen Secret-Management-Eintrag und entfernt das Skript. Der Plattform Owner prüft zusätzlich die Zertifikatsliste und findet zwei bald ablaufende Zertifikate. Im ISMS-Review wird entschieden, Ablaufwarnungen und Secret-Scans verbindlich in den Releaseprozess aufzunehmen.

Evidenz:

- Secret-Finding und Bereinigungsticket,
- Nachweis Schlüsselwiderruf und Neuanlage im Secret-Management,
- aktualisierte Zertifikatsliste,
- Tickets zur Zertifikatserneuerung,
- Reviewentscheidung zur CI/CD-Prüfung.
