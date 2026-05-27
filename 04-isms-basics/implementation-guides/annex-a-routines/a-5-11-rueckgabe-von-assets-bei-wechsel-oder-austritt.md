
# A.5.11 — Rückgabe von Assets bei Wechsel oder Austritt

## Zweck

Diese Routine stellt sicher, dass Organisationswerte bei Rollenwechsel, Austritt oder Vertragsende nicht unkontrolliert bei Personen, Teams oder Dienstleistern verbleiben. Gemeint sind physische Geräte, Zutrittsmittel, Datenträger, Unterlagen, Softwarelizenzen, Token, Schlüssel, mobile Geräte und andere Mittel, mit denen Informationen genutzt oder geschützt werden.

Der Kern ist nicht die Unterschrift auf einer Rückgabeliste, sondern ein verlässlicher Abschlussprozess: Was wurde übergeben, was muss zurück, wer prüft Vollständigkeit, welche Risiken entstehen bei Verlust und wann werden Zugriffe oder Ersatzmaßnahmen ausgelöst?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Routine für Rückgabe, Sperrung, Bereinigung, Wiederverwendung oder sichere Entsorgung von Assets bei Eintrittsänderungen, Rollenwechseln, Austritten und externen Vertragsenden. Die Routine verbindet HR-/People-Ereignisse, Assetinventar, IT-Betrieb, Facility, Fachbereiche, Lieferantenmanagement und Evidence Review.

## Typische Risiken

- Wenn Laptops, Mobilgeräte oder Datenträger beim Austritt nicht zurückgegeben werden, können Informationen außerhalb der Kontrolle der Organisation verbleiben.
- Wenn Zutrittskarten, Schlüssel oder Token aktiv bleiben, kann unberechtigter physischer oder logischer Zugriff entstehen.
- Wenn Rollenwechsel nicht als Rückgabeereignis betrachtet werden, bleiben Spezialgeräte, Projektunterlagen oder erhöhte Berechtigungsmedien im falschen Bereich.
- Wenn Dienstleistergeräte oder Leihhardware nicht nachverfolgt werden, fehlen Verantwortlichkeit, Kostenkontrolle und Sicherheitsentscheidung.
- Wenn Rückgabe nur manuell über Erinnerung läuft, werden Abwesenheiten, kurzfristige Austritte oder dezentrale Standorte zu blinden Flecken.

## Trigger

- Austritt, Vertragsende, Kündigung, Ruhestand oder Ende externer Mitarbeit.
- Rollenwechsel, Teamwechsel, Standortwechsel oder Projektende.
- längere Abwesenheit mit erhöhtem Risiko oder unklarem Assetstatus.
- Verlustmeldung, Diebstahl, Beschädigung oder Verdacht auf Manipulation.
- Offboarding eines Dienstleisters, Lieferantenwechsel oder Ende eines Managed Service.
- Assetinventur, Auditfinding oder Abweichung zwischen HR-/Asset-/IT-Daten.
- Managemententscheidung zu Kosten, Ersatzbeschaffung oder Risikoakzeptanz.

## Rollen und Verantwortung

- **HR / People-Funktion:** meldet Wechsel- und Austrittsereignisse rechtzeitig und stößt Offboarding an.
- **Führungskraft / Prozess Owner:** bestätigt, welche projekt- oder rollenbezogenen Assets zurückzugeben sind.
- **Asset Owner / IT-Asset-Management:** führt Bestand, Zuordnung, Rückgabestatus und Wiederverwendung.
- **IT-Betrieb / Workplace-Team:** nimmt Geräte entgegen, sperrt, löscht, prüft und bereitet Neuverwendung oder Entsorgung vor.
- **Facility / Standortverantwortliche:** steuert Schlüssel, Zutrittskarten, Schließmedien und physische Gegenstände.
- **Einkauf / Lieferantenmanagement:** verfolgt externe Assets, Leihgeräte und vertragliche Rückgaben.
- **ISMS-Owner / Security-Rolle:** definiert Mindestanforderungen, Eskalation und Evidenzlogik.
- **Management:** entscheidet bei fehlenden Assets, Restrisiken, Kosten oder nicht durchsetzbaren Rückgaben.

## Implementierung

### Minimalstart

Ziel: Kritische Assets bei Wechsel oder Austritt nicht verlieren.

1. Die Organisation legt fest, welche Assettypen in den Rückgabeprozess fallen: Geräte, Datenträger, Zutrittsmittel, Unterlagen, Token, Spezialhardware.
2. Für neue Ausgaben wird mindestens Person, Asset, Datum und Owner dokumentiert.
3. HR- oder Führungskräfteereignisse lösen eine Rückgabecheckliste aus.
4. Kritische Assets werden vor oder spätestens zum Austrittstag geprüft.
5. Fehlende Assets werden als Ausnahme mit Risiko, Maßnahme und Wiedervorlage erfasst.
6. IT und Facility bestätigen Rückgabe, Sperrung, Löschung oder Verlustbehandlung.

