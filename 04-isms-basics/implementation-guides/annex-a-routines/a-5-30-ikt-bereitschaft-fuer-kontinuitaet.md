
# A.5.30 — IKT-Bereitschaft für Kontinuität

## Zweck

IKT-Bereitschaft für Kontinuität sorgt dafür, dass digitale Dienste, Infrastruktur, Daten, Identitäten und Betriebsfähigkeiten auf Ausfälle vorbereitet sind. Ziel ist nicht ein schönes Notfallhandbuch, sondern eine überprüfbare Verbindung zwischen Geschäftsanforderungen, technischen Wiederherstellungsfähigkeiten, Übungen, Entscheidungen und Verbesserungen.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der kritische IKT-Services für Kontinuität geplant, vorbereitet, getestet, reviewed und verbessert werden. Anforderungen aus Geschäftsprozessen, BCM, Risikoanalyse, Lieferantensteuerung und IT-Betrieb werden in konkrete Wiederanlauf- und Mindestbetriebsfähigkeiten übersetzt.

## Typische Risiken

- Wenn kritische Services nicht priorisiert sind, werden im Ausfall die falschen Systeme zuerst wiederhergestellt.
- Wenn Wiederherstellungsziele nicht mit technischen Fähigkeiten abgeglichen werden, entstehen unrealistische Erwartungen.
- Wenn Backups nie getestet werden, ist Wiederherstellung im Ernstfall ungewiss.
- Wenn Abhängigkeiten zu Identität, Netzwerk, Cloud, DNS, Lieferanten oder Schlüsselpersonen fehlen, scheitert der Wiederanlauf an Nebensystemen.
- Wenn Notfallübungen nur dokumentarisch stattfinden, bleiben technische und organisatorische Lücken verborgen.
- Wenn Sicherheitsanforderungen im Wiederanlauf ignoriert werden, können kompromittierte oder unvollständige Systeme produktiv werden.

## Trigger

- neue oder geänderte kritische Geschäftsprozesse, Services, Systeme oder Datenbestände.
- Business-Impact-Analyse, Risikoanalyse, BCM-Review oder Managemententscheidung.
- größere Architektur-, Cloud-, Netzwerk-, Backup- oder Lieferantenänderung.
- Ausfall, Sicherheitsvorfall, Wiederherstellungstest oder Krisenübung.
- Auditfinding oder interne Prüfung zu Kontinuität, Backup oder Wiederanlauf.
- neue Abhängigkeit von SaaS, Managed Service, Plattform oder Standort.
- turnusmäßiger Review von Wiederanlaufzielen und Testnachweisen.

## Rollen und Verantwortung

- **BCM-Owner / Prozess Owner:** definiert kritische Geschäftsprozesse, Prioritäten und tolerierbare Unterbrechungen.
- **Service Owner / Asset Owner:** übersetzt Geschäftsanforderungen in Serviceanforderungen und akzeptiert offene Lücken oder eskaliert sie.
- **IT-Betrieb / Plattformteam:** plant und betreibt Backup, Wiederherstellung, Redundanz, Monitoring und technische Notverfahren.
- **ISMS-Owner / Security-Rolle:** prüft Sicherheitsanforderungen im Notbetrieb und Wiederanlauf.
- **Lieferantenmanagement:** klärt Kontinuitätszusagen, Kontaktwege und Abhängigkeiten externer Dienste.
- **Management:** entscheidet Zielkonflikte zwischen Kosten, Wiederanlaufzeit, Restrisiko und Servicepriorität.
- **Fachbereiche:** testen Arbeitsfähigkeit im Not- oder Wiederanlaufbetrieb.

## Implementierung

### Minimalstart

Ziel: Die wichtigsten IKT-Services kennen und ihre Wiederherstellbarkeit grundlegend prüfen.

1. Die wichtigsten Geschäftsprozesse und zugehörigen IKT-Services im Scope benennen.
2. Für jeden kritischen Service Owner, technische Verantwortliche und zentrale Abhängigkeiten erfassen.
3. Einfache Wiederanlaufziele dokumentieren: Priorität, tolerierbare Unterbrechung, benötigte Datenaktualität, Mindestbetrieb.
4. Backup- und Wiederherstellungsnachweise für kritische Daten oder Systeme sammeln.
5. Mindestens einen Wiederherstellungstest oder Tabletop für einen kritischen Service durchführen.
6. Lücken als Maßnahmen mit Owner, Frist und Management-Handoff dokumentieren.

Minimaler Nachweis:

- Liste kritischer IKT-Services mit Ownern,
- Abhängigkeitsübersicht,
- Wiederanlaufanforderungen,
- Backup-/Restore-Testnachweis,
- Maßnahmenlog zu Kontinuitätslücken.

### Solide Praxis

Ziel: Kontinuitätsanforderungen sind abgestimmt, getestet und in Betriebsroutinen verankert.

