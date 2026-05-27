
# A.7.13 — Instandhaltung von Geräten

## Zweck

Instandhaltung sorgt dafür, dass Geräte im Scope zuverlässig, sicher und nachvollziehbar gewartet werden, ohne dabei Informationen, Konfigurationen oder Betriebsumgebungen unnötig offenzulegen. Gemeint sind nicht nur Reparaturen, sondern die gesteuerte Routine rund um Wartungsbedarf, Dienstleisterzugang, Ersatzteile, Protokollierung, Rückgabe in den Betrieb und offene Restrisiken.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Wartungsroutine für Geräte mit Informationssicherheitsbezug. Wartung wird geplant, autorisiert, begleitet, dokumentiert und nachbereitet; besondere Risiken durch externe Techniker, ausgetauschte Komponenten, Datenträger, Remote-Wartung oder ungeplante Reparaturen werden sichtbar entschieden.

## Typische Risiken

- Wenn Geräte ungeplant oder informell gewartet werden, können Konfigurationen verändert, Schutzmaßnahmen deaktiviert oder Daten offengelegt werden.
- Wenn externe Wartungspersonen unbeaufsichtigt Zugriff auf Geräte oder Räume erhalten, entstehen unklare Verantwortlichkeit und Missbrauchsmöglichkeiten.
- Wenn defekte Komponenten mit Datenträgern oder Speicher ausgebaut werden, können Informationen außerhalb der Organisation landen.
- Wenn Wartungsfenster nicht mit Betrieb und Change Management abgestimmt sind, können kritische Services ausfallen.
- Wenn Wartungsnachweise fehlen, bleiben Abweichungen, Ausnahmen und wiederkehrende Defekte unsichtbar.

## Trigger

- geplanter Wartungstermin, Herstellervorgabe oder Servicevertrag.
- Störung, Defekt, Sicherheitsereignis oder auffälliges Geräteverhalten.
- Standortwechsel, Geräteumzug, Ersatzbeschaffung oder Außerbetriebnahme.
- externe Wartung vor Ort oder Remote-Zugriff durch Hersteller, Dienstleister oder Managed Service.
- Änderung des Schutzbedarfs, neue Risikobewertung oder Auditfinding.
- wiederkehrender Review von kritischen Geräten, Wartungsverträgen und offenen Reparaturen.

## Rollen und Verantwortung

- **Asset Owner / Geräte Owner:** legt Kritikalität, Schutzbedarf und Freigabe für Wartung fest.
- **IT-/Facility-Betrieb:** koordiniert Termin, Zugriff, Begleitung, technische Umsetzung und Rücknahme in den Betrieb.
- **ISMS-Owner / Security-Rolle:** definiert Mindestanforderungen, Ausnahmebehandlung und Evidenzlogik.
- **Dienstleister-/Lieferantenmanagement:** prüft Vertrag, Leistungsumfang, Ansprechpartner und Eskalationswege.
- **Datenschutz / Legal:** prüft personenbezogene Daten, Vertragsfragen, Remote-Zugriff oder Datenabflussrisiken.
- **Management:** entscheidet bei Ressourcenmangel, kritischen Ausnahmen oder nicht tragbaren Restrisiken.

## Implementierung

### Minimalstart

Ziel: Wartung kritischer Geräte kontrolliert und nachweisbar machen.

1. Kritische Geräte im ISMS-Scope werden mit Owner, Standort und Wartungsverantwortung erfasst.
2. Wartung erfolgt nur nach Ticket, Auftrag oder dokumentierter Freigabe.
3. Externe Wartung wird begleitet oder technisch begrenzt; Remote-Zugriff wird zeitlich und sachlich eingeschränkt.
4. Ausgebaute Komponenten mit möglichem Informationsgehalt werden gesondert behandelt.
5. Nach Wartung wird geprüft, ob Gerät, Schutzmaßnahmen und Konfiguration wieder betriebsfähig sind.
6. Abweichungen und nicht abgeschlossene Reparaturen werden mit Wiedervorlage dokumentiert.

Minimaler Nachweis:

- Geräteliste mit Owner und Kritikalität,
- Wartungsticket oder Auftrag,
- Nachweis zu Freigabe und Durchführung,
- Rücknahme-/Funktionsprüfung,
- Ausnahme- oder Abweichungsvermerk.

### Solide Praxis

Ziel: Wartung wird mit Betrieb, Lieferantensteuerung und Risikomanagement verbunden.

