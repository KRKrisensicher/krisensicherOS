
# A.8.25 — Sicherer Entwicklungslebenszyklus

## Zweck

Ein sicherer Entwicklungslebenszyklus sorgt dafür, dass Informationssicherheit nicht erst kurz vor dem Go-live geprüft wird. Sicherheitsfragen werden von Idee, Anforderung, Architektur, Umsetzung, Test, Release, Betrieb und Außerbetriebnahme mitgeführt.

Der Kern ist keine große Prozessbürokratie, sondern eine klare Arbeitsweise: Welche Sicherheitsentscheidungen müssen in welchem Entwicklungsschritt getroffen werden, wer trifft sie, welche Mindestprüfungen gelten und welche Evidenz entsteht?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt Entwicklung so, dass Sicherheitsanforderungen, Risiken, Architekturentscheidungen, Codequalität, Tests, Freigaben, Betriebsübergabe und Lessons Learned nachvollziehbar zusammenhängen. Der Entwicklungsprozess macht sichtbar, wann Sicherheitsrisiken akzeptiert, behandelt oder eskaliert werden.

## Typische Risiken

- Wenn Sicherheitsanforderungen erst am Ende betrachtet werden, entstehen teure Nacharbeiten oder unsichere Releases.
- Wenn Produkt-, Entwicklungs- und Betriebsteams unterschiedliche Sicherheitsannahmen haben, bleiben Lücken zwischen Design, Umsetzung und Betrieb.
- Wenn externe Entwicklungsanteile nicht in die gleiche Governance eingebunden sind, entstehen unbekannte Abhängigkeiten, unsichere Komponenten oder fehlende Nachweise.
- Wenn Findings aus Tests nicht in Releaseentscheidungen einfließen, gehen bekannte Schwächen produktiv.
- Wenn Sicherheitsentscheidungen nicht dokumentiert werden, sind Ausnahmen, Restrisiken und technische Schulden später nicht mehr nachvollziehbar.
- Wenn Außerbetriebnahme und Wartungsende fehlen, bleiben veraltete Anwendungen, Repositories oder Schnittstellen aktiv.

## Trigger

- neues Produkt, neue Anwendung, größere Funktion oder relevantes Release.
- Architektur-, Technologie-, Cloud-, Plattform- oder Schnittstellenänderung.
- neue Datenklasse, neue Nutzergruppe, externe Erreichbarkeit oder erhöhte Kritikalität.
- Schwachstelle, Sicherheitsereignis, Penetrationstest- oder Auditfinding.
- Wechsel von Entwicklungsdienstleister, Framework, Build-Pipeline oder Betriebsmodell.
- Entscheidung über Go-live, Ausnahme, Wartungsende oder Außerbetriebnahme.
- turnusmäßiger Review des Entwicklungsprozesses und seiner Sicherheitsgates.

## Rollen und Verantwortung

- **Product Owner / Service Owner:** verantwortet Geschäftsbedarf, Schutzbedarf, Priorisierung und Releaseentscheidung.
- **Entwicklungsteam / Tech Lead:** setzt Sicherheitsanforderungen, sichere Programmierpraktiken und technische Maßnahmen um.
- **Security-Rolle / AppSec-Rolle:** definiert Mindestgates, unterstützt Risiko- und Testlogik und bewertet kritische Findings.
- **Architekturrolle:** prüft Architekturentscheidungen, Vertrauensgrenzen, Integrationen und technische Schulden.
- **IT-Betrieb / Plattformteam:** übernimmt Betriebsanforderungen, Monitoring, Konfiguration und Patchfähigkeit.
- **ISMS-Owner:** verbindet Entwicklungsroutine mit Risikoregister, Maßnahmenlog, Evidenz und Management Review.
- **Einkauf / Lieferantenmanagement:** bindet externe Entwicklung, SaaS, Komponenten und Dienstleister ein.
- **Management:** entscheidet bei Ressourcenmangel, akzeptierten Restrisiken, Termin-/Sicherheitskonflikten und dauerhaften Ausnahmen.

## Implementierung

### Minimalstart

Ziel: Sicherheitsentscheidungen in jedem relevanten Entwicklungsvorhaben sichtbar machen.

1. Die Organisation legt fest, welche Anwendungen und Entwicklungsvorhaben im Scope sind.
2. Für jedes Vorhaben werden Product Owner, technischer Owner und Sicherheitsansprechpunkt benannt.
3. Eine kurze Sicherheits-Checkliste wird in Planung, Umsetzung, Test und Release genutzt.
4. Sicherheitsanforderungen, kritische Architekturannahmen und offene Risiken werden im Ticket- oder Maßnahmenlog erfasst.
5. Vor Go-live wird geprüft, ob kritische Findings geschlossen, akzeptiert oder eskaliert sind.
6. Externe Entwicklungsanteile werden mit Mindestnachweisen und Ansprechpartnern eingebunden.

Minimaler Nachweis:

- Vorhabenliste mit Ownern,
- Sicherheits-Checkliste oder Gate-Nachweis,
- dokumentierte Sicherheitsanforderungen und offene Risiken,
- Test- oder Reviewnachweise,
- Releaseentscheidung mit offenen Findings oder Ausnahmeentscheidungen.

