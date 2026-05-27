
# A.5.35 — Unabhängige Überprüfung der Informationssicherheit

## Zweck

Diese Routine sorgt dafür, dass Informationssicherheit nicht nur von denjenigen bewertet wird, die sie betreiben. Unabhängige Überprüfung schafft Abstand, prüft blinde Flecken, macht Abweichungen sichtbar und gibt Management und Ownern belastbare Entscheidungsgrundlagen.

Der Kern ist nicht ein Audit um des Audits willen, sondern eine wiederholbare Reviewlogik: Was wird unabhängig geprüft, durch wen, mit welchem Scope, welcher Evidenz, welchen Findings und welchem Management-Handoff?

## Control-Ziel in Repo-Sprache

Die Organisation plant und betreibt unabhängige Prüfungen der Informationssicherheit risikobasiert. Prüfende Rollen sind ausreichend unabhängig vom geprüften Betrieb, Ergebnisse werden nachvollziehbar dokumentiert, Findings werden priorisiert und Maßnahmen bis zur Wirksamkeitsprüfung verfolgt.

## Typische Risiken

- Wenn Teams ihre eigene Sicherheitswirksamkeit allein bewerten, bleiben blinde Flecken, Zielkonflikte und Gewöhnungseffekte unentdeckt.
- Wenn Prüfungen nur dokumentenorientiert sind, wird die tatsächliche Betriebsroutine nicht sichtbar.
- Wenn Findings nicht priorisiert und nachverfolgt werden, entsteht Audit-Theater ohne Risikoreduktion.
- Wenn Prüfende zu nah an Umsetzung oder Interessenlage sind, können kritische Abweichungen abgeschwächt werden.
- Wenn Management nur Ergebnisnoten statt Entscheidungsbedarf erhält, bleiben Ressourcen- und Restrisikofragen ungelöst.
- Wenn externe Prüfungen nicht vorbereitet oder ausgewertet werden, gehen Lern- und Verbesserungsmöglichkeiten verloren.

## Trigger

- jährliche oder risikobasierte Prüfplanung.
- wesentliche Änderung von Organisation, Architektur, Dienstleister, Systemen oder Bedrohungslage.
- Sicherheitsereignis, Beinahevorfall, Schwachstelle oder Krisenübung mit strukturellem Finding.
- Managementfrage zu Wirksamkeit, Reife, Ressourcen oder Restrisiko.
- neue regulatorische, vertragliche oder Kundenanforderung.
- Abschluss wichtiger Maßnahmen, Programme oder Migrationen.
- wiederholte Abweichungen, überfällige Findings oder hohe Ausnahmequote.

## Rollen und Verantwortung

- **Management / Leitung:** beauftragt unabhängige Reviews, schützt Unabhängigkeit und entscheidet über Ressourcen, Restrisiken und Prioritäten.
- **ISMS-Owner:** koordiniert Prüfplan, Scope, Evidenzbereitstellung und Maßnahmenverfolgung, ohne eigene Verantwortung wegzudelegieren.
- **Unabhängige Reviewer / interne Prüfung / externe Prüfer:** prüfen Scope, Durchführung, Evidenz und Wirksamkeit mit ausreichender Distanz.
- **Control Owner / Prozess Owner:** erklären Betrieb, liefern Evidenz, bewerten Findings und setzen Maßnahmen um.
- **Risk Owner:** ordnet Findings in Risiken, Akzeptanzen und Priorisierung ein.
- **Legal / Datenschutz:** prüfen, wenn Reviewdaten, Verträge, personenbezogene Informationen oder Berichtsempfänger betroffen sind.
- **Audit-/Evidence-Rolle:** unterstützt Nachweisqualität, Quellen, Versionen und Nachverfolgbarkeit.

## Implementierung

### Minimalstart

Ziel: Erste unabhängige Sicht auf kritische Sicherheitsbereiche schaffen.

1. Management und ISMS-Owner benennen kritische Prüfbereiche: Zugriff, Incident Response, Schwachstellen, Lieferanten, Backup, Awareness oder Datenschutz-Handoffs.
2. Für jeden Bereich werden Prüffrage, Scope, Reviewer und Zeitraum festgelegt.
3. Reviewer dürfen nicht allein die Umsetzung prüfen, die sie selbst verantworten.
4. Prüfung betrachtet mindestens Dokumentation, Stichprobe aus dem Betrieb und offene Ausnahmen.
5. Findings werden mit Owner, Risiko, Priorität, Maßnahme und Frist dokumentiert.
6. Kritische Findings oder ungeklärte Zielkonflikte gehen ins Management Review.

Minimaler Nachweis:

- Reviewauftrag mit Scope und Reviewer,
- Evidenzliste oder Stichprobenplan,
- Prüfnotiz mit Findings,
- Maßnahmenlog mit Owner und Frist,
- Managemententscheidung bei kritischen Findings.

### Solide Praxis