1. Business-Impact-Anforderungen werden mit technischen Recovery-Fähigkeiten abgeglichen.
2. Kritische Abhängigkeiten werden betrachtet: Identität, Netzwerk, DNS, Zertifikate, Schlüssel, Monitoring, Adminzugänge, Dienstleister, Standorte.
3. Wiederherstellungspläne enthalten Reihenfolge, Rollen, Kommunikationswege, Sicherheitschecks und Rückfalloptionen.
4. Restore-Tests prüfen nicht nur einzelne Dateien, sondern Servicefähigkeit und Datenintegrität.
5. Lieferanten werden in Kontinuitätsreviews einbezogen, wenn sie kritische Services tragen.
6. Abweichungen zwischen Anforderung und Fähigkeit führen zu Risikoentscheidung, Maßnahme oder Managementpriorisierung.

### Fortgeschritten

Ziel: IKT-Kontinuität ist belastbar, geübt und in Architekturentscheidungen integriert.

1. Kritische Services haben abgestufte Wiederanlaufkonzepte mit technischen Tests und fachlicher Abnahme.
2. Szenarien wie Ransomware, Cloud-Ausfall, Standortverlust, Identitätsausfall und Lieferantenausfall werden geübt.
3. Automatisierte Überwachung prüft Backup-Erfolg, Replikation, Schlüsselabhängigkeiten und Wiederanlaufbereitschaft.
4. Architekturentscheidungen berücksichtigen Resilienz, Wiederherstellbarkeit, Portabilität und Sicherheitskontrollen.
5. Kontinuitätskennzahlen fließen in Management Review, Investitionsplanung und Risikobehandlung.
6. Lessons Learned aus Störungen und Übungen verbessern Technik, Verträge, Prozesse und Krisenroutinen.

## Ablauf als Routine

1. **Kritikalität bestimmen:** Geschäftsprozess, Service, Daten, Nutzergruppen und Auswirkung einordnen.
2. **Anforderungen festlegen:** Wiederanlaufpriorität, tolerierbare Unterbrechung, Datenaktualität, Mindestbetrieb und Sicherheitsanforderungen beschreiben.
3. **Abhängigkeiten erfassen:** technische, organisatorische und lieferantenbezogene Voraussetzungen aufnehmen.
4. **Fähigkeit prüfen:** Backup, Restore, Redundanz, Notzugriff, Monitoring und Personalverfügbarkeit bewerten.
5. **Planung aktualisieren:** Wiederherstellungsreihenfolge, Rollen, Checklisten, Kontakte und Sicherheitsprüfpunkte festlegen.
6. **Testen oder üben:** technisch, fachlich oder als Tabletop; Ergebnis und Lücken dokumentieren.
7. **Entscheiden:** Lücken priorisieren, Restrisiken akzeptieren oder Maßnahmen finanzieren.
8. **Verbessern:** technische, vertragliche oder organisatorische Maßnahmen umsetzen und erneut prüfen.

## Entscheidungen

- Welche IKT-Services sind für den Geschäftsbetrieb und die Sicherheitsfähigkeit kritisch?
- Welche Wiederanlaufziele sind realistisch und finanziell tragbar?
- Welche Datenverluste oder Unterbrechungen wären nicht akzeptabel?
- Welche Services brauchen technische Redundanz, welche können manuell oder zeitversetzt wiederhergestellt werden?
- Welche Sicherheitschecks sind vor Wiederinbetriebnahme zwingend?
- Welche Lieferantenabhängigkeiten benötigen Vertragsanpassung oder Exit-/Fallback-Planung?
- Welche Kontinuitätslücken akzeptiert das Management bewusst?

## Evidenz

### Starke Evidenz

- kritischer Servicekatalog mit Ownern und Abhängigkeiten,
- abgestimmte Wiederanlaufanforderungen,
- Wiederherstellungsplan mit Rollen und Sicherheitschecks,
- Backup- und Restore-Testprotokolle,
- fachliche Abnahme eines Wiederherstellungstests,
- Maßnahmenlog zu Kontinuitätslücken,
- Managemententscheidung zu Restrisiko, Investition oder Priorisierung.

### Schwache Evidenz

- Backup-Policy ohne Restore-Nachweis,
- Systemliste ohne Geschäftsprozessbezug,
- Notfallplan ohne Testdatum,
- technische Redundanzbehauptung ohne Ausfall- oder Umschaltnachweis,
- Lieferantenzusage ohne Servicebezug oder Review.

### Evidenzlücken

- keine Owner für kritische Services,
- unklare Abhängigkeit von Identität, Netzwerk, Cloud oder Dienstleistern,
- Wiederanlaufziele wurden nie mit Fachbereichen abgestimmt,
- Backups sind vorhanden, aber Wiederherstellung wurde nicht geprüft,
- Sicherheitsprüfung vor Wiederanlauf fehlt,
- Kontinuitätslücken ohne Managemententscheidung.

