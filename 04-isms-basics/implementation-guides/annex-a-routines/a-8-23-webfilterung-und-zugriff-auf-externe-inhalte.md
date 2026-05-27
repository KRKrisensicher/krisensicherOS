
# A.8.23 — Webfilterung und Zugriff auf externe Inhalte

## Zweck

Webfilterung und gesteuerter Zugriff auf externe Inhalte reduzieren Risiken durch schädliche Webseiten, ungeeignete Downloads, Phishing-Ziele, betrügerische Dienste und nicht freigegebene Cloud-/KI- oder Austauschplattformen. Die Routine verbindet technische Filterung mit klarer Entscheidung: Was wird blockiert, was wird erlaubt, wer entscheidet Ausnahmen und wie werden Treffer genutzt?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Routine für Webzugriffe und externe Inhalte. Kategorien, Schutzmechanismen, Ausnahmen, Logging, Datenschutzgrenzen, Nutzerkommunikation, Incident-Handoffs und Reviews sind geregelt, ohne pauschal Arbeitsfähigkeit oder legitime Recherche zu blockieren.

## Typische Risiken

- Wenn schädliche oder betrügerische Webseiten erreichbar bleiben, können Malware, Zugangsdatenabfluss oder Social Engineering erleichtert werden.
- Wenn Downloads aus unbekannten Quellen ungeprüft erfolgen, können Endgeräte, Server oder Entwicklungsumgebungen kompromittiert werden.
- Wenn Schatten-Cloud-Dienste oder nicht freigegebene KI-/Dateiaustauschdienste genutzt werden, können Informationen unkontrolliert abfließen.
- Wenn Webfilter nur technisch aktiv sind, aber Ausnahmen und Reviews fehlen, entstehen Umgehungen oder dauerhafte Fehlfreigaben.
- Wenn Weblogs personenbezogen ausgewertet werden, ohne Datenschutzklärung, entstehen zusätzliche Governance- und Vertrauensprobleme.

## Trigger

- Einführung oder Änderung von Proxy, DNS-Filter, Secure Web Gateway, Browser-Policy, EDR-Webschutz oder Cloud Access Security.
- neuer externer Webdienst, Cloud-Dienst, KI-Dienst, Downloadquelle oder Fachanwendung.
- Phishing-Welle, Malwarefund, Incident, auffälliger Webzugriff oder Threat-Intelligence-Hinweis.
- Nutzerantrag auf Freischaltung, Blockierungsbeschwerde oder Geschäftsbedarf für externe Inhalte.
- Änderung von Datenklassen, Arbeitsmodellen, Entwicklungsprozessen oder Lieferantenkanälen.
- turnusmäßiger Review von Kategorien, Ausnahmen, Logs und Wirksamkeit.

## Rollen und Verantwortung

- **IT-/Security-Betrieb:** betreibt Filtertechnik, Kategorien, Policies, technische Ausnahmen und Monitoring.
- **Service Owner / Fachbereich:** begründet legitime Geschäftsbedarfe und bewertet Auswirkungen von Blockierungen.
- **ISMS-Owner / Security-Rolle:** definiert Risikologik, Ausnahmeprozess, Review und Handoff in Incident Response.
- **Datenschutz / Legal:** prüfen personenbezogene Logauswertung, Inhaltsinspektion, Beschäftigtenbezug und Nutzungsregelungen.
- **HR / Kommunikation:** unterstützt klare Nutzerinformation und Schulungsbezug, soweit erforderlich.
- **Management:** entscheidet bei Zielkonflikten zwischen Arbeitsfähigkeit, Sicherheitsniveau, Datenschutzgrenzen und Ressourcen.

## Implementierung

### Minimalstart

Ziel: riskante Webzugriffe reduzieren und Ausnahmen steuerbar machen.

1. Die Organisation legt fest, welche Schutzmechanismen für Standardendgeräte und kritische Nutzergruppen gelten.
2. Risikokategorien werden definiert, zum Beispiel bekannte Malware-/Phishing-Ziele, neu registrierte Domains, unerwünschte Downloads oder nicht freigegebene Datenaustauschdienste.
3. Es gibt einen einfachen Freigabeprozess für blockierte Seiten oder Dienste: Antrag, Begründung, Owner, Laufzeit, Entscheidung.
4. Kritische Treffer werden an Incident Triage oder Security-Betrieb übergeben.
5. Nutzer erhalten eine verständliche Information, warum blockiert wird und wie sie legitime Freigaben beantragen.
6. Datenschutzgrenzen für Logauswertungen werden vor personenbezogenen Analysen geklärt.

Minimaler Nachweis:

- Webfilter-/Browser-Policy oder Betriebsvorgabe,
- Liste aktiver Kategorien oder Schutzregeln,
- Ausnahme- und Freigabetickets,
- Nachweis Nutzerinformation,
- Incident-Tickets aus kritischen Treffern,
- Datenschutz-/Legal-Reviewpunkt bei Logauswertungen.

### Solide Praxis

