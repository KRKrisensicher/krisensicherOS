
# A.5.25 — Bewertung und Entscheidung bei Sicherheitsereignissen

## Zweck

Sicherheitsereignisse werden erst durch Bewertung und Entscheidung steuerbar. Diese Routine hilft, Meldungen, Alarme, Hinweise oder Verdachtsfälle nicht ungeordnet zu behandeln, sondern nachvollziehbar zu triagieren: Was ist passiert? Wie schwer ist es? Wer entscheidet? Wird daraus ein Sicherheitsvorfall, ein Risiko, eine Maßnahme oder ein Fehlalarm?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Triage- und Entscheidungsroutine für Sicherheitsereignisse. Ereignisse werden erfasst, bewertet, klassifiziert, priorisiert und an den passenden Bearbeitungsweg übergeben. Entscheidungen bleiben nachvollziehbar, insbesondere wenn eskaliert, geschlossen, beobachtet oder als Vorfall behandelt wird.

## Typische Risiken

- Wenn Ereignisse nicht bewertet werden, bleiben echte Vorfälle im Alarmrauschen liegen.
- Wenn jedes Ereignis gleich behandelt wird, werden Teams überlastet und kritische Fälle verzögern sich.
- Wenn Klassifikation und Entscheidung nicht dokumentiert werden, ist später nicht nachvollziehbar, warum nicht eskaliert wurde.
- Wenn Datenschutz, Legal oder Management zu spät eingebunden werden, entstehen Entscheidungs- und Kommunikationsrisiken.
- Wenn Fehlalarme nicht ausgewertet werden, verbessert sich Detektion nicht.

## Trigger

- Sicherheitsmeldung von Beschäftigten, Kunden, Lieferanten oder externen Stellen.
- Monitoring-, SIEM-, EDR-, Cloud-, IAM-, Netzwerk- oder Anwendungstreffer.
- Schwachstellenhinweis mit Ausnutzungsverdacht.
- Auffälliges Verhalten, Datenabflussverdacht, Kontokompromittierung oder Policy-Verstoß.
- Ergebnis aus Audit, Test, Übung oder Dienstleistermeldung.
- Neue Information zu einem bereits bewerteten Ereignis.

## Rollen und Verantwortung

- **Triage Owner / Security-Rolle:** nimmt Ereignisse an, bewertet Erstinformationen und schlägt Klassifikation vor.
- **Incident Lead:** übernimmt, wenn das Ereignis als Sicherheitsvorfall behandelt wird oder Eskalation nötig ist.
- **IT-/Plattform Owner:** liefert technische Einordnung, Logs, Systemstatus und erste Eindämmungsoptionen.
- **Service Owner / Fachbereich:** bewertet Geschäfts- und Prozessauswirkung.
- **ISMS-Owner / Risikoverantwortliche:** verbindet Ereignisse mit Risiken, Maßnahmen und Lessons Learned.
- **Legal / Datenschutz:** bewertet prüfungsbedürftige Rechts-, Datenschutz- oder Meldepflichtnähe.
- **Management:** entscheidet bei hoher Auswirkung, Restrisiko, externer Kommunikation, Ressourcen oder Krisenpotenzial.

## Implementierung

### Minimalstart

Ziel: jedes relevante Ereignis wird erfasst, bewertet und nachvollziehbar entschieden.

1. Ein Eingangskanal für Sicherheitsereignisse wird festgelegt.
2. Eine einfache Triagevorlage erfasst Quelle, Zeitpunkt, betroffene Systeme, erste Hinweise, mögliche Auswirkung und Sofortbedarf.
3. Ein kleines Bewertungsschema unterscheidet mindestens: Fehlalarm, Beobachtung, Sicherheitsereignis mit Maßnahme, Sicherheitsvorfall mit Eskalation.
4. Für jede Bewertung wird eine Entscheidung dokumentiert: schließen, nachforschen, eskalieren, Maßnahme anlegen oder Incident starten.
5. Datenschutz-/Legal- und Management-Handoffs werden als Stop-Punkte markiert.
6. Ereignisse werden regelmäßig auf Muster und wiederkehrende Ursachen geprüft.

Minimaler Nachweis:

- Ereignislog oder Ticketliste,
- Triageentscheidung,
- Klassifikation,
- Übergabe an Maßnahme oder Incident,
- dokumentierter Schließgrund bei Fehlalarm,
- Eskalationsnachweis bei kritischen Fällen.

### Solide Praxis

Ziel: Bewertung und Entscheidung werden konsistent, risikobasiert und reviewfähig.

