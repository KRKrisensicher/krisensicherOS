
# A.5.14 — Informationsübertragung zwischen Parteien

## Zweck

Informationsübertragung zwischen Parteien sorgt dafür, dass Informationen beim Teilen, Versenden, Bereitstellen oder Empfangen kontrolliert bleiben. Betroffen sind interne und externe Übertragungen: E-Mail, Datenräume, Schnittstellen, Portale, Datenträger, Supportzugänge, Messenger, Dateiablagen, Papierpost und persönliche Übergaben.

Der Kern ist nicht „wir verschlüsseln manchmal“, sondern eine klare Entscheidungsroutine: Welche Information wird an wen übertragen, über welchen Kanal, mit welcher Freigabe, welchem Schutz, welchem Nachweis und welcher Rückmeldung?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Routine für sichere, zweckgebundene und überprüfbare Informationsübertragung. Die Routine verbindet Klassifizierung, Empfängerprüfung, Freigaben, geeignete Kanäle, technische Schutzmaßnahmen, vertragliche oder fachliche Handoffs, Protokollierung, Ausnahmebehandlung und Incident-Eskalation.

## Typische Risiken

- Wenn vertrauliche Informationen über ungeeignete Kanäle übertragen werden, können sie unbefugt offengelegt oder verändert werden.
- Wenn Empfänger oder Zweck nicht geprüft werden, entstehen Fehlversand, übermäßige Weitergabe oder unklare Verantwortung.
- Wenn Schnittstellen und Datenaustausche ohne Owner betrieben werden, bleiben Änderungen, Fehler und Sicherheitsereignisse unbemerkt.
- Wenn externe Parteien Schutzanforderungen nicht kennen, endet Kontrolle an der Organisationsgrenze.
- Wenn Übertragungsnachweise fehlen, können Freigaben, Zustellung, Integrität oder Rücknahme nicht nachvollzogen werden.

## Trigger

- neue externe Partei, neuer Dienstleister, neue Kunden- oder Behördenkommunikation.
- neue Schnittstelle, Datenraum, Portal, API, Export oder regelmäßiger Datenaustausch.
- Übertragung vertraulicher, personenbezogener, geschäftskritischer oder vertraglich geschützter Informationen.
- Änderung von Klassifizierung, Empfänger, Zweck, Kanal, Datenumfang oder Frequenz.
- Fehlversand, Zustellproblem, Datenabfluss, Manipulationsverdacht oder Incident.
- Auditfinding, Kundenanforderung, Vertragsänderung oder Risikoentscheidung.
- turnusmäßiger Review wichtiger Datenübertragungen.

## Rollen und Verantwortung

- **Information Owner / Prozess Owner:** entscheidet Zweck, Umfang, Empfänger und fachliche Freigabe.
- **ISMS-Owner / Security-Rolle:** definiert Mindestanforderungen, Risikologik, Ausnahmebehandlung und Review.
- **IT-/Plattform Owner:** stellt geeignete Kanäle, Verschlüsselung, Datenräume, Schnittstellen und Logs bereit.
- **Datenschutz / Legal:** prüft personenbezogene Daten, Verträge, Geheimhaltung, internationale oder rechtlich sensible Übertragungen.
- **Einkauf / Lieferantenmanagement:** verbindet Übertragung mit Dienstleisterverträgen, Subdienstleistern und Rückgaberegeln.
- **Fachbereiche:** prüfen Empfänger, Zweck, Datenumfang und korrekten Kanal im Alltag.
- **Incident Response:** übernimmt bei Fehlversand, Verdacht auf Offenlegung oder Kompromittierung.
- **Management:** entscheidet bei hohen Restrisiken, Ressourcenkonflikten oder nicht vermeidbarer unsicherer Übertragung.

## Implementierung

### Minimalstart

Ziel: Kritische Informationsübertragungen bewusst freigeben und nachweisbar durchführen.

1. Die Organisation benennt zulässige Standardkanäle je Informationsklasse, zum Beispiel Kollaborationsplattform, Datenraum, verschlüsselte E-Mail, Portal oder persönliche Übergabe.
2. Für vertrauliche oder kritische Informationen werden Empfänger, Zweck und Datenumfang vor Übertragung geprüft.
3. Wiederkehrende externe Übertragungen erhalten Owner, Frequenz und Ablageort für Nachweise.
4. Fehlversand oder falsche Empfänger werden als Sicherheitsmeldung behandelt.
5. Ausnahmen von Standardkanälen werden begründet, befristet und reviewed.
6. Fachbereiche erhalten eine kurze Entscheidungshilfe für Versand und Teilen.

Minimaler Nachweis:

- Kanal- und Umgangsmatrix je Informationsklasse,
- Freigabe- oder Ticketnachweis für kritische Übertragung,
- Liste regelmäßiger externer Datenaustausche,
- Kommunikations- oder Schulungsnachweis,
- Incident- oder Ausnahmeprotokoll bei Abweichung.

### Solide Praxis

