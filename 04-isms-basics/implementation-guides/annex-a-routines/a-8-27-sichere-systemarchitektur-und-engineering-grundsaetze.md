
# A.8.27 — Sichere Systemarchitektur und Engineering-Grundsätze

## Zweck

Sichere Systemarchitektur und Engineering-Grundsätze sorgen dafür, dass Systeme nicht zufällig sicher werden müssen. Sicherheitsprinzipien werden in Architekturentscheidungen, Plattformstandards, Integrationen, Betriebsmodellen und technischen Leitplanken verankert.

Der Kern ist eine Architektur- und Engineering-Routine: Kritische Systeme werden entlang klarer Prinzipien entworfen, geprüft und verbessert, bevor unsichere Strukturen im Betrieb schwer korrigierbar werden.

## Control-Ziel in Repo-Sprache

Die Organisation nutzt nachvollziehbare Sicherheitsprinzipien für Entwurf, Änderung und Betrieb von Systemen. Architekturentscheidungen machen Vertrauensgrenzen, Datenflüsse, Identitäten, Abhängigkeiten, Segmentierung, Ausfallszenarien, Überwachung und Wartbarkeit sichtbar und entscheidbar.

## Typische Risiken

- Wenn Architekturentscheidungen ohne Sicherheitsprinzipien getroffen werden, entstehen schwer behebbare strukturelle Schwächen.
- Wenn Vertrauensgrenzen und Datenflüsse unklar sind, können Zugriffe, Schnittstellen und Protokollierung falsch ausgelegt werden.
- Wenn Komplexität unkontrolliert wächst, werden Fehler, Abhängigkeiten und Betriebsrisiken unsichtbar.
- Wenn Sicherheitsanforderungen nur als Einzelmaßnahmen umgesetzt werden, fehlen belastbare Systemprinzipien wie Begrenzung von Rechten, Trennung, Robustheit und Beobachtbarkeit.
- Wenn Legacy-Ausnahmen nicht gesteuert werden, werden technische Schulden dauerhaft zum Sicherheitsrisiko.
- Wenn Cloud-, Plattform- oder Lieferantenarchitekturen nicht reviewed werden, entstehen blinde Flecken außerhalb des eigenen Betriebs.

## Trigger

- neues System, neue Plattform, neue Anwendung oder neue Integrationsarchitektur.
- größere Änderung an Netzwerk, Cloud, Identität, Datenhaltung, Mandantenfähigkeit oder Schnittstellen.
- Einführung externer Dienste, Managed Services, APIs oder Entwicklungsplattformen.
- Sicherheitsereignis, Schwachstellenmuster, Penetrationstest- oder Auditfinding.
- Migration, Modernisierung, Ablösung oder Außerbetriebnahme.
- wiederkehrende Betriebsstörungen, Skalierungsprobleme oder technische Schulden.
- turnusmäßiger Architekturreview kritischer Systeme.

## Rollen und Verantwortung

- **Architekturrolle / Enterprise- oder Solution Architect:** führt Architekturentscheidungen, Prinzipien und Reviews.
- **System Owner / Service Owner:** verantwortet Schutzbedarf, Geschäftsrisiko und Priorisierung.
- **Tech Lead / Engineering-Team:** setzt Architektur- und Engineering-Entscheidungen technisch um.
- **Security-Rolle:** bewertet Sicherheitsprinzipien, Risiken, Abweichungen und Kontrollbedarf.
- **Plattform-/Cloud-/Netzwerkteam:** stellt technische Leitplanken, Baselines und Betriebsfähigkeiten bereit.
- **IT-Betrieb:** bewertet Wartbarkeit, Monitoring, Backup, Patchfähigkeit und Incident-Fähigkeit.
- **ISMS-Owner:** verbindet Architekturentscheidungen mit Risikoregister, Maßnahmen und Management Review.
- **Management:** entscheidet bei Zielkonflikten, technischen Schulden, hohen Migrationskosten oder akzeptierten Restrisiken.

## Implementierung

### Minimalstart

Ziel: Kritische Architekturentscheidungen werden sichtbar und sicherheitsseitig reviewed.

1. Die Organisation benennt kritische Systeme, Plattformen und Integrationen im Scope.
2. Für diese Systeme werden Owner, Datenflüsse, externe Schnittstellen und zentrale Abhängigkeiten beschrieben.
3. Ein kurzer Satz von Engineering-Prinzipien wird vereinbart, etwa minimale Rechte, klare Vertrauensgrenzen, sichere Defaults, Nachvollziehbarkeit, Wartbarkeit und Ausfallszenarien.
4. Neue oder geänderte kritische Architekturen erhalten einen Sicherheitsreview vor Umsetzung oder Go-live.
5. Abweichungen werden mit Begründung, Risiko, Kompensation und Wiedervorlage dokumentiert.

Minimaler Nachweis:

- Liste kritischer Systeme und Integrationen,
- Architekturübersicht oder Datenflussbild,
- dokumentierte Engineering-Prinzipien,
- Reviewnotiz zu Architekturentscheidungen,
- Ausnahme- oder Maßnahmenlog.

### Solide Praxis

