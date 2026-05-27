
# A.7.5 — Schutz vor physischen und umweltbedingten Gefahren

## Zweck

Physische und umweltbedingte Gefahren können Informationswerte, IT-Betrieb und kritische Prozesse auch ohne Cyberangriff beeinträchtigen: Feuer, Wasser, Hitze, Stromausfall, Staub, Bauarbeiten, Unwetter, Vandalismus oder ungeeignete Lagerung. Diese Routine sorgt dafür, dass solche Gefahren nicht nur allgemein bekannt sind, sondern standort- und assetbezogen bewertet, behandelt und reviewed werden.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der physische und umweltbedingte Gefahren für Standorte, Räume, Systeme, Datenträger und kritische Betriebsprozesse identifiziert, bewertet, behandelt und in BCM-, Facility- und ISMS-Reviews überführt werden.

## Typische Risiken

- Wenn Technikräume nicht gegen Wasser, Hitze oder Stromprobleme betrachtet werden, kann ein lokales Ereignis zentrale Dienste ausfallen lassen.
- Wenn Bauarbeiten, Wartung oder Fremdfirmen nicht sicherheitsseitig bewertet werden, entstehen Schäden, Unterbrechungen oder unbemerkte Exposition.
- Wenn Datenträger, Papierarchive oder Geräte ungeeignet gelagert werden, können Informationen beschädigt, verloren oder offengelegt werden.
- Wenn Umweltgefahren nicht mit Business-Continuity-Anforderungen verbunden sind, fehlen Ersatzverfahren und Prioritäten.
- Wenn Warnungen, Sensoren oder Wartungen nicht reviewed werden, bleiben schleichende Risiken wie Feuchte, Temperatur oder Strominstabilität unsichtbar.

## Trigger

- neuer Standort, Raum, Technikbereich, Archiv, Lager oder Produktionsumgebung.
- Umbau, Bauarbeiten, Wartung, Änderung von Klima-, Strom-, Wasser- oder Brandschutzumgebung.
- neues kritisches System, neuer Prozess oder veränderte Verfügbarkeitsanforderung.
- Störung, Wasserschaden, Brandereignis, Überhitzung, Stromausfall, Unwetter oder Beinaheereignis.
- Versicherungs-, Vermieter-, Facility-, BCM- oder Risikoreview.
- Lieferantenänderung bei Facility, Wartung, Energieversorgung, Rechenzentrum oder Lagerdienst.
- Auditfinding oder Managementfrage zu Standort- und Betriebsresilienz.

## Rollen und Verantwortung

- **Standort-/Facility Owner:** verantwortet Gefahrenaufnahme, bauliche und technische Schutzmaßnahmen, Wartung und Dienstleisterkoordination.
- **Asset Owner / Service Owner:** bewertet Auswirkungen auf Informationen, Systeme, Prozesse und Wiederanlaufprioritäten.
- **BCM-Owner:** verbindet physische Gefahren mit Notfallplanung, Wiederanlauf und Ersatzverfahren.
- **IT-/Plattform Owner:** bewertet Technikräume, Strom, Klima, Backup-Medien, Netzwerk und Betriebsabhängigkeiten.
- **ISMS-Owner / Risikoverantwortliche:** führt Risiken, Maßnahmen, Ausnahmen und Reviews zusammen.
- **Einkauf / Vendor Management:** steuert externe Facility-, Rechenzentrums-, Wartungs- oder Lagerdienstleister.
- **Management:** entscheidet über Investitionen, Restrisiken, Prioritäten und akzeptierte Standortabhängigkeiten.

## Implementierung

### Minimalstart

Ziel: Offensichtliche physische und Umweltgefahren für kritische Bereiche sichtbar und steuerbar machen.

1. Kritische Räume, Technikflächen, Archive, Lager und Arbeitsbereiche im ISMS-Scope werden benannt.
2. Für jeden Bereich werden typische Gefahren grob geprüft: Feuer, Wasser, Hitze/Kälte, Strom, Bauarbeiten, Staub, Zutritt, Lagerung.
3. Vorhandene Schutzmaßnahmen und Abhängigkeiten werden dokumentiert: Melder, Wartung, Klima, USV, Löschmittel, Vermieter, Dienstleister.
4. Offene Lücken werden als Maßnahmen, befristete Ausnahmen oder Managemententscheidungen geführt.
5. Störungen und Beinaheereignisse werden als Lessons Learned in den Review aufgenommen.
6. BCM-Handoff wird ausgelöst, wenn Ausfall eines Bereichs kritische Dienste oder Wiederanlaufziele betrifft.

Minimaler Nachweis:

- Liste kritischer Bereiche mit Owner,
- einfache Gefahren- und Maßnahmenübersicht,
- Wartungs- oder Prüfhinweise,
- Störungs-/Beinaheereignisnotiz,
- Maßnahme oder Risikoentscheidung.

### Solide Praxis

Ziel: Physische und Umweltgefahren werden risikobasiert mit Facility, IT und BCM gesteuert.

