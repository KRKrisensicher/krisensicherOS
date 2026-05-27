
# A.8.15 — Protokollierung

## Zweck

Protokollierung sorgt dafür, dass sicherheitsrelevante Ereignisse in Systemen, Anwendungen, Identitätsdiensten und Plattformen nachvollziehbar werden. Der Wert liegt nicht im Sammeln möglichst vieler Logs, sondern in einer betreibbaren Routine: relevante Ereignisse erfassen, schützen, auswertbar halten und für Untersuchungen, Reviews und Entscheidungen nutzbar machen.

## Control-Ziel in Repo-Sprache

Die Organisation legt fest, welche Ereignisse für Betriebssicherheit, Zugriffsschutz, Fehleranalyse, Incident Response und Nachvollziehbarkeit protokolliert werden, wer für Logquellen verantwortlich ist, wie Logs geschützt und aufbewahrt werden und wann aus Logdaten eine Prüfung, Eskalation oder Verbesserungsmaßnahme entsteht.

## Typische Risiken

- Wenn kritische Systeme keine verwertbaren Logs erzeugen, können Angriffe, Fehlbedienungen oder Ausfälle nicht nachvollzogen werden.
- Wenn Logquellen uneinheitlich konfiguriert sind, entstehen blinde Flecken zwischen Endgerät, Server, Cloud, Netzwerk und Anwendung.
- Wenn Logs ungeschützt bleiben, können Angreifer Spuren verändern oder löschen.
- Wenn zu viele irrelevante Daten gesammelt werden, gehen relevante Ereignisse unter und Datenschutz-/Aufbewahrungsfragen werden unnötig komplex.
- Wenn personenbezogene oder Beschäftigtendaten ohne geklärte Regeln verarbeitet werden, entstehen rechtliche und vertrauensbezogene Risiken.
- Wenn Aufbewahrungsfristen, Zugriff und Löschung ungeklärt sind, sind Logs im Ernstfall nicht verfügbar oder werden länger als nötig gehalten.

## Trigger

- neues oder wesentlich geändertes System, Anwendung, Cloud-Service oder Identitätsverfahren.
- neuer Incident, Verdacht auf Missbrauch oder Lessons Learned aus einer Untersuchung.
- Einführung oder Änderung von SIEM, EDR, Monitoring, IAM, Netzwerk- oder Cloud-Logging.
- neue Datenklasse, neue Schnittstelle oder neue administrative Rolle.
- Auditfinding, interne Prüfung oder Managementfrage zur Nachvollziehbarkeit.
- regulärer Review von Logquellen, Aufbewahrung, Zugriffen und Auswertbarkeit.
- Lieferanten- oder Managed-Service-Änderung, die Logverfügbarkeit oder Herausgabe betrifft.

## Rollen und Verantwortung

- **IT-/Plattform Owner:** betreibt Logquellen, Weiterleitung, Speicher, Schutzmechanismen und technische Verfügbarkeit.
- **Service Owner / Application Owner:** legt fachlich relevante Ereignisse, Fehler- und Sicherheitsereignisse für den Service fest.
- **Security-Rolle / ISMS-Owner:** definiert Mindestanforderungen, Prioritäten, Reviewlogik und Eskalationswege.
- **Incident-Response-Rolle:** nutzt Logs für Triage, Untersuchung und Lessons Learned.
- **Datenschutz-/Legal-Rolle:** prüft bei personenbezogenen Daten, Beschäftigtenbezug, Aufbewahrung oder Auswertungszwecken die organisationsspezifischen Vorgaben.
- **Lieferantenmanagement:** klärt Logzugang, Herausgabe, Aufbewahrung und Verantwortlichkeiten bei extern betriebenen Diensten.
- **Management:** entscheidet bei Ressourcenbedarf, Restrisiken, fehlender Abdeckung oder Zielkonflikten zwischen Transparenz, Aufwand und Schutzrechten.

## Implementierung

### Minimalstart

Ziel: Für kritische Systeme gibt es verwertbare, geschützte und auffindbare Protokolle.

1. Kritische Logquellen im Scope benennen: Identitätsdienst, zentrale Server, Internet-exponierte Dienste, Kernanwendungen, Firewalls, VPN, Cloud-Admin-Ebene.
2. Pro Logquelle Owner, Zweck, Ereignistypen und Ablageort festlegen.
3. Mindestereignisse definieren, zum Beispiel Anmeldeereignisse, fehlgeschlagene Zugriffe, administrative Aktionen, Rechteänderungen, sicherheitsrelevante Konfigurationsänderungen und Systemfehler.
4. Zugriff auf Logs begrenzen und Änderung/Löschung durch unberechtigte Rollen verhindern.
5. Aufbewahrung und Löschung pragmatisch festlegen und Reviewtermin setzen.
6. Einen einfachen Nachweis führen: Logquellenliste, Konfigurationsauszug, Stichprobe und offene Lücken.

### Solide Praxis