Ziel: Architektur und Engineering werden wiederholbar risikobasiert gesteuert.

1. Architekturentscheidungen werden als Architecture Decision Records oder vergleichbare kurze Entscheidungsnotizen dokumentiert.
2. Reviews betrachten Identitäten, Berechtigungen, Segmentierung, Datenflüsse, Kryptografiebedarf, Logging, Betriebsfähigkeit, Backup, Resilienz und Lieferantenabhängigkeiten.
3. Plattformstandards und sichere Referenzmuster reduzieren Einzelentscheidungen.
4. Kritische Abweichungen werden in Risiko- oder Schuldenregistern verfolgt.
5. Architekturreviews sind mit Sicherheitsanforderungen, Entwicklung, Change Management und Schwachstellenmanagement verbunden.
6. Wiederkehrende Findings lösen Anpassungen an Standards, Templates oder Plattformleitplanken aus.
7. Management erhält Transparenz über große technische Schulden und akzeptierte Architekturrestrisiken.

Starke Evidenz:

- Architekturprinzipien und Referenzmuster,
- System- und Datenflussdokumentation,
- Architecture Decision Records,
- Reviewprotokolle mit Entscheidungen,
- Maßnahmenlog für Abweichungen,
- Risikoentscheidungen zu technischen Schulden,
- Nachweise angepasster Plattform- oder Engineering-Standards.

### Fortgeschritten

Ziel: Sichere Architektur wird durch Plattformen, Automatisierung und kontinuierlichen Review gestützt.

1. Sicherheitsprinzipien sind in Cloud-Policies, Infrastrukturvorlagen, CI/CD-Gates, Netzwerkzonen und Identitätsplattformen eingebettet.
2. Kritische Architekturentscheidungen nutzen Threat Modeling, Resilienzanalysen oder Angriffsflächensicht.
3. Architektur- und Betriebsdaten liefern Indikatoren zu Exposition, Abhängigkeiten, technischen Schulden und Kontrolllücken.
4. Referenzarchitekturen und Self-Service-Plattformen machen sichere Wege einfacher als unsichere Sonderlösungen.
5. Legacy- und Ausnahme-Architekturen werden mit Zielbild, Migrationspfad und Managemententscheidung geführt.
6. Architektur-Lessons-Learned aus Incidents, Tests und Audits ändern aktiv Standards und Leitplanken.

## Ablauf als Routine

1. **Architekturtrigger entsteht:** neues System, Änderung, Migration, externe Integration oder Finding.
2. **Kontext aufnehmen:** Zweck, Daten, Nutzer, Schnittstellen, Abhängigkeiten, Exposition und Betriebsmodell erfassen.
3. **Prinzipien anwenden:** Vertrauensgrenzen, geringstmögliche Rechte, Trennung, sichere Defaults, Beobachtbarkeit und Wartbarkeit prüfen.
4. **Risiken bewerten:** strukturelle Schwächen, Abhängigkeiten, Legacy-Anteile und Ausfallszenarien einordnen.
5. **Entscheidung dokumentieren:** gewählte Architektur, Alternativen, Restrisiken und offene Maßnahmen festhalten.
6. **Umsetzung begleiten:** technische Leitplanken, Plattformstandards und Reviews in Umsetzung und Change einbinden.
7. **Validieren:** Tests, Betriebsübergabe, Monitoring, Schwachstellenbefunde oder Architekturabnahme prüfen.
8. **Abweichungen steuern:** befristen, kompensieren, eskalieren oder in Migrationsplan überführen.
9. **Standards verbessern:** Muster aus Findings in Referenzarchitektur und Engineering-Prinzipien zurückspielen.

## Entscheidungen

- Welche Systeme brauchen einen Architektur-Sicherheitsreview?
- Welche Engineering-Prinzipien sind verpflichtend, welche sind Zielbild?
- Welche Abweichungen sind tolerierbar und wer akzeptiert sie?
- Wann ist eine technische Schuld ein Managementrisiko?
- Welche Plattformstandards sollen Teams entlasten?
- Wann muss eine Legacy-Architektur abgelöst statt kompensiert werden?

## Evidenz

### Starke Evidenz

- aktuelle Architektur- und Datenflussübersichten kritischer Systeme,
- dokumentierte Sicherheits- und Engineering-Prinzipien,
- Review- oder Entscheidungsprotokolle,
- Architecture Decision Records mit Sicherheitsbezug,
- Nachweise zu Segmentierung, Identitätsmodell, Logging, Backup oder Monitoring,
- Maßnahmen und Zieltermine für Abweichungen,
- Managemententscheidungen zu technischen Schulden oder Restrisiken.

### Schwache Evidenz

- veraltetes Architekturdiagramm ohne Owner oder Datum,
- allgemeine Prinzipienfolie ohne Anwendung auf Systeme,
- Toolkonfiguration ohne dokumentierte Architekturentscheidung,
- Review mit offenen Punkten ohne Nachverfolgung,
- Aussage „Cloud-Provider übernimmt Sicherheit“ ohne Verantwortlichkeitsklärung.

### Evidenzlücken

