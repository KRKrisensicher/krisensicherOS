
# A.7.6 — Arbeiten in geschützten Bereichen

## Zweck

Geschützte Bereiche verlieren ihren Wert, wenn Arbeiten darin ungeplant, unbeaufsichtigt oder ohne klare Regeln stattfinden. Diese Routine sorgt dafür, dass Tätigkeiten in Serverräumen, Archiven, Technikflächen, Laboren, Sicherheitszonen oder anderen schutzbedürftigen Bereichen kontrolliert vorbereitet, durchgeführt, dokumentiert und nachbereitet werden.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Arbeitsroutine für geschützte Bereiche, die Zutrittsberechtigung, Arbeitsauftrag, Begleitung, Verhaltensregeln, mitgebrachte Geräte, Nachweisführung, Ausnahmebehandlung und Handoffs an Facility, IT, Datenschutz, Incident Response und Management verbindet.

## Typische Risiken

- Wenn Wartung, Reinigung oder Lieferungen in geschützten Bereichen ohne Auftrag und Begleitung stattfinden, können Systeme, Informationen oder Datenträger unbeabsichtigt gefährdet werden.
- Wenn Arbeiten nicht dokumentiert werden, sind spätere Störungen, Manipulationen oder Verluste nicht nachvollziehbar.
- Wenn Werkzeuge, mobile Geräte oder Kameras unkontrolliert eingebracht werden, entstehen Abfluss-, Manipulations- oder Verwechslungsrisiken.
- Wenn Notfallzugänge informell genutzt werden, werden Schutzregeln im Alltag umgangen.
- Wenn Verhaltensregeln nicht rollenbezogen erklärt sind, treffen Mitarbeitende und Dienstleister vor Ort unsichere Ad-hoc-Entscheidungen.

## Trigger

- geplanter Zutritt zu Serverraum, Technikbereich, Archiv, Labor, Sicherheitszone oder sonstigem geschützten Bereich.
- Wartung, Reinigung, Reparatur, Lieferung, Inventur, Umbau, Auditbegehung oder Notfallmaßnahme.
- neuer Dienstleister, neue Tätigkeit oder geänderte Arbeitsanweisung.
- Störung, Alarm, unbegleiteter Zutritt, fehlende Dokumentation oder Verdacht auf Regelverstoß.
- Änderung von Schutzbedarf, Raumklassifizierung oder Zutrittsberechtigung.
- turnusmäßiger Review von Arbeitsregeln, Besucher-/Dienstleisterzugängen oder Zutrittsprotokollen.

## Rollen und Verantwortung

- **Bereichs-/Raum Owner:** entscheidet, welche Arbeiten zulässig sind und welche Regeln im Bereich gelten.
- **Auftraggeber / Service Owner:** beschreibt Zweck, Zeitraum, Umfang und erwartetes Ergebnis der Arbeit.
- **Facility / Office Management:** koordiniert Zutritt, Begleitung, Schlüssel/Karten und externe Dienstleister.
- **IT-/Plattform Owner:** bewertet technische Risiken bei Arbeiten an Infrastruktur, Racks, Verkabelung oder Systemen.
- **ISMS-Owner / Security-Rolle:** definiert Mindestanforderungen, Ausnahmebehandlung, Review und Eskalation.
- **Dienstleister / Besucher:** arbeiten nur im freigegebenen Umfang und melden Abweichungen sofort.
- **Management:** entscheidet bei dauerhaften Ausnahmen, Ressourcenlücken oder nicht akzeptablen Betriebsrisiken.

## Implementierung

### Minimalstart

Ziel: Arbeiten in kritischen Bereichen sind beauftragt, begleitet und nachvollziehbar.

1. Geschützte Bereiche werden benannt und einem Owner zugeordnet.
2. Für geplante Arbeiten gibt es einen einfachen Auftrag: wer, wann, wo, warum, mit welcher Begleitung.
3. Externe Personen erhalten nur zeitlich und sachlich begrenzten Zutritt.
4. Grundregeln werden vor Zutritt kommuniziert: keine unbeauftragten Arbeiten, keine Fotos, keine offenen Türen, keine Alleinarbeit ohne Freigabe, Auffälligkeiten melden.
5. Zutritt und Abschluss werden dokumentiert.
6. Abweichungen, Schäden oder unerwartete Funde werden als Incident, Facility- oder Maßnahmenpunkt behandelt.

Minimaler Nachweis:

- Liste geschützter Bereiche mit Owner,
- Arbeitsauftrag oder Besucherticket,
- Zutritts-/Begleitnachweis,
- kurze Arbeits- oder Abschlussnotiz,
- Abweichungs- oder Maßnahmenlog bei Problemen.

### Solide Praxis

Ziel: Arbeiten werden risikobasiert vorbereitet, gesteuert und nachbereitet.

