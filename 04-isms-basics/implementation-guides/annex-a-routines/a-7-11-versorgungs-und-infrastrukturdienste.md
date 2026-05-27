
# A.7.11 — Versorgungs- und Infrastrukturdienste

## Zweck

Versorgungs- und Infrastrukturdienste wie Strom, Kühlung, Netzwerk-/Carrier-Anbindung, Wasser, Brandschutz, Gebäudeleittechnik, Zutrittstechnik oder externe Rechenzentrumsleistungen können die Verfügbarkeit und Sicherheit von Informationsverarbeitung direkt beeinflussen. Diese Routine sorgt dafür, dass solche Abhängigkeiten nicht nur als Facility-Thema behandelt werden, sondern als gesteuerte Betriebs- und Resilienzabhängigkeiten.

Der Kern ist nicht „USV vorhanden“, sondern die Frage: Welche Dienste hängen wovon ab, welche Ausfälle sind tolerierbar, wer überwacht die Abhängigkeit, wer entscheidet über Redundanz, Wartung, Eskalation und Restrisiko?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der kritische Informationsverarbeitungs- und Geschäftsprozesse ihren relevanten Versorgungs- und Infrastrukturabhängigkeiten zugeordnet, geschützt, überwacht, getestet und bei Änderungen reviewed werden.

## Typische Risiken

- Wenn Strom, Kühlung oder Netzwerkversorgung für kritische Systeme nicht bewertet sind, können einzelne Ausfälle ganze Dienste unterbrechen.
- Wenn Wartungen an Gebäude- oder Infrastrukturtechnik nicht mit IT-Betrieb abgestimmt werden, entstehen ungeplante Ausfälle.
- Wenn Redundanzen nur angenommen, aber nicht getestet werden, versagen sie im Ereignisfall.
- Wenn externe Infrastruktur- oder Carrier-Abhängigkeiten unbekannt sind, fehlen Eskalationswege und Wiederanlaufpläne.
- Wenn Umwelt- oder Gebäudetechnikalarme nicht in Betriebsprozesse einfließen, werden kritische Vorzeichen übersehen.
- Wenn Zielkonflikte zwischen Kosten, Nachhaltigkeit, Sicherheit und Verfügbarkeit nicht entschieden werden, bleiben Risiken verdeckt.

## Trigger

- neuer oder geänderter Standort, Technikraum, Rechenzentrum, Carrier, Cloud-/Housing-Dienst oder Produktionsbereich.
- Einführung oder Änderung eines kritischen Services.
- Wartung, Umbau, Renovierung, Stromabschaltung, Kühlungsänderung oder Netzwerkarbeiten.
- Ausfall, Beinaheausfall, Alarm, Incident oder BCM-Übung.
- Lieferantenwechsel, Vertragsänderung oder SLA-Review.
- Risikoanalyse, Business-Impact-Analyse, Asset-Review oder Managementfrage.
- turnusmäßiger Infrastruktur-, Facility- oder Resilienzreview.

## Rollen und Verantwortung

- **Service Owner / Prozess Owner:** bewertet geschäftliche Kritikalität, tolerierbare Ausfallzeiten und Auswirkungen.
- **IT-/Plattform Owner:** benennt technische Abhängigkeiten, Monitoringbedarf, Failover- und Wiederanlaufanforderungen.
- **Facility-/Standort Owner:** verantwortet Strom, Klima, Räume, technische Gebäudeinfrastruktur und Wartungskoordination.
- **BCM-Owner / Krisenrolle:** verbindet Infrastrukturabhängigkeiten mit BIA, Notfallplänen, Übungen und Wiederanlauf.
- **ISMS-Owner / Security-Rolle:** definiert Bewertungslogik, Risiko- und Evidenzanforderungen.
- **Einkauf / Lieferantenmanagement:** steuert Verträge, SLAs, Eskalationskontakte und Dienstleisterreviews.
- **Management:** entscheidet über Redundanz, Investitionen, Restrisiken, Prioritäten und Serviceziele.

