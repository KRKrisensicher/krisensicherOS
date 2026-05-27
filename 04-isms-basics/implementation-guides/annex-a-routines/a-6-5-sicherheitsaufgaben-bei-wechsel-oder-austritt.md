
# A.6.5 — Sicherheitsaufgaben bei Wechsel oder Austritt

## Zweck

Sicherheitsaufgaben bei Wechsel oder Austritt sorgen dafür, dass Rollenänderungen, interne Wechsel, Vertragsenden und Austritte kontrolliert abgewickelt werden. Zugriffe, Geräte, Informationen, Verantwortlichkeiten und Wissen sollen geordnet übergeben oder entzogen werden.

Der Kern ist ein verlässlicher Mover-/Leaver-Prozess: nicht erst am letzten Arbeitstag reagieren, sondern frühzeitig Aufgaben, Owner, Fristen und Nachweise auslösen.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der Rollenwechsel und Austritte sicherheitsrelevant erkannt, bewertet, umgesetzt und nachgewiesen werden. Die Routine verbindet HR-/Auftragsereignisse, Zugriffsentzug, Asset-Rückgabe, Wissensübergabe, Geheimhaltungs-/Verantwortungshinweise, Lieferantenbezug und Review.

## Typische Risiken

- Wenn Austritte nicht rechtzeitig an IT und Fachbereiche gemeldet werden, bleiben Konten, Tokens oder physische Zugänge aktiv.
- Wenn Rollenwechsel nicht bereinigt werden, wachsen Berechtigungen über die Zeit und Trennungskonflikte entstehen.
- Wenn Wissen und Verantwortlichkeiten nicht übergeben werden, entstehen Betriebs- und Krisenrisiken.
- Wenn externe Mitarbeitende oder Dienstleisterenden fehlen, bleiben Drittzugriffe unkontrolliert.
- Wenn Geräte, Datenträger oder Unterlagen nicht zurückgeführt werden, können Informationen abfließen.

## Trigger

- Kündigung, Vertragsende, Ende eines Projekts oder geplanter letzter Arbeitstag.
- interner Rollenwechsel, Teamwechsel, Beförderung, längere Abwesenheit oder Änderung der Aufgaben.
- Ende oder Änderung einer Dienstleisterbeauftragung, Subdienstleisterwechsel oder externer Zugriff.
- Sicherheitsereignis, Verdacht auf Missbrauch oder sofortiger Entzug erforderlich.
- Änderung des Schutzbedarfs einer Rolle oder eines Systems.
- turnusmäßiger Review von offenen Mover-/Leaver-Fällen.

## Rollen und Verantwortung

- **HR / People-Funktion:** löst Beschäftigtenwechsel und Austritte rechtzeitig aus und koordiniert personenbezogene Prozessschritte.
- **Führungskraft / Auftraggeber:** bewertet Rollenänderung, Übergabe, Wissenssicherung und fachliche Zugriffe.
- **IT-/IAM-Owner:** entzieht, ändert oder bestätigt Konten, Gruppen, Tokens, Geräte und technische Zugänge.
- **Asset Owner / Service Owner:** bestätigt, welche fachlichen Rechte, Verantwortlichkeiten und Datenbestände betroffen sind.
- **ISMS-Owner / Security-Rolle:** definiert Mindestaufgaben, Risikokriterien, Eskalation und Stichprobenreview.
- **Einkauf / Lieferantenmanagement:** steuert externe Personen, Vertragsenden und Dienstleisterzugriffe.
- **Legal / Datenschutz:** prüft Sonderfälle, Aufbewahrung, Kommunikation, Untersuchungen oder Konflikte.
- **Management:** entscheidet bei Hochrisiko-Austritten, Konflikten, Ausnahmen oder Ressourcenproblemen.

## Implementierung

### Minimalstart

Ziel: Kritische Wechsel und Austritte lösen zuverlässig Sicherheitsaufgaben aus.

1. HR oder Auftraggeber meldet Wechsel und Austritte an IT, Führungskraft und relevante Owner.
2. Eine Checkliste deckt mindestens Konten, Gruppen, Adminrechte, externe Zugänge, Geräte, Schlüssel/Badges, Datenträger, Übergabe und offene Verantwortlichkeiten ab.
3. Zugriffe werden zum passenden Zeitpunkt entzogen oder angepasst.
4. Kritische Rollen erhalten eine zusätzliche Prüfung durch Asset Owner oder ISMS-Owner.
5. Abschluss und Ausnahmen werden dokumentiert.

Minimaler Nachweis:

- Mover-/Leaver-Ticket,
- Checkliste mit Verantwortlichen und Fristen,
- Nachweis entzogener oder geänderter Zugriffe,
- Asset-/Geräterückgabe,
- Übergabe- oder Ausnahmeentscheidung.

