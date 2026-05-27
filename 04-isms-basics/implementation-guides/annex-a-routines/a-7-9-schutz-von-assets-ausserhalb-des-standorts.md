
# A.7.9 — Schutz von Assets außerhalb des Standorts

## Zweck

Assets außerhalb des Standorts — etwa Laptops, mobile Datenträger, Ersatzgeräte, Projekttechnik, Unterlagen, Testgeräte oder Geräte bei Dienstleistern — verlassen die kontrollierte Umgebung der Organisation. Diese Routine sorgt dafür, dass solche Assets nicht unsichtbar werden, sondern mit Owner, Schutzbedarf, Nutzungskontext, Rückgabe- oder Löschlogik und Evidenz gesteuert werden.

Der Kern ist nicht „Homeoffice erlaubt“, sondern die Frage: Welche Assets dürfen wohin, unter welchen Bedingungen, mit welchem Schutz und wie erkennt die Organisation Verlust, Missbrauch oder vergessene Rückgaben?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Routine für Assets außerhalb eigener Standorte. Sie verbindet Assetinventar, Freigabe, technische und organisatorische Schutzmaßnahmen, Nutzungsregeln, Verlustmeldung, Rückgabe und Review.

## Typische Risiken

- Wenn mobile Geräte ohne Verschlüsselung, Sperre oder Inventarbezug genutzt werden, kann Verlust zu Informationsabfluss und Betriebsunterbrechung führen.
- Wenn Unterlagen, Speichermedien oder Ersatzgeräte außerhalb des Standorts nicht erfasst werden, fehlen Rückgabe, Löschung und Verantwortlichkeit.
- Wenn Beschäftigte oder Dienstleister Assets informell mitnehmen, bleiben Schutzbedarf und Nutzungskontext ungeklärt.
- Wenn Assets in Fahrzeugen, Hotels, Veranstaltungen oder privaten Umgebungen unbeaufsichtigt bleiben, steigt Diebstahl- und Einsichtsrisiko.
- Wenn Rückgabe bei Rollenwechsel, Austritt oder Projektende nicht geprüft wird, bleiben Geräte, Daten oder Zugänge außerhalb der Kontrolle.
- Wenn Verlustmeldungen unklar sind, werden Incident Response, Datenschutzprüfung und Ersatzmaßnahmen verzögert.

## Trigger

- Ausgabe, Mitnahme oder Versand eines Assets außerhalb eines kontrollierten Standorts.
- Homeoffice, mobiles Arbeiten, Reise, Veranstaltung, Kundenprojekt oder Außendienst.
- Bereitstellung von Ersatzgeräten, Testgeräten oder Leihhardware.
- Dienstleisterzugriff, Reparatur, Wartung oder Rücksendung.
- Rollenwechsel, Austritt, Projektende oder Vertragsende.
- Verlust, Diebstahl, Beschädigung, Manipulationsverdacht oder verspätete Rückgabe.
- turnusmäßige Inventur oder Review mobiler und externer Assets.

## Rollen und Verantwortung

- **Asset Owner / Service Owner:** legt Schutzbedarf, zulässige Nutzung und Rückgabeanforderungen fest.
- **IT-/Endpoint Owner:** stellt technische Schutzmaßnahmen, Verwaltung, Sperrung, Löschung und Nachverfolgung bereit.
- **Nutzende Person / Fachbereich:** schützt das Asset im Alltag, meldet Verlust oder Abweichung und hält Rückgaberegeln ein.
- **Führungskraft / Projekt Owner:** bestätigt geschäftlichen Bedarf und sorgt für Rückgabe bei Rollen- oder Projektende.
- **ISMS-Owner / Security-Rolle:** definiert Mindestschutz, Ausnahmebehandlung, Review und Eskalationslogik.
- **HR / People-Funktion:** löst Rückgabe- und Zugriffsprüfung bei Austritt oder Rollenwechsel aus.
- **Einkauf / Lieferantenmanagement:** steuert Assets bei Dienstleistern, Reparaturen, Versand und Vertragsende.
- **Datenschutz / Legal:** prüft personenbezogene Daten, Verlustfolgen, Vertrags- und Meldepflichtfragen im Human Review.