## Wirksamkeitsprüfung

Prüffragen:

- Sind kritische IKT-Services und Abhängigkeiten aktuell bekannt?
- Passen technische Wiederherstellungsfähigkeiten zu fachlichen Anforderungen?
- Gibt es aktuelle Restore- oder Wiederanlauftests für kritische Services?
- Werden Sicherheitsanforderungen im Wiederanlauf geprüft?
- Werden Lieferantenabhängigkeiten in Kontinuitätsplanung und Übungen berücksichtigt?
- Führen Testlücken zu Maßnahmen, Risikoentscheidungen oder Investitionsentscheidungen?

Mögliche Kennzahlen:

- Anteil kritischer Services mit aktuellem Wiederanlaufplan,
- Anteil kritischer Services mit erfolgreichem Restore-Test,
- offene Kontinuitätslücken nach Kritikalität,
- Abweichung zwischen gefordertem und getestetem Wiederanlauf,
- überfällige Tests oder Reviews,
- kritische Lieferanten ohne geprüfte Kontinuitätszusagen.

## BSIG-/NIS2-Anschluss

IKT-Bereitschaft für Kontinuität ist anschlussfähig an NIS2-orientierte Themen wie Business Continuity, Backup- und Wiederherstellungsfähigkeit, Krisenmanagement, Risikomanagement, Lieferkettensicherheit und Aufrechterhaltung wesentlicher Dienste.

Für betroffene Organisationen sollte der konkrete Bezug im Anforderungsregister, in BCM-Unterlagen und im Management Review geprüft werden. Dieses Artefakt ersetzt keine rechtliche Bewertung von Betroffenheit, Anforderungen oder Nachweispflichten.

## Grenzen

- Dieses Artefakt ist kein vollständiger Business-Continuity-Plan und kein technisches Hochverfügbarkeitsdesign.
- Es ersetzt keine Architektur-, Cloud-, Netzwerk- oder Backup-Fachplanung.
- Es garantiert keine Verfügbarkeit, Wiederherstellbarkeit oder Konformität.
- Es trifft keine Rechts- oder Datenschutzbewertung.
- Öffentliche Beispiele nutzen keine echten Organisations- oder Systemdaten.

## Handoffs

- **BCM-Handoff:** Business-Impact-Anforderungen, Wiederanlaufprioritäten, Übungen und Krisenrollen.
- **IT-Betriebs-Handoff:** Backup, Restore, Redundanz, Monitoring, Notzugriffe, technische Runbooks.
- **Security-/ISMS-Handoff:** Sicherheitschecks, Integrität, Zugriffsschutz, Notbetrieb und Risikoakzeptanz.
- **Lieferanten-Handoff:** SaaS, Managed Services, Cloud, Supportzeiten, Kontinuitätszusagen und Exit-/Fallback-Fragen.
- **Management-Handoff:** Investitionen, Zielkonflikte, nicht erfüllbare Wiederanlaufziele und akzeptierte Restrisiken.
- **Audit-/Evidence-Handoff:** Testprotokolle, Abnahmen, Maßnahmen und Reviewnachweise.

## Typische Fehler

- Backups werden mit Wiederherstellungsfähigkeit verwechselt.
- Kritische Abhängigkeiten wie IAM, DNS, Zertifikate oder Adminzugänge fehlen in Plänen.
- Fachbereiche kennen Wiederanlaufziele nicht oder haben sie nie bestätigt.
- Tests prüfen nur Technik, aber nicht fachliche Arbeitsfähigkeit.
- Sicherheitschecks werden aus Zeitdruck übersprungen.
- Lieferantenversprechen werden nicht mit eigenen Wiederanlaufanforderungen abgeglichen.
- Management sieht Kosten, aber nicht das akzeptierte Ausfall- und Wiederanlaufrisiko.

## Fiktives Mini-Beispiel

Ein fiktiver Logistikdienstleister identifiziert das Versandportal als kritischen IKT-Service. Der Service Owner dokumentiert Abhängigkeiten zu Identitätsdienst, Datenbank, DNS und einem SaaS-Dienst. Ein Restore-Test zeigt, dass die Datenbank wiederhergestellt werden kann, aber der Identitätsdienst kein getestetes Notverfahren hat. Das Management entscheidet, ein Notfallverfahren für privilegierte Zugriffe und einen jährlichen kombinierten Wiederanlauftest zu finanzieren.

Evidenz:

- kritischer Serviceeintrag mit Abhängigkeiten,
- Wiederanlaufanforderungen,
- Restore-Testprotokoll,
- identifizierte Lücke beim Identitätsdienst,
- Managemententscheidung zur Maßnahme,
- Termin für kombinierten Wiederanlauftest.
