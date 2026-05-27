
# A.6.6 — Vertraulichkeits- und Geheimhaltungsvereinbarungen

## Zweck

Vertraulichkeits- und Geheimhaltungsvereinbarungen schaffen eine klare Erwartung, welche Informationen geschützt werden müssen, wer darüber sprechen oder sie weitergeben darf und was bei Rollenwechsel, Projektende oder Vertragsende weiter gilt. Der Wert liegt nicht im unterschriebenen Formular allein, sondern in der Verbindung aus Schutzbedarf, Rolle, verständlicher Verpflichtung, Nachweis und Review.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der Vertraulichkeitspflichten für Beschäftigte, externe Mitarbeitende, Dienstleister, Projektpartner und andere beteiligte Rollen passend zum Informationsrisiko festgelegt, kommuniziert, nachgehalten und bei Änderungen überprüft werden.

## Typische Risiken

- Wenn Personen sensible Informationen erhalten, ohne ihre Vertraulichkeitspflichten zu kennen, können Daten unkontrolliert weitergegeben oder falsch verwendet werden.
- Wenn Vereinbarungen nicht zum Schutzbedarf der Informationen passen, bleiben besonders kritische Projekte, Kundeninformationen, Geschäftsgeheimnisse oder Sicherheitsdetails unzureichend abgesichert.
- Wenn externe Beteiligte nur technisch Zugriff erhalten, aber keine passende vertragliche oder organisatorische Bindung besteht, fehlt ein belastbarer Handlungsrahmen bei Fehlverhalten oder Vertragsende.
- Wenn Vertraulichkeitsregeln nach Rollenwechsel oder Austritt nicht erneut eingeordnet werden, entstehen blinde Flecken bei ehemaligen Projektmitgliedern oder Dienstleistern.
- Wenn Formulierungen ungeprüft kopiert werden, können rechtliche, arbeitsrechtliche oder datenschutzbezogene Fragen ungeklärt bleiben.

## Trigger

- Eintritt, Rollenwechsel, Projektstart, Projektende oder Austritt.
- Zugriff auf vertrauliche, interne, schutzbedürftige oder geschäftskritische Informationen.
- Beauftragung von Dienstleistern, Freelancern, Beratern, Prüfern oder Entwicklungspartnern.
- Einführung neuer Datenklassen, neuer Informationswerte oder neuer Kollaborationsräume.
- Sicherheitsereignis, Verdacht auf Informationsabfluss oder Regelverstoß.
- Vertragsänderung, Lieferantenwechsel oder Ende einer Zusammenarbeit.
- turnusmäßiger Review von HR-, Einkaufs-, Projekt- oder ISMS-Unterlagen.

## Rollen und Verantwortung

- **HR / People-Funktion:** integriert Vertraulichkeit in Onboarding, Rollenwechsel und Austritt.
- **Führungskraft / Projekt Owner:** bewertet, welche Informationen die Rolle oder das Projekt berührt und ob Zusatzpflichten nötig sind.
- **Information Owner / Asset Owner:** legt Schutzbedarf und erwartete Umgangsregeln für Informationswerte fest.
- **Einkauf / Vendor Management:** stellt sicher, dass externe Beteiligte vor Zugriff passend eingebunden sind.
- **ISMS-Owner / Security-Rolle:** definiert Mindestlogik, Datenklassenbezug, Evidenzanforderungen und Reviewpunkte.
- **Legal / Datenschutz:** prüft Vertrags-, Arbeitsrechts-, Geheimhaltungs- und Datenschutzfragen.
- **Management:** entscheidet bei Zielkonflikten, Ausnahmen, kritischen Projekten oder Restrisiken.

## Implementierung

### Minimalstart

Ziel: Für Personen mit Zugriff auf schutzbedürftige Informationen ist nachvollziehbar, welche Vertraulichkeitsbindung besteht.

1. Die Organisation benennt Datenklassen oder Informationsarten, für die Vertraulichkeit ausdrücklich geregelt sein muss.
2. Für Beschäftigte und externe Beteiligte wird festgelegt, wann eine Vertraulichkeitsvereinbarung oder ein entsprechender Vertragsbaustein erforderlich ist.
3. Onboarding und Dienstleisterfreigabe enthalten einen Prüfschritt vor Zugriffserteilung.
4. Nachweise werden zentral auffindbar gehalten: Person oder Organisation, Datum, Scope, Art der Vereinbarung, verantwortliche Stelle.
5. Ausnahmen werden nur befristet und mit Owner dokumentiert.

Minimaler Nachweis:

- Datenklassen- oder Schutzbedarfsbezug,
- Onboarding-/Vertragscheckliste,
- Nachweis der Verpflichtung oder Vereinbarung,
- Liste offener Ausnahmen,
- Reviewnotiz für kritische Rollen oder externe Zugriffe.

### Solide Praxis

Ziel: Vertraulichkeitspflichten werden risikobasiert und wiederholbar in HR-, Projekt- und Lieferantenprozesse eingebaut.

