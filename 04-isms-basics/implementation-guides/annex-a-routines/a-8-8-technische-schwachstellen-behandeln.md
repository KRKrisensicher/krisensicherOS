
# A.8.8 — Technische Schwachstellen behandeln

## Zweck

Schwachstellenbehandlung sorgt dafür, dass bekannte technische Verwundbarkeiten erkannt, bewertet, priorisiert, behandelt und nachverfolgt werden. Der Wert liegt nicht im Scanbericht, sondern in der Fähigkeit, aus technischen Findings risikobasierte Entscheidungen und wirksame Maßnahmen zu machen.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der Schwachstellen aus Scans, Herstellerhinweisen, Threat Intelligence, Penetrationstests, Bug Reports, Incident Lessons Learned oder Lieferantenmeldungen in ein priorisiertes Maßnahmen- und Entscheidungsmanagement überführt werden.

## Typische Risiken

- Wenn bekannte Schwachstellen nicht erkannt oder nicht bewertet werden, bleiben ausnutzbare Angriffsflächen offen.
- Wenn Scanberichte nicht priorisiert werden, ertrinken Teams in Findings und kritische Lücken bleiben liegen.
- Wenn Asset Owner fehlen, können Schwachstellen keinem Risiko, System oder Service zugeordnet werden.
- Wenn Patches ohne Change- und Verfügbarkeitsbewertung eingespielt werden, entstehen Betriebsstörungen.
- Wenn Ausnahmen nicht dokumentiert werden, wird „nicht gepatcht“ unsichtbar.
- Wenn Lieferantenmeldungen nicht verarbeitet werden, bleiben Drittkomponenten und SaaS-Abhängigkeiten blinde Flecken.

## Trigger

- neuer Schwachstellenscan oder Penetrationstest.
- Herstellerhinweis, CVE-Meldung, CERT-/CSIRT-Hinweis oder Threat-Intelligence-Treffer.
- neue oder geänderte Systeme, Anwendungen, Container, Bibliotheken oder Cloud-Ressourcen.
- Sicherheitsereignis oder Verdacht auf Ausnutzung.
- Lieferantenmeldung zu Produkt- oder Diensteschwachstellen.
- regulärer Patch- oder Vulnerability-Review.
- Auditfinding, Kundenanforderung oder Managementfrage zu technischer Risikolage.

## Rollen und Verantwortung

- **Asset Owner / Service Owner:** bewertet geschäftliche Kritikalität und akzeptiert oder eskaliert Restrisiken.
- **IT-/Plattform Owner:** betreibt Scans, Patches, Konfigurationen und technische Maßnahmen.
- **Entwicklung / Product Owner:** bewertet Anwendungscode, Bibliotheken, Images und Releaseabhängigkeiten.
- **Security-Rolle / ISMS-Owner:** definiert Bewertungslogik, Fristen, Eskalationswege und Reporting.
- **Change Owner:** koordiniert Tests, Rollout und Betriebsrisiken.
- **Lieferantenmanagement:** verfolgt Schwachstellen in externen Produkten oder Diensten.
- **Management:** entscheidet bei nicht tragbaren Restrisiken, Ressourcenmangel oder akzeptierten Ausnahmen.

## Implementierung

### Minimalstart

Ziel: kritische Schwachstellen sichtbar, zugeordnet und nachverfolgt behandeln.

1. Kritische Assets im ISMS-Scope werden benannt: Internet-exponierte Systeme, zentrale Identitätsdienste, Kernanwendungen, produktive Server, wichtige SaaS-Dienste.
2. Für diese Assets gibt es Owner und technische Verantwortliche.
3. Schwachstellenquellen werden festgelegt: mindestens Herstellerhinweise, zentrale Scans oder Dienstleistermeldungen.
4. Findings werden in einem Maßnahmenlog erfasst: Asset, Schwachstelle, Bewertung, Owner, Entscheidung, Frist, Status.
5. Kritische Findings werden zeitnah triagiert und bei Bedarf eskaliert.
6. Nicht behobene Findings erhalten Ausnahme, Kompensationsmaßnahme oder Risikoentscheidung.

Minimaler Nachweis:

- Assetliste im Scope,
- Schwachstellenlog oder Ticketliste,
- Bewertungs- und Priorisierungsentscheidung,
- Nachweis behobener Findings,
- Ausnahme- oder Risikoakzeptanz bei offenen kritischen Findings.

### Solide Praxis

Ziel: Schwachstellenbehandlung wird risikobasiert, wiederholbar und mit Change Management verbunden.

