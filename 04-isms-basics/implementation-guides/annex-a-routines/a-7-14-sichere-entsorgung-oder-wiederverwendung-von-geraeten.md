
# A.7.14 — Sichere Entsorgung oder Wiederverwendung von Geräten

## Zweck

Sichere Entsorgung oder Wiederverwendung verhindert, dass Informationen über alte, defekte, zurückgegebene oder neu zugewiesene Geräte abfließen. Der Kern ist eine kontrollierte Übergaberoutine: Gerät identifizieren, Daten- und Schutzbedarf klären, Löschung oder Vernichtung auslösen, Ergebnis prüfen und Verbleib nachweisen.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Routine für Geräte, Datenträger und speicherfähige Komponenten, die entsorgt, verkauft, repariert, zurückgegeben, gespendet oder intern wiederverwendet werden. Niemand verlässt sich auf Annahmen wie „war bestimmt leer“, sondern auf Owner, Freigabe, Lösch-/Vernichtungsnachweis und Stichproben.

## Typische Risiken

- Wenn Geräte mit lokalen Daten ungeprüft weitergegeben werden, können vertrauliche Informationen offengelegt werden.
- Wenn Datenträger in defekten Geräten übersehen werden, verlassen Informationen unkontrolliert die Organisation.
- Wenn Rückläufer aus Homeoffice, Leasing oder Dienstleisterbetrieb nicht erfasst werden, fehlt der Verbleibsnachweis.
- Wenn Löschung nicht validiert wird, besteht Scheinsicherheit durch unvollständige oder ungeeignete Verfahren.
- Wenn Entsorgungsdienstleister nicht gesteuert werden, bleiben Kette, Verantwortlichkeit und Nachweisqualität unklar.

## Trigger

- Geräteausmusterung, Leasingrückgabe, Verkauf, Spende oder Verschrottung.
- interne Wiederverwendung, Neuinstallation, Rollenwechsel oder Rückgabe aus Projekt/Homeoffice.
- Defekt, Reparatur, Komponententausch oder Garantiefall mit Gerätetransport.
- Austritt von Beschäftigten oder Ende eines Dienstleistereinsatzes.
- Änderung der Datenklasse, Auditfinding, Sicherheitsereignis oder Verdacht auf Datenabfluss.
- turnusmäßiger Review von Lager, Altgeräten, Rückläufern und Entsorgungsnachweisen.

## Rollen und Verantwortung

- **Asset Owner / Geräte Owner:** entscheidet über Ausmusterung, Wiederverwendung und Schutzbedarf.
- **IT-Betrieb / Workplace-Team:** führt Rücknahme, Inventarprüfung, Löschung, Neuaufsetzung oder Übergabe aus.
- **Facility / Lager / Einkauf:** steuert physische Lagerung, Entsorgung, Leasingrückgabe oder Weitergabe.
- **ISMS-Owner / Security-Rolle:** definiert Mindestlogik, Stichproben, Ausnahmebehandlung und Evidenzanforderungen.
- **Datenschutz / Legal:** prüft personenbezogene Daten, Vertrags- und Nachweisanforderungen sowie Dienstleisterfragen.
- **Management:** entscheidet bei Kosten, Ausnahmen, hohem Restrisiko oder fehlender Entsorgungsfähigkeit.

## Implementierung

### Minimalstart

Ziel: Kein Gerät verlässt den Scope ohne dokumentierte Datenentscheidung.

1. Rücknahme- und Ausmusterungsfälle werden in einem Ticket oder Register erfasst.
2. Geräte werden identifiziert: Typ, Seriennummer/Asset-ID, Owner, letzter Nutzer oder Einsatzbereich.
3. Es wird geprüft, ob Datenträger, Speicher, SIM-/Speicherkarten oder Konfigurationsdaten vorhanden sein können.
4. Löschung, Neuaufsetzung oder Vernichtung wird dokumentiert; bei Unsicherheit wird Vernichtung oder gesonderte Freigabe gewählt.
5. Wiederverwendung erfolgt erst nach Rücksetzung und Freigabe.
6. Externe Entsorgung oder Rückgabe erhält einen Übergabe- und Ergebnisnachweis.

Minimaler Nachweis:

- Rücknahme-/Ausmusterungsticket,
- Asset-ID oder Seriennummer,
- Lösch-, Neuinstallations- oder Vernichtungsnachweis,
- Übergabenachweis an Entsorger/Leasinggeber,
- Ausnahmeentscheidung bei fehlendem Nachweis.

### Solide Praxis

Ziel: Entsorgung und Wiederverwendung werden als wiederholbarer Asset-Lifecycle-Prozess betrieben.

