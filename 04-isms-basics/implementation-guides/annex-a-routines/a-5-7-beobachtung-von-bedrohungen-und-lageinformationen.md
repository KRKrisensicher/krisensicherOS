
# A.5.7 — Beobachtung von Bedrohungen und Lageinformationen

## Zweck

Bedrohungs- und Lagebeobachtung sorgt dafür, dass relevante Entwicklungen nicht zufällig wahrgenommen werden. Die Organisation erkennt Warnungen, Angriffsmuster, Schwachstellenlagen, Lieferantenhinweise und branchenspezifische Entwicklungen früh genug, um Risiken, Prioritäten und Maßnahmen anzupassen.

Der Kern ist nicht möglichst viel Threat Intelligence, sondern eine nutzbare Lage-Routine: Welche Informationen werden beobachtet, wie werden sie bewertet, wer handelt und wann wird eskaliert?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine wiederholbare Routine, mit der Bedrohungs- und Lageinformationen aus definierten Quellen gesammelt, gefiltert, bewertet und in konkrete Entscheidungen überführt werden. Relevante Erkenntnisse fließen in Risikoanalyse, Schwachstellenmanagement, Incident Response, Awareness, Lieferantensteuerung, BCM und Management Review.

## Typische Risiken

- Wenn Bedrohungen nicht beobachtet werden, bleiben Angriffsbewegungen, aktive Ausnutzungen oder Branchenvorfälle zu lange unberücksichtigt.
- Wenn zu viele unbewertete Informationen eintreffen, übersehen Teams die wenigen wirklich relevanten Signale.
- Wenn Lageinformationen nicht mit Assets und Services verbunden werden, entstehen keine konkreten Maßnahmen.
- Wenn Warnungen nur technisch betrachtet werden, bleiben Geschäftsrisiken, Lieferkettenfolgen oder Krisenbezug unsichtbar.
- Wenn keine Eskalationslogik existiert, werden kritische Hinweise zu spät an Incident Response oder Management gegeben.
- Wenn Quellen ungeprüft genutzt werden, können Fehlalarme, Gerüchte oder interessengeleitete Informationen Entscheidungen verzerren.

## Trigger

- neue Warnung aus CERT, CSIRT, Hersteller, Dienstleister, Branche, Behörde oder vertrauenswürdiger Fachquelle.
- Hinweis auf aktive Ausnutzung, neue Angriffskampagne, kritische Schwachstelle oder branchenspezifischen Vorfall.
- Sicherheitsereignis, Beinahevorfall, Kunden- oder Lieferantenmeldung.
- neues kritisches Asset, neuer Dienstleister, neue Technologie oder neue Exposition.
- Risiko-Review, Management Review, BCM-Übung oder Incident-Lessons-Learned.
- deutliche Änderung der geopolitischen, regulatorischen, technischen oder branchenspezifischen Lage.
- turnusmäßiger Review der Quellen, Suchprofile und Bewertungslogik.

## Rollen und Verantwortung

- **Security-Rolle / ISMS-Owner:** definiert Quellen, Bewertungslogik, Triage, interne Verteilung und Review.
- **IT-/Plattform Owner:** bewertet technische Betroffenheit, Exposition und Behandlungsbedarf.
- **Asset Owner / Service Owner:** bewertet Geschäftsrelevanz und priorisiert Maßnahmen.
- **Incident-Response-Rolle:** übernimmt Hinweise mit möglicher aktiver Ausnutzung oder Kompromittierung.
- **Lieferantenmanagement:** verfolgt Bedrohungs- und Lagehinweise zu externen Diensten, Produkten oder Managed Services.
- **BCM-/Krisenrolle:** bewertet Lageinformationen mit potenzieller Auswirkung auf Verfügbarkeit, Lieferfähigkeit oder Krisenorganisation.
- **Management:** entscheidet Ressourcen, Priorisierung, Risikoakzeptanz und Kommunikation bei erhöhter Lage.

## Implementierung

### Minimalstart

Ziel: kritische Lagehinweise zuverlässig erkennen und in Maßnahmen übersetzen.

1. Die Organisation legt wenige relevante Quellen fest: nationale Warnkanäle, Herstellerhinweise, Dienstleistermeldungen, Brancheninformationen und interne Incident-Erkenntnisse.
2. Für jede Quelle wird ein Owner und ein Prüfintervall festgelegt.
3. Eingehende Hinweise werden auf Betroffenheit geprüft: Asset, Technologie, Dienstleister, Prozess, Branche, Datenklasse.
4. Relevante Hinweise werden in Ticket, Maßnahmenlog oder Risikoregister erfasst.
5. Kritische Hinweise lösen definierte Handoffs aus: Incident Response, Schwachstellenmanagement, Lieferantenmanagement oder Management.
6. Nicht relevante Hinweise werden kurz begründet verworfen, damit Entscheidungen nachvollziehbar bleiben.

Minimaler Nachweis:

- Quellenliste mit Owner und Prüfintervall,
- Triage-Notiz für relevante Warnungen,
- Betroffenheitsprüfung zu kritischen Assets,
- Maßnahmen- oder Risikoeintrag,
- Eskalationsnachweis bei kritischer Lage.

### Solide Praxis

Ziel: Lagebeobachtung wird risikoorientiert, wiederholbar und entscheidungsfähig.

1. Beobachtungsprofile werden aus dem ISMS-Scope abgeleitet: kritische Technologien, Kernservices, Dienstleister, Datenarten, Branche.
2. Quellen werden nach Verlässlichkeit, Aktualität, Relevanz und Handlungsnutzen bewertet.
3. Hinweise werden klassifiziert: beobachten, prüfen, behandeln, eskalieren, kommunizieren oder schließen.
4. Lageinformationen werden mit Assetinventar, Schwachstellenlog, Risikoregister und Incident-Routine verbunden.
5. Regelmäßige Lage-Reviews verdichten Top-Themen, offene Maßnahmen und mögliche Managemententscheidungen.
6. False Positives und Informationsüberlastung werden aktiv reduziert.
7. Lessons Learned aus Vorfällen passen Suchprofile und Quellen an.

Starke Evidenz:

- Beobachtungsprofil für kritische Services und Technologien,
- Quellenbewertung,
- Triage- und Entscheidungslog,
- Tickets oder Maßnahmen aus Lageinformationen,
- Lage-Review mit Top-Risiken und offenen Entscheidungen,
- Aktualisierung von Risikoanalyse, Awareness oder BCM-Szenarien.

### Fortgeschritten

Ziel: Bedrohungslage wird Teil von Security Operations, Risiko- und Krisensteuerung.

1. Lageinformationen werden halbautomatisiert mit Assetdaten, Schwachstellen, Exposition und Lieferanteninformationen korreliert.
2. Kritische Warnungen erzeugen vordefinierte Playbooks oder Priorisierungsregeln.
3. Die Organisation nutzt Szenarioanalysen, um mögliche Auswirkungen auf Kernservices, Lieferketten und Krisenfähigkeit zu bewerten.
4. Management erhält kurze Lagebriefings mit Entscheidungsbedarf, nicht nur technische Warnlisten.
5. Threat-Intelligence-Feeds, SIEM/SOC, Incident Response und Schwachstellenmanagement sind abgestimmt.
6. Die Qualität der Lagebeobachtung wird anhand von Reaktionszeit, Trefferquote und Maßnahmenwirkung reviewed.

## Ablauf als Routine

1. **Information trifft ein:** Warnmeldung, Advisory, Branchenhinweis, Dienstleistermeldung, Incident-Erkenntnis oder Lageupdate.
2. **Quelle prüfen:** Verlässlichkeit, Aktualität, Kontext und mögliche Relevanz bewerten.
3. **Betroffenheit klären:** Asset, Technologie, Dienstleister, Standort, Prozess oder Datenklasse zuordnen.
4. **Dringlichkeit bestimmen:** aktive Ausnutzung, Exposition, Geschäftsauswirkung und vorhandene Schutzmaßnahmen einordnen.
5. **Handoff auslösen:** Schwachstellenmanagement, Incident Response, Lieferantenmanagement, BCM oder Management einbinden.
6. **Maßnahme oder Entscheidung dokumentieren:** behandeln, beobachten, kommunizieren, Risiko anpassen oder begründet schließen.
7. **Nachverfolgen:** Frist, Owner, Status und Wirksamkeitsprüfung festhalten.
8. **Lagebild aktualisieren:** Muster, Trends und offene Entscheidungen in Reviewformate überführen.

## Entscheidungen

- Welche Quellen sind für Scope, Branche und Technologie wirklich relevant?
- Welche Hinweise müssen sofort triagiert werden, welche reichen für den nächsten Review?
- Wann wird ein Lagehinweis zum Incident-Verdacht?
- Welche Lageinformationen rechtfertigen Ressourcenverschiebung, Change-Freeze, Patch-Priorisierung oder Krisenvorbereitung?
- Wer entscheidet über interne oder externe Kommunikation?
- Wie wird Informationsüberlastung begrenzt, ohne kritische Signale zu verlieren?

## Evidenz

### Starke Evidenz

- definierte Quellen- und Beobachtungsprofile,
- dokumentierte Triage kritischer Lagehinweise,
- Betroffenheitsprüfungen mit Asset- oder Servicebezug,
- Maßnahmen-, Incident- oder Schwachstellentickets,
- Lage-Review mit Entscheidungen und offenen Risiken,
- Anpassungen an Risikoregister, Playbooks, Awareness oder BCM-Szenarien,
- Managemententscheidung bei erhöhter Lage oder Ressourcenbedarf.

### Schwache Evidenz

- ungefilterte Feed- oder Newsletterliste,
- Screenshots einzelner Warnungen ohne Bewertung,
- Tool-Dashboard ohne Owner und Handoff,
- pauschale Aussage „wird durch Dienstleister beobachtet“ ohne Rückmeldung,
- Lagebericht ohne Maßnahmen- oder Entscheidungsbezug.