1. Arbeitsarten werden klassifiziert: Routinewartung, Reinigung, Reparatur, Installation, Audit, Notfallzugang.
2. Je Arbeitsart werden Freigaben, Begleitung, zulässige Geräte, Fotoregeln, Materialein-/ausbringung und Dokumentation festgelegt.
3. Dienstleister erhalten vertraglich oder operativ klare Sicherheitsvorgaben.
4. Arbeiten an kritischer Technik werden mit Change-, Wartungs- oder Notfallprozessen verbunden.
5. Zutrittsprotokolle und Arbeitsnachweise werden regelmäßig stichprobenartig gegen Aufträge geprüft.
6. Wiederkehrende Abweichungen führen zu Schulung, Dienstleistergespräch, Prozessänderung oder Management-Handoff.
7. Notfallzugänge werden nachträglich reviewed.

Starke Evidenz:

- Bereichs- und Arbeitsartenmatrix,
- freigegebene Arbeitsaufträge,
- Besucher-/Dienstleister- und Begleitnachweise,
- Change- oder Wartungstickets,
- Abschluss-/Abnahmeprotokolle,
- Stichprobenreview von Zutritt gegen Auftrag,
- Maßnahmen aus Abweichungen.

### Fortgeschritten

Ziel: Arbeiten in geschützten Bereichen sind mit Zutritt, Change, Dienstleistersteuerung und Incident-Fähigkeit integriert.

1. Zutrittsberechtigungen, Arbeitsaufträge und Change-Fenster werden vorab abgeglichen.
2. Kritische Tätigkeiten nutzen Vier-Augen-Prinzip, temporäre Berechtigungen oder dokumentierte Freigabe durch Bereichs- und Service Owner.
3. Material, Datenträger und Geräte werden bei Ein- und Ausbringung nachvollziehbar behandelt.
4. Dienstleisterleistung, Abweichungen und Wiederholungsfehler fließen in Vendor Reviews ein.
5. Notfallarbeiten werden mit nachgelagertem Review, Evidenz und Risikoentscheidung abgeschlossen.
6. Kennzahlen zeigen nicht genehmigte Zutritte, nachträgliche Notfallzugänge, fehlende Abschlussnotizen und wiederkehrende Findings.

## Ablauf als Routine

1. **Arbeitsbedarf entsteht:** Wartung, Reparatur, Lieferung, Audit, Reinigung, Notfall oder Change.
2. **Auftrag erfassen:** Bereich, Zweck, Personen, Zeitraum, Tätigkeit, Geräte/Material, Begleitbedarf.
3. **Risiko prüfen:** Schutzbedarf, kritische Systeme, Datenträger, personenbezogene Daten, Betriebsunterbrechung.
4. **Freigeben:** Bereichsowner, Service Owner, Facility oder Change Owner bestätigen den Arbeitsrahmen.
5. **Zutritt steuern:** Identität prüfen, Begleitung organisieren, Regeln kommunizieren, Zutritt protokollieren.
6. **Arbeit durchführen:** nur freigegebene Tätigkeit, Abweichungen sofort melden.
7. **Abschluss dokumentieren:** Ergebnis, Auffälligkeiten, Materialbewegungen, offene Punkte.
8. **Nachbereiten:** Zutritt schließen, temporäre Rechte entziehen, Abweichungen behandeln, Review ablegen.
9. **Verbessern:** Muster aus Findings in Arbeitsregeln, Verträge, Schulung oder Raumkonzept zurückführen.

## Entscheidungen

- Welche Bereiche gelten als geschützt und welche Arbeitsregeln gelten dort?
- Welche Tätigkeiten brauchen Begleitung, Vier-Augen-Prinzip oder Change-Freigabe?
- Welche Geräte, Fotos, Datenträger oder Materialien dürfen eingebracht oder entfernt werden?
- Wann darf ein Notfallzugang Regeln temporär übersteuern und wer reviewed danach?
- Welche Dienstleister dürfen eigenständig arbeiten und welche nicht?
- Welche Abweichungen sind Incident, Vertragsproblem oder Managementthema?

## Evidenz

### Starke Evidenz

- aktueller Scope geschützter Bereiche mit Owner,
- Arbeitsauftrag mit Zweck, Zeitraum, Personen und Freigabe,
- Zutritts-, Besucher- oder Begleitprotokoll,
- Change-/Wartungs-/Abnahmeticket,
- Nachweis entfernter temporärer Berechtigungen,
- Abweichungs- oder Incident-Dokumentation,
- Review von Notfallzugängen und wiederkehrenden Findings.

### Schwache Evidenz

- allgemeine Hausordnung ohne bereichsspezifische Arbeitsregeln,
- Besucherliste ohne Bezug zum Arbeitsauftrag,
- Dienstleistervertrag ohne operative Nachweise,
- Zutrittsprotokoll ohne Abschlussnotiz,
- mündliche Freigaben für kritische Tätigkeiten.

