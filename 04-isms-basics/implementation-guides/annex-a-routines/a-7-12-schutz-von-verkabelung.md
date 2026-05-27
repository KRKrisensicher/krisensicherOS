
# A.7.12 — Schutz von Verkabelung

## Zweck

Verkabelung verbindet Systeme, Räume, Standorte, Netzsegmente, Sensorik und Versorgungsinfrastruktur. Ungeschützte oder unklare Kabelwege können Ausfälle, Manipulation, Fehlanschlüsse, unbefugtes Mithören, Sabotage oder schwierige Wiederherstellung verursachen. Diese Routine sorgt dafür, dass kritische Kabelwege, Patchfelder, Leitungswege und Anschlussdosen nicht als unsichtbare Infrastruktur behandelt werden.

Der Kern ist nicht „Kabel ordentlich verlegen“, sondern eine betriebene Schutzlogik: Welche Verbindungen sind kritisch, wo verlaufen sie, wer darf Änderungen vornehmen, wie werden Manipulation und Fehlpatching verhindert und wie wird nachgewiesen, dass der Zustand kontrolliert bleibt?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der kritische Daten-, Netzwerk-, Kommunikations- und relevante Versorgungsverkabelung geplant, dokumentiert, gegen unbeabsichtigte oder unbefugte Einwirkung geschützt, geändert und reviewed wird.

## Typische Risiken

- Wenn Patchfelder oder Netzwerkdosen frei zugänglich sind, können unbefugte Geräte angeschlossen oder Verbindungen verändert werden.
- Wenn Kabelwege nicht dokumentiert sind, verzögern Störungen, Umzüge und Wiederanlaufmaßnahmen den Betrieb.
- Wenn kritische Leitungen durch öffentliche oder ungeschützte Bereiche laufen, können Beschädigung, Manipulation oder Abhören wahrscheinlicher werden.
- Wenn Änderungen an Verkabelung informell erfolgen, entstehen Fehlpatching, Netzsegmentierungsfehler oder Schattenverbindungen.
- Wenn Daten- und Versorgungsverkabelung ohne Abstimmung verändert wird, können Ausfälle oder Sicherheitslücken entstehen.
- Wenn temporäre Kabel für Projekte dauerhaft bleiben, umgehen sie Schutz- und Dokumentationslogik.

## Trigger

- Neubau, Umbau, Renovierung, Umzug oder Flächenänderung.
- neue oder geänderte Netzwerk-, Telefonie-, Produktions-, Gebäude- oder Sicherheitsverkabelung.
- Patchänderung, neue Netzwerkdose, Carrier-/WAN-Änderung oder Technikraumänderung.
- Störung, Ausfall, Manipulationsverdacht, unklarer Port oder unbekanntes Gerät.
- neuer Dienstleister, Wartung, Gebäudearbeiten oder Facility-Maßnahme.
- Auditfinding, Standortreview oder Sicherheitsereignis.
- turnusmäßiger Review von Technikräumen, Patchfeldern, Kabelwegen und Dokumentation.

## Rollen und Verantwortung

- **Netzwerk-/IT-Infrastruktur Owner:** verantwortet technische Verkabelungslogik, Patchfelder, Netzwerkdosen, Dokumentation und Änderungsfreigaben.
- **Facility-/Standort Owner:** verantwortet bauliche Kabelwege, Schächte, Räume, Dienstleisterzugang und Schutz vor Umwelteinwirkung.
- **Service Owner / Asset Owner:** bewertet Kritikalität betroffener Verbindungen und Auswirkung von Änderungen.
- **ISMS-Owner / Security-Rolle:** definiert Schutz-, Review- und Ausnahmeanforderungen für kritische Kabelwege.
- **Dienstleister / Installationspartner:** setzt Änderungen nur nach Auftrag, Freigabe und Dokumentationsanforderung um.
- **BCM-Owner / Krisenrolle:** berücksichtigt kritische Verbindungen in Wiederanlauf- und Ausweichplanung.
- **Management:** entscheidet bei baulichem Schutzbedarf, Redundanzkosten, Restrisiken oder dauerhaften Ausnahmen.