1. Geräte werden nach Kritikalität, Standort, Datenbezug und Wartungsmodell klassifiziert.
2. Wartungsfenster werden mit Change Management, Service Ownern und Betriebszeiten abgestimmt.
3. Externe Zugriffe werden über Besucher-, Zutritts-, Remote-Access- oder Dienstleisterprozesse gesteuert.
4. Datenträger, Speicherbausteine und ersetzte Komponenten erhalten klare Behandlung: Rückgabe, Löschung, Vernichtung oder Verbleib.
5. Wiederkehrende Defekte führen zu Ursachenanalyse, Ersatzplanung oder Risikoentscheidung.
6. Wartungsverträge, Kontaktwege und Eskalationen werden regelmäßig überprüft.

Starke Evidenz:

- klassifiziertes Geräte-/Assetregister,
- Wartungsplan und Wartungsprotokolle,
- Change- oder Service-Tickets,
- Nachweis über Begleitung oder Begrenzung externer Zugriffe,
- Komponentennachweis bei Austausch,
- Maßnahmenlog für Abweichungen und wiederkehrende Fehler.

### Fortgeschritten

Ziel: Wartung wird proaktiv gesteuert und in Resilienz, Monitoring und Lieferantenmanagement integriert.

1. Kritische Geräte liefern Zustands-, Garantie-, Patch- oder Wartungsindikatoren in ein zentrales Betriebsbild.
2. Wartungsereignisse werden mit Konfigurationsmanagement, Schwachstellenmanagement und Ersatzteilstrategie verknüpft.
3. Remote-Wartung nutzt freigegebene Zugangswege, Protokollierung und zeitlich begrenzte Freischaltung.
4. Kritische Wartungsabhängigkeiten fließen in BCM, Notfallplanung und Management Review ein.
5. Lieferantenleistung wird anhand Reaktionszeit, Qualität, Sicherheitsvorgaben und offener Risiken bewertet.
6. Kennzahlen zeigen überfällige Wartungen, ungeplante Reparaturen, wiederkehrende Defekte und Ausnahmen.

## Ablauf als Routine

1. **Wartungsbedarf entsteht:** Plantermin, Störung, Herstellerhinweis, Monitoring oder Review.
2. **Scope und Kritikalität prüfen:** Gerät, Standort, Datenbezug, Serviceauswirkung und Owner bestimmen.
3. **Freigabe und Termin klären:** Wartungsart, Zugriff, Begleitung, Wartungsfenster und Dienstleister festlegen.
4. **Durchführen:** Wartung kontrolliert umsetzen, Änderungen und Komponentenwechsel dokumentieren.
5. **Rücknahme prüfen:** Funktion, Schutzmaßnahmen, Konfiguration und Betriebsfreigabe kontrollieren.
6. **Evidenz ablegen:** Ticket, Protokoll, Abweichung, Komponentennachweis und offene Punkte sichern.
7. **Nachverfolgen:** Defekte, Ausnahmen, wiederkehrende Muster oder Lieferantenprobleme behandeln.
8. **Eskalieren:** kritische Ausfälle, Datenrisiken oder nicht finanzierte Ersatzbedarfe ins Management geben.

## Entscheidungen

- Welche Geräte gelten als kritisch und brauchen gesteuerte Wartung?
- Welche Wartungsarten dürfen intern, extern, remote oder nur begleitet erfolgen?
- Wie werden ausgebaute Komponenten mit möglichem Informationsgehalt behandelt?
- Welche Wartungsfenster sind mit Service- oder BCM-Anforderungen vereinbar?
- Wann ist Reparatur nicht mehr angemessen und Ersatz erforderlich?
- Wer darf Ausnahmen akzeptieren und wie lange?

## Evidenz

### Starke Evidenz

- aktuelles Assetregister mit Owner, Standort und Kritikalität,
- freigegebene Wartungsaufträge oder Tickets,
- Protokolle mit durchgeführten Arbeiten und Abweichungen,
- Nachweise zu externem Zugriff, Begleitung oder Remote-Freigabe,
- Rücknahmeprüfung nach Wartung,
- Komponenten- oder Datenträgernachweis,
- Managemententscheidung bei kritischen Ausnahmen oder Ersatzbedarf.

### Schwache Evidenz

- allgemeiner Wartungsvertrag ohne Geräte- und Ownerbezug,
- einzelne Rechnungen ohne Sicherheits- oder Rücknahmeprüfung,
- informelle E-Mail-Absprachen ohne Status und Abweichungen,
- Assetliste ohne Wartungshistorie,
- Aussage „macht der Dienstleister“ ohne Leistungsnachweis.

### Evidenzlücken

