
# A.8.21 — Sicherheit von Netzwerkdiensten

## Zweck

Netzwerkdienste wie Internetzugang, Standortvernetzung, DNS, VPN, Proxy, WLAN, Cloud-Konnektivität oder Managed Network Services sind oft Voraussetzung für den Betrieb. Diese Routine sorgt dafür, dass solche Dienste nicht nur beschafft oder technisch aktiviert werden, sondern mit Sicherheitsanforderungen, Verantwortlichkeiten, Nachweisen und Reviewpunkten gesteuert werden.

## Control-Ziel in Repo-Sprache

Die Organisation definiert und betreibt Sicherheitsanforderungen für interne, externe und ausgelagerte Netzwerkdienste. Serviceumfang, Schutzmechanismen, Zuständigkeiten, Monitoring, Änderungswege, Vorfallkommunikation, Nachweise und Ausnahmen sind nachvollziehbar geregelt.

## Typische Risiken

- Wenn Netzwerkdienste ohne Sicherheitsanforderungen beauftragt werden, fehlen später Nachweise, Meldewege oder technische Schutzoptionen.
- Wenn Provider- und Organisationsverantwortung unklar bleiben, werden Incidents, Schwachstellen oder Konfigurationsfehler nicht rechtzeitig behandelt.
- Wenn DNS, VPN, Proxy oder WLAN als reine Infrastruktur betrachtet werden, können Manipulation, Fehlkonfiguration oder Ausfall zentrale Dienste beeinträchtigen.
- Wenn Dienstleisterzugänge nicht geprüft werden, entstehen unkontrollierte Wege in interne Systeme.
- Wenn Leistungs- und Sicherheitskennzahlen fehlen, bemerkt die Organisation Verschlechterungen erst bei Störung oder Angriff.

## Trigger

- neuer Netzwerkdienst, Providerwechsel, Vertragsverlängerung oder Ausschreibung.
- Änderung von Serviceumfang, Standort, Bandbreite, Zugangstechnik, Sicherheitsoptionen oder Betriebsmodell.
- Incident, Störung, Schwachstellenmeldung, Providerhinweis oder Auditfinding.
- neue Cloud-, Remote-Access-, WLAN-, DNS-, Proxy- oder Standortvernetzung.
- geänderte Schutzbedarfe, Business-Continuity-Anforderungen oder Managemententscheidung.
- turnusmäßiger Service- und Sicherheitsreview.

## Rollen und Verantwortung

- **Service Owner:** verantwortet Geschäftsbedarf, Leistungsumfang, Kritikalität und Review des Netzwerkdienstes.
- **Netzwerk-/Plattform Owner:** bewertet technische Sicherheitsanforderungen und betreibt interne Konfigurationen.
- **Einkauf / Lieferantenmanagement:** verankert Anforderungen, Nachweise, Ansprechpartner und Eskalationswege im Lieferantenprozess.
- **Security-Rolle / ISMS-Owner:** definiert Mindestanforderungen, Risiko- und Evidenzlogik.
- **BCM-Verantwortliche:** prüfen Abhängigkeiten, Wiederanlauf, Ausweichwege und kritische Betriebsfolgen.
- **Legal / Datenschutz:** prüfen Vertrags-, Datenschutz- und Kommunikationsfragen, soweit betroffen.
- **Management:** entscheidet bei kritischen Abhängigkeiten, Kosten-/Sicherheitskonflikten oder akzeptierten Restrisiken.

## Implementierung

### Minimalstart

Ziel: kritische Netzwerkdienste mit Owner, Sicherheitsanforderungen und Ansprechpartnern sichtbar machen.

1. Die Organisation listet die wichtigsten Netzwerkdienste im Scope: Internetanbindung, VPN, DNS, WLAN, Proxy, Standortvernetzung, Cloud-Konnektivität oder Managed Services.
2. Für jeden kritischen Dienst werden Owner, Provider, Zweck, Kritikalität und betroffene Standorte oder Services erfasst.
3. Mindestanforderungen werden dokumentiert: Authentisierung, Verschlüsselung, Logging, Verfügbarkeit, Supportweg, Vorfallkontakt und Änderungsprozess.
4. Verträge, Servicebeschreibungen oder Betriebsdokumente werden auf Sicherheits- und Eskalationspunkte geprüft.
5. Offene Lücken werden als Maßnahmen, Ausnahmen oder Managementfragen geführt.

Minimaler Nachweis:

- Netzwerkdiensteregister mit Ownern,
- Servicebeschreibung oder Vertragsreferenz,
- dokumentierte Mindestanforderungen,
- Ansprechpartner- und Eskalationsliste,
- Reviewnotiz mit Lücken und Maßnahmen.

### Solide Praxis

Ziel: Netzwerkdienste werden risikobasiert beschafft, betrieben und reviewed.

