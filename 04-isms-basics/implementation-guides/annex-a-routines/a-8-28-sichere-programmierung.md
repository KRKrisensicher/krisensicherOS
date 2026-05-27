
# A.8.28 — Sichere Programmierung

## Zweck

Sichere Programmierung sorgt dafür, dass Code, Konfigurationen, Skripte und Automatisierungen nicht systematisch vermeidbare Schwachstellen erzeugen. Es geht nicht um perfekte Fehlerfreiheit, sondern um eine belastbare Routine für sichere Patterns, Reviews, Toolsignale, Entwicklerbefähigung und Umgang mit Findings.

Der Kern ist: Teams wissen, welche Fehlerklassen für ihre Technologien relevant sind, wie sichere Umsetzung aussieht, welche Prüfungen vor Merge oder Release gelten und wie Abweichungen entschieden werden.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine sichere Coding-Routine, die Entwicklungsleitlinien, Code Reviews, automatisierte Prüfungen, Dependency- und Secret-Checks, sichere Framework-Nutzung, Entwicklerbefähigung und Finding-Behandlung verbindet. Sicherheitsrelevante Codeentscheidungen werden nachvollziehbar, testbar und verbesserbar.

## Typische Risiken

- Wenn Entwicklerinnen und Entwickler keine sicheren Patterns kennen, entstehen wiederkehrende Fehler bei Eingaben, Ausgaben, Authentisierung, Autorisierung, Sessions, Fehlerbehandlung oder Kryptografie.
- Wenn Code Reviews nur Funktionalität prüfen, bleiben sicherheitsrelevante Logikfehler unentdeckt.
- Wenn Secrets, Tokens oder Zugangsdaten in Repositories landen, können Systeme und Daten kompromittiert werden.
- Wenn Abhängigkeiten ungeprüft eingebunden werden, entstehen verwundbare oder nicht wartbare Komponenten.
- Wenn Security-Tools viele Findings erzeugen, aber niemand triagiert, werden kritische Signale ignoriert.
- Wenn KI-gestützter Code ungeprüft übernommen wird, können unsichere Muster, Lizenz- oder Qualitätsprobleme in Produkte gelangen.

## Trigger

- neuer Code, Merge Request, Pull Request, Release oder Hotfix.
- neue Bibliothek, Framework, Container-Image, Build-Tool oder Codegenerator.
- Sicherheitsfinding aus SAST, DAST, SCA, Secret-Scan, Code Review, Test oder Incident.
- neue Fehlerklasse, Schwachstellenmeldung oder wiederkehrendes Finding-Muster.
- Einstieg neuer Entwickler, externes Entwicklungsteam oder Technologie-Wechsel.
- Änderung an Authentisierung, Berechtigungen, Eingabevalidierung, Kryptografie, Logging oder Datenzugriff.
- Review der Coding-Guidelines und Tool-Gates.

## Rollen und Verantwortung

- **Entwicklungsteam:** setzt sichere Patterns um, führt Peer Reviews durch und bearbeitet Findings.
- **Tech Lead:** verantwortet Coding-Standards, Reviewqualität, technische Entscheidungen und Schulungsbedarf im Team.
- **Security-/AppSec-Rolle:** definiert sicherheitsrelevante Prüfbereiche, unterstützt Triage und verbessert Guidelines.
- **Product Owner:** priorisiert Sicherheitsarbeit im Backlog und entscheidet fachliche Auswirkungen.
- **DevOps-/Plattformteam:** betreibt Build-, Scan-, Secret- und Dependency-Prüfungen in der Pipeline.
- **ISMS-Owner:** verbindet Coding-Findings mit Risikoregister, Maßnahmen und Management Review.
- **Einkauf / Lieferantenmanagement:** bindet externe Entwicklung und Liefernachweise ein.
- **Management:** entscheidet bei Ressourcenmangel, Tooling, wiederkehrenden kritischen Schulden oder akzeptierten Restrisiken.

## Implementierung

### Minimalstart

Ziel: Die häufigsten vermeidbaren Code- und Repository-Risiken werden sichtbar und bearbeitet.

1. Für aktive Repositories werden Owner und verantwortliche Teams benannt.
2. Eine kurze sichere Coding-Checkliste wird für die genutzten Technologien erstellt.
3. Änderungen an sicherheitsrelevanten Funktionen benötigen Peer Review.
4. Secret-Scanning und Dependency-Prüfung werden mindestens für kritische Repositories eingeführt.
5. Kritische Findings werden als Tickets mit Owner, Priorität, Frist und Entscheidung erfasst.
6. Entwickler erhalten kurze, praxisnahe Hinweise zu wiederkehrenden Fehlern.

Minimaler Nachweis:

- Repository-Liste mit Ownern,
- Coding-Checkliste oder Teamstandard,
- Pull-/Merge-Request-Reviews,
- Scan- oder Prüfnachweise,
- Finding-Tickets mit Behandlung,
- Ausnahmeentscheidung bei offenen kritischen Findings.

