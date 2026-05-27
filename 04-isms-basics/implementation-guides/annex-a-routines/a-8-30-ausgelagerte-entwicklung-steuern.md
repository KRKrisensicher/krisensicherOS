
# A.8.30 — Ausgelagerte Entwicklung steuern

## Zweck

Ausgelagerte Entwicklung sorgt für Geschwindigkeit und Spezialwissen, kann aber Sicherheitsverantwortung, Architekturentscheidungen und Nachweise unscharf machen. Diese Routine stellt sicher, dass externe Entwicklungsanteile nicht nur vertraglich beauftragt, sondern fachlich gesteuert, sicherheitsbezogen reviewed und evidenzfähig abgenommen werden.

Der Kern ist nicht „Dienstleister beauftragt“, sondern: Welche Entwicklungsleistungen liegen extern? Welche Sicherheitsanforderungen gelten? Wer prüft Ergebnisse? Wie werden Code, Komponenten, Zugänge, Testdaten, Schwachstellen und Abnahmen gesteuert?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Steuerungsroutine für ausgelagerte Entwicklung. Sie verbindet Beschaffung, Produktverantwortung, Secure Development, Zugriffsschutz, Lieferantennachweise, Änderungssteuerung, Abnahme und Risikoentscheidung.

## Typische Risiken

- Wenn externe Entwickler ohne klare Sicherheitsanforderungen arbeiten, können unsichere Architektur, unsichere Komponenten oder fehlende Nachweise entstehen.
- Wenn Quellcode, Build-Pipelines oder Repositories extern zugänglich sind, können übermäßige Rechte, unklare Eigentümerschaft oder Datenabflüsse auftreten.
- Wenn Sicherheitsreviews erst bei Abnahme stattfinden, werden grundlegende Designfehler spät und teuer sichtbar.
- Wenn Dienstleister eigene Unterauftragnehmer einsetzen, können Verantwortlichkeiten, Zugriffspfade und Geheimhaltung unklar werden.
- Wenn Findings aus Code Review, Tests oder Penetrationstests nicht vertraglich und operativ nachverfolgt werden, gehen Risiken in Produktion.
- Wenn Know-how und Dokumentation beim Dienstleister verbleiben, entsteht Abhängigkeit für Betrieb, Wartung und Incident Response.

## Trigger

- neues Entwicklungsprojekt mit externem Anteil.
- Erweiterung, Wartung oder Betrieb einer extern entwickelten Anwendung.
- Lieferantenwechsel, neue Unterauftragnehmer oder geändertes Delivery-Modell.
- Zugriff auf Repositories, CI/CD, Entwicklungsumgebungen, Testdaten oder produktionsnahe Informationen.
- sicherheitsrelevante Architektur-, Technologie- oder Komponentenentscheidung.
- Schwachstelle, Auditfinding, Incident oder Abnahmeproblem mit externem Entwicklungsbezug.
- Vertragsverlängerung, Projektabschluss oder Übergabe in Betrieb.

## Rollen und Verantwortung

- **Product Owner / Auftraggeber:** definiert fachlichen Scope, Abnahmekriterien und Prioritäten.
- **Entwicklungsverantwortliche / Architekturrolle:** prüft Design, Codequalität, technische Schulden und Übergabefähigkeit.
- **Security-Rolle / ISMS-Owner:** definiert Sicherheitsanforderungen, Reviewpunkte, Evidenzlogik und Eskalation.
- **IT-/Plattform Owner:** steuert Repositories, Zugänge, Build-/Deploy-Pipelines und technische Integration.
- **Einkauf / Vendor Management:** verankert Anforderungen, Nachweise, Unterauftragnehmerlogik und Exit-Themen im Lieferantenprozess.
- **Datenschutz / Legal:** prüft personenbezogene Daten, Vertragsfragen, Geheimhaltung, Rechte an Arbeitsergebnissen und Unterauftragnehmer.
- **Management:** entscheidet über Restrisiken, Ressourcen, Lieferantenwechsel oder Go-live trotz offener Findings.

## Implementierung

### Minimalstart

Ziel: externe Entwicklungsarbeit wird vor Beginn sicherheitsbezogen greifbar und bei Abnahme geprüft.

