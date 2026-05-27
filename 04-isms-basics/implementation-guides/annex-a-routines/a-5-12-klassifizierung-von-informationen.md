
# A.5.12 — Klassifizierung von Informationen

## Zweck

Klassifizierung von Informationen macht sichtbar, wie kritisch Informationen für Vertraulichkeit, Integrität, Verfügbarkeit und Nachvollziehbarkeit sind. Sie hilft Menschen und Systemen zu entscheiden, welche Schutzmaßnahmen, Freigaben, Speicherorte, Übertragungswege und Reviewroutinen angemessen sind.

Der Wert liegt nicht in möglichst vielen Labels, sondern in einer verständlichen Entscheidungshilfe: Welche Information braucht welchen Umgang, wer darf die Einstufung festlegen, wann wird sie überprüft und welche Folgen hat sie im Betrieb?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine einheitliche, rollenverständliche Klassifizierungsroutine für Informationen im ISMS-Scope. Die Routine verbindet Informationswerte, Geschäftsprozesse, Schutzbedarf, Datenklassen, Owner-Entscheidungen, Tooling, Schulung, Zugriff, Übertragung, Aufbewahrung und Löschung.

## Typische Risiken

- Wenn kritische Informationen nicht erkannt werden, werden sie in ungeeigneten Ablagen, Tools oder Kommunikationswegen verarbeitet.
- Wenn alles als hochkritisch markiert wird, verlieren Labels Steuerungswirkung und Teams umgehen die Regeln.
- Wenn Fachbereiche die Einstufung nicht verstehen, entstehen inkonsistente Entscheidungen und falsche Schutzmaßnahmen.
- Wenn Klassifizierung nicht mit Zugriff, Teilen, Aufbewahrung und Löschung verbunden ist, bleibt sie ein Papierlabel ohne Wirkung.
- Wenn Datenschutz-, Vertrags- oder Geheimhaltungsanforderungen nicht berücksichtigt werden, entstehen rechtliche und geschäftliche Risiken, die menschlich geprüft werden müssen.

## Trigger

- neuer Geschäftsprozess, neues Informationsasset, neues System oder neue Datenablage.
- Einführung oder Änderung von Datenklassen, Schutzbedarf oder Informationsarten.
- neues Produkt, neuer Dienstleister, neue Schnittstelle oder neue Übertragung an Dritte.
- Sicherheitsereignis, Fehlversand, Datenabfluss, Auditfinding oder Kundenanforderung.
- Änderung von Verträgen, gesetzlichen Rahmenbedingungen oder internen Risikoentscheidungen.
- turnusmäßiger Review von Assetinventar, Datenflüssen oder Schutzbedarfen.
- Migration in Cloud-, Kollaborations- oder KI-gestützte Arbeitsumgebungen.

## Rollen und Verantwortung

- **Information Owner / Prozess Owner:** legt fachliche Einstufung und Schutzbedarf für Informationsarten fest.
- **ISMS-Owner / Security-Rolle:** definiert Klassifizierungsmodell, Mindestlogik, Review und Eskalation.
- **Datenschutz / Legal:** prüft personenbezogene Daten, Vertragsbindungen, Vertraulichkeitszusagen und rechtliche Fragen.
- **IT-/Plattform Owner:** übersetzt Klassifizierung in Ablagen, Zugriff, Labels, DLP, Backup oder technische Kontrollen.
- **Fachbereiche:** wenden Einstufungen im Alltag an und melden unklare Informationsarten.
- **Einkauf / Lieferantenmanagement:** verbindet Klassifizierung mit Dienstleisteranforderungen und Datenweitergabe.
- **Management:** entscheidet Zielkonflikte, Toleranzen und Ressourcen für Schutzmaßnahmen.

## Implementierung

### Minimalstart

Ziel: wenige verständliche Klassen mit klarer Handlungswirkung einführen.

1. Die Organisation definiert drei bis vier Informationsklassen in eigener Sprache, zum Beispiel öffentlich, intern, vertraulich, streng vertraulich.
2. Für jede Klasse werden typische Beispiele und Mindesthandlungen beschrieben: Ablage, Zugriff, Teilen, Versand, Aufbewahrung, Entsorgung.
3. Kritische Informationsarten im ISMS-Scope erhalten einen Owner und eine Einstufung.
4. Neue oder geänderte Informationsarten werden über Prozess-, System- oder Lieferantenänderungen geprüft.
5. Unklare Einstufungen werden an den Information Owner oder ISMS-Owner eskaliert.
6. Die Anwendung wird stichprobenartig geprüft.

Minimaler Nachweis:

- Klassifizierungsmodell mit Beispielen,
- Liste kritischer Informationsarten mit Owner und Klasse,
- Entscheidungsnotiz für Einstufungen,
- Schulungs- oder Kommunikationsnachweis,
- Stichprobe oder Reviewnotiz.

### Solide Praxis