### Solide Praxis

Ziel: Sichere Programmierung wird Teil des täglichen Entwicklungsflusses.

1. Coding-Guidelines sind technologiespezifisch und enthalten sichere Beispiele für relevante Fehlerklassen.
2. Reviewkriterien berücksichtigen Eingabevalidierung, Berechtigungslogik, Fehlerbehandlung, Logging, Secrets, Abhängigkeiten und sichere Framework-Nutzung.
3. SAST, SCA, Secret-Scanning und ausgewählte Lintersignale laufen in der Pipeline mit definierter Triage.
4. Toolfindings werden nach Risiko, Ausnutzbarkeit, Codepfad und Assetkritikalität bewertet.
5. Kritische oder wiederkehrende Findings führen zu Pairing, Schulung, Pattern-Änderung oder Architektur-Handoff.
6. Externe Entwickler nutzen dieselben Mindeststandards und liefern passende Nachweise.
7. KI-gestützte Codevorschläge werden wie anderer Code reviewed, getestet und nicht ungeprüft übernommen.

Starke Evidenz:

- technologiespezifische Coding-Guidelines,
- Review-Checklisten und Pull-/Merge-Request-Historie,
- Pipeline-Scanergebnisse mit Triage,
- Finding-Backlog mit Owner, Frist und Status,
- Nachweise behobener Secrets oder verwundbarer Abhängigkeiten,
- Schulungs- oder Team-Learning-Nachweise,
- Lieferantennachweise für externe Entwicklung.

### Fortgeschritten

Ziel: Coding-Sicherheit wird messbar verbessert und in Plattformen eingebettet.

1. Sichere Templates, Framework-Konfigurationen und interne Libraries reduzieren unsichere Einzelentscheidungen.
2. Pipeline-Gates sind risikobasiert: Kritische Findings blockieren, niedrigere Findings werden gesteuert statt blind blockiert.
3. Findings werden nach Ursache ausgewertet: Wissenslücke, unsicheres Framework-Pattern, fehlende Plattformfunktion, Architekturproblem oder Zeitdruck.
4. Security Champions oder vergleichbare Rollen unterstützen Teams direkt im Entwicklungsalltag.
5. Relevante Metriken zeigen Wiederholungsfehler, Behebungszeiten, False-Positive-Last und kritische technische Schulden.
6. Coding-Lessons-Learned aus Incidents und Tests ändern Guidelines, Templates und Trainings.

## Ablauf als Routine

1. **Codeänderung entsteht:** Feature, Bugfix, Infrastrukturcode, Skript, Automatisierung oder Hotfix.
2. **Sicherheitsrelevanz prüfen:** betrifft die Änderung Datenzugriff, Rollen, Eingaben, Secrets, Kryptografie, Logging, Schnittstellen oder Abhängigkeiten?
3. **Sichere Patterns anwenden:** Teamstandard, Frameworkfunktionen und geprüfte Bausteine nutzen.
4. **Prüfungen ausführen:** Peer Review, automatisierte Scans und relevante Tests durchführen.
5. **Findings triagieren:** echte Risiken, False Positives und technische Schulden unterscheiden.
6. **Behandeln:** Code ändern, Abhängigkeit aktualisieren, Secret rotieren, Test ergänzen oder Kompensation festlegen.
7. **Entscheiden:** offene kritische Findings vor Merge oder Release akzeptieren, blockieren oder eskalieren.
8. **Lernen:** wiederkehrende Muster in Guidelines, Templates, Schulung oder Architektur zurückführen.

## Entscheidungen

- Welche Repositories und Codearten sind für den Start kritisch?
- Welche Findings blockieren Merge oder Release?
- Wer darf eine Abweichung akzeptieren und wie lange?
- Welche Toolsignale werden genutzt, welche erzeugen zu viel Rauschen?
- Welche wiederkehrenden Fehler brauchen Training, Template oder Architekturänderung?
- Wie wird KI-unterstützter Code überprüft und dokumentiert?

## Evidenz

### Starke Evidenz

- Repository- und Ownerübersicht,
- sichere Coding-Guidelines mit Technologiebezug,
- Pull-/Merge-Request-Reviews mit Sicherheitskommentaren,
- Scanergebnisse mit nachvollziehbarer Triage,
- Tickets zu behobenen Findings,
- Secret-Rotation oder Dependency-Update-Nachweise,
- Ausnahmeentscheidungen mit Ablaufdatum,
- Nachweise zu Team-Learnings oder Guideline-Updates.

### Schwache Evidenz

- allgemeines Secure-Coding-PDF ohne Anwendung im Team,
- Tooldashboard ohne Triage oder Behebung,
- Code Review als reine Formalfreigabe,
- lange Finding-Liste ohne Priorisierung,
- Aussage „Framework verhindert das“ ohne Prüfnachweis,
- Schulungsteilnahme ohne Bezug zu wiederkehrenden Fehlern.

