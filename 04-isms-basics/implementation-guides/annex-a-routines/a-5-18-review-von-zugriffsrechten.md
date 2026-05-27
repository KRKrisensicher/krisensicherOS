
# A.5.18 — Review von Zugriffsrechten

## Zweck

Zugriffsrechte verändern sich schneller als Zuständigkeiten dokumentiert werden: neue Aufgaben, Projektrollen, Vertretungen, Dienstleisterzugriffe und technische Gruppen erzeugen Rechte, die später oft nicht zurückgebaut werden. Diese Routine sorgt dafür, dass bestehende Zugriffe regelmäßig fachlich geprüft, korrigiert, entzogen oder bewusst als Ausnahme entschieden werden.

Der Review ist keine Listenübung. Er ist ein Governance-Moment: Owner bestätigen, ob Zugriffe noch benötigt werden, ob sie zum Schutzbedarf passen und ob auffällige Rechte ein Risiko oder eine Managemententscheidung auslösen.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine risikobasierte Reviewroutine für Nutzer-, Admin-, externe und technische Zugriffe. Reviews haben klaren Scope, verständliche Entscheidungskriterien, zuständige Owner, dokumentierte Ergebnisse und Nachverfolgung bis zur Umsetzung.

## Typische Risiken

- Wenn Rechte nach Rollenwechseln bestehen bleiben, entstehen überhöhte oder unvereinbare Berechtigungen.
- Wenn ehemalige Dienstleister, Projektmitglieder oder externe Konten nicht reviewed werden, bleiben unbemerkte Zugriffspfade offen.
- Wenn Owner unverständliche Gruppenlisten abnicken, entsteht Scheinreview ohne fachliche Entscheidung.
- Wenn Adminrechte wie normale Zugriffe behandelt werden, bleiben besonders wirksame Rechte zu lange aktiv.
- Wenn technische Konten und API-Zugriffe fehlen, ist der Review nur auf Menschen beschränkt.
- Wenn Review-Ergebnisse nicht umgesetzt werden, bleibt das Risiko trotz Protokoll unverändert.

## Trigger

- geplanter monatlicher, quartalsweiser, halbjährlicher oder jährlicher Berechtigungsreview.
- Eintritt, Rollenwechsel, Teamwechsel, Austritt, Projektende oder Dienstleisterende.
- neues System, neue Datenablage, neue privilegierte Rolle oder geändertes Rollenmodell.
- Sicherheitsereignis, kompromittiertes Konto, ungewöhnliche Nutzung oder Auditfinding.
- Änderung von Schutzbedarf, Geschäftsprozess, Datenklasse oder regulatorischer Betroffenheit.
- Migration, Bereinigung, Systemablösung oder Einführung eines IAM-/Rezertifizierungstools.
- Managementfrage zu kritischen Altberechtigungen, externen Zugriffen oder Trennungskonflikten.

## Rollen und Verantwortung

- **Information Owner / Asset Owner:** entscheidet, ob Zugriffe fachlich noch benötigt werden.
- **Prozess Owner / Führungskraft:** bestätigt Rollenbezug, Geschäftsbedarf und organisatorische Änderungen.
- **IT-/Plattform Owner:** erstellt Berechtigungsexporte, erklärt Gruppenlogik und setzt Entzug oder Korrektur um.
- **IAM-/Access-Owner:** definiert Reviewverfahren, Frequenzen, Kritikalitätsklassen und Rezertifizierungslogik.
- **ISMS-Owner / Security-Rolle:** prüft Risikobezug, Ausnahmebehandlung und Eskalation.
- **HR / Einkauf:** liefert Rollenwechsel-, Austritts-, Projektende- und Dienstleisterinformationen.
- **Datenschutz / Legal:** prüft personenbezogene Auswertungen, Beschäftigtenbezug und Vertragsfragen.
- **Management:** entscheidet über akzeptierte Restrisiken, Ressourcenkonflikte und nicht auflösbare Trennungskonflikte.

## Implementierung

### Minimalstart

Ziel: kritische und privilegierte Zugriffe werden regelmäßig sichtbar geprüft.

1. Die Organisation benennt die wichtigsten Systeme, Datenablagen, Adminrollen und externen Zugriffe im Scope.
2. Für jedes Reviewobjekt gibt es einen fachlichen Owner und einen technischen Ansprechpartner.
3. IT stellt verständliche Berechtigungsauszüge bereit: Person oder Konto, Rolle/Gruppe, Zweck, letzter bekannter Bezug.
4. Owner entscheiden pro auffälligem Zugriff: bestätigen, entziehen, ändern, klären oder befristet ausnehmen.
5. Entzug und Korrektur werden als Tickets nachverfolgt.
6. Offene oder strittige Punkte erhalten Frist, Eskalationsweg und Wiedervorlage.

Minimaler Nachweis:

- Reviewscope mit Systemen und Ownern,
- Berechtigungsexport zum Reviewzeitpunkt,
- Reviewprotokoll mit Entscheidungen,
- Tickets für Entzug oder Anpassung,
- Ausnahmen mit Begründung und Ablaufdatum.

### Solide Praxis

