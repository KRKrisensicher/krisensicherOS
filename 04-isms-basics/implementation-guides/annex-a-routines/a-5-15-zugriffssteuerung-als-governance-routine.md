
# A.5.15 — Zugriffssteuerung als Governance-Routine

## Zweck

Zugriffssteuerung sorgt dafür, dass Menschen, Dienste und technische Identitäten nur die Zugriffe erhalten, die sie für legitime Aufgaben benötigen — und dass diese Zugriffe nachvollziehbar beantragt, genehmigt, geändert, geprüft und entzogen werden.

Der Kern ist nicht „Berechtigungsliste vorhanden“, sondern ein belastbarer Entscheidungs- und Reviewprozess: Wer darf worauf zugreifen, warum, wie lange, mit welcher Freigabe und mit welchem Risiko?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Routine für Zugriff auf Informationen, Anwendungen, Systeme, Räume, Schnittstellen und administrative Funktionen. Die Routine verbindet Rollen, Schutzbedarf, Geschäftsbedarf, Genehmigung, technische Umsetzung, Review und Ausnahmebehandlung.

## Typische Risiken

- Wenn ehemalige Beschäftigte, Dienstleister oder technische Konten aktiv bleiben, können Informationen unbefugt eingesehen, verändert oder gelöscht werden.
- Wenn Berechtigungen über Rollenwechsel hinweg wachsen, entstehen unbemerkte Machtkonzentrationen und Trennungskonflikte.
- Wenn Fachbereiche Zugriffe informell vergeben, fehlen Genehmigung, Nachvollziehbarkeit und Widerruf.
- Wenn privilegierte Rechte nicht getrennt betrachtet werden, kann ein einzelnes kompromittiertes Konto erheblichen Schaden verursachen.
- Wenn Zugriffskonzepte nur für zentrale Systeme existieren, bleiben Cloud-Dienste, SaaS-Tools, Datenablagen, Schnittstellen oder Servicekonten ungesteuert.

## Trigger

- Eintritt, Rollenwechsel, Teamwechsel oder Austritt.
- neues System, neue Datenablage, neuer Cloud-Dienst oder neue Schnittstelle.
- Änderung des Schutzbedarfs, neue Risikoentscheidung oder neue regulatorische Betroffenheit.
- Lieferantenwechsel, Ende eines Vertrags oder geänderter Dienstleisterzugriff.
- Sicherheitsereignis, Verdacht auf Kontokompromittierung oder Auditfeststellung.
- turnusmäßiger Berechtigungsreview.
- Einführung oder Änderung von Rollenmodellen, Gruppen, Adminrechten oder technischen Konten.

## Rollen und Verantwortung

- **Information Owner / Asset Owner:** legt fest, wer aus fachlicher Sicht Zugriff braucht und welche Einschränkungen gelten.
- **Führungskraft / Prozess Owner:** bestätigt Geschäftsbedarf und Rollenbezug.
- **IT-/Plattform Owner:** setzt Berechtigungen technisch um und liefert Auswertungen.
- **ISMS-Owner / Security-Rolle:** definiert Mindestlogik, Reviewanforderungen, Risikohandling und Eskalation.
- **HR / People-Funktion:** liefert Eintritts-, Wechsel- und Austrittsereignisse.
- **Datenschutz / Legal:** prüft personenbezogene Auswertungen, Beschäftigtendaten, Protokollierung und vertragliche Fragen.
- **Management:** entscheidet über Ausnahmen, Restrisiken, Ressourcen und Zielkonflikte.

## Implementierung

### Minimalstart

Ziel: kritische Zugriffe sichtbar und reviewfähig machen.

1. Die Organisation benennt die wichtigsten Systeme, Datenablagen und Adminzugriffe im ISMS-Scope.
2. Für jedes kritische Ziel wird ein Owner festgelegt.
3. Neue Zugriffe werden nur mit nachvollziehbarem Antrag oder Ticket vergeben.
4. Austritte und Rollenwechsel lösen eine Zugriffprüfung aus.
5. Ein einfacher quartalsweiser Review prüft mindestens privilegierte und externe Zugriffe.
6. Ausnahmen werden mit Begründung, Laufzeit und Wiedervorlage dokumentiert.

Minimaler Nachweis:

- System-/Datenablagenliste mit Owner,
- Ticket oder Freigabenachweis für Zugriff,
- Austritts-/Rollenwechselprüfung,
- Reviewprotokoll für kritische Zugriffe,
- Ausnahmeentscheidung.

### Solide Praxis

Ziel: wiederholbare Zugriffssteuerung über Rollen und Risiken.