Minimaler Nachweis:

- Assetliste oder Ausgaberegister,
- Offboarding- oder Wechselcheckliste,
- Rückgabebestätigung,
- Ticket für Sperrung/Löschung,
- Ausnahme- oder Verlustentscheidung.

### Solide Praxis

Ziel: Rückgabe wird als wiederholbare Offboarding- und Change-Routine betrieben.

1. Assetausgabe und Assetrückgabe sind mit Joiner-/Mover-/Leaver-Prozessen verbunden.
2. Assetklassen erhalten Mindesthandlungen: Rückgabe, Remote-Sperre, Datenlöschung, Wiederaufbereitung, Entsorgung, Ersatzforderung.
3. Führungskräfte prüfen projekt- und fachbereichsspezifische Gegenstände, nicht nur zentrale IT-Geräte.
4. Dienstleister und externe Mitarbeitende werden im selben Rückgabestatus geführt.
5. Offene Rückgaben werden eskaliert und nicht als erledigtes Offboarding geschlossen.
6. Stichproben vergleichen HR-Austritte, Assetregister, Zutrittsmedien und IT-Tickets.

Starke Evidenz:

- aktuelles Assetregister mit Zuordnung,
- Offboarding-Tickets mit Rückgabestatus,
- Bestätigung technischer Bereinigung oder Löschung,
- Facility-Nachweis zu Zutrittsmitteln,
- Ausnahmeentscheidungen mit Frist,
- Stichprobenprotokoll mit Korrekturen.

### Fortgeschritten

Ziel: Assetrückgabe ist in Identitäts-, Zutritts-, Beschaffungs- und Risikosteuerung integriert.

1. HR-System, Assetmanagement, IAM, MDM und Zutrittssysteme liefern abgestimmte Offboarding-Aufgaben.
2. Mobile Geräte können bei Verlust oder Nichtrückgabe risikobasiert gesperrt, lokalisiert oder gelöscht werden, soweit zulässig und geklärt.
3. Hochkritische Assets erhalten besondere Rückgabefristen und Nachweisanforderungen.
4. Ausnahmen fließen in Risiko-, Kosten- und Managementreporting ein.
5. Wiederkehrende Rückgabeprobleme führen zu Prozessverbesserungen bei Ausgabe, Inventarisierung oder Vertragsgestaltung.
6. Kennzahlen zeigen überfällige Rückgaben, nicht zuordenbare Assets, Verlustquoten und Bearbeitungszeiten.

## Ablauf als Routine

1. **Ereignis entsteht:** Wechsel, Austritt, Vertragsende, Projektende oder Verlustmeldung.
2. **Assetscope ermitteln:** zentrale Assetliste, Führungskraft, Projektowner, Facility und Dienstleisterstatus prüfen.
3. **Rückgabe planen:** Frist, Ort, Verantwortliche und Sonderfälle festlegen.
4. **Rückgabe durchführen:** physische Annahme, Versand, Abholung oder gesicherte Übergabe dokumentieren.
5. **Technisch behandeln:** Sperren, Daten sichern oder löschen, Geräte prüfen, Token deaktivieren, Wiederverwendung oder Entsorgung entscheiden.
6. **Status nachhalten:** vollständig, offen, verloren, beschädigt, Ausnahme oder Managemententscheidung.
7. **Eskalieren:** fehlende kritische Assets, sensible Daten, rechtliche Fragen oder Kostenkonflikte weitergeben.
8. **Verbessern:** Abweichungen in Assetausgabe, Inventar, Offboarding oder Verträgen korrigieren.

## Entscheidungen

- Welche Assettypen sind rückgabepflichtig und welche nur zu dokumentieren?
- Welche Rückgabefrist gilt für kritische Geräte, Zutrittsmittel oder Datenträger?
- Wann wird remote gesperrt oder gelöscht und welche Datenschutz-/Rechtsklärung ist nötig?
- Wer entscheidet bei Verlust, Beschädigung, Nichtrückgabe oder Kostenersatz?
- Wann ist ein Offboarding trotz fehlendem Asset abgeschlossen, wann bleibt ein Risiko offen?
- Welche externen Parteien müssen vertraglich zur Rückgabe oder Vernichtung verpflichtet werden?

## Evidenz

### Starke Evidenz

- Assetregister mit Person, Owner, Ausgabe- und Rückgabestatus,
- Offboarding-Ticket mit bestätigten Teilaufgaben,
- Nachweis der Geräteannahme oder Versandrückgabe,
- technische Sperr-, Lösch- oder Wiederaufbereitungsnachweise,
- Facility-Bestätigung zu Zutrittsmitteln,
- Ausnahme mit Risikoentscheidung, Frist und Wiedervorlage,
- Managemententscheidung bei kritischer Nichtrückgabe.

### Schwache Evidenz

