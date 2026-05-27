
# A.5.5 — Kontakt zu zuständigen Behörden

## Zweck

Kontakt zu zuständigen Behörden stellt sicher, dass eine Organisation relevante öffentliche Stellen, Aufsichts- oder Meldestellen nicht erst im Ernstfall suchen muss. Ziel ist eine vorbereitete, freigegebene Kontakt- und Eskalationsroutine — ohne dabei rechtliche Meldepflichten vorschnell selbst zu bewerten.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der zuständige Behördenkontakte, Kommunikationswege, interne Freigaben und Human-Gates für behördliche Kommunikation gepflegt, getestet und bei Ereignissen aktiviert werden können.

## Typische Risiken

- Wenn Behördenkontakte erst während eines Sicherheitsereignisses recherchiert werden, gehen Zeit und Koordinationsfähigkeit verloren.
- Wenn unklar ist, wer extern kommunizieren darf, entstehen widersprüchliche oder nicht freigegebene Aussagen.
- Wenn rechtliche Bewertung, Datenschutz und Incident Response nicht verbunden sind, können Meldungen falsch priorisiert oder verspätet vorbereitet werden.
- Wenn Kontaktlisten veralten, erreichen dringende Informationen die falschen Stellen oder niemanden.
- Wenn Übungen Behördenkommunikation ausklammern, bleibt die Organisation im Ernstfall unsicher.
- Wenn echte Vorfalldaten unkontrolliert geteilt werden, können Vertraulichkeit, Datenschutz oder Ermittlungsinteressen beeinträchtigt werden.

## Trigger

- Sicherheitsereignis, Beinahevorfall, Krisenlage oder Verdacht auf meldepflichtigen Sachverhalt.
- Änderung regulatorischer Betroffenheit, Branche, Standort, Dienstleistung oder kritischer Prozesse.
- neue oder geänderte behördliche Kontaktwege, Portale, Meldeformate oder Ansprechpartner.
- Krisenübung, Incident-Tabletop oder Lessons Learned.
- Managemententscheidung zu externer Kommunikation oder Krisenorganisation.
- geplanter Review der Kontaktliste und Freigaberoutine.
- externe Anfrage einer Behörde oder öffentliche Warnung mit Organisationsbezug.

## Rollen und Verantwortung

- **Incident Manager / Security-Rolle:** erkennt mögliche Behördenrelevanz und startet interne Eskalation.
- **ISMS-Owner:** pflegt Kontakt- und Routinenlogik, Nachweise und Reviewtermine.
- **Legal / Compliance:** bewertet rechtliche Melde-, Auskunfts- oder Kommunikationsfragen.
- **Datenschutzrolle:** bewertet personenbezogene Aspekte und mögliche Datenschutzmeldungen.
- **Management / Krisenstab:** entscheidet externe Kommunikation, Freigaben, Ressourcen und Eskalation.
- **Kommunikation / PR:** stimmt Wortlaut, Timing und externe Anschlusskommunikation ab.
- **Fach- oder Service Owner:** liefert belastbare Fakten zu betroffenen Diensten, Kunden, Daten oder Auswirkungen.

## Implementierung

### Minimalstart

Ziel: Die Organisation weiß, wen sie im Ereignisfall intern einbindet und wo freigegebene Behördenkontakte liegen.

1. Relevante Behörden- und Meldestellen werden als Kontaktkategorien erfasst, nicht als Rechtsbewertung.
2. Für jede Kategorie wird festgelegt, wer intern die Bewertung und Freigabe übernimmt.
3. Eine Kontaktliste enthält offizielle Webseiten, Portale, Telefonnummern oder Postfächer sowie Reviewdatum.
4. Der Incident-Prozess enthält einen Stop-Punkt: mögliche Behördenrelevanz an Legal, Datenschutz und Management eskalieren.
5. Externe Kommunikation erfolgt nur über freigegebene Rollen.
6. Die Kontaktliste wird mindestens jährlich und nach Übungen oder Vorfällen geprüft.

Minimaler Nachweis:

- Behördenkontaktliste mit Quelle und Reviewdatum,
- interne Freigabe- und Eskalationsmatrix,
- Incident-Stop-Punkt für Behördenrelevanz,
- Reviewnotiz,
- Übungs- oder Vorfallprotokoll mit Lessons Learned.

### Solide Praxis

Ziel: Behördenkontakt ist in Incident, Krisenmanagement und Governance integriert.