## Implementierung

### Minimalstart

Ziel: Mobile und externe Assets sind sichtbar, geschützt und rückholbar.

1. Die Organisation benennt Assettypen, die außerhalb des Standorts genutzt werden dürfen: Laptops, Smartphones, Datenträger, Unterlagen, Testgeräte, Schlüssel, Token oder Ersatzhardware.
2. Für diese Assettypen werden Owner und Mindestschutz festgelegt: Inventareintrag, Bildschirmsperre, Verschlüsselung, sichere Aufbewahrung, Verlustmeldung, Rückgabe.
3. Ausgabe oder Mitnahme wird nachvollziehbar dokumentiert.
4. Austritt, Rollenwechsel und Projektende lösen eine Rückgabeprüfung aus.
5. Verlust oder Diebstahl löst einen Incident- und Datenschutz-/Legal-Handoff nach definierter Schwelle aus.
6. Ausnahmen werden befristet und mit Begründung dokumentiert.

Minimaler Nachweis:

- Assetliste oder Ausgabeprotokoll mit Owner,
- Mindestschutzregel für externe Nutzung,
- Rückgabenachweis oder Offboarding-Check,
- Verlust-/Incident-Ticket bei Abweichung,
- Ausnahme mit Frist.

### Solide Praxis

Ziel: Externe Assetnutzung wird risikobasiert und wiederholbar gesteuert.

1. Assets werden nach Datenklasse, Gerätekontrolle, Standorttyp und Nutzergruppe klassifiziert.
2. Technische Baselines für mobile Geräte werden betrieben: Verschlüsselung, Gerätesperre, Patchstand, Remote-Sperre oder -Löschung, zentrale Verwaltung, Backup- oder Sync-Regel.
3. Papierunterlagen, Datenträger und Spezialgeräte erhalten eigene Transport-, Aufbewahrungs- und Rückgaberegeln.
4. Dienstleister, Reparaturen und Versand werden über Tickets, Lieferscheine oder Vertragskontakte nachverfolgt.
5. Regelmäßige Inventur gleicht ausgegebene Assets mit Personen, Projekten und Dienstleistern ab.
6. Nicht zurückgegebene oder nicht erreichbare Assets werden eskaliert.
7. Lessons Learned aus Verlusten fließen in Schulung, Endpoint-Management oder Reise-/Homeoffice-Regeln ein.

Starke Evidenz:

- Assetinventar mit externer Nutzung, Person/Projekt und Owner,
- technische Compliance-Auswertung mobiler Geräte,
- Ausgabe-, Versand-, Reparatur- oder Rückgabeprotokolle,
- Offboarding-Checklisten mit Assetrückgabe,
- Incident- und Lessons-Learned-Nachweise,
- Ausnahme- und Risikoentscheidungen.

### Fortgeschritten

Ziel: Externe Assets werden mit Identitäts-, Endpoint-, Lieferanten- und Incident-Prozessen integriert.

1. Assetinventar, MDM/Endpoint-Management, HR-Ereignisse und Ticketing sind verbunden.
2. Nicht konforme, lange offline befindliche oder vermisste Geräte erzeugen Alerts.
3. Mobile Nutzung wird mit Datenklassifizierung, Conditional Access, Backup, DLP oder Remote-Wipe-Fähigkeit gekoppelt.
4. Dienstleister-Assets und Reparaturwege werden mit Vertrags- und Lieferantenreviews abgeglichen.
5. Management erhält Kennzahlen zu fehlenden Assets, Non-Compliance, Verlusten, Rückgabezeiten und Ausnahmequoten.
6. Szenarien wie Messe, Außendienst, Notfallarbeit oder Krisenbetrieb werden mit BCM und Incident Response geübt.

