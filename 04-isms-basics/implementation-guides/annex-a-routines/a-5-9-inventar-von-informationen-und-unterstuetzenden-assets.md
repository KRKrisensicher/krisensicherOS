
# A.5.9 — Inventar von Informationen und unterstützenden Assets

## Zweck

Ein Inventar von Informationen und unterstützenden Assets macht sichtbar, welche Informationen, Systeme, Dienste, Geräte, Datenablagen, Schnittstellen und externen Abhängigkeiten für Sicherheit und Betrieb relevant sind. Ohne dieses Bild können Risiken, Zugriffe, Schutzbedarf, Schwachstellen, Notfallplanung und Verantwortlichkeiten nur zufällig gesteuert werden.

Der Kern ist nicht eine perfekte CMDB, sondern ein aktuelles, nutzbares Inventar mit Ownern, Kritikalität, Schutzbedarf und Anschluss an Routinen.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Inventar-Routine, die relevante Informationen und unterstützende Assets im ISMS-Scope identifiziert, verantwortet, klassifiziert, aktualisiert und mit Risiko-, Zugriff-, Schwachstellen-, Lieferanten-, Change- und BCM-Prozessen verbindet.

## Typische Risiken

- Wenn kritische Assets unbekannt sind, werden sie nicht geschützt, gepatcht, gesichert oder im Notfall priorisiert.
- Wenn Informationen nicht zugeordnet sind, fehlen Owner, Schutzbedarf und Nutzungsvorgaben.
- Wenn Inventare veralten, beruhen Risikoanalysen und Reviews auf falschen Annahmen.
- Wenn SaaS-Dienste, Schnittstellen oder Datenablagen fehlen, entstehen Schatten-IT und unkontrollierte Datenflüsse.
- Wenn technische Assets ohne Geschäftsbezug geführt werden, können Schwachstellen und Zugriffe nicht priorisiert werden.
- Wenn unterstützende Assets wie Dienstleister, Schlüssel, Zertifikate, Backups oder Dokumentationsorte fehlen, brechen Abhängigkeiten erst im Ereignisfall auf.

## Trigger

- neuer oder geänderter Service, Prozess, Standort, Datenbestand, System, SaaS-Dienst, Schnittstelle oder Dienstleister.
- Projektstart, Change, Migration, Rückbau, Beschaffung oder Betriebsübergabe.
- Schwachstellenfund, Incident, Auditfinding oder BCM-Übung mit unbekanntem Assetbezug.
- Änderung von Schutzbedarf, Datenklasse, Kritikalität oder Owner.
- turnusmäßiger Inventar-Review.
- Rollenwechsel bei Asset Ownern oder technischen Verantwortlichen.
- Managemententscheidung zu Scope, Priorisierung, Budget oder Risikoakzeptanz.

## Rollen und Verantwortung

- **Asset Owner / Information Owner:** verantwortet fachliche Zuordnung, Schutzbedarf, Kritikalität und Nutzungskontext.
- **IT-/Plattform Owner:** pflegt technische Assetdaten, Lebenszyklus, Konfigurationen und Betriebsstatus.
- **ISMS-Owner / Security-Rolle:** definiert Mindestfelder, Reviewlogik, Risiko- und Evidenzbezug.
- **Fachbereich / Prozess Owner:** benennt Informationen, Datenablagen, Prozesse und Abhängigkeiten.
- **Einkauf / Vendor Management:** liefert Dienstleister-, SaaS- und Vertragsbezüge.
- **BCM-Rolle:** nutzt Inventardaten für Kritikalität, Wiederanlauf, Abhängigkeiten und Notfallplanung.
- **Management:** entscheidet über Scope, Ressourcen, tolerierte Inventarlücken und Priorisierung.

## Implementierung

### Minimalstart

Ziel: die wichtigsten Informationen und Assets im ISMS-Scope sichtbar und verantwortet machen.

1. Die Organisation definiert einen Start-Scope: Kernservices, kritische Prozesse, wichtigste Datenbestände, zentrale Systeme und relevante SaaS-Dienste.
2. Für jeden Eintrag werden Mindestfelder gepflegt: Name, Typ, Owner, Zweck, Kritikalität, Daten-/Schutzbedarf, Standort oder Dienst, technischer Verantwortlicher, Reviewdatum.
3. Neue Projekte und Changes müssen prüfen, ob Inventareinträge anzulegen oder zu ändern sind.
4. Kritische Assets werden mit Zugriff, Backup, Schwachstellenmanagement und Notfallplanung verknüpft.
5. Mindestens quartalsweise oder halbjährlich wird geprüft, ob kritische Einträge aktuell sind.
6. Bekannte Lücken werden mit Owner und Wiedervorlage dokumentiert.

Minimaler Nachweis:

- Inventarliste für kritische Informationen und Assets,
- Owner- und Reviewdatum je kritischem Eintrag,
- Schutzbedarfs- oder Kritikalitätseinstufung,
- Änderungsnachweise aus Projekt/Change,
- Liste offener Inventarlücken.

### Solide Praxis

Ziel: das Inventar wird als Steuerungsgrundlage für ISMS-Routinen genutzt.

