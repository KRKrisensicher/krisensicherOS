
# A.5.29 — Informationssicherheit bei Störungen und Krisen

## Zweck

Informationssicherheit bei Störungen und Krisen sorgt dafür, dass Sicherheitsanforderungen nicht verschwinden, sobald Zeitdruck, Ausfall, Notbetrieb oder Krisenkommunikation einsetzen. Ziel ist eine arbeitsfähige Krisenroutine, die Verfügbarkeit, Vertraulichkeit, Integrität, Nachvollziehbarkeit und Entscheidungsfähigkeit angemessen berücksichtigt.

## Control-Ziel in Repo-Sprache

Die Organisation integriert Informationssicherheit in Störungs-, Notfall- und Krisenabläufe. Kritische Sicherheitsrollen, Mindestkontrollen, Kommunikationswege, Ausnahmen, Entscheidungen und Nachweise sind so vorbereitet, dass sie auch unter Druck genutzt werden können.

## Typische Risiken

- Wenn Krisenpläne Sicherheitsfragen ausblenden, entstehen unsichere Notzugriffe, unkontrollierte Datenweitergaben oder nicht nachvollziehbare Entscheidungen.
- Wenn Notbetrieb improvisiert wird, bleiben Ausnahmen dauerhaft bestehen.
- Wenn Kommunikationskanäle ausfallen oder unsicher gewählt werden, können falsche Informationen, vertrauliche Daten oder Angriffsflächen entstehen.
- Wenn Rollen unklar sind, konkurrieren Incident Response, BCM, IT-Betrieb, Management und Fachbereiche um Entscheidungen.
- Wenn Wiederanlauf nur auf Verfügbarkeit optimiert wird, können kompromittierte Systeme zu früh zurückkehren.
- Wenn Krisenentscheidungen nicht dokumentiert werden, sind Restrisiken und Lessons Learned später nicht mehr nachvollziehbar.

## Trigger

- größere IT-Störung, Sicherheitsvorfall, Serviceausfall oder Krisenstabsaktivierung.
- Aktivierung eines Notfall-, Wiederanlauf- oder Krisenkommunikationsplans.
- Ausfall kritischer Sicherheitsfunktionen wie IAM, Monitoring, Backup, E-Mail oder Netzwerksegmentierung.
- geplante Notfall-, Krisen- oder Tabletop-Übung.
- wesentliche Architektur-, Dienstleister- oder Prozessänderung mit Auswirkungen auf Krisenfähigkeit.
- Managemententscheidung zu Notbetrieb, Priorisierung, Restrisiko oder externer Kommunikation.
- Review nach Störung, Krise oder Übung.

## Rollen und Verantwortung

- **Krisenstabsleitung / BCM-Rolle:** koordiniert Gesamtentscheidung, Prioritäten und Krisenroutinen.
- **ISMS-Owner / Security-Rolle:** hält Sicherheitsmindestanforderungen, Risikohinweise und Eskalationen sichtbar.
- **Incident Owner:** steuert Sicherheitsvorfälle und Abgrenzung zu reinen Betriebsstörungen.
- **Service Owner / Fachbereich:** bewertet Geschäftsfolgen, Notbetrieb und fachliche Prioritäten.
- **IT-Betrieb / Plattformteam:** stellt Wiederherstellung, technische Notmaßnahmen und Sicherheitsfunktionen bereit.
- **Kommunikation / HR / Legal / Datenschutz:** prüfen interne und externe Kommunikation, Beschäftigten- und Datenschutzfragen.
- **Management:** entscheidet bei Zielkonflikten, Ressourcen, Risikoakzeptanz und öffentlicher oder behördlicher Kommunikation.

## Implementierung

### Minimalstart

Ziel: Sicherheitsentscheidungen in Störung und Krise nicht vergessen.

1. Kritische Störungs- und Krisenszenarien benennen: Ausfall Identität, Ransomware-Verdacht, Cloud-Ausfall, Kommunikationsausfall, Datenabflussverdacht.
2. In bestehende Notfallkontakte eine Security- und ISMS-Rolle aufnehmen.
3. Für Notbetrieb Mindestregeln definieren: Notzugriffe, Datenweitergabe, Kommunikationskanäle, Protokollierung, spätere Rücknahme.
4. Krisenentscheidungen in einem Ereignislog dokumentieren: Entscheidung, Zeitpunkt, Rolle, Begründung, Restrisiko.
5. Nach Störung oder Übung eine kurze Sicherheitsnachbereitung durchführen.
6. Ausnahmen aus dem Notbetrieb mit Frist und Owner zurückführen.

Minimaler Nachweis:

- Krisenkontaktliste mit Security-Rolle,
- Sicherheitscheckliste für Notbetrieb,
- Ereignis- oder Entscheidungslog,
- Ausnahme- und Rückführungsnachweis,
- Lessons-Learned-Notiz.

### Solide Praxis

Ziel: Informationssicherheit wird fest in BCM, Incident Response und Krisenmanagement verankert.