1. Schwachstellen werden nach technischer Kritikalität, Exposition, Assetkritikalität, Ausnutzbarkeit und vorhandenen Kompensationsmaßnahmen bewertet.
2. Behandlungsfristen werden nach Risikoklasse definiert.
3. Patches und Konfigurationsänderungen laufen über einen angemessenen Change-Prozess.
4. False Positives, akzeptierte Risiken und technisch nicht behebbare Findings werden nachvollziehbar dokumentiert.
5. Wiederholte Findings führen zu Ursachenanalyse: fehlender Patchprozess, veraltete Plattform, unsichere Architektur, mangelnde Zuständigkeit.
6. Lieferanten- und SaaS-Schwachstellen werden über Vertrags-/Servicekontakte verfolgt.
7. Status und Top-Risiken fließen in ISMS-Review und Management Review.

Starke Evidenz:

- definierte Bewertungs- und Fristenlogik,
- regelmäßige Scan- oder Meldungsnachweise,
- Tickets mit Owner, Frist und Status,
- Patch-/Change-Nachweise,
- Re-Scan oder Validierungsnachweis,
- Ausnahmeentscheidungen mit Ablaufdatum,
- Managemententscheidung bei dauerhaften Restrisiken.

### Fortgeschritten

Ziel: Schwachstellenmanagement wird in Architektur, Entwicklung, Betrieb und Lagebild integriert.

1. Assetinventar, CMDB, Cloudinventar, Container-/Dependency-Scanning und Ticketing sind miteinander verbunden.
2. Exposition und Business-Kritikalität beeinflussen Priorisierung automatisch oder halbautomatisch.
3. Kritische Schwachstellen werden mit Threat Intelligence, aktiver Ausnutzung und Incident-Triage gekoppelt.
4. Patch- und Remediation-SLAs werden überwacht und berichtet.
5. Secure Development, Baseline-Konfigurationen und Architekturentscheidungen reduzieren wiederkehrende Findings.
6. Lessons Learned aus Incidents und Penetrationstests führen zu strukturellen Verbesserungen.
7. Management sieht nicht nur Anzahl der Findings, sondern Risikoentwicklung, überfällige kritische Lücken, technische Schulden und Ressourcenbedarf.

## Ablauf als Routine

1. **Schwachstelle wird bekannt:** Scan, Meldung, Advisory, Incident, Lieferant oder Test.
2. **Zuordnen:** betroffenes Asset, Owner, Service, Datenklasse und Exposition bestimmen.
3. **Bewerten:** technische Kritikalität, Ausnutzbarkeit, Business-Auswirkung und vorhandene Schutzmaßnahmen einordnen.
4. **Priorisieren:** Frist, Behandlungsweg und Eskalationsbedarf festlegen.
5. **Behandeln:** Patch, Konfiguration, Deaktivierung, Segmentierung, Monitoring, Workaround oder Architekturmaßnahme.
6. **Validieren:** Re-Scan, Test, Herstellerbestätigung oder technischer Nachweis.
7. **Dokumentieren:** Status, Entscheidung, Evidenz und Restrisiko festhalten.
8. **Eskalieren:** überfällige kritische Findings, nicht behebbare Schwachstellen oder Ressourcenprobleme ins Management Review geben.
9. **Lernen:** Ursachen und Muster in Architektur, Betrieb, Beschaffung oder Entwicklung zurückspielen.

## Entscheidungen

- Welche Assets werden zuerst und regelmäßig geprüft?
- Welche Bewertungslogik verbindet technische Schwere mit Geschäftsrisiko?
- Welche Fristen gelten für kritische, hohe, mittlere und niedrige Findings?
- Wann ist ein Workaround ausreichend, wann braucht es Patch oder Abschaltung?
- Wer darf eine Ausnahme akzeptieren und wie lange?
- Wann wird eine Schwachstelle zum Incident oder Managementthema?
- Wie werden Lieferanten- oder SaaS-Schwachstellen nachverfolgt?

## Evidenz

### Starke Evidenz

- aktueller Scope kritischer Assets,
- Schwachstellenquelle mit Datum und Abdeckung,
- priorisierte Finding-Liste mit Ownern,
- Tickets mit Behandlungsschritt und Frist,
- technische Nachweise für Patch, Konfigurationsänderung oder Kompensation,
- Re-Scan oder Validierung,
- Ausnahme mit Risikoentscheidung und Ablaufdatum,
- Managemententscheidung bei nicht behobenen kritischen Risiken.

### Schwache Evidenz

- Scanbericht ohne Triage,
- CVSS-Wert ohne Asset- oder Expositionsbewertung,
- Patchpolicy ohne Nachweis der Umsetzung,
- Ticketliste ohne Validierung,
- monatliche Finding-Anzahl ohne Risikokontext,
- pauschale Aussage „vom Dienstleister betreut“ ohne Rückmeldung oder SLA.

### Evidenzlücken

- unbekannte Assetabdeckung,
- keine Owner für Findings,
- keine Fristen oder Eskalationsregeln,
- keine Behandlung von Ausnahmen,
- keine Lieferantenverfolgung,
- keine Validierung nach Behebung,
- kritische Altfindings ohne Managemententscheidung.

