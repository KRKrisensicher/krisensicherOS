
# A.5.22 — Überwachung und Änderung von Lieferantendiensten

## Zweck

Diese Routine sorgt dafür, dass ausgelagerte oder extern bezogene Dienste nach Vertragsstart nicht aus dem Blick geraten. Lieferantendienste verändern sich: Leistungen, Unterauftragnehmer, Schnittstellen, Standorte, Sicherheitsnachweise, Servicequalität oder Abhängigkeiten. Die Organisation braucht deshalb eine wiederkehrende Arbeitsweise, um Änderungen zu erkennen, Risiken neu zu bewerten und Entscheidungen nachvollziehbar zu treffen.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der relevante Lieferantendienste überwacht, Änderungen bewertet und bei Bedarf in Risiko-, Vertrags-, Betriebs- oder Managemententscheidungen überführt werden. Ziel ist nicht Lieferantenkontrolle um ihrer selbst willen, sondern belastbare Steuerung kritischer Abhängigkeiten.

## Typische Risiken

- Wenn ein kritischer Dienstleister seine Leistung, Plattform oder Unterauftragnehmer ändert, ohne dass die Organisation dies bewertet, können neue Sicherheits- oder Verfügbarkeitsrisiken entstehen.
- Wenn Serviceberichte nur abgelegt, aber nicht gelesen werden, bleiben wiederkehrende Störungen, SLA-Abweichungen oder Sicherheitslücken ohne Entscheidung.
- Wenn Lieferantenänderungen nicht mit Asset-, Risiko- und Vertragsdaten verbunden werden, entstehen blinde Flecken in der Lieferkette.
- Wenn Sicherheitsnachweise veralten, verlässt sich die Organisation auf überholte Annahmen.
- Wenn Fachbereich, Einkauf, IT und ISMS getrennt arbeiten, werden Änderungen zu spät oder gar nicht eskaliert.

## Trigger

- neuer, geänderter oder beendeter Lieferantendienst.
- Änderung von Leistungsumfang, Architektur, Standort, Datenverarbeitung, Schnittstellen oder Unterauftragnehmern.
- Sicherheitsmeldung, Schwachstellenhinweis, Incident, SLA-Verletzung oder wiederholte Qualitätsprobleme beim Lieferanten.
- Ablauf oder Aktualisierung von Sicherheitsnachweisen, Zertifikaten, Versicherungen, Prüfberichten oder Selbstauskünften.
- geänderter Schutzbedarf des unterstützten Geschäftsprozesses.
- Vertragsreview, Lieferantenreview, ISMS-Risikoreview oder Managementfrage zu kritischen Abhängigkeiten.

## Rollen und Verantwortung

- **Service Owner / Fachbereich:** bewertet geschäftliche Kritikalität, Leistungsqualität und fachliche Auswirkungen.
- **Lieferantenmanagement / Einkauf:** hält Vertrags-, Kontakt-, Leistungs- und Reviewdaten aktuell.
- **ISMS-Owner / Security-Rolle:** definiert Sicherheitsanforderungen, Bewertungslogik und Eskalationskriterien.
- **IT-/Plattform Owner:** bewertet technische Schnittstellen, Integrationen, Zugriff und Betriebsabhängigkeiten.
- **Legal / Datenschutz:** prüft Vertrags-, Datenschutz- oder rechtliche Fragen bei relevanten Änderungen.
- **Management:** entscheidet bei kritischen Abhängigkeiten, nicht tragbaren Restrisiken, Ressourcenbedarf oder Wechselstrategie.

## Implementierung

### Minimalstart

Ziel: kritische Lieferantendienste sichtbar und reviewfähig machen.

1. Kritische Lieferantendienste im ISMS-Scope werden benannt.
2. Jeder Dienst erhält einen Service Owner und einen Vertrags-/Lieferantenkontakt.
3. Für jeden kritischen Dienst werden Mindestinformationen geführt: Zweck, unterstützter Prozess, Datenarten, Schnittstellen, Kritikalität, Vertragslaufzeit, Reviewdatum.
4. Lieferantenänderungen werden über einen einfachen Änderungs- oder Reviewpunkt erfasst.
5. Auffälligkeiten werden im Risikoregister oder Maßnahmenlog referenziert.
6. Offene Restrisiken, fehlende Nachweise oder kritische Abweichungen werden eskaliert.

Minimaler Nachweis:

- Liste kritischer Lieferantendienste mit Owner,
- letztes Reviewdatum,
- dokumentierte Lieferantenänderung oder Servicebewertung,
- offenes Maßnahmen- oder Risikolog,
- Eskalations- oder Managemententscheidung bei kritischem Befund.

### Solide Praxis

Ziel: Lieferantenüberwachung wird risikobasiert, wiederholbar und mit Vertragssteuerung verbunden.

