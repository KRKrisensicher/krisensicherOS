
# A.8.29 — Sicherheitstests in Entwicklung und Abnahme

## Zweck

Sicherheitstests in Entwicklung und Abnahme sorgen dafür, dass Sicherheitsanforderungen, Architekturannahmen und Coding-Entscheidungen vor produktiver Nutzung geprüft werden. Ziel ist nicht möglichst viel Testvolumen, sondern risikobasierte Testfähigkeit: Die richtigen Dinge werden zum richtigen Zeitpunkt getestet, Findings werden entschieden und Abnahmen bleiben nachvollziehbar.

Der Kern ist eine Test- und Abnahmeroutine, die Entwicklung, Security, QA, Betrieb und Product Owner verbindet.

## Control-Ziel in Repo-Sprache

Die Organisation plant, führt und bewertet Sicherheitstests risikobasiert in Entwicklung, Release und Abnahme. Testergebnisse führen zu Behebung, Kompensation, Risikoentscheidung oder Releaseblockade. Abnahmen zeigen, welche Sicherheitsanforderungen geprüft wurden und welche Restrisiken offen bleiben.

## Typische Risiken

- Wenn Sicherheitstests erst nach Fertigstellung stattfinden, sind Findings teuer, politisch schwierig oder werden trotz Risiko akzeptiert.
- Wenn Tests nicht an Anforderungen und Architektur gekoppelt sind, prüfen sie zufällige Punkte statt relevante Risiken.
- Wenn Testumgebungen produktionsfremd sind, bleiben Konfigurations-, Berechtigungs- oder Integrationsfehler unentdeckt.
- Wenn Findings nicht triagiert werden, entstehen lange Listen ohne Entscheidung und ohne Behebung.
- Wenn externe Tests ohne Scope, Regeln und Nachverfolgung laufen, entstehen Lücken, Betriebsrisiken oder unklare Verantwortlichkeiten.
- Wenn Abnahmeprotokolle offene Sicherheitsrisiken nicht ausweisen, trifft der Product Owner keine echte Releaseentscheidung.

## Trigger

- neues Produkt, neue Anwendung, relevantes Release oder neue kritische Funktion.
- Änderung an Authentisierung, Autorisierung, Schnittstellen, Datenflüssen, Kryptografie, Logging oder Plattform.
- neue externe Erreichbarkeit, neue Datenklasse, neue Mandantentrennung oder neue Lieferantenintegration.
- Sicherheitsanforderung, Architekturreview, Codefinding oder Schwachstellenmeldung.
- Penetrationstest, Red-Team-Übung, Bug Report, Incident oder Auditfinding.
- Abnahme vor Go-live, Kundenfreigabe, Betriebsübergabe oder wesentlicher Change.
- regelmäßiger Review des Testportfolios für kritische Anwendungen.

## Rollen und Verantwortung

- **Product Owner / Service Owner:** entscheidet Release, Priorisierung, Akzeptanz offener Findings und fachliche Auswirkungen.
- **Test-/QA-Rolle:** plant Testfälle, dokumentiert Ergebnisse und verbindet Anforderungen mit Abnahme.
- **Entwicklungsteam:** behebt Findings, ergänzt Tests und erklärt technische Ursachen.
- **Security-/AppSec-Rolle:** definiert Testtiefe, unterstützt Triage und bewertet kritische Findings.
- **Architekturrolle:** prüft, ob Tests relevante Vertrauensgrenzen, Schnittstellen und Datenflüsse abdecken.
- **IT-Betrieb / Plattformteam:** stellt testbare Umgebungen, Konfiguration, Logging, Monitoring und Betriebsübergabe sicher.
- **Externe Tester / Dienstleister:** liefern Tests innerhalb vereinbartem Scope, Regeln und Nachweisformat.
- **Management:** entscheidet bei Releasekonflikten, Ressourcenengpässen, Risikoakzeptanz oder wiederkehrenden kritischen Findings.

## Implementierung

### Minimalstart

Ziel: Sicherheitsrelevante Releases werden nicht ohne nachvollziehbare Prüfung und Entscheidung abgenommen.

1. Kritische Anwendungen, Releases und Änderungen werden identifiziert.
2. Für diese Vorhaben werden Sicherheitsanforderungen in Test- oder Abnahmepunkte übersetzt.
3. Mindestens grundlegende Prüfungen werden festgelegt: Rollen/Rechte, Eingaben, Fehlerfälle, Schnittstellen, Logging, Secrets, bekannte Schwachstellen.
4. Findings werden in einem Ticket- oder Maßnahmenlog mit Owner, Priorität und Entscheidung geführt.
5. Vor Go-live dokumentiert der Product Owner, welche kritischen Findings behoben, offen, kompensiert oder akzeptiert sind.
6. Testscope und Testergebnisse werden so abgelegt, dass sie später nachvollziehbar sind.

Minimaler Nachweis:

- Liste sicherheitsrelevanter Releases oder Anwendungen,
- Testscope mit Sicherheitsanforderungen,
- Testprotokoll oder Toolnachweis,
- Finding-Liste mit Entscheidungen,
- Abnahmeprotokoll mit offenen Restrisiken.

