
# A.8.33 — Testinformationen schützen

## Zweck

Testinformationen machen Entwicklung, Qualitätssicherung, Migrationen, Schulungen und Fehleranalyse möglich. Gleichzeitig können Testdaten sensible Geschäftslogik, personenbezogene Daten, Geheimnisse, Produktionsstrukturen oder realistische Angriffspfade enthalten. Diese Routine sorgt dafür, dass Testinformationen zweckgebunden, geschützt, begrenzt und überprüfbar genutzt werden.

Der Kern ist nicht „Testdaten vorhanden“, sondern: Welche Informationen werden wofür genutzt? Sind echte Daten erforderlich? Wer genehmigt sie? Wie werden sie geschützt, bereinigt und gelöscht?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine für Auswahl, Freigabe, Schutz, Nutzung, Ablage und Löschung von Testinformationen. Sie verbindet Testbedarf, Datenklassifizierung, Datenschutz-Handoff, Umgebungstrennung, Zugriffsschutz und Evidenz.

## Typische Risiken

- Wenn produktive Daten ungeprüft in Testumgebungen kopiert werden, können vertrauliche oder personenbezogene Informationen unnötig exponiert werden.
- Wenn Testdaten reale Zugangsdaten, Tokens oder Schlüssel enthalten, können produktive Systeme kompromittiert werden.
- Wenn Testdaten lange liegen bleiben, entstehen vergessene Datenbestände mit schwächerem Schutz.
- Wenn externe Tester oder Entwickler breite Testdaten erhalten, können Datenabflüsse oder unklare Verantwortlichkeiten entstehen.
- Wenn Anonymisierung oder Maskierung ungeprüft bleibt, kann Re-Identifikation oder Rückschluss auf echte Personen, Kunden oder Geschäftsgeheimnisse möglich sein.
- Wenn Testdaten nicht zum Testziel passen, entstehen Scheintests und unerkannte Fehler.

## Trigger

- neues Test-, Entwicklungs-, Schulungs-, Analyse- oder Migrationsvorhaben.
- Kopie, Extrakt oder Bereitstellung produktiver oder produktionsnaher Daten.
- Nutzung externer Tester, Dienstleister, Entwickler oder Cloud-Testdienste.
- Fehleranalyse mit realistischen Daten oder Logauszügen.
- neue Datenklasse, neues System, neue Schnittstelle oder geänderte Datenflüsse.
- Auditfinding, Datenschutzfrage, Incident oder Datenabflussverdacht.
- turnusmäßiger Review von Testdatenbeständen und Testumgebungen.

## Rollen und Verantwortung

- **Test Owner / QA-Verantwortliche:** beschreibt Testzweck, Datenbedarf und Akzeptanzkriterien.
- **Data Owner / Information Owner:** entscheidet, welche Daten oder Datenklassen für den Test zulässig sind.
- **Product Owner / Service Owner:** priorisiert Testbedarf und akzeptiert funktionale Einschränkungen bei synthetischen Daten.
- **IT-/Plattform Owner:** stellt Testumgebung, Zugriffsschutz, Bereinigung, Löschung und technische Schutzmaßnahmen bereit.
- **Security-Rolle / ISMS-Owner:** definiert Schutzanforderungen, Reviewlogik, Ausnahmebehandlung und Evidenz.
- **Datenschutz / Legal:** prüft personenbezogene Daten, Anonymisierung, Maskierung, Aufbewahrung, Dienstleister und Zweckbindung.
- **Management:** entscheidet bei Zielkonflikten zwischen Testqualität, Aufwand, Datenschutz-/Schutzbedarf und Lieferterminen.

## Implementierung

### Minimalstart

Ziel: Testinformationen werden nicht ungeprüft aus Produktion kopiert.

1. Jeder Testdatenbedarf für kritische Systeme wird kurz beschrieben: Zweck, System, Datenklasse, Nutzerkreis und Dauer.
2. Standard ist synthetische, anonymisierte, maskierte oder reduzierte Testinformation, soweit sie das Testziel erfüllt.
3. Produktive oder produktionsnahe Daten benötigen eine nachvollziehbare Freigabe durch Data Owner und gegebenenfalls Datenschutz-/Legal-Handoff.
4. Testdatenzugriffe werden auf notwendige Personen und Laufzeit begrenzt.
5. Secrets, Passwörter, Tokens und Schlüssel werden nicht aus Produktion in Testbestände übernommen.
6. Nach Testende werden Daten gelöscht, bereinigt oder in einen geregelten Bestand überführt.

Minimaler Nachweis:

- Testdatenantrag oder Testdatensteckbrief,
- Freigabe des Data Owners,
- Schutz- oder Maskierungsentscheidung,
- Zugriffsnachweis für Testdaten,
- Lösch- oder Bereinigungsnachweis,
- Ausnahmeentscheidung bei produktionsnahen Daten.

### Solide Praxis

Ziel: Testdatenmanagement ist wiederholbar und risikobasiert.

