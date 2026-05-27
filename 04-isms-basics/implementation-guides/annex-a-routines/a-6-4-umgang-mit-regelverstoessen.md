
# A.6.4 — Umgang mit Regelverstößen

## Zweck

Der Umgang mit Regelverstößen sorgt dafür, dass Sicherheitsabweichungen fair, nachvollziehbar und wirksam behandelt werden. Ziel ist nicht möglichst harte Sanktion, sondern ein belastbarer Prozess, der Schutzbedarf, Sachverhaltsklärung, Verhältnismäßigkeit, Lernen und notwendige Eskalation verbindet.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine geklärte Routine für Meldung, Bewertung, Behandlung und Nachverfolgung sicherheitsrelevanter Regelverstöße durch Beschäftigte oder externe Beteiligte. Die Routine trennt fachliche Sicherheitsbewertung, arbeits-/vertragsrechtliche Schritte, Incident Handling und Verbesserungsmaßnahmen.

## Typische Risiken

- Wenn Verstöße informell behandelt werden, entstehen Ungleichbehandlung, Wiederholungsfehler und fehlende Nachvollziehbarkeit.
- Wenn jeder Verstoß automatisch als Disziplinarfall behandelt wird, sinkt die Meldebereitschaft und Lernchancen gehen verloren.
- Wenn schwere Verstöße nicht eskaliert werden, bleiben Schaden, Insider-Risiken oder rechtliche Folgen unbehandelt.
- Wenn Incident Response und HR/Legal nicht abgestimmt sind, werden Beweise, Rechte oder Schutzmaßnahmen gefährdet.
- Wenn Dienstleisterverstöße nicht vertraglich verfolgt werden, bleiben externe Risiken ohne Konsequenz.

## Trigger

- Meldung oder Beobachtung eines Sicherheitsverstoßes.
- Incident, Beinahevorfall, Auditfinding, Kontrollabweichung oder wiederholte Nichtbeachtung.
- Missbrauch oder unsachgemäße Nutzung von Zugriffen, Daten, Geräten, Cloud-Diensten oder Kommunikationskanälen.
- Verstoß externer Mitarbeitender oder Dienstleister gegen vereinbarte Sicherheitsregeln.
- Ergebnis aus Monitoring, Review oder Untersuchung, soweit zulässig und geklärt.
- Management-, HR-, Legal- oder Datenschutzanfrage zu einem sicherheitsrelevanten Sachverhalt.

## Rollen und Verantwortung

- **ISMS-Owner / Security-Rolle:** bewertet Sicherheitsrelevanz, Risikowirkung und notwendige Schutzmaßnahmen.
- **Führungskraft / Auftraggeber:** klärt Kontext, Alltagspraxis und unmittelbare organisatorische Maßnahmen.
- **HR / People-Funktion:** steuert Beschäftigtenbezug, Fairness, Kommunikation und arbeitsrechtliche Schnittstellen.
- **Legal / Datenschutz:** prüft Untersuchungsrahmen, Beweismittel, Datenschutz, Vertrags- und Mitbestimmungsfragen.
- **Incident Response:** übernimmt, wenn der Verstoß ein Sicherheitsereignis oder einen Verdacht auf Kompromittierung auslöst.
- **Einkauf / Lieferantenmanagement:** verfolgt Verstöße externer Parteien und vertragliche Maßnahmen.
- **Management:** entscheidet bei schweren Fällen, Ausnahmen, Ressourcen und Kulturthemen.

## Implementierung

### Minimalstart

Ziel: Regelverstöße werden konsistent erfasst, bewertet und eskaliert.

1. Ein Meldeweg für sicherheitsrelevante Verstöße wird festgelegt.
2. Eine einfache Klassifizierung unterscheidet Versehen, wiederholte Abweichung, grobe Pflichtverletzung, Incident-Verdacht und externen Vertragsverstoß.
3. Verantwortliche Rollen für Erstbewertung, HR/Legal-Handoff und Incident-Handoff sind benannt.
4. Jede Behandlung dokumentiert Sachverhalt, Bewertung, Entscheidung, Maßnahme und Wiedervorlage.
5. Wiederholungsmuster führen zu Schulungs-, Prozess- oder Kontrollverbesserung.

Minimaler Nachweis:

- Melde- und Eskalationsweg,
- Fall- oder Ticketprotokoll,
- Entscheidung zur Klassifizierung,
- Maßnahmen- und Abschlussnachweis,
- Handoff an HR, Legal, Datenschutz, Incident Response oder Lieferantenmanagement.

### Solide Praxis

