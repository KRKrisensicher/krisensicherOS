
# A.6.8 — Meldung von Sicherheitsereignissen durch Beschäftigte

## Zweck

Die Meldung von Sicherheitsereignissen durch Beschäftigte sorgt dafür, dass Verdachtsmomente, Fehler, Verluste, ungewöhnliche Beobachtungen und mögliche Vorfälle früh sichtbar werden. Ziel ist eine niedrigschwellige, bekannte und geübte Melderoutine — nicht Schuldzuweisung, sondern schnelle Einordnung, Eindämmung, Lernen und Entscheidung.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt einen klaren Meldeweg, über den Beschäftigte und relevante externe Mitarbeitende Sicherheitsereignisse erkennen, melden und in die Incident-Triage übergeben können. Die Routine verbindet Awareness, Führung, Helpdesk/Security, Datenschutz-/Legal-Handoffs, Eskalation und Lessons Learned.

## Typische Risiken

- Wenn Beschäftigte Meldewege nicht kennen, werden Phishing, Geräteverlust, Fehlversand oder verdächtige Zugriffe zu spät behandelt.
- Wenn Meldungen sanktionierend wirken, melden Personen Fehler oder Unsicherheiten gar nicht oder nur informell.
- Wenn Helpdesk, Führungskraft und Security unterschiedliche Wege nutzen, gehen Meldungen verloren oder werden falsch priorisiert.
- Wenn Ereignisse nicht sauber triagiert werden, bleiben mögliche Incidents, Datenschutzfragen oder externe Meldeentscheidungen unklar.
- Wenn aus Meldungen nicht gelernt wird, wiederholen sich Fehler in Prozessen, Tools oder Schulungen.

## Trigger

- Phishing-Verdacht, verdächtige Nachricht, ungewöhnlicher Login oder Malware-Hinweis.
- Verlust oder Diebstahl von Gerät, Ausweis, Token, Unterlagen oder Datenträger.
- Fehlversand, falsche Freigabe, versehentliche Veröffentlichung oder unbefugte Einsichtnahme.
- ungewöhnliches Systemverhalten, unbekannte Person in geschütztem Bereich oder verdächtige Anfrage.
- Sicherheitsfrage im Arbeitsalltag, bei der Beschäftigte unsicher sind.
- Onboarding, Awareness-Kampagne, Meldewegtest oder Rollenwechsel.
- Incident, Beinahevorfall, Auditfinding oder Review des Meldeprozesses.

## Rollen und Verantwortung

- **Beschäftigte und externe Mitarbeitende im Scope:** melden Verdachtsmomente, Fehler und Ereignisse schnell über definierte Wege.
- **Führungskräfte:** fördern meldefreundliche Kultur, blockieren Meldungen nicht und eskalieren bei Zielkonflikten.
- **Helpdesk / Service Desk:** nimmt Meldungen an, erfasst Mindestinformationen und leitet an Triage-Rollen weiter.
- **Security-/Incident-Rolle:** bewertet Ereignisse, priorisiert, koordiniert Eindämmung und entscheidet über Incident-Eskalation.
- **ISMS-Owner:** definiert Meldeprozess, Evidenzlogik, Trainingsbezug und Review.
- **Datenschutz / Legal:** prüft personenbezogene Datenschutz-, Rechts- oder Kommunikationsfragen.
- **Management:** entscheidet bei kritischen Incidents, Ressourcenbedarf, Kulturproblemen oder externen Kommunikationsfragen.

## Implementierung

### Minimalstart

Ziel: Jede Person im Scope weiß, was sie melden soll und über welchen Weg.

1. Ein zentraler Meldeweg wird festgelegt: E-Mail, Telefon, Ticket, Chatkanal oder Hotline mit klarer Zuständigkeit.
2. Kurze Beispiele erklären, was meldewürdig ist: Phishing, Verlust, Fehlversand, verdächtiger Zugriff, unbekannte Person, falsche Freigabe.
3. Onboarding und Awareness nennen den Meldeweg ausdrücklich.
4. Der Helpdesk oder die Security-Rolle nutzt eine einfache Triage-Checkliste.
5. Meldungen werden nachvollziehbar erfasst: Zeitpunkt, Melderrolle, Ereignistyp, Ersteinschätzung, nächster Schritt.
6. Kritische Meldungen werden an Incident Response, Datenschutz, Legal oder Management eskaliert.

Minimaler Nachweis:

- veröffentlichter Meldeweg,
- Onboarding- oder Awareness-Nachweis,
- Melde- oder Triage-Tickets,
- Eskalationsnachweise,
- Reviewnotiz zu Meldungen und Verbesserungen.

### Solide Praxis

Ziel: Meldungen werden einheitlich triagiert, zeitnah eskaliert und für Lernen genutzt.

