
# A.7.3 — Schutz von Räumen und Gebäuden

## Zweck

Räume und Gebäude schützen Informationen, Systeme und Arbeitsfähigkeit nicht nur durch Türen, Schlösser oder Empfangsbereiche. Entscheidend ist eine betriebene Routine, die Schutzbedarf, Standortnutzung, Zutritt, bauliche Schwachstellen, Besucherwege und Verantwortlichkeiten zusammenführt.

Der Kern ist: Kritische Bereiche sollen nicht zufällig geschützt sein, sondern nachvollziehbar geplant, betrieben, reviewed und bei Veränderungen angepasst werden.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine standortbezogene Schutzroutine für Gebäude, Etagen, Räume und Zonen, in denen Informationen, IT-Systeme, Träger mediengebundener Informationen oder kritische Prozesse geschützt werden müssen. Die Routine verbindet Standortscope, Owner, Schutzbedarf, Zutrittslogik, bauliche oder organisatorische Maßnahmen, Review und Ausnahmebehandlung.

## Typische Risiken

- Wenn Server-, Technik-, Archiv- oder Lagerbereiche nicht klar abgegrenzt sind, können unbefugte Personen sensible Informationen oder Systeme erreichen.
- Wenn Empfangs-, Besucher- und Lieferwege nicht gesteuert werden, entstehen unbeobachtete Bewegungen in schutzbedürftigen Bereichen.
- Wenn Umzüge, Umbauten oder Flächenänderungen ohne Sicherheitsreview stattfinden, passen alte Schutzmaßnahmen nicht mehr zur neuen Nutzung.
- Wenn Schlüssel, Karten oder Raumrechte nicht regelmäßig geprüft werden, bleiben alte oder zu weitreichende Zutritte aktiv.
- Wenn Gebäuderisiken nicht mit Informationswerten verbunden sind, werden Investitionen in Schutzmaßnahmen beliebig oder zu spät entschieden.

## Trigger

- neuer Standort, Umzug, Umbau, Flächenwechsel oder Änderung der Raumnutzung.
- neue kritische Systeme, Archive, Labor-, Produktions- oder Betriebsbereiche.
- Änderung von Schutzbedarf, Datenklassen, Kundenanforderungen oder Prozesskritikalität.
- Sicherheitsereignis, Einbruch, Verlust, unbegleiteter Besucher oder auffälliger Zutrittsversuch.
- Wechsel von Facility-Dienstleister, Vermieter, Sicherheitsdienst oder Reinigungsdienst.
- turnusmäßiger Standort- oder Raumreview.
- Auditfinding, Risikoanalyse, BCM-Review oder Managemententscheidung.

## Rollen und Verantwortung

- **Standort-/Facility Owner:** verantwortet Gebäude- und Raumlogik, bauliche Maßnahmen, Schlüssel-/Kartenprozesse und Dienstleisterkoordination.
- **Asset Owner / Process Owner:** benennt Schutzbedarf der Informationen, Systeme und Prozesse im Raum.
- **ISMS-Owner / Security-Rolle:** definiert Mindestlogik für Zonen, Reviews, Ausnahmen und Risikohandling.
- **IT-/Plattform Owner:** bewertet Technikräume, Netzwerkflächen, Racks, Medienlager und Betriebsabhängigkeiten.
- **Empfang / Office Management:** betreibt Besucher-, Lieferanten- und Tageszugangsprozesse.
- **Einkauf / Vendor Management:** bindet Facility-, Sicherheits-, Wartungs- und Reinigungsdienstleister ein.
- **Management:** entscheidet über Investitionen, Restrisiken, Standortkompromisse und dauerhafte Ausnahmen.

## Implementierung

### Minimalstart

Ziel: Kritische Räume und Gebäudebereiche sichtbar, zugeordnet und reviewfähig machen.

1. Die Organisation benennt Standorte und Räume im ISMS-Scope, die erhöhte Schutzrelevanz haben.
2. Für jeden kritischen Bereich wird ein fachlicher Owner und ein Facility-Ansprechpartner festgelegt.
3. Zutrittsberechtigte Gruppen werden grob dokumentiert: Beschäftigte, Dienstleister, Besucher, Notfallzugang.
4. Besucher- und Lieferwege werden so beschrieben, dass schutzbedürftige Bereiche nicht unbeabsichtigt offenstehen.
5. Ein einfacher Review prüft mindestens jährlich oder bei Veränderung, ob Raum, Nutzung und Schutzmaßnahmen zusammenpassen.
6. Abweichungen werden als Maßnahme, Ausnahme oder Managemententscheidung dokumentiert.

Minimaler Nachweis:

- Standort-/Raumliste mit Ownern,
- Zonen- oder Raumskizze auf angemessenem Detailniveau,
- Liste der berechtigten Rollen oder Gruppen,
- Reviewnotiz mit Findings,
- Ausnahme oder Maßnahmenentscheidung.

