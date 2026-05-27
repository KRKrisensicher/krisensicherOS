
# A.7.4 — Physische Sicherheitsüberwachung

## Zweck

Physische Sicherheitsüberwachung sorgt dafür, dass relevante Ereignisse an Standorten, Zugängen und geschützten Bereichen nicht unbemerkt bleiben. Der Wert liegt nicht im Vorhandensein von Kameras, Sensoren oder Wachrunden, sondern in einer geklärten Routine: Was wird beobachtet, warum, durch wen, wie wird reagiert und welche Nachweise entstehen?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine angemessene Überwachungsroutine für physische Sicherheitsereignisse an Standorten und geschützten Bereichen. Sie verbindet Risikoanalyse, Überwachungsmittel, Reaktionswege, Datenschutz-/Legal-Handoffs, Dienstleistersteuerung, Review und Managemententscheidungen.

## Typische Risiken

- Wenn unbefugte Zutrittsversuche, Türalarme oder Manipulationen nicht erkannt werden, bleiben Angriffe oder Fehlverhalten ohne Reaktion.
- Wenn Überwachungstechnik vorhanden ist, aber niemand Alarme bewertet, entsteht Scheinsicherheit.
- Wenn Kamera-, Zutritts- oder Sensordaten ohne klare Zwecke verarbeitet werden, entstehen Datenschutz-, Akzeptanz- und Governance-Probleme.
- Wenn Dienstleisteralarme nicht mit internen Eskalationswegen verbunden sind, gehen kritische Ereignisse in Übergaben verloren.
- Wenn Aufzeichnungen nicht geschützt oder zu lange aufbewahrt werden, können sie selbst zum Risiko werden.

## Trigger

- neuer Standort, neuer geschützter Bereich oder geänderte Zutrittslogik.
- Sicherheitsereignis, Einbruch, Sabotageverdacht, Vandalismus, Diebstahl oder wiederholte Fehlalarme.
- Einführung, Änderung oder Abschaltung von Kamera-, Alarm-, Sensor- oder Zutrittssystemen.
- Wechsel von Sicherheitsdienst, Empfang, Facility-Dienstleister oder Leitstelle.
- Datenschutz-/Legal-Review, Betriebsrats-/Mitbestimmungsfrage oder Beschwerde.
- turnusmäßiger Test von Alarmierung, Reaktionszeit oder Aufzeichnungszugriff.
- Auditfinding, Risikoanalyse, BCM-Review oder Managemententscheidung.

## Rollen und Verantwortung

- **Standort-/Facility Owner:** verantwortet Überwachungsbedarf, Betrieb der physischen Systeme und Dienstleisterkoordination.
- **Security-/ISMS-Owner:** definiert Risikologik, Ereigniskategorien, Eskalationswege und Reviewanforderungen.
- **Datenschutz / Legal:** prüft Zwecke, Rechtsgrundlagen, Betroffeneninformationen, Aufbewahrung, Zugriffe und Mitbestimmungsfragen.
- **Sicherheitsdienst / Leitstelle / Empfang:** bewertet Ereignisse nach Vorgabe und eskaliert definierte Fälle.
- **IT-/Plattform Owner:** unterstützt bei Systemschutz, Protokollierung, Schnittstellen und Zugriffen auf Überwachungssysteme.
- **Incident Response:** übernimmt bei Verdacht auf Angriff, Sabotage, Informationsabfluss oder Zusammenhang mit Cyberereignissen.
- **Management:** entscheidet über Investitionen, Restrisiken, Überwachungsumfang und Zielkonflikte.

## Implementierung

### Minimalstart

Ziel: Kritische physische Ereignisse werden erkannt, bewertet und nachvollziehbar eskaliert.

1. Die Organisation benennt die Standorte und Bereiche, bei denen physische Überwachung relevant ist.
2. Für jeden Bereich wird festgelegt, welche Ereignisse wichtig sind: Tür offen, Zutritt außerhalb Zeitfenster, Einbruchalarm, Technikraumöffnung, Lieferantenzugang.
3. Bestehende Überwachungsmittel werden erfasst: Empfang, Wachgang, Zutrittssystem, Alarmanlage, Kamera, Sensor, Dienstleistermeldung.
4. Eine einfache Ereignis- und Eskalationslogik beschreibt, wer wann informiert wird.
5. Datenschutz-/Legal-Handoff wird ausgelöst, sobald personenbezogene Überwachungsdaten verarbeitet werden.
6. Mindestens ein regelmäßiger Funktionstest oder Review prüft, ob Meldung und Reaktion funktionieren.

Minimaler Nachweis:

- Scope der überwachten Bereiche,
- Ereignis- und Eskalationsmatrix,
- Dienstleister- oder Betriebsanweisung,
- Test- oder Alarmprotokoll,
- Datenschutz-/Legal-Klärung, falls personenbezogene Daten betroffen sind.

### Solide Praxis