1. Sicherheitsanforderungen werden vor Beschaffung oder Änderung geprüft und in Auswahl, Vertrag oder Betriebsvereinbarung übernommen.
2. Kritische Netzwerkdienste erhalten definierte SLAs, Sicherheitskontakte, Wartungsfenster, Meldewege und Nachweisformate.
3. Provider-Changes, Wartungen und Störungen werden in internen Change-, Incident- und BCM-Prozessen gespiegelt.
4. Dienstleisterzugänge werden mit Zugriffskontrolle, Zweck, Laufzeit und Review verbunden.
5. Service Reviews prüfen Störungen, Sicherheitsmeldungen, offene Risiken, Änderungen und Nachweise.
6. Abhängigkeiten fließen in Risikoanalyse, Notfallplanung und Management Review.

Starke Evidenz:

- Anforderungen aus Ausschreibung, Vertrag oder Servicebeschreibung,
- Service-Review-Protokolle mit Sicherheitsanteil,
- Nachweise zu Verfügbarkeit, Störungen, Sicherheitsmeldungen oder Wartungen,
- Tickets zu Provider-Changes und internen Folgeänderungen,
- Risiko- und BCM-Bewertung kritischer Netzwerkdienste,
- dokumentierte Ausnahmen mit Ablaufdatum.

### Fortgeschritten

Ziel: Netzwerkdienste werden als kritische Liefer- und Betriebsabhängigkeiten gesteuert.

1. Serviceinformationen, Providerkontakte, SLAs, Störungen und Sicherheitsereignisse werden zentral auswertbar geführt.
2. Kritische Netzwerkdienste sind in Monitoring, Incident Response, Krisenkommunikation und BCM-Übungen eingebunden.
3. Redundanz, alternative Zugangswege und Abhängigkeiten werden regelmäßig getestet oder plausibilisiert.
4. Sicherheitskennzahlen wie ungeklärte Providerfindings, SLA-Verletzungen, Störungsdauer, ungeprüfte Changes und offene Ausnahmen werden berichtet.
5. Bei besonders kritischen Diensten werden unabhängige Nachweise, technische Tests oder gemeinsame Übungen mit Dienstleistern genutzt.

## Ablauf als Routine

1. **Bedarf oder Änderung entsteht:** neuer Dienst, Vertragsänderung, Providerhinweis, Störung oder Review.
2. **Dienst einordnen:** Zweck, Kritikalität, betroffene Services, Datenflüsse, Standorte und Abhängigkeiten bestimmen.
3. **Anforderungen festlegen:** Sicherheit, Verfügbarkeit, Monitoring, Incident-Kommunikation, Nachweise und Zugriffsschutz definieren.
4. **Lieferanten-/Vertragscheck durchführen:** Verantwortlichkeiten, Ansprechpartner und Eskalationswege klären.
5. **Technisch und organisatorisch umsetzen:** Konfiguration, Monitoring, Kontakte, Betriebsdokumentation und Change-Wege einrichten.
6. **Nachweise erfassen:** Vertrag, Servicebeschreibung, Review, Störung, Change oder Providerbestätigung ablegen.
7. **Reviewen:** Leistung, Sicherheit, Findings, Ausnahmen und Abhängigkeiten regelmäßig prüfen.
8. **Eskalieren:** kritische Lücken, ungeklärte Verantwortlichkeiten oder nicht akzeptable Abhängigkeiten ins Management geben.

## Entscheidungen

- Welche Netzwerkdienste sind kritisch für Geschäft, Sicherheit oder Verfügbarkeit?
- Welche Sicherheitsanforderungen sind vor Beauftragung zwingend, welche risikobasiert?
- Welche Nachweise muss ein Provider regelmäßig liefern?
- Welche Störungen oder Sicherheitsmeldungen lösen Incident-, BCM- oder Management-Handoff aus?
- Welche Abhängigkeiten benötigen Redundanz oder Ausweichverfahren?
- Wer darf Ausnahmen bei Provideranforderungen akzeptieren und wie lange?

## Evidenz

### Starke Evidenz

- aktuelles Netzwerkdiensteregister mit Owner, Provider, Kritikalität und Reviewdatum,
- dokumentierte Sicherheitsanforderungen und Servicebeschreibungen,
- Vertrags- oder Lieferantennachweise zu Zuständigkeiten, Meldewegen und Support,
- Service-Review-Protokolle mit Entscheidungen,
- Incident-/Störungs- und Change-Tickets mit Providerbezug,
- BCM- oder Risikoanalyse kritischer Netzwerkdienste,
- Managemententscheidung bei akzeptierten Abhängigkeiten oder Lücken.

### Schwache Evidenz

- Providervertrag ohne Sicherheitsauswertung,
- technische Produktbeschreibung ohne interne Owner,
- SLA-Werte ohne Review oder Maßnahmen,
- Kontaktliste ohne Test oder Aktualitätsdatum,
- pauschale Aussage „Provider ist verantwortlich“ ohne Verantwortungsmatrix.

### Evidenzlücken