Ziel: Die Behandlung ist verhältnismäßig, wiederholbar und lernorientiert.

1. Kategorien und Eskalationskriterien sind beschrieben und für Führungskräfte nutzbar.
2. Untersuchungen folgen geklärten Regeln zu Zugriff auf Beweismittel, Datenschutz und Beteiligung relevanter Stellen.
3. Maßnahmen reichen von Coaching, Nachschulung und Prozesskorrektur bis zu formalen arbeits- oder vertragsrechtlichen Schritten.
4. Schwere Fälle werden mit Incident Response, Legal, Datenschutz und Management koordiniert.
5. Externe Verstöße werden über Lieferantenmanagement und Vertragspflichten nachverfolgt.
6. Trends fließen in Awareness, Zugriffskontrolle, Betriebsregeln und Management Review ein.

Starke Evidenz:

- Klassifizierungs- und Eskalationsschema,
- Fallakte mit Entscheidung und Handoffs,
- Nachweis verhältnismäßiger Maßnahmen,
- Lessons Learned und Kontrollverbesserungen,
- Managemententscheidung bei schweren oder wiederkehrenden Fällen,
- Lieferantenkommunikation bei externem Verstoß.

### Fortgeschritten

Ziel: Regelverstöße werden als Governance-Signal genutzt, ohne Fairness und Rechtsrahmen zu verlieren.

1. Fallmuster werden aggregiert ausgewertet, ohne unnötige personenbezogene Detailauswertung.
2. Wiederkehrende Verstöße lösen Ursachenanalysen aus: unklare Regel, unrealistischer Prozess, Toolproblem, Führungsthema oder bewusste Umgehung.
3. Incident-, HR-, Legal-, Datenschutz- und Lieferantenprozesse sind mit klaren Übergabepunkten integriert.
4. Führungskräfte werden für frühe, faire und dokumentierte Behandlung befähigt.
5. Management sieht entscheidungsfähige Trends: kritische Wiederholungen, Prozesslücken, Ressourcenkonflikte und Kulturindikatoren.

## Ablauf als Routine

1. **Verstoß wird bekannt:** Meldung, Review, Incident, Audit oder Beobachtung.
2. **Erstschutz prüfen:** unmittelbare Risiken begrenzen, etwa Zugriff sperren oder Datenabfluss stoppen, wenn erforderlich.
3. **Sachverhalt abgrenzen:** was ist bekannt, welche Regeln sind betroffen, welche Systeme oder Daten sind involviert?
4. **Klassifizieren:** Versehen, Wiederholung, schwerer Verstoß, Incident-Verdacht oder externer Vertragsverstoß.
5. **Handoffs auslösen:** HR, Legal, Datenschutz, Incident Response, Lieferantenmanagement oder Management nach Kriterien einbeziehen.
6. **Maßnahme entscheiden:** Coaching, Nachschulung, Prozessänderung, Zugriffsanpassung, formale Schritte oder Vertragsmaßnahme.
7. **Nachverfolgen:** Umsetzung, Abschluss, Wiedervorlage und mögliche Wiederholung dokumentieren.
8. **Lernen:** Regel, Schulung, Tooling oder Kontrolle anpassen.

## Entscheidungen

- Welche Fälle dürfen Führungskräfte selbst behandeln und welche müssen eskaliert werden?
- Wann wird ein Regelverstoß zum Incident oder Untersuchungsfall?
- Welche Beweismittel dürfen genutzt werden und wer entscheidet darüber?
- Welche Maßnahmen sind verhältnismäßig und wirksam?
- Wie werden externe Verstöße vertraglich oder operativ behandelt?
- Welche Muster gehören ins Management Review?

## Evidenz

### Starke Evidenz

- dokumentierter Fall mit Sachverhalt, Klassifizierung und Entscheidung,
- Handoff-Nachweis an HR, Legal, Datenschutz, Incident Response oder Lieferantenmanagement,
- Maßnahmen- und Abschlussnachweis,
- Lessons Learned mit Anpassung von Regel, Schulung oder Kontrolle,
- aggregierte Trendanalyse,
- Managemententscheidung bei schweren oder wiederkehrenden Verstößen.

### Schwache Evidenz

- informelle E-Mail ohne Entscheidung oder Abschluss,
- pauschale Abmahnungs- oder Sanktionsliste ohne Sicherheitsbewertung,
- Incident-Ticket ohne HR/Legal-Klärung bei Personenbezug,
- Schulung als Standardantwort ohne Ursachenanalyse,
- Statistik ohne Kategorien und Handoffs.

