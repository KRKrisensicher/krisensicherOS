
# A.7.2 — Physischer Zutritt

## Zweck

Physischer Zutritt steuert, wer Gebäude, Räume und Sicherheitsbereiche betreten darf — und wie Berechtigungen beantragt, vergeben, geprüft, entzogen und bei Auffälligkeiten behandelt werden. Entscheidend ist nicht das Türsystem allein, sondern die nachvollziehbare Verbindung aus Rolle, Bedarf, Freigabe, Ausweis/Schlüssel, Besucherlogik, Review und Entzug.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine für physischen Zutritt zu Standorten und geschützten Bereichen. Die Routine verbindet HR-Ereignisse, Facility, Asset Owner, Besuchermanagement, Dienstleisterzugänge, Protokollierung, Incident-Meldung und Managemententscheidungen.

## Typische Risiken

- Wenn Zutrittsrechte nach Austritt oder Rollenwechsel aktiv bleiben, können ehemalige oder unzuständige Personen geschützte Bereiche betreten.
- Wenn Schlüssel, Karten oder Codes nicht kontrolliert ausgegeben und zurückgenommen werden, entstehen nicht nachvollziehbare Zugänge.
- Wenn Besucher, Lieferanten oder Wartungsdienstleister unbeaufsichtigt Zugang erhalten, können Informationen eingesehen, Geräte manipuliert oder Betriebsabläufe gestört werden.
- Wenn Zutrittsrechte pauschal vergeben werden, passen physische Zugänge nicht zum tatsächlichen Arbeitsbedarf.
- Wenn Protokollierung oder Video ohne Klärung eingesetzt wird, entstehen Datenschutz- und Beschäftigtenthemen.

## Trigger

- Eintritt, Rollenwechsel, Standortwechsel, Projektwechsel oder Austritt.
- neuer Standort, neuer Sicherheitsbereich, Umbau oder Änderung des Schließ-/Zutrittssystems.
- Verlust von Ausweis, Schlüssel, Token oder Zutrittscode.
- Besuch, Wartung, Lieferung, Fremdfirma oder Notzugang.
- Sicherheitsereignis, unbefugter Zutrittsversuch, Tailgating, verdächtige Beobachtung oder Diebstahl.
- turnusmäßiger Zutrittsreview oder Standortbegehung.
- Lieferantenwechsel, Reinigungs-/Wachschutzänderung oder Vertragsende.

## Rollen und Verantwortung

- **Standort-/Facility Owner:** betreibt Zutrittssystem, Schlüssel-/Ausweisverwaltung, Besucherprozess und Standortregeln.
- **HR / People-Funktion:** liefert Eintritts-, Rollenwechsel-, Standortwechsel- und Austrittsereignisse.
- **Führungskraft / Bereichsverantwortliche:** bestätigt geschäftlichen Bedarf für Zutritt.
- **Asset Owner / Sicherheitsbereichs-Owner:** entscheidet über Zutritt zu kritischen Räumen oder Bereichen.
- **ISMS-Owner / Security-Rolle:** definiert Mindestlogik, Reviewanforderungen, Risikobezug und Eskalation.
- **Datenschutz / Legal:** prüft Zutrittslogs, Video, Besucherlisten, Wachschutz- und Beschäftigtendaten.
- **Management:** entscheidet bei kritischen Ausnahmen, Investitionen, Zielkonflikten und Restrisiken.

## Implementierung

### Minimalstart

Ziel: Zutritt zu kritischen Bereichen ist nachvollziehbar vergeben, überprüfbar und entziehbar.

1. Kritische Räume und Bereiche werden benannt und mit Ownern verbunden.
2. Zutritt wird nur mit nachvollziehbarer Freigabe vergeben: Person/Rolle, Bereich, Grund, Dauer, genehmigende Rolle.
3. Schlüssel, Karten, Codes oder Ausweise werden in einer einfachen Ausgabe- und Rückgabeliste geführt.
4. Austritt, Rollenwechsel, Verlust und Vertragsende lösen Entzug oder Sperrung aus.
5. Besucher und Wartungsdienstleister werden registriert und, wenn nötig, begleitet.
6. Ausnahmen und Notzugänge werden dokumentiert und nachträglich reviewed.

Minimaler Nachweis:

- Liste kritischer Bereiche und Owner,
- Zutrittsanträge oder Freigaben,
- Ausgabe-/Rückgabeliste für Ausweise, Schlüssel oder Codes,
- Besucher- oder Wartungsnachweise,
- Entzugs- oder Sperrnachweise,
- Ausnahme- oder Incident-Tickets.

### Solide Praxis

Ziel: Physischer Zutritt wird rollenbasiert, ereignisgetrieben und regelmäßig reviewed.