Ziel: Überwachung wird risikobasiert, reaktionsfähig und kontrolliert betrieben.

1. Überwachungszwecke werden pro Bereich dokumentiert und mit Risiken verknüpft.
2. Ereigniskategorien erhalten Reaktionsfristen, Eskalationspunkte und Dokumentationspflichten.
3. Zugriff auf Aufzeichnungen, Alarmdaten und Systeme wird begrenzt, protokolliert und regelmäßig reviewed.
4. Fehlalarme, ausgebliebene Reaktionen und technische Störungen werden ausgewertet.
5. Dienstleisterleistungen werden über definierte Meldewege, Berichte und Reviewtermine gesteuert.
6. Aufbewahrung, Löschung und Auswertung von personenbezogenen Daten werden mit Legal/Datenschutz geklärt.
7. Ergebnisse fließen in Standort-, Zutritts-, Incident- und BCM-Reviews ein.

Starke Evidenz:

- risikobezogener Überwachungsscope,
- Ereignis-/Eskalationsmatrix,
- Alarm- oder Wachprotokolle mit Reaktion,
- Testnachweise für Alarme und Meldeketten,
- Zugriffsreview für Überwachungssysteme,
- Datenschutz-/Legal-Freigabe oder Prüfnotiz,
- Maßnahmen aus Störungen oder Fehlalarmen.

### Fortgeschritten

Ziel: Physische Überwachung unterstützt Lagebild, Incident Response und Standortresilienz ohne ausufernde Kontrolle.

1. Alarm-, Zutritts-, Sensor- und Dienstleistermeldungen werden in ein abgestimmtes Lage- und Eskalationsmodell integriert.
2. Kritische Ereignisse werden mit Cyber-Incident-Triage, BCM und Krisenkommunikation verbunden.
3. Technische Systeme werden gegen Manipulation, Ausfall und unbefugten Zugriff geschützt.
4. Kennzahlen zeigen Reaktionszeiten, Fehlalarmquote, offene Störungen, ungeklärte Ereignisse und Dienstleisterleistung.
5. Übungen testen Meldeketten außerhalb regulärer Geschäftszeiten.
6. Überwachungsumfang wird regelmäßig gegen Zweckbindung, Verhältnismäßigkeit, Risiko und Akzeptanz reviewed.

## Ablauf als Routine

1. **Überwachungsbedarf entsteht:** Standort, Raum, Ereignis, Risiko oder Dienstleister ändert sich.
2. **Zweck und Scope bestimmen:** Welche Bereiche und Ereignisse sollen aus welchem Grund überwacht werden?
3. **Datenschutz-/Legal-Handoff prüfen:** Personenbezug, Aufzeichnung, Auswertung, Beschäftigtenkontext und Aufbewahrung klären.
4. **Ereignislogik festlegen:** Kategorie, Reaktionsweg, Eskalation, Dokumentation und Verantwortliche definieren.
5. **Betrieb sicherstellen:** Technik, Dienstleister, Empfang oder Wachroutine einrichten.
6. **Ereignisse bearbeiten:** Alarm bewerten, reagieren, dokumentieren, gegebenenfalls Incident auslösen.
7. **Nachweise schützen:** Zugriff auf Protokolle und Aufzeichnungen begrenzen und nachvollziehbar halten.
8. **Wirksamkeit prüfen:** Tests, Stichproben, Fehlalarmreview und Lessons Learned durchführen.
9. **Verbessern:** Technik, Prozesse, Dienstleistervorgaben oder Standortschutz anpassen.

## Entscheidungen

- Welche Bereiche brauchen Überwachung und welche ausdrücklich nicht?
- Welche Ereignisse sind sicherheitsrelevant genug für Alarmierung oder Eskalation?
- Wer darf Aufzeichnungen einsehen und unter welchen Bedingungen?
- Wie lange werden Ereignis- und Aufzeichnungsdaten aufbewahrt?
- Wann wird ein physisches Ereignis zum Security Incident oder BCM-Thema?
- Welche Zielkonflikte bestehen zwischen Schutzbedarf, Datenschutz, Kosten und Arbeitskultur?

## Evidenz

### Starke Evidenz

- aktueller Überwachungsscope mit Zweck und Owner,
- Ereignis- und Eskalationsmatrix,
- Alarm-, Test- oder Wachprotokolle mit dokumentierter Reaktion,
- Nachweis korrigierter Störungen oder Fehlalarme,
- Zugriffs- und Rollenreview für Überwachungssysteme,
- Datenschutz-/Legal-Prüfnotiz,
- Managemententscheidung bei Ausweitung, Einschränkung oder Restrisiko.

### Schwache Evidenz

- Kameras oder Alarmanlage ohne definierte Reaktionsroutine,
- Dienstleistervertrag ohne Ereignisberichte,
- Screenshots eines Systems ohne Test oder Alarmfall,
- Protokolle ohne Bewertung oder Nachverfolgung,
- allgemeine Aussage „wird überwacht“ ohne Zweck und Verantwortliche.

