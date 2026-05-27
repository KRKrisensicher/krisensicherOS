
# A.8.3 — Zugriff auf Informationen einschränken

## Zweck

Informationen müssen dort zugänglich sein, wo sie für legitime Aufgaben gebraucht werden — und dort begrenzt werden, wo Zugriff unnötig, riskant oder nicht entschieden ist. Diese Routine verbindet Informationsklassifizierung, Rollen, Speicherorte, Anwendungen und technische Zugriffskontrollen zu einer prüfbaren Arbeitsweise.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der Zugriff auf Informationen nach Geschäftsbedarf, Schutzbedarf, Rollen, Datenablage und Risiko eingeschränkt wird. Fachliche Owner entscheiden, IT setzt kontrolliert um, Reviews prüfen tatsächliche Zugriffe, und Ausnahmen werden befristet und nachvollziehbar behandelt.

## Typische Risiken

- Wenn sensible Informationen in offenen Ablagen liegen, können zu viele Personen mitlesen, kopieren oder verändern.
- Wenn Rollen- und Schutzbedarf nicht verbunden sind, werden Berechtigungen zu breit oder dauerhaft vergeben.
- Wenn Daten in Schattenablagen, Exporten oder Kollaborationstools landen, umgehen sie die vorgesehene Zugriffskontrolle.
- Wenn externe oder projektbezogene Zugriffe nicht befristet sind, bleiben Informationen nach Bedarfende offen.
- Wenn Reviews nur Gruppenlisten prüfen, aber Datenablagen und Informationswerte nicht verstehen, entstehen Scheinkontrollen.

## Trigger

- neue Datenablage, Anwendung, Share, Datenbank, Bericht, Schnittstelle oder Kollaborationsraum.
- neue Datenklasse, neues Projekt, neue Rolle oder geänderte Schutzbedarfsbewertung.
- Eintritt, Rollenwechsel, Austritt oder Ende externer Mitarbeit.
- Datenmigration, Cloud-/SaaS-Einführung, neue Schnittstelle oder Reporting-Export.
- Sicherheitsereignis, Fehlfreigabe, Auditfinding oder Datenschutzfrage.
- turnusmäßiger Review kritischer Informationsbestände und Zugriffsgruppen.

## Rollen und Verantwortung

- **Information Owner / Data Owner:** legt Schutzbedarf, zulässige Rollen und Freigabelogik fest.
- **Prozess-/Fachbereichsowner:** bestätigt Geschäftsbedarf und projektbezogene Zugriffe.
- **IT-/Plattform Owner:** setzt technische Zugriffsbeschränkungen, Gruppen und Ablagen um.
- **ISMS-Owner / Security-Rolle:** definiert Mindestlogik, Reviewfrequenzen, Ausnahmen und Evidenzanforderungen.
- **Datenschutz / Legal:** prüft personenbezogene, vertrauliche oder vertraglich gebundene Informationen und Auswertungen.
- **Management:** entscheidet bei Zielkonflikten zwischen Arbeitsfähigkeit, Transparenz, Schutzbedarf und Ressourcen.

## Implementierung

### Minimalstart

Ziel: kritische Informationen nicht in offenen oder ungeprüften Ablagen betreiben.

1. Die wichtigsten Informationsbestände im Scope werden benannt: Datenablagen, Anwendungen, Berichte, Schnittstellen oder Projektbereiche.
2. Für jeden kritischen Bestand gibt es einen Information Owner.
3. Der Owner legt zulässige Rollen oder Gruppen fest und begründet Abweichungen.
4. Neue Zugriffe werden per Ticket oder dokumentierter Freigabe vergeben.
5. Externe, projektbezogene und erhöhte Zugriffe sind befristet.
6. Kritische Ablagen werden regelmäßig auf offene Gruppen, Altzugriffe und unklare Owner geprüft.

Minimaler Nachweis:

- Liste kritischer Informationsbestände mit Owner,
- Zugriffsmodell oder Rollen-/Gruppenzuordnung,
- Freigabetickets,
- Reviewprotokoll kritischer Ablagen,
- Ausnahmeentscheidungen mit Ablaufdatum.

### Solide Praxis

Ziel: Zugriffseinschränkung wird mit Datenklassifizierung, Rollenmodell und Review verbunden.