Ziel: Unabhängige Reviews werden risikobasiert geplant und nachverfolgt.

1. Ein Prüfplan priorisiert Controls, Prozesse, Standorte, Systeme und Dienstleister nach Risiko und Veränderung.
2. Unabhängigkeit wird je Review festgelegt: anderes Team, interne Prüfung, externer Spezialist oder Peer Review.
3. Prüfmethoden kombinieren Interview, Dokumentensichtung, Stichprobe, technische Nachweise und Walkthrough.
4. Findings werden nach Auswirkung, Ursache, betroffenen Assets und Entscheidungsbedarf klassifiziert.
5. Maßnahmen werden bis zur Umsetzung und Wirksamkeitsprüfung verfolgt.
6. Wiederholungsfindings und systemische Ursachen werden gesondert an Management berichtet.
7. Lessons Learned verbessern Controls, Schulung, Architektur, Lieferantensteuerung oder Evidence Design.

Starke Evidenz:

- risikobasierter Prüfplan,
- Unabhängigkeits- und Scope-Begründung,
- Stichproben- und Reviewprotokolle,
- Findings mit Ursache, Risiko und Owner,
- Maßnahmenstatus und Validierungsnachweise,
- Management Review zu kritischen oder wiederholten Findings.

### Fortgeschritten

Ziel: Unabhängige Überprüfung ist Teil des Steuerungs- und Verbesserungszyklus.

1. Prüfplanung nutzt Risikoregister, Incident-Trends, Schwachstellenlage, Lieferantenrisiken und Managementprioritäten.
2. Reviews werden mit interner Revision, technischen Tests, Tabletop-Übungen, Architekturreviews und Evidence-Pack-Reviews abgestimmt.
3. Prüfende Rollen haben klare Mandate, Zugang zu relevanter Evidenz und Eskalationswege.
4. Finding-Daten zeigen Muster: Root Causes, Control-Schwächen, Wiederholung, überfällige Maßnahmen und Ressourcenkonflikte.
5. Maßnahmenvalidierung prüft nicht nur Abschluss, sondern tatsächliche Wirksamkeit.
6. Management erhält entscheidungsfähige Berichte mit Restrisiken, Optionen und Human-Gates.

## Ablauf als Routine

1. **Reviewbedarf erkennen:** Turnus, Risikoänderung, Vorfall, Managementfrage, Auditfinding oder abgeschlossene Maßnahme.
2. **Scope und Unabhängigkeit festlegen:** Was wird geprüft, wer prüft, welche Interessenkonflikte sind zu vermeiden?
3. **Prüfansatz planen:** Prüffragen, Stichproben, Evidenzquellen, Interviews und technische Nachweise definieren.
4. **Durchführen:** Betrieb nachvollziehen, Nachweise prüfen, Abweichungen und gute Praxis erfassen.
5. **Findings bewerten:** Ursache, Risiko, Auswirkung, Owner, Priorität und Entscheidungsbedarf festlegen.
6. **Maßnahmen vereinbaren:** Korrektur, Risikobehandlung, Ausnahme, Akzeptanz oder Managemententscheidung dokumentieren.
7. **Nachverfolgen:** Fristen, Status, Hindernisse und Eskalationen steuern.
8. **Wirksamkeit validieren:** Stichprobe, Test, Re-Review oder Nachweis prüfen.
9. **Lernen:** Ergebnisse in Prüfplan, Controls, Schulung und Management Review zurückspielen.

## Entscheidungen

- Welche Sicherheitsbereiche brauchen unabhängige Prüfung und wie häufig?
- Welche Form von Unabhängigkeit ist für den jeweiligen Scope ausreichend?
- Welche Findings sind operativ lösbar, welche benötigen Managemententscheidung?
- Wann braucht es externe Spezialisten oder interne Revision?
- Welche Evidenz reicht, um Wirksamkeit einer Maßnahme zu bestätigen?
- Wie wird mit Interessenkonflikten, Berichtsdruck oder strittigen Findings umgegangen?

## Evidenz

### Starke Evidenz

- genehmigter Prüfplan mit Risikobezug,
- Reviewauftrag mit Scope, Methode und Reviewer,
- Nachweis der Unabhängigkeitsbetrachtung,
- Stichprobenliste und geprüfte Evidenzquellen,
- Finding-Register mit Ursache, Risiko, Owner und Frist,
- Validierungsnachweis nach Maßnahmenabschluss,
- Managemententscheidung zu kritischen Findings, Ausnahmen oder Ressourcen.

### Schwache Evidenz

- allgemeine Auditplanung ohne Risikobezug,
- Selbstauskunft des geprüften Teams ohne unabhängige Stichprobe,
- Findings ohne Owner oder Frist,
- Ampelbericht ohne Ursachen und Entscheidungsbedarf,
- geschlossene Maßnahmen ohne Wirksamkeitsnachweis,
- externe Prüfberichte ohne interne Auswertung.