1. Gefahren werden pro Standort und Raumtyp systematisch bewertet.
2. Schutzmaßnahmen werden mit Owner, Wartungsintervall, Testlogik und Eskalationsweg geführt.
3. Änderungen an Bau, Strom, Klima, Wasser, Brandschutz oder Lagerung lösen einen Sicherheits- und BCM-Review aus.
4. Kritische Systeme werden mit Verfügbarkeitsanforderungen, Ersatzverfahren und Wiederanlaufprioritäten verbunden.
5. Dienstleister- und Vermieterabhängigkeiten werden dokumentiert und reviewed.
6. Störungen führen zu Ursachenanalyse und Maßnahmenverfolgung.
7. Restrisiken, Investitionsbedarf und nicht lösbare Standortabhängigkeiten werden ins Management Review gegeben.

Starke Evidenz:

- standortbezogene Gefahrenanalyse,
- Maßnahmen- und Wartungsregister,
- Sensor-, Test-, Wartungs- oder Prüfprotokolle,
- Änderungsreview bei Bau oder technischer Infrastruktur,
- Lessons Learned aus Störungen,
- BCM-Verknüpfung für kritische Services,
- Managemententscheidung zu Restrisiken oder Investitionen.

### Fortgeschritten

Ziel: Standortresilienz, Umweltmonitoring und Wiederanlauffähigkeit werden integriert betrieben.

1. Umwelt- und Infrastrukturdaten wie Temperatur, Feuchte, Strom, USV, Leckage oder Alarmstatus werden risikobasiert überwacht.
2. Kritische Standortabhängigkeiten sind mit BIA, BCM-Plänen, Wiederanlaufübungen und Lieferantensteuerung verbunden.
3. Bau- und Wartungsarbeiten werden über Freigabe-, Begleit- und Abnahmeprozesse gesteuert.
4. Szenarien wie Stromausfall, Wassereintritt, Feuer, Hitzeperiode oder Standortverlust werden in Übungen betrachtet.
5. Wiederkehrende Störungen führen zu strukturellen Entscheidungen: Umbau, Verlagerung, Redundanz, Dienstleisterwechsel oder akzeptiertes Restrisiko.
6. Management erhält Kennzahlen und Entscheidungsvorlagen zu Standort- und Infrastrukturresilienz.

## Ablauf als Routine

1. **Gefahr oder Änderung entsteht:** Standort, Raum, Technik, Bau, Wetterlage, Störung oder neuer Service.
2. **Betroffenheit klären:** Welche Informationen, Systeme, Prozesse, Datenträger oder Menschen sind betroffen?
3. **Risiko bewerten:** Eintrittsmöglichkeit, Auswirkung, vorhandene Schutzmaßnahmen und Wiederanlaufabhängigkeit einordnen.
4. **Maßnahmen festlegen:** Vermeidung, Schutz, Monitoring, Wartung, Ersatzverfahren oder Kompensation.
5. **Umsetzen und testen:** Facility, IT, BCM und Dienstleister führen Maßnahmen, Tests oder Wartungen durch.
6. **Evidenz sichern:** Review, Test, Wartung, Störung oder Entscheidung nachvollziehbar dokumentieren.
7. **Abweichungen steuern:** offene Lücke, überfällige Wartung oder nicht tragbares Risiko eskalieren.
8. **Lernen:** Störungen und Beinaheereignisse in Risikoanalyse, Standortplanung und BCM zurückführen.

## Entscheidungen

- Welche Räume, Systeme und Prozesse sind gegenüber physischen oder Umweltgefahren kritisch?
- Welche Gefahren werden akzeptiert, kompensiert oder investiv reduziert?
- Welche Wartungen, Tests oder Sensoren sind für den Schutzbedarf angemessen?
- Wann führt eine Standortlücke zu BCM-Maßnahmen oder Verlagerungsentscheidung?
- Welche Abhängigkeiten von Vermieter, Energieversorgung, Rechenzentrum oder Facility-Dienstleister sind tolerierbar?
- Wer akzeptiert Restrisiken, wenn bauliche Maßnahmen nicht kurzfristig möglich sind?

## Evidenz

### Starke Evidenz

- aktueller Scope kritischer Räume und Assets,
- standort- oder raumbezogene Gefahrenanalyse,
- Maßnahmenregister mit Owner, Frist und Status,
- Wartungs-, Sensor-, Prüf- oder Testprotokolle,
- Änderungsfreigaben bei Bau-/Infrastrukturarbeiten,
- Lessons Learned aus Störungen oder Beinaheereignissen,
- BCM-Verknüpfung und Managemententscheidung bei Restrisiken.

### Schwache Evidenz

- allgemeine Standortbeschreibung ohne Gefahrenbezug,
- Versicherungs- oder Vermieterunterlagen ohne interne Bewertung,
- Wartungsnachweis ohne Zuordnung zu kritischen Bereichen,
- alte Begehung ohne Maßnahmenverfolgung,
- Aussage „Rechenzentrum ist professionell“ ohne Lieferanten- oder Nachweisprüfung.

