
# A.7.10 — Umgang mit Speichermedien

## Zweck

Speichermedien können große Mengen schutzbedürftiger Informationen transportieren, vervielfältigen oder nach der Nutzung weiter enthalten. Diese Routine sorgt dafür, dass USB-Sticks, externe Festplatten, Backup-Medien, Speicherkarten, mobile Datenträger, ausgemusterte Laufwerke und vergleichbare Medien nicht informell entstehen, herumliegen, weitergegeben oder entsorgt werden.

Der Kern ist nicht „USB verbieten“, sondern eine betriebene Medienlogik: Welche Medien sind erlaubt, wer verantwortet sie, welche Daten dürfen darauf, wie werden sie geschützt, transportiert, gelöscht, vernichtet und nachgewiesen?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine für Speichermedien über den gesamten Lebenszyklus: Bedarf, Freigabe, Kennzeichnung oder Zuordnung, Nutzung, Transport, Lagerung, Rückgabe, sichere Löschung, Vernichtung und Ausnahmebehandlung.

## Typische Risiken

- Wenn unverschlüsselte Medien verloren gehen, können vertrauliche oder personenbezogene Informationen offengelegt werden.
- Wenn Medien ohne Inventar genutzt werden, fehlen Owner, Rückgabe, Löschung und Verantwortlichkeit.
- Wenn alte Festplatten, Backup-Bänder oder Speicherkarten vor Entsorgung nicht sicher behandelt werden, bleiben Daten rekonstruierbar.
- Wenn externe Medien ungeprüft angeschlossen werden, können Schadsoftware, Datenabfluss oder unkontrollierte Kopien entstehen.
- Wenn Backup- oder Exportmedien nicht geschützt gelagert werden, können Wiederherstellungsfähigkeit und Vertraulichkeit zugleich gefährdet sein.
- Wenn Medien an Dienstleister, Behörden, Kunden oder Reparaturstellen gehen, können Übergabe, Rückgabe und Löschung unklar bleiben.

## Trigger

- Bedarf an Datentransport, Backup, Export, Migration, Forensik, Reparatur oder Archivierung.
- Ausgabe, Rückgabe, Versand, Verlust oder Fund eines Speichermediums.
- Beschaffung oder Außerbetriebnahme von Geräten mit eingebauten Datenträgern.
- Projektende, Systemmigration, Dienstleisterwechsel oder Vertragsende.
- Sicherheitsereignis, Malwareverdacht, Datenabflussverdacht oder Datenschutzprüfung.
- Änderung von Datenklassifizierung, Verschlüsselungsregel oder Endpoint-Policy.
- turnusmäßiger Medieninventur-, Backup- oder Entsorgungsreview.

## Rollen und Verantwortung

- **Information Owner / Asset Owner:** entscheidet, welche Daten auf Medien gespeichert werden dürfen und welcher Schutzbedarf gilt.
- **IT-/Endpoint-/Backup Owner:** stellt zugelassene Medien, Verschlüsselung, Sperrregeln, Löschung und technische Kontrolle bereit.
- **Nutzende Person / Fachbereich:** verwendet Medien nur freigegeben, schützt sie und meldet Verlust oder Abweichungen.
- **ISMS-Owner / Security-Rolle:** definiert Medienklassen, Mindestschutz, Ausnahme- und Reviewlogik.
- **Datenschutz / Legal:** prüft personenbezogene Daten, Übergaben, Verlustfolgen und vertragliche Fragen im Human Review.
- **Einkauf / Lieferantenmanagement:** steuert Medienvernichtung, Reparatur, Versand, externe Lagerung oder Dienstleisterübergaben.
- **Management:** entscheidet bei Restrisiken, Ausnahmen, Ressourcenbedarf oder nicht rückholbaren Medien.

## Implementierung

### Minimalstart

Ziel: Speichermedien mit schutzbedürftigen Daten sind begrenzt, zugeordnet und geschützt.

