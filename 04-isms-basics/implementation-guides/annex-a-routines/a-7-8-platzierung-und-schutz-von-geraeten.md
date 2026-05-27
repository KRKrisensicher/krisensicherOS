
# A.7.8 — Platzierung und Schutz von Geräten

## Zweck

Platzierung und Schutz von Geräten sorgt dafür, dass Server, Netzwerkkomponenten, Arbeitsplätze, Drucker, Kiosksysteme, Sensorik oder andere technische Geräte nicht unnötig physischem Zugriff, Manipulation, Umwelteinflüssen oder Beobachtung ausgesetzt sind.

Der Kern ist nicht „Gerät steht irgendwo im Büro“, sondern eine nachvollziehbare Entscheidung: Welches Gerät ist kritisch, wo darf es stehen, welche Umgebung braucht es, wer darf daran arbeiten und wie wird geprüft, ob der Schutz im Alltag hält?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der Geräte entsprechend Kritikalität, Standort, Zugriffsmöglichkeit und Umgebungsrisiken platziert, geschützt, reviewed und bei Änderungen neu bewertet werden.

## Typische Risiken

- Wenn kritische Netzwerkgeräte frei zugänglich stehen, können unbefugte Personen Kabel ziehen, Geräte neu starten, Ports nutzen oder Konfigurationen verändern.
- Wenn Bildschirme, Drucker oder Multifunktionsgeräte in offenen Bereichen stehen, können Informationen mitgelesen, mitgenommen oder falsch abgeholt werden.
- Wenn Geräte in ungeeigneter Umgebung betrieben werden, können Hitze, Feuchtigkeit, Staub, Erschütterung oder Stromprobleme Ausfälle verursachen.
- Wenn temporäre Geräte bei Projekten, Veranstaltungen oder Umzügen nicht bewertet werden, entstehen ungeschützte Übergangslösungen.
- Wenn Schutzanforderungen nur beim Erstaufbau betrachtet werden, bleiben spätere Umbauten, neue Teams oder geänderte Nutzung unbemerkt.

## Trigger

- neues Gerät, neue Geräteklasse oder geänderter Standort.
- Büro-, Lager-, Technikraum- oder Rechenzentrumsumzug.
- Umbau, Renovierung, Flächenänderung oder neue Besucher-/Dienstleisterwege.
- neuer Service, der lokale Geräte oder Edge-Komponenten benötigt.
- Sicherheitsereignis, Verlust, Manipulationsverdacht, Ausfall oder Beinahevorfall.
- Wartung, Gerätetausch, Außerbetriebnahme oder Inventur.
- turnusmäßiger Standort-, Asset- oder Facility-Review.

## Rollen und Verantwortung

- **Asset Owner / Service Owner:** bewertet Kritikalität, Schutzbedarf und geschäftliche Auswirkung eines Geräts.
- **IT-/Plattform Owner:** definiert technische Mindestanforderungen, betreibt Geräte und dokumentiert Änderungen.
- **Facility-/Standort Owner:** verantwortet Räume, Möblierung, physische Schutzmaßnahmen und Standortänderungen.
- **ISMS-Owner / Security-Rolle:** legt Bewertungslogik, Reviewfrequenz, Ausnahmebehandlung und Eskalationswege fest.
- **Fachbereich / Prozess Owner:** meldet Nutzungsänderungen, besondere Sichtschutz- oder Verfügbarkeitsanforderungen.
- **Einkauf / Lieferantenmanagement:** berücksichtigt Geräteaufstellung, Wartungszugang und Dienstleistereinsatz bei Beschaffung und Verträgen.
- **Management:** entscheidet bei Zielkonflikten zwischen Kosten, Ergonomie, Verfügbarkeit, Sicherheit und Flächennutzung.

## Implementierung

### Minimalstart

Ziel: Kritische Geräte stehen nicht zufällig, sondern mit Owner, Standortentscheidung und einfacher Prüfung.

1. Die Organisation identifiziert kritische Geräteklassen im Scope: Netzwerkgeräte, Server, Backup-Hardware, zentrale Drucker, Empfangs-/Kiosksysteme, Produktions- oder Gebäudetechnik mit IT-Bezug.
2. Für jede kritische Geräteklasse wird ein Owner benannt.
3. Standorte werden mit einfacher Schutzlogik bewertet: öffentlich zugänglich, beaufsichtigt, abschließbar, klimatisch geeignet, manipulationsanfällig.
4. Offensichtliche Risiken werden behandelt: abschließbarer Raum oder Schrank, Sichtschutz, Portschutz, getrennte Besucherbereiche, klare Wartungsregel.
5. Änderungen an Standort oder Nutzung lösen eine kurze Neubewertung aus.
6. Ausnahmen werden mit Begründung, Laufzeit und Wiedervorlage dokumentiert.

Minimaler Nachweis:

- Liste kritischer Geräteklassen oder Geräte mit Owner,
- Standort-/Raumzuordnung,
- einfache Schutzbewertung oder Checkliste,
- Ticket oder Reviewnotiz bei Umzug/Änderung,
- dokumentierte Ausnahme mit Wiedervorlage.

### Solide Praxis

Ziel: Geräteplatzierung wird in Asset-, Standort- und Change-Prozesse eingebaut.

1. Geräte werden nach Kritikalität und Standorttyp klassifiziert: Technikraum, Bürofläche, öffentlich zugänglicher Bereich, Produktionsbereich, Außenstelle, mobiles/temporäres Setup.
2. Mindestschutz je Klasse wird festgelegt: Zutrittsbeschränkung, Umgebungsbedingungen, Sichtschutz, Kabelschutz, Portnutzung, Wartungszugang, Inventarkennzeichnung.
3. Beschaffung, Umzug und Change Management prüfen Standortanforderungen vor Inbetriebnahme.
4. Facility und IT führen gemeinsame Stichproben durch.
5. Findings führen zu Maßnahme, Ausnahme oder Managemententscheidung.
6. Schutzanforderungen für Dienstleisterwartung und temporäre Installationen werden in Tickets oder Arbeitsaufträgen sichtbar.

Starke Evidenz:

- Geräte-/Assetinventar mit Standort und Owner,
- Mindestschutzlogik je Standort- oder Geräteklasse,
- Change- oder Umzugstickets mit Standortprüfung,
- Stichprobenprotokolle mit Maßnahmen,
- Nachweise behobener Mängel,
- Ausnahmeentscheidungen mit Frist.

### Fortgeschritten

Ziel: Geräteschutz wird mit Monitoring, Facility Management und Resilienzplanung verbunden.

1. Kritische Räume und Geräte sind mit Zutritts-, Umwelt- oder Verfügbarkeitsmonitoring verbunden.
2. Assetinventar, CMDB, Standortpläne und Wartungsverträge werden regelmäßig abgeglichen.
3. Kritische Geräte haben definierte Anforderungen an Redundanz, Ersatzteile, Wartungsfenster und Eskalation.
4. Manipulations-, Temperatur-, Strom- oder Standortalarme fließen in Incident Triage oder Betriebsmonitoring ein.
5. Standortentscheidungen werden bei BCM-, Krisen- und Architekturreviews berücksichtigt.
6. Management erhält entscheidungsfähige Informationen zu Standortrestrisiken, Investitionsbedarf und wiederkehrenden Mängeln.

## Ablauf als Routine

1. **Bedarf entsteht:** neues Gerät, neuer Standort, Umzug, Wartung oder Änderung.
2. **Kritikalität klären:** betroffener Service, Daten, Abhängigkeiten und Auswirkung einordnen.
3. **Standort bewerten:** Zugänglichkeit, Sichtbarkeit, Manipulationsmöglichkeit, Umweltbedingungen und Wartungsbedarf prüfen.
4. **Schutz festlegen:** Raum, Schrank, Position, Kennzeichnung, Sichtschutz, Port-/Kabelschutz oder organisatorische Regel bestimmen.
5. **Umsetzen:** IT, Facility oder Dienstleister setzen die Maßnahme um.
6. **Evidenz sichern:** Inventar, Ticket, Foto nur falls unkritisch, Checkliste oder Reviewnotiz ablegen.
7. **Reviewen:** Stichprobe oder Standortreview prüft, ob Geräte noch passend stehen.
8. **Eskalieren:** nicht umsetzbare Schutzmaßnahmen, Kostenkonflikte oder Restrisiken ins Management geben.

## Entscheidungen

- Welche Geräte gelten im ISMS-Scope als kritisch?
- Welche Standorte sind für welche Geräteklassen zulässig?
- Wann reicht organisatorische Kontrolle, wann braucht es baulichen oder technischen Schutz?
- Welche Geräte dürfen in öffentlich zugänglichen oder unbeaufsichtigten Bereichen stehen?
- Wie werden temporäre Aufstellungen, Testgeräte und Projektflächen behandelt?
- Wer akzeptiert Restrisiken, wenn Standort oder Budget keinen angemessenen Schutz erlauben?

## Evidenz

### Starke Evidenz

- aktuelles Geräteinventar mit Standort und Owner,
- dokumentierte Standort- und Schutzbewertung,
- Change-/Umzugstickets mit Freigabe,
- Facility- oder IT-Stichproben mit Findings und Maßnahmen,
- Nachweis umgesetzter Schutzmaßnahmen,
- befristete Ausnahme mit Risikoentscheidung,
- Managemententscheidung bei nicht behebbaren Standortkonflikten.

### Schwache Evidenz