Ziel: Protokollierung wird risikobasiert, wiederholbar und mit Incident Response verbunden.

1. Loganforderungen werden je Systemklasse definiert: Endpunkte, Server, Anwendungen, Cloud, Netzwerk, Identität, Datenbanken.
2. Logweiterleitung, Zeitstempel, Integritätsschutz und Rollen für Zugriff/Auswertung sind dokumentiert.
3. Fehlende oder ausfallende Logquellen werden erkannt und als Betriebsabweichung behandelt.
4. Logzugriffe und Auswertungen sind auf berechtigte Zwecke und Rollen begrenzt.
5. Aufbewahrung, Löschung und Herausgabe werden mit Datenschutz/Legal geprüft, wenn personenbezogene oder Beschäftigtendaten betroffen sind.
6. Incident-Playbooks benennen, welche Logs bei typischen Szenarien benötigt werden.
7. Regelmäßige Stichproben prüfen, ob Logs vollständig, lesbar und für Untersuchungen nutzbar sind.

### Fortgeschritten

Ziel: Logs werden als belastbare Grundlage für Lagebild, Detektion, Forensikvorbereitung und Managemententscheidungen genutzt.

1. Kritische Logquellen sind zentral angebunden, normalisiert und mit Asset-, Identitäts- und Servicekontext verknüpft.
2. Manipulationsschutz, getrennte Berechtigungen und abgestufte Aufbewahrung sind technisch umgesetzt.
3. Use Cases für Detektion, Incident Response und Compliance-nahe Nachvollziehbarkeit werden gepflegt und getestet.
4. Logabdeckung und Ausfälle werden überwacht und berichtet.
5. Cloud-, SaaS- und Lieferantenlogs sind in Verantwortlichkeiten, Verträgen und Betriebsroutinen berücksichtigt.
6. Erkenntnisse aus Incidents, Tests und Reviews verbessern Logumfang, Qualität und Auswertung.
7. Management erhält entscheidungsfähige Aussagen zu blinden Flecken, Kosten, Risiken und benötigten Fähigkeiten.

## Ablauf als Routine

1. **Scope bestimmen:** kritische Systeme und relevante Ereignisse festlegen.
2. **Logquelle einrichten:** Ereignisse aktivieren, Weiterleitung konfigurieren, Zeitbezug sichern.
3. **Schutz festlegen:** Zugriff, Änderungsschutz, Aufbewahrung und Löschung regeln.
4. **Stichprobe prüfen:** erzeugen relevante Aktionen tatsächlich auswertbare Einträge?
5. **Betrieb überwachen:** Logausfälle, fehlende Quellen oder Speicherprobleme als Abweichung behandeln.
6. **Auswertung nutzen:** bei Incident, Review, Schwachstellenlage oder Managementfrage gezielt prüfen.
7. **Lücken entscheiden:** fehlende Abdeckung, Kosten oder rechtliche Fragen in passende Handoffs geben.
8. **Verbessern:** Erkenntnisse aus Vorfällen, Übungen und Reviews in Loganforderungen zurückführen.

## Entscheidungen

- Welche Systeme und Ereignisse sind für Nachvollziehbarkeit und Incident Response unverzichtbar?
- Welche Logdaten werden zentral gesammelt, welche verbleiben lokal oder beim Dienstleister?
- Wer darf Logs administrieren, wer darf sie auswerten, wer darf Ausnahmen genehmigen?
- Wie lange werden Logdaten für unterschiedliche Zwecke benötigt?
- Welche blinden Flecken werden akzeptiert, kompensiert oder priorisiert geschlossen?
- Wann ist eine Logauswertung ein Security-Thema, wann braucht sie Datenschutz-/Legal-Review?
- Welche Kosten für Speicherung, Tooling und Betrieb sind risikogerecht?

## Evidenz

### Starke Evidenz

- aktuelle Logquellenliste mit Owner, Zweck, Ereignistypen und Kritikalität,
- Konfigurationsnachweise für zentrale Logquellen und Weiterleitung,
- Stichproben, die auswertbare Ereignisse zeigen,
- Zugriffskonzept für Logadministration und Logauswertung,
- Nachweise zu Aufbewahrung, Löschung und Schutz vor unbefugter Änderung,
- Incident- oder Übungsnachweise, in denen Logs tatsächlich genutzt wurden,
- dokumentierte Entscheidungen zu Lücken, Ausnahmen und Verbesserungen.

### Schwache Evidenz

- allgemeine Logging-Policy ohne Systembezug,
- Tool-Screenshot ohne Aussage zur Abdeckung,
- Logdateien ohne Owner, Zeitbezug oder Suchfähigkeit,
- pauschale Aussage „Logs werden gesammelt“ ohne Ereignistypen und Aufbewahrung,
- SIEM-Betrieb ohne Nachweis, dass kritische Quellen angebunden sind,
- Aufbewahrungsfristen ohne Zweck- und Reviewbezug.

### Evidenzlücken