1. Für jedes externe Entwicklungsvorhaben werden Owner, Lieferant, Scope, Systeme, Datenklassen und Zugriffsbedarf festgehalten.
2. Mindestanforderungen werden vor Start geklärt: sichere Entwicklung, Umgang mit Geheimnissen, Testdaten, Komponenten, Dokumentation, Review und Abnahme.
3. Externe Zugänge zu Repository, Ticketing, Build- oder Testumgebung werden beantragt, befristet und reviewed.
4. Sicherheitsrelevante Ergebnisse werden vor Übernahme geprüft: Code Review, Dependency-Check, Testnachweis, Architekturreview oder Abnahmecheck.
5. Offene Findings erhalten Owner, Frist, Entscheidung und gegebenenfalls Ausnahme.
6. Übergabe in Betrieb enthält Dokumentation, bekannte Risiken, Betriebsanforderungen und Support-/Exit-Informationen.

Minimaler Nachweis:

- Lieferanten-/Projektsteckbrief mit Owner und Scope,
- Sicherheitsanforderungen oder Abnahmekriterien,
- Zugriffsfreigaben für externe Beteiligte,
- Review- oder Testnachweise,
- Finding-/Maßnahmenliste,
- Übergabenotiz an Betrieb oder Product Owner.

### Solide Praxis

Ziel: externe Entwicklung ist in Beschaffung, SDLC, Change und Risikomanagement eingebettet.

1. Lieferanten werden nach Kritikalität, Systemnähe, Datenbezug und Entwicklungsanteil klassifiziert.
2. Sicherheitsanforderungen werden wiederverwendbar formuliert: Secure Coding, Secrets, Logging, Komponenten, Schwachstellen, Dokumentation, Zugriff, Testdaten, Übergabe.
3. Projektmeilensteine enthalten Security-Gates: Architektur, Implementierung, Test, Abnahme, Go-live und Übergabe.
4. Externe Findings laufen in dasselbe Maßnahmenlog wie interne Entwicklungs- und Schwachstellenfindings.
5. Unterauftragnehmer, Offshore-/Nearshore-Modelle, Toolnutzung und Repository-Zugriffe werden transparent gemacht.
6. Ausnahmen werden befristet, risikobewertet und bei kritischen Systemen ins Management Review gebracht.
7. Vertrags- und Lieferantenreviews prüfen, ob Nachweise, Reaktionszeiten, Rechte, Exit und Support zur Kritikalität passen.

Starke Evidenz:

- Lieferantenklassifizierung mit Entwicklungsbezug,
- wiederverwendbare Sicherheitsanforderungen,
- Security-Gate-Protokolle,
- Tickets zu Findings und Korrekturen,
- Zugriffreviews externer Konten,
- Übergabedokumentation,
- Managemententscheidung bei offenen Restrisiken.

### Fortgeschritten

Ziel: externe Entwicklung wird technisch und governance-seitig wie ein integrierter Teil der eigenen Lieferkette gesteuert.

1. Externe Teams arbeiten in kontrollierten Repositories, Pipelines und Entwicklungsumgebungen mit nachvollziehbaren Identitäten.
2. SAST, Dependency-Scanning, Secret-Scanning, Container-/IaC-Prüfungen und Reviewregeln sind in Delivery-Pipelines integriert.
3. Lieferantennachweise werden mit Risiko-, Asset-, Change- und Schwachstellenmanagement verknüpft.
4. Kritische Komponenten erhalten Software-Bill-of-Materials- oder Komponentenübersichten, soweit für Betrieb und Risikoentscheidung erforderlich.
5. Dienstleisterperformance wird nicht nur fachlich, sondern auch sicherheitsbezogen reviewed: Findings, Reaktionszeit, Wiederholungsfehler, Dokumentationsqualität.
6. Exit- und Notfallfähigkeit werden getestet: Zugriffsentzug, Repository-Übergabe, Build-Reproduzierbarkeit, Betriebswissen.

## Ablauf als Routine