1. Kontaktkategorien werden mit Szenarien verbunden: Cyberangriff, Datenschutzereignis, Ausfall kritischer Dienste, strafrechtlicher Verdacht, branchenspezifische Lage.
2. Melde- oder Auskunftsfragen werden als Legal-/Datenschutz-Human-Gate geführt.
3. Kommunikationsvorlagen enthalten nur Strukturfragen, keine ungeprüften Aussagen oder Rechtsclaims.
4. Übungen testen, ob interne Freigaben, Faktenlage und Kontaktwege funktionieren.
5. Behördliche Informationen, Warnungen oder Rückmeldungen werden in Risiko-, Incident- oder Maßnahmenroutinen zurückgeführt.
6. Kontaktlisten werden versioniert und mit Stellvertretungen gepflegt.

### Fortgeschritten

Ziel: Externe Schnittstellen werden als Teil des Lagebilds und der Krisenfähigkeit betrieben.

1. Behördenkontakte, CERT-/CSIRT-Informationen, Branchenwarnungen und Krisenkommunikation sind in ein Lagebild eingebunden.
2. Rollen können in Übungen unter Zeitdruck entscheiden, was intern zu bewerten, freizugeben und extern zu kommunizieren ist.
3. Faktenmanagement trennt bestätigte Informationen, Annahmen, offene Fragen und freigegebene Aussagen.
4. Management, Legal, Datenschutz, Kommunikation, Incident Response und BCM arbeiten mit abgestimmten Eskalationsstufen.
5. Nach Ereignissen werden Kontaktwege, Antwortzeiten, Entscheidungsqualität und Dokumentation reviewed.
6. Schnittstellen zu Dienstleistern berücksichtigen, wer Behördenkontakt unterstützt und welche Informationen bereitgestellt werden können.

## Ablauf als Routine

1. **Kontaktbasis pflegen:** relevante offizielle Kontaktquellen, Portale und interne Freigaberollen aktualisieren.
2. **Ereignis erkennen:** Incident, Ausfall, Anfrage oder Warnung kann Behördenrelevanz haben.
3. **Human-Gate auslösen:** Legal, Datenschutz, Management und Kommunikation einbinden, bevor externe Aussagen erfolgen.
4. **Faktenlage sichern:** betroffene Dienste, Zeiten, Auswirkungen, Datenarten, Maßnahmen und Unsicherheiten strukturieren.
5. **Entscheiden:** ob, wann, über welchen Kanal und mit welchem freigegebenen Inhalt kommuniziert wird.
6. **Kommunizieren:** nur über autorisierte Rollen und nachvollziehbare Kanäle.
7. **Dokumentieren:** Kontaktversuch, Inhalte, Freigaben, Zeitpunkte und Rückmeldungen festhalten.
8. **Nachbereiten:** Lessons Learned in Kontaktliste, Incident-Prozess, Übungen und Management Review übernehmen.

## Entscheidungen

- Welche Behörden- oder Meldestellenkategorien sind für die Organisation relevant zu prüfen?
- Wer darf externe Behördenkommunikation freigeben und durchführen?
- Welche Ereignisse lösen Legal-, Datenschutz-, Management- oder Krisenstab-Handoff aus?
- Welche Fakten müssen vor externer Kommunikation mindestens belastbar sein?
- Wie werden Annahmen, Unsicherheiten und noch ungeprüfte Informationen behandelt?
- Wie werden behördliche Rückmeldungen in Maßnahmen und Risikoarbeit überführt?

## Evidenz

### Starke Evidenz

- aktuelle Kontaktliste mit offiziellen Quellen, Owner und Reviewdatum,
- Eskalationsmatrix für Behördenrelevanz und externe Freigaben,
- Incident- oder Krisenprozess mit Behörden-Human-Gate,
- Übungsprotokoll mit getesteter Kontakt- und Freigaberoutine,
- Vorfallakte mit Zeitpunkten, Freigaben, Kontaktwegen und Rückmeldungen,
- Lessons Learned mit Prozess- oder Kontaktlistenänderungen,
- Managemententscheidung zu externer Kommunikation.

### Schwache Evidenz

- unkommentierte Linkliste ohne Owner oder Reviewdatum,
- allgemeiner Satz „Behörden werden informiert“ ohne Freigabeweg,
- veraltete Telefonnummern in einem Notfallordner,
- Kommunikationsvorlagen ohne Legal-/Datenschutzprüfung,
- Übung ohne externe Kommunikationsentscheidung.

### Evidenzlücken

- keine interne Freigaberolle für Behördenkontakt,
- keine Verbindung zum Incident- oder Krisenprozess,
- unklare Trennung zwischen Fakten, Annahmen und freigegebenen Aussagen,
- Kontaktliste nicht auf offizielle Quellen zurückführbar,
- Dienstleister können relevante Fakten nicht rechtzeitig liefern,
- externe Anfrage wird ohne Dokumentation beantwortet.