## Wirksamkeitsprüfung

Prüffragen:

- Sind die wichtigsten Assets im Schwachstellenprozess abgedeckt?
- Können kritische Findings einem Owner und einer Frist zugeordnet werden?
- Werden Schwachstellen nach Geschäftsrisiko und Exposition priorisiert?
- Gibt es Nachweise, dass Behebungen validiert wurden?
- Werden überfällige kritische Findings eskaliert?
- Werden Ursachen wiederkehrender Findings strukturell behandelt?
- Sind Lieferanten- und SaaS-Schwachstellen im Prozess sichtbar?

Mögliche Kennzahlen:

- Abdeckung kritischer Assets,
- offene kritische Findings,
- überfällige Findings nach Risikoklasse,
- mittlere Behebungszeit je Kritikalität,
- Ausnahmequote und überfällige Ausnahmen,
- Reopen-Rate nach Validierung,
- wiederkehrende Findings pro Plattform oder Team.

## BSIG-/NIS2-Anschluss

Schwachstellenbehandlung ist anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Cyberhygiene, sichere Beschaffung und Entwicklung, Incident-Prävention, Monitoring und Aufrechterhaltung sicherer Dienste. Für betroffene Organisationen sollte der konkrete Bezug im Anforderungsregister, in Risikoanalysen und im Management Review geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung von Meldepflichten, Betroffenheit oder Nachweispflichten.

## Grenzen

- Dieses Artefakt ist keine technische Scannerempfehlung und keine Hardening-Baseline.
- Es ersetzt keine Produkt-, Cloud-, Netzwerk- oder Anwendungssicherheitsanalyse.
- CVSS oder Tool-Schweregrade ersetzen keine organisationsspezifische Risikobewertung.
- Keine Rechtsberatung, keine Datenschutzberatung, keine Zertifizierungszusage.
- Keine ISO-27002-Texte oder vertraulichen Schwachstellendetails in öffentlichen Beispielen.

## Handoffs

- **Incident-Handoff:** aktive Ausnutzung, Kompromittierungsverdacht, kritische exponierte Schwachstelle.
- **Change-Handoff:** Patch, Konfigurationsänderung, Testbedarf, Rollback-Plan, Wartungsfenster.
- **Entwicklungs-Handoff:** Code-, Dependency-, Container- oder CI/CD-Findings.
- **Lieferanten-Handoff:** Drittprodukt, SaaS, Managed Service, fehlende Herstellerinformation.
- **BCM-Handoff:** Behebung gefährdet Verfügbarkeit kritischer Dienste oder erfordert Notfallentscheidung.
- **Management-Handoff:** Ressourcenmangel, überfällige kritische Findings, akzeptiertes Restrisiko, technische Schulden.
- **Datenschutz-Handoff:** Schwachstelle betrifft personenbezogene Daten oder mögliche Verletzung des Schutzes personenbezogener Daten.
- **Audit-/Evidence-Handoff:** fehlende Abdeckung, fehlende Validierung oder unklare Ausnahmebehandlung.

## Typische Fehler

- Scanberichte werden erzeugt, aber nicht verantwortet.
- Priorisierung folgt nur Toolscore, nicht Assetkritikalität oder Exposition.
- Findings werden geschlossen, ohne Behebung zu validieren.
- Ausnahmen laufen unbegrenzt.
- Kritische Legacy-Systeme werden aus dem Scan ausgenommen, ohne Risikoentscheidung.
- Lieferantenrisiken bleiben außerhalb des Schwachstellenprozesses.
- Management sieht Volumenkennzahlen, aber keine entscheidungsfähigen Restrisiken.
- Patchen wird vom Change-Prozess entkoppelt und erzeugt Betriebsstörungen.

## Fiktives Mini-Beispiel

Ein fiktiver Betreiber eines Kundenportals erhält einen Herstellerhinweis zu einer aktiv ausgenutzten Schwachstelle in einer Webkomponente. Der Plattform Owner ordnet das betroffene System als internet-exponiert und kritisch ein. Ein Ticket wird mit hoher Priorität erstellt, ein Wartungsfenster abgestimmt und der Patch eingespielt. Ein Re-Scan bestätigt die Behebung. Für ein zweites internes System ist der Patch nicht sofort möglich; der Service Owner dokumentiert eine befristete Ausnahme mit zusätzlicher Netzwerkbeschränkung und Wiedervorlage im Management Review.

Evidenz:

- Herstellerhinweis als Referenz,
- betroffene Assetliste,
- priorisierte Tickets,
- Change- und Patchnachweis,
- Re-Scan,
- Ausnahme mit Kompensationsmaßnahme und Ablaufdatum,
- Management-Review-Punkt für Restrisiko.