### Solide Praxis

Ziel: Sicherheitstests werden risikobasiert, wiederholbar und mit Entwicklung sowie Abnahme verbunden.

1. Testtiefe wird anhand von Kritikalität, Exposition, Datenklasse, Änderungstyp und Architektur bestimmt.
2. Testarten werden sinnvoll kombiniert: manuelle Sicherheitschecks, automatisierte Scans, Code-/Dependency-Prüfungen, API-Tests, Konfigurationsprüfungen, Penetrationstests oder Abnahmetests.
3. Testumgebungen, Testdaten und Berechtigungen werden kontrolliert bereitgestellt.
4. Findings werden nach Risiko, Ausnutzbarkeit, Betroffenheit und Betriebswirkung triagiert.
5. Releasekriterien definieren, welche Findings blockieren und welche mit Maßnahme oder Ausnahme akzeptiert werden können.
6. Re-Tests oder Validierungen bestätigen Behebung kritischer Findings.
7. Testergebnisse fließen in Backlog, Sicherheitsanforderungen, Coding-Guidelines und Architekturstandards zurück.

Starke Evidenz:

- risikobasierter Testplan,
- Zuordnung von Anforderungen zu Testfällen,
- Testprotokolle, Scanberichte oder externe Testberichte mit Scope,
- Finding-Log mit Triage und Ownern,
- Re-Test- oder Validierungsnachweise,
- Release- und Abnahmeentscheidung,
- Lessons Learned und Verbesserungsmaßnahmen.

### Fortgeschritten

Ziel: Sicherheitstests liefern kontinuierliche Steuerungsinformationen für Produkt, Architektur und Betrieb.

1. Automatisierte Tests und Security-Gates sind in CI/CD und Releaseprozesse integriert.
2. Kritische Systeme erhalten regelmäßig unabhängige oder vertiefte Tests nach risikobasiertem Plan.
3. Testabdeckung wird gegen Architektur, Datenflüsse, Bedrohungsszenarien und vergangene Findings geprüft.
4. Externe Tests, interne Toolsignale und Betriebsmonitoring werden in einem gemeinsamen Finding- und Risikobild zusammengeführt.
5. Management erhält entscheidungsfähige Kennzahlen zu offenen kritischen Findings, Re-Test-Erfolg, Ausnahmequote, Testabdeckung und wiederkehrenden Ursachen.
6. Testmethodik wird nach Incidents, neuen Angriffsmustern und Technologieänderungen aktualisiert.

## Ablauf als Routine

1. **Testtrigger entsteht:** neues Release, kritische Änderung, Architekturreview, Finding oder Abnahmebedarf.
2. **Testscope definieren:** Anwendung, Funktionen, Schnittstellen, Rollen, Daten, Umgebung und Ausschlüsse festlegen.
3. **Testtiefe bestimmen:** Kritikalität, Exposition, Datenklasse, Änderungstyp und frühere Findings berücksichtigen.
4. **Tests planen:** Anforderungen, Testfälle, Tools, manuelle Prüfungen, externe Tester und Zeitfenster festlegen.
5. **Durchführen:** Tests kontrolliert ausführen und Betriebsrisiken beachten.
6. **Findings triagieren:** Schwere, Ausnutzbarkeit, Geschäftsrisiko, False Positives und Behebungsweg bewerten.
7. **Behandeln und validieren:** Fix, Konfiguration, Kompensation, Re-Test oder Ausnahme dokumentieren.
8. **Abnahme entscheiden:** Release freigeben, blockieren oder mit Restrisikoentscheidung versehen.
9. **Verbessern:** Muster in Anforderungen, Architektur, Coding, Betrieb und Testmethodik zurückführen.

## Entscheidungen

- Welche Anwendungen und Änderungen brauchen welche Testtiefe?
- Welche Findings blockieren Release oder Abnahme?
- Wer darf offene Findings akzeptieren und für wie lange?
- Wann ist ein Re-Test zwingend?
- Welche Tests können automatisiert werden, welche brauchen manuelle oder externe Prüfung?
- Welche Testdaten und Testumgebungen sind zulässig?
- Wann wird ein Finding zum Incident oder Managementthema?

## Evidenz

### Starke Evidenz

- Teststrategie oder risikobasierter Testplan,
- Testscope mit Annahmen und Ausschlüssen,
- Zuordnung von Sicherheitsanforderungen zu Testfällen,
- Testprotokolle und Toolnachweise,
- externe Testberichte mit Scope und Datum,
- priorisierte Findings mit Owner, Frist und Status,
- Re-Test- oder Validierungsnachweise,
- Abnahmeentscheidung mit offenen Restrisiken und Wiedervorlage.

### Schwache Evidenz

- Scanbericht ohne Scope, Triage oder Behebungsstatus,
- Penetrationstestbericht ohne Nachverfolgung,
- Abnahmeprotokoll ohne offene Sicherheitsrisiken,
- Testfälle ohne Bezug zu Sicherheitsanforderungen,
- pauschale Aussage „QA hat getestet“,
- Tooldashboard ohne Releaseentscheidung.

