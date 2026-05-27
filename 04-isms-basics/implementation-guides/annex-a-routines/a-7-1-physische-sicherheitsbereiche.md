
# A.7.1 — Physische Sicherheitsbereiche

## Zweck

Physische Sicherheitsbereiche sorgen dafür, dass besonders schutzbedürftige Räume, Zonen und Standorte nicht wie normale Büroflächen behandelt werden. Ziel ist eine nachvollziehbare Abgrenzung: Wo befinden sich kritische Informationen, Systeme oder Betriebsprozesse, wer trägt Verantwortung, welche Schutzlogik gilt und wie wird sie überprüft?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der physische Bereiche nach Schutzbedarf eingeordnet, abgegrenzt, verantwortet, dokumentiert und reviewed werden. Die Routine verbindet Standort, Assetkritikalität, Zutritt, Besuchermanagement, Facility-Prozesse, Incident-Meldung, BCM und Managemententscheidungen.

## Typische Risiken

- Wenn Serverräume, Archive, Leitstände oder Technikflächen nicht klar abgegrenzt sind, können unbefugte Personen Informationen einsehen, Geräte manipulieren oder Betriebsstörungen verursachen.
- Wenn Schutzbereiche nicht mit Asset- und Prozesskritikalität verbunden sind, werden kritische Räume zu schwach oder unwichtige Flächen zu aufwendig geschützt.
- Wenn bauliche, organisatorische und technische Maßnahmen nicht zusammenpassen, entstehen Lücken trotz vorhandener Türen, Karten oder Kameras.
- Wenn Umzüge, Umbauten oder neue Nutzungskonzepte nicht geprüft werden, verändert sich der Schutzbedarf unbemerkt.
- Wenn Facility und ISMS getrennt arbeiten, fehlen Nachweise, Reviews und Entscheidungen zu Restrisiken.

## Trigger

- neuer Standort, Umzug, Umbau, Flächenänderung oder Nutzungsänderung.
- Einrichtung oder Änderung von Serverraum, Archiv, Labor, Leitstand, Lager, Netzwerktechnik oder Krisenraum.
- neue kritische Assets, höherer Schutzbedarf oder geänderte Betriebsabhängigkeit.
- Sicherheitsereignis, Zutrittsauffälligkeit, Manipulationsverdacht oder Facility-Finding.
- Wechsel von Vermieter, Gebäudedienstleister, Wachschutz oder Wartungsdienstleister.
- BCM-Review, Risikoanalyse, interne Prüfung oder Managemententscheidung.
- turnusmäßiger Standort- oder Sicherheitsbereichsreview.

## Rollen und Verantwortung

- **Standort-/Facility Owner:** verantwortet Flächen, bauliche Maßnahmen, Dienstleisterkoordination und Standortnachweise.
- **Asset Owner / Service Owner:** benennt kritische Systeme, Informationen und Prozesse im Bereich.
- **ISMS-Owner / Security-Rolle:** definiert Schutzlogik, Reviewanforderungen, Risikobezug und Eskalation.
- **IT-/Betriebsrolle:** bewertet Technikräume, Netzwerkinfrastruktur, Server, Medien und Betriebsabhängigkeiten.
- **Führungskräfte / Bereichsverantwortliche:** stellen Alltagstauglichkeit und Regelumsetzung sicher.
- **Datenschutz / Legal:** prüfen Video, Zutrittsprotokolle, Miet-/Dienstleisterfragen und personenbezogene Daten.
- **Management:** entscheidet über Investitionen, Restrisiken, Ausnahmen und Standortprioritäten.

## Implementierung

### Minimalstart

Ziel: Kritische physische Bereiche sind bekannt, einem Owner zugeordnet und mit Mindestschutz versehen.

1. Die Organisation listet physische Bereiche im ISMS-Scope, in denen kritische Informationen, Systeme oder Prozesse liegen.
2. Für jeden Bereich wird ein Owner benannt und der Zweck beschrieben.
3. Mindestregeln werden festgelegt: wer darf hinein, wie werden Besucher begleitet, wie werden Türen/Schränke gesichert, wie werden Auffälligkeiten gemeldet.
4. Der Bezug zu Assetliste, Risikoanalyse oder BCM-Priorität wird dokumentiert.
5. Ausnahmen oder bauliche Schwächen werden mit Risikoentscheidung und Wiedervorlage geführt.
6. Mindestens jährlich oder bei Änderung wird geprüft, ob Bereich, Schutzbedarf und Nutzung noch zusammenpassen.

Minimaler Nachweis:

- Liste physischer Sicherheitsbereiche mit Ownern,
- Bereichsbeschreibung mit Schutzbedarf,
- einfache Zutritts- und Besucherregel,
- Standort- oder Reviewprotokoll,
- Maßnahmen- oder Ausnahmelog.

### Solide Praxis

Ziel: Schutzbereiche werden risikobasiert und standortübergreifend konsistent gesteuert.