- kritische Dienste ohne Owner oder Eskalationskontakt,
- unklare Trennung zwischen Provider- und Eigenverantwortung,
- keine Nachweise zu Sicherheitsmeldungen oder Störungen,
- Dienstleisterzugänge ohne Zugriffsroutine,
- fehlender BCM-Bezug bei zentralen Netzwerkabhängigkeiten,
- Ausnahmen ohne Laufzeit oder Risikoentscheidung.

## Wirksamkeitsprüfung

Prüffragen:

- Sind alle kritischen Netzwerkdienste mit Owner, Provider und Kritikalität bekannt?
- Sind Sicherheitsanforderungen vor Beschaffung oder Änderung geprüft worden?
- Können Störungen und Sicherheitsmeldungen einem internen Prozess zugeordnet werden?
- Werden Provider-Changes und Dienstleisterzugriffe nachvollziehbar gesteuert?
- Gibt es aktuelle Eskalationskontakte und wurden sie plausibilisiert?
- Sind kritische Abhängigkeiten im Risiko- und BCM-Kontext sichtbar?

Mögliche Kennzahlen:

- Anteil kritischer Netzwerkdienste mit aktuellem Review,
- offene Providerfindings nach Kritikalität,
- SLA-Verletzungen oder wiederholte Störungen,
- ungeklärte Provider-Changes,
- überfällige Ausnahmen,
- kritische Dienste ohne getesteten Eskalationsweg.

## BSIG-/NIS2-Anschluss

Sichere Netzwerkdienste sind anschlussfähig an NIS2-orientierte Themen wie Risikomanagement, Lieferkettensicherheit, Betriebssicherheit, Incident Handling, Business Continuity und sichere Kommunikation. Der konkrete Bezug sollte organisationsspezifisch im Anforderungsregister, Lieferantenmanagement und Management Review geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung von Anwendbarkeit, Vertragsgestaltung oder Nachweispflichten.

## Grenzen

- Dieses Artefakt ist keine Vertragsvorlage und keine Rechtsberatung.
- Es ersetzt keine technische Providerprüfung oder Netzarchitekturprüfung.
- SLAs allein belegen keine Sicherheit oder Wirksamkeit.
- Datenschutzfragen können entstehen, wenn Netzwerkdienste Logs, Nutzerbezug oder Inhaltsdaten verarbeiten.
- Keine Zertifizierungszusage und keine Übernahme lizenzpflichtiger Normtexte.

## Handoffs

- **Einkauf-/Lieferanten-Handoff:** neue Dienste, Vertragsänderungen, Providerwechsel, fehlende Sicherheitsnachweise.
- **Change-Handoff:** technische Umstellung, Wartung, Routing-, DNS-, VPN-, Proxy- oder Cloud-Konnektivitätsänderung.
- **Incident-Handoff:** Provider-Sicherheitsmeldung, Dienststörung mit Sicherheitswirkung, Verdacht auf Missbrauch.
- **BCM-Handoff:** kritische Abhängigkeit, Ausfallrisiko, Redundanzbedarf oder Notfallübung.
- **Datenschutz-/Legal-Handoff:** personenbezogene Logs, Inhaltsfilterung, Vertrags- oder Meldepflichtfragen.
- **Management-Handoff:** Kosten-/Sicherheitskonflikt, nicht erfüllbare Mindestanforderung, akzeptiertes Restrisiko.
- **Audit-/Evidence-Handoff:** fehlende Reviews, unklare Verantwortungsmatrix oder veraltete Nachweise.

## Typische Fehler

- Netzwerkdienste werden als technische Commodity beschafft, ohne Sicherheitsanforderungen zu klären.
- Providerverantwortung wird überschätzt; interne Owner fehlen.
- Eskalationskontakte existieren, werden aber nie getestet oder aktualisiert.
- Störungen werden betrieblich gelöst, aber nicht für Risiko- und BCM-Reviews genutzt.
- Dienstleisterzugänge bleiben außerhalb der Zugriffsroutine.
- Sicherheitsnachweise werden erst im Audit gesucht.
- Redundanz wird angenommen, aber nicht mit Abhängigkeiten und Wiederanlauf geprüft.

## Fiktives Mini-Beispiel

Ein fiktiver Handelsbetrieb wechselt den Internetprovider für zwei Standorte. Der Service Owner erfasst den Dienst im Netzwerkdiensteregister, Einkauf ergänzt Sicherheits- und Eskalationskontakte in der Vertragsakte, der Netzwerk Owner prüft DNS-, Firewall- und Monitoring-Anpassungen. Im ersten Service Review wird eine Lücke sichtbar: Wartungsmeldungen erreichen nur eine Einzelperson. Das Management entscheidet, den Eskalationsweg auf ein Gruppenpostfach und einen Bereitschaftskontakt umzustellen.

Evidenz:

- aktualisiertes Netzwerkdiensteregister,
- Vertrags-/Servicebeschreibung mit Kontakten,
- Change-Tickets für technische Umstellung,
- Service-Review-Protokoll,
- Managemententscheidung zum Eskalationsweg.