## Ablauf als Routine

1. **Externe Nutzung entsteht:** Ausgabe, Mitnahme, Versand, Reparatur, Projekt- oder Reisebedarf.
2. **Schutzbedarf klären:** Assettyp, Datenklasse, Kritikalität, Nutzergruppe und Zielort bewerten.
3. **Freigeben:** fachlicher Bedarf und Mindestschutz werden bestätigt.
4. **Ausgeben oder versenden:** Inventar, Verantwortlichkeit, Rückgabedatum und Schutzanforderungen dokumentieren.
5. **Betreiben:** technische Compliance, Nutzungsregeln und Verlustmeldeweg sicherstellen.
6. **Abweichung behandeln:** Verlust, Diebstahl, verspätete Rückgabe oder Non-Compliance als Ticket/Incident bearbeiten.
7. **Zurückgeben oder löschen:** Rückgabe, sichere Löschung, Entzug von Zugriffen und Inventaraktualisierung nachweisen.
8. **Reviewen:** Inventur, Musteranalyse und Maßnahmen im ISMS-Review behandeln.

## Entscheidungen

- Welche Assettypen dürfen außerhalb kontrollierter Standorte genutzt werden?
- Welche Datenklassen dürfen auf mobilen oder externen Assets verarbeitet werden?
- Welche Mindestschutzmaßnahmen sind Pflicht, bevor ein Asset ausgegeben wird?
- Wann ist externe Nutzung zu riskant und braucht Managemententscheidung?
- Wer darf Ausnahmen genehmigen und wie lange?
- Welche Verlust- oder Diebstahlszenarien lösen Incident-, Legal- oder Datenschutz-Handoff aus?
- Wie werden Assets bei Dienstleistern, Reparaturen und Versand nachverfolgt?

## Evidenz

### Starke Evidenz

- aktuelles Assetinventar mit externer Zuordnung,
- Ausgabe- und Rückgabenachweise,
- technische Compliance-Berichte für mobile Geräte,
- Offboarding- oder Projektabschlussnachweise,
- Verlust-/Diebstahl-Tickets mit Entscheidungen,
- Versand-, Reparatur- oder Dienstleisterprotokolle,
- befristete Ausnahmen mit Reviewdatum,
- Managemententscheidung bei nicht rückholbaren oder risikoreichen Assets.

### Schwache Evidenz

- allgemeine Homeoffice-Regel ohne Assetbezug,
- Inventarliste ohne Person, Projekt oder Rückgabestatus,
- Gerätescreenshot ohne Datum oder Compliance-Kontext,
- mündliche Zusage, dass Geräte verschlüsselt sind,
- Verlustmeldung ohne Folgeentscheidung.

### Evidenzlücken

- ausgegebene Assets ohne Owner,
- externe Nutzung ohne Freigabe oder Schutzbedarf,
- Rückgabe bei Austritt nicht nachweisbar,
- nicht konforme Geräte ohne Eskalation,
- Reparatur oder Versand ohne Nachverfolgung,
- Datenträger oder Papierunterlagen außerhalb des Standorts ohne Regel.

## Wirksamkeitsprüfung

Prüffragen:

- Ist für externe Assets nachvollziehbar, wer sie nutzt, warum und bis wann?
- Sind mobile Geräte technisch geschützt und prüfbar verwaltet?
- Werden Austritte, Rollenwechsel und Projektenden mit Rückgabe verknüpft?
- Werden Verlust und Diebstahl schnell genug gemeldet und behandelt?
- Sind Dienstleister-, Reparatur- und Versandwege sichtbar?
- Führen Inventurfindings zu Maßnahmen oder Managemententscheidungen?

Mögliche Kennzahlen:

- Anteil externer Assets mit Owner und Rückgabestatus,
- Anzahl überfälliger Rückgaben,
- Geräte außerhalb technischer Compliance,
- Zeit von Verlustmeldung bis Sperr-/Löschentscheidung,
- offene Ausnahmen und überfällige Wiedervorlagen,
- Inventurdifferenzen je Assetklasse.