Ziel: Webzugriffe werden risikobasiert, nachvollziehbar und mit Incident-Fähigkeit gesteuert.

1. Filterkategorien werden nach Risiko, Arbeitsbedarf und Nutzergruppen differenziert.
2. Ausnahmen werden befristet, fachlich begründet und regelmäßig reviewed.
3. Downloads, Makros, Skripte, Browser-Erweiterungen oder Entwicklerquellen werden gesondert betrachtet, wenn sie erhöhtes Risiko erzeugen.
4. Sicherheitsmeldungen aus Webfiltern fließen in Incident Triage, Awareness und Schwachstellenmanagement.
5. Neue Cloud-, KI- oder Dateiaustauschdienste werden mit Datenklasse, Zugriffsschutz und Lieferantenbezug geprüft.
6. Reporting zeigt Muster, blockierte Risikokategorien, Ausnahmequalität und offene Entscheidungen, nicht einzelne Personen ohne geklärte Grundlage.

Starke Evidenz:

- dokumentierte Kategorie- und Ausnahmelogik,
- Freigabetickets mit Zweck, Laufzeit und Entscheidung,
- Reviewprotokolle zu Ausnahmen und Fehlblockierungen,
- Incident- oder Alertnachweise aus kritischen Treffern,
- Kommunikations- oder Awareness-Nachweise,
- Datenschutzklärung für personenbezogene oder inhaltsnahe Auswertungen.

### Fortgeschritten

Ziel: Webfilterung wird mit Risiko-, Daten- und Detektionslogik verbunden.

1. Webzugriffe werden mit Endpoint-, Identitäts-, E-Mail-, DNS- und Cloud-Signalen korreliert, soweit zulässig und verhältnismäßig.
2. Hochrisikogruppen oder privilegierte Rollen erhalten stärkere Schutzprofile und engere Ausnahmeprüfung.
3. Nicht freigegebene Cloud-/KI-Dienste werden über einen geregelten Freigabeprozess in sichere Nutzungsalternativen überführt.
4. Threat Intelligence und Incident Lessons Learned aktualisieren Kategorien und Blocklisten.
5. Management erhält entscheidungsfähige Kennzahlen zu Ausnahmequote, kritischen Treffern, Schatten-IT-Mustern, Fehlblockierungen und Datenschutz-/Akzeptanzthemen.

## Ablauf als Routine

1. **Signal oder Bedarf entsteht:** Blockierung, Freigabeantrag, Threat-Hinweis, Incident oder neuer Dienst.
2. **Einordnen:** URL/Dienst, Kategorie, Nutzergruppe, Datenklasse, Geschäftsbedarf und Risiko bewerten.
3. **Entscheiden:** blockieren, erlauben, befristen, alternative Lösung anbieten oder eskalieren.
4. **Technisch umsetzen:** Kategorie, Policy, Ausnahme, Browserregel oder DNS-/Proxy-Konfiguration anpassen.
5. **Kommunizieren:** Antragsteller oder betroffene Gruppe über Entscheidung, Begründung und Laufzeit informieren.
6. **Überwachen:** kritische Treffer an Incident Triage geben und Muster prüfen.
7. **Reviewen:** Ausnahmen, Fehlblockierungen, neue Risikokategorien und Schatten-IT-Hinweise regelmäßig bewerten.
8. **Verbessern:** Policies, Awareness, Tooling oder freigegebene Alternativen anpassen.

## Entscheidungen

- Welche Kategorien werden standardmäßig blockiert und welche nur überwacht?
- Welche Rollen oder Systeme benötigen strengere Webschutzprofile?
- Wer darf Ausnahmen genehmigen und für welche Dauer?
- Wann ist eine Freigabe ein Sicherheits-, Datenschutz-, Einkaufs- oder Managementthema?
- Welche Logauswertungen sind zulässig und notwendig?
- Wie wird zwischen Arbeitsfähigkeit, Recherchefreiheit, Datenschutz und Sicherheitsniveau abgewogen?

## Evidenz

### Starke Evidenz

- Webfilter- oder Browser-Sicherheitsvorgabe mit Owner und Reviewdatum,
- aktive Kategorie-/Policy-Übersicht,
- Ausnahmeentscheidungen mit Zweck, Laufzeit und fachlichem Owner,
- Reviewprotokoll zu Ausnahmen, Fehlblockierungen und Risikotreffern,
- Incident-Tickets oder Alerts aus Webschutzsignalen,
- Nachweis über Nutzerkommunikation und Meldeweg,
- Datenschutz-/Legal-Klärung für personenbezogene Auswertungen.

### Schwache Evidenz

- Screenshot eines Filterdashboards ohne Entscheidungslogik,
- pauschale Blockliste ohne Geschäftsbezug,
- Ausnahmeliste ohne Ablaufdatum,
- hohe Blockierungszahl ohne Auswertung oder Maßnahmen,
- Nutzerinformation ohne Freigabe- oder Eskalationsweg.

### Evidenzlücken

