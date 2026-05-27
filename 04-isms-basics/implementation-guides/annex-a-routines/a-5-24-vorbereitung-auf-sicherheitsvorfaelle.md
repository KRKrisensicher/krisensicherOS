
# A.5.24 — Vorbereitung auf Sicherheitsvorfälle

## Zweck

Vorbereitung auf Sicherheitsvorfälle schafft Handlungsfähigkeit, bevor Druck entsteht. Die Organisation legt Rollen, Meldewege, Eskalationen, Kommunikationswege, Entscheidungsrechte, technische Zugänge und Übungsroutinen fest, damit ein Sicherheitsereignis nicht erst im Ernstfall organisiert werden muss.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Incident-Preparedness-Routine: Sie weiß, wer bei Verdacht handelt, wie Ereignisse gemeldet und triagiert werden, welche Rollen erreichbar sind, welche Informationen benötigt werden, welche Human Gates gelten und wie die Vorbereitung regelmäßig getestet und verbessert wird.

## Typische Risiken

- Wenn Meldewege unklar sind, gehen frühe Hinweise verloren oder erreichen die falschen Personen.
- Wenn Rollen erst im Vorfall bestimmt werden, verzögern sich Eindämmung, Entscheidung und Kommunikation.
- Wenn technische Zugänge, Logs oder Ansprechpartner fehlen, kann der Vorfall nicht belastbar bewertet werden.
- Wenn externe Dienstleister, Legal, Datenschutz oder Management nicht vorbereitet sind, entstehen Lücken bei Bewertung und Eskalation.
- Wenn nie geübt wird, wirken Playbooks im Dokument gut, brechen aber im Betrieb.

## Trigger

- Aufbau oder Review des Incident-Response-Prozesses.
- neues kritisches System, neuer Cloud-Dienst, neuer Dienstleister oder neuer Geschäftsprozess.
- Sicherheitsereignis, Beinahevorfall, Schwachstellenfund, Auditfinding oder Lessons Learned.
- Änderung von Meldewegen, Rufbereitschaft, Managementstruktur oder externen Kontakten.
- gesetzliche, vertragliche oder kundenbezogene Anforderung, die rechtlich zu prüfen ist.
- regelmäßige Übung, Tabletop, Krisenstabsprobe oder ISMS-Review.

## Rollen und Verantwortung

- **Incident Owner / Incident Lead:** koordiniert Vorbereitung, Triagefähigkeit und Vorfallroutine.
- **ISMS-Owner / Security-Rolle:** definiert Mindestprozess, Klassifikationslogik, Evidenz und Review.
- **IT-Betrieb / Plattformteam:** stellt technische Kontaktwege, Logs, Zugriff und Wiederherstellungsfähigkeit bereit.
- **Fachbereich / Service Owner:** bewertet Geschäftsfolgen und priorisiert kritische Dienste.
- **Kommunikation / Management:** bereitet interne und externe Kommunikationsentscheidungen vor.
- **Legal / Datenschutz:** bewertet rechtliche, Datenschutz- und Meldepflichtfragen im Human Review.
- **BCM-/Krisenrolle:** verbindet Sicherheitsvorfälle mit Notfall- und Krisenmanagement.

## Implementierung

### Minimalstart

Ziel: Bei Verdacht wissen alle, wohin gemeldet wird und wer die erste Bewertung übernimmt.

1. Ein zentraler Meldeweg für Sicherheitsereignisse wird festgelegt und kommuniziert.
2. Eine kleine Incident-Kernrolle wird benannt: Incident Lead, IT-Kontakt, ISMS/Security, Management-Eskalation.
3. Ein einfacher Triagebogen hält fest: was ist passiert, wann, betroffenes System, erste Auswirkung, meldende Stelle, Sofortmaßnahmen.
4. Eine Kontakt- und Eskalationsliste wird gepflegt.
5. Kritische Systeme und Logquellen werden für erste Analysen benannt.
6. Mindestens jährlich wird ein Meldeweg- oder Tabletop-Test durchgeführt.

Minimaler Nachweis:

- veröffentlichter Meldeweg,
- Rollen- und Kontaktliste,
- Triagevorlage,
- Liste kritischer Systeme/Logquellen,
- Übungs- oder Testnachweis,
- Maßnahmen aus Lessons Learned.

### Solide Praxis

Ziel: Vorbereitung wird risikobasiert, geübt und mit Geschäftsprozessen verbunden.