## Implementierung

### Minimalstart

Ziel: Kritische Infrastrukturabhängigkeiten sind sichtbar und haben Owner.

1. Die Organisation identifiziert die wichtigsten Services, Standorte oder Technikbereiche im ISMS-Scope.
2. Für diese werden relevante Abhängigkeiten erfasst: Strom, Kühlung, Netzwerk/Internet, Zutritt, Brandschutz, Wasser/Leckage, externe Rechenzentrums- oder Carrierleistungen.
3. Owner und Eskalationskontakte werden dokumentiert.
4. Für kritische Abhängigkeiten wird geprüft, ob Mindestschutz existiert: USV, Klimamonitoring, Ersatzweg, Wartungsvertrag, Alarmierung oder manuelle Ersatzroutine.
5. Wartungen und Änderungen an Infrastruktur werden mit IT/Service Ownern abgestimmt.
6. Offene Lücken werden als Risiko, Maßnahme oder Managemententscheidung geführt.

Minimaler Nachweis:

- Abhängigkeitsliste kritischer Services/Standorte,
- Owner- und Kontaktliste,
- Wartungs- oder Änderungsticket,
- Nachweis vorhandener Schutz- oder Monitoringmaßnahme,
- Risiko-/Maßnahmenlog bei Lücken.

### Solide Praxis

Ziel: Infrastrukturabhängigkeiten werden risikobasiert gesteuert, getestet und reviewed.

1. Services werden mit tolerierbaren Ausfallzeiten, Wiederanlaufpriorität und Infrastrukturabhängigkeiten verbunden.
2. Mindestanforderungen je Kritikalitätsklasse werden festgelegt: Redundanz, USV-Laufzeit, Kühlung, Netzwerkpfad, Alarmierung, Wartungsfenster, Eskalation.
3. Wartungen werden über Change- oder Facility-Prozesse mit Risiko- und Kommunikationsprüfung gesteuert.
4. Monitoring- und Alarmwege werden regelmäßig geprüft.
5. Redundanzen, Notstrom, Failover oder Ersatzverfahren werden angemessen getestet.
6. Dienstleister-SLAs und Eskalationskontakte werden reviewed.
7. Findings fließen in BCM, ISMS-Review und Management Review.

Starke Evidenz:

- Service-Abhängigkeitsmatrix,
- Wartungs- und Change-Nachweise,
- Monitoring- oder Alarmtestprotokolle,
- Testnachweise für USV, Failover, Ersatzleitung oder Wiederanlauf,
- SLA-/Dienstleisterreview,
- Risiko- und Maßnahmenentscheidungen.

### Fortgeschritten

Ziel: Infrastrukturresilienz ist in Architektur, Monitoring, BCM und Managementsteuerung integriert.

1. Infrastrukturabhängigkeiten werden in CMDB, Servicekatalog, BIA und Krisenplänen konsistent gepflegt.
2. Kritische Infrastruktur hat definierte Schwellenwerte, Alarme, Eskalationsketten und Bereitschaftslogik.
3. Kapazität, Lebenszyklus, Wartungszustand und Single Points of Failure werden regelmäßig bewertet.
4. Übungen testen kombinierte Szenarien: Stromausfall, Kühlungsausfall, Carrierstörung, Zutrittssystemausfall oder Standortverlust.
5. Investitionsentscheidungen werden mit Risikoreduktion, Servicekritikalität und BCM-Zielen begründet.
6. Management erhält Kennzahlen zu Abhängigkeiten, Teststatus, offenen Single Points of Failure und überfälligen Infrastrukturmaßnahmen.

## Ablauf als Routine