### Solide Praxis

Ziel: Gebäudeschutz wird risikobasiert, wiederholbar und mit Zutrittssteuerung verbunden.

1. Räume werden nach Schutzbedarf gruppiert: öffentliche Bereiche, Büroflächen, interne Bereiche, geschützte Technik- oder Archivbereiche.
2. Zutrittsregeln, Begleitpflichten, Besucherregistrierung und Dienstleisterzugänge werden pro Zone beschrieben.
3. Schlüssel, Karten, Codes oder mechanische Berechtigungen werden mit Ausgabe, Rückgabe, Verlustmeldung und Review geführt.
4. Umbauten, neue Nutzung oder neue kritische Assets lösen einen Sicherheitsreview aus.
5. Regelmäßige Begehungen prüfen Türen, Beschilderung, Lagerung, Besucherwege und technische Schutzmaßnahmen.
6. Findings führen zu Maßnahmen mit Owner, Frist und Priorität.
7. Restrisiken und Investitionsbedarfe gehen in ISMS- oder Management Review.


### Fortgeschritten

Ziel: Gebäudeschutz wird in Standortplanung, BCM, Zutrittssysteme und Lagebild integriert.

1. Standort- und Raumdaten sind mit Assetinventar, Prozesskritikalität und Zutrittssteuerung verbunden.
2. Kritische Bereiche haben dokumentierte Schutzkonzepte mit Zonen, Verantwortlichkeiten, Eskalationswegen und Notfallzugängen.
3. Zutrittsereignisse, Störungen und Facility-Findings fließen in Security-, BCM- und Risikoreviews ein.
4. Standortentscheidungen berücksichtigen Sicherheits-, Verfügbarkeits-, Lieferketten- und Umweltaspekte.
5. Dienstleisterzugänge werden mit Vertragslogik, Identitätsprüfung, Begleitung und Review verbunden.
6. Management erhält entscheidungsfähige Informationen zu Standortrestrisiken, Investitionsbedarf und wiederkehrenden Findings.

## Ablauf als Routine

1. **Schutzbedarf entsteht oder ändert sich:** Standort, Raum, Asset, Prozess oder Dienstleisterzugang verändert sich.
2. **Scope klären:** betroffene Räume, Informationen, Systeme, Prozesse und Personen bestimmen.
3. **Schutzbedarf bewerten:** Kritikalität, Exposition, Besucher-/Dienstleisterkontakt und vorhandene Maßnahmen einordnen.
4. **Zonen und Regeln festlegen:** Zutritt, Begleitung, Schlüssel/Karten, Besucherwege und Ausnahmen definieren.
5. **Umsetzen:** Facility, IT, Office Management und betroffene Owner setzen Maßnahmen um.
6. **Nachweis ablegen:** Raumliste, Berechtigung, Begehung, Finding oder Entscheidung dokumentieren.
7. **Review durchführen:** Begehung, Berechtigungsabgleich, Dienstleisterreview oder Standortreview.
8. **Abweichungen steuern:** Maßnahme, befristete Ausnahme oder Management-Handoff.
9. **Verbessern:** Findings in Bauplanung, Zutrittsprozess, Dienstleistersteuerung oder BCM zurückspielen.

## Entscheidungen

- Welche Räume gelten als schutzbedürftig und warum?
- Welche Zonen brauchen Begleitpflicht, gesonderte Berechtigung oder technische Absicherung?
- Wer darf dauerhafte Raum- oder Zutrittsausnahmen genehmigen?
- Welche baulichen Lücken werden akzeptiert, kompensiert oder investiv behoben?
- Wie werden geteilte Gebäude, Co-Working-Flächen oder Vermieterabhängigkeiten behandelt?
- Welche Standortrestrisiken müssen ins Management Review?

## Evidenz

### Starke Evidenz

- aktueller Standort- und Raumscope mit Ownern,
- Zonenmodell oder Raumklassifizierung,
- Zutritts-/Besucher-/Dienstleisterprozess,
- Schlüssel-, Karten- oder Berechtigungsreview,
- Begehungsprotokoll mit Maßnahmenstatus,
- Nachweis behobener baulicher oder organisatorischer Findings,
- Managemententscheidung zu Restrisiken oder Investitionen.

### Schwache Evidenz

- allgemeine Gebäuderegel ohne Raum- oder Schutzbedarfsbezug,
- veraltete Raumpläne ohne Owner,
- Schlüsselliste ohne Rückgabe- oder Reviewdatum,
- pauschale Aussage „Zutritt nur für Berechtigte“ ohne Prozessnachweis,
- Begehungsfotos ohne Bewertung oder Maßnahme.

### Evidenzlücken