1. Zugriffstypen werden klassifiziert: Standardzugriff, erhöhter Zugriff, privilegierter Zugriff, externer Zugriff, technisches Konto.
2. Rollenmodelle oder Berechtigungsgruppen werden beschrieben und mit Ownern verbunden.
3. Genehmigungen folgen einer klaren Logik: Fachfreigabe, technische Umsetzung, Sicherheitsprüfung bei erhöhtem Risiko.
4. Berechtigungsreviews werden risikobasiert geplant: kritische Systeme häufiger, niedriger Schutzbedarf seltener.
5. Rezertifizierungsergebnisse führen zu Entzug, Korrektur, Ausnahme oder Managemententscheidung.
6. Joiner-/Mover-/Leaver-Prozesse werden mit HR- oder Identitätsdaten verbunden.

Starke Evidenz:

- Rollen-/Gruppenkatalog,
- genehmigte Zugriffsanträge,
- technische Berechtigungsexporte,
- Reviewliste mit Entscheidungen,
- Nachweis entzogener oder korrigierter Zugriffe,
- Ausnahme- und Risikoakzeptanzlog.

### Fortgeschritten

Ziel: Zugriff als laufende Governance- und Detektionsroutine betreiben.

1. Identitätsquelle, Rollenmodell, Systemgruppen und Rezertifizierung sind integriert.
2. Kritische Rechte werden mit Segregation-of-Duties-Regeln, Risikoindikatoren oder Alerts überwacht.
3. Just-in-time- oder zeitlich begrenzte Privilegien werden für besonders kritische Tätigkeiten genutzt.
4. Servicekonten, API-Tokens und Maschinenidentitäten werden mit Owner, Zweck, Rotation und Ablaufdatum geführt.
5. Auffällige Zugriffsmuster fließen in Monitoring, Incident Triage und Risiko-Review.
6. Management erhält entscheidungsfähige Kennzahlen: überfällige Reviews, Ausnahmequote, kritische Altberechtigungen, externe Zugriffe, nicht zuordenbare Konten.

## Ablauf als Routine

1. **Zugriffsbedarf entsteht:** neue Rolle, Aufgabe, Dienstleister, Systemfunktion oder Ausnahme.
2. **Antrag erfassen:** wer, worauf, warum, wie lange, mit welchem Rollen-/Risikobezug.
3. **Fachlich entscheiden:** Owner prüft Geschäftsbedarf und Schutzbedarf.
4. **Sicherheitslogik prüfen:** erhöhte Rechte, externe Zugriffe, Trennungskonflikte oder personenbezogene Auswertungen werden gesondert betrachtet.
5. **Technisch umsetzen:** IT setzt Berechtigung gemäß Freigabe um.
6. **Nachweis ablegen:** Antrag, Entscheidung und Umsetzung bleiben nachvollziehbar.
7. **Review durchführen:** Owner bestätigt, entzieht, korrigiert oder eskaliert.
8. **Ausnahmen steuern:** befristet, begründet, risikobewertet, mit Wiedervorlage.
9. **Verbessern:** Findings und Muster fließen in Rollenmodell, Prozess oder Tooling zurück.

## Entscheidungen

- Welche Systeme und Datenablagen sind für den Start kritisch genug?
- Welche Zugriffe brauchen Fachfreigabe, Sicherheitsfreigabe oder Managemententscheidung?
- Wie oft werden welche Zugriffstypen reviewed?
- Welche Ausnahmen sind tolerierbar, welche nicht?
- Wie werden externe Zugriffe, Adminrechte und technische Konten priorisiert?
- Welche Zielkonflikte bestehen zwischen schneller Arbeitsfähigkeit und restriktiver Rechtevergabe?

## Evidenz

### Starke Evidenz

- aktueller Asset-/Systemscope mit Ownern,
- Zugriffsanträge mit Begründung und Freigabe,
- Berechtigungsexporte oder Systemnachweise zum Reviewzeitpunkt,
- Reviewprotokolle mit Entscheidung pro auffälligem Zugriff,
- Nachweise über entzogene Rechte,
- dokumentierte Ausnahmen mit Ablaufdatum,
- Managemententscheidung bei akzeptierten Restrisiken.

### Schwache Evidenz

- allgemeine Access-Policy ohne konkrete Durchführung,
- Screenshot einzelner Gruppen ohne Owner oder Reviewdatum,
- unvollständige Listen ohne Systemscope,
- „wird durch IT geregelt“ ohne Nachweis der Entscheidung,
- alte Rollenmatrix ohne Rezertifizierung.

### Evidenzlücken