### Solide Praxis

Ziel: Sicherheit wird wiederholbar in den Entwicklungsprozess integriert.

1. Der Entwicklungsprozess enthält definierte Sicherheitsaktivitäten je Phase: Anforderungsanalyse, Design, Code, Build, Test, Release, Betrieb.
2. Risiko- und Schutzbedarfslogik bestimmen, welche Sicherheitsgates notwendig sind.
3. Architekturreviews, Code Reviews, Dependency-Prüfungen und Sicherheitstests sind risikobasiert vorgesehen.
4. Findings werden priorisiert, einem Owner zugeordnet und vor Release entschieden.
5. Externe Entwicklung wird über Verträge, Liefergegenstände, Nachweise und Abnahme eingebunden.
6. Sicherheitsbezogene technische Schulden werden im Backlog geführt und reviewed.
7. Lessons Learned aus Incidents, Tests und Betriebsproblemen fließen in Standards und Templates zurück.

Starke Evidenz:

- definierter SDLC mit Sicherheitsgates,
- risikobasierte Gate-Kriterien,
- Architektur- und Code-Review-Nachweise,
- Test- und Findings-Log,
- Releasefreigaben mit Sicherheitsentscheidung,
- Backlog für Sicherheitsmaßnahmen und technische Schulden,
- Lieferantennachweise für externe Entwicklungsanteile.

### Fortgeschritten

Ziel: Der Entwicklungslebenszyklus erzeugt laufend steuerbare Sicherheitsinformationen.

1. Sicherheitsgates sind in CI/CD, Ticketing, Architekturentscheidungen und Releaseprozesse integriert.
2. Threat Modeling, Abuse Cases oder vergleichbare Methoden werden für kritische Vorhaben genutzt.
3. Build-, Dependency-, Secret- und Container-Prüfungen liefern automatisierte Signale an Teams.
4. Releaseentscheidungen nutzen Risikoindikatoren wie offene kritische Findings, Testabdeckung, Ausnahmen und Betriebsfähigkeit.
5. Sicherheitsmuster, sichere Templates und Plattform-Controls reduzieren Wiederholungsaufwand.
6. Management sieht nicht nur Toolmetriken, sondern Entscheidungsbedarf: überfällige Sicherheitsarbeit, technische Schulden, Risikoakzeptanzen und Ressourcenengpässe.

## Ablauf als Routine

1. **Vorhaben startet:** Product Owner oder Tech Lead meldet neues oder geändertes Entwicklungsvorhaben.
2. **Scope und Risiko klären:** Daten, Nutzergruppen, Exposition, Kritikalität, Lieferanten und Betriebsmodell einordnen.
3. **Sicherheitsaktivitäten planen:** notwendige Anforderungen, Architekturreview, Tests und Freigaben festlegen.
4. **Umsetzung begleiten:** Sicherheitsanforderungen in Tickets, Definition of Done oder Akzeptanzkriterien aufnehmen.
5. **Reviews und Tests durchführen:** Architektur, Code, Abhängigkeiten, Pipeline und Anwendung risikobasiert prüfen.
6. **Findings entscheiden:** beheben, kompensieren, zurückstellen, akzeptieren oder eskalieren.
7. **Release freigeben:** Go-live nur mit nachvollziehbarer Sicherheits- und Restrisikoentscheidung.
8. **Betriebsübergabe sichern:** Monitoring, Patchfähigkeit, Owner, Dokumentation und Supportpfade übergeben.
9. **Lernen:** Findings, Incidents und Betriebsprobleme in Standards, Backlog und Schulung zurückspielen.

## Entscheidungen

- Welche Entwicklungsvorhaben fallen in den gesicherten Entwicklungsprozess?
- Welche Sicherheitsgates sind für welche Kritikalität verpflichtend?
- Wann darf ein Release trotz offener Findings live gehen?
- Wer akzeptiert technische Schulden oder Restrisiken und für wie lange?
- Welche externen Entwicklungsnachweise sind ausreichend?
- Welche Automatisierung lohnt sich, ohne Teams mit Fehlalarmen zu überlasten?

## Evidenz

### Starke Evidenz

- Vorhaben- oder Anwendungsregister mit Kritikalität und Ownern,
- Sicherheitsanforderungen in Backlog oder Spezifikation,
- Architekturentscheidungen und Reviewprotokolle,
- Code-, Dependency-, Pipeline- und Sicherheitstestnachweise,
- Finding-Log mit Priorität, Owner, Frist und Status,
- Releasefreigabe mit Restrisikoentscheidung,
- Nachweise zur Betriebsübergabe und Lessons Learned.

### Schwache Evidenz

- allgemeine Entwicklungsrichtlinie ohne konkrete Anwendung auf Vorhaben,
- Toolberichte ohne Triage oder Releasebezug,
- mündliche Aussage „Security prüft mit“ ohne Gate oder Nachweis,
- Backlog-Tickets ohne Sicherheitspriorisierung,
- Lieferantenzusage ohne überprüfbare Liefernachweise.

### Evidenzlücken