1. Gerätekategorien werden nach Daten- und Speicherrisiko unterschieden: Clients, Smartphones, Server, Netzwerkgeräte, Drucker, Wechseldatenträger, IoT/OT-Komponenten.
2. Freigegebene Verfahren für Löschung, Zurücksetzen, Kryptolöschung oder Vernichtung sind je Kategorie beschrieben.
3. Rückläufer werden bis zur Bearbeitung geschützt gelagert und gegen unbefugte Entnahme gesichert.
4. Entsorgungsdienstleister und Leasingprozesse liefern nachvollziehbare Nachweise.
5. Stichproben prüfen, ob Löschung, Inventarstatus und Verbleib übereinstimmen.
6. Fehlende Geräte oder Nachweise lösen Incident-, Risiko- oder Managementprüfung aus.

Starke Evidenz:

- Asset-Lifecycle-Register,
- Gerätekategorien mit Verfahren,
- Lösch-/Vernichtungsprotokolle,
- geschützte Lager- oder Übergabenachweise,
- Stichprobenergebnisse,
- Maßnahmenlog bei Abweichungen.

### Fortgeschritten

Ziel: Geräteabgänge sind in Identitäts-, Asset-, Endpoint- und Lieferantenprozesse integriert.

1. Assetmanagement, Endpoint-Management, HR-/Leaver-Prozess und Beschaffung liefern Abgangs- und Rückgabeereignisse.
2. Verschlüsselungsstatus, Gerätemanagementstatus und Remote-Wipe-Ergebnisse werden bei Rücknahme berücksichtigt.
3. Entsorgungsdienstleister werden anhand Nachweisqualität, Kette, Reaktionszeit und Abweichungen bewertet.
4. Lagerbestände, Altgeräte und nicht zuordenbare Geräte werden regelmäßig automatisch oder halbautomatisch abgeglichen.
5. Kennzahlen zeigen offene Rückläufer, Entsorgungsdauer, fehlende Nachweise und Abweichungsquote.
6. Wiederverwendung wird mit Standard-Builds, Hardening und Rollenfreigabe verknüpft.

## Ablauf als Routine

1. **Abgang oder Wiederverwendung wird ausgelöst:** Rückgabe, Defekt, Austritt, Leasingende, Neuverteilung oder Entsorgung.
2. **Gerät identifizieren:** Asset-ID, Seriennummer, Owner, letzter Einsatz, mögliche Datenarten.
3. **Datenrisiko bewerten:** lokale Daten, Konfiguration, Schlüssel, Tokens, Datenträger oder Speichermedien prüfen.
4. **Behandlung wählen:** sichere Löschung, Neuaufsetzung, Kryptolöschung, Datenträgerausbau, Vernichtung oder Rückgabeweg.
5. **Durchführen und prüfen:** Ergebnis dokumentieren und bei Stichprobe validieren.
6. **Verbleib festhalten:** Lager, Wiederverwendung, Entsorgung, Leasingrückgabe oder Dienstleisterübergabe.
7. **Abweichungen behandeln:** fehlendes Gerät, fehlender Nachweis, nicht löschbarer Datenträger oder Verdacht auf Datenabfluss eskalieren.
8. **Verbessern:** Muster in Rückgabeprozess, Beschaffung, Gerätemanagement oder Entsorgersteuerung zurückspielen.

## Entscheidungen

- Welche Gerätekategorien brauchen Löschung, Vernichtung oder gesonderte Prüfung?
- Wann reicht Neuaufsetzen, wann ist physische Vernichtung erforderlich?
- Wer darf Geräte zur Wiederverwendung freigeben?
- Wie werden nicht auffindbare Geräte oder fehlende Nachweise behandelt?
- Welche Entsorgungs- oder Leasingnachweise sind für interne Steuerung belastbar?
- Welche Kosten- und Nachhaltigkeitsziele stehen im Zielkonflikt mit Schutzbedarf?

## Evidenz

### Starke Evidenz

- aktuelles Assetregister mit Abgangsstatus,
- Rücknahme- und Ausmusterungstickets,
- Lösch-, Wipe-, Neuinstallations- oder Vernichtungsprotokolle,
- Übergabenachweise mit Assetbezug,
- Stichprobenprotokolle zur Wirksamkeit,
- Ausnahme- oder Risikoentscheidungen bei fehlenden Nachweisen,
- Managemententscheidung bei systematischen Rückgabe- oder Entsorgungsproblemen.

### Schwache Evidenz

- pauschale Entsorgerbescheinigung ohne Assetbezug,
- Excel-Liste ohne Lösch- oder Übergabenachweis,
- Aussage „Geräte werden immer neu installiert“ ohne Prüfung,
- Rechnung für Entsorgung ohne Kette oder Ergebnis,
- alte Richtlinie ohne aktuelle Rückläufer.

### Evidenzlücken

- Geräte verlassen Lager ohne dokumentierte Datenbehandlung,
- Rückläufer aus Homeoffice oder Dienstleistereinsatz fehlen,
- Datenträger in Druckern, Netzwerkgeräten oder Servern werden übersehen,
- Entsorgungsdienstleister liefert keine verwertbaren Nachweise,
- Wiederverwendung erfolgt ohne Standard-Build oder Freigabe.