Ziel: Zugriffsreviews werden risikobasiert, verständlich und wiederholbar.

1. Zugriffstypen werden getrennt betrachtet: Standardzugriff, privilegierter Zugriff, externer Zugriff, technische Konten, Funktionskonten.
2. Reviewfrequenzen orientieren sich an Schutzbedarf, Exposition und Berechtigungsmacht.
3. Reviewlisten werden für Owner verständlich aufbereitet: sprechende Rollen, Systemzweck, Kritikalität, letzte Änderung, externe Kennzeichnung.
4. HR-, Projekt- und Lieferantenereignisse werden mit dem Review abgeglichen.
5. Rezertifizierungsergebnisse führen zu messbaren Aktionen: Entzug, Rollenbereinigung, Ausnahme, Risikoentscheidung oder Prozessverbesserung.
6. Wiederkehrende Auffälligkeiten werden in Rollenmodell, Joiner-/Mover-/Leaver-Prozess oder Schulung zurückgespielt.
7. Kritische überfällige Reviews gehen ins ISMS- oder Management Review.

Starke Evidenz:

- risikobasierter Reviewplan,
- aktuelle Owner-Matrix,
- verständlich aufbereitete Reviewlisten,
- Entscheidungen je Zugriff oder Zugriffsgruppe,
- Umsetzungsnachweise für Entzug und Korrektur,
- Ausnahme- und Eskalationslog.

### Fortgeschritten

Ziel: Reviews werden mit Identitätsdaten, Risikoindikatoren und Managementsteuerung integriert.

1. IAM, HR-Quelle, Systemgruppen, Servicekonten und Ticketing sind verbunden.
2. Hochrisiko-Zugriffe werden häufiger oder ereignisbasiert rezertifiziert.
3. Segregation-of-Duties-Konflikte, ungewöhnliche Kombinationen, verwaiste Konten und externe Altzugriffe werden automatisch markiert.
4. Reviews erzeugen strukturierte Aufgaben und Nachweise im Ticket- oder GRC-System.
5. Kennzahlen zeigen überfällige Reviews, Entzugsdauer, Ausnahmequote, nicht zuordenbare Konten und wiederkehrende Rollenprobleme.
6. Management erhält nicht nur Listenstatus, sondern entscheidungsfähige Restrisiken und Ressourcenbedarfe.

## Ablauf als Routine

1. **Review auslösen:** Turnus, Ereignis, Incident, Auditfinding oder Managementfrage.
2. **Scope festlegen:** Systeme, Datenablagen, Rollen, externe Konten, Adminrechte und technische Konten bestimmen.
3. **Daten aufbereiten:** Berechtigungen exportieren, Owner zuordnen, unklare Gruppen übersetzen und Auffälligkeiten markieren.
4. **Fachlich prüfen:** Owner bewerten Geschäftsbedarf, Rollenbezug, Schutzbedarf und Trennungskonflikte.
5. **Entscheiden:** bestätigen, entziehen, reduzieren, befristen, eskalieren oder weiter klären.
6. **Technisch umsetzen:** IT/IAM ändert Rechte und dokumentiert Umsetzung.
7. **Nachverfolgen:** offene Punkte, Ausnahmen und überfällige Entscheidungen mit Frist führen.
8. **Wirksamkeit prüfen:** Stichprobe, Re-Export oder Validierung, ob beschlossene Änderungen umgesetzt wurden.
9. **Verbessern:** Rollenmodell, On-/Offboarding, Lieferantenprozess oder Systemgruppen anpassen.

## Entscheidungen

- Welche Systeme, Rollen und Zugriffstypen werden zuerst reviewed?
- Wie häufig werden Standard-, Admin-, externe und technische Zugriffe geprüft?
- Welche Kriterien machen einen Zugriff auffällig oder kritisch?
- Wer darf Zugriffe bestätigen und wer darf Ausnahmen akzeptieren?
- Wann wird fehlende Owner-Rückmeldung eskaliert?
- Welche Trennungskonflikte sind nicht akzeptabel und welche brauchen Managemententscheidung?
- Wie wird sichergestellt, dass Review-Ergebnisse tatsächlich umgesetzt werden?

## Evidenz

### Starke Evidenz

- Reviewplan mit risikobasierter Frequenz,
- System-/Assetscope mit Ownern,
- Berechtigungsexport oder Rezertifizierungsdatensatz zum Reviewzeitpunkt,
- fachliche Entscheidungen mit Datum und verantwortlicher Rolle,
- Entzugs-, Änderungs- oder Bereinigungstickets,
- Validierung nach Umsetzung,
- befristete Ausnahmen mit Risikoentscheidung,
- Managemententscheidung bei dauerhaften Konflikten.

### Schwache Evidenz

- unterschriebene Liste ohne erkennbare Einzelentscheidung,
- Screenshot von Gruppen ohne Owner, Datum oder Scope,
- Reviewmail ohne Nachverfolgung der Änderungen,
- pauschale Bestätigung „alles ok“ durch IT statt fachlicher Owner-Prüfung,
- IAM-Toolstatus ohne Nachweis, dass offene Findings bearbeitet wurden.