1. Ereigniskategorien und Prioritäten werden definiert, ohne Beschäftigte mit Fachjargon zu überfordern.
2. Meldewege werden regelmäßig getestet, etwa mit einer Phishing-Übung oder einem Meldeweg-Drill.
3. Führungskräfte erhalten Leitlinien, Meldungen ernst zu nehmen und nicht informell zu lösen.
4. Datenschutz-, Legal-, BCM- und Kommunikations-Handoffs sind für bestimmte Ereignistypen beschrieben.
5. Lessons Learned aus Meldungen fließen in Awareness, technische Maßnahmen, Prozessänderungen oder Management Review.
6. Wiederholte Meldehemmnisse, lange Reaktionszeiten oder unklare Zuständigkeiten werden als Maßnahmen verfolgt.

### Fortgeschritten

Ziel: Die Melderoutine wird Teil eines belastbaren Sicherheitslagebilds und einer vertrauensbasierten Sicherheitskultur.

1. Meldekanäle, Ticketing, Incident Triage und Security Monitoring sind miteinander verbunden.
2. Kennzahlen betrachten nicht nur Anzahl der Meldungen, sondern Qualität, Reaktionszeit, Eskalationstreffer und Lernwirkung.
3. Hochrisikobereiche erhalten Szenarioübungen: Fehlversand, Ransomware-Verdacht, Social Engineering, physische Beobachtung.
4. Anonyme oder vertrauliche Hinweiswege werden geprüft, wenn Kultur, Hierarchie oder externe Rollen sonst Meldungen hemmen.
5. Management erhält entscheidungsfähige Informationen zu Meldekultur, Ressourcen, kritischen Mustern und Prozesslücken.

## Ablauf als Routine

1. **Ereignis bemerken:** Person sieht, verliert, erhält, versendet oder erlebt etwas Sicherheitsrelevantes.
2. **Sofort melden:** definierter Kanal wird genutzt; bei Unsicherheit gilt „lieber melden als abwarten“.
3. **Mindestinformationen erfassen:** was, wann, wo, betroffenes System oder Information, bereits unternommene Schritte.
4. **Triage durchführen:** Helpdesk oder Security bewertet Dringlichkeit, mögliche Auswirkungen und Handoffs.
5. **Eskalieren:** Incident Response, Datenschutz, Legal, Facility, HR, BCM oder Management werden bei Triggern einbezogen.
6. **Maßnahmen verfolgen:** Eindämmung, Rückfrage, Korrektur, Kommunikation oder technische Prüfung werden dokumentiert.
7. **Rückmeldung geben:** Melder oder Führungskraft erhalten passende Information, damit Vertrauen entsteht.
8. **Lernen:** Muster werden in Awareness, Prozessverbesserung, technische Kontrollen oder Managemententscheidungen übersetzt.

## Entscheidungen

- Welche Ereignisse müssen Beschäftigte immer melden?
- Welche Kanäle sind für dringende, vertrauliche oder außerhalb der Arbeitszeit auftretende Ereignisse geeignet?
- Welche Informationen dürfen vom Melder verlangt werden, ohne Meldungen zu erschweren?
- Wann wird eine Meldung zum Incident, Datenschutz-, Legal- oder Managementthema?
- Wie wird eine meldefreundliche, nicht strafende Kultur konkret umgesetzt?
- Welche Kennzahlen helfen, ohne personenbezogene Leistungs- oder Verhaltenskontrolle zu erzeugen?

## Evidenz

### Starke Evidenz

- veröffentlichter Meldeweg mit Zuständigkeit und Erreichbarkeit,
- Awareness- oder Onboarding-Nachweis zum Meldeprozess,
- Triage-Tickets mit Ereignistyp, Zeit, Bewertung, Entscheidung und Status,
- Eskalationsnachweise an Incident Response, Datenschutz, Legal oder Management,
- Ergebnisse von Meldewegtests oder Übungen,
- Lessons-Learned-Maßnahmen mit Owner und Frist,
- Managemententscheidung bei Ressourcen-, Kultur- oder Eskalationsproblemen.

### Schwache Evidenz

- Policy-Satz „Vorfälle sind zu melden“ ohne Kanal oder Beispiele,
- allgemeine Awareness-Folie ohne Nachweis des Meldewegs,
- E-Mail-Postfach ohne Triage- oder Verantwortungslogik,
- Meldestatistik ohne Bewertung, Reaktionszeit oder Maßnahmen,
- informelle Teams- oder Chatmeldungen ohne Nachverfolgung.

### Evidenzlücken

- externe Mitarbeitende kennen den Meldeweg nicht,
- keine Erreichbarkeit bei dringenden Ereignissen,
- keine dokumentierte Triage oder Eskalation,
- Datenschutz-/Legal-Handoffs werden nicht erkannt,
- keine Rückmeldung und kein Lernen aus Meldungen,
- Meldehemmnisse oder Angstkultur werden nicht adressiert.

## Wirksamkeitsprüfung

Prüffragen:

- Können Beschäftigte typische meldewürdige Ereignisse benennen?
- Ist der Meldeweg im Onboarding und Alltag sichtbar?
- Werden Meldungen zeitnah erfasst, triagiert und eskaliert?
- Gibt es Beispiele, in denen Meldungen zu Maßnahmen oder Lessons Learned geführt haben?
- Werden Fehlversand, Geräteverlust und Phishing zuverlässig erkannt und übergeben?
- Sind Datenschutz-, Legal- und Managemententscheidungen sauber vom operativen Triageprozess getrennt?
- Wird Meldekultur betrachtet, statt nur niedrige oder hohe Meldezahlen zu bewerten?

Mögliche Kennzahlen:

- Zeit von Ereignis bis Meldung,
- Zeit von Meldung bis Triage,
- Anteil Meldungen mit vollständiger Triage,
- Meldeweg-Testquote,
- wiederkehrende Ereignistypen,
- offene Lessons-Learned-Maßnahmen,
- Anteil externer Mitarbeitender mit Meldeweg-Onboarding.

## BSIG-/NIS2-Anschluss

Die Melderoutine ist anschlussfähig an NIS2-orientierte Themen wie Incident Handling, Cyberhygiene, Schulung, Governance, Melde- und Eskalationsfähigkeit sowie Managementverantwortung. Der konkrete Bezug, insbesondere zu möglichen externen Meldepflichten, muss organisationsspezifisch und menschlich geprüft werden.

Dieses Artefakt trifft keine rechtliche Bewertung, ob ein Ereignis meldepflichtig ist, und ersetzt keine Datenschutz- oder Rechtsprüfung.

## Grenzen

- Dieses Artefakt ist keine vollständige Incident-Response-Policy.
- Es ersetzt keine rechtliche oder datenschutzrechtliche Bewertung von Meldepflichten.
- Es darf nicht als Grundlage für personenbezogene Leistungs- oder Verhaltenskontrolle genutzt werden, ohne geeignete Klärung.
- Niedrige Meldezahlen belegen nicht automatisch Sicherheit; hohe Meldezahlen belegen nicht automatisch Unsicherheit.
- Es enthält keine ISO-27002-Texte und keine echten Incidentdaten.

## Handoffs

- **Incident-Handoff:** Verdacht auf Kompromittierung, Malware, unbefugten Zugriff, Datenabfluss oder aktive Ausnutzung.
- **Datenschutz-Handoff:** mögliche Verletzung des Schutzes personenbezogener Daten, Fehlversand personenbezogener Informationen oder unbefugte Einsichtnahme.
- **Legal-/Kommunikations-Handoff:** externe Kommunikation, Behörden-/Kundenkontakt, arbeitsrechtliche Fragen oder strittige Sachverhalte.
- **HR-Handoff:** Meldekultur, Schulung, Rollenpflichten, wiederholte Nichtmeldung oder Konflikte im Team.
- **Facility-Handoff:** physische Beobachtungen, verlorene Ausweise, unbekannte Personen oder Zutrittsereignisse.
- **BCM-/Krisen-Handoff:** Ereignisse mit möglicher Auswirkung auf kritische Leistungen oder Krisenorganisation.
- **Management-Handoff:** kritische Incidents, Ressourcenkonflikte, Kulturprobleme oder akzeptierte Restrisiken.
- **Audit-/Evidence-Handoff:** fehlende Triage, unklare Eskalation oder nicht nachvollziehbare Lessons Learned.

## Typische Fehler

- Der Meldeweg steht nur in einer Policy und ist im Alltag nicht präsent.
- Beschäftigte werden für Fehler beschämt und melden deshalb später oder gar nicht.
- Führungskräfte lösen Sicherheitsmeldungen informell, statt sie in die Triage zu geben.
- Phishing-Buttons existieren, aber Fehlversand, Geräteverlust oder physische Beobachtungen sind nicht abgedeckt.
- Meldungen werden gezählt, aber nicht ausgewertet oder verbessert.
- Datenschutz- und Legal-Fragen werden zu spät einbezogen.
- Externe Mitarbeitende und Dienstleister kennen den Meldeweg nicht.

## Fiktives Mini-Beispiel

Eine fiktive Mitarbeiterin erhält eine verdächtige E-Mail mit einem Link zu einem angeblichen Dokument. Im Onboarding hat sie gelernt, den Security-Meldekanal zu nutzen. Der Helpdesk erfasst die Meldung, Security prüft die Nachricht und erkennt eine laufende Phishing-Welle. Die Mail wird aus Postfächern entfernt, ein kurzer Warnhinweis wird veröffentlicht und im nächsten Awareness-Review wird das Beispiel als Szenario ergänzt.

Evidenz:

- Awareness-Nachweis zum Meldeweg,
- Triage-Ticket zur Meldung,
- Security-Analyse und Maßnahme,
- Kommunikationsnachweis zur Warnung,
- Lessons-Learned-Eintrag für Awareness-Update.