### Solide Praxis

Ziel: Wechsel und Austritte sind mit IAM, Asset Management und Wissensübergabe verbunden.

1. Rollenwechsel lösen eine Rezertifizierung bestehender Rechte aus, nicht nur neue Rechte.
2. Kritische Konten, Servicekonten, API-Tokens, Shared Secrets und Adminrechte werden gesondert betrachtet.
3. Geräte, Schlüssel, Badges, Datenträger und Dokumentenbestände werden über Asset- oder Facility-Prozesse nachverfolgt.
4. Verantwortlichkeiten für Systeme, Risiken, Lieferanten, Notfallrollen oder offene Maßnahmen werden übergeben.
5. Externe Mitarbeitende werden über Beauftragungsende, Dienstleisterkontakt und Zugriffsliste gesteuert.
6. Stichproben prüfen fristgerechte Umsetzung und finden Altberechtigungen.

Starke Evidenz:

- Mover-/Leaver-Workflow,
- IAM-Änderungs- oder Entzugsnachweise,
- Rechte-Review bei Rollenwechsel,
- Asset-Rückgabeprotokolle,
- Übergabeprotokoll für kritische Verantwortung,
- Ausnahme- und Eskalationslog,
- Stichprobenreview.

### Fortgeschritten

Ziel: Wechsel- und Austrittssteuerung ist weitgehend integriert und risikobasiert überwacht.

1. HR-, Lieferanten-, IAM-, Asset- und Facility-Informationen erzeugen automatisierte oder halbautomatische Aufgaben.
2. Hochrisiko-Austritte erhalten vorab definierte Eskalations- und Schutzmaßnahmen.
3. Maschinenidentitäten, Secrets, Zertifikate, Tokens und geteilte Konten werden systematisch rotiert oder entzogen.
4. Kritische Verantwortlichkeiten werden in BCM-, Incident-, Risiko- und Service-Owner-Registern aktualisiert.
5. Kennzahlen zeigen überfällige Entzüge, Rollenwechsel ohne Rezertifizierung, offene Assets und externe Zugänge nach Vertragsende.
6. Management erhält Trends zu Prozesslücken, technischen Schulden und Ressourcenbedarf.

## Ablauf als Routine

1. **Ereignis erfassen:** Rollenwechsel, Austritt, Projektende, Dienstleisterende oder Sonderfall.
2. **Risiko einstufen:** Rolle, Zugriffe, Daten, Privilegien, Konfliktlage und Kritikalität bewerten.
3. **Aufgaben erzeugen:** Zugriff, Geräte, physische Zugänge, Übergaben, Verantwortlichkeiten und Kommunikation zuweisen.
4. **Umsetzen:** Rechte anpassen oder entziehen, Assets zurückführen, Secrets rotieren, Verantwortung übertragen.
5. **Bestätigen:** technische und fachliche Owner bestätigen Abschluss oder begründen offene Punkte.
6. **Ausnahmen steuern:** zeitlich begrenzen, kompensieren und entscheidungsfähig dokumentieren.
7. **Reviewen:** Stichproben, Altberechtigungen und Lessons Learned prüfen.
8. **Eskalieren:** überfällige Hochrisiko-Aufgaben oder Konflikte ins Management geben.

## Entscheidungen

- Welche Rollenwechsel brauchen vollständigen Rechte-Review?
- Wann müssen Zugriffe sofort, am letzten Tag oder nach Übergabe entzogen werden?
- Welche Rollen gelten als Hochrisiko-Austritt?
- Wer darf temporäre Restzugriffe genehmigen und wie lange?
- Welche Secrets, Tokens oder geteilten Zugänge müssen rotiert werden?
- Wie werden externe Zugriffe nach Projekt- oder Vertragsende nachgewiesen beendet?

## Evidenz

### Starke Evidenz

- vollständiges Mover-/Leaver-Ticket mit Datum, Ownern und Status,
- IAM-Logs oder Tickets zum Entzug bzw. zur Anpassung von Rechten,
- Review bestehender Berechtigungen bei Rollenwechsel,
- Asset-, Badge- oder Schlüsselrückgabe,
- Übergabeprotokoll kritischer Verantwortlichkeiten,
- Nachweis beendeter externer Zugriffe,
- Ausnahmeentscheidung mit Ablaufdatum und Management-Handoff bei Risiko.

### Schwache Evidenz

- HR-Austrittsmeldung ohne technische Abschlussbestätigung,
- Checkliste ohne Systemscope,
- manuelle E-Mail „alles erledigt“ ohne Nachweise,
- Entzug des Hauptkontos, aber keine Prüfung von SaaS, Tokens oder Gruppen,
- Geräteübersicht ohne Rückgabe- oder Löschstatus.

### Evidenzlücken