1. Lieferantendienste werden nach Kritikalität und Informationsrisiko klassifiziert.
2. Reviewfrequenzen und Mindestnachweise richten sich nach Kritikalität.
3. Serviceberichte, Sicherheitsnachweise, Incidents, Auditfindings und Leistungsabweichungen werden zusammen bewertet.
4. Änderungen werden vor Umsetzung oder spätestens bei Bekanntwerden auf Sicherheits-, Verfügbarkeits- und Vertragsauswirkung geprüft.
5. Ausnahmen oder nicht erfüllte Anforderungen erhalten Owner, Frist, Maßnahme und Wiedervorlage.
6. Ergebnisse fließen in Lieferantenbewertung, Risikoregister, Vertragsreview und Management Review.

Starke Evidenz:

- Lieferanten-/Serviceregister mit Kritikalität,
- Reviewprotokolle mit Entscheidungen,
- Änderungsbewertungen,
- Nachweise zu SLA, Sicherheitsmeldungen oder Prüfberichten,
- Maßnahmenlog mit Owner und Frist,
- dokumentierte Eskalationen oder Vertragsentscheidungen.

### Fortgeschritten

Ziel: kritische Lieferantenabhängigkeiten werden als laufendes Lagebild gesteuert.

1. Lieferantenregister, Assetinventar, Risikoregister und Vertragsdaten sind miteinander verknüpft.
2. Kritische Dienständerungen lösen automatisch Review- oder Freigabe-Workflows aus.
3. Lieferantenrisiken werden mit Incident Management, Schwachstellenmanagement, BCM und Exit-Planung verbunden.
4. Unterauftragnehmer, Konzentrationsrisiken und regionale Abhängigkeiten werden regelmäßig betrachtet.
5. Management erhält entscheidungsfähige Kennzahlen: kritische Dienste ohne aktuellen Review, offene Lieferantenmaßnahmen, wiederholte SLA-Abweichungen, überfällige Nachweise, hohe Abhängigkeiten.

## Ablauf als Routine

1. **Dienst oder Änderung erkennen:** über Lieferantenmeldung, Vertragsreview, Servicebericht, Fachbereich, Incident oder Einkauf.
2. **Scope bestimmen:** betroffener Prozess, Daten, Systeme, Schnittstellen, Standorte und Nutzergruppen.
3. **Kritikalität prüfen:** geschäftliche Auswirkung, Schutzbedarf, Abhängigkeit und Alternativen bewerten.
4. **Änderung bewerten:** Sicherheits-, Verfügbarkeits-, Datenschutz-, Vertrags- und Betriebsfolgen einordnen.
5. **Entscheidung treffen:** akzeptieren, Auflagen setzen, Maßnahme planen, Eskalation auslösen oder Dienst anpassen.
6. **Nachweis ablegen:** Review, Bewertung, Entscheidung und Maßnahmen nachvollziehbar dokumentieren.
7. **Nachverfolgen:** offene Punkte bis Abschluss prüfen und bei Verzug eskalieren.
8. **Lernen:** Muster aus Störungen, Änderungen oder Lieferantenproblemen in Beschaffung und Vertragsgestaltung zurückspielen.

## Entscheidungen

- Welche Lieferantendienste sind kritisch genug für regelmäßige Überwachung?
- Welche Änderungen dürfen Lieferanten ohne Vorabfreigabe umsetzen, welche nicht?
- Welche Nachweise werden akzeptiert und wann sind sie zu alt oder zu schwach?
- Wann wird aus einer Lieferantenabweichung ein Risiko, Incident, Vertragsproblem oder Managementthema?
- Welche Ausnahmen sind befristet tragbar?
- Wann braucht die Organisation Exit-Plan, Zweitanbieter oder technische Kompensation?

## Evidenz

### Starke Evidenz

- aktuelles Register kritischer Lieferantendienste mit Owner und Kritikalität,
- Reviewprotokolle mit konkreten Entscheidungen,
- Änderungsbewertungen vor oder nach Lieferantenänderung,
- Nachweise über nachverfolgte Lieferantenmaßnahmen,
- verknüpfte Risiko- oder Maßnahmenregistereinträge,
- Managemententscheidung bei kritischer Abhängigkeit oder Restrisiko.

### Schwache Evidenz

- allgemeine Lieferantenliste ohne Kritikalität,
- abgelegte Zertifikate ohne Reviewdatum oder Scope-Bezug,
- Vertragsklauseln ohne Betriebsroutine,
- Serviceberichte ohne Bewertung,
- pauschale Aussage „vom Anbieter abgesichert“ ohne Nachweis.

### Evidenzlücken

- keine Owner für kritische Lieferantendienste,
- unbekannte Unterauftragnehmer oder Schnittstellen,
- keine Bewertung von Lieferantenänderungen,
- überfällige Sicherheitsnachweise,
- offene Lieferantenabweichungen ohne Frist oder Entscheidung,
- kritische Abhängigkeiten ohne Exit- oder Eskalationslogik.