1. Schweregrade werden anhand technischer Hinweise, Datenbezug, Exposition, Geschäftsauswirkung und Ausbreitungspotenzial definiert.
2. Triagefristen richten sich nach Schweregrad und Kritikalität.
3. Ereignisse werden mit Assets, Service Ownern, Datenklassen und Risiken verknüpft.
4. Klassifikationsentscheidungen werden durch Vier-Augen-Prinzip oder Review bei kritischen Fällen abgesichert.
5. Ereignisse mit Personenbezug, Datenabflussverdacht, Kundenwirkung oder externer Meldepflichtnähe lösen Human Review aus.
6. Wiederkehrende Ereignisse führen zu Detektionsverbesserung, Schulung, Schwachstellenbehandlung oder Risikoanpassung.

Starke Evidenz:

- definierte Klassifikations- und Schweregradlogik,
- Ereignistickets mit Bewertung und Entscheidung,
- Log- oder Analyseauszüge mit Bezug zum Fall,
- Übergaben an Incident Response, Change, IAM, Datenschutz oder Lieferantenmanagement,
- Review von Fehlalarmen und wiederkehrenden Mustern,
- Managemententscheidung bei kritischen oder uneindeutigen Fällen.

### Fortgeschritten

Ziel: Ereignisbewertung ist Teil eines belastbaren Security-Lagebilds.

1. Monitoring, Ticketing, Assetdaten, Kritikalität und Incident-Prozess sind miteinander verbunden.
2. Korrelationen helfen, Einzelereignisse zu Vorfallmustern zusammenzuführen.
3. Runbooks unterstützen häufige Triagefälle, ohne menschliche Entscheidung bei kritischen Punkten zu ersetzen.
4. Metriken zeigen Qualität der Bewertung: Zeit bis Triage, Eskalationsquote, Fehlalarmquote, wiedereröffnete Fälle, kritische Ereignisse ohne Owner.
5. Lessons Learned verbessern Detektionsregeln, Playbooks, Schulung und Risikobewertung.

## Ablauf als Routine

1. **Ereignis erfassen:** Quelle, Zeitpunkt, Meldende, betroffene Systeme und erste Fakten dokumentieren.
2. **Erstprüfung durchführen:** Plausibilität, Dringlichkeit, bekannte Muster und Sofortgefahr einschätzen.
3. **Kontext ergänzen:** Asset, Owner, Datenklasse, Nutzer, Lieferant, Logs und aktuelle Lage prüfen.
4. **Schweregrad festlegen:** mögliche Auswirkung, Ausbreitung, Datenbezug und Betriebsrelevanz bewerten.
5. **Entscheidung treffen:** schließen, beobachten, technische Maßnahme starten, Risiko aufnehmen oder Incident eskalieren.
6. **Handoffs auslösen:** Incident, Datenschutz, Legal, Management, Lieferant, IAM, BCM oder Change einbeziehen.
7. **Nachweise sichern:** Bewertung, Entscheidungsgrund und Übergabe dokumentieren.
8. **Reviewen:** Stichproben, Fehlalarme und wiederkehrende Ereignisse auswerten.

## Entscheidungen

- Welche Ereignisse werden sofort eskaliert?
- Welche Kriterien machen aus einem Ereignis einen Sicherheitsvorfall?
- Wer darf ein Ereignis schließen und wann braucht es Vier-Augen-Review?
- Wann wird Datenschutz, Legal, Kommunikation oder Management einbezogen?
- Welche Informationen reichen für eine Entscheidung, welche müssen nachgefordert werden?
- Wann wird ein wiederkehrendes Ereignis zum Risiko- oder Maßnahmenproblem?

## Evidenz

### Starke Evidenz

- Ereignislog mit Quelle, Zeitpunkt, Owner und Status,
- dokumentierte Triageentscheidung mit Begründung,
- Klassifikation und Schweregrad,
- technische Analyse- oder Logreferenzen,
- Übergaben an Incident, Maßnahme, Risiko oder Human Review,
- Schließentscheidung bei Fehlalarm,
- Auswertung wiederkehrender Muster.

### Schwache Evidenz

- Alarmexport ohne Entscheidung,
- Chatverlauf ohne Ticket oder Owner,
- Schweregrad nur aus Toolscore ohne Kontext,
- geschlossene Meldung ohne Begründung,
- Monatszahl von Ereignissen ohne Qualitätsbewertung.

### Evidenzlücken