- keine Übersicht kritischer Datenflüsse oder Schnittstellen,
- keine dokumentierten Vertrauensgrenzen,
- technische Schulden ohne Risiko- oder Migrationsentscheidung,
- Abweichungen ohne Ablaufdatum,
- fehlende Betriebsanforderungen in Architekturentscheidungen,
- Lieferanten- oder Plattformabhängigkeiten ohne Owner.

## Wirksamkeitsprüfung

Prüffragen:

- Sind kritische Systeme mit Architektur, Ownern und Datenflüssen nachvollziehbar beschrieben?
- Werden Sicherheitsprinzipien bei neuen und geänderten Architekturen angewendet?
- Führen Reviews zu konkreten Entscheidungen, Maßnahmen oder Ausnahmen?
- Sind technische Schulden und Legacy-Risiken transparent und priorisiert?
- Werden wiederkehrende Findings in Architekturstandards übersetzt?
- Sind Cloud-, Plattform- und Lieferantenabhängigkeiten in der Architektur sichtbar?

Mögliche Kennzahlen:

- Anteil kritischer Systeme mit aktuellem Architekturreview,
- offene Architekturabweichungen nach Kritikalität,
- technische Schulden mit Managemententscheidung,
- wiederkehrende Architektur-Findings,
- Systeme ohne aktuelle Datenflussübersicht,
- Ausnahmequote bei Referenzarchitekturen.

## BSIG-/NIS2-Anschluss

Sichere Systemarchitektur und Engineering-Grundsätze sind anschlussfähig an NIS2-orientierte Themen wie Risikomanagement, Schutz digitaler Dienste, sichere Entwicklung, Business Continuity, Lieferkettensicherheit, Schwachstellenmanagement und Cyberhygiene. Der konkrete Bezug sollte im Anforderungsregister und in Risiko- sowie Managementreviews organisationsspezifisch geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Prüfung und keine technische Sicherheitszusage.

## Grenzen

- Dieses Artefakt ist keine vollständige Referenzarchitektur und keine technische Hardening-Baseline.
- Es ersetzt keine detaillierte Cloud-, Netzwerk-, Produkt- oder Resilienzprüfung.
- Es trifft keine Aussage zur Zertifizierungsfähigkeit oder gesetzlichen Konformität.
- Es enthält keine ISO-27002-Texte und keine vertraulichen Architekturdetails.
- Es ersetzt keine menschliche Entscheidung über Zielarchitektur, Migration oder Risikoakzeptanz.

## Handoffs

- **Entwicklungs-Handoff:** Architekturentscheidungen müssen in Backlog, Code, Tests und Releasegates umgesetzt werden.
- **Betriebs-Handoff:** Monitoring, Backup, Patchbarkeit, Wiederanlauf, Logging und Supportmodell vor Übergabe klären.
- **Cloud-/Plattform-Handoff:** Landing Zones, Infrastrukturvorlagen, Identität, Netzwerkzonen und technische Leitplanken.
- **Datenschutz-/Legal-Handoff:** personenbezogene Datenflüsse, Aufbewahrung, Protokollierung, Mandantentrennung oder Vertragszusagen.
- **Lieferanten-Handoff:** externe Plattformen, Managed Services, proprietäre Abhängigkeiten oder unklare Verantwortlichkeiten.
- **BCM-/Krisen-Handoff:** Architekturentscheidungen mit Auswirkungen auf Verfügbarkeit, Wiederanlauf oder kritische Prozesse.
- **Management-Handoff:** große technische Schulden, Migrationsbedarf, nicht kompensierbare Risiken oder Zielkonflikte.

## Typische Fehler

- Architekturreviews finden nur für große Projekte statt, nicht für riskante kleine Änderungen.
- Diagramme werden gepflegt, aber Entscheidungen und Risiken nicht dokumentiert.
- Sicherheitsprinzipien sind bekannt, aber nicht in Plattformen oder Templates übersetzt.
- Legacy-Ausnahmen werden dauerhaft, weil kein Zielbild existiert.
- Betriebsanforderungen werden erst nach dem Go-live sichtbar.
- Lieferanten- und Cloud-Verantwortlichkeiten bleiben implizit.
- Management bekommt technische Details, aber keine klare Risiko- oder Investitionsentscheidung.

## Fiktives Mini-Beispiel

Ein fiktiver Industriebetrieb migriert eine interne Anwendung in eine Cloud-Umgebung. Der Architekturreview zeigt neue externe Schnittstellen, ein geändertes Identitätsmodell und höhere Anforderungen an Monitoring. Das Team dokumentiert die Entscheidung, nutzt eine freigegebene Netzwerk- und Identitätsvorlage und legt eine befristete Ausnahme für ein Legacy-Protokoll an. Im Management Review wird entschieden, die Legacy-Komponente innerhalb von sechs Monaten abzulösen.

Evidenz:

- Architektur- und Datenflussübersicht,
- dokumentierte Architekturentscheidung,
- Reviewprotokoll mit Sicherheitsprinzipien,
- Plattformvorlage als Umsetzungsnachweis,
- Ausnahme mit Migrationsziel,
- Managemententscheidung zur Ablösung.