- kritische Geräte ohne Owner oder Wartungsplan,
- externe Wartung ohne Zutritts-, Zugriffs- oder Begleitnachweis,
- ausgebaute Komponenten ohne Verbleibsnachweis,
- Wartung ändert Konfiguration ohne Review,
- offene Defekte ohne Risikoentscheidung.

## Wirksamkeitsprüfung

Prüffragen:

- Sind kritische Geräte und deren Wartungsverantwortliche bekannt?
- Kann für eine Stichprobe nachvollzogen werden, wann und durch wen Wartung erfolgte?
- Werden externe und Remote-Wartungen kontrolliert und dokumentiert?
- Werden Datenträger oder speicherfähige Komponenten sicher behandelt?
- Führen Wartungsabweichungen zu Maßnahmen, Ersatzplanung oder Managemententscheidung?
- Sind Wartungsfenster mit Betriebs- und Notfallanforderungen abgestimmt?

Mögliche Kennzahlen:

- überfällige Wartungen kritischer Geräte,
- ungeplante Reparaturen je Gerätekategorie,
- offene Wartungsabweichungen,
- externe Wartungen ohne vollständigen Nachweis,
- wiederkehrende Defekte,
- kritische Ersatzbedarfe ohne Entscheidung.

## BSIG-/NIS2-Anschluss

Geräteinstandhaltung ist anschlussfähig an NIS2-orientierte Themen wie Betriebsstabilität, Resilienz, physische Sicherheit, Lieferantensteuerung, Zugriffsschutz und Risikomanagement für kritische Assets. Der konkrete Bezug sollte im Anforderungsregister, im Assetregister und bei kritischen Wartungsabhängigkeiten im Management Review geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung und keine verbindliche Prüfung von Anwendbarkeit oder Nachweispflichten.

## Grenzen

- Dieses Artefakt ist kein technisches Wartungshandbuch und keine Herstellervorgabe.
- Es ersetzt keine Vertrags-, Datenschutz- oder Arbeitsschutzprüfung.
- Es gibt keine Aussage zu Zertifizierungsfähigkeit oder gesetzlicher Erfüllung.
- Es enthält keine lizenzpflichtigen Normtexte und keine vertraulichen Gerätedetails.
- Es genügt nicht als Nachweis, wenn Wartung tatsächlich ungesteuert erfolgt.

## Handoffs

- **Facility-/IT-Betrieb-Handoff:** Planung, Zutritt, Wartungsfenster, Rücknahme in den Betrieb.
- **Lieferanten-Handoff:** externe Techniker, Hersteller, Managed Service, Service-Level-Probleme.
- **Change-Handoff:** Wartung verändert Konfiguration, Firmware, Netzanschluss oder Serviceverfügbarkeit.
- **Datenschutz-/Legal-Handoff:** personenbezogene Daten, Remote-Zugriff, Vertrags- oder Haftungsfragen.
- **BCM-Handoff:** Wartung oder Defekt betrifft kritische Services oder Notfallausstattung.
- **Management-Handoff:** Ersatzinvestition, dauerhafte Ausnahme, nicht tragbares Restrisiko.
- **Audit-/Evidence-Handoff:** fehlende Nachweise zu Wartung, Zugriff oder Komponentenverbleib.

## Typische Fehler

- Wartung wird als rein technisches Thema ohne Owner und Schutzbedarf behandelt.
- Externe Wartung erhält pauschalen Zugang zu Räumen oder Geräten.
- Ausgebaute Komponenten werden wie normales Ersatzmaterial behandelt.
- Nach Wartung wird nicht geprüft, ob Schutzmaßnahmen wieder aktiv sind.
- Kritische Geräte haben Wartungsverträge, aber keine interne Reviewroutine.
- Wiederkehrende Defekte werden repariert, aber nicht als Risiko oder Ersatzbedarf eskaliert.

## Fiktives Mini-Beispiel

Ein fiktiver Produktionsstandort lässt ein Netzwerkgerät warten, das die Verbindung zu einem Lagerbereich bereitstellt. Der IT-Owner erstellt ein Ticket, stimmt ein Wartungsfenster mit dem Service Owner ab und begleitet den externen Techniker. Nach dem Austausch eines Speichermoduls wird der Verbleib dokumentiert. Die Rücknahmeprüfung zeigt eine abweichende Konfiguration, die korrigiert und im Ticket nachgehalten wird. Im nächsten Review wird entschieden, ähnliche Geräte in die Ersatzteilplanung aufzunehmen.

Evidenz:

- Wartungsticket mit Freigabe,
- Begleit- und Zugriffsvermerk,
- Komponentennachweis,
- Rücknahmeprüfung,
- Korrekturmaßnahme,
- Reviewentscheidung zur Ersatzteilplanung.