- kritische Räume ohne benannten Owner,
- Dienstleisterzugänge ohne Begleit- oder Freigabelogik,
- Umbauten ohne Sicherheitsreview,
- verlorene Schlüssel oder Karten ohne dokumentierte Reaktion,
- dauerhafte Gebäudelücken ohne Risikoentscheidung.

## Wirksamkeitsprüfung

Prüffragen:

- Sind kritische Räume und Gebäudebereiche bekannt und einem Owner zugeordnet?
- Passen Zutrittsregeln zur tatsächlichen Nutzung und zum Schutzbedarf?
- Werden Umzüge, Umbauten und Nutzungsänderungen sicherheitsseitig reviewed?
- Führen Begehungen zu nachvollziehbaren Maßnahmen?
- Sind Besucher-, Lieferanten- und Dienstleisterwege praktisch steuerbar?
- Sind akzeptierte bauliche Restrisiken entscheidungsfähig dokumentiert?

Mögliche Kennzahlen:

- Anteil kritischer Räume mit aktuellem Owner,
- offene Findings aus Standortbegehungen,
- überfällige Zutritts-/Schlüsselreviews,
- Anzahl befristeter Ausnahmen,
- Zeit bis Reaktion auf Karten-/Schlüsselverlust,
- Managementpunkte zu Standortrestrisiken.

## BSIG-/NIS2-Anschluss

Der Schutz von Räumen und Gebäuden ist anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, physische Resilienz, Schutz kritischer Dienste, Business Continuity und Lieferantensteuerung. Betroffene Organisationen sollten im Anforderungsregister prüfen, welche Standorte, Nachweise und Managemententscheidungen relevant sind.

Dieses Artefakt trifft keine rechtliche Aussage zur Anwendbarkeit und ersetzt keine baurechtliche, arbeitsschutzrechtliche, datenschutzrechtliche oder versicherungsbezogene Prüfung.

## Grenzen

- Dieses Artefakt ist kein vollständiges Gebäudesicherheitskonzept und keine Bauplanung.
- Es ersetzt keine rechtliche, versicherungsbezogene oder arbeitsschutzfachliche Bewertung.
- Es garantiert keine Einbruch-, Sabotage- oder Ausfallsicherheit.
- Es enthält keine ISO-27002-Texte oder Zertifizierungszusage.
- Öffentliche Beispiele bleiben fiktiv und ohne sensible Standortdetails.

## Handoffs

- **Facility-Handoff:** bauliche Maßnahmen, Schlüssel/Karten, Türen, Zonen, Wartung, Vermieterabstimmung.
- **IT-Handoff:** Technikräume, Racks, Netzwerkflächen, Medienlager, Notfallzugänge.
- **Einkauf-/Vendor-Handoff:** Reinigungs-, Sicherheits-, Wartungs-, Empfangs- oder Facility-Dienstleister.
- **BCM-Handoff:** Standortausfall, Ersatzflächen, kritische Betriebsräume, Notzugang.
- **Datenschutz-/Legal-Handoff:** Besucherprotokolle, Ausweisdaten, Video- oder Zutrittsdaten, Vertragsfragen.
- **Management-Handoff:** Investitionsbedarf, nicht behebbare bauliche Lücken, Standortrestrisiken.
- **Audit-/Evidence-Handoff:** fehlende Raumliste, fehlende Reviews oder nicht nachvollziehbare Ausnahmen.

## Typische Fehler

- Gebäude werden als Facility-Thema behandelt, ohne Verbindung zu Informationswerten.
- Raumpläne sind aktuell, aber Schutzbedarf und Owner fehlen.
- Schlüssel oder Karten werden ausgegeben, aber nicht regelmäßig überprüft.
- Besucherprozesse funktionieren am Empfang, aber nicht bei Seiteneingängen, Lieferungen oder Wartung.
- Umbauten verändern Schutzgrenzen, ohne dass ISMS oder IT eingebunden werden.
- Bauliche Schwächen bleiben bekannt, aber ohne Entscheidung oder Kompensation.

## Fiktives Mini-Beispiel

Ein fiktiver Softwaredienstleister zieht in eine neue Büroetage. Beim Standortreview wird festgestellt, dass ein Netzwerkschrank in einem allgemein zugänglichen Kopierraum steht. Facility und IT legen den Bereich als geschützten Technikraum fest, verlegen Druckernutzung in einen anderen Raum und beschränken den Zutritt auf IT und Facility. Bis zur baulichen Anpassung wird eine befristete Kompensationsmaßnahme mit wöchentlicher Sichtprüfung dokumentiert.

Evidenz:

- aktualisierte Raumliste mit Owner,
- Entscheidung zur Raumklassifizierung,
- Ticket zur Zutrittsänderung,
- befristete Kompensationsmaßnahme,
- Reviewnotiz nach baulicher Anpassung.