- pauschale Austrittscheckliste ohne konkrete Assets,
- E-Mail „alles zurückgegeben“ ohne Assetbezug,
- veraltete Inventarliste ohne Zuordnung,
- mündliche Bestätigung der Führungskraft,
- Gerätefoto ohne Rückgabe-, Lösch- oder Sperrstatus.

### Evidenzlücken

- kein Abgleich zwischen HR-Austritten und Assetregister,
- externe Personen ohne Assetstatus,
- Zutrittsmittel außerhalb des Offboarding-Prozesses,
- Verlust ohne Risikoentscheidung,
- Gerätewiederverwendung ohne Bereinigungsnachweis.

## Wirksamkeitsprüfung

Prüffragen:

- Können alle kritischen Assets einer aktiven oder ehemaligen Person zugeordnet werden?
- Lösen Rollenwechsel und Projektenden Rückgabeprüfungen aus?
- Werden fehlende Assets risikobasiert behandelt und eskaliert?
- Ist technische Bereinigung vor Wiederverwendung nachweisbar?
- Werden externe Mitarbeitende und Dienstleister einbezogen?
- Führt die Routine zu Korrekturen im Assetregister?

Mögliche Kennzahlen:

- überfällige Rückgaben,
- offene Rückgaben nach Kritikalität,
- nicht zuordenbare Assets,
- Bearbeitungszeit vom Austritt bis Abschluss,
- Verlustquote je Assetklasse,
- Anteil Offboardings mit vollständigem Assetabgleich.

## BSIG-/NIS2-Anschluss

Assetrückgabe ist anschlussfähig an NIS2-orientierte Themen wie Risikomanagement, Zugriffsschutz, Cyberhygiene, Lieferkettensicherheit, physische Sicherheit und Aufrechterhaltung kontrollierter Betriebsumgebungen. Der konkrete Bezug sollte im Anforderungsregister und in den organisationsspezifischen Risikoentscheidungen geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Prüfung von arbeits-, eigentums-, datenschutz- oder vertragsrechtlichen Fragen.

## Grenzen

- Keine Rechts- oder Datenschutzberatung zu Herausgabe, Kostenersatz, Ortung oder Remote-Löschung.
- Keine Garantie, dass eine Rückgabeliste allein Sicherheit oder Konformität belegt.
- Keine technischen Vorgaben zur Geräteforensik, Datenlöschung oder Entsorgungstiefe.
- Keine ISO-27002-Texte oder Zertifizierungszusage.
- Keine echten Personen-, Kunden- oder Gerätedaten in öffentlichen Beispielen.

## Handoffs

- **HR-Handoff:** Austritt, Rollenwechsel, Vertragsende, Abwesenheit mit Rückgaberelevanz.
- **IT-/Workplace-Handoff:** Geräteannahme, Sperrung, MDM-Aktion, Datenlöschung, Wiederaufbereitung.
- **Facility-Handoff:** Schlüssel, Zutrittskarten, Schränke, Schließmedien, Standortgegenstände.
- **Legal-/Datenschutz-Handoff:** Remote-Löschung, Ortung, Streitfall, personenbezogene Daten, arbeits- oder vertragsrechtliche Fragen.
- **Lieferanten-Handoff:** externe Geräte, Leihhardware, Subdienstleister, Rückgabe- oder Vernichtungsnachweise.
- **Incident-Handoff:** Verdacht auf missbräuchliche Nutzung, fehlender Datenträger, kompromittiertes Gerät.
- **Management-Handoff:** kritische Nichtrückgabe, Kostenkonflikt, akzeptiertes Restrisiko.

## Typische Fehler

- Rückgabe wird nur beim Austritt, nicht beim Rollenwechsel geprüft.
- Assetregister und tatsächliche Ausgabe passen nicht zusammen.
- Zutrittsmittel und Token werden vergessen, weil IT nur Laptops betrachtet.
- Offboarding wird geschlossen, obwohl kritische Assets offen sind.
- Externe Mitarbeitende fallen durch das Raster.
- Geräte werden neu ausgegeben, ohne Bereinigung nachzuweisen.
- Verlust wird administrativ notiert, aber nicht risikobewertet.

## Fiktives Mini-Beispiel

Ein fiktiver Projektleiter wechselt in einen anderen Bereich. Die Führungskraft stößt einen Rollenwechsel-Check an. Das Assetregister zeigt einen Laptop, ein Testtelefon, eine Zutrittskarte für einen Projektraum und einen Hardware-Token. Das Testtelefon und der Projektraumzugang werden zurückgegeben, der Laptop bleibt wegen der neuen Rolle zugeordnet. Der Hardware-Token ist nicht auffindbar; IT sperrt ihn, dokumentiert den Verlust und der ISMS-Owner nimmt den Vorgang in die nächste Stichprobe auf.

Evidenz:

- Rollenwechsel-Ticket,
- Assetregister mit aktualisierter Zuordnung,
- Rückgabebestätigung für Testtelefon und Zutrittskarte,
- Sperrnachweis für Token,
- Ausnahme-/Verlustnotiz mit Reviewpunkt.