1. Assettypen werden unterschieden: Informationen, Anwendungen, Infrastruktur, Endgeräte, Cloud-/SaaS-Dienste, Schnittstellen, Identitäten, Dienstleister, Schlüssel/Zertifikate, Backups.
2. Mindestfelder und Pflegeverantwortung sind je Assettyp definiert.
3. Inventareinträge werden mit Risiken, Controls, Datenklassen, Zugriffsreviews, Schwachstellenquellen, Lieferanten und BCM-Kritikalität verbunden.
4. Lebenszykluszustände werden geführt: geplant, produktiv, eingeschränkt, in Migration, außer Betrieb, archiviert.
5. Stichproben und Abgleiche prüfen Vollständigkeit: Einkauf, Cloud-Konsole, Netzwerk, Endpoint-Management, SaaS-Liste, Projektportfolio.
6. Unbekannte oder nicht zuordenbare Assets werden triagiert und eskaliert.
7. Inventarqualität wird im ISMS-Review berichtet.

Starke Evidenz:

- Asset- und Informationsregister mit definierten Mindestfeldern,
- Owner-Bestätigung kritischer Einträge,
- Abgleichsprotokolle gegen technische oder kaufmännische Quellen,
- Änderungs- und Stilllegungsnachweise,
- Verknüpfungen zu Risiken, Zugriffen, Schwachstellen und BCM,
- Maßnahmenlog für Inventarlücken.

### Fortgeschritten

Ziel: Inventardaten sind aktuell, integriert und entscheidungsfähig.

1. Technische Discovery, Cloud-Inventare, Endpoint-Management, CMDB, SaaS-Register und Vertragsdaten werden zusammengeführt oder regelmäßig abgeglichen.
2. Kritikalität, Exposition, Datenklasse und Abhängigkeiten beeinflussen Priorisierung in Schwachstellen-, Zugriffs-, Backup- und Incident-Prozessen.
3. Änderungen erzeugen automatische oder halbautomatische Inventar-Updates.
4. Abhängigkeiten zwischen Services, Schnittstellen, Dienstleistern und Wiederanlaufzielen sind sichtbar.
5. Management erhält Kennzahlen zu Abdeckung, unbekannten Assets, kritischen Lücken, veralteten Einträgen und technischen Schulden.
6. Inventarqualität wird als Voraussetzung für relevante Sicherheitsentscheidungen behandelt.

## Ablauf als Routine

1. **Asset oder Information entsteht:** neues System, Datenbestand, Dienst, Schnittstelle, Vertrag, Gerät oder Schlüsselmaterial.
2. **Eintrag anlegen oder aktualisieren:** Typ, Zweck, Owner, Verantwortliche, Kritikalität, Schutzbedarf und Status erfassen.
3. **Abhängigkeiten zuordnen:** Prozess, Service, Datenklasse, Zugriff, Lieferant, Backup, Monitoring, Schwachstellenquelle und BCM-Bezug verbinden.
4. **Review durchführen:** Owner bestätigt Aktualität oder meldet Korrekturen.
5. **Lücken bearbeiten:** unbekannte, doppelte, veraltete oder nicht zuordenbare Assets triagieren.
6. **Änderungen nachhalten:** Projekte, Changes, Migrationen und Stilllegungen aktualisieren das Inventar.
7. **Evidenz sichern:** Review, Abgleich, Korrektur und Managemententscheidungen dokumentieren.
8. **Verbessern:** Mindestfelder, Quellen und Abgleiche an Findings und Betriebsbedarf anpassen.

## Entscheidungen

- Welche Informationen und Assets sind für den Start-Scope kritisch genug?
- Welche Mindestfelder sind notwendig, ohne das Inventar unpflegbar zu machen?
- Wer darf Kritikalität, Schutzbedarf und Owner ändern?
- Welche Inventarlücken sind tolerierbar, welche müssen eskaliert werden?
- Welche Quellen gelten als führend: Fachbereich, IT, Einkauf, Cloud-Plattform, CMDB?
- Wie wird mit Schatten-IT, unbekannten SaaS-Diensten oder nicht zuordenbaren Assets umgegangen?

## Evidenz

### Starke Evidenz

- aktuelles Inventar mit Ownern, Kritikalität, Schutzbedarf und Reviewdatum,
- Nachweise über Owner-Reviews und Korrekturen,
- Abgleich gegen technische, kaufmännische oder projektbezogene Quellen,
- Verknüpfung kritischer Assets zu Risiko-, Zugriff-, Schwachstellen-, Backup- und BCM-Routinen,
- Stilllegungs- oder Änderungsnachweise,
- Maßnahmen und Entscheidungen zu Inventarlücken,
- Managemententscheidung bei nicht tragbaren unbekannten Assets oder Ressourcenbedarf.

### Schwache Evidenz

- einmalige Excel-Liste ohne Owner oder Reviewdatum,
- rein technische Geräteliste ohne Geschäftsbezug,
- CMDB-Auszug ohne Kritikalität und Schutzbedarf,
- Assetliste nur für On-Premise-Systeme ohne SaaS und Cloud,
- Inventarpolicy ohne Nachweis der Pflege,
- Screenshots einzelner Tools ohne Abgleich oder Entscheidung.