1. Informationsbestände werden nach Schutzbedarf, Prozess, Datenklasse und Speicherort beschrieben.
2. Rollen- oder Gruppenmodelle bilden Standardzugriffe ab; Sonderzugriffe brauchen zusätzliche Freigabe.
3. Datenablagen und Kollaborationstools erhalten klare Regeln für Eigentümer, Freigabe, externe Links und Weitergabe.
4. Zugriffsreviews berücksichtigen tatsächliche Inhalte, externe Zugriffe, Projektlaufzeiten und Rollenwechsel.
5. Datenexporte, Berichte und Schnittstellen werden als eigene Zugriffspfade betrachtet.
6. Findings führen zu Bereinigung, Rollenmodell-Anpassung, Schulung oder Managemententscheidung.

Starke Evidenz:

- Informationsregister oder Datenablagenübersicht,
- Schutzbedarfs- und Rollenlogik,
- Gruppen-/Berechtigungsexporte zum Reviewzeitpunkt,
- Reviewentscheidungen mit Korrekturen,
- Nachweise zu entfernten offenen Links oder externen Zugängen,
- Ausnahme- und Maßnahmenlog.

### Fortgeschritten

Ziel: Informationszugriff wird kontinuierlich aus Datenkontext, Identität und Nutzungssignalen gesteuert.

1. Datenklassifizierung, IAM, DLP-/CASB-/SaaS-Reports und Assetregister liefern ein gemeinsames Lagebild.
2. Zugriff auf sensible Informationen wird risikobasiert durch Geräte-, Standort-, Rollen- oder Kontextsignale begrenzt.
3. Offene Freigaben, Massenexfiltration, ungewöhnliche Exporte oder externe Links lösen Triage aus.
4. Projekte und Datenräume haben automatische Ablauf- oder Rezertifizierungslogik.
5. Schnittstellen und technische Konten werden mit Datenumfang, Zweck und Owner reviewed.
6. Management sieht entscheidungsfähige Kennzahlen zu offenen Ablagen, externen Freigaben, Altzugriffen und Datenbewegungen.

## Ablauf als Routine

1. **Informationszugriff entsteht:** neuer Bestand, Projekt, Rolle, Bericht, Schnittstelle oder Freigabe.
2. **Information einordnen:** Owner, Schutzbedarf, Datenklasse, Speicherort und Geschäftsbedarf klären.
3. **Zugriffsmodell festlegen:** Standardrollen, Sonderzugriffe, externe Zugriffe, technische Zugänge und Ablaufdatum.
4. **Freigeben und umsetzen:** Fachliche Entscheidung dokumentieren, IT setzt Gruppen oder Kontrollen um.
5. **Nutzung prüfen:** offene Links, breite Gruppen, externe Zugriffe, Exporte und Altberechtigungen erkennen.
6. **Review durchführen:** bestätigen, einschränken, entziehen, befristen oder eskalieren.
7. **Ausnahmen steuern:** begründet, risikobewertet, mit Wiedervorlage und Kompensation.
8. **Verbessern:** Rollenmodell, Ablagenstruktur, Schulung oder Tooling anpassen.

## Entscheidungen

- Welche Informationen sind kritisch genug für einen priorisierten Start?
- Wer entscheidet über Zugriff auf Daten, wenn Prozess- und Systemowner auseinanderfallen?
- Welche Daten dürfen in Kollaborationstools, Exporte oder externe Freigaben?
- Welche Zugriffe sind standardisiert, welche brauchen Einzelfreigabe?
- Wie lange gelten Projekt-, externe oder Sonderzugriffe?
- Wann wird Arbeitsfähigkeit höher gewichtet als strikte Einschränkung — und wer akzeptiert das Risiko?

## Evidenz

### Starke Evidenz

- Informations- oder Datenablagenregister mit Owner und Schutzbedarf,
- definierte Rollen-/Gruppenmodelle,
- genehmigte Zugriffsanträge mit Zweck und Laufzeit,
- technische Berechtigungsexporte oder SaaS-Reports,
- Reviewprotokolle mit Entzug, Einschränkung oder Bestätigung,
- Nachweise bereinigter offener Links, Altzugriffe oder externer Freigaben,
- Managemententscheidung bei Zielkonflikten oder dauerhaften Ausnahmen.

### Schwache Evidenz

- allgemeine Access-Policy ohne Informationsbezug,
- Berechtigungsliste ohne Erklärung der Daten oder Rollen,
- Screenshots einzelner Shares ohne Datum und Owner,
- Aussage „nur Fachbereich hat Zugriff“ ohne Export oder Review,
- Datenklassifizierung ohne technische Umsetzung.

### Evidenzlücken

- kritische Datenablagen ohne Information Owner,
- offene Gruppen wie „alle Mitarbeitenden“ ohne begründeten Bedarf,
- externe Links ohne Ablaufdatum,
- Berichte und Exporte außerhalb des Reviewscopes,
- technische Konten mit Datenzugriff ohne Zweck und Owner.