- Ereignisse ohne zentralen Eingang,
- keine Kriterien für Eskalation,
- keine Verbindung zu Assets oder Datenklassen,
- keine nachvollziehbare Entscheidung,
- keine Legal-/Datenschutz-Prüfung trotz Datenbezug,
- wiederkehrende Fehlalarme ohne Verbesserung.

## Wirksamkeitsprüfung

Prüffragen:

- Werden Sicherheitsereignisse zuverlässig erfasst?
- Ist für Stichproben nachvollziehbar, warum eskaliert oder geschlossen wurde?
- Werden kritische Ereignisse schnell genug triagiert?
- Sind Owner, Assets und Datenbezug erkennbar?
- Werden Human-Gate-Punkte rechtzeitig ausgelöst?
- Führen Muster aus Ereignissen zu Verbesserungen in Detektion, Schulung oder Maßnahmen?

Mögliche Kennzahlen:

- Zeit bis Ersttriage nach Schweregrad,
- Anteil Ereignisse mit dokumentierter Entscheidung,
- Eskalationsquote zu Incident Response,
- Fehlalarmquote und wiederkehrende Fehlalarme,
- Ereignisse ohne Owner,
- überfällige Triagefälle.

## BSIG-/NIS2-Anschluss

Die Bewertung und Entscheidung bei Sicherheitsereignissen ist anschlussfähig an NIS2-orientierte Themen wie Incident Handling, Detektion, Melde- und Eskalationsfähigkeit, Risikomanagement und Managementverantwortung. Ob ein konkretes Ereignis rechtliche Meldepflichten oder Datenschutzpflichten auslöst, muss im Einzelfall durch zuständige Menschen geprüft werden.

Dieses Artefakt ersetzt keine Rechtsberatung und keine verbindliche Bewertung von Meldepflichten.

## Grenzen

- Keine rechtliche Klassifikation von Vorfällen oder Datenschutzverletzungen.
- Kein Ersatz für forensische Analyse, Incident Response oder Krisenkommunikation.
- Keine Aussage, dass eine Triageentscheidung regulatorisch ausreichend ist.
- Keine ISO-27002-Texte oder Zertifizierungszusage.
- Keine echten Vorfalls-, Kunden-, Personen- oder Logdaten in öffentlichen Beispielen.

## Handoffs

- **Incident-Handoff:** Ereignis erfüllt definierte Kriterien für Vorfall, Ausbreitung, Kompromittierung oder hohe Auswirkung.
- **Datenschutz-/Legal-Handoff:** Personenbezug, Datenabflussverdacht, Kundenwirkung, Meldepflichtnähe oder arbeitsrechtliche Fragen.
- **IAM-Handoff:** Kontoauffälligkeit, Privilegienmissbrauch, verdächtige Anmeldung oder technischer Identitätsmissbrauch.
- **Change-/Betriebs-Handoff:** technische Korrektur, Konfigurationsänderung, Patch oder Sperrmaßnahme.
- **Lieferanten-Handoff:** Anbieterereignis, SaaS-Alarm, Managed-Service-Hinweis oder fehlende Information.
- **BCM-/Krisen-Handoff:** mögliche erhebliche Betriebsunterbrechung oder Krisenpotenzial.
- **Management-Handoff:** hohe Auswirkung, Ressourcenbedarf, externe Kommunikation, Restrisiko oder unklare Entscheidungslage.

## Typische Fehler

- Alarme werden gesammelt, aber nicht entschieden.
- Tool-Schweregrade ersetzen Kontextbewertung.
- Kritische Ereignisse gehen in Chatkanälen verloren.
- Fehlalarme werden geschlossen, ohne Detektionsregeln zu verbessern.
- Datenschutz oder Legal werden erst nach externer Kommunikation eingebunden.
- Triageentscheidungen sind nicht prüfbar.
- Wiederkehrende Ereignisse werden nicht in Risiken oder Maßnahmen übersetzt.

## Fiktives Mini-Beispiel

Ein fiktives Monitoring meldet mehrere fehlgeschlagene Admin-Logins aus einem ungewohnten Land. Der Triage Owner erfasst das Ereignis, prüft Assetkritikalität und Logkontext und erkennt kurz darauf eine erfolgreiche Anmeldung. Der Fall wird als möglicher Sicherheitsvorfall eskaliert. Der Incident Lead startet Kontosperrung und Analyse; Datenschutz und Management werden wegen möglicher Datenbetroffenheit als Human Gate markiert.

Evidenz:

- Ereignisticket,
- Logreferenzen,
- Triageentscheidung mit Schweregrad,
- Übergabe an Incident Response,
- dokumentierte Human-Gate-Markierung,
- Maßnahmenstatus.