Ziel: Klassifizierung steuert konkrete Schutzmaßnahmen und Reviews.

1. Das Klassifizierungsmodell ist mit Assetinventar, Datenflüssen, Zugriffssteuerung, Informationsübertragung und Aufbewahrung verbunden.
2. Owner prüfen Einstufungen bei neuen Systemen, Prozessänderungen, Dienstleistereinbindung und wesentlichen Risiken.
3. Für jede Klasse gibt es Mindestschutz: Freigabe, Verschlüsselung, Speicherort, externe Weitergabe, Druck, Entsorgung, Backup und Logging, soweit passend.
4. Datenschutz- und Legal-Handoffs werden ausgelöst, wenn personenbezogene Daten, Geheimhaltungszusagen oder Vertragsanforderungen betroffen sind.
5. Falschklassifizierung, fehlende Labels oder unklare Datenflüsse werden als Findings behandelt.
6. Klassifizierung wird in Onboarding und rollenbezogene Schulung eingebaut.

Starke Evidenz:

- Klassifizierungsrichtlinie in eigener Sprache,
- Informationsasset-Register mit Einstufung,
- Schutzmaßnahmenmatrix je Klasse,
- Reviewentscheidungen der Owner,
- Nachweise aus Stichproben oder Korrekturmaßnahmen,
- Managemententscheidung bei Schutz-/Nutzbarkeitskonflikten.

### Fortgeschritten

Ziel: Klassifizierung wird in Daten- und Tool-Governance integriert.

1. Klassifizierung kann in Kollaborationstools, Dokumentenmanagement, E-Mail, DLP oder Cloud-Plattformen unterstützt werden.
2. Datenflüsse, Schnittstellen und KI-Nutzung werden anhand der Informationsklasse gesteuert.
3. Automatische oder assistierte Labels werden durch Owner-Reviews und Fehlklassifizierungsprozesse abgesichert.
4. Kennzahlen zeigen Abdeckung kritischer Informationsarten, Labelqualität, Ausnahmen und Korrekturen.
5. Klassifizierung fließt in Lieferantenbewertung, Incident Triage, BCM, Zugriff, Kryptografie und Löschkonzepte ein.
6. Management erhält entscheidungsfähige Sicht auf besonders schutzbedürftige Informationsbestände und offene Zielkonflikte.

## Ablauf als Routine

1. **Informationsart entsteht oder ändert sich:** neuer Prozess, Datenfluss, System, Bericht, Vertrag oder Datensatz.
2. **Owner bestimmen:** fachliche Verantwortung und Entscheidungsbefugnis klären.
3. **Schutzbedarf einordnen:** Auswirkungen bei Offenlegung, Veränderung, Verlust oder Nichtverfügbarkeit bewerten.
4. **Klasse festlegen:** anhand des Organisationsmodells und typischer Beispiele entscheiden.
5. **Handlungsfolgen ableiten:** Zugriff, Ablage, Versand, externe Weitergabe, Aufbewahrung, Löschung und technische Maßnahmen bestimmen.
6. **Nachweis ablegen:** Einstufung, Begründung, Owner und Reviewdatum dokumentieren.
7. **Anwendung prüfen:** Stichprobe, Toolauswertung, Incident-Auswertung oder Fachbereichsreview.
8. **Korrigieren:** falsche Einstufungen, fehlende Owner oder ungeeignete Ablagen beheben.

## Entscheidungen

- Welche Informationsklassen sind für die Organisation verständlich und ausreichend?
- Wer darf Einstufungen festlegen oder ändern?
- Welche Informationsarten sind so kritisch, dass Management oder Legal/Datenschutz einzubeziehen sind?
- Welche Mindestmaßnahmen gelten je Klasse?
- Wie werden Konflikte zwischen einfacher Zusammenarbeit und Schutzbedarf entschieden?
- Wie häufig werden Einstufungen reviewed?
- Welche Tools dürfen welche Informationsklassen verarbeiten?

## Evidenz

### Starke Evidenz

- aktuelles Klassifizierungsmodell mit Beispielen und Handlungsfolgen,
- Informationsasset-Register mit Owner, Klasse und Reviewdatum,
- dokumentierte Einstufungsentscheidungen bei neuen Prozessen oder Systemen,
- Stichproben mit Korrekturmaßnahmen,
- Schulungsnachweise für relevante Rollen,
- Managemententscheidungen bei Schutzbedarfskonflikten,
- Nachweise, dass Klassifizierung Zugriff, Übertragung oder Ablage steuert.

### Schwache Evidenz

- allgemeine Policy ohne Beispiele oder Betriebsfolgen,
- Labels in Dokumenten ohne Owner oder Review,
- lange Klassenliste, die niemand im Alltag nutzt,
- Schutzbedarfsanalyse ohne Verbindung zu Ablage und Zugriff,
- Schulungsfolie ohne Nachweis der Anwendung.

### Evidenzlücken