1. Rollen und Beteiligte werden nach Informationszugriff geclustert: Standardrolle, privilegierte Rolle, Projektrolle, externe Rolle, Prüferrolle.
2. Für erhöhte Risiken werden zusätzliche Hinweise oder Vereinbarungen ausgelöst, etwa bei Geschäftsgeheimnissen, Sicherheitsarchitektur, Kundendaten oder M&A-/Krisenthemen.
3. Vertraulichkeit wird mit Zugriffserteilung, Datenklassifizierung, Schulung und Austritt verknüpft.
4. Projektende, Lieferantenende und Rollenwechsel lösen eine Prüfung aus, ob Zugriffe, Unterlagen, Geräte und Ablagen bereinigt wurden.
5. Legal und Datenschutz prüfen Vorlagen, bevor sie produktiv verwendet oder wesentlich geändert werden.
6. Findings aus Incidents, Audits oder Lieferantenreviews fließen in Vorlagen und Prozesse zurück.

### Fortgeschritten

Ziel: Vertraulichkeit wird als laufende Governance über Informationswerte, Identitäten und externe Beziehungen gesteuert.

1. Vertraulichkeitsstatus, Rollen, Zugriff und Lieferantenbeziehung sind in HR-, IAM-, Vertrags- oder GRC-Prozessen verknüpft.
2. Kritische Projekte führen ein Beteiligtenregister mit Informationsscope, Verpflichtungsstatus, Zugriffen und Offboarding-Check.
3. Ausnahmen und fehlende Nachweise erzeugen Eskalationen vor Zugriffserteilung.
4. Management erhält Berichte zu kritischen Lücken, externen Beteiligten ohne aktuellen Nachweis und wiederkehrenden Prozessfehlern.
5. Lessons Learned aus Informationsabflüssen, Fehlversand oder Projektwechseln verbessern Schulung, Klassifizierung und Vertragsroutinen.

## Ablauf als Routine

1. **Informationsbezug erkennen:** Rolle, Projekt, Lieferant oder Zusammenarbeit benötigt Zugriff auf schutzbedürftige Informationen.
2. **Schutzbedarf einordnen:** Information Owner oder Projekt Owner ordnet Datenklasse, Kritikalität und Weitergaberisiko ein.
3. **Verpflichtungsbedarf prüfen:** HR, Einkauf oder Projektleitung prüft, welche Vereinbarung oder Vertragsklausel erforderlich ist.
4. **Human Review auslösen:** Legal, Datenschutz oder Arbeitnehmervertretung werden einbezogen, wenn Formulierung, Beschäftigtenbezug oder personenbezogene Daten betroffen sind.
5. **Nachweis erfassen:** Verpflichtung, Datum, Scope und verantwortliche Stelle werden dokumentiert.
6. **Zugriff freigeben:** Zugriff erfolgt erst nach erfülltem Prüfschritt oder dokumentierter Ausnahme.
7. **Änderung prüfen:** Rollenwechsel, Projektende, Austritt oder Vertragsende lösen Offboarding- und Nachweisprüfung aus.
8. **Verbessern:** Lücken, Verstöße oder unklare Vereinbarungen fließen in Prozess- und Vorlagenreview.

## Entscheidungen

- Welche Informationsarten benötigen explizite Vertraulichkeitsbindung?
- Welche Rollen oder externen Beteiligten brauchen zusätzliche Vereinbarungen?
- Darf Zugriff vor vollständigem Nachweis erfolgen, und wer akzeptiert das Risiko?
- Wie lange werden Nachweise aufbewahrt und wer darf sie einsehen?
- Welche Änderungen an Vorlagen benötigen Legal-, Datenschutz- oder Managementfreigabe?
- Wie wird mit Altverträgen oder alten Beschäftigtenunterlagen ohne klare Nachweise umgegangen?

## Evidenz

### Starke Evidenz

- aktuelle Datenklassen- oder Schutzbedarfslogik,
- Onboarding-, Projekt- oder Lieferantencheck mit Vertraulichkeitsprüfung,
- signierte oder anderweitig nachvollziehbar bestätigte Vereinbarung,
- Register kritischer externer Beteiligter mit Verpflichtungsstatus,
- Offboarding-Nachweis bei Rollen-, Projekt- oder Vertragsende,
- Ausnahmeentscheidung mit Laufzeit und Risikoakzeptanz,
- Legal-/Datenschutzreview bei neuen oder geänderten Vorlagen.

### Schwache Evidenz

- allgemeine Policy ohne Bezug zu Rollen oder Informationswerten,
- Vorlagenablage ohne Nachweis der Nutzung,
- pauschale Aussage „steht im Arbeitsvertrag“ ohne prüfbare Zuordnung,
- Lieferantenvertrag ohne Zugriffsscope oder Owner,
- alte Unterschriftenliste ohne Aktualität, Scope oder Verantwortlichen.

### Evidenzlücken