1. Datenklassen und Testdatenarten werden unterschieden: synthetisch, anonymisiert, maskiert, pseudonymisiert, produktionsnah, Logdaten, Referenzdaten.
2. Für jede Klasse gibt es Mindestschutz: Zugriff, Speicherort, Verschlüsselung, Aufbewahrung, Weitergabe, Löschung.
3. Maskierungs- und Anonymisierungsverfahren werden durch Data Owner und Datenschutz passend zum Risiko geprüft.
4. Testdatenbestände werden inventarisiert: System, Zweck, Owner, Datenklasse, Erstellungsdatum, Ablaufdatum, Umgebung.
5. Externe Nutzung wird mit Lieferanten-, Zugriffs- und Vertragssteuerung verbunden.
6. Testdatenreviews prüfen verwaiste Bestände, zu breite Zugriffe und überfällige Löschung.
7. Findings aus Tests, Incidents oder Audits verbessern Testdatenregeln und Umgebungsstandards.

Starke Evidenz:

- Testdatenregister,
- Datenklassifizierung je Testbestand,
- Freigaben und Datenschutz-/Legal-Handoffs,
- Maskierungs- oder Synthetisierungsnachweise,
- Zugriffreviews,
- Löschprotokolle,
- Ausnahme- und Risikoentscheidungen.

### Fortgeschritten

Ziel: Testinformationen werden automatisiert, reproduzierbar und datensparsam bereitgestellt.

1. Testdaten werden über definierte Pipelines erzeugt, maskiert, synthetisiert oder bereitgestellt.
2. Automatisierte Checks verhindern Übernahme von Secrets, produktiven Identifikatoren oder unzulässigen Datenklassen.
3. Testdatenbestände haben technische Ablaufdaten, Bereinigungsjobs oder Löschworkflows.
4. Rollenbasierte Self-Service-Bereitstellung verbindet Testzweck, Genehmigung, Datenklasse und Zugriff.
5. Qualität synthetischer oder maskierter Testdaten wird gegen Testziele geprüft, damit Schutz nicht zu Scheintests führt.
6. Kennzahlen zeigen produktionsnahe Testdaten, überfällige Bestände, externe Nutzung, Löschfristen und Ausnahmen.

## Ablauf als Routine

1. **Testbedarf entsteht:** Feature, Release, Fehleranalyse, Migration, Schulung oder Abnahmetest.
2. **Datenbedarf beschreiben:** Testziel, benötigte Felder, Realitätsgrad, Datenklasse, Nutzerkreis und Dauer klären.
3. **Schutzvariante wählen:** synthetisch, anonymisiert, maskiert, reduziert oder begründet produktionsnah.
4. **Freigabe einholen:** Data Owner und bei personenbezogenen oder sensiblen Daten Datenschutz/Legal einbeziehen.
5. **Daten bereitstellen:** kontrollierte Umgebung, getrennte Secrets, angemessene Zugriffsbeschränkung und Protokollierung nutzen.
6. **Test durchführen:** Nutzung auf Zweck und Laufzeit begrenzen.
7. **Bestand prüfen:** nicht mehr benötigte Daten löschen, Zugriffe entziehen, Ausnahmen schließen.
8. **Evidenz sichern:** Antrag, Entscheidung, Schutzmaßnahme, Zugriff und Löschung dokumentieren.
9. **Verbessern:** wiederkehrende Testdatenprobleme in Datenmodell, Teststrategie oder Plattformstandard zurückspielen.

## Entscheidungen

- Wann reichen synthetische oder reduzierte Daten für den Testzweck aus?
- Welche Datenklassen dürfen nie oder nur mit Sonderfreigabe in Testumgebungen?
- Wer darf produktionsnahe Testdaten genehmigen und für wie lange?
- Welche Maskierung oder Anonymisierung ist ausreichend, ohne eine Datenschutzbewertung zu ersetzen?
- Welche externen Beteiligten dürfen Testinformationen erhalten?
- Wann wird fehlende Testdatenqualität zum Risiko für Release oder Abnahme?
- Welche Altbestände müssen bereinigt oder ins Management Review eskaliert werden?

## Evidenz

### Starke Evidenz

- Testdatensteckbrief mit Zweck, Datenklasse, Owner und Laufzeit,
- Data-Owner-Freigabe und Datenschutz-/Legal-Handoff bei Bedarf,
- Nachweis von Maskierung, Anonymisierung, Reduktion oder synthetischer Erzeugung,
- Testdatenregister mit Ablaufdatum,
- Zugriffsnachweise und Reviews,
- Lösch- oder Bereinigungsprotokolle,
- Ausnahme mit Risikoentscheidung und Wiedervorlage.

### Schwache Evidenz

- allgemeine Aussage „Testdaten sind anonymisiert“ ohne Nachweis oder Scope,
- Datenbankkopie ohne Freigabe,
- Testumgebung mit unklarem Datenbestand,
- Screenshot einer Maskierungsregel ohne Ergebnisprüfung,
- Zugriffsgruppe ohne Owner oder Ablaufdatum,
- alte Testdatenrichtlinie ohne Bestandsreview.

### Evidenzlücken