1. Zutrittsgruppen werden mit Rollen, Bereichen und Schutzbedarf verbunden.
2. Joiner-/Mover-/Leaver-Ereignisse aus HR werden mit Facility-Prozessen verknüpft.
3. Kritische Bereiche erhalten häufigere Reviews als allgemeine Büroflächen.
4. Besucher-, Lieferanten- und Wartungsprozesse definieren Anmeldung, Identitätsprüfung, Begleitung, Aufenthaltsbereich und Nachweis.
5. Verlorene Ausweise, Schlüssel oder Codes haben einen schnellen Sperr- und Austauschprozess.
6. Zutrittsauffälligkeiten werden an Security, Facility oder Incident Response übergeben.
7. Datenschutz und Legal prüfen Protokollierung, Video, Aufbewahrung und Einsichtsrechte.

### Fortgeschritten

Ziel: Zutrittssteuerung wird in Identitäts-, Facility-, Incident- und Risikosteuerung integriert.

1. HR-System, Zutrittssystem, Besuchermanagement und Sicherheitsbereichsregister sind organisatorisch oder technisch verbunden.
2. Zutrittsreviews nutzen Rollen-, Bereichs- und Risikoinformationen statt reiner Namenslisten.
3. Auffälligkeiten wie wiederholte Fehlversuche, Zutritt außerhalb üblicher Zeiten oder nicht zurückgegebene Ausweise werden risikobasiert geprüft.
4. Dienstleisterzugänge sind mit Verträgen, Leistungszeiten, Ansprechpartnern und Offboarding verbunden.
5. Management erhält Kennzahlen zu überfälligen Entzügen, offenen Ausweisen, kritischen Ausnahmen und Investitionsbedarf.

## Ablauf als Routine

1. **Zutrittsbedarf entsteht:** neue Person, neue Rolle, Besuch, Wartung, Projekt oder Notfall.
2. **Bereich und Schutzbedarf prüfen:** allgemeiner Standort, Sicherheitsbereich oder besonders kritischer Raum.
3. **Freigabe einholen:** Führungskraft, Facility oder Bereichs-/Asset Owner bestätigt Bedarf und Dauer.
4. **Zutritt ausgeben:** Ausweis, Schlüssel, Code oder Besucherausweis wird dokumentiert und erklärt.
5. **Nutzung betreiben:** Besucher werden begleitet, Dienstleister kontrolliert, Auffälligkeiten gemeldet.
6. **Änderung verarbeiten:** Rollenwechsel, Austritt, Verlust oder Vertragsende führen zu Sperrung, Rückgabe oder Codewechsel.
7. **Review durchführen:** Owner prüfen, ob Zutritte noch notwendig und angemessen sind.
8. **Abweichungen behandeln:** unklare Rechte, verlorene Medien, nicht zurückgegebene Schlüssel oder Auffälligkeiten werden eskaliert.
9. **Verbessern:** Findings führen zu geänderten Rollen, Prozessen, Systemen oder Schulung.

## Entscheidungen

- Welche Bereiche erfordern formale Zutrittsfreigabe und welche nicht?
- Wer darf Zutritt zu kritischen Bereichen genehmigen?
- Wie lange gelten Besucher-, Dienstleister- oder Projektzugänge?
- Welche Zutrittsereignisse werden protokolliert und wie wird Datenschutz geklärt?
- Wann reicht Begleitung, wann braucht es dauerhaften Zutritt?
- Welche Ausnahmen oder Notzugänge sind tolerierbar und wer reviewed sie?
- Wie werden physische Zutrittsrechte mit HR- und Vertragsende verknüpft?

## Evidenz

### Starke Evidenz

- aktuelle Bereichs- und Zutrittsgruppenliste mit Ownern,
- freigegebene Zutrittsanträge mit Grund und Dauer,
- Ausgabe-, Sperr- und Rückgabenachweise für Ausweise, Schlüssel oder Codes,
- Besucher- und Wartungslogs mit Begleitregel,
- Reviewprotokolle mit Entzugs- oder Korrekturentscheidungen,
- Incident- oder Auffälligkeitstickets,
- Datenschutz-/Legalreview für Protokollierung oder Video,
- Managemententscheidung bei dauerhaften Ausnahmen oder Investitionsbedarf.

### Schwache Evidenz

- Schlüsselbrett oder Kartenliste ohne Owner und Reviewdatum,
- allgemeine Hausordnung ohne konkrete Zutrittsfreigaben,
- Zutrittssystemexport ohne Rollen- oder Bereichsbezug,
- Besucherbuch ohne Auswertung oder Eskalationslogik,
- mündliche Freigaben für Dienstleisterzugänge.

### Evidenzlücken

- nicht zurückgegebene Schlüssel oder Ausweise ohne Nachverfolgung,
- Zutrittsrechte ehemaliger Beschäftigter oder Dienstleister,
- kritische Bereiche ohne gesonderten Review,
- Notzugänge ohne Protokoll oder Nachprüfung,
- Zutrittslogs oder Video ohne Datenschutzklärung,
- Codes, die geteilt werden und keinen Personenbezug mehr haben.

## Wirksamkeitsprüfung

Prüffragen:

- Können Zutrittsrechte zu kritischen Bereichen einer Rolle, Freigabe und Dauer zugeordnet werden?
- Werden Austritte, Rollenwechsel und Vertragsenden zeitnah verarbeitet?
- Sind Besucher und Wartungsdienstleister nachvollziehbar registriert und angemessen begleitet?
- Führt der Zutrittsreview zu Entzug oder Korrektur unnötiger Rechte?
- Werden verlorene Ausweise, Schlüssel oder Codes schnell gesperrt oder ersetzt?
- Sind Datenschutzfragen bei Protokollierung und Video geklärt?
- Werden Zutrittsauffälligkeiten als Sicherheitsereignisse behandelt?

Mögliche Kennzahlen:

- überfällige Zutrittsreviews,
- offene Rückgaben von Ausweisen oder Schlüsseln,
- Zeit bis Sperrung nach Austritt oder Verlust,
- Anzahl kritischer Ausnahmen oder Notzugänge,
- Findings aus Besucher- und Wartungsprozessen,
- Zutrittsrechte ohne klaren Owner oder Geschäftsbedarf.

## BSIG-/NIS2-Anschluss

Physischer Zutritt ist anschlussfähig an NIS2-orientierte Themen wie Risikomanagement, Schutz kritischer Betriebsumgebungen, Incident-Prävention, Lieferantensteuerung, Business Continuity und Cyberhygiene. Der konkrete Bezug zu Diensten, Standorten und Nachweisen sollte organisationsspezifisch geprüft werden.

Dieses Artefakt ersetzt keine rechtliche oder datenschutzrechtliche Bewertung von Zutrittsprotokollierung, Videoüberwachung, Beschäftigtendaten oder externen Meldepflichten.

## Grenzen

- Dieses Artefakt ist kein vollständiges Gebäudesicherheits- oder Schließanlagenkonzept.
- Es ersetzt keine Datenschutzprüfung für Zutrittslogs, Besucherlisten oder Video.
- Es bestätigt keine Konformität, Zertifizierungsfähigkeit oder physische Sicherheit allein durch ein Zutrittssystem.
- Es enthält keine ISO-27002-Texte und keine echten Standort-, Personen- oder Zutrittsdaten.
- Es ist nicht ausreichend, wenn Zutritte vergeben, aber nicht entzogen oder reviewed werden.

## Handoffs

- **HR-Handoff:** Eintritt, Rollenwechsel, Standortwechsel, Austritt, längere Abwesenheit.
- **Facility-Handoff:** Ausweis-/Schlüsselverwaltung, Schließsystem, Besucherprozess, Standortbegehung.
- **Asset-/Bereichs-Owner-Handoff:** Freigabe und Review für kritische Räume und Sicherheitsbereiche.
- **Datenschutz-/Legal-Handoff:** Zutrittslogs, Video, Besucherlisten, Aufbewahrung, Einsichtsrechte, Wachschutzverträge.
- **Vendor-Handoff:** Dienstleister-, Wartungs-, Reinigungs- oder Wachschutzzugänge und Vertragsende.
- **Incident-Handoff:** unbefugter Zutritt, verlorener Ausweis, Tailgating, Manipulation oder Diebstahl.
- **Management-Handoff:** Investitionsbedarf, dauerhaft nicht lösbare Zutrittslücken, akzeptierte Restrisiken.
- **Audit-/Evidence-Handoff:** fehlende Freigaben, unklare Zutrittsgruppen oder nicht nachvollziehbare Reviews.

## Typische Fehler

- Physischer Zutritt wird beim Eintritt vergeben, aber bei Rollenwechsel oder Austritt nicht bereinigt.
- Generalschlüssel oder Sammelcodes werden genutzt, ohne klare Verantwortung und Review.
- Dienstleister erhalten dauerhafte Zugänge, obwohl nur temporäre Einsätze stattfinden.
- Besucherprozesse existieren am Empfang, aber nicht für Nebeneingänge oder Lieferwege.
- Zutrittssystemexporte werden geprüft, ohne Bereichs- oder Geschäftsbedarf zu verstehen.
- Datenschutz wird erst betrachtet, nachdem Protokollierung oder Video schon produktiv genutzt wird.
- Notzugänge bleiben nach dem Notfall bestehen.

## Fiktives Mini-Beispiel

Ein fiktiver Bürostandort führt einen separaten Zutritt für den Serverraum ein. Der IT-Owner genehmigt Zutritt nur für zwei Administratoren und Facility für Wartungsfälle. Beim quartalsweisen Review fällt auf, dass ein ehemaliger Dienstleister noch eine aktive Karte besitzt. Facility sperrt die Karte, dokumentiert die Korrektur und ergänzt den Lieferanten-Offboarding-Check. Datenschutz prüft parallel die Aufbewahrung der Zutrittsprotokolle.

Evidenz:

- Serverraum-Zutrittsgruppe mit Owner,
- Freigaben für berechtigte Rollen,
- Reviewprotokoll mit Finding,
- Sperrnachweis für Dienstleisterkarte,
- aktualisierter Offboarding-Check,
- Datenschutzreview zur Protokollaufbewahrung.