1. Die Organisation legt fest, welche Medientypen im Scope erlaubt sind und welche grundsätzlich nicht genutzt werden sollen.
2. Medien mit schutzbedürftigen Daten werden einem Owner, Zweck und Rückgabepunkt zugeordnet.
3. Für erlaubte Medien gelten Mindestanforderungen: Verschlüsselung, sichere Aufbewahrung, keine private Nutzung, Verlustmeldung, sichere Löschung oder Vernichtung.
4. Eingebaute Datenträger aus ausgemusterten oder reparierten Geräten werden vor Weitergabe bewertet.
5. Verlust, Fund oder ungeklärter Medienstatus wird als Sicherheitsereignis behandelt.
6. Ausnahmen werden befristet und mit Risikoentscheidung dokumentiert.

Minimaler Nachweis:

- Medienregel oder Kurzstandard,
- Liste ausgegebener oder kritischer Medien mit Owner,
- Nachweis Verschlüsselung oder sichere Aufbewahrung,
- Lösch-/Vernichtungsnachweis,
- Verlust-/Incident-Ticket oder Ausnahmeentscheidung.

### Solide Praxis

Ziel: Der Medienlebenszyklus ist in Betrieb, Backup, Endpoint, Entsorgung und Lieferantensteuerung eingebunden.

1. Medien werden nach Zweck und Schutzbedarf klassifiziert: Transportmedium, Backupmedium, Exportmedium, Forensikmedium, Archivmedium, Geräte-Datenträger.
2. Technische Richtlinien regeln Anschluss, Schreibrechte, Verschlüsselung und Protokollierung, soweit angemessen.
3. Ausgabe, Transport, externe Übergabe und Rückgabe werden über Tickets oder Übergabeprotokolle nachverfolgt.
4. Sichere Löschung und Vernichtung erfolgen mit nachvollziehbarer Methode und Nachweis.
5. Backup- und Archivmedien werden gegen Verlust, Diebstahl, Beschädigung und unbefugten Zugriff geschützt.
6. Dienstleister für Vernichtung, Reparatur oder Lagerung werden über Verträge, Aufträge und Nachweise gesteuert.
7. Medienereignisse fließen in Incident Response, Datenschutzprüfung und Lessons Learned ein.

Starke Evidenz:

- Medienklassifikation und erlaubte Nutzung,
- Medieninventar mit Owner, Zweck, Datenklasse und Status,
- Übergabe-, Versand- oder Rückgabeprotokolle,
- technische Richtlinien oder Endpoint-Auswertungen,
- Lösch- oder Vernichtungsnachweise,
- Dienstleisterbestätigung,
- Incident- und Ausnahmeentscheidungen.

### Fortgeschritten

Ziel: Medienkontrolle ist mit Datenklassifizierung, DLP, Backup-Resilienz und Entsorgungsprozessen integriert.

1. Endpoint- und DLP-Regeln beschränken oder überwachen Mediennutzung risikobasiert.
2. Verschlüsselungs- und Schlüsselmanagement sind für Mediennutzung und Wiederherstellung geregelt.
3. Backupmedien werden regelmäßig auf Wiederherstellbarkeit und sichere Lagerung geprüft.
4. Geräteausmusterung verbindet Assetinventar, sichere Löschung, Entsorgung und Nachweisführung.
5. Medienverluste oder ungewöhnliche Exportmuster erzeugen Security- oder Datenschutz-Triage.
6. Management erhält entscheidungsfähige Kennzahlen zu Medienausnahmen, Verlusten, Vernichtungslücken und Backup-/Archivrisiken.

## Ablauf als Routine