1. Bereiche werden nach Schutzbedarf oder Kritikalität klassifiziert, ohne unnötige Komplexität aufzubauen.
2. Schutzmaßnahmen werden je Bereich dokumentiert: bauliche Abgrenzung, Zutrittssteuerung, Besucherbegleitung, Schließkonzept, Umwelt- und Betriebsrisiken, Meldewege.
3. Facility-, IT-, Security- und BCM-Reviews werden aufeinander abgestimmt.
4. Änderungen an Flächen, Nutzung, Dienstleistern oder kritischen Assets lösen einen Sicherheitsbereichsreview aus.
5. Findings aus Begehungen, Incidents oder Wartungen werden als Maßnahmen mit Owner und Frist verfolgt.
6. Datenschutz und Legal werden einbezogen, wenn Protokollierung, Video, Wachschutz oder Vermieterzugänge betroffen sind.

### Fortgeschritten

Ziel: Physische Sicherheitsbereiche sind in Risiko-, BCM-, Zutritts- und Facility-Steuerung integriert.

1. Bereichsinventar, Assetinventar, Zutrittsgruppen, Wartungspläne und Risikoregister sind miteinander verbunden.
2. Kritische Bereiche erhalten risikobasierte Reviewfrequenzen und Szenariobetrachtungen: Ausfall, Sabotage, Wasserschaden, Feuer, Strom, unbefugter Zutritt.
3. Zutrittsereignisse, Facility-Findings und Wartungsaktivitäten werden regelmäßig auf Muster geprüft.
4. Bau- und Umzugsprojekte enthalten frühzeitig einen Security-/BCM-Check.
5. Management erhält entscheidungsfähige Informationen zu Standortlücken, Investitionsbedarf, kritischen Ausnahmen und Betriebsabhängigkeiten.

## Ablauf als Routine

1. **Bereich identifizieren:** Standort, Raum oder Zone enthält kritische Assets, Informationen oder Betriebsprozesse.
2. **Schutzbedarf einordnen:** Asset Owner, Facility und ISMS bewerten Kritikalität, Bedrohungen und Abhängigkeiten.
3. **Bereich abgrenzen:** physische Grenze, Verantwortliche, erlaubte Rollen und Besucherlogik werden beschrieben.
4. **Maßnahmen festlegen:** Zutritt, Begleitung, Schließung, Kennzeichnung, Wartung, Monitoring und Meldeweg werden angemessen definiert.
5. **Nachweis erfassen:** Bereichsinventar, Skizze oder Beschreibung, Owner, Risiken, Maßnahmen und Ausnahmen werden abgelegt.
6. **Betrieb prüfen:** Begehung, Review, Zutrittsprüfung oder Facility-Check bewertet den Zustand.
7. **Abweichungen behandeln:** bauliche Lücken, Nutzungsänderungen oder unklare Zutritte werden als Maßnahmen verfolgt.
8. **Eskalieren:** nicht tragbare Restrisiken, Investitionen oder Standortentscheidungen gehen ins Management Review.

## Entscheidungen

- Welche Räume oder Zonen sind physische Sicherheitsbereiche?
- Welche Schutzstufe ist für welchen Bereich angemessen?
- Wer darf regelmäßig hinein, wer nur begleitet und wer gar nicht?
- Welche baulichen oder organisatorischen Lücken werden akzeptiert, kompensiert oder priorisiert behoben?
- Wie werden Vermieter, Reinigung, Wartung und externe Dienstleister eingebunden?
- Welche Standort- oder BCM-Risiken erfordern Managemententscheidung?

## Evidenz

### Starke Evidenz

- aktuelles Register physischer Sicherheitsbereiche mit Ownern,
- Schutzbedarfs- oder Kritikalitätsbezug je Bereich,
- dokumentierte Zutritts- und Besucherlogik,
- Begehungs- oder Reviewprotokolle mit Findings,
- Maßnahmenlog mit Owner, Frist und Status,
- Risiko- oder Ausnahmeentscheidung bei baulichen Lücken,
- Managemententscheidung zu Investitionen oder Restrisiken.

### Schwache Evidenz

- Gebäudeplan ohne Schutzbedarf oder Owner,
- allgemeine Hausordnung ohne kritische Bereiche,
- Türschloss oder Karte als Nachweis ohne Reviewlogik,
- veraltete Raumliste nach Umzug oder Umbau,
- pauschale Aussage „Facility kümmert sich“ ohne ISMS-Bezug.

### Evidenzlücken

- Server-, Technik- oder Archivräume ohne Owner,
- Besucher- oder Wartungszugänge nicht geregelt,
- keine Verbindung zu Assetkritikalität oder BCM,
- bauliche Schwächen ohne Risikoentscheidung,
- keine Reviews nach Umzug, Umbau oder Nutzungsänderung,
- personenbezogene Zutritts- oder Videodaten ohne Klärung.