### Evidenzlücken

- aktive Repositories ohne Owner,
- kritische Findings ohne Ticket oder Entscheidung,
- Secrets im Repository ohne Rotationsnachweis,
- externe Entwicklung ohne Review- oder Scan-Nachweise,
- keine Behandlung wiederkehrender Fehlerklassen,
- KI-generierter Code ohne Review- und Testspur.

## Wirksamkeitsprüfung

Prüffragen:

- Haben kritische Repositories Owner, Reviewpflicht und angemessene Prüfungen?
- Werden sicherheitsrelevante Codeänderungen vor Merge oder Release reviewed?
- Werden Toolfindings triagiert und risikobasiert behandelt?
- Sinkt die Wiederholung bekannter Fehlerklassen?
- Werden Secrets und verwundbare Abhängigkeiten schnell behandelt?
- Werden externe und KI-unterstützte Codeanteile kontrolliert eingebunden?

Mögliche Kennzahlen:

- Anteil kritischer Repositories mit aktiven Prüfungen,
- offene kritische Code- oder Dependency-Findings,
- mittlere Behebungszeit je Kritikalität,
- False-Positive-Quote relevanter Tools,
- wiederkehrende Fehlerklassen pro Team,
- Findings ohne Owner oder Frist,
- blockierte Releases wegen kritischer Coding-Findings.

## BSIG-/NIS2-Anschluss

Sichere Programmierung ist anschlussfähig an NIS2-orientierte Themen wie sichere Entwicklung, Schwachstellenbehandlung, Cyberhygiene, Risikomanagement, Lieferkettensicherheit und Schutz digitaler Dienste. Der konkrete Bezug sollte über Anforderungsregister, Entwicklungsprozesse und Risikoentscheidungen organisationsspezifisch geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung, Datenschutzprüfung oder Sicherheitsgarantie.

## Grenzen

- Dieses Artefakt ist kein vollständiges Secure-Coding-Handbuch für alle Programmiersprachen.
- Es ersetzt keine Codeprüfung, Sicherheitstests oder Architekturprüfung im Einzelfall.
- Es garantiert keine fehlerfreie oder sichere Software.
- Es enthält keine ISO-27002-Texte und keine vertraulichen Codebeispiele.
- Es trifft keine Rechts-, Lizenz- oder Datenschutzbewertung zu konkretem Code.

## Handoffs

- **SDLC-Handoff:** Coding-Standards müssen in Entwicklungsprozess, Definition of Done und Releasegates eingebunden werden.
- **Architektur-Handoff:** wiederkehrende Codefehler, die aus Design oder Plattformgrenzen entstehen.
- **Sicherheitstest-Handoff:** kritische Codebereiche, Authentisierung, Berechtigungen, Eingaben oder Schnittstellen brauchen gezielte Tests.
- **Incident-Handoff:** Secret-Leak, aktive Ausnutzung, Kompromittierungsverdacht oder kritisches verwundbares Dependency.
- **Lieferanten-Handoff:** externe Entwicklung, fremde Repositories, nicht prüfbare Komponenten oder fehlende Scan-Nachweise.
- **Datenschutz-/Legal-Handoff:** Code betrifft personenbezogene Protokollierung, Tracking, Datenexporte, Lizenzen oder vertragliche Zusagen.
- **Management-Handoff:** Tooling, Ressourcen, wiederkehrende kritische Schulden oder akzeptierte Release-Risiken.

## Typische Fehler

- Secure Coding wird als einmalige Schulung statt als Review- und Verbesserungsroutine behandelt.
- Tools werden eingeführt, aber Findings werden nicht verantwortet.
- Code Reviews prüfen Stil, aber nicht Sicherheitslogik.
- Secrets werden entfernt, aber nicht rotiert.
- Dependency-Updates werden ohne Test- und Betriebsabstimmung eingespielt oder dauerhaft verschoben.
- Externe Entwicklung liefert Code ohne gemeinsame Mindeststandards.
- KI-Code wird übernommen, weil er plausibel aussieht, aber nicht geprüft wurde.

## Fiktives Mini-Beispiel

Ein fiktives Entwicklungsteam betreut eine API für Partnerzugriffe. In einem Merge Request erkennt der Secret-Scan einen versehentlich eingecheckten Test-Token. Der Merge wird gestoppt, der Token rotiert, das Repository geprüft und ein Ticket zur Verbesserung der lokalen Entwicklerumgebung erstellt. Zusätzlich ergänzt der Tech Lead die Team-Checkliste um API-Token und Logging sensibler Werte. Im nächsten Review wird geprüft, ob ähnliche Findings erneut auftreten.

Evidenz:

- Merge-Request mit blockiertem Secret-Finding,
- Rotationsnachweis für den Token,
- Ticket zur Umgebungsverbesserung,
- aktualisierte Coding-Checkliste,
- Reviewnotiz zu Wiederholungsprüfung.