- Rollenwechsel ohne Berechtigungsbereinigung,
- externe Konten nach Vertragsende aktiv,
- Adminrechte oder Servicezugänge nicht geprüft,
- Assets oder Datenträger unklar,
- kritische Verantwortung ohne Nachfolger,
- Ausnahmen ohne Frist oder Risikoentscheidung.

## Wirksamkeitsprüfung

Prüffragen:

- Werden Wechsel und Austritte rechtzeitig an alle relevanten Owner ausgelöst?
- Sind Zugriffe fristgerecht angepasst oder entzogen?
- Werden Rollenwechsel als Bereinigungsereignis genutzt?
- Sind externe Personen und Dienstleisterenden vollständig abgedeckt?
- Werden Assets, physische Zugänge und Secrets berücksichtigt?
- Gibt es Nachweise für Übergabe kritischer Verantwortlichkeiten?
- Werden überfällige Hochrisiko-Fälle eskaliert?

Mögliche Kennzahlen:

- Zeit bis Zugriffsentzug nach Austritt,
- Rollenwechsel mit abgeschlossenem Rechte-Review,
- offene Mover-/Leaver-Aufgaben,
- externe Konten nach Vertragsende,
- überfällige Asset-Rückgaben,
- Ausnahmen und überfällige Restzugriffe,
- Findings aus Stichproben.

## BSIG-/NIS2-Anschluss

Mover-/Leaver-Routinen sind anschlussfähig an NIS2-orientierte Governance, Zugriffsschutz, Cyberhygiene, Lieferkettensteuerung, Incident-Prävention und Business Continuity. Der konkrete Bezug sollte im Anforderungsregister, Rollenmodell und Management Review organisationsspezifisch geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Prüfung von Arbeits-, Vertrags-, Datenschutz- oder Meldefragen.

## Grenzen

- Kein vollständiges HR-Offboarding- oder IAM-Tooldesign.
- Keine Rechts- oder Datenschutzberatung zu Austritt, Konfliktfällen oder Aufbewahrung.
- Keine Garantie, dass ein dokumentierter Entzug alle Schattenzugriffe abdeckt.
- Keine Zertifizierungs-, Konformitäts- oder Sicherheitszusage.
- Keine ISO-27002-Texte oder echten Personen-/Organisationsdaten.

## Handoffs

- **HR-Handoff:** Beschäftigtenwechsel, Austritt, Zeitpunkte, Kommunikation und Sonderfälle.
- **Access-/IAM-Handoff:** Konten, Gruppen, Adminrechte, SaaS, Tokens, Zertifikate und Servicekonten.
- **Asset-/Facility-Handoff:** Geräte, Datenträger, Schlüssel, Badges, physische Zugänge und Rückgabe.
- **Fachbereichs-Handoff:** Wissensübergabe, Prozessverantwortung, offene Maßnahmen und Datenbestände.
- **Lieferanten-Handoff:** externe Personen, Projektende, Vertragsende und Subdienstleisterzugriffe.
- **Legal-/Datenschutz-Handoff:** Konfliktfälle, Untersuchungen, Aufbewahrung, personenbezogene Daten und Kommunikation.
- **Management-Handoff:** Hochrisiko-Austritte, überfällige Entzüge, Ausnahmen oder Ressourcenlücken.

## Typische Fehler

- Nur Austritte werden betrachtet, Rollenwechsel aber nicht.
- Hauptkonto wird deaktiviert, aber SaaS, Tokens und externe Zugänge bleiben aktiv.
- Führungskräfte melden Wechsel zu spät.
- Externe Projektmitarbeitende verschwinden aus dem Blick, sobald das Projekt endet.
- Wissens- und Verantwortungsübergabe wird nicht als Sicherheitsaufgabe verstanden.
- Ausnahmen für Restzugriffe werden nicht befristet.
- Stichproben finden Altberechtigungen, aber der Prozess wird nicht verbessert.

## Fiktives Mini-Beispiel

Eine fiktive Mitarbeiterin wechselt vom Support in den Vertrieb. HR löst ein Mover-Ticket aus. Der Support Lead bestätigt, dass Zugriff auf Kundentickets nicht mehr benötigt wird, während der Vertriebszugriff neu beantragt wird. IT entfernt Support-Gruppen, prüft ein geteiltes Reporting-Konto und dokumentiert die Änderung. Der Service Owner übernimmt zwei offene Maßnahmen aus dem alten Rollenprofil. Eine Stichprobe zeigt später, dass ein SaaS-Zugang vergessen wurde; der Mover-Prozess wird um diesen Dienst ergänzt.

Evidenz:

- Mover-Ticket,
- Rechte-Review Support/Vertrieb,
- IAM-Änderungsnachweis,
- Übergabe offener Maßnahmen,
- Stichprobenfinding,
- Prozessanpassung für den SaaS-Dienst.