1. Krisenpläne enthalten Sicherheitsprüfpunkte für Wiederanlauf, Notzugriffe, Kommunikation, Datenabzug und Dienstleister.
2. Rollen und Eskalationswege zwischen Incident Response, BCM, IT-Betrieb und Management sind abgestimmt.
3. Kritische Sicherheitsfunktionen haben Ausweich- oder Mindestbetriebsverfahren.
4. Krisenübungen enthalten Security-Injektionspunkte: kompromittierte Identität, unsichere Kommunikation, nicht vertrauenswürdiges Backup, Lieferantenausfall.
5. Entscheidungen zu Abweichungen von Sicherheitsregeln werden befristet, begründet und reviewed.
6. Lessons Learned fließen in ISMS, BCM, Awareness, Lieferantenmanagement und technische Architektur zurück.

### Fortgeschritten

Ziel: Die Organisation hält Sicherheitsgovernance auch in komplexen Krisenlagen entscheidungsfähig.

1. Sicherheitslagebild, Betriebsstatus und Geschäftsfolgen werden in Krisenentscheidungen gemeinsam betrachtet.
2. Wiederanlaufkriterien verbinden Verfügbarkeit mit Vertrauenswürdigkeit, Integrität und Monitoringfähigkeit.
3. Notfallkommunikation ist mit sicheren Alternativkanälen, Freigaben und Informationsklassifizierung vorbereitet.
4. Krisenübungen prüfen mehrere parallele Belastungen, etwa Ransomware, Cloud-Ausfall und Medienanfrage.
5. Krisenentscheidungen werden strukturiert ausgewertet: War die Sicherheitsrolle früh genug eingebunden? Waren Nachweise verfügbar? Wurden Ausnahmen zurückgenommen?
6. Management erhält entscheidungsfähige Kennzahlen zu Krisenfähigkeit, offenen Schwachstellen und Wiederanlaufrestrisiken.

## Ablauf als Routine

1. **Störung oder Krise erkennen:** Ereignis wird als Betriebsstörung, Sicherheitsvorfall oder kombinierte Lage eingeordnet.
2. **Rollen aktivieren:** Krisenstab, Incident Owner, ISMS/Security, Service Owner und Kommunikation einbinden.
3. **Sicherheitslage klären:** betroffene Assets, Daten, Zugriffe, Integrität, Monitoring, Dienstleister und Kommunikationskanäle bewerten.
4. **Notbetrieb entscheiden:** Mindestkontrollen, Ausnahmen, manuelle Workarounds und Protokollierung festlegen.
5. **Wiederanlauf steuern:** nicht nur Verfügbarkeit, sondern Vertrauenswürdigkeit und Kontrollfähigkeit prüfen.
6. **Kommunikation freigeben:** intern und extern abgestimmt, mit Legal-/Datenschutz-Handoff bei sensiblen Inhalten.
7. **Entscheidungen dokumentieren:** Zeitpunkt, Rolle, Begründung, Risiko, Laufzeit und Wiedervorlage erfassen.
8. **Rückkehr in Normalbetrieb:** Notzugriffe, Workarounds und Ausnahmen zurücknehmen oder bewusst verlängern.
9. **Nachbereiten:** Sicherheits-Lessons-Learned und Maßnahmen ableiten.

## Entscheidungen

- Welche Sicherheitsmindestanforderungen gelten auch im Notbetrieb?
- Wann darf Verfügbarkeit vor Sicherheit priorisiert werden, und wer akzeptiert das Restrisiko?
- Welche Systeme dürfen nach einem Sicherheitsverdacht wieder online gehen?
- Welche Kommunikationskanäle sind für Kriseninformationen zulässig?
- Welche Notzugriffe werden erlaubt, protokolliert und nachträglich überprüft?
- Wann wird aus einer Störung ein Sicherheitsvorfall oder eine melde-/kommunikationsrelevante Lage?
- Welche Dienstleister müssen in Krisenentscheidungen eingebunden werden?

## Evidenz

### Starke Evidenz

- Krisen- oder Notfallplan mit Sicherheitsrollen und Sicherheitsprüfpunkten,
- Ereignis- und Entscheidungslog,
- dokumentierte Notzugriffe und deren Rücknahme,
- Wiederanlaufcheck mit Integritäts- und Sicherheitsbewertung,
- Übungsprotokoll mit Security-Szenarien,
- Maßnahmen aus Lessons Learned,
- Managemententscheidung zu Restrisiken oder Ressourcen.

### Schwache Evidenz

- allgemeiner Krisenplan ohne Security-Rolle,
- Chatverlauf als einzige Entscheidungsgrundlage,
- Wiederanlaufnotiz ohne Integritäts- oder Zugriffsbewertung,
- Kommunikationsentwurf ohne Freigabe- und Klassifizierungslogik,
- Übung ohne Auswertung oder Maßnahmen.

### Evidenzlücken