## Wirksamkeitsprüfung

Prüffragen:

- Kann für eine Stichprobe ausgemusterter Geräte der Verbleib nachvollzogen werden?
- Gibt es Nachweise, dass Datenbehandlung vor Weitergabe oder Entsorgung erfolgte?
- Sind Gerätekategorien mit verstecktem Speicher berücksichtigt?
- Werden fehlende Geräte, fehlende Nachweise und Löschfehler eskaliert?
- Ist die Wiederverwendung mit sicherer Neuaufsetzung und Freigabe verbunden?
- Werden Entsorger- oder Leasingnachweise regelmäßig bewertet?

Mögliche Kennzahlen:

- offene Rückläufer und überfällige Rückgaben,
- Geräte mit fehlendem Lösch-/Vernichtungsnachweis,
- Dauer von Rücknahme bis finalem Verbleib,
- Abweichungen je Gerätekategorie,
- Stichprobenfehlerquote,
- ungeklärte Altgeräte im Lager.

## BSIG-/NIS2-Anschluss

Sichere Entsorgung und Wiederverwendung sind anschlussfähig an NIS2-orientierte Themen wie Risikomanagement, Schutz von Informationen, Cyberhygiene, Lieferantensteuerung und sichere Betriebsprozesse. Der konkrete Bezug sollte über Asset-Lifecycle, Datenklassifizierung, Dienstleistersteuerung und Anforderungsregister geprüft werden.

Dieses Artefakt ersetzt keine rechtliche, datenschutzrechtliche oder entsorgungsrechtliche Bewertung.

## Grenzen

- Dieses Artefakt ist keine technische Löschanleitung und keine Produktempfehlung.
- Es ersetzt keine Datenschutz-, Vertrags-, Umwelt- oder Entsorgungsprüfung.
- Es trifft keine verbindliche Aussage zu gesetzlichen Pflichten oder Zertifizierungsfähigkeit.
- Öffentliche Beispiele enthalten keine echten Geräte-, Personen- oder Kundendaten.
- Löschbehauptungen ohne Nachweis gelten nicht als wirksame Routine.

## Handoffs

- **HR-/Leaver-Handoff:** Rückgabe von Geräten bei Austritt, Rollenwechsel oder längerer Abwesenheit.
- **IT-/Endpoint-Handoff:** Remote Wipe, Neuinstallation, Verschlüsselungsstatus, Standard-Build.
- **Facility-/Lager-Handoff:** gesicherte Zwischenlagerung, Abholung, Übergabe und Inventarabgleich.
- **Einkauf-/Lieferanten-Handoff:** Leasingrückgabe, Entsorger, Dienstleistergerät, Nachweisqualität.
- **Datenschutz-/Legal-Handoff:** personenbezogene Daten, Vertragsfragen, Datenabflussverdacht oder Auftragsverarbeitung.
- **Incident-Handoff:** verlorenes Gerät, fehlender Datenträger, ungeklärter Verbleib oder Verdacht auf Offenlegung.
- **Management-Handoff:** systematische Rückgabelücken, Kostenkonflikt, fehlende Entsorgungsfähigkeit.

## Typische Fehler

- Entsorgung wird erst am Ende betrachtet, nicht als Teil des Asset-Lifecycle.
- Nur Laptops werden berücksichtigt; Drucker, Netzwerkgeräte oder mobile Datenträger fehlen.
- Pauschale Entsorgungszertifikate werden akzeptiert, obwohl kein Assetbezug besteht.
- Wiederverwendung erfolgt nach „Zurücksetzen“ ohne Prüfung des Ergebnisses.
- Altgeräte lagern ungesichert, weil Entsorgungskosten oder Zuständigkeit ungeklärt sind.
- Fehlende Rückläufer werden administrativ ausgebucht statt als Risiko geprüft.

## Fiktives Mini-Beispiel

Ein fiktives Beratungsunternehmen ersetzt zwanzig Notebooks. Das Workplace-Team erfasst jedes Gerät per Asset-ID, prüft Verschlüsselungs- und Managementstatus und führt eine dokumentierte Neuinstallation durch. Drei Geräte lassen sich wegen Defekt nicht zuverlässig löschen; die Datenträger werden ausgebaut und vernichtet. Der Entsorger bestätigt die Abholung der Restgeräte mit Assetliste. Bei einer Stichprobe fehlt ein Rückläufer aus dem Homeoffice; HR und IT lösen eine Nachverfolgung aus.

Evidenz:

- Assetliste mit Abgangsstatus,
- Neuinstallations-/Wipe-Nachweise,
- Vernichtungsnachweis für Datenträger,
- Entsorger-Übergabeprotokoll,
- Stichprobenvermerk,
- Nachverfolgungsticket für fehlenden Rückläufer.