## Wirksamkeitsprüfung

Prüffragen:

- Sind kritische Informationsbestände und Owner bekannt?
- Kann erklärt werden, wer auf eine sensible Ablage zugreifen darf und warum?
- Werden externe, projektbezogene und technische Zugriffe befristet und reviewed?
- Führen Reviews zu tatsächlicher Bereinigung offener oder alter Zugriffe?
- Sind Datenexporte, Berichte und Schnittstellen als Zugriffspfade sichtbar?
- Werden Zielkonflikte zwischen Zusammenarbeit und Schutzbedarf entschieden statt informell gelöst?

Mögliche Kennzahlen:

- kritische Informationsbestände mit Owner und Reviewdatum,
- offene oder sehr breite Freigaben,
- externe Zugriffe ohne Ablaufdatum,
- überfällige Zugriffsreviews,
- entfernte Altberechtigungen,
- Ausnahmen nach Datenklasse oder Fachbereich.

## BSIG-/NIS2-Anschluss

Eingeschränkter Informationszugriff ist anschlussfähig an NIS2-orientierte Themen wie Zugriffsschutz, Risikomanagement, Cyberhygiene, Schutz kritischer Informationen, Incident-Prävention und sichere Lieferketten-/Dienstleisterzugriffe. Der konkrete Bezug sollte im Anforderungsregister, in Datenklassifizierung und im Zugriffskonzept geprüft werden.

Dieses Artefakt ersetzt keine rechtliche oder datenschutzrechtliche Bewertung von Datenverarbeitung, Beschäftigtenauswertungen oder Offenlegungspflichten.

## Grenzen

- Dieses Artefakt ist kein vollständiges Rollenmodell und keine DLP-Architektur.
- Es ersetzt keine Datenschutz-, Geheimschutz-, Vertrags- oder Rechtsprüfung.
- Es trifft keine Zertifizierungs- oder Konformitätszusage.
- Es enthält keine echten Datenablagen, Kundeninformationen oder internen Berechtigungslisten.
- Eine Policy ohne technische Umsetzung und Review ist keine wirksame Zugriffseinschränkung.

## Handoffs

- **Access-/IAM-Handoff:** Rollen, Gruppen, Joiner-Mover-Leaver, technische Konten.
- **Datenschutz-/Legal-Handoff:** personenbezogene Daten, vertrauliche Informationen, externe Freigabe, Vertragsbindung.
- **Fachbereichs-Handoff:** Ownerentscheidung, Geschäftsbedarf, Projektlaufzeit und Datenqualität.
- **DLP-/Monitoring-Handoff:** offene Links, ungewöhnliche Exporte, Massenbewegungen oder externe Weitergabe.
- **Incident-Handoff:** Fehlfreigabe, unbefugter Zugriff, Datenabflussverdacht.
- **Management-Handoff:** breite Freigaben aus Arbeitsfähigkeitsgründen, Ressourcen- oder Toolkonflikte, akzeptierte Restrisiken.
- **Audit-/Evidence-Handoff:** fehlende Owner, fehlender Review oder unklare Ausnahmebehandlung.

## Typische Fehler

- Zugriff wird systemzentriert geprüft, obwohl Daten an mehreren Orten liegen.
- Offene Kollaborationsräume werden als Kulturfrage statt als Schutzbedarfsentscheidung behandelt.
- Externe Links und Projekträume laufen nach Projektende weiter.
- Datenexporte und BI-Berichte umgehen das eigentliche Berechtigungskonzept.
- Fachbereiche bestätigen Berechtigungen pauschal, weil Rollen unverständlich sind.
- Datenklassifizierung wird gepflegt, aber nicht mit Zugriffskontrollen verbunden.
- Technische Konten und Schnittstellen werden im Review vergessen.

## Fiktives Mini-Beispiel

Ein fiktiver Hersteller führt einen neuen Projektraum für Produktdaten ein. Der Information Owner ordnet die Daten als intern kritisch ein und legt drei Rollen fest: Kernteam, Leserechte für Support und zeitlich begrenzter externer Zugriff für einen Dienstleister. Beim ersten Review fällt auf, dass ein öffentlicher Freigabelink für einen Export existiert. Der Link wird entfernt, der Exportprozess angepasst und externe Zugriffe erhalten künftig ein Ablaufdatum.

Evidenz:

- Eintrag im Informationsregister,
- Rollen- und Freigabeentscheidung,
- Berechtigungsexport zum Review,
- Ticket zur Entfernung des Freigabelinks,
- Anpassung des Exportprozesses,
- Reviewnotiz zu Ablaufdaten für externe Zugriffe.