1. **Medienbedarf entsteht:** Transport, Backup, Export, Reparatur, Migration, Forensik oder Archivierung.
2. **Zweck und Datenklasse klären:** Welche Informationen sollen auf das Medium und warum?
3. **Freigabe und Schutz festlegen:** erlaubter Medientyp, Verschlüsselung, Lagerung, Transport, Rückgabe und Löschung.
4. **Ausgeben oder nutzen:** Medium wird zugeordnet, gekennzeichnet oder im Register geführt.
5. **Transport oder Übergabe steuern:** Empfänger, Übergabeweg und Rückgabepunkt nachvollziehbar machen.
6. **Beenden:** Daten löschen, Medium zurückgeben, wiederverwenden oder vernichten.
7. **Nachweis sichern:** Ticket, Register, Lösch-/Vernichtungsnachweis oder Übergabeprotokoll ablegen.
8. **Abweichung behandeln:** Verlust, Fund, Malwareverdacht oder unbekannter Medienstatus eskalieren.
9. **Verbessern:** Muster aus Verlusten, Ausnahmen oder Schattennutzung in Regeln und Technik zurückspielen.

## Entscheidungen

- Welche Speichermedien sind grundsätzlich erlaubt, eingeschränkt oder untersagt?
- Welche Datenklassen dürfen auf transportable Medien?
- Wann ist Verschlüsselung, Vier-Augen-Übergabe oder spezielle Lagerung erforderlich?
- Welche Lösch- oder Vernichtungsmethode ist für welche Medienklasse angemessen?
- Wer darf Medienausnahmen akzeptieren und wie lange?
- Wann wird Medienverlust zum Incident-, Datenschutz- oder Managementthema?
- Wie werden Dienstleister für Vernichtung, Reparatur und Lagerung überprüft?

## Evidenz

### Starke Evidenz

- aktueller Medienstandard mit Rollen und Triggern,
- Medienregister mit Owner, Zweck, Datenklasse und Status,
- Nachweise über Verschlüsselung oder technische Medienkontrolle,
- Übergabe-, Versand-, Rückgabe- und Löschprotokolle,
- Vernichtungszertifikat oder dokumentierter interner Vernichtungsnachweis,
- Incidentticket bei Verlust oder Fund,
- befristete Ausnahme mit Risikoentscheidung,
- Managemententscheidung bei nicht klärbaren oder kritischen Medienrisiken.

### Schwache Evidenz

- pauschale Aussage „USB ist verboten“ ohne technische oder organisatorische Prüfung,
- Liste von USB-Sticks ohne Datenklasse oder Owner,
- Vernichtungsrechnung ohne Bezug zu konkreten Medien,
- Screenshot einer Endpoint-Regel ohne Review oder Ausnahmebehandlung,
- Backupregel ohne Lagerungs- oder Wiederherstellungsnachweis.

### Evidenzlücken

- Medien mit schutzbedürftigen Daten ohne Zuordnung,
- ausgemusterte Geräte ohne Lösch- oder Vernichtungsnachweis,
- externe Übergaben ohne Empfänger- und Rückgabedokumentation,
- Verlust ohne Incident- oder Datenschutzprüfung,
- Backupmedien ohne Schutz- oder Restore-Nachweis,
- Ausnahmen ohne Ablaufdatum.

## Wirksamkeitsprüfung

Prüffragen:

- Sind erlaubte und nicht erlaubte Medienarten verständlich geregelt?
- Können kritische Medien einem Owner, Zweck und Status zugeordnet werden?
- Gibt es Nachweise für sichere Löschung oder Vernichtung vor Weitergabe?
- Werden externe Übergaben, Versand und Reparaturen nachvollziehbar gesteuert?
- Werden Medienverluste schnell genug gemeldet und bewertet?
- Sind Backup- und Archivmedien sowohl geschützt als auch wiederherstellbar?
- Führen Ausnahmen und Findings zu Korrekturen?

Mögliche Kennzahlen:

- Anzahl ausgegebener kritischer Medien,
- offene oder überfällige Rückgaben,
- Medienausnahmen nach Datenklasse,
- Lösch-/Vernichtungsnachweise je Entsorgungswelle,
- Medienverluste und Bearbeitungszeit,
- nicht autorisierte Medienanschlüsse, sofern technisch erhoben und datenschutzrechtlich geklärt.

## BSIG-/NIS2-Anschluss

Der Umgang mit Speichermedien ist anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Cyberhygiene, Schutz von Informationen, Incident Handling, Business Continuity und Lieferkettensicherheit bei Entsorgung oder externer Lagerung. Der konkrete Bezug sollte im Anforderungsregister und in den Daten-/Assetprozessen geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung von Datenschutzfolgen, Meldepflichten, Aufbewahrungspflichten oder Anwendbarkeit.

## Grenzen

- Dieses Artefakt ist keine detaillierte Kryptografie-, Backup- oder Forensik-Anleitung.
- Es ersetzt keine Datenschutzprüfung bei personenbezogenen Daten auf Medien.
- Es ersetzt keine vertragliche Prüfung von Entsorgungs-, Reparatur- oder Lagerdienstleistern.
- Es trifft keine Zertifizierungs- oder Konformitätszusage.
- Es darf keine echten Mediennummern, Standortdetails oder vertraulichen Daten in öffentlichen Beispielen enthalten.

## Handoffs

- **IT-/Endpoint-Handoff:** Medienfreigabe, Anschlusskontrolle, Verschlüsselung, Löschung und technische Auswertungen.
- **Backup-/BCM-Handoff:** Backupmedien, Wiederherstellbarkeit, Offsite-Lagerung und Notfallzugriff.
- **Datenschutz-/Legal-Handoff:** personenbezogene Daten, Verlust, externe Übergabe, Aufbewahrung und Löschpflichtfragen.
- **Incident-Handoff:** Verlust, Fund, Malwareverdacht, ungeklärte Kopie oder möglicher Datenabfluss.
- **Einkauf-/Lieferanten-Handoff:** Vernichtung, Reparatur, Transport, externe Lagerung oder Dienstleisterbestätigung.
- **Management-Handoff:** kritische Ausnahme, nicht klärbarer Medienstatus, Investitionsbedarf oder akzeptiertes Restrisiko.
- **Audit-/Evidence-Handoff:** fehlende Lösch-, Vernichtungs-, Übergabe- oder Rückgabenachweise.

## Typische Fehler

- Medien werden verboten, aber Ausnahmen entstehen informell.
- Festplatten aus Altgeräten werden wie Elektroschrott behandelt, nicht wie Datenträger.
- Backupmedien werden auf Verfügbarkeit geprüft, aber nicht auf Vertraulichkeit geschützt.
- Vernichtungsnachweise lassen nicht erkennen, welche Medien betroffen waren.
- Externe Übergaben an Dienstleister laufen ohne Rückgabe- oder Löschbestätigung.
- Verlustmeldungen werden als Beschaffungsthema behandelt, nicht als Sicherheitsereignis.
- Technische Sperren werden eingeführt, ohne berechtigte Sonderfälle zu regeln.

## Fiktives Mini-Beispiel

Ein fiktiver Fachbereich möchte Kundendaten für eine Migration auf einer externen SSD an einen Dienstleister übergeben. Der Information Owner verlangt Verschlüsselung, Übergabeprotokoll und Rückgabe- oder Löschbestätigung. IT stellt ein freigegebenes Medium bereit und dokumentiert die Zuordnung im Ticket. Nach Abschluss bestätigt der Dienstleister die Löschung, der Asset Owner schließt das Ticket und der ISMS-Owner nimmt die Ausnahmequote in den nächsten Review auf.

Evidenz:

- Freigabeticket mit Zweck und Datenklasse,
- Medienregistereintrag,
- Nachweis Verschlüsselung,
- Übergabeprotokoll,
- Löschbestätigung des Dienstleisters,
- Reviewnotiz zur Medienausnahme.
