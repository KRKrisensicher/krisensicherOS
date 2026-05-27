
# A.8.10 — Informationen löschen

## Zweck

Informationen zu löschen bedeutet, Daten, Kopien, Zwischenspeicher, Datenträger und Zugriffspfade kontrolliert aus dem Betrieb zu nehmen, wenn sie nicht mehr benötigt werden oder gelöscht werden müssen. Der Kern ist nicht ein Löschversprechen, sondern eine nachvollziehbare Routine: Was wird wann von wem gelöscht, wo bleiben technische Restbestände, und wer entscheidet über Ausnahmen?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine für geplantes, anlassbezogenes und überprüfbares Löschen von Informationen über Systeme, Speichermedien, Cloud-Dienste, Backups, mobile Geräte, Logs und Dienstleister hinweg. Löschung wird mit Informationsklassifizierung, Aufbewahrungsregeln, Berechtigungen, Vertragsende, Systemstilllegung und Datenschutz-/Legal-Handoffs verbunden.

## Typische Risiken

- Wenn Informationen über ihren Nutzungszweck hinaus in Ablagen, Postfächern, Exporten oder Schattenkopien verbleiben, steigt das Risiko unbefugter Einsicht und späterer Datenabflüsse.
- Wenn Systeme außer Betrieb genommen werden, aber Datenbanken, Snapshots oder Datenträger nicht kontrolliert behandelt werden, bleiben verwertbare Altbestände zurück.
- Wenn Löschungen nur manuell und informell erfolgen, kann niemand nachweisen, welche Daten tatsächlich betroffen waren.
- Wenn Backups, Logs und Archive nicht in die Löschlogik einbezogen werden, entstehen Scheinnachweise und unerwartete Wiederherstellungen alter Daten.
- Wenn Dienstleisterdaten nach Vertragsende nicht bestätigt gelöscht oder zurückgegeben werden, bleibt Verantwortung unklar.

## Trigger

- Ende eines Geschäftsprozesses, Vertrags, Projekts, Dienstleisterzugriffs oder Systems.
- Ablauf einer definierten Aufbewahrungsfrist oder Wegfall eines fachlichen Nutzungszwecks.
- Stilllegung, Migration, Mandantenwechsel oder Ausmusterung von Geräten und Speichermedien.
- Datenschutz-/Legal-Anforderung, Betroffenenanfrage oder interne Löschanforderung mit Human Review.
- Sicherheitsereignis, unberechtigter Datenbestand, Auditfinding oder Bereinigungsmaßnahme.
- Änderung der Datenklassifizierung, Speicherarchitektur, Backupstrategie oder Cloud-/SaaS-Nutzung.
- turnusmäßiger Review von Datenbeständen, Shares, Exporten, Logs und Altarchiven.

## Rollen und Verantwortung

- **Information Owner / Prozess Owner:** bestimmt fachlichen Nutzungszweck, Aufbewahrungsbedarf und Freigabe zur Löschung.
- **IT-/Plattform Owner:** setzt Löschung, sichere Außerbetriebnahme, Medienbehandlung und technische Nachweise um.
- **Datenschutz / Legal:** prüft Löschanforderungen, Aufbewahrungspflichten, personenbezogene Daten und Streit-/Nachweissituationen.
- **Records-/Dokumentenverantwortliche:** koordiniert Aufbewahrungs- und Archivlogik, soweit vorhanden.
- **Lieferantenmanagement:** holt Lösch-/Rückgabebestätigungen und vertragliche Nachweise ein.
- **ISMS-Owner / Security-Rolle:** definiert Mindestlogik, Evidenzanforderungen, Risiko- und Eskalationswege.
- **Management:** entscheidet bei Zielkonflikten zwischen Löschung, Nachweisbedarf, Betriebsrisiko, Kosten und Restrisiko.

## Implementierung

### Minimalstart