- allgemeine Clean-Desk- oder Facility-Regel ohne Gerätebezug,
- veraltete Raumpläne ohne Assetabgleich,
- Fotos ohne Datum, Owner oder Bewertung,
- Aussage „im Serverraum geschützt“ ohne Zutritts- oder Reviewnachweis,
- Inventarliste ohne Standortqualität.

### Evidenzlücken

- kritische Geräte ohne Owner,
- Geräte in offenen Bereichen ohne Schutzbewertung,
- Umzüge ohne Sicherheitsprüfung,
- temporäre Installationen ohne Ablaufdatum,
- Mängel ohne Maßnahme oder Ausnahmeentscheidung.

## Wirksamkeitsprüfung

Prüffragen:

- Können kritische Geräte einem Standort, Owner und Schutzbedarf zugeordnet werden?
- Werden Standortänderungen vor Inbetriebnahme geprüft?
- Sind Geräte in offenen Bereichen bewusst bewertet und geschützt?
- Führen Stichproben zu Korrekturen oder Entscheidungen?
- Sind Umwelt- und Manipulationsrisiken für kritische Geräte sichtbar?
- Werden Ausnahmen befristet und reviewed?

Mögliche Kennzahlen:

- Anteil kritischer Geräte mit Standort und Owner,
- offene Findings aus Standortreviews,
- überfällige Ausnahmen,
- ungeplante Ausfälle mit Standort-/Umgebungsbezug,
- Anzahl nicht inventarisierter Geräte in Stichproben.

## BSIG-/NIS2-Anschluss

Die Platzierung und der Schutz von Geräten sind anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, physische Sicherheit, Cyberhygiene, Aufrechterhaltung kritischer Dienste und Business Continuity. Für betroffene Organisationen sollte im Anforderungsregister geprüft werden, welche Standorte, Dienste und Nachweise relevant sind.

Dieses Artefakt ersetzt keine rechtliche Prüfung, keine baurechtliche Bewertung und keine verbindliche Aussage zur Anwendbarkeit.

## Grenzen

- Dieses Artefakt ist kein detaillierter Bau-, Rechenzentrums- oder Brandschutzstandard.
- Es ersetzt keine Arbeitsschutz-, Datenschutz-, Versicherungs- oder Gebäudesicherheitsprüfung.
- Es trifft keine Zertifizierungs- oder Konformitätszusage.
- Es enthält keine ISO-27002-Texte und keine vertraulichen Standortdetails.
- Es genügt nicht als Nachweis, wenn Geräte tatsächlich ungeprüft oder ungeschützt betrieben werden.

## Handoffs

- **Facility-Handoff:** Raum, Schrank, Klima, Zutritt, Umbau, Möblierung oder Standortmangel.
- **IT-Betrieb-Handoff:** Geräteaufbau, Portschutz, Konfiguration, Monitoring, Wartung und Inventarpflege.
- **BCM-Handoff:** Standort- oder Umgebungsrisiko kann kritischen Dienst unterbrechen.
- **Incident-Handoff:** Manipulationsverdacht, Diebstahl, unbefugter Zugriff oder unerklärter Ausfall.
- **Einkauf-/Lieferanten-Handoff:** neue Geräte, Wartungsverträge, Dienstleisterzugang oder Standortanforderungen.
- **Management-Handoff:** bauliche Investition, Flächenkonflikt, akzeptiertes Restrisiko oder dauerhafte Ausnahme.
- **Audit-/Evidence-Handoff:** fehlender Owner, veraltete Standortdaten oder nicht nachvollziehbare Reviewnachweise.

## Typische Fehler

- Geräte werden beim Aufbau geschützt, aber nach Umzügen nicht neu bewertet.
- Kleine Netzwerkkomponenten werden nicht als kritische Assets betrachtet.
- Drucker und Multifunktionsgeräte stehen in offenen Bereichen ohne Informationsschutzlogik.
- Facility und IT arbeiten mit unterschiedlichen Standortlisten.
- Temporäre Installationen bleiben dauerhaft bestehen.
- Umweltbedingungen werden erst nach Ausfällen betrachtet.
- Management erhält Mängellisten, aber keine entscheidungsfähigen Risiko- und Investitionsoptionen.

## Fiktives Mini-Beispiel

Ein fiktiver Dienstleister zieht ein Team in eine neue Bürofläche um. Beim Standortcheck fällt auf, dass ein Switch für das Kundennetz in einem offenen Sideboard geplant ist. Der IT-Owner bewertet das Gerät als kritisch, Facility stellt einen abschließbaren Netzwerkschrank bereit und der Umzugsticket wird erst nach Dokumentation des Standorts geschlossen. Eine Ausnahme bleibt für ein temporäres Testgerät bestehen und wird auf vier Wochen befristet.

Evidenz:

- Umzugsticket mit Standortprüfung,
- Asseteintrag mit Owner und Standort,
- Nachweis des abschließbaren Schranks,
- befristete Ausnahme für das Testgerät,
- Reviewtermin nach Projektende.