## Wirksamkeitsprüfung

Prüffragen:

- Sind alle kritischen physischen Bereiche im Scope bekannt und einem Owner zugeordnet?
- Passt der Schutzbereich zur Kritikalität der enthaltenen Assets und Prozesse?
- Sind Besucher, Wartung und externe Dienstleister nachvollziehbar geregelt?
- Haben Begehungen oder Reviews zu Maßnahmen geführt?
- Werden Umbauten, Umzüge und Nutzungsänderungen frühzeitig geprüft?
- Sind Ausnahmen befristet und mit Risikoentscheidung versehen?
- Erkennt Management Standortlücken und Investitionsbedarf?

Mögliche Kennzahlen:

- Anteil kritischer Bereiche mit aktuellem Review,
- offene Findings aus Standortbegehungen,
- überfällige Maßnahmen zu baulichen oder organisatorischen Lücken,
- Anzahl nicht geregelter Dienstleisterzugänge,
- Ausnahmen je Standort oder Bereich,
- Zeit bis Review nach Umbau oder Nutzungsänderung.

## BSIG-/NIS2-Anschluss

Physische Sicherheitsbereiche sind anschlussfähig an NIS2-orientierte Themen wie Schutz kritischer Betriebsumgebungen, Risikomanagement, Business Continuity, Lieferantensteuerung und Incident-Prävention. Der konkrete Bezug zu Diensten, Standorten und Nachweisen sollte organisationsspezifisch im Anforderungsregister und in Risikoanalysen geprüft werden.

Dieses Artefakt ersetzt keine baurechtliche, arbeitsschutzrechtliche, datenschutzrechtliche oder sonstige rechtliche Bewertung.

## Grenzen

- Dieses Artefakt ist kein bauliches Sicherheitskonzept und keine Planungsvorgabe für Gebäudetechnik.
- Es ersetzt keine Datenschutzprüfung für Video, Zutrittslogs oder Wachschutz.
- Es bestätigt keine Konformität, Zertifizierungsfähigkeit oder physische Sicherheit allein durch Bereichsdefinitionen.
- Es enthält keine ISO-27002-Texte und keine echten Standortpläne oder vertraulichen Gebäudedaten.
- Es ist nicht ausreichend, wenn Schutzbereiche definiert, aber nicht betrieben oder reviewed werden.

## Handoffs

- **Facility-Handoff:** bauliche Abgrenzung, Schließsysteme, Wartung, Dienstleisterkoordination, Standortbegehung.
- **Asset-/IT-Handoff:** kritische Systeme, Netzwerktechnik, Serverräume, technische Betriebsabhängigkeiten.
- **BCM-Handoff:** Ausfall von Räumen, Ausweichstandorte, Notbetrieb, Standortresilienz.
- **Datenschutz-/Legal-Handoff:** Video, Zutrittsprotokolle, Wachschutz, Vermieterrechte, personenbezogene Daten.
- **Incident-Handoff:** Manipulationsverdacht, unbefugter Zutritt, Diebstahl, Sabotage oder verdächtige Beobachtung.
- **Management-Handoff:** Investitionsbedarf, Standortrestrisiken, dauerhafte Ausnahmen oder strategische Standortentscheidung.
- **Audit-/Evidence-Handoff:** fehlende Bereichsliste, unklare Owner, nicht nachvollziehbare Reviews.

## Typische Fehler

- Physische Sicherheit wird nur als Facility-Thema behandelt und nicht mit Informationsrisiken verbunden.
- Serverräume, Archive oder Technikflächen sind bekannt, aber nicht als Schutzbereiche geführt.
- Besucher- und Wartungszugänge werden informell geregelt.
- Nach Umbauten bleibt die alte Schutzbereichslogik bestehen.
- Video oder Zutrittslogs werden genutzt, ohne Datenschutz-Handoff auszulösen.
- Findings aus Begehungen werden nicht als Maßnahmen verfolgt.
- Management sieht Kosten, aber nicht die damit verbundenen Betriebsrisiken.

## Fiktives Mini-Beispiel

Ein fiktiver Produktionsbetrieb richtet einen neuen Netzwerktechnikraum ein. Der IT-Owner meldet den Raum an das ISMS, Facility ergänzt ihn in das Bereichsregister und definiert Zutritt nur für IT, Facility und begleitete Wartungsdienstleister. Bei einer Begehung fällt auf, dass Reinigungskräfte unbeaufsichtigten Zugang hätten. Facility ändert den Reinigungsplan, und das Management genehmigt eine Nachrüstung am Schließsystem.

Evidenz:

- Bereichsregister mit Owner und Zweck,
- Schutzbedarfsbezug zur Netzwerkinfrastruktur,
- dokumentierte Zutritts- und Besucherregel,
- Begehungsfinding,
- Maßnahme zum Reinigungsprozess,
- Managemententscheidung zur Nachrüstung.