### Evidenzlücken

- keine einheitliche Klassifizierung,
- schwere Fälle ohne Management- oder Legal-Handoff,
- Beweismittelverwendung ohne Datenschutzklärung,
- externe Verstöße ohne Lieferantenverfolgung,
- Wiederholungen ohne Prozessverbesserung.

## Wirksamkeitsprüfung

Prüffragen:

- Werden Verstöße konsistent und fair klassifiziert?
- Sind Handoffs bei Personenbezug, Incident-Verdacht und externen Parteien klar?
- Führen Maßnahmen zu weniger Wiederholungen oder besseren Prozessen?
- Werden schwere Fälle rechtzeitig eskaliert?
- Sind Nachweise vollständig, aber datensparsam?
- Erkennt das Management strukturelle Ursachen statt nur Einzelfälle?

Mögliche Kennzahlen:

- Anzahl Fälle je Kategorie,
- Zeit bis Erstbewertung,
- Anteil wiederholter Verstöße,
- Fälle mit ausgelöstem Incident-/HR-/Legal-Handoff,
- offene Maßnahmen aus Regelverstößen,
- Prozessverbesserungen aus Lessons Learned.

## BSIG-/NIS2-Anschluss

Der geregelte Umgang mit Verstößen ist anschlussfähig an NIS2-orientierte Governance, Incident-Fähigkeit, Cyberhygiene, Sicherheitskultur, Lieferkettensteuerung und Managementverantwortung. Konkrete Anforderungen und Meldebezüge müssen organisationsspezifisch und menschlich geprüft werden.

Dieses Artefakt ersetzt keine Rechts-, Arbeitsrechts- oder Datenschutzberatung und keine Meldepflichtbewertung.

## Grenzen

- Keine rechtliche Bewertung einzelner Verstöße oder arbeitsrechtlicher Maßnahmen.
- Keine Aufforderung zu Überwachung oder personenbezogener Auswertung ohne Klärung.
- Keine Gleichsetzung von Fehlern, Lernen und Disziplinarmaßnahmen.
- Keine Zertifizierungs-, Konformitäts- oder Sicherheitszusage.
- Keine ISO-27002-Texte oder echten Falldaten.

## Handoffs

- **HR-Handoff:** Beschäftigtenbezug, Führung, Maßnahmen, Fairness und Personalprozess.
- **Legal-/Datenschutz-Handoff:** Untersuchungsrahmen, Beweismittel, personenbezogene Daten, Vertrags- oder Meldefragen.
- **Incident-Handoff:** Kompromittierungsverdacht, Datenabfluss, Missbrauch von Zugriffen oder laufende Gefahr.
- **Lieferanten-Handoff:** Verstöße externer Personen, Vertragsmaßnahmen und Nachweise.
- **Management-Handoff:** schwere Verstöße, Wiederholungsmuster, Kulturprobleme oder Ressourcenkonflikte.
- **Audit-/Evidence-Handoff:** unvollständige Fallakten, fehlende Entscheidungen oder nicht nachverfolgte Maßnahmen.

## Typische Fehler

- Regelverstöße werden entweder bagatellisiert oder sofort maximal sanktioniert.
- Sicherheitsbewertung, HR-Prozess und Incident Response laufen unkoordiniert.
- Führungskräfte behandeln ähnliche Fälle unterschiedlich.
- Personenbezogene Daten werden gesammelt, ohne Zweck und Grenzen zu klären.
- Externe Verstöße verschwinden im Dienstleisterkanal ohne Nachweis.
- Lessons Learned erreichen Schulung, Regeln oder technische Kontrollen nicht.

## Fiktives Mini-Beispiel

Ein fiktiver Fachbereich nutzt einen nicht freigegebenen Cloud-Speicher, um Projektdateien zu teilen. Die Führungskraft meldet den Fall an den ISMS-Owner. Die Erstbewertung ergibt keinen Hinweis auf Datenabfluss, aber einen wiederholten Prozessverstoß. Datenschutz wird einbezogen, weil personenbezogene Daten betroffen sein könnten. Die Maßnahme kombiniert Löschung aus dem Tool, Freigabe eines geeigneten Austauschwegs und ein Teambriefing. Im Management Review wird entschieden, den offiziellen Dateiaustausch schneller bereitzustellen.

Evidenz:

- Fallticket mit Klassifizierung,
- Datenschutz-Handoff,
- Nachweis der Bereinigung,
- Teambriefing,
- Maßnahme zur offiziellen Austauschlösung,
- Managemententscheidung zum Ressourcenthema.