- kritische Informationsarten ohne Owner,
- Klassifizierung nicht im Assetregister sichtbar,
- externe Weitergaben ohne Einstufungsentscheidung,
- keine Prüfung von Fehlklassifizierungen,
- personenbezogene oder vertraglich geschützte Informationen ohne Handoff.

## Wirksamkeitsprüfung

Prüffragen:

- Können Fachbereiche die Klassen erklären und auf eigene Informationen anwenden?
- Sind kritische Informationsarten mit Owner und Reviewdatum erfasst?
- Führt eine höhere Klasse tatsächlich zu anderen Schutzmaßnahmen?
- Werden neue Systeme und Dienstleister anhand der Informationsklasse geprüft?
- Werden Fehlklassifizierungen gefunden und korrigiert?
- Sind Legal-/Datenschutzfragen bei sensiblen Informationsarten sichtbar eskaliert?

Mögliche Kennzahlen:

- Anteil kritischer Informationsassets mit aktueller Einstufung,
- Anzahl ungeklärter Informationsarten,
- Findings aus Klassifizierungsstichproben,
- überfällige Reviews,
- Ausnahmen von Mindestschutzmaßnahmen,
- Fehlversand- oder Ablagevorfälle mit Klassifizierungsbezug.

## BSIG-/NIS2-Anschluss

Informationsklassifizierung ist anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Zugriffsschutz, sichere Informationsverarbeitung, Lieferkettensicherheit, Incident Handling, Business Continuity und Governance. Sie hilft, Schutzbedarf und Nachweise nachvollziehbar zu machen, ersetzt aber keine organisationsspezifische rechtliche Bewertung.

Der konkrete Bezug sollte im Anforderungsregister, in Risikoanalysen und bei relevanten Managemententscheidungen geprüft werden.

## Grenzen

- Keine Rechts- oder Datenschutzberatung und keine verbindliche Einstufung personenbezogener Daten.
- Keine Zertifizierungs-, Konformitäts- oder Sicherheitsgarantie.
- Keine ISO-27002-Texte oder Normersatz.
- Klassifizierung allein schützt keine Information; sie muss Maßnahmen auslösen.
- Keine echten Kunden-, Personen-, Vertrags- oder Geheimdaten in Beispielen.

## Handoffs

- **Datenschutz-Handoff:** personenbezogene Daten, besondere Sensibilität, Betroffenenrechte, Löschung, Zweckbindung oder Auswertungen.
- **Legal-Handoff:** Vertragsgeheimnisse, Geheimhaltungszusagen, Export-/Branchenanforderungen, Streitfälle.
- **IT-/Plattform-Handoff:** technische Labels, DLP, Speicherorte, Verschlüsselung, Backup, Zugriff.
- **Lieferanten-Handoff:** Weitergabe klassifizierter Informationen an Dienstleister oder Subdienstleister.
- **Incident-Handoff:** Fehlversand, Datenabfluss, falsche Ablage oder unberechtigter Zugriff.
- **Management-Handoff:** hohe Schutzanforderungen, Ressourcenbedarf, Nutzbarkeitskonflikte, Risikoakzeptanz.
- **Audit-/Evidence-Handoff:** fehlende Owner, veraltete Einstufungen oder nicht nachvollziehbare Entscheidungen.

## Typische Fehler

- Zu viele Klassen werden definiert und im Alltag ignoriert.
- Klassifizierung wird als Labeling-Projekt verstanden, nicht als Schutzentscheidungsroutine.
- Fachbereiche haben keine Beispiele für ihre Informationsarten.
- Vertrauliche Informationen dürfen technisch weiterhin beliebig geteilt werden.
- Einstufungen werden nie überprüft, obwohl Prozesse und Systeme sich ändern.
- Datenschutz und Legal werden erst nach einem Fehlversand einbezogen.
- Management erhält keine Sicht auf Schutzbedarfskonflikte.

## Fiktives Mini-Beispiel

Ein fiktiver Fachbereich führt ein Lieferantenportal ein. Im Projektstart werden Vertragsunterlagen, Supporttickets und technische Schnittstellendaten als Informationsarten erfasst. Der Prozess Owner stuft Vertragsunterlagen als vertraulich und Schnittstellenschlüssel als streng vertraulich ein. Daraus folgen eingeschränkte Ablageorte, ein Freigabeprozess für externe Weitergabe und ein Datenschutz-/Legal-Handoff für personenbezogene Supportdaten. Eine Stichprobe nach drei Monaten findet zwei falsch abgelegte Dokumente; der Fachbereich korrigiert die Ablage und ergänzt ein Kurzbriefing.

Evidenz:

- Informationsasset-Einträge mit Owner und Klasse,
- Einstufungsentscheidung im Projektprotokoll,
- Schutzmaßnahmen je Klasse,
- Stichprobenergebnis,
- Korrekturmaßnahme und Kurzbriefing.