### Evidenzlücken

- keine Kriterien, welche Releases Sicherheitstests brauchen,
- kritische Findings ohne Owner oder Frist,
- keine Validierung nach Behebung,
- Testumgebung weicht sicherheitsrelevant von Produktion ab, ohne Bewertung,
- externe Testergebnisse werden nicht in Backlog oder Risikoentscheidungen überführt,
- offene Findings gehen live ohne dokumentierte Akzeptanz.

## Wirksamkeitsprüfung

Prüffragen:

- Werden Sicherheitstests risikobasiert vor relevanten Releases geplant?
- Sind Testscope, Testtiefe und Ausschlüsse nachvollziehbar?
- Sind Tests mit Sicherheitsanforderungen, Architektur und bekannten Risiken verbunden?
- Werden Findings priorisiert, behoben und validiert?
- Sind Release- und Abnahmeentscheidungen bei offenen Findings nachvollziehbar?
- Verbessern Testergebnisse Anforderungen, Architektur, Coding und Betrieb?

Mögliche Kennzahlen:

- Anteil kritischer Releases mit Sicherheitstestnachweis,
- offene kritische Findings vor Go-live,
- Re-Test-Erfolgsquote,
- mittlere Behebungszeit je Kritikalität,
- Findings ohne Owner oder Entscheidung,
- wiederkehrende Finding-Kategorien,
- Abweichungen zwischen Testscope und Produktionsrealität.

## BSIG-/NIS2-Anschluss

Sicherheitstests in Entwicklung und Abnahme sind anschlussfähig an NIS2-orientierte Themen wie sichere Entwicklung, Schwachstellenmanagement, Risikomanagement, Cyberhygiene, Incident-Prävention und Schutz digitaler Dienste. Der konkrete Bezug sollte im Anforderungsregister, in Risikoanalysen und bei Managemententscheidungen organisationsspezifisch geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung, keine Meldepflichtprüfung und keine Zertifizierungszusage.

## Grenzen

- Dieses Artefakt ist keine Penetrationstest-Methodik und keine Toolauswahl.
- Es ersetzt keine technische Prüfung durch qualifizierte Tester bei kritischen Systemen.
- Es garantiert nicht, dass eine Anwendung frei von Schwachstellen ist.
- Es enthält keine ISO-27002-Texte und keine vertraulichen Findings.
- Es ersetzt keine Datenschutzprüfung für Testdaten, Protokollierung oder externe Tester.

## Handoffs

- **Anforderungs-Handoff:** fehlende oder untestbare Sicherheitsanforderungen müssen in Spezifikation oder Backlog zurück.
- **Architektur-Handoff:** Findings aus Vertrauensgrenzen, Schnittstellen, Datenflüssen oder Plattformdesign.
- **Secure-Coding-Handoff:** Codefehler, Dependency-Findings, Secrets oder wiederkehrende Fehlerklassen.
- **Betriebs-Handoff:** Konfiguration, Logging, Monitoring, Patchfähigkeit, Testumgebung und Produktionsabweichungen.
- **Incident-Handoff:** aktive Ausnutzung, Kompromittierungsverdacht oder kritisches produktives Finding.
- **Datenschutz-/Legal-Handoff:** Testdaten, externe Tester, personenbezogene Protokolle, Vertrags- oder Kundenzusagen.
- **Management-Handoff:** Release trotz kritischer Findings, Ressourcenmangel, Ausnahmeentscheidung oder wiederkehrende strukturelle Schwächen.

## Typische Fehler

- Sicherheitstests werden als einmaliger Penetrationstest vor Launch verstanden.
- Tests prüfen Toolstandard statt konkrete Risiken der Anwendung.
- Kritische Findings werden geschlossen, ohne Re-Test oder Validierung.
- Abnahmen dokumentieren Funktionsfreigabe, aber keine Sicherheitsentscheidung.
- Testdaten enthalten echte personenbezogene oder vertrauliche Informationen ohne Klärung.
- Externe Testberichte landen in der Ablage, aber nicht im Backlog.
- Automatisierte Scans blockieren Teams ohne Triage und Priorisierung.

## Fiktives Mini-Beispiel

Ein fiktiver SaaS-Anbieter plant ein Release mit neuer API-Funktion. Wegen externer Erreichbarkeit und Rollenmodell wird ein Sicherheitstest vor Go-live angesetzt. QA erstellt Testfälle zu Berechtigungen und Fehlerantworten, AppSec führt API-Tests durch, ein Scan meldet eine verwundbare Bibliothek. Das Team aktualisiert die Abhängigkeit und validiert den Fix. Ein niedriges Logging-Finding wird mit Frist in den nächsten Sprint übernommen und im Abnahmeprotokoll dokumentiert.

Evidenz:

- risikobasierter Testscope,
- Testfälle zu Sicherheitsanforderungen,
- API-Test- und Scanergebnisse,
- Ticket und Validierung zum Dependency-Fix,
- Abnahmeprotokoll mit offenem niedrigem Finding,
- Backlog-Eintrag für Nacharbeit.