- keine Owner für Kategorien oder Ausnahmen,
- unklare Behandlung von nicht freigegebenen Cloud-/KI-Diensten,
- kritische Webtreffer ohne Incident-Handoff,
- personenbezogene Loganalyse ohne Datenschutzklärung,
- lokale Browser- oder Entwicklerumgehungen ohne Review,
- dauerhafte Whitelists ohne Wiedervorlage.

## Wirksamkeitsprüfung

Prüffragen:

- Sind Webschutzprofile für relevante Nutzergruppen und Endgeräte aktiv?
- Werden Ausnahmen fachlich begründet, befristet und reviewed?
- Führen kritische Treffer zu Incident Triage oder anderen Maßnahmen?
- Werden Fehlblockierungen und Arbeitsfähigkeitsprobleme sichtbar behandelt?
- Sind Datenschutzgrenzen für Logging und Auswertung geklärt?
- Gibt es einen Umgang mit Schatten-Cloud-, KI- und Downloadrisiken?

Mögliche Kennzahlen:

- Anzahl kritischer Webschutztreffer nach Kategorie,
- Ausnahmequote und überfällige Ausnahmen,
- Zeit bis Entscheidung über Freigabeanträge,
- wiederholte Treffer auf Phishing-/Malware-Kategorien,
- Fehlblockierungsrate oder Beschwerden,
- nicht freigegebene Cloud-/KI-Dienste im Review.

## BSIG-/NIS2-Anschluss

Webfilterung und gesteuerter Zugriff auf externe Inhalte sind anschlussfähig an NIS2-orientierte Themen wie Cyberhygiene, Malware- und Phishing-Prävention, Incident Handling, Zugriffsschutz, Datenabflussrisiken, Schulung und sichere Nutzung externer Dienste. Die konkrete Einordnung sollte organisationsspezifisch im Anforderungsregister und Datenschutz-/Risikoreview erfolgen.

Dieses Artefakt ersetzt keine rechtliche, arbeitsrechtliche oder datenschutzrechtliche Bewertung.

## Grenzen

- Webfilterung ersetzt keine Awareness, E-Mail-Sicherheit, Endpoint-Schutz, Patchmanagement oder DLP-Governance.
- Inhaltsinspektion und personenbezogene Logauswertung können rechtlich und datenschutzrechtlich sensibel sein.
- Zu harte Blockierung kann Umgehungen und Schatten-IT fördern.
- Dieses Artefakt ist keine Empfehlung für bestimmte Filterprodukte oder Kategorienanbieter.
- Keine Zertifizierungszusage und keine Normtextübernahme.

## Handoffs

- **Incident-Handoff:** Malware-/Phishing-Treffer, Credential-Abflussverdacht, auffällige Download- oder C2-Muster.
- **Datenschutz-/Legal-Handoff:** personenbezogene Logs, Inhaltsinspektion, Beschäftigtenbezug, Nutzungsregelung oder Monitoring.
- **Einkauf-/Lieferanten-Handoff:** neuer Cloud-, KI-, Download- oder Austauschdienst mit Geschäftsbedarf.
- **Awareness-Handoff:** wiederholte Phishing-Klicks, unsichere Downloadmuster, unklare Nutzerkommunikation.
- **Change-Handoff:** neue Filterprofile, Browserrichtlinien, Proxy-/DNS-Änderungen.
- **Management-Handoff:** Zielkonflikt zwischen Arbeitsfähigkeit, Datenschutz, Sicherheitsniveau und Kosten.
- **Audit-/Evidence-Handoff:** fehlende Ausnahmebelege, unklare Reviews oder nicht nachvollziehbare Logauswertungen.

## Typische Fehler

- Filtertechnik wird eingeschaltet, aber niemand entscheidet Kategorien und Ausnahmen.
- Whitelists wachsen dauerhaft und werden nie bereinigt.
- Weblogs werden personenbezogen ausgewertet, ohne vorherige Klärung.
- Blockierungen erzeugen Frust, weil ein legitimer Freigabeprozess fehlt.
- Kritische Treffer bleiben im Tool und erreichen Incident Response nicht.
- Nicht freigegebene Cloud- oder KI-Dienste werden nur blockiert, ohne sichere Alternativen zu klären.
- Reporting zählt Blockierungen, aber zeigt keine Risiko- oder Entscheidungswirkung.

## Fiktives Mini-Beispiel

Ein fiktiver Projektbereich möchte einen externen Dateiaustauschdienst nutzen. Der Webfilter blockiert den Dienst wegen unklarer Datenverarbeitung. Der Fachbereich stellt einen Freigabeantrag mit Zweck und Datenklasse. Datenschutz und Einkauf prüfen den Dienst; das Management entscheidet, stattdessen eine bereits freigegebene Plattform zu nutzen. Die Ausnahme wird nicht erteilt, und die Nutzerinformation wird um den sicheren Alternativweg ergänzt.

Evidenz:

- Blockierungs- und Freigabeticket,
- dokumentierte Datenklassenbewertung,
- Datenschutz-/Einkauf-Handoff,
- Managemententscheidung zur Alternative,
- aktualisierte Nutzerinformation.