1. Vorfallkategorien und Schweregrade werden in eigener Sprache beschrieben.
2. Playbooks oder Checklisten decken typische Szenarien ab: Phishing, Kontokompromittierung, Malware, Datenabflussverdacht, Cloud-Fehlkonfiguration, Lieferantenincident, Ausfall kritischer Dienste.
3. Rollen, Stellvertretungen und Erreichbarkeiten werden regelmäßig geprüft.
4. Entscheidungs- und Human-Gate-Punkte werden vorab festgelegt: Abschaltung, externe Kommunikation, Risikoakzeptanz, Datenschutz-/Legal-Prüfung, Managementeskalation.
5. Übungen prüfen nicht nur Technik, sondern Entscheidungen, Kommunikation und Evidenzfluss.
6. Erkenntnisse aus Übungen und echten Vorfällen aktualisieren Playbooks, Schulungen und technische Voraussetzungen.

Starke Evidenz:

- Incident-Response-Rollenmodell,
- aktuelle Kontakt- und Eskalationsliste,
- szenariobezogene Checklisten,
- Übungsprotokolle mit Maßnahmen,
- Nachweise zu Logzugriffen und kritischen Informationsquellen,
- Managemententscheidung zu Ressourcen oder Bereitschaftsmodell.

### Fortgeschritten

Ziel: Incident Preparedness ist in Lagebild, BCM, Lieferantensteuerung und technische Detektion integriert.

1. Incident-Response-Plan, Krisenmanagement, Business Continuity und Kommunikationsprozesse sind aufeinander abgestimmt.
2. Kritische Logs, Alarme, Forensikzugänge und Dienstleisterkontakte sind vorab getestet.
3. Szenarien werden nach Risiko priorisiert und regelmäßig mit Fachbereichen, Management und externen Partnern geübt.
4. Entscheidungsräume sind vorbereitet: Abschaltung, Isolation, Wiederanlauf, Kundenkommunikation, Behördenkontakt, Lieferanteneskalation.
5. Kennzahlen zeigen Vorbereitungsstand: geübte Szenarien, offene Preparedness-Maßnahmen, erreichbare Rollen, Logabdeckung, Übungsfindings.

## Ablauf als Routine

1. **Vorbereitungsumfang festlegen:** kritische Prozesse, Systeme, Daten, Dienstleister und Szenarien bestimmen.
2. **Meldeweg und Rollen definieren:** Incident Lead, technische Rollen, Fachbereich, Management, Legal, Datenschutz, Kommunikation, BCM.
3. **Triagefähigkeit herstellen:** Vorlagen, Schweregrade, Kontaktlisten, Logquellen und erste Maßnahmen vorbereiten.
4. **Playbooks erstellen:** kurze, nutzbare Ablaufhilfen für wichtigste Szenarien.
5. **Kommunizieren und befähigen:** Meldeweg und Rollen in Awareness, Onboarding und Führungskräftebriefings verankern.
6. **Üben:** Tabletop, Meldewegtest, technische Probe oder Krisenübung durchführen.
7. **Verbessern:** Findings in Maßnahmenlog, Playbooks, Rollen, Tooling und Schulung zurückspielen.
8. **Reviewen:** mindestens jährlich oder nach wesentlichen Änderungen prüfen.

## Entscheidungen

- Welche Szenarien sind für die Organisation am wichtigsten?
- Wer darf im Vorfall technische Sofortmaßnahmen anstoßen?
- Wann wird Management, Legal, Datenschutz, Kommunikation oder BCM zwingend einbezogen?
- Welche Informationen müssen in den ersten Minuten oder Stunden verfügbar sein?
- Welche externen Dienstleister, Forensiker oder Anbieter müssen vorbereitet sein?
- Welche Bereitschafts- oder Ressourcenlücken akzeptiert die Organisation nicht?

## Evidenz

### Starke Evidenz

- aktueller Incident-Response-Plan in eigener Sprache,
- kommunizierter Meldeweg,
- Rollen-, Kontakt- und Stellvertretungsliste,
- Triage- und Playbook-Vorlagen,
- Übungsprotokolle mit Entscheidungen und Maßnahmen,
- Nachweise über getestete Log-, Zugriff- oder Eskalationswege,
- Managemententscheidungen zu Bereitschaft, Tools oder externem Support.

### Schwache Evidenz

- allgemeines Notfalldokument ohne Rollen und Kontakte,
- Playbook ohne Test oder Aktualisierung,
- Meldeweg nur im Intranet, aber nicht bekannt,
- Kontaktliste ohne Owner oder Reviewdatum,
- technische Toolliste ohne geprüfte Zugriffe.

### Evidenzlücken