- produktive Datenkopien ohne dokumentierten Zweck,
- Secrets oder echte Zugangsdaten in Testdaten,
- externe Nutzung ohne Lieferanten- oder Zugriffsklärung,
- keine Löschfristen für Testbestände,
- keine Prüfung der Maskierungsqualität,
- verwaiste Testumgebungen mit sensiblen Daten.

## Wirksamkeitsprüfung

Prüffragen:

- Kann für kritische Testdatenbestände Zweck, Owner, Datenklasse und Laufzeit nachvollzogen werden?
- Wird produktionsnahe Nutzung begründet und freigegeben?
- Werden Secrets und produktive Zugangsdaten zuverlässig aus Testdaten entfernt?
- Sind Testdatenzugriffe auf notwendige Personen und Zeiträume begrenzt?
- Werden alte Testdatenbestände gelöscht oder reviewed?
- Ist Datenschutz/Legal eingebunden, wenn personenbezogene oder besonders sensible Daten betroffen sind?
- Unterstützen die gewählten Testdaten das Testziel, ohne unnötige Schutzrisiken zu erzeugen?

Mögliche Kennzahlen:

- Anzahl produktionsnaher Testdatenbestände,
- überfällige Testdatenlöschungen,
- Testdatenbestände ohne Owner,
- externe Zugriffe auf Testinformationen,
- Ausnahmen zur Nutzung produktiver Daten,
- Findings zu Secrets oder unzulässigen Daten in Testumgebungen.

## BSIG-/NIS2-Anschluss

Der Schutz von Testinformationen ist anschlussfähig an NIS2-orientierte Themen wie sichere Entwicklung, Datenschutz-nahe Schutzmaßnahmen, Zugriffsschutz, Risikomanagement, Lieferkettensicherheit und Schutz digitaler Dienste. Der konkrete Bezug sollte organisationsspezifisch über Datenklassifizierung, Anforderungsregister und Human Review geprüft werden.

Dieses Artefakt ersetzt keine Datenschutzberatung und keine rechtliche Prüfung der Datenverarbeitung.

## Grenzen

- Dieses Artefakt ist keine Datenschutz-Folgenabschätzung und kein Rechtsgutachten.
- Es ersetzt keine technische Bewertung von Anonymisierung, Maskierung oder Re-Identifikationsrisiken.
- Es garantiert keine Datenschutzkonformität, Sicherheit oder Zertifizierungsfähigkeit.
- Es enthält keine echten Daten, Geheimnisse oder ISO-27002-Texte.
- Es darf nicht dazu verleiten, produktive Daten aus Bequemlichkeit in Testumgebungen zu kopieren.

## Handoffs

- **Datenschutz-/Legal-Handoff:** personenbezogene Daten, Re-Identifikationsrisiko, Maskierung, Zweckbindung, Dienstleister, Aufbewahrung oder Betroffenenrisiken.
- **Data-Owner-Handoff:** Freigabe von Datenklassen, Datenminimierung, Qualität und zulässiger Testzweck.
- **Access-Handoff:** Testdatenzugriffe, externe Tester, Dienstleister und Ablauf von Berechtigungen.
- **Umgebungs-Handoff:** Test-, Staging- oder Entwicklungsumgebung mit produktionsnahen Daten.
- **Development-/QA-Handoff:** Testziel, Datenqualität, synthetische Daten, Fehleranalyse und Release-Risiken.
- **Incident-Handoff:** Verdacht auf Testdatenabfluss, Secrets in Testdaten oder unzulässige Datenkopie.
- **Management-Handoff:** Zielkonflikt zwischen Testrealismus, Liefertermin, Schutzbedarf und Aufwand.

## Typische Fehler

- Produktionsdaten werden kopiert, weil es der schnellste Weg ist.
- Maskierung wird behauptet, aber nicht auf Ergebnis und Rückschlussrisiken geprüft.
- Testdaten enthalten echte Passwörter, Tokens oder Schlüssel.
- Testdaten werden nach Projektende nicht gelöscht.
- Externe Entwickler erhalten breite Datenpakete ohne Zweck- und Laufzeitbegrenzung.
- Testdaten sind so stark verfälscht, dass wichtige Fehler nicht gefunden werden.
- Datenschutz wird erst gefragt, nachdem Daten bereits kopiert wurden.

## Fiktives Mini-Beispiel

Ein fiktives Entwicklungsteam benötigt realistische Daten für einen Migrations-Test. Der Test Owner beschreibt die benötigten Felder und stellt fest, dass echte Namen und Kontaktdaten nicht erforderlich sind. Der Data Owner genehmigt einen maskierten Auszug mit reduziertem Umfang. Datenschutz prüft den Personenbezug. Die Plattform erzeugt den Auszug in einer geschützten Staging-Umgebung und setzt ein Löschdatum. Nach Testabschluss wird der Bestand gelöscht und im Testdatenregister geschlossen.

Evidenz:

- Testdatensteckbrief,
- Data-Owner-Freigabe,
- Datenschutz-Handoff,
- Maskierungsnachweis,
- Zugriffsliste für Staging,
- Löschprotokoll,
- geschlossener Registereintrag.