### Evidenzlücken

- keine Owner für kritische Systeme oder Datenablagen,
- Adminrechte, Servicekonten oder externe Konten außerhalb des Reviews,
- Review-Ergebnisse ohne Umsetzungstickets,
- dauerhaft offene Klärfälle ohne Eskalation,
- Rollenwechsel und Austritte nicht mit Reviewdaten abgeglichen,
- Ausnahmen ohne Frist oder Risikoakzeptanz.

## Wirksamkeitsprüfung

Prüffragen:

- Werden die kritischsten Zugriffe häufiger und tiefer reviewed als Standardrechte?
- Können Owner die Reviewlisten fachlich verstehen und entscheiden?
- Führen Reviews zu tatsächlichem Entzug, Reduktion oder Rollenbereinigung?
- Sind externe, privilegierte und technische Zugriffe sichtbar enthalten?
- Werden überfällige Reviews und offene Klärfälle eskaliert?
- Gibt es Validierung, dass beschlossene Änderungen umgesetzt wurden?
- Werden wiederkehrende Auffälligkeiten in den Zugriffsprozess zurückgespielt?

Mögliche Kennzahlen:

- Anteil kritischer Systeme mit aktuellem Review,
- überfällige Reviews nach Kritikalität,
- Anzahl entzogener oder reduzierter Zugriffe,
- offene Klärfälle älter als definierte Frist,
- Entzugsdauer nach Reviewentscheidung,
- Ausnahmequote und überfällige Ausnahmen,
- nicht zuordenbare Konten.

## BSIG-/NIS2-Anschluss

Reviews von Zugriffsrechten sind anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Cyberhygiene, Zugriffsschutz, Governance, Incident-Prävention und Nachvollziehbarkeit sicherheitsrelevanter Entscheidungen.

Für BSIG-/NIS2-Betroffenheit sollte die Organisation im Anforderungsregister prüfen, welche Systeme, Rollen, Reviewfrequenzen und Nachweise relevant sind. Dieses Artefakt ersetzt keine rechtliche Auslegung und keine verbindliche Prüfung der Anwendbarkeit.

## Grenzen

- Dieses Artefakt ersetzt kein vollständiges Identity-&-Access-Management-Konzept.
- Es ist keine Datenschutzbewertung für Beschäftigtenauswertungen oder Protokolldaten.
- Ein Reviewprotokoll ersetzt nicht die technische Umsetzung beschlossener Änderungen.
- Keine Rechtsberatung, keine Datenschutzberatung, keine Zertifizierungszusage.
- Keine ISO-27002-Texte und keine echten Personen-, Kunden- oder Systemdaten in Beispielen.

## Handoffs

- **IAM-/IT-Handoff:** Berechtigungsexporte, Gruppenlogik, Entzug, Rollenmodell und technische Validierung.
- **HR-Handoff:** Eintritt, Austritt, Rollenwechsel, Organisationsänderungen und längere Abwesenheiten.
- **Einkauf-/Lieferanten-Handoff:** externe Konten, Projektende, Vertragsende oder geänderter Dienstleisterscope.
- **Datenschutz-/Legal-Handoff:** personenbezogene Auswertungen, Beschäftigtenbezug, Protokolldaten oder Vertragsfragen.
- **Incident-Handoff:** verdächtige Rechte, kompromittierte Konten oder unberechtigte Nutzung.
- **Management-Handoff:** dauerhafte Ausnahmen, Trennungskonflikte, Ressourcenmangel oder akzeptierte Restrisiken.
- **Audit-/Evidence-Handoff:** fehlende Reviewnachweise, unklare Entscheidungen oder nicht validierte Umsetzung.

## Typische Fehler

- Reviewlisten sind so technisch, dass Fachbereiche sie nicht sinnvoll bewerten können.
- Owner bestätigen alle Rechte aus Zeitdruck pauschal.
- Admin-, externe und technische Konten werden nicht separat geprüft.
- Entscheidungen werden dokumentiert, aber Entzug oder Änderung wird nicht nachverfolgt.
- Reviews finden jährlich statt, obwohl kritische Zugriffe häufigere Prüfung brauchen.
- Ausnahmen erhalten kein Ablaufdatum.
- Das IAM-Tool wird als Kontrolle verstanden, obwohl Owner-Entscheidungen fehlen.

## Fiktives Mini-Beispiel

Ein fiktiver Produktionsbetrieb führt einen quartalsweisen Review der ERP-Adminrechte durch. Der IT-Owner liefert eine Liste mit Admin- und Supportrollen. Der Fachowner erkennt zwei ehemalige Projektrollen, die nicht mehr benötigt werden. IT entzieht die Rechte und bestätigt dies per Re-Export. Ein externer Supportzugang bleibt befristet aktiv, weil ein Updatefenster ansteht; die Ausnahme erhält Ablaufdatum und Wiedervorlage im nächsten Review.

Evidenz:

- ERP-Reviewscope mit Owner,
- Berechtigungsexport zum Stichtag,
- Entscheidungen des Fachowners,
- Entzugsticket und Re-Export,
- befristete Ausnahme für externen Supportzugang.