- keine Verbindung zwischen HR-Ereignissen und Zugriffsentzug,
- externe Konten ohne Vertrags- oder Ownerbezug,
- technische Konten ohne Verantwortlichen,
- Adminrechte ohne gesonderten Review,
- dauerhafte Ausnahmen ohne Risikoakzeptanz.

## Wirksamkeitsprüfung

Prüffragen:

- Kann für ein kritisches System nachvollzogen werden, wer Zugriff hat und warum?
- Sind Rollenwechsel und Austritte innerhalb definierter Fristen verarbeitet?
- Gibt es Nachweise, dass Reviews zu Korrekturen geführt haben?
- Sind privilegierte, externe und technische Zugriffe besonders betrachtet?
- Sind Ausnahmen befristet und entscheidungsfähig dokumentiert?
- Erkennt das Management, wo Ressourcen- oder Zielkonflikte bestehen?

Mögliche Kennzahlen:

- Anteil kritischer Systeme mit aktuellem Owner,
- überfällige Berechtigungsreviews,
- Anzahl kritischer Altberechtigungen,
- Dauer bis Entzug nach Austritt,
- Ausnahmequote und überfällige Ausnahmen,
- nicht zuordenbare Konten.

## BSIG-/NIS2-Anschluss

Zugriffssteuerung ist ein zentraler Anschluss an NIS2-orientierte Risikomanagementmaßnahmen, insbesondere Cyberhygiene, Zugriffsschutz, Umgang mit kritischen Systemen, Incident-Prävention und Governance der Informationssicherheit.

Für BSIG-/NIS2-Betroffenheit sollte die Organisation im Anforderungsregister prüfen, welche Dienste, Systeme, Rollen und Nachweise relevant sind. Dieses Artefakt ersetzt keine rechtliche Auslegung und keine verbindliche Prüfung der Anwendbarkeit.

## Grenzen

- Dieses Artefakt ist kein Identity-&-Access-Management-Tooldesign.
- Es ersetzt keine Datenschutzprüfung für Beschäftigtenauswertungen, Logging oder Monitoring.
- Es trifft keine verbindliche Aussage zu gesetzlichen Pflichten.
- Es enthält keine ISO-27002-Texte oder Zertifizierungszusage.
- Es darf nicht als Nachweis genügen, wenn die tatsächliche Zugriffspraxis ungeprüft bleibt.

## Handoffs

- **HR-Handoff:** Eintritt, Rollenwechsel, Austritt, längere Abwesenheit oder Funktionswechsel.
- **Datenschutz-Handoff:** personenbezogene Zugriffsauswertungen, Monitoring, Verhaltens- oder Leistungskontrollrisiko.
- **Legal-/Einkauf-Handoff:** externe Zugriffe, Dienstleister, Vertragsende, Zugriffspflichten in Vereinbarungen.
- **Incident-Handoff:** Verdacht auf kompromittiertes Konto, unberechtigte Nutzung, nicht erklärbare Berechtigung.
- **Management-Handoff:** dauerhafte Ausnahmen, Ressourcenkonflikte, nicht umsetzbare Trennung, akzeptierte Restrisiken.
- **Audit-/Evidence-Handoff:** fehlende Reviewnachweise oder unvollständiger Systemscope.

## Typische Fehler

- Zugriff wird beim Eintritt sauber vergeben, aber bei Rollenwechseln nicht bereinigt.
- Adminrechte werden wie normale Nutzerrechte behandelt.
- Berechtigungsreviews werden verschickt, aber Entscheidungen nicht nachgehalten.
- Fachbereiche genehmigen pauschal alle bestehenden Rechte, weil die Liste unverständlich ist.
- Servicekonten und API-Tokens fehlen im Review.
- Ausnahmen werden dauerhaft, weil kein Ablaufdatum gesetzt wurde.
- Die Organisation verwechselt ein IAM-Tool mit funktionierender Governance.

## Fiktives Mini-Beispiel

Ein fiktiver Mittelständler betreibt ein Kundenportal. Beim Review fällt auf, dass drei ehemalige Projektmitglieder noch Zugriff auf die Administrationsgruppe haben. Der IT-Owner erstellt einen Berechtigungsexport, der Product Owner bestätigt fehlenden Geschäftsbedarf, IT entzieht die Rechte und dokumentiert die Änderung im Ticket. Im Management Review wird entschieden, dass Adminrechte künftig monatlich und normale Fachzugriffe quartalsweise geprüft werden.

Evidenz:

- Export der Admingruppe zum Reviewzeitpunkt,
- Entscheidung des Product Owners,
- Ticket mit Rechteentzug,
- aktualisierte Reviewfrequenz,
- Managemententscheidung zur Priorisierung.