Ziel: Informationsübertragung wird risikobasiert, wiederholbar und vertraglich anschlussfähig gesteuert.

1. Datenflüsse und regelmäßige Übertragungen werden im Informations- oder Schnittstellenregister geführt.
2. Schutzmaßnahmen orientieren sich an Klassifizierung, Empfänger, Zweck, Kanal, Integritätsbedarf und Nachweisbedarf.
3. Externe Parteien bestätigen Umgangsanforderungen über Vertrag, Vereinbarung, Portalregeln oder technische Nutzungsbedingungen, soweit passend.
4. Schnittstellen erhalten Owner, technische Verantwortung, Monitoring, Änderungsprozess und Störungsweg.
5. Freigabe- und Vier-Augen-Regeln werden für besonders kritische Übertragungen definiert.
6. Stichproben prüfen Empfänger, Kanal, Umfang, Freigabe und Nachweis.
7. Lessons Learned aus Fehlversand und Schnittstellenproblemen fließen in Regeln und Schulungen ein.

Starke Evidenz:

- Datenfluss- oder Übertragungsregister,
- Freigaben mit Zweck, Empfänger und Umfang,
- technische Kanal- oder Verschlüsselungsnachweise,
- Schnittstellendokumentation mit Owner,
- Lieferanten- oder Vertragsnachweise,
- Stichproben- und Korrekturprotokolle,
- Incident-Lessons-Learned.

### Fortgeschritten

Ziel: Kritische Übertragungen werden technisch unterstützt, überwacht und entscheidungsfähig berichtet.

1. Datenräume, Portale, APIs, Managed File Transfer, DLP oder Rechteverwaltung erzwingen oder unterstützen geeignete Schutzmaßnahmen.
2. Regelmäßige Datenaustausche sind mit Monitoring, Fehlerbehandlung, Integritätsprüfung und Änderungsfreigabe verbunden.
3. Hochkritische Übertragungen nutzen zusätzliche Kontrollen wie Empfängerbestätigung, Ablaufdatum, Wasserzeichen, Zugriffsentzug oder Protokollreview, sofern angemessen.
4. Abweichungen aus DLP, Mail-Gateways, Schnittstellenmonitoring oder Supportprozessen werden triagiert.
5. Kennzahlen zeigen kritische Übertragungen, Ausnahmen, Fehlversand, überfällige Reviews und offene Lieferantenrückmeldungen.
6. Management sieht Zielkonflikte zwischen Geschwindigkeit, Kollaboration, Kosten und Schutzbedarf.

## Ablauf als Routine

1. **Übertragungsbedarf entsteht:** Anfrage, Projekt, Schnittstelle, Export, Supportfall oder externe Zusammenarbeit.
2. **Information einordnen:** Klasse, Schutzbedarf, personenbezogene oder vertraglich geschützte Inhalte prüfen.
3. **Empfänger und Zweck prüfen:** Berechtigung, Identität, Rolle, Organisation und Datenminimierung klären.
4. **Kanal wählen:** Standardkanal oder begründete Ausnahme festlegen.
5. **Freigabe einholen:** Owner, Fachbereich, Legal/Datenschutz oder Management je nach Risiko einbeziehen.
6. **Übertragen:** Schutzmaßnahmen anwenden und Nachweis erzeugen.
7. **Bestätigen und überwachen:** Zustellung, Zugriff, Schnittstellenlauf, Fehler oder Rücknahme prüfen.
8. **Abweichung behandeln:** Fehlversand, falscher Kanal, unklare Empfänger oder technische Fehler eskalieren.
9. **Reviewen:** regelmäßige Übertragungen, Ausnahmen und Findings aktualisieren.

## Entscheidungen

- Welche Kanäle sind je Informationsklasse zulässig?
- Welche Übertragungen brauchen Owner-Freigabe, Vier-Augen-Prinzip oder Managemententscheidung?
- Wann ist Verschlüsselung, Datenraum, Portal oder Schnittstelle erforderlich?
- Welche Empfängerprüfung ist vor externer Übertragung nötig?
- Wie werden wiederkehrende Datenaustausche registriert und reviewed?
- Wann wird ein Fehlversand zum Incident?
- Welche Ausnahmen sind zulässig und wie lange?

## Evidenz

### Starke Evidenz

- Übertragungsregister mit Owner, Empfänger, Zweck, Kanal, Frequenz und Klasse,
- Freigabeprotokoll für kritische Übertragungen,
- technische Nachweise für Kanal, Verschlüsselung, Zugriff oder Integritätsprüfung,
- Schnittstellenmonitoring oder Laufprotokolle,
- Lieferanten-/Vertragsnachweise zu Umgang und Rückgabe,
- Stichproben mit Korrekturmaßnahmen,
- Incident- und Lessons-Learned-Nachweise bei Fehlübertragung.

### Schwache Evidenz

- allgemeiner Hinweis „vertrauliche Daten verschlüsseln“ ohne Kanalentscheidung,
- E-Mail-Verlauf ohne Freigabe oder Empfängerprüfung,
- Schnittstellenliste ohne Owner,
- Tool-Screenshot ohne Nachweis der Nutzung,
- Vertrag ohne Bezug zu tatsächlichen Datenflüssen.