### Evidenzlücken

- kein Prüfplan oder keine Priorisierung,
- Reviewer prüft ausschließlich eigene Arbeit,
- keine Stichproben oder Betriebsnachweise,
- Findings werden nicht nachverfolgt,
- Management sieht kritische Restrisiken nicht,
- Datenschutz-/Legal-Fragen zu Reviewdaten ungeklärt.

## Wirksamkeitsprüfung

Prüffragen:

- Deckt der Prüfplan die wichtigsten Risiken, Änderungen und kritischen Controls ab?
- Ist die Unabhängigkeit der Reviewer für den Scope nachvollziehbar?
- Prüfen Reviews tatsächliche Durchführung und Wirksamkeit, nicht nur Dokumente?
- Werden Findings priorisiert, mit Owner versehen und bis zur Validierung verfolgt?
- Werden wiederholte oder systemische Schwächen sichtbar gemacht?
- Erhält Management klare Entscheidungen statt bloßer Prüfberichte?

Mögliche Kennzahlen:

- Abdeckung risikokritischer Prüfbereiche,
- Anteil Findings mit Owner und Frist,
- überfällige Maßnahmen,
- wiederholte Findings,
- validierte Maßnahmenquote,
- Zeit von Finding bis Managemententscheidung,
- Anteil Reviews mit dokumentierter Unabhängigkeitsbetrachtung.

## BSIG-/NIS2-Anschluss

Unabhängige Überprüfung ist anschlussfähig an NIS2-orientierte Governance, Risikomanagement, Managementaufsicht, Wirksamkeitsprüfung, Incident-Lessons-Learned und Lieferkettensteuerung. Der konkrete Bezug sollte im Anforderungsregister, Prüfplan und Management Review organisationsspezifisch festgelegt werden.

Dieses Artefakt ersetzt keine rechtliche Auslegung, keine Zertifizierungsprüfung und keine verbindliche Bewertung regulatorischer Pflichten.

## Grenzen

- Keine Zertifizierungs-, Konformitäts- oder Sicherheitsgarantie.
- Kein Ersatz für interne Revision, externe Prüfung, Penetrationstest oder Rechtsberatung.
- Keine ISO-27002-Texte oder Normersatzformulierung.
- Keine Veröffentlichung oder externe Weitergabe von Prüfberichten ohne Freigabe.
- Keine echten Kunden-, Personen-, Sicherheits- oder Geheimdaten in öffentlichen Beispielen.

## Handoffs

- **Management-Handoff:** Prüfauftrag, kritische Findings, Ressourcenbedarf, Risikoakzeptanz, Priorisierung.
- **Interne Prüfung/Audit-Handoff:** Prüfmethodik, Stichproben, Bericht, Nachverfolgung.
- **Risk-Handoff:** Findings mit Risikoänderung, Akzeptanzbedarf oder Maßnahmenpriorisierung.
- **IT-/Security-Handoff:** technische Abweichungen, Kontrolldesign, Maßnahmenumsetzung.
- **Legal-/Datenschutz-Handoff:** personenbezogene Reviewdaten, Verträge, externe Prüfer, Berichtsempfänger, Vertraulichkeit.
- **Incident-/BCM-Handoff:** Findings aus Vorfällen, Übungen oder Krisenroutinen.
- **Evidence-Handoff:** fehlende oder schwache Nachweise, nicht prüfbare Controls.

## Typische Fehler

- Review wird mit Selbstauskunft verwechselt.
- Prüfplan folgt Kalenderlogik statt Risiko- und Veränderungslage.
- Findings werden weich formuliert, damit keine Entscheidung nötig wird.
- Maßnahmen werden geschlossen, sobald ein Dokument erstellt wurde.
- Externe Berichte werden abgelegt, aber nicht in Maßnahmen und Risiken übersetzt.
- Unabhängigkeit wird behauptet, aber Interessenkonflikte werden nicht betrachtet.
- Management bekommt Ampeln ohne konkrete Entscheidungspunkte.

## Fiktives Mini-Beispiel

Ein fiktives Unternehmen lässt nach einer Cloud-Migration die Zugriffsteuerung unabhängig prüfen. Ein Reviewer aus einem anderen Bereich erhält Scope, Stichprobenplan und Zugriff auf Freigabetickets. Die Prüfung zeigt, dass externe Adminzugriffe zwar dokumentiert, aber nicht fristgerecht reviewed werden. Der Cloud Owner erstellt eine Maßnahme, der ISMS-Owner setzt eine Wiedervorlage und Management entscheidet, für drei kritische Systeme monatliche Reviews zu priorisieren.

Evidenz:

- Reviewauftrag mit unabhängiger Reviewer-Rolle,
- Stichprobenliste,
- Finding zu externen Adminzugriffen,
- Maßnahmenticket mit Owner und Frist,
- Managemententscheidung zur Reviewfrequenz,
- Validierungsnotiz nach erstem Monatsreview.