1. **Auslagerung entsteht:** Projekt, Wartung, Erweiterung oder Lieferantenwechsel wird geplant.
2. **Scope und Kritikalität klären:** betroffene Anwendung, Daten, Schnittstellen, Produktivnähe und Geschäftsrelevanz bestimmen.
3. **Anforderungen festlegen:** Security-, Datenschutz-, Architektur-, Dokumentations- und Abnahmepunkte definieren.
4. **Zugänge steuern:** externe Identitäten, Rechte, Tools und Laufzeiten freigeben und dokumentieren.
5. **Entwicklung begleiten:** Reviews, Tests, Findings und Architekturentscheidungen während der Lieferung nachhalten.
6. **Abnahme durchführen:** Sicherheitskriterien, offene Risiken und Betriebsübergabe prüfen.
7. **Risiken entscheiden:** offene Findings beheben, akzeptieren, kompensieren oder eskalieren.
8. **Übergabe und Exit sichern:** Dokumentation, Zugriffsentzug, Support, Wissenstransfer und Eigentums-/Nutzungsfragen klären.
9. **Lieferantenreview nutzen:** Muster und Schwächen in Beschaffung, Verträge, SDLC oder Architektur zurückspielen.

## Entscheidungen

- Welche externen Entwicklungsleistungen sind kritisch genug für zusätzliche Security-Gates?
- Welche Sicherheitsanforderungen sind vor Beauftragung zwingend, welche projektabhängig?
- Wer darf externe Zugänge zu Code, Pipelines, Testdaten oder produktionsnahen Informationen genehmigen?
- Welche Findings blockieren Abnahme oder Go-live?
- Wie werden Unterauftragnehmer und Toolketten des Dienstleisters transparent gemacht?
- Wann wird ein Restrisiko vom Product Owner, wann vom Management entschieden?
- Welche Dokumentation und Rechte sind für Betrieb, Wartung und Exit unverzichtbar?

## Evidenz

### Starke Evidenz

- Projekt-/Lieferantensteckbrief mit Scope, Kritikalität und Ownern,
- vereinbarte Sicherheits- und Abnahmekriterien,
- nachvollziehbare Zugriffsfreigaben und Reviews externer Konten,
- Architektur-, Code-, Test-, Dependency- oder Schwachstellennachweise,
- Maßnahmenlog mit externen Findings und Entscheidungen,
- Abnahmeprotokoll mit offenen Risiken,
- Übergabe- und Exit-Nachweise,
- Managemententscheidung bei akzeptierten kritischen Restrisiken.

### Schwache Evidenz

- allgemeiner Dienstleistungsvertrag ohne konkreten Sicherheitsbezug,
- mündliche Zusage „der Dienstleister entwickelt sicher“,
- Codeablage ohne Review- oder Abnahmenachweis,
- einmaliger Penetrationstest ohne Finding-Nachverfolgung,
- Zugriffsliste externer Konten ohne Owner oder Ablaufdatum,
- Projektabschluss ohne Betriebsübergabe.

### Evidenzlücken

- externe Entwicklungsanteile sind im Lieferantenregister nicht sichtbar,
- keine Sicherheitsanforderungen vor Beauftragung,
- unklare Unterauftragnehmer oder Toolketten,
- keine Nachverfolgung offener Findings,
- keine Übersicht über externe Repository- oder Pipeline-Zugriffe,
- fehlende Rechte-, Dokumentations- oder Exit-Klärung.

## Wirksamkeitsprüfung

Prüffragen:

- Sind alle externen Entwicklungsanteile mit Owner, Scope und Kritikalität erfasst?
- Werden Sicherheitsanforderungen vor Start und nicht erst bei Abnahme geklärt?
- Sind externe Zugänge befristet, nachvollziehbar und reviewed?
- Können offene Findings bis zur Entscheidung oder Behebung verfolgt werden?
- Werden Abnahme und Go-live bei kritischen offenen Risiken bewusst entschieden?
- Ist der Betrieb nach Übergabe ohne stilles Dienstleisterwissen handlungsfähig?
- Werden Lieferantenmuster in Beschaffung, SDLC und Risikomanagement zurückgespielt?

Mögliche Kennzahlen:

- Anteil externer Entwicklungsprojekte mit Sicherheitsanforderungen vor Start,
- offene kritische Findings je Lieferant oder Projekt,
- überfällige externe Zugriffsreviews,
- Abnahmen mit offenen Ausnahmen,
- Zeit bis Behebung sicherheitsrelevanter Lieferantenfindings,
- Projekte mit vollständiger Übergabedokumentation.

## BSIG-/NIS2-Anschluss

Ausgelagerte Entwicklung ist anschlussfähig an NIS2-orientierte Themen wie Lieferkettensicherheit, sichere Entwicklung, Risikomanagement, Zugriffsschutz, Schwachstellenbehandlung und Aufrechterhaltung sicherer digitaler Dienste. Der konkrete Bezug sollte im Anforderungsregister, in Lieferantenklassifizierung und im Management Review geprüft werden.

Dieses Artefakt ersetzt keine rechtliche, datenschutzrechtliche oder vertragliche Bewertung.

## Grenzen

- Dieses Artefakt ist kein Mustervertrag und keine Rechtsberatung.
- Es ersetzt keine technische Code-, Architektur- oder Produktsicherheitsprüfung.
- Es bestätigt keine Konformität, Zertifizierungsfähigkeit oder Lieferanteneignung.
- Es enthält keine ISO-27002-Texte und keine vertraulichen Lieferanteninformationen.
- Es darf nicht als Nachweis genügen, wenn externe Entwicklung praktisch nicht gesteuert wird.

## Handoffs

- **Einkauf-/Vendor-Handoff:** neue Entwicklungsleistung, Lieferantenklassifizierung, Unterauftragnehmer, Vertrags- oder Exit-Fragen.
- **Legal-/Datenschutz-Handoff:** personenbezogene Daten, Rechte an Arbeitsergebnissen, Geheimhaltung, Auftragsverarbeitung, internationale Leistungserbringung oder Unterauftragnehmer.
- **Entwicklungs-/Architektur-Handoff:** Designentscheidungen, Code Review, Komponenten, technische Schulden, Dokumentations- und Übergabeanforderungen.
- **Access-Handoff:** externe Repository-, Ticketing-, Pipeline-, Cloud- oder Testumgebungszugriffe.
- **Change-/Release-Handoff:** Abnahme, Go-live, Rollback, Betriebsübergabe und offene Findings.
- **Incident-Handoff:** Verdacht auf kompromittierten Lieferantenzugang, Datenabfluss, manipulierten Code oder unsichere Komponente.
- **Management-Handoff:** kritische Restrisiken, Ressourcenmangel, Lieferantenwechsel oder Go-live mit offenen Risiken.

## Typische Fehler

- Sicherheitsanforderungen werden erst nach Vertragsschluss oder kurz vor Go-live formuliert.
- Externe Entwickler erhalten breite Zugänge ohne Laufzeit und Review.
- Abnahme prüft nur Fachfunktion, nicht Sicherheit, Betrieb und Übergabe.
- Findings werden als Projektthema behandelt und verschwinden nach Projektende.
- Unterauftragnehmer und Toolketten bleiben unsichtbar.
- Der Betrieb kann das Ergebnis nicht warten, bauen oder incident-fähig betreiben.
- Management bekommt Lieferstatus, aber keine entscheidungsfähigen Restrisiken.

## Fiktives Mini-Beispiel

Ein fiktiver Softwareanbieter beauftragt einen Dienstleister mit einer Erweiterung für ein Kundenportal. Vor Projektstart erstellt der Product Owner einen Scope-Steckbrief. Die Security-Rolle ergänzt Abnahmekriterien zu Authentisierung, Logging, Dependency-Check und Secret-Handling. Externe Entwickler erhalten befristete Repository-Zugänge. Vor Go-live zeigt ein Dependency-Scan eine kritische Bibliothek. Der Dienstleister liefert ein Update; für eine mittlere Schwachstelle wird eine befristete Ausnahme mit Wiedervorlage dokumentiert. Die Betriebsdokumentation wird als Go-live-Bedingung nachgereicht.

Evidenz:

- Projektsteckbrief,
- Sicherheits- und Abnahmekriterien,
- externe Zugriffsfreigaben,
- Dependency-Scan und Korrekturticket,
- Ausnahme mit Ablaufdatum,
- Übergabenachweis an Betrieb.