- Notzugriffe werden nicht protokolliert oder zurückgenommen,
- Ausnahmen aus der Krise bleiben dauerhaft aktiv,
- Security wird erst nach Wiederanlauf eingebunden,
- keine sichere Alternativkommunikation,
- keine Abgrenzung zwischen Störung, Sicherheitsvorfall und Krise,
- fehlende Dokumentation von Risikoentscheidungen unter Zeitdruck.

## Wirksamkeitsprüfung

Prüffragen:

- Ist Informationssicherheit in Krisenrollen, Checklisten und Übungen sichtbar eingebunden?
- Werden Sicherheitsausnahmen im Notbetrieb dokumentiert, befristet und zurückgeführt?
- Werden Wiederanlaufentscheidungen auch an Integrität und Kontrollfähigkeit gemessen?
- Funktionieren Kommunikations- und Eskalationswege unter Ausfallbedingungen?
- Werden Krisenentscheidungen später nachvollziehbar ausgewertet?
- Fließen Erkenntnisse in ISMS, BCM, Incident Response und Architektur zurück?

Mögliche Kennzahlen:

- Anteil Krisenübungen mit Security-Szenario,
- offene Maßnahmen aus Krisen-Lessons-Learned,
- überfällige Rücknahmen von Notzugriffen,
- Zeit bis Einbindung Security/ISMS in kritischer Lage,
- kritische Services mit Wiederanlauf-Sicherheitscheck,
- nicht dokumentierte Krisenentscheidungen aus Stichprobe.

## BSIG-/NIS2-Anschluss

Diese Routine ist anschlussfähig an NIS2-orientierte Themen wie Business Continuity, Krisenmanagement, Incident Handling, Aufrechterhaltung wesentlicher Dienste, sichere Kommunikation und Governance unter außergewöhnlichen Bedingungen.

Für betroffene Organisationen sollte der konkrete Bezug im Anforderungsregister, im BCM-Kontext und im Management Review geprüft werden. Dieses Artefakt ersetzt keine rechtliche Bewertung von Meldepflichten, Betroffenheit oder Kommunikationspflichten.

## Grenzen

- Dieses Artefakt ist kein vollständiger BCM- oder Krisenstabsplan.
- Es ersetzt keine Rechts-, Datenschutz-, Kommunikations- oder Arbeitsschutzprüfung.
- Es garantiert keine Verfügbarkeit, Sicherheit oder Konformität in Krisenlagen.
- Es beschreibt keine verbindlichen Meldepflichten.
- Es nutzt ausschließlich fiktive, public-safe Beispiele.

## Handoffs

- **BCM-Handoff:** Aktivierung von Notfallplänen, Wiederanlauf, Priorisierung kritischer Prozesse.
- **Incident-Handoff:** Kompromittierungsverdacht, Datenabfluss, Manipulation oder Angriffsindikatoren.
- **IT-Betriebs-Handoff:** Notzugriffe, Wiederherstellung, Monitoring, Backup, technische Workarounds.
- **Kommunikations-Handoff:** interne Lagekommunikation, Kundeninformation, Medienanfragen oder Stakeholderkommunikation.
- **Legal-/Datenschutz-Handoff:** Meldepflichtverdacht, personenbezogene Daten, Vertragsfragen, externe Aussagen.
- **Management-Handoff:** Zielkonflikte, Risikoakzeptanz, Ressourcen, externe Kommunikation und Priorisierung.
- **Evidence-Handoff:** Ereignislog, Entscheidungsnachweise, Übungs- und Lessons-Learned-Unterlagen.

## Typische Fehler

- Krisenmanagement konzentriert sich nur auf Verfügbarkeit.
- Notzugriffe werden eingerichtet, aber nicht überprüft oder zurückgenommen.
- Kommunikation nutzt schnelle, aber ungeeignete Kanäle für vertrauliche Informationen.
- Systeme gehen wieder online, ohne Integrität oder Kompromittierungsverdacht zu prüfen.
- Security wird als Bremse gesehen und deshalb zu spät eingebunden.
- Übungen enden mit einem guten Gefühl, aber ohne Maßnahmenlog.
- Managemententscheidungen unter Zeitdruck werden nicht dokumentiert.

## Fiktives Mini-Beispiel

Ein fiktiver Produktionsdienstleister verliert während einer größeren Störung den Zugriff auf das zentrale Identitätssystem. Der Krisenstab aktiviert ein Notverfahren für zwei Administrationskonten, begrenzt auf vier Stunden und mit manueller Protokollierung. Der ISMS-Owner ergänzt einen Sicherheitscheck für den Wiederanlauf: Protokolle prüfen, Notzugriffe entziehen, Monitoring bestätigen. Nach der Übung wird entschieden, einen sicheren Alternativkanal für Krisenkommunikation einzuführen.

Evidenz:

- Krisenentscheidungslog,
- Notzugriffsfreigabe mit Laufzeit,
- Protokoll der Rücknahme,
- Wiederanlauf-Sicherheitscheck,
- Übungs-Lessons-Learned,
- Managemententscheidung zum Alternativkanal.