## Wirksamkeitsprüfung

Prüffragen:

- Ist klar, welche Rolle mögliche Behördenrelevanz erkennt und eskaliert?
- Sind Kontaktquellen aktuell und auf offizielle Stellen zurückführbar?
- Werden Legal, Datenschutz, Management und Kommunikation rechtzeitig eingebunden?
- Kann die Organisation Faktenlage und Freigaben nachvollziehbar dokumentieren?
- Wurde die Kontakt- und Kommunikationsroutine geübt?
- Fließen Rückmeldungen oder Warnungen in Risiko- und Maßnahmenarbeit ein?

Mögliche Kennzahlen:

- Aktualität der Kontaktliste,
- Anteil Übungen mit Behördenkommunikationsszenario,
- Zeit bis interne Eskalation bei möglicher Behördenrelevanz,
- offene Lessons Learned aus Kommunikationsübungen,
- externe Anfragen mit vollständiger Dokumentation,
- Dienstleisterkontakte mit definiertem Faktenlieferweg.

## BSIG-/NIS2-Anschluss

Behördenkontakt ist anschlussfähig an NIS2-orientierte Incident-Fähigkeit, Krisenkommunikation, Managementaufsicht, Lagebild und mögliche Melde- oder Informationsprozesse. Der konkrete Bezug muss organisationsspezifisch durch Legal, Datenschutz und zuständige Verantwortliche geprüft werden.

Dieses Artefakt bewertet keine Meldepflicht, keine Frist und keine Zuständigkeit verbindlich.

## Grenzen

- Keine Rechtsberatung und keine verbindliche Meldepflichtbewertung.
- Keine Datenschutzberatung oder Bewertung von Datenschutzverletzungen.
- Keine Vorlage für echte Behördenmeldungen mit Organisationsdaten.
- Keine Zertifizierungs- oder Konformitätszusage.
- Keine Weitergabe vertraulicher, personenbezogener oder ermittlungsrelevanter Informationen ohne Human Review.

## Handoffs

- **Incident-Handoff:** mögliche Behördenrelevanz, strafrechtlicher Verdacht, erheblicher Sicherheitsvorfall oder externe Anfrage.
- **Legal-Handoff:** Meldepflichten, Auskunftspflichten, Strafanzeige, Vertrags- oder Regulierungsfragen.
- **Datenschutz-Handoff:** personenbezogene Daten, mögliche Verletzung des Schutzes personenbezogener Daten, Betroffenenkommunikation.
- **Management-/Krisenstab-Handoff:** externe Kommunikation, Ressourcen, Lageentscheidung, Reputations- oder Betriebswirkung.
- **Kommunikations-Handoff:** abgestimmte Aussagen, Medien- oder Kundenanschlusskommunikation.
- **Vendor-Handoff:** Fakten aus Dienstleisterbetrieb, Managed Service, Cloud oder Drittprodukt.
- **Audit-/Evidence-Handoff:** Nachweise zu Freigaben, Kontaktwegen und Lessons Learned.

## Typische Fehler

- Behördenkontakt wird erst im Incident recherchiert.
- Security kommuniziert extern, ohne Legal, Datenschutz oder Management einzubinden.
- Kontaktlisten enthalten private Notizen statt offizielle Quellen.
- Meldepflichten werden im Technikteam spekulativ bewertet.
- Kommunikationsvorlagen enthalten zu konkrete Aussagen, bevor Fakten gesichert sind.
- Dienstleister liefern keine verwertbaren Zeitpunkte oder Betroffenheitsinformationen.
- Übungen testen Technik, aber nicht Entscheidung und externe Kommunikation.

## Fiktives Mini-Beispiel

Ein fiktiver Cloud-Dienstleister übt einen Ransomware-Verdacht. Während der Tabletop-Übung erkennt der Incident Manager mögliche Behördenrelevanz und löst den internen Stop-Punkt aus. Legal und Datenschutz prüfen die Lage, das Management entscheidet, vorerst nur Fakten zu sammeln und keine externe Meldung ohne weitere Bewertung abzugeben. Die Kontaktliste wird aktualisiert, weil ein offizielles Portal veraltet verlinkt war.

Evidenz:

- Übungsprotokoll mit ausgelöstem Behörden-Handoff,
- aktualisierte Kontaktliste mit offizieller Quelle,
- Legal-/Datenschutz-Prüfauftrag,
- Managemententscheidung zur Kommunikationsfreigabe,
- Lessons-Learned-Maßnahme für Faktenmanagement.