### Evidenzlücken

- keine definierten Quellen,
- keine Betroffenheitsprüfung,
- keine Verbindung zu Assetinventar oder Risikoregister,
- keine Eskalationskriterien für kritische Warnungen,
- keine Nachverfolgung offener Maßnahmen,
- keine Vertretung für Lagebeobachtung,
- keine Reviewroutine zur Quellenqualität.

## Wirksamkeitsprüfung

Prüffragen:

- Können kritische Lagehinweise einem Owner, Asset und Entscheidungsweg zugeordnet werden?
- Werden aktive Ausnutzungen oder branchenspezifische Warnungen zeitnah bewertet?
- Führt Lagebeobachtung zu konkreten Maßnahmen oder bewusst dokumentiertem Nicht-Handeln?
- Sind Quellen aktuell, relevant und nicht überladen?
- Werden Lieferanten- und SaaS-Hinweise sichtbar verarbeitet?
- Werden Lageinformationen in Risiko-, Incident-, Schwachstellen- und BCM-Routinen zurückgespielt?

Mögliche Kennzahlen:

- Zeit von Warnungseingang bis Triage,
- Anteil kritischer Hinweise mit Betroffenheitsprüfung,
- Anzahl Maßnahmen aus Lageinformationen,
- überfällige Lagehinweise ohne Entscheidung,
- Trefferquote relevanter Quellen,
- Anzahl Lieferantenhinweise mit Rückmeldung.

## BSIG-/NIS2-Anschluss

Bedrohungs- und Lagebeobachtung ist anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Incident Handling, Schwachstellenmanagement, Lieferkettensicherheit, Business Continuity und Managementaufsicht. Für betroffene Organisationen sollte der konkrete Bezug im Anforderungsregister, im Risikoregister und in Incident-/Lageprozessen geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung von Meldepflichten, Betroffenheit oder behördlicher Kommunikation.

## Grenzen

- Dieses Artefakt ist kein SOC-Design und keine Pflicht zu bestimmten kommerziellen Threat-Intelligence-Feeds.
- Es ersetzt keine technische Schwachstellenbewertung oder Incident-Forensik.
- Lageinformationen sind Entscheidungshilfen, keine Gewissheit über tatsächliche Betroffenheit.
- Keine Rechts- oder Datenschutzberatung, keine Zertifizierungszusage.
- Keine vertraulichen Lage- oder Kundendaten in öffentlichen Beispielen.

## Handoffs

- **Schwachstellen-Handoff:** Warnung betrifft konkrete Technologie, CVE, Konfiguration oder Produktversion.
- **Incident-Handoff:** aktive Ausnutzung, Kompromittierungsverdacht oder auffällige Indikatoren.
- **Lieferanten-Handoff:** Hinweis betrifft SaaS, Managed Service, Produktlieferant oder Drittkomponente.
- **BCM-/Krisen-Handoff:** Lage kann Verfügbarkeit, Lieferfähigkeit, Standortbetrieb oder Krisenorganisation betreffen.
- **Management-Handoff:** erhöhter Ressourcenbedarf, Risikoakzeptanz, Prioritätsverschiebung oder Kommunikationsentscheidung.
- **Kommunikations-/Legal-Handoff:** externe Aussagen, Kundeninformation, vertragliche oder rechtliche Fragen.
- **Audit-/Evidence-Handoff:** fehlende Triage, unklare Quellen oder nicht nachverfolgte Hinweise.

## Typische Fehler

- Möglichst viele Feeds werden abonniert, aber niemand triagiert sie.
- Warnungen werden nur technisch gelesen und nicht mit Geschäftsservices verbunden.
- Kritische Hinweise bleiben im Postfach einzelner Personen.
- Lageberichte enthalten viele Informationen, aber keine Entscheidungspunkte.
- Dienstleister werden verantwortlich gemacht, ohne Rückmelde- oder Eskalationsweg.
- Quellen werden nie auf Relevanz oder Fehlalarme geprüft.
- Management wird erst informiert, wenn operative Teams bereits blockiert sind.

## Fiktives Mini-Beispiel

Ein fiktiver Softwaredienstleister erhält eine Warnung zu aktiv ausgenutzten Schwachstellen in einer verbreiteten VPN-Komponente. Die Security-Rolle prüft die Quellenverlässlichkeit, ordnet die Komponente zwei Standorten zu und erstellt Tickets für den Plattform Owner. Weil ein Standort extern erreichbar ist, wird der Hinweis an Incident Response und Management eskaliert. Nach Prüfung und Patch wird das Lage-Log aktualisiert und die Quelle als hochrelevant markiert.

Evidenz:

- Warnhinweis mit Quelle und Datum,
- Betroffenheitsprüfung gegen Assetliste,
- Patch- und Validierungstickets,
- Eskalationsnotiz an Incident Response und Management,
- aktualisiertes Lage- und Quellenreview.