## Implementierung

### Minimalstart

Ziel: Kritische Verkabelung und Patchpunkte sind sichtbar, geschützt und änderungskontrolliert.

1. Die Organisation identifiziert kritische Kabelbereiche: Technikräume, Patchfelder, Carrier-Übergabepunkte, Verbindungen zu kritischen Systemen, Außenstellen, Produktions- oder Gebäudetechnik.
2. Für diese Bereiche werden Owner und Kontaktwege benannt.
3. Änderungen an kritischen Patchungen oder Kabelwegen erfolgen nur per Ticket oder dokumentiertem Arbeitsauftrag.
4. Offene Patchfelder, unklare Ports, lose oder temporäre Kabel werden im Standortreview erfasst.
5. Kritische Bereiche werden gegen einfachen unbefugten Zugriff geschützt, etwa durch abschließbare Räume, Schränke oder klare Zutrittsregel.
6. Ausnahmen werden befristet und mit Risiko- oder Servicebezug dokumentiert.

Minimaler Nachweis:

- Liste kritischer Kabelbereiche oder Patchpunkte,
- Owner- und Kontaktzuordnung,
- einfache Verkabelungs- oder Patchdokumentation,
- Änderungsticket oder Arbeitsauftrag,
- Reviewnotiz mit Findings und Maßnahmen,
- Ausnahme mit Frist.

### Solide Praxis

Ziel: Verkabelungsschutz ist in Facility-, Netzwerk- und Change-Prozesse integriert.

1. Kabelwege und Patchfelder werden nach Kritikalität und Zugänglichkeit klassifiziert.
2. Mindestschutz wird festgelegt: Zutritt, Beschriftung, Dokumentation, Trennung relevanter Leitungen, Schutz vor Beschädigung, Dienstleisterbegleitung.
3. Patch- und Kabeländerungen werden über Change Management, Arbeitsauftrag oder Wartungsfenster gesteuert.
4. Netzwerkdosen und Ports werden mit Inventar, Raum, Segment oder Zweck verbunden.
5. Unbekannte oder nicht genutzte Ports werden geprüft und bei Bedarf deaktiviert oder dokumentiert.
6. Umbauten und Renovierungen enthalten eine IT-/Security-Prüfung für Kabelwege.
7. Regelmäßige Stichproben vergleichen Dokumentation und tatsächlichen Zustand.

Starke Evidenz:

- Patch- und Kabeldokumentation mit Datum,
- Change-/Arbeitsaufträge mit Freigabe und Abschlussnotiz,
- Standortreview von Technikräumen und Patchfeldern,
- Port-/Doseninventar oder Netzplandaten,
- Nachweis behobener Fehlpatches oder offener Kabelmängel,
- Dienstleisterprotokolle und Abnahmen.

### Fortgeschritten

Ziel: Kritische Verbindungen werden mit Segmentierung, Monitoring, Redundanz und Resilienzplanung verbunden.

1. Kritische Kabelwege und Carrier-Übergaben sind in Netzwerkarchitektur, CMDB, BIA und Wiederanlaufplänen verknüpft.
2. Redundante Leitungswege werden bewusst geplant, dokumentiert und auf gemeinsame Schwachstellen geprüft.
3. Port-Security, NAC, Link-Monitoring oder vergleichbare Kontrollen erkennen unerwartete Geräte oder Verbindungsänderungen.
4. Bauliche Kabelwege, Schächte und Technikräume werden mit Facility-Risikoreviews verbunden.
5. Kritische Patch- oder Leitungsänderungen erzeugen automatische oder halbautomatische Service- und Security-Checks.
6. Management erhält Informationen zu Single Points of Failure, baulichen Schutzlücken und Investitionsbedarf.

## Ablauf als Routine