### Evidenzlücken

- regelmäßige externe Exporte ohne Register,
- vertrauliche Informationen über private oder ungeprüfte Kanäle,
- keine Freigabe für besonders kritische Übertragungen,
- keine Behandlung von Fehlversand,
- unbekannte Subdienstleister oder Empfängerketten,
- Schnittstellenänderungen ohne Review.

## Wirksamkeitsprüfung

Prüffragen:

- Sind die wichtigsten externen und internen Datenübertragungen bekannt und owned?
- Können Fachbereiche je Informationsklasse den richtigen Kanal wählen?
- Gibt es Freigaben und Nachweise für kritische Übertragungen?
- Werden Fehlversand und Kanalabweichungen gemeldet und korrigiert?
- Sind Schnittstellen mit Owner, Monitoring und Änderungsprozess versehen?
- Werden Legal-/Datenschutz-Handoffs rechtzeitig ausgelöst?

Mögliche Kennzahlen:

- Anteil kritischer Übertragungen mit Owner und Registereintrag,
- Anzahl Kanalabweichungen oder Fehlversandmeldungen,
- überfällige Reviews regelmäßiger Datenaustausche,
- Ausnahmen von Standardkanälen,
- offene Lieferantenrückmeldungen,
- Schnittstellenfehler mit Sicherheitsrelevanz.

## BSIG-/NIS2-Anschluss

Kontrollierte Informationsübertragung ist anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, sichere Kommunikation, Lieferkettensicherheit, Incident Handling, Business Continuity, Zugriffsschutz und Governance. Die konkrete Relevanz sollte organisationsspezifisch im Anforderungsregister, in Datenflussübersichten und Risikoentscheidungen geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung zu Datenschutz, Meldepflichten, Geheimhaltung, grenzüberschreitender Übertragung oder Vertragsfragen.

## Grenzen

- Keine Rechts- oder Datenschutzberatung.
- Keine verbindliche Aussage, welcher Kanal in jedem Fall zulässig ist.
- Keine Zertifizierungs-, Konformitäts- oder Sicherheitsgarantie.
- Keine technische Verschlüsselungsbaseline oder Produktempfehlung.
- Keine ISO-27002-Texte oder vertraulichen Praxisdaten.

## Handoffs

- **Klassifizierungs-Handoff:** unklare Informationsklasse oder Schutzbedarf.
- **Datenschutz-/Legal-Handoff:** personenbezogene Daten, Geheimhaltung, Verträge, internationale Übertragung, Streitfälle.
- **IT-/Plattform-Handoff:** Datenräume, E-Mail-Schutz, Schnittstellen, Verschlüsselung, Logging, Monitoring.
- **Lieferanten-Handoff:** externe Parteien, Subdienstleister, Datenrückgabe, Löschung, Sicherheitsanforderungen.
- **Incident-Handoff:** Fehlversand, falscher Empfänger, Datenabfluss, kompromittierter Kanal.
- **BCM-Handoff:** kritische Übertragung ist für Geschäftsfortführung oder Krisenkommunikation notwendig.
- **Management-Handoff:** nicht vermeidbare unsichere Übertragung, Ressourcenbedarf, akzeptiertes Restrisiko.

## Typische Fehler

- Der Kanal wird nach Bequemlichkeit gewählt, nicht nach Informationsklasse.
- Wiederkehrende Exporte existieren, aber niemand kennt Owner oder Empfänger.
- Schnittstellen werden als rein technisches Thema ohne Fachfreigabe behandelt.
- Vertrauliche Anhänge werden an Verteiler gesendet, ohne Empfängerprüfung.
- Fehlversand wird korrigiert, aber nicht als Lernsignal genutzt.
- Externe Parteien erhalten Informationen ohne klare Umgangserwartung.
- Verschlüsselung wird erwähnt, aber Schlüsselübergabe oder Empfängerprüfung bleiben ungeklärt.

## Fiktives Mini-Beispiel

Ein fiktiver Fachbereich möchte monatlich Supportdaten an einen externen Wartungsdienstleister übertragen. Der Prozess Owner erfasst den Datenaustausch im Übertragungsregister: Zweck, Empfänger, Datenumfang, Klasse, Frequenz und Kanal. Datenschutz und Legal prüfen die Vertrags- und Personenbezugsfragen. IT richtet einen Datenraum mit Ablaufdatum und Zugriffsnachweis ein. Nach zwei Monaten zeigt eine Stichprobe, dass ein Export zu viele Felder enthielt; der Fachbereich reduziert den Datensatz und dokumentiert die Korrektur.

Evidenz:

- Übertragungsregistereintrag,
- Freigabe durch Prozess Owner,
- Legal-/Datenschutz-Handoff-Notiz,
- Datenraum- und Zugriffsnachweis,
- Stichprobenergebnis,
- Korrektur des Exportumfangs.