## Wirksamkeitsprüfung

Prüffragen:

- Sind die kritischen Lieferantendienste vollständig und mit Ownern erfasst?
- Werden Änderungen an Leistung, Plattform, Unterauftragnehmern oder Sicherheitsnachweisen erkannt?
- Können Serviceberichte oder Lieferantenmeldungen zu Entscheidungen und Maßnahmen zurückverfolgt werden?
- Werden wiederholte Abweichungen oder fehlende Nachweise eskaliert?
- Sind Risiken und Maßnahmen mit dem ISMS-Risikoregister verbunden?
- Erkennt das Management kritische Konzentrations- oder Exit-Risiken?

Mögliche Kennzahlen:

- Anteil kritischer Lieferantendienste mit aktuellem Review,
- überfällige Lieferantennachweise,
- offene Lieferantenmaßnahmen nach Kritikalität,
- wiederholte SLA- oder Sicherheitsabweichungen,
- kritische Dienste ohne Exit-Überlegung,
- Dauer bis Abschluss einer Lieferantenänderungsbewertung.

## BSIG-/NIS2-Anschluss

Die Routine ist anschlussfähig an NIS2-orientierte Themen wie Lieferkettensicherheit, Risikomanagement, Steuerung externer Dienste, Business Continuity und Incident-Fähigkeit. Für betroffene Organisationen sollte der konkrete Bezug im Anforderungsregister, im Risikoregister und im Lieferantenmanagement geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung von Pflichten, Verträgen, Datenschutzfragen oder Meldeanforderungen.

## Grenzen

- Keine Rechts-, Vertrags- oder Datenschutzberatung.
- Keine Aussage, dass ein Lieferant durch einzelne Nachweise sicher oder konform ist.
- Keine Übernahme lizenzpflichtiger Normtexte oder Zertifizierungszusage.
- Keine Bewertung echter Lieferanten oder vertraulicher Vertragsdaten in öffentlichen Beispielen.
- Kein Ersatz für technische Prüfung, Incident Response, BCM oder Exit-Planung.

## Handoffs

- **Einkauf-/Vendor-Handoff:** Vertragsänderung, Lieferantenreview, fehlende Nachweise, Leistungsabweichung.
- **Legal-/Datenschutz-Handoff:** Änderung von Datenverarbeitung, Standorten, Unterauftragnehmern, Vertragsklauseln oder Meldepflichtnähe.
- **IT-/Architektur-Handoff:** neue Schnittstellen, technische Integrationen, Plattformwechsel oder Zugriffserweiterungen.
- **Incident-Handoff:** Sicherheitsmeldung, Verdacht auf Kompromittierung, Dienststörung mit Sicherheitsbezug.
- **BCM-Handoff:** kritische Abhängigkeit, fehlende Ausweichmöglichkeit, Exit- oder Notfallbedarf.
- **Management-Handoff:** hohes Restrisiko, Anbieterwechsel, Budgetbedarf, strategische Abhängigkeit.
- **Audit-/Evidence-Handoff:** fehlende oder schwache Nachweise für Review, Entscheidung oder Maßnahmenverfolgung.

## Typische Fehler

- Lieferanten werden nur beim Onboarding geprüft und danach nicht mehr gesteuert.
- Zertifikate werden gesammelt, aber nicht auf Scope, Aktualität oder Relevanz geprüft.
- Fachbereiche erfahren von Änderungen, aber ISMS, Einkauf oder IT nicht.
- SLA-Probleme werden operativ behandelt, ohne Risiko- oder Vertragsentscheidung.
- Unterauftragnehmer und technische Schnittstellen bleiben außerhalb des Reviews.
- Offene Lieferantenmaßnahmen haben keinen Owner oder kein Fälligkeitsdatum.
- Management erhält Listen, aber keine entscheidungsfähigen Abhängigkeiten.

## Fiktives Mini-Beispiel

Ein fiktiver SaaS-Anbieter kündigt an, einen Teil seines Betriebs auf eine neue Plattform zu verlagern. Der Fachbereich meldet die Änderung an Einkauf und ISMS. Der Service Owner prüft betroffene Prozesse und Daten, der IT-Owner bewertet Schnittstellen, Datenschutz und Legal klären prüfungsbedürftige Punkte. Bis zur Klärung wird eine befristete Maßnahme dokumentiert: zusätzlicher Review der Adminzugriffe und aktualisierte Exit-Notiz. Das Ergebnis wird im Lieferantenreview festgehalten.

Evidenz:

- Lieferantenmeldung,
- Änderungsbewertung,
- aktualisierter Registereintrag,
- Maßnahmenlog mit Owner und Frist,
- Reviewentscheidung zur weiteren Nutzung.
