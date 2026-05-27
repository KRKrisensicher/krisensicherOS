
# A.8.26 — Sicherheitsanforderungen an Anwendungen

## Zweck

Sicherheitsanforderungen an Anwendungen sorgen dafür, dass Anwendungen nicht nur fachlich funktionieren, sondern auch angemessen mit Identitäten, Daten, Schnittstellen, Fehlern, Protokollierung, Verfügbarkeit und Missbrauchsszenarien umgehen.

Der Kern ist eine frühe, prüfbare Anforderungsroutine: Welche Sicherheitsbedarfe ergeben sich aus Nutzung, Daten, Exposition und Geschäftsprozess — und wie werden sie in Spezifikation, Backlog, Abnahme und Betrieb nachgehalten?

## Control-Ziel in Repo-Sprache

Die Organisation definiert, priorisiert und prüft Sicherheitsanforderungen für Anwendungen risikobasiert. Anforderungen sind so formuliert, dass Product Owner, Entwicklung, Architektur, Test und Betrieb sie verstehen, umsetzen, abnehmen und bei Änderungen erneut bewerten können.

## Typische Risiken

- Wenn Sicherheitsanforderungen nicht früh festgelegt werden, entscheidet das Entwicklungsteam implizit über Schutzbedarf und Risiko.
- Wenn Anforderungen zu generisch sind, entstehen Funktionen ohne prüfbare Akzeptanzkriterien.
- Wenn Authentisierung, Autorisierung, Session-Handling oder Protokollierung unklar bleiben, können unbefugte Zugriffe oder fehlende Nachvollziehbarkeit entstehen.
- Wenn Schnittstellen, Datenflüsse und Fehlerfälle nicht betrachtet werden, entstehen Datenabflüsse, Manipulationsmöglichkeiten oder instabile Services.
- Wenn gesetzliche, vertragliche oder Kundenerwartungen ungeprüft in technische Anforderungen übersetzt werden, entstehen falsche Zusagen oder Lücken.
- Wenn Anforderungen nach Änderungen nicht aktualisiert werden, veralten Sicherheitsannahmen.

## Trigger

- neue Anwendung, neues Modul, neue Schnittstelle oder wesentliche Funktionsänderung.
- Verarbeitung neuer Datenklassen, neuer Mandanten, neuer Nutzerrollen oder externer Zugriffe.
- Änderung von Architektur, Plattform, Authentisierung, Berechtigungsmodell oder Logging.
- neues Risiko, Schwachstelle, Incident, Auditfinding oder Kundenanforderung.
- Ausschreibung, Beschaffung oder Anpassung einer Standardsoftware oder SaaS-Anwendung.
- Releaseplanung, Abnahmeentscheidung oder Übergabe in den Betrieb.
- regelmäßiger Review kritischer Anwendungen und ihrer Sicherheitsanforderungen.

## Rollen und Verantwortung

- **Product Owner / Fachbereich:** beschreibt Geschäftsprozess, Schutzbedarf, Nutzerrollen, Missbrauchsauswirkungen und Akzeptanzkriterien.
- **Entwicklungsteam:** übersetzt Anforderungen in technische Umsetzung und macht Umsetzbarkeit sichtbar.
- **Architekturrolle:** prüft Datenflüsse, Schnittstellen, Vertrauensgrenzen und technische Abhängigkeiten.
- **Security-Rolle / AppSec-Rolle:** unterstützt bei Sicherheitsanforderungen, Bedrohungsszenarien, Priorisierung und Testbarkeit.
- **Test-/QA-Rolle:** führt Sicherheitsanforderungen in Testfällen, Abnahmekriterien und Findings nach.
- **IT-Betrieb / Plattformteam:** benennt Betriebsanforderungen wie Monitoring, Logging, Backup, Patchfähigkeit und Konfiguration.
- **Datenschutz / Legal:** prüft personenbezogene Daten, Vertragszusagen, Aufbewahrung, Protokollierung und regulatorische Fragen.
- **Management:** entscheidet bei Zielkonflikten zwischen Funktionsumfang, Termin, Kosten und Sicherheitsrisiko.

## Implementierung

### Minimalstart

Ziel: Kritische Sicherheitsanforderungen werden vor Umsetzung und Release sichtbar.

1. Für jede relevante Anwendung werden Owner, Nutzergruppen, Datenklassen und Exposition beschrieben.
2. Ein kurzer Anforderungskatalog wird verwendet: Zugriff, Rollen/Rechte, Datenfluss, Eingaben, Fehlerfälle, Logging, Verfügbarkeit, Schnittstellen, Betriebsübergabe.
3. Sicherheitsanforderungen werden als Tickets, Akzeptanzkriterien oder Abnahmepunkte erfasst.
4. Anforderungen mit Datenschutz-, Vertrags- oder Risikoauswirkung erhalten einen Human-Review-Handoff.
5. Vor Release wird geprüft, welche Anforderungen erfüllt, offen, kompensiert oder akzeptiert sind.

Minimaler Nachweis:

- Anwendungsscope mit Owner,
- Sicherheitsanforderungen im Backlog oder in der Spezifikation,
- Akzeptanzkriterien oder Testfälle,
- Reviewnotiz zu offenen Anforderungen,
- Entscheidung bei Abweichung oder Restrisiko.

### Solide Praxis

Ziel: Sicherheitsanforderungen werden risikobasiert, wiederholbar und testbar gesteuert.

1. Anwendungen werden nach Kritikalität, Daten, Exposition und Geschäftsprozess priorisiert.
2. Standardanforderungen werden für typische Themen gepflegt: Identität, Berechtigung, Eingabevalidierung, Kryptografie, Logging, Schnittstellen, Fehlertoleranz, Mandantentrennung, Secrets, Betrieb.
3. Für kritische Anwendungen werden Missbrauchsfälle oder Bedrohungsszenarien in Anforderungen übersetzt.
4. Anforderungen enthalten Akzeptanzkriterien, Testweg und verantwortliche Rolle.
5. Änderungen an Daten, Rollen, Schnittstellen oder Plattform lösen einen Anforderungsreview aus.
6. Offene Anforderungen werden im Risikoregister, Maßnahmenlog oder technischen Schulden-Backlog verfolgt.
7. Beschaffte Anwendungen und SaaS werden über Sicherheitsanforderungen, Lieferantennachweise und Abnahme eingebunden.

Starke Evidenz:

- Anwendungskritikalität und Schutzbedarfsnotiz,
- risikobasierter Sicherheitsanforderungskatalog,
- Tickets mit Akzeptanzkriterien,
- Test- und Abnahmeprotokolle,
- Änderungsreview bei relevanten Releases,
- Ausnahme- oder Risikoentscheidung,
- Lieferantenantworten oder Abnahmen für Drittanwendungen.

### Fortgeschritten

Ziel: Sicherheitsanforderungen werden als lebender Bestandteil von Produktsteuerung, Architektur und Betrieb genutzt.

1. Anforderungsbausteine sind in Templates, Definition of Ready/Done, Architekturentscheidungen und Testmanagement integriert.
2. Bedrohungsmodellierung, Datenschutzprüfung und Betriebsanforderungen werden für kritische Anwendungen koordiniert, ohne Verantwortlichkeiten zu vermischen.
3. Automatisierte Tests und Pipeline-Gates prüfen ausgewählte Anforderungen kontinuierlich.
4. Produktmetriken zeigen offene Sicherheitsanforderungen, Ausnahmequoten, wiederkehrende Anforderungsfehler und Releaseblocker.
5. Anforderungen werden bei Incidents, Schwachstellen, Kundenfeedback und Plattformänderungen aktualisiert.
6. Management erhält entscheidungsfähige Sicht auf Risiken, nicht nur Erfüllungsquoten.

## Ablauf als Routine

1. **Anwendungsbedarf entsteht:** neues Produkt, Änderung, Beschaffung oder Release.
2. **Kontext erfassen:** Nutzer, Daten, Schnittstellen, Exposition, Kritikalität und Betriebsmodell beschreiben.
3. **Sicherheitsanforderungen ableiten:** Standardanforderungen auswählen und risikospezifische Anforderungen ergänzen.
4. **Testbarkeit klären:** Akzeptanzkriterien, Testfälle und Abnahmepunkte festlegen.
5. **Umsetzung planen:** Anforderungen in Backlog, Spezifikation oder Lieferantenanforderung aufnehmen.
6. **Review durchführen:** Security, Architektur, Datenschutz/Legal oder Betrieb einbeziehen, wenn Trigger greifen.
7. **Abnahme entscheiden:** erfüllte, offene, kompensierte und akzeptierte Anforderungen dokumentieren.
8. **Betrieb beobachten:** Incidents, Findings und Änderungen in Anforderungen zurückführen.
9. **Verbessern:** Anforderungskatalog, Templates und Testfälle anpassen.

## Entscheidungen

- Welche Anwendungen brauchen vollständige Sicherheitsanforderungen, welche nur Minimalanforderungen?
- Welche Anforderungen sind Releaseblocker?
- Wer entscheidet, wenn eine Anforderung technisch oder wirtschaftlich nicht umgesetzt wird?
- Welche Anforderungen gehören in Verträge oder Lieferantenabnahmen?
- Welche Anforderungen erfordern Datenschutz-, Rechts- oder Managementprüfung?
- Wie werden Sicherheitsanforderungen gegenüber Funktions-, Termin- und Budgetdruck priorisiert?

## Evidenz

### Starke Evidenz

- Anwendungsliste mit Owner, Kritikalität und Datenklassen,
- Sicherheitsanforderungen mit Akzeptanzkriterien,
- Risiko- oder Bedrohungsszenarien als Begründung,
- Review- und Abnahmeprotokolle,
- Testnachweise zu Sicherheitsanforderungen,
- dokumentierte Abweichungen mit Frist und Entscheidung,
- aktualisierte Anforderungen nach Änderung oder Incident.

### Schwache Evidenz

- pauschale Aussage „Anwendung muss sicher sein“,
- generischer Katalog ohne Bezug zur Anwendung,
- Spezifikation ohne Sicherheitsakzeptanzkriterien,
- Testprotokoll ohne Verbindung zu Anforderungen,
- Lieferantenaussage ohne Prüffrage, Nachweis oder Abnahmeentscheidung.