1. **Änderungs- oder Reviewbedarf entsteht:** Umbau, Patchänderung, Störung, neuer Dienst oder Standortreview.
2. **Kritikalität bestimmen:** betroffene Services, Netzsegmente, Standorte, Datenflüsse und Wiederanlaufrelevanz einordnen.
3. **Kabelweg oder Patchpunkt prüfen:** Zugänglichkeit, Dokumentation, Beschriftung, Schutz und Abhängigkeiten bewerten.
4. **Änderung freigeben:** Owner, Change-Fenster, Dienstleisterzugang und Rollback-/Wiederherstellungsoption klären.
5. **Umsetzen:** Patchen, Verlegen, Schützen, Entfernen oder Deaktivieren gemäß Auftrag.
6. **Dokumentieren:** Pläne, Portdaten, Tickets, Fotos nur falls unkritisch, Abnahme oder Testnachweise aktualisieren.
7. **Validieren:** Verbindung, Segmentierung, Servicefunktion und unerwartete Nebeneffekte prüfen.
8. **Reviewen:** Stichproben und Findings in Maßnahmenlog und Risikoanalyse zurückspielen.
9. **Eskalieren:** bauliche Mängel, Single Points of Failure oder nicht akzeptable temporäre Lösungen ins Management geben.

## Entscheidungen

- Welche Kabelwege, Patchfelder und Übergabepunkte sind kritisch?
- Welche Bereiche brauchen baulichen oder organisatorischen Zugriffsschutz?
- Welche Änderungen dürfen im Standardprozess erfolgen, welche brauchen Change- oder Managementfreigabe?
- Wie detailliert muss Verkabelung dokumentiert werden, ohne sensible Pläne unnötig breit zugänglich zu machen?
- Welche temporären Kabel oder Provisorien sind zulässig und wie lange?
- Wann braucht es Redundanz, getrennte Leitungswege oder zusätzlichen Schutz?
- Wie werden unbekannte Ports, Dosen oder Geräte behandelt?

## Evidenz

### Starke Evidenz

- aktuelle Patch-, Port- oder Kabelwegedokumentation für kritische Bereiche,
- Tickets oder Arbeitsaufträge zu Änderungen,
- Abnahme- und Testnachweise nach Verkabelungsarbeiten,
- Standortreview mit Findings, Maßnahmen und Ownern,
- Nachweis deaktivierter oder bereinigter unbekannter Ports,
- Risikoentscheidung zu temporären Kabeln oder ungeschützten Leitungswegen,
- Managemententscheidung bei Redundanz- oder Bauinvestitionen.

### Schwache Evidenz

- veralteter Netzwerkplan ohne Abgleich mit Ist-Zustand,
- Fotos von Patchfeldern ohne Datum, Owner oder Bewertung,
- Dienstleisterrechnung ohne Dokumentations- oder Abnahmebezug,
- mündliche Aussage „das macht der Elektriker“ ohne Auftrag und Freigabe,
- Kabelbeschriftung ohne Verbindung zu Service oder Inventar.

### Evidenzlücken

- kritische Patchfelder ohne Zutritts- oder Änderungsregel,
- unbekannte aktive Ports,
- temporäre Kabel ohne Ablaufdatum,
- Umbauten ohne IT-/Security-Prüfung,
- Redundanzannahmen ohne Nachweis getrennter Wege,
- Kabeländerungen ohne Dokumentationsupdate.

## Wirksamkeitsprüfung

Prüffragen:

- Sind kritische Kabelwege, Patchpunkte und Übergaben bekannt?
- Stimmen Dokumentation und tatsächlicher Zustand in Stichproben überein?
- Werden Kabel- und Patchänderungen kontrolliert freigegeben und dokumentiert?
- Sind frei zugängliche Patchfelder oder aktive Ports bewertet?
- Werden temporäre Kabel und Provisorien zurückgebaut oder entschieden?
- Sind Single Points of Failure und Redundanzannahmen geprüft?
- Fließen Störungen und Fehlpatches in Verbesserungen ein?

Mögliche Kennzahlen:

- Anteil kritischer Patchbereiche mit aktueller Dokumentation,
- offene Findings aus Kabel-/Patchreviews,
- unbekannte aktive Ports,
- überfällige temporäre Verkabelungen,
- Störungen durch Fehlpatching oder Kabelschäden,
- überfällige Dokumentationsupdates nach Changes.

## BSIG-/NIS2-Anschluss

Der Schutz von Verkabelung ist anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Betriebssicherheit, physische Sicherheit, Aufrechterhaltung kritischer Dienste, Incident-Prävention und Business Continuity. Der konkrete Bezug sollte im Anforderungsregister, in Architekturunterlagen und in Standort-/BCM-Reviews geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Prüfung, keine Fachplanung für Elektro-/Netzwerkinfrastruktur und keine verbindliche Aussage zur Anwendbarkeit.

## Grenzen

- Dieses Artefakt ist kein technischer Verkabelungsstandard und keine Installationsnorm.
- Es ersetzt keine Bau-, Elektro-, Brandschutz-, Arbeitsschutz- oder Versicherungsprüfung.
- Es ersetzt keine Netzwerkarchitektur oder Segmentierungsbaseline.
- Es trifft keine Zertifizierungs- oder Konformitätszusage.
- Detaillierte Kabel- und Netzpläne können vertraulich sein und gehören nicht in öffentliche Beispiele.

## Handoffs

- **Facility-Handoff:** Schächte, Trassen, Räume, baulicher Schutz, Renovierung, Dienstleisterzugang und Gebäudearbeiten.
- **IT-/Netzwerk-Handoff:** Patchung, Portfreigabe, Segmentierung, Dokumentation, Monitoring und Störungsbearbeitung.
- **Change-Handoff:** kritische Leitungs-, Patch- oder Carrieränderung mit Serviceauswirkung.
- **BCM-Handoff:** Single Points of Failure, redundante Wege, Wiederanlauf und Standortausfall.
- **Incident-Handoff:** Manipulationsverdacht, unbekanntes Gerät, unerklärte Verbindung, Kabelschaden oder Sabotageverdacht.
- **Lieferanten-Handoff:** Installationspartner, Carrier, Wartungsdienstleister, Abnahme und Dokumentationspflichten.
- **Management-Handoff:** baulicher Schutzbedarf, Redundanzinvestition, nicht akzeptiertes Restrisiko oder dauerhafte Provisorien.
- **Audit-/Evidence-Handoff:** veraltete Pläne, fehlende Abnahmen oder unklare Change-Nachweise.

## Typische Fehler

- Patchfelder sind physisch offen, obwohl sie kritische Netzsegmente verbinden.
- Kabeldokumentation wird beim Neubau erstellt und danach nie aktualisiert.
- Temporäre Kabel werden zum Dauerzustand.
- Facility beauftragt Umbauten, ohne IT- und Service Owner einzubeziehen.
- Redundante Leitungen verlaufen durch denselben Schacht und teilen denselben Ausfallpunkt.
- Unbekannte aktive Ports bleiben aus Bequemlichkeit aktiv.
- Detaillierte Netz- und Kabelpläne werden zu breit geteilt oder ungeschützt abgelegt.

## Fiktives Mini-Beispiel

Ein fiktiver Standort erweitert eine Bürofläche. Beim Review entdeckt der Netzwerk Owner mehrere aktive Dosen in einem öffentlich zugänglichen Besprechungsbereich und ein temporäres Kabel zu einem Drucker. Die aktiven Ports werden geprüft, nicht benötigte Ports deaktiviert und das temporäre Kabel durch eine dokumentierte Festverkabelung ersetzt. Facility ergänzt den Umbauprozess um einen IT-Prüfpunkt vor Abnahme.

Evidenz:

- Standortreview mit gefundenen Ports,
- Änderungstickets zur Deaktivierung und Neuverkabelung,
- aktualisierte Portdokumentation,
- Abnahmeprotokoll nach Verkabelungsarbeit,
- ergänzter IT-Prüfpunkt im Umbauprozess.