### Evidenzlücken

- kritische Räume ohne Gefahrenbewertung,
- keine Reaktion auf wiederholte Temperatur-, Strom- oder Feuchteereignisse,
- Bauarbeiten ohne Sicherheits- oder BCM-Review,
- externe Rechenzentrums- oder Lagerabhängigkeit ohne Owner,
- akzeptierte bauliche Lücken ohne Risikoentscheidung.

## Wirksamkeitsprüfung

Prüffragen:

- Sind relevante physische und Umweltgefahren für kritische Bereiche bekannt?
- Werden Schutzmaßnahmen gewartet, getestet und bei Störung nachverfolgt?
- Lösen Bau-, Wartungs- und Standortänderungen einen Review aus?
- Sind kritische Systeme mit Wiederanlauf- und Ersatzlogik verbunden?
- Werden Vermieter- und Dienstleisterabhängigkeiten aktiv gesteuert?
- Gibt es Managemententscheidungen zu nicht kurzfristig behebbaren Restrisiken?

Mögliche Kennzahlen:

- kritische Bereiche mit aktueller Gefahrenbewertung,
- offene Maßnahmen aus Begehungen oder Störungen,
- überfällige Wartungen oder Tests,
- Anzahl relevanter Umweltalarme,
- Zeit bis Behebung kritischer Facility-Störungen,
- BCM-relevante Standortrestrisiken.

## BSIG-/NIS2-Anschluss

Der Schutz vor physischen und umweltbedingten Gefahren ist anschlussfähig an NIS2-orientierte Themen wie Risikomanagement, Business Continuity, Krisenfähigkeit, Schutz kritischer Betriebsumgebungen und Lieferketten-/Dienstleisterabhängigkeiten. Konkrete Anforderungen sollten organisationsspezifisch im Anforderungsregister und in Risiko- sowie BCM-Artefakten geprüft werden.

Dieses Artefakt ersetzt keine rechtliche, bauliche, arbeitsschutzfachliche, versicherungsbezogene oder behördliche Bewertung.

## Grenzen

- Dieses Artefakt ist keine Brandschutz-, Bau-, Elektro- oder Arbeitsschutzberatung.
- Es ersetzt keine technische Planung für Rechenzentren, Gebäude oder Produktionsumgebungen.
- Es gibt keine Sicherheits-, Verfügbarkeits- oder Konformitätsgarantie.
- Es enthält keine ISO-27002-Texte oder Zertifizierungszusage.
- Öffentliche Beispiele bleiben fiktiv und ohne sensible Standortdetails.

## Handoffs

- **Facility-Handoff:** Gebäude, Wartung, Klima, Strom, Wasser, Brandschutz, Bauarbeiten, Vermieter.
- **IT-Handoff:** Technikräume, Netzwerke, Server, Backup-Medien, USV, Monitoring.
- **BCM-Handoff:** Ausfall kritischer Bereiche, Ersatzstandort, Wiederanlauf, Übungen.
- **Einkauf-/Vendor-Handoff:** Rechenzentrum, Lager, Wartung, Energie, Facility-Dienstleister.
- **Management-Handoff:** Investitionen, Standortabhängigkeiten, akzeptierte Restrisiken, Priorisierung.
- **Legal-/Datenschutz-Handoff:** Vertragsfragen, personenbezogene Daten in Störungs-/Zutrittsprotokollen, behördliche Themen.
- **Audit-/Evidence-Handoff:** fehlende Wartungs-, Test-, Störungs- oder Risikoentscheidungsnachweise.

## Typische Fehler

- Umweltgefahren werden nur bei Rechenzentren betrachtet, nicht bei Archiven, Lagern oder Büroflächen.
- Wartungsnachweise liegen vor, aber niemand bewertet ihre Relevanz für kritische Services.
- Bauarbeiten werden als Facility-Thema behandelt und nicht mit IT, ISMS oder BCM abgestimmt.
- Beinaheereignisse werden informell gelöst, aber nicht in Risikoanalyse und Maßnahmenlog übertragen.
- Abhängigkeiten von Vermieter oder Dienstleister werden nicht entscheidungsfähig gemacht.
- Sensoren alarmieren, aber Reaktionswege und Verantwortlichkeiten fehlen.

## Fiktives Mini-Beispiel

Ein fiktiver Fachverlag lagert Vertragsarchive und Backup-Medien in einem Kellerraum. Nach Starkregen entdeckt Facility Feuchtigkeit an einer Wand. ISMS-Owner, Facility und IT bewerten den Raum als ungeeignet für Backup-Medien. Kurzfristig werden die Medien in einen trockenen, abgeschlossenen Raum verlagert; mittelfristig entscheidet das Management über externe Lagerung und bessere Standorttrennung.

Evidenz:

- Störungsnotiz zum Feuchteereignis,
- aktualisierte Gefahrenbewertung des Kellerraums,
- Ticket zur Verlagerung der Medien,
- Risikoentscheidung zur Übergangslösung,
- Managemententscheidung zur künftigen Lagerstrategie.