- externe Beteiligte mit Zugriff, aber ohne Vertraulichkeitsnachweis,
- kritische Projekte ohne Beteiligten- und Offboardingübersicht,
- keine Prüfung bei Rollenwechsel oder Vertragsende,
- unklare Zuständigkeit für Vorlagen und Nachweise,
- Ausnahmen ohne Ablaufdatum oder Managemententscheidung.

## Wirksamkeitsprüfung

Prüffragen:

- Können kritische Informationszugriffe einer passenden Vertraulichkeitsbindung zugeordnet werden?
- Wird die Prüfung vor Zugriffserteilung und bei externen Beteiligten wirksam durchgeführt?
- Sind Rollenwechsel, Projektende und Vertragsende in der Routine sichtbar?
- Werden Vorlagen und Sonderfälle durch geeignete menschliche Rollen geprüft?
- Gibt es nachvollziehbare Ausnahmen mit Wiedervorlage?
- Haben Incidents oder Findings zu Prozessverbesserungen geführt?

Mögliche Kennzahlen:

- Anteil kritischer Rollen mit aktuellem Nachweis,
- externe Beteiligte ohne vollständigen Nachweis,
- offene oder überfällige Ausnahmen,
- Nachweisquote bei Projektstart und Projektende,
- Findings aus Offboarding- oder Lieferantenreviews.

## BSIG-/NIS2-Anschluss

Vertraulichkeits- und Geheimhaltungsroutinen sind anschlussfähig an NIS2-orientierte Themen wie Governance, Risikomanagement, Lieferkettensicherheit, Zugriffsschutz, Schulung und Incident-Prävention. Der konkrete Bezug sollte im Anforderungsregister organisationsspezifisch geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Prüfung von Arbeitsverträgen, Geheimhaltungsvereinbarungen, Datenschutzfragen oder gesetzlichen Pflichten.

## Grenzen

- Dieses Artefakt ist keine Vertragsvorlage und keine Rechtsberatung.
- Es ersetzt keine Datenschutzprüfung und keine arbeitsrechtliche Bewertung.
- Es bestätigt keine Konformität, Zertifizierungsfähigkeit oder Wirksamkeit allein durch Unterschriften.
- Es enthält keine ISO-27002-Texte und keine vertraulichen Beispielklauseln.
- Es genügt nicht, wenn Zugriffspraxis und Offboarding nicht tatsächlich betrieben werden.

## Handoffs

- **HR-Handoff:** Eintritt, Rollenwechsel, Austritt, Personalakte oder Beschäftigtenverpflichtung.
- **Legal-Handoff:** Vertragsvorlagen, Geheimhaltungsumfang, Durchsetzbarkeit, Sonderfälle, Altverträge.
- **Datenschutz-Handoff:** personenbezogene Daten in Nachweisen, Vertragsdaten, Trainings- oder Zugriffsauswertungen.
- **Einkauf-/Vendor-Handoff:** externe Beteiligte, Dienstleisterzugriff, Projektpartner, Vertragsende.
- **Access-Handoff:** Zugriff darf erst nach geklärtem Verpflichtungsstatus oder dokumentierter Ausnahme erfolgen.
- **Incident-Handoff:** Verdacht auf Informationsabfluss, Fehlversand, unerlaubte Weitergabe oder Regelverstoß.
- **Management-Handoff:** kritische Ausnahmen, Altlasten, Zielkonflikte oder nicht akzeptable Restrisiken.
- **Audit-/Evidence-Handoff:** fehlende Nachweise, unklare Scopes oder nicht prüfbare Verpflichtungslogik.

## Typische Fehler

- Vertraulichkeit wird als einmalige Unterschrift behandelt und nicht mit Zugriffen verbunden.
- Externe Mitarbeitende starten im Projekt, bevor Vertrags- oder Verpflichtungsstatus geklärt ist.
- Besonders kritische Informationsarten erhalten keine zusätzliche Betrachtung.
- Rollenwechsel und Projektende lösen keine Offboarding-Prüfung aus.
- Vorlagen werden ohne Legal-/Datenschutzreview geändert.
- Nachweise liegen verteilt bei HR, Einkauf und Projektteams und sind im Review nicht auffindbar.
- Ausnahmen werden dauerhaft, weil keine Wiedervorlage gesetzt wurde.

## Fiktives Mini-Beispiel

Ein fiktives Softwareunternehmen startet ein Produktentwicklungsprojekt mit zwei externen Entwicklern. Der Product Owner stuft Architekturunterlagen und Roadmap als vertraulich ein. Einkauf prüft vor Zugriffserteilung den Vertragsstatus, Legal bestätigt die verwendete Vereinbarung, und der ISMS-Owner ergänzt die Entwickler in das Projektbeteiligtenregister. Beim Projektende bestätigt der Product Owner den Entzug der Zugriffe und die Rückgabe projektbezogener Unterlagen.

Evidenz:

- Projektbeteiligtenregister mit Informationsscope,
- Vertrags- oder Verpflichtungsnachweis,
- Legal-Review der Vorlage,
- Zugriffsticket nach erfülltem Prüfschritt,
- Offboarding-Nachweis zum Projektende.