- keine Liste der Anwendungen oder Entwicklungsvorhaben im Scope,
- keine benannten Owner für Sicherheit im Vorhaben,
- offene kritische Findings ohne Releaseentscheidung,
- externe Entwicklung ohne Sicherheitsnachweise,
- keine Rückführung von Incidents oder Tests in den Entwicklungsprozess.

## Wirksamkeitsprüfung

Prüffragen:

- Sind sicherheitsrelevante Entwicklungsvorhaben frühzeitig im Prozess sichtbar?
- Werden Sicherheitsanforderungen, Architekturentscheidungen und Tests risikobasiert geplant?
- Können offene Findings einer Release- oder Risikoentscheidung zugeordnet werden?
- Sind externe Entwicklungsanteile in Gates und Evidenz eingebunden?
- Führt der Prozess zu weniger wiederkehrenden Findings oder schnelleren Entscheidungen?
- Erhält das Management entscheidungsfähige Informationen zu Restrisiken und Ressourcenbedarf?

Mögliche Kennzahlen:

- Anteil kritischer Vorhaben mit Sicherheitsgate,
- offene kritische Findings vor Release,
- überfällige Sicherheitsmaßnahmen im Backlog,
- Anteil externer Entwicklungsanteile mit Nachweisen,
- wiederkehrende Finding-Typen,
- Anzahl akzeptierter Restrisiken und deren Wiedervorlagen.

## BSIG-/NIS2-Anschluss

Ein sicherer Entwicklungslebenszyklus ist anschlussfähig an NIS2-orientierte Themen wie Risikomanagement, sichere Entwicklung, Schwachstellenbehandlung, Lieferkettensicherheit, Cyberhygiene und Sicherheit digitaler Dienste. Der konkrete Bezug sollte im Anforderungsregister, in Risikoanalysen und bei Managemententscheidungen organisationsspezifisch geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung, keine Datenschutzprüfung und keine Aussage zur Anwendbarkeit.

## Grenzen

- Dieses Artefakt ist kein vollständiges AppSec-Programm und kein CI/CD-Tooldesign.
- Es ersetzt keine technische Architektur-, Code- oder Penetrationstestprüfung.
- Es trifft keine Zertifizierungs-, Konformitäts- oder Sicherheitsgarantie.
- Es enthält keine ISO-27002-Texte und keine vertraulichen Entwicklungsdetails.
- Es darf nicht als Ersatz für menschliche Risiko- und Releaseentscheidungen genutzt werden.

## Handoffs

- **Architektur-Handoff:** neue Vertrauensgrenzen, kritische Schnittstellen, Cloud-/Plattformwechsel, hohe technische Schulden.
- **Secure-Coding-Handoff:** wiederkehrende Codefehler, unsichere Patterns, fehlende Entwicklerbefähigung.
- **Sicherheitstest-Handoff:** neue kritische Funktion, externer Go-live, hohe Kritikalität oder ungeklärte Findings.
- **Betriebs-Handoff:** Monitoring, Patchfähigkeit, Incident-Kontakte, Konfiguration und Supportmodell vor Go-live.
- **Lieferanten-Handoff:** externe Entwicklung, Fremdkomponenten, SaaS, fehlende Nachweise oder unklare Verantwortlichkeiten.
- **Datenschutz-/Legal-Handoff:** personenbezogene Daten, vertragliche Zusagen, Nutzungsbedingungen, Logging oder grenzüberschreitende Verarbeitung.
- **Management-Handoff:** Release trotz kritischer Findings, Ressourcenmangel, dauerhafte Ausnahme, akzeptiertes Restrisiko.

## Typische Fehler

- Security wird als spätes Abnahmehindernis statt als Entwicklungsroutine eingebunden.
- Gates existieren, werden aber bei Termindruck übersprungen.
- Toolfunde werden erzeugt, aber nicht risikobasiert entschieden.
- Externe Entwicklung wird schneller beauftragt als sicherheitsseitig gesteuert.
- Releasefreigaben dokumentieren Funktionalität, aber keine offenen Sicherheitsrisiken.
- Lessons Learned aus Incidents ändern weder Templates noch Standards.
- Der Prozess ist so schwergewichtig, dass Teams ihn umgehen.

## Fiktives Mini-Beispiel

Ein fiktiver Softwareanbieter entwickelt ein neues Kundenmodul. Beim Vorhabenstart wird wegen externer Erreichbarkeit und personenbezogener Daten ein Architekturreview festgelegt. Das Entwicklungsteam ergänzt Sicherheitsanforderungen im Backlog, führt Dependency-Scans und Code Reviews durch und dokumentiert zwei Findings. Ein kritisches Finding wird vor Release behoben; ein mittleres Finding erhält eine befristete Ausnahme mit Maßnahme im nächsten Sprint. Der Betrieb übernimmt Monitoring und Patchverantwortung.

Evidenz:

- Vorhabeneintrag mit Kritikalität,
- Sicherheitsanforderungen im Backlog,
- Architekturreview,
- Scan- und Code-Review-Nachweise,
- Finding-Entscheidung vor Release,
- Betriebsübergabe mit Ownern.