### Evidenzlücken

- keine Klärung personenbezogener Überwachungsdaten,
- Alarme laufen auf unbesetzte Postfächer oder unklare Rufnummern,
- Aufzeichnungen ohne Zugriffsbeschränkung,
- Fehlalarme werden ignoriert,
- technische Störungen ohne Maßnahmenlog,
- Dienstleistermeldungen ohne interne Bewertung.

## Wirksamkeitsprüfung

Prüffragen:

- Werden relevante physische Ereignisse tatsächlich erkannt und an die richtige Stelle gemeldet?
- Sind Reaktionswege auch außerhalb normaler Arbeitszeiten klar?
- Sind Zweck, Zugriff, Aufbewahrung und Auswertung von Überwachungsdaten geklärt?
- Führen Fehlalarme und Störungen zu Verbesserungen?
- Sind Dienstleisterleistungen messbar und reviewed?
- Werden physische Sicherheitsereignisse mit Incident Response und BCM verbunden?

Mögliche Kennzahlen:

- erfolgreich getestete Alarmketten,
- mittlere Reaktionszeit auf kritische Alarme,
- Fehlalarmquote,
- offene Störungen an Überwachungssystemen,
- überfällige Zugriffsreviews,
- ungeklärte Ereignisse nach Standort oder Bereich.

## BSIG-/NIS2-Anschluss

Physische Sicherheitsüberwachung ist anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Schutz kritischer Betriebsumgebungen, Incident Handling, Business Continuity und Governance von Sicherheitsmaßnahmen. Der konkrete Bezug ist im Anforderungsregister, in der Risikoanalyse und bei personenbezogenen Daten mit Human Review zu prüfen.

Dieses Artefakt ersetzt keine Rechts-, Datenschutz- oder Mitbestimmungsprüfung.

## Grenzen

- Dieses Artefakt ist keine Kamera- oder Alarmanlagenplanung.
- Es ersetzt keine Datenschutz-Folgenabschätzung, Rechtsprüfung oder Mitbestimmungsklärung.
- Es garantiert keine lückenlose Erkennung physischer Angriffe.
- Es enthält keine Zertifizierungszusage und keine ISO-27002-Texte.
- Öffentliche Beispiele enthalten keine realen Standort- oder Sicherheitsdetails.

## Handoffs

- **Datenschutz-/Legal-Handoff:** Video, Zutrittslogs, Beschäftigtendaten, Aufbewahrung, Auskunft, Mitbestimmung.
- **Facility-/Sicherheitsdienst-Handoff:** Alarmtechnik, Wachrunden, Leitstelle, Empfang, Wartung.
- **IT-Handoff:** Systemzugriffe, Protokollschutz, Netzwerkanbindung, Ausfallsicherheit der Überwachungstechnik.
- **Incident-Handoff:** Einbruch, Sabotage, Manipulation, unbefugter Zutritt, Zusammenhang mit Cyberereignis.
- **BCM-Handoff:** Ausfall von Standort, Leitstelle, Alarmierung oder kritischer Zutrittsüberwachung.
- **Management-Handoff:** Ausweitung der Überwachung, Kosten, Restrisiken, Akzeptanz- oder Zielkonflikte.
- **Audit-/Evidence-Handoff:** fehlende Testnachweise, unklare Aufbewahrung oder nicht nachvollziehbare Reaktion.

## Typische Fehler

- Technik wird beschafft, bevor Zweck, Reaktion und Datenschutz geklärt sind.
- Alarme werden erzeugt, aber niemand ist für Bewertung und Nachverfolgung verantwortlich.
- Aufzeichnungen sind verfügbar, aber Zugriffe darauf werden nicht gesteuert.
- Fehlalarme führen zu Alarmmüdigkeit und werden nicht analysiert.
- Dienstleisterberichte werden abgelegt, aber nicht in Risikoreviews genutzt.
- Überwachung wird ausgeweitet, ohne Managemententscheidung und Human Gate.

## Fiktives Mini-Beispiel

Ein fiktiver Betreiber eines kleinen Rechenraums stellt fest, dass Türalarme nachts an eine allgemeine Mailbox gesendet werden. Facility und ISMS-Owner definieren eine Eskalationsmatrix: außerhalb der Geschäftszeiten geht ein kritischer Alarm an die Leitstelle und an den IT-Bereitschaftskontakt. Datenschutz prüft die Verarbeitung der Zutrittslogs. Ein Test zeigt, dass die Meldekette funktioniert; zwei Fehlalarme führen zu einer Wartungsmaßnahme am Türkontakt.

Evidenz:

- Ereignis- und Eskalationsmatrix,
- Testprotokoll der Alarmkette,
- Datenschutz-Prüfnotiz zu Zutrittslogs,
- Wartungsticket für Türkontakt,
- Reviewnotiz im Standort-Sicherheitsreview.