Ziel: kritische Datenbestände und Systemstilllegungen kontrolliert löschen können.

1. Die Organisation benennt Datenbestände mit hohem Schutzbedarf, alte Ablagen und Systeme im ISMS-Scope.
2. Für jeden Bestand gibt es einen fachlichen Owner und einen technischen Ansprechpartner.
3. Löschanlässe werden in einem einfachen Löschlog oder Ticket erfasst: Bestand, Anlass, Owner, Entscheidung, Methode, Datum, Nachweis.
4. Systemstilllegung, Geräteausmusterung und Vertragsende erhalten eine Lösch-/Rückgabe-Checkliste.
5. Ausnahmen werden befristet dokumentiert, etwa wegen Nachweisbedarf, Backupzyklus oder laufender Klärung.
6. Mindestens jährlich wird stichprobenartig geprüft, ob Altbestände und Exporte noch benötigt werden.

Minimaler Nachweis:

- Liste kritischer Datenbestände mit Owner,
- Lösch- oder Stilllegungsticket,
- Freigabe des fachlichen Owners,
- technischer Lösch- oder Vernichtungsnachweis,
- Ausnahme mit Begründung und Wiedervorlage.

### Solide Praxis

Ziel: Löschung wird mit Datenlebenszyklus, Aufbewahrung und Dienstleistersteuerung verbunden.

1. Datenklassen erhalten Lösch- und Aufbewahrungslogiken, die fachlich und rechtlich geprüft werden.
2. Systeme, Datenbanken, File Shares, SaaS-Dienste, Logs, Backups und Archive werden mit zuständigen Ownern verknüpft.
3. Löschmethoden werden je Kontext festgelegt: logische Löschung, sichere Überschreibung, Schlüsselvernichtung, Medienvernichtung, Mandantenbereinigung oder Dienstleisterbestätigung.
4. Migrationen und Stilllegungen enthalten Pflichtschritte für Restdaten, Snapshots, Testkopien und temporäre Exporte.
5. Regelmäßige Reviews identifizieren verwaiste Ablagen, Altprojekte, unkontrollierte Exporte und überfällige Datenbestände.
6. Löschkonflikte werden entschieden: Aufbewahrung, Beweissicherung, Datenschutz, Betrieb, Kosten und Risiko.

Starke Evidenz:

- Datenbestands-/Systemliste mit Löschowner,
- geprüfte Lösch- und Aufbewahrungsregeln,
- Tickets mit Freigabe, Durchführung und Validierung,
- Datenträgervernichtungs- oder Löschzertifikate,
- Dienstleisterbestätigungen,
- Reviewprotokolle zu Altbeständen,
- Managemententscheidung bei Konflikten oder Restrisiken.

### Fortgeschritten

Ziel: Löschung ist automatisiert, risikobasiert und über Datenflüsse hinweg steuerbar.

1. Datenklassifizierung, Aufbewahrungsfristen, DLP-/Discovery-Ergebnisse und Systeminventar sind miteinander verbunden.
2. Löschläufe werden technisch protokolliert und bei Fehlern eskaliert.
3. Schlüsselmanagement unterstützt kontrollierte Unzugänglichmachung verschlüsselter Datenbestände, wo geeignet und geprüft.
4. Cloud- und SaaS-Dienste werden regelmäßig auf Export-, Papierkorb-, Snapshot- und Mandantenrestbestände geprüft.
5. Backup- und Archivkonzepte benennen, wann Löschanforderungen unmittelbar, verzögert oder nur über Ablaufzyklen wirken.
6. Kennzahlen zeigen überfällige Löschungen, Altbestände, Ausnahmen, nicht zuordenbare Datenbestände und offene Dienstleisterbestätigungen.

## Ablauf als Routine