- keine Liste kritischer Logquellen,
- unklare Zuständigkeit für Logausfälle,
- keine Prüfung der Lesbarkeit oder Vollständigkeit,
- keine Regel für Zugriff auf Logdaten,
- keine Abstimmung bei personenbezogenen oder Beschäftigtendaten,
- externe Dienste ohne geklärte Logverfügbarkeit,
- keine Entscheidung zu bekannten blinden Flecken.

## Wirksamkeitsprüfung

Prüffragen:

- Sind die wichtigsten Identitäts-, Netzwerk-, Cloud-, Server- und Anwendungssysteme abgedeckt?
- Können relevante Sicherheitsereignisse zeitnah gefunden und einem System, Konto oder Service zugeordnet werden?
- Sind Logs gegen unbefugte Änderung und unberechtigten Zugriff geschützt?
- Werden Logausfälle oder fehlende Quellen erkannt und behandelt?
- Wurde die Nutzbarkeit der Logs in Incident-Übungen oder Stichproben geprüft?
- Sind Aufbewahrung, Löschung und Auswertung für sensible Logdaten menschlich geprüft?
- Werden erkannte Lücken priorisiert, entschieden und nachverfolgt?

Mögliche Kennzahlen:

- Abdeckung kritischer Logquellen,
- Anteil aktiver und fehlerfreier Logweiterleitungen,
- ungeklärte Loglücken nach Kritikalität,
- Zeit bis Logquelle nach neuem System angebunden ist,
- Logausfälle je Monat,
- Anteil Incident-Übungen mit ausreichender Loglage.

## BSIG-/NIS2-Anschluss

Protokollierung ist anschlussfähig an NIS2-orientierte Themen wie Risikomanagement, Detektion, Incident Handling, Zugriffsschutz, Betriebsüberwachung und Nachvollziehbarkeit sicherheitsrelevanter Ereignisse. Der konkrete Bezug sollte im Anforderungsregister, in der Risikoanalyse und im Incident-Response-Konzept organisationsspezifisch geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung von Protokollierung, Beschäftigtendaten, Meldepflichten oder Nachweispflichten.

## Grenzen

- Dieses Artefakt ist keine SIEM-Architektur, keine Forensikrichtlinie und keine Datenschutzprüfung.
- Mehr Logs bedeuten nicht automatisch bessere Sicherheit; Zweck, Qualität und Auswertbarkeit entscheiden.
- Logdaten dürfen nicht als öffentliche Beispiele oder Testdaten mit echten Personen-, Kunden- oder Geheimdaten verwendet werden.
- Keine Zertifizierungs-, Konformitäts- oder Sicherheitsgarantie.
- Keine Übernahme lizenzpflichtiger Normtexte.

## Handoffs

- **Incident-Handoff:** Verdacht auf Missbrauch, Kompromittierung, Manipulation oder fehlende Loglage im Vorfall.
- **Datenschutz-/Legal-Handoff:** personenbezogene Daten, Beschäftigtenbezug, Zweckänderung, Aufbewahrung, Herausgabe oder Auswertungsumfang.
- **Service-/Plattform-Handoff:** fehlende Logquelle, defekte Weiterleitung, Speicher-/Kostenproblem oder technische Schutzmaßnahme.
- **Lieferanten-Handoff:** Logs liegen bei SaaS, Managed Service oder Outsourcing-Partner und sind nicht ausreichend verfügbar.
- **Management-Handoff:** akzeptierte blinde Flecken, Budget für zentrale Auswertung, Speicher oder Personal.
- **Audit-/Evidence-Handoff:** Logabdeckung, Zugriff, Aufbewahrung oder Stichproben sind nicht nachvollziehbar.

## Typische Fehler

- Logs werden gesammelt, aber niemand prüft Abdeckung oder Nutzbarkeit.
- Kritische Systeme fehlen, während unkritische Systeme große Datenmengen erzeugen.
- Administratoren können Logs verändern, ohne dass dies auffällt.
- Aufbewahrung wird technisch voreingestellt, aber nie entschieden.
- Datenschutzfragen werden erst im Incident gestellt.
- Lieferantenlogs sind vertraglich oder praktisch nicht verfügbar.
- Management sieht Datenvolumen, aber keine Aussage zu blinden Flecken und Risiko.

## Fiktives Mini-Beispiel

Ein fiktiver Mittelständler betreibt ein Kundenportal und einen zentralen Identitätsdienst. Nach einer Incident-Übung stellt das Team fest, dass administrative Rollenänderungen im Portal nicht zentral auffindbar sind. Der Service Owner ergänzt diese Ereignisse in der Logquellenliste, das Plattformteam aktiviert die Weiterleitung und die Security-Rolle prüft eine Stichprobe. Datenschutz wird eingebunden, weil Nutzerkennungen und Beschäftigtenkonten in den Logs erscheinen. Eine verbleibende Lücke bei einem SaaS-Dienst wird ins Lieferantenmanagement gegeben und im nächsten Management Review als offenes Restrisiko vorgelegt.