- kein zentraler Meldeweg,
- keine erste Triageverantwortung,
- keine erreichbaren Stellvertretungen,
- unklare Legal-/Datenschutz-Eskalation,
- fehlende Logquellen für kritische Systeme,
- Übungen ohne Maßnahmenverfolgung.

## Wirksamkeitsprüfung

Prüffragen:

- Können Beschäftigte und externe Mitarbeitende Sicherheitsverdacht melden?
- Ist klar, wer die erste Bewertung übernimmt und wer eskaliert?
- Sind Kontaktlisten, Stellvertretungen und Dienstleisterkontakte aktuell?
- Wurden relevante Szenarien geübt und Findings nachverfolgt?
- Sind Legal, Datenschutz, Kommunikation, BCM und Management an den richtigen Stellen vorbereitet?
- Sind kritische Logs und technische Zugänge im Ernstfall verfügbar?

Mögliche Kennzahlen:

- Meldeweg-Bekanntheit oder Testergebnis,
- Anzahl geübter Szenarien,
- offene Maßnahmen aus Übungen,
- Aktualität der Kontaktliste,
- kritische Systeme mit verfügbarer Logquelle,
- Zeit bis Incident Lead erreichbar ist.

## BSIG-/NIS2-Anschluss

Die Vorbereitung auf Sicherheitsvorfälle ist anschlussfähig an NIS2-orientierte Themen wie Incident Handling, Melde- und Eskalationsfähigkeit, Business Continuity, Risikomanagement, Lieferantenabhängigkeiten und Managementverantwortung. Konkrete gesetzliche Melde- oder Nachweispflichten müssen organisationsspezifisch und rechtlich geprüft werden.

Dieses Artefakt ersetzt keine Rechtsberatung und keine verbindliche Bewertung der Anwendbarkeit.

## Grenzen

- Kein Ersatz für rechtliche Bewertung von Meldepflichten oder Datenschutzvorfällen.
- Kein vollständiges Forensik-, Krisen- oder Kommunikationshandbuch.
- Keine Garantie, dass ein Vorfall verhindert oder vollständig beherrscht wird.
- Keine ISO-27002-Texte oder Zertifizierungszusage.
- Keine echten Vorfalldaten, Kundendaten oder personenbezogenen Daten in öffentlichen Beispielen.

## Handoffs

- **Incident-Handoff:** vom Meldeweg in Triage, Klassifikation und Vorfallbearbeitung.
- **Legal-/Datenschutz-Handoff:** möglicher Personenbezug, Datenabfluss, Meldepflichtnähe, externe Kommunikation.
- **Kommunikations-Handoff:** interne Lagekommunikation, Kunden-, Partner- oder Öffentlichkeitskommunikation nur mit Freigabe.
- **BCM-/Krisen-Handoff:** Ausfall kritischer Dienste, Reputationsrisiko, Managementlage oder Krisenmodus.
- **Lieferanten-Handoff:** Anbieterincident, SaaS-Ausfall, Managed-Service-Abhängigkeit, fehlende Logs.
- **Management-Handoff:** Ressourcen, Bereitschaftsmodell, Abschaltung, Restrisiko, externe Unterstützung.
- **Audit-/Evidence-Handoff:** fehlende Übungsnachweise, unklare Rollen, nicht nachverfolgte Findings.

## Typische Fehler

- Incident Response wird erst beim Vorfall organisiert.
- Playbooks sind zu lang und im Stress nicht nutzbar.
- Meldewege existieren, sind aber Beschäftigten nicht bekannt.
- Übungen testen Technik, aber keine Entscheidungen und Kommunikation.
- Kontaktlisten sind veraltet oder ohne Stellvertretung.
- Datenschutz, Legal und Kommunikation werden zu spät einbezogen.
- Lessons Learned führen nicht zu Maßnahmen.

## Fiktives Mini-Beispiel

Ein fiktives Unternehmen führt einen Tabletop-Test zu kompromittierten Cloud-Zugangsdaten durch. Die Übung zeigt, dass der Meldeweg funktioniert, aber die Stellvertretung des Cloud-Admins nicht erreichbar ist und unklar bleibt, wer externe Kommunikation freigibt. Der Incident Lead dokumentiert zwei Maßnahmen: aktualisierte Rufliste und Managemententscheidung zum Kommunikationsfreigabeprozess.

Evidenz:

- Übungsszenario,
- Teilnehmer- und Rollenliste,
- Findings,
- Maßnahmenlog mit Owner und Frist,
- aktualisierte Kontaktliste,
- Managemententscheidung zur Freigabe.