1. **Service oder Standort betrachten:** kritischer Prozess, Technikraum, Rechenzentrum, Außenstelle oder neuer Dienst.
2. **Abhängigkeiten erfassen:** Strom, Kühlung, Netzwerk, Zutritt, Brand-/Wasserschutz, externe Anbieter und Gebäudeleittechnik.
3. **Kritikalität bewerten:** Auswirkung, tolerierbare Unterbrechung, Wiederanlaufpriorität und Daten-/Servicebezug.
4. **Schutz und Überwachung festlegen:** Redundanz, Monitoring, Wartung, Ersatzverfahren, Eskalation.
5. **Änderungen koordinieren:** Wartung und Umbau mit Change-, Facility- und Servicekalender abstimmen.
6. **Testen und validieren:** Alarm, USV, Failover, Wiederanlauf oder manuelle Ersatzroutine prüfen.
7. **Evidenz sichern:** Matrix, Ticket, Testprotokoll, SLA-Review oder Maßnahmenlog ablegen.
8. **Eskalieren:** nicht akzeptable Single Points of Failure, Investitionsbedarf oder überfällige Maßnahmen ins Management geben.
9. **Lernen:** Ausfälle, Tests und Beinahevorfälle in BCM, Architektur und Betrieb zurückspielen.

## Entscheidungen

- Welche Services und Standorte sind kritisch genug für detaillierte Infrastruktursteuerung?
- Welche Ausfallzeiten und Wiederanlaufziele sind fachlich tragbar?
- Welche Redundanzen sind notwendig, welche Restrisiken werden akzeptiert?
- Wie werden Wartungen priorisiert und kommuniziert?
- Welche Infrastrukturabhängigkeiten müssen getestet werden und wie oft?
- Welche externen Dienstleister oder Carrier brauchen SLA- und Eskalationsreviews?
- Wann wird ein Infrastrukturmangel zum Management- oder BCM-Thema?

## Evidenz

### Starke Evidenz

- aktuelle Abhängigkeitsmatrix für kritische Services,
- dokumentierte Owner, Eskalationskontakte und SLAs,
- Wartungs-/Change-Tickets mit Risiko- und Kommunikationsprüfung,
- Monitoring- und Alarmtestnachweise,
- USV-, Failover-, Notstrom-, Kühlungs- oder Wiederanlauftest,
- Findings mit Maßnahmen und Verantwortlichen,
- Managemententscheidung zu Redundanz, Investition oder Restrisiko.

### Schwache Evidenz

- allgemeine Aussage „Facility ist zuständig“ ohne Servicebezug,
- USV- oder Klimageräteinventar ohne Testnachweis,
- SLA-Dokument ohne Eskalationsübung oder Review,
- Raumplan ohne Abhängigkeit zu kritischen Services,
- Wartungsankündigung ohne Risiko- oder Kommunikationsbewertung.

### Evidenzlücken

- kritische Services ohne Infrastrukturabhängigkeitsanalyse,
- unbekannte Single Points of Failure,
- Alarme ohne Empfänger oder Reaktionsprozess,
- Redundanzen ohne Test,
- Wartungen ohne IT-/Service-Abstimmung,
- externe Abhängigkeiten ohne Ansprechpartner oder SLA-Review.

## Wirksamkeitsprüfung

Prüffragen:

- Sind kritische Services ihren wichtigsten Versorgungs- und Infrastrukturabhängigkeiten zugeordnet?
- Sind Owner und Eskalationskontakte aktuell?
- Werden Wartungen und Änderungen abgestimmt, bevor sie Dienste gefährden?
- Wurden Redundanzen, Alarme oder Ersatzverfahren tatsächlich getestet?
- Sind Single Points of Failure bekannt und entschieden?
- Fließen Ausfälle und Beinaheausfälle in Maßnahmen und BCM-Planung ein?

Mögliche Kennzahlen:

- Anteil kritischer Services mit Abhängigkeitsmatrix,
- offene Single Points of Failure,
- überfällige Infrastrukturtests,
- ungeplante Ausfälle mit Infrastrukturursache,
- Alarmreaktionszeit,
- überfällige SLA- oder Lieferantenreviews,
- offene Maßnahmen aus BCM-Übungen.

## BSIG-/NIS2-Anschluss

Versorgungs- und Infrastrukturdienste sind anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Business Continuity, Incident Handling, Sicherheit der Lieferkette, Betriebssicherheit und Aufrechterhaltung wesentlicher Dienste. Der konkrete Bezug sollte über Anforderungsregister, Risikoanalyse, BIA und Management Review geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung, keine technische Planung durch Fachingenieurinnen oder Fachingenieure und keine verbindliche Aussage zur Anwendbarkeit.

## Grenzen

- Dieses Artefakt ist kein Gebäude-, Elektro-, Klima-, Brandschutz- oder Rechenzentrumsplanungsstandard.
- Es ersetzt keine Arbeitsschutz-, Bau-, Versicherungs- oder Betreiberpflichtenprüfung.
- Es ersetzt keine BCM-Strategie, sondern liefert Anschlussstellen für Infrastrukturabhängigkeiten.
- Es trifft keine Zertifizierungs- oder Konformitätszusage.
- Es enthält keine vertraulichen Standort-, Netz- oder Gebäudepläne.

## Handoffs

- **Facility-Handoff:** Strom, Klima, Gebäudeinfrastruktur, Wartung, Alarmierung, Zutritt und bauliche Maßnahmen.
- **IT-Betrieb-Handoff:** Monitoring, Failover, Wiederanlauf, Plattformabhängigkeiten und Change-Koordination.
- **BCM-/Krisen-Handoff:** BIA, Notfallstrategie, Wiederanlaufprioritäten, Übungen und Krisenentscheidungen.
- **Lieferanten-Handoff:** Carrier, Rechenzentrum, Wartungsdienstleister, SLA, Eskalationskontakte und Vertragsreviews.
- **Incident-Handoff:** Infrastrukturstörung, Beinaheausfall, Alarm oder Sicherheitsverdacht.
- **Management-Handoff:** Redundanzinvestition, nicht tragbarer Single Point of Failure, Ressourcenmangel oder Restrisikoakzeptanz.
- **Audit-/Evidence-Handoff:** fehlende Tests, veraltete Kontakte oder nicht nachvollziehbare Abhängigkeitsdaten.

## Typische Fehler

- Infrastruktur wird als Facility-Thema behandelt und nicht mit kritischen Services verbunden.
- Redundanz wird angenommen, aber nie getestet.
- Wartungen an Strom, Klima oder Netz werden nicht mit Service Ownern abgestimmt.
- Externe Carrier- oder Rechenzentrumsabhängigkeiten fehlen im Risikobild.
- Alarme laufen an Einzelpersonen ohne Vertretung oder Reaktionsroutine.
- USV, Kühlung oder Brandschutz sind vorhanden, aber Wartungs- und Testnachweise fehlen.
- Management sieht Investitionswünsche, aber keine risikobasierten Optionen.

## Fiktives Mini-Beispiel

Ein fiktiver Mittelständler betreibt eine zentrale Warenwirtschaft in einem lokalen Technikraum. Bei der BIA wird klar, dass Stromausfall und Kühlungsausfall denselben Service treffen. Facility und IT erstellen eine Abhängigkeitsmatrix, testen den USV-Alarm und stellen fest, dass die Benachrichtigung nur an eine Einzelperson geht. Die Alarmkette wird erweitert; eine zweite Internetanbindung wird als Managemententscheidung mit Kosten- und Risikobewertung vorbereitet.

Evidenz:

- Service-Abhängigkeitsmatrix,
- USV-Alarmtest,
- aktualisierte Eskalationsliste,
- Maßnahmenticket zur Alarmkette,
- Managementvorlage zur zweiten Anbindung.