### Evidenzlücken

- kritische Services ohne zugeordnete Assets,
- Informationen ohne Owner,
- unbekannte externe Dienste oder Datenablagen,
- technische Konten, Zertifikate oder Schnittstellen ohne Verantwortlichen,
- keine Verbindung zu Schwachstellenmanagement oder Backup,
- veraltete Einträge nach Migration oder Stilllegung,
- keine Review- oder Abgleichsroutine.

## Wirksamkeitsprüfung

Prüffragen:

- Sind die wichtigsten Informationen, Systeme, Dienste und Abhängigkeiten im Scope sichtbar?
- Hat jedes kritische Asset einen fachlichen und technischen Verantwortlichen?
- Werden neue Projekte, Changes und Beschaffungen im Inventar nachgezogen?
- Können Schwachstellen, Zugriffe und Notfallplanung auf Inventardaten aufbauen?
- Werden unbekannte oder veraltete Assets gefunden und behandelt?
- Führt das Inventar zu Entscheidungen, Priorisierung und Maßnahmen statt nur zu Ablage?

Mögliche Kennzahlen:

- Anteil kritischer Assets mit Owner und Reviewdatum,
- Anzahl unbekannter oder nicht zuordenbarer Assets,
- Anteil Assets mit Kritikalität und Schutzbedarf,
- überfällige Inventarreviews,
- Abweichungen aus technischen oder kaufmännischen Abgleichen,
- Anteil kritischer Assets mit Backup-, Schwachstellen- und BCM-Bezug.

## BSIG-/NIS2-Anschluss

Ein belastbares Inventar ist anschlussfähig an NIS2-orientiertes Risikomanagement, Incident Handling, Schwachstellenmanagement, Zugriffsschutz, Lieferkettensicherheit, Business Continuity und Managementaufsicht. Für betroffene Organisationen sollte der konkrete Bezug im Anforderungsregister, in Risikoanalyse und Evidence Pack geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung der Anwendbarkeit und keine verbindliche Festlegung gesetzlicher Nachweispflichten.

## Grenzen

- Dieses Artefakt ist kein vollständiges CMDB- oder ITAM-Tooldesign.
- Es ersetzt keine technische Discovery, Vertragsprüfung, Datenschutzinventare oder Architekturmodellierung.
- Es gibt keine Zertifizierungs-, Konformitäts- oder Sicherheitsgarantie.
- Es enthält keine lizenzpflichtigen Normtexte.
- Ein Inventar ist nur so belastbar wie seine Pflege- und Reviewroutine.

## Handoffs

- **Projekt-/Change-Handoff:** neue, geänderte oder stillgelegte Assets und Datenbestände.
- **Zugriffs-Handoff:** Owner, kritische Datenbestände, Adminzugriffe und externe Zugriffe.
- **Schwachstellen-Handoff:** technische Assets, Exposition, Kritikalität und Patchverantwortung.
- **BCM-Handoff:** kritische Services, Abhängigkeiten, Wiederanlauf und Notfallpriorisierung.
- **Lieferanten-Handoff:** SaaS, Managed Services, Drittprodukte, Supportzugriffe und Vertragsbezug.
- **Datenschutz-/Legal-Handoff:** personenbezogene Daten, Aufbewahrung, Vertrags- oder Rechtsfragen.
- **Management-Handoff:** unbekannte kritische Assets, Ressourcenbedarf, nicht akzeptable Inventarlücken.
- **Audit-/Evidence-Handoff:** fehlende Owner, fehlende Reviews oder nicht nachvollziehbare Abdeckung.

## Typische Fehler

- Das Inventar wird einmalig aufgebaut und danach nicht betrieben.
- Nur Server werden erfasst, aber Informationen, SaaS, Schnittstellen und Dienstleister fehlen.
- Owner werden eingetragen, prüfen aber nie die Aktualität.
- Kritikalität wird technisch geschätzt und nicht mit Geschäftsprozessen verbunden.
- Stillgelegte Systeme bleiben im Inventar, neue Cloud-Ressourcen fehlen.
- Inventar und Schwachstellenmanagement arbeiten mit unterschiedlichen Assetnamen.
- Management erhält Listen, aber keine Aussage zu Lücken, Prioritäten und Risiken.

## Fiktives Mini-Beispiel

Ein fiktiver Mittelständler nimmt ein Kundenportal in den ISMS-Scope. Der ISMS-Owner erstellt mit IT und Fachbereich ein Minimalinventar: Portal, Datenbank, Identitätsdienst, Backup-Speicher, Monitoring, externer Hostingdienst und zwei Schnittstellen. Beim Review fehlt ein Owner für eine alte Exportablage. Der Fachbereich benennt den Owner, reduziert die Aufbewahrung und erstellt ein Change-Ticket zur Stilllegung.

Evidenz:

- Inventareinträge mit Ownern und Kritikalität,
- Reviewnotiz zur Exportablage,
- Entscheidung zur Stilllegung,
- Change-Ticket,
- aktualisierte Verbindung zu Backup und Schwachstellenprozess.