## BSIG-/NIS2-Anschluss

Der Schutz von Assets außerhalb des Standorts ist anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Cyberhygiene, Zugriffsschutz, Incident-Fähigkeit, Lieferkettensicherheit und Business Continuity. Der konkrete Bezug sollte im Anforderungsregister, in Risikoanalysen und in Offboarding-/Assetprozessen geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung von Meldepflichten, Datenschutzfolgen oder Anwendbarkeit.

## Grenzen

- Dieses Artefakt ist keine vollständige Mobile-Device-Management-Architektur.
- Es ersetzt keine Datenschutzprüfung bei Verlust personenbezogener Daten.
- Es ersetzt keine arbeitsrechtliche, versicherungsrechtliche oder vertragliche Bewertung.
- Es trifft keine Zertifizierungs- oder Konformitätszusage.
- Öffentliche Beispiele dürfen keine echten Personen-, Geräte- oder Standortdaten enthalten.

## Handoffs

- **HR-Handoff:** Austritt, Rollenwechsel, längere Abwesenheit oder Rückgabeeskalation.
- **IT-/Endpoint-Handoff:** Verschlüsselung, Sperrung, Löschung, Compliance, Backup und Geräteaustausch.
- **Incident-Handoff:** Verlust, Diebstahl, Manipulationsverdacht, nicht autorisierte Nutzung oder nicht erreichbares Gerät.
- **Datenschutz-/Legal-Handoff:** mögliche Offenlegung personenbezogener Daten, Vertragsfragen, Meldepflichtprüfung oder arbeitsrechtliche Aspekte.
- **Einkauf-/Lieferanten-Handoff:** Reparatur, Versand, Dienstleistergeräte, Leihgeräte oder Vertragsende.
- **BCM-Handoff:** externe Assets sind für Notfallarbeit oder kritische Betriebsfähigkeit erforderlich.
- **Management-Handoff:** nicht rückholbare Assets, hohe Ausnahmequote, Investitionsbedarf oder akzeptiertes Restrisiko.
- **Audit-/Evidence-Handoff:** unklare Inventardaten, fehlende Rückgabenachweise oder lückenhafte Verlustbearbeitung.

## Typische Fehler

- Laptops werden inventarisiert, aber Papierunterlagen, Datenträger und Spezialgeräte vergessen.
- Homeoffice-Regeln ersetzen keine Asset- und Rückgaberoutine.
- Offboarding prüft Zugänge, aber nicht Geräte, Token, Schlüssel oder Unterlagen.
- Verlustmeldungen erreichen IT, aber nicht Incident Response oder Datenschutzprüfung.
- Reparaturen und Versand laufen informell über Einzelpersonen.
- Technische Geräteschutzmaßnahmen sind vorhanden, aber nicht überprüfbar.
- Ausnahmen für Projektgeräte laufen unbegrenzt weiter.

## Fiktives Mini-Beispiel

Ein fiktives Beratungsteam gibt für ein Kundenprojekt fünf Laptops und zwei Testgeräte aus. Das Projektticket enthält Assetnummern, Nutzer, Rückgabedatum und Mindestschutz. Beim Projektabschluss fehlt ein Testgerät. Der Projekt Owner meldet die Abweichung, IT sperrt zugehörige Zugänge und das Management entscheidet, ob Ersatzbeschaffung und Risikoakzeptanz erforderlich sind. Die Rückgabeprüfung wird anschließend in die Projektabschluss-Checkliste aufgenommen.

Evidenz:

- Projektticket mit Assetzuordnung,
- technische Compliance-Auswertung der Laptops,
- Rückgabeprotokoll,
- Abweichungsticket zum fehlenden Testgerät,
- Managemententscheidung und aktualisierte Abschluss-Checkliste.