### Evidenzlücken

- keine Owner für Anwendungen oder Anforderungen,
- keine Zuordnung zwischen Datenklasse und Sicherheitsanforderung,
- offene Sicherheitsanforderungen ohne Releaseentscheidung,
- Schnittstellen und Rollenmodell nicht beschrieben,
- Anforderungen veralten nach Architektur- oder Prozessänderungen.

## Wirksamkeitsprüfung

Prüffragen:

- Sind Sicherheitsanforderungen vor Umsetzung und nicht erst bei Abnahme sichtbar?
- Sind Anforderungen testbar formuliert und einem Owner zugeordnet?
- Werden Datenklasse, Exposition, Nutzerrollen und Schnittstellen berücksichtigt?
- Können offene Anforderungen einer Entscheidung oder Maßnahme zugeordnet werden?
- Werden Anforderungen nach Incidents, Schwachstellen und Änderungen aktualisiert?
- Werden Drittanwendungen und SaaS in die Anforderungsroutine einbezogen?

Mögliche Kennzahlen:

- Anteil kritischer Anwendungen mit aktuellen Sicherheitsanforderungen,
- offene Sicherheitsanforderungen pro Release,
- Anforderungen ohne Akzeptanzkriterium,
- Ausnahmen und überfällige Wiedervorlagen,
- wiederkehrende Findings aus fehlenden Anforderungen,
- Drittanwendungen mit dokumentierter Sicherheitsabnahme.

## BSIG-/NIS2-Anschluss

Sicherheitsanforderungen an Anwendungen sind anschlussfähig an NIS2-orientierte Themen wie Risikomanagement, sichere Entwicklung, sichere Beschaffung, Schwachstellenmanagement, Cyberhygiene und Schutz digitaler Dienste. Der konkrete Bezug sollte organisationsspezifisch über Anforderungsregister, Risikoanalyse und Human Review geprüft werden.

Dieses Artefakt ist keine Rechtsberatung und bestätigt keine gesetzliche Anwendbarkeit oder Konformität.

## Grenzen

- Dieses Artefakt ist kein vollständiger technischer Anforderungskatalog.
- Es ersetzt keine Datenschutz-Folgenabschätzung, Rechtsprüfung oder Vertragsprüfung.
- Es garantiert keine sichere Anwendung und keine Zertifizierungsfähigkeit.
- Es enthält keine ISO-27002-Texte und keine vertraulichen Kundenvorgaben.
- Es ersetzt keine Sicherheitstests, Code Reviews oder Architekturprüfungen.

## Handoffs

- **Architektur-Handoff:** neue Schnittstellen, Vertrauensgrenzen, Mandantentrennung, Plattformwechsel oder kritische Datenflüsse.
- **Datenschutz-/Legal-Handoff:** personenbezogene Daten, Protokollierung, Aufbewahrung, Vertragszusagen, internationale Nutzung oder Kundenanforderungen.
- **Test-Handoff:** Anforderungen brauchen konkrete Testfälle, Abnahmekriterien oder Penetrationstest-Scope.
- **Betriebs-Handoff:** Logging, Monitoring, Backup, Patchfähigkeit, Konfiguration und Supportmodell.
- **Lieferanten-Handoff:** Standardsoftware, SaaS, externe Entwicklung oder fehlende Nachweise.
- **Management-Handoff:** Releaseblocker, Termin-/Sicherheitskonflikte, akzeptiertes Restrisiko oder Ressourcenbedarf.

## Typische Fehler

- Sicherheitsanforderungen werden erst aus Testfindings abgeleitet.
- Anforderungen bleiben abstrakt und sind nicht testbar.
- Der Fachbereich beschreibt Funktionen, aber keine Missbrauchs- oder Schadensszenarien.
- Drittanwendungen werden eingeführt, ohne Sicherheitsanforderungen zu formulieren.
- Datenschutz-, Betriebs- und Sicherheitsanforderungen werden zu spät zusammengeführt.
- Offene Anforderungen verschwinden im Backlog ohne Risikoentscheidung.
- Anforderungen werden nach Änderungen nicht reviewed.

## Fiktives Mini-Beispiel

Ein fiktives Unternehmen plant eine Self-Service-Anwendung für Geschäftskunden. Beim Anforderungsworkshop werden Nutzerrollen, Mandantentrennung, Passwort-Reset, Protokollierung sicherheitsrelevanter Aktionen und API-Zugriffe als Sicherheitsanforderungen erfasst. QA ergänzt Testfälle, Architektur prüft die Datenflüsse, Datenschutz bewertet die Protokollierung. Vor Release bleibt ein Logging-Dashboard offen; der Product Owner dokumentiert eine befristete Maßnahme und legt die Entscheidung im Releaseprotokoll ab.

Evidenz:

- Anwendungsscope mit Datenklassen,
- Sicherheitsanforderungen mit Akzeptanzkriterien,
- Architektur- und Datenschutzreview,
- Testfälle und Testergebnisse,
- Releaseprotokoll mit offener Maßnahme.