### Evidenzlücken

- Arbeiten in geschützten Bereichen ohne Auftrag,
- externe Personen ohne Begleit- oder Identitätsnachweis,
- Notfallzugänge ohne nachträglichen Review,
- offene Türen, mitgebrachte Geräte oder Fotos ohne Regelung,
- temporäre Berechtigungen bleiben aktiv,
- Schäden oder Auffälligkeiten werden nicht nachverfolgt.

## Wirksamkeitsprüfung

Prüffragen:

- Kann für Stichproben nachvollzogen werden, warum eine Person in einem geschützten Bereich gearbeitet hat?
- Passen Arbeitsauftrag, Zutrittszeit und Abschlussnotiz zusammen?
- Werden externe Personen angemessen begleitet und eingewiesen?
- Sind Notfallzugänge selten, begründet und nachträglich reviewed?
- Werden Abweichungen als Maßnahmen, Incident oder Dienstleisterthema behandelt?
- Sind temporäre Berechtigungen und Schlüssel/Karten nach Abschluss entzogen oder zurückgegeben?

Mögliche Kennzahlen:

- Arbeiten ohne vollständigen Auftrag,
- fehlende Abschlussnotizen,
- nachträgliche Notfallzugänge,
- Abweichungen je Dienstleister oder Bereich,
- überfällige temporäre Zutritte,
- Findings aus Stichprobenreviews.

## BSIG-/NIS2-Anschluss

Arbeiten in geschützten Bereichen ist anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Schutz kritischer Betriebsumgebungen, Lieferantensteuerung, Incident-Prävention und Business Continuity. Der konkrete Bezug sollte im Anforderungsregister, in Standort- und Dienstleisterrisiken sowie in BCM-Reviews geprüft werden.

Dieses Artefakt ersetzt keine Rechts-, Datenschutz-, Arbeits-, Vertrags- oder Arbeitsschutzprüfung.

## Grenzen

- Dieses Artefakt ist keine vollständige Arbeits-, Bau-, Wartungs- oder Arbeitsschutzanweisung.
- Es ersetzt keine Vertragsprüfung für Dienstleister und keine Datenschutzbewertung bei Protokollierung.
- Es garantiert keine Manipulations- oder Sabotagefreiheit.
- Es enthält keine ISO-27002-Texte oder Zertifizierungszusage.
- Öffentliche Beispiele bleiben fiktiv und ohne reale Standortdetails.

## Handoffs

- **Facility-Handoff:** Zutritt, Begleitung, Schlüssel/Karten, Reinigung, Wartung, bauliche Arbeiten.
- **IT-/Change-Handoff:** Arbeiten an Racks, Netzwerk, Servern, Verkabelung, Strom, Klima oder produktiver Infrastruktur.
- **Einkauf-/Vendor-Handoff:** Dienstleisterregeln, Vertragsvorgaben, wiederholte Abweichungen, Leistungsreview.
- **Incident-Handoff:** unbefugter Zutritt, Manipulationsverdacht, Verlust, Schaden, unbeauftragte Tätigkeit.
- **Datenschutz-/Legal-Handoff:** Besucher-/Zutrittsprotokolle, Beschäftigtendaten, Fotos, Vertrags- oder Haftungsfragen.
- **BCM-Handoff:** Arbeiten gefährden kritische Dienste oder erfordern Notfallzugang.
- **Management-Handoff:** dauerhafte Ausnahmen, Ressourcenmangel, kritische Dienstleisterprobleme oder akzeptierte Restrisiken.

## Typische Fehler

- Geschützte Bereiche sind definiert, aber Arbeitsregeln fehlen.
- Besuchende werden registriert, aber nicht mit einem konkreten Auftrag verbunden.
- Reinigung und Wartung werden als niedriges Risiko betrachtet, obwohl sie regelmäßig Zugang zu kritischen Bereichen haben.
- Notfallzugänge werden nicht nachbereitet.
- Temporäre Zutritte bleiben nach Abschluss aktiv.
- Abweichungen werden lokal gelöst und erreichen ISMS, Facility oder Vendor Management nicht.

## Fiktives Mini-Beispiel

Ein fiktiver IT-Dienstleister lässt einen Klimaservice in den Serverraum. Bisher wurde der Zutritt nur telefonisch angekündigt. Nach einem Review führt die Organisation ein Wartungsticket ein: Zeitraum, Personen, Begleitung, erlaubte Tätigkeiten und Abschlussnotiz. Beim ersten Termin fällt auf, dass ein Dienstleister Fotos machen möchte. Die Fotoregel wird ergänzt und im nächsten Vendor Review besprochen.

Evidenz:

- Wartungsticket mit Freigabe,
- Besucher- und Begleitnachweis,
- Abschlussnotiz des Facility Owners,
- dokumentierte Abweichung zur Fotoregel,
- aktualisierte Dienstleisteranweisung.