1. **Löschanlass entsteht:** Fristablauf, Systemstilllegung, Vertragsende, Anfrage, Reviewfinding oder Incident.
2. **Scope klären:** betroffene Datenbestände, Kopien, Systeme, Backups, Dienstleister und Datenträger bestimmen.
3. **Freigabe prüfen:** fachlicher Owner bestätigt Nutzungsende; Legal/Datenschutz prüft Aufbewahrung oder Sperrgründe, falls relevant.
4. **Methode festlegen:** passende Lösch-, Sperr-, Vernichtungs- oder Schlüsselmaßnahme wählen.
5. **Umsetzen:** IT, Fachbereich oder Dienstleister führt die Löschung kontrolliert durch.
6. **Validieren:** Stichprobe, Protokoll, Systemstatus, Zertifikat oder Dienstleisterbestätigung prüfen.
7. **Nachweis ablegen:** Entscheidung, Durchführung, Restbestände und Ausnahmen dokumentieren.
8. **Eskalieren:** unklare Aufbewahrung, fehlender Owner, technische Nichtlöschbarkeit oder Kostenkonflikt ins Management bzw. Legal/Datenschutz geben.
9. **Verbessern:** Ursachen für Altbestände in Datenhaltung, Rollen, Systemdesign oder Beschaffung zurückspielen.

## Entscheidungen

- Welche Datenbestände und Speichermedien sind für den Start kritisch genug?
- Wer darf Löschung freigeben, aussetzen oder eine Ausnahme akzeptieren?
- Wie werden Backups, Archive, Logs, Snapshots und Papierkörbe behandelt?
- Welche Löschmethoden sind für welche Datenklasse und Plattform angemessen?
- Wann reicht eine Dienstleisterbestätigung, wann braucht es zusätzliche Prüfung?
- Wie werden Zielkonflikte zwischen Löschung, Nachweispflicht, Betrieb und Forensik entschieden?

## Evidenz

### Starke Evidenz

- aktueller Daten-/Systemscope mit Ownern,
- Löschanforderung mit Anlass, Freigabe und Datum,
- technisches Löschprotokoll oder Datenträgervernichtungsnachweis,
- dokumentierte Behandlung von Backups, Archiven und Restkopien,
- Dienstleisterbestätigung bei extern gespeicherten Daten,
- Reviewnachweis zu Altbeständen und Korrekturmaßnahmen,
- Ausnahme mit Laufzeit, Risikoentscheidung und Wiedervorlage.

### Schwache Evidenz

- allgemeine Löschpolicy ohne konkrete Durchführung,
- mündliche Bestätigung „wurde gelöscht“,
- Screenshot eines leeren Ordners ohne Scope,
- Ticket ohne fachliche Freigabe oder Validierung,
- Dienstleistervertrag ohne konkrete Löschbestätigung,
- Aufbewahrungsplan ohne Systembezug.

### Evidenzlücken

- unbekannte Kopien in Testsystemen, Exports, Postfächern oder Schattenablagen,
- keine Regel für Backups und Snapshots,
- Datenträgerausmusterung ohne Nachweis,
- Dienstleisterende ohne Rückgabe-/Löschbestätigung,
- dauerhafte Ausnahmen ohne Entscheidung,
- kein Owner für Altarchive.

## Wirksamkeitsprüfung

Prüffragen:

- Können kritische Datenbestände einem Owner und einer Löschlogik zugeordnet werden?
- Werden Löschanlässe tatsächlich in Tickets oder Logs verarbeitet?
- Sind Backups, Archive, Logs, Exporte und Testkopien in der Routine sichtbar?
- Gibt es Nachweise, dass Löschungen validiert oder Dienstleisterbestätigungen eingeholt wurden?
- Werden unklare Aufbewahrungs- oder Datenschutzfragen rechtzeitig eskaliert?
- Werden Altbestände reduziert und Ursachen für neue Altbestände behoben?

Mögliche Kennzahlen:

- überfällige Löschanforderungen,
- Anteil kritischer Datenbestände mit Owner und Löschlogik,
- offene Dienstleisterbestätigungen,
- Anzahl verwaister Altbestände,
- Ausnahmequote und überfällige Ausnahmen,
- Zeit von Löschanlass bis Nachweis.

## BSIG-/NIS2-Anschluss

Kontrolliertes Löschen ist anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Cyberhygiene, Zugriffsschutz, Umgang mit sensiblen Informationen, Lieferantensteuerung und Incident-Folgebearbeitung. Für betroffene Organisationen sollte der konkrete Bezug im Anforderungsregister und in Daten-/Systeminventaren geprüft werden.

Dieses Artefakt ersetzt keine rechtliche oder datenschutzrechtliche Prüfung von Löschpflichten, Aufbewahrungspflichten oder Betroffenenrechten.

## Grenzen

- Dieses Artefakt ist kein Rechts- oder Datenschutzgutachten zu Löschfristen.
- Es ersetzt keine forensische Sicherungsentscheidung und keine Archivierungsstrategie.
- Es garantiert nicht, dass alle technischen Restdaten vollständig entfernt sind.
- Es enthält keine ISO-27002-Texte und keine Zertifizierungszusage.
- Öffentliche Beispiele dürfen keine echten Organisations-, Kunden-, Personen- oder Geheimdaten enthalten.

## Handoffs

- **Datenschutz-/Legal-Handoff:** Löschbegehren, Aufbewahrungspflichten, personenbezogene Daten, Streitfälle, Beweissicherung.
- **IT-/Plattform-Handoff:** technische Löschung, Backups, Snapshots, Datenträger, Schlüssel, Validierung.
- **Lieferanten-Handoff:** Vertragsende, Cloud-/SaaS-Daten, Subdienstleister, Lösch-/Rückgabebestätigung.
- **Incident-Handoff:** unzulässiger Datenbestand, Datenabfluss, forensische Sicherung vor Löschung.
- **BCM-Handoff:** Löschung oder Schlüsselvernichtung kann Wiederherstellbarkeit oder Notbetrieb beeinflussen.
- **Management-Handoff:** Kosten, technische Nichtlöschbarkeit, Restrisiko, dauerhafte Ausnahme.
- **Audit-/Evidence-Handoff:** fehlende Nachweise oder nicht prüfbare Löschentscheidungen.

## Typische Fehler

- Löschung wird als IT-Aufgabe verstanden, ohne fachliche Freigabe.
- Backups, Logs, Testdaten und Exporte werden vergessen.
- Stillgelegte Systeme bleiben als Datenfriedhof erreichbar.
- Dienstleisterbestätigungen werden nach Vertragsende nicht eingeholt.
- Ausnahmen werden nicht befristet.
- Löschfristen werden pauschal behauptet, ohne Legal-/Datenschutzprüfung.
- Es wird gelöscht, obwohl Beweissicherung oder Aufbewahrung noch ungeklärt ist.

## Fiktives Mini-Beispiel

Ein fiktiver Maschinenbaudienstleister stellt ein altes Projektportal ab. Der Service Owner bestätigt, dass die Projektdaten nicht mehr operativ benötigt werden. Legal prüft, welche Unterlagen noch aufbewahrt werden müssen. IT exportiert den freigegebenen Archivanteil, löscht den Portalmandanten, dokumentiert die Behandlung der Backups über reguläre Ablaufzyklen und lässt den Hosting-Dienstleister die Mandantenlöschung bestätigen. Eine alte Testdatenkopie wird beim Review gefunden und separat gelöscht.

Evidenz:

- Stilllegungsticket mit fachlicher Freigabe,
- Legal-/Datenschutz-Prüfnotiz ohne Rechtsberatung im Artefakt,
- technisches Löschprotokoll,
- Dienstleisterbestätigung,
- Nachweis zur Testdatenbereinigung,
- Ausnahmevermerk für Backup-Ablaufzyklen.
