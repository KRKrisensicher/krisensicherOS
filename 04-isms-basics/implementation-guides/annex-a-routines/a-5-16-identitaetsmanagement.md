
# A.5.16 — Identitätsmanagement

## Zweck

Identitätsmanagement sorgt dafür, dass digitale und organisatorische Identitäten eindeutig, nachvollziehbar und über ihren Lebenszyklus gesteuert werden. Dazu gehören Beschäftigte, externe Mitarbeitende, Dienstleister, technische Konten, Servicekonten, API-Identitäten und privilegierte Identitäten.

Der Kern ist nicht „ein Benutzerkonto existiert“, sondern eine verlässliche Identitätsroutine: Wer oder was ist eine Identität, welcher Owner ist verantwortlich, wann wird sie erstellt, geändert, gesperrt, reviewed oder gelöscht und wie wird Missbrauch erkennbar?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Routine für Anlage, Änderung, Prüfung und Beendigung von Identitäten im ISMS-Scope. Die Routine verbindet HR-/Lieferantenereignisse, eindeutige Identitätsquellen, Rollenbezug, technische Umsetzung, Zugriffsteuerung, Nachweisführung, Ausnahmebehandlung und Eskalation.

## Typische Risiken

- Wenn Identitäten nicht eindeutig Personen, Rollen oder technischen Zwecken zugeordnet sind, können Handlungen nicht nachvollzogen werden.
- Wenn Konten ohne gültigen Anlass bestehen bleiben, entstehen unbemerkte Zugriffs- und Angriffsmöglichkeiten.
- Wenn Sammelkonten oder geteilte Konten genutzt werden, gehen Verantwortlichkeit und Nachvollziehbarkeit verloren.
- Wenn externe oder technische Identitäten keinen Owner haben, bleiben Ablauf, Rotation, Rechte und Abschaltung ungeklärt.
- Wenn Identitätsdaten aus HR, Lieferantenmanagement und IT nicht zusammenpassen, scheitern Joiner-/Mover-/Leaver-Prozesse.

## Trigger

- Eintritt, Rollenwechsel, Teamwechsel, längere Abwesenheit oder Austritt.
- Beginn, Änderung oder Ende externer Mitarbeit oder Dienstleisterzugriffe.
- neues System, neue Plattform, neue Schnittstelle, neue API oder neues Servicekonto.
- Änderung von Rollenmodell, Organisationsstruktur oder Identitätsquelle.
- Sicherheitsereignis, Kontokompromittierung, verdächtige Anmeldung oder Auditfinding.
- turnusmäßiger Identitäts- und Kontenreview.
- Migration in Cloud, SSO, IAM, PAM oder neue Kollaborationsumgebung.

## Rollen und Verantwortung

- **HR / People-Funktion:** liefert verlässliche Ereignisse für interne Personenidentitäten.
- **Führungskraft / Prozess Owner:** bestätigt Rollenbezug, Start, Wechsel, Ende und Geschäftsbedarf.
- **Lieferantenmanagement / Einkauf:** führt externe Parteien, Vertragsbezug und Ende externer Identitäten.
- **Identity Owner / IAM-Verantwortliche:** betreibt Identitätsquelle, Kontenlogik, Lifecycle und Abgleich.
- **IT-/Plattform Owner:** setzt Konten, Gruppen, technische Identitäten und Systemintegration um.
- **Asset Owner / Service Owner:** verantwortet Identitäten mit Zugriff auf eigene Systeme oder Daten.
- **ISMS-Owner / Security-Rolle:** definiert Mindestanforderungen, Reviews, Ausnahmebehandlung und Eskalation.
- **Datenschutz / Legal:** prüft personenbezogene Auswertungen, Beschäftigtendaten, Protokollierung und Vertragsfragen.
- **Management:** entscheidet bei Sammelkonten, Ressourcenkonflikten, Restrisiken oder Toolinvestitionen.

## Implementierung

### Minimalstart

Ziel: Kritische Identitäten sind eindeutig, zugeordnet und beendbar.

1. Die Organisation benennt eine führende Quelle für interne Personenidentitäten und eine verantwortliche Stelle für externe Identitäten.
2. Neue Identitäten werden nur mit Anlass, Owner, Rolle oder Zweck angelegt.
3. Austritt, Rollenwechsel und Vertragsende lösen Sperrung, Änderung oder Löschung aus.
4. Kritische Systeme und privilegierte Konten werden auf verwaiste, geteilte oder nicht zuordenbare Identitäten geprüft.
5. Technische Konten erhalten mindestens Owner, Zweck, Systembezug und Reviewdatum.
6. Ausnahmen wie Sammelkonten werden begründet, befristet und risikobewertet.

Minimaler Nachweis:

- Identitäts- oder Kontenliste für kritische Systeme,
- Joiner-/Mover-/Leaver-Tickets,
- Owner- und Zwecknachweis für technische Konten,
- Reviewprotokoll kritischer Identitäten,
- Ausnahmeentscheidung für geteilte oder nicht standardkonforme Konten.

### Solide Praxis

Ziel: Identitätslebenszyklen sind wiederholbar und mit Zugriffssteuerung verbunden.

1. Identitätstypen werden unterschieden: interne Person, externe Person, privilegierte Identität, technische Identität, Servicekonto, Break-Glass-Konto.
2. Lifecycle-Regeln legen Anlage, Änderung, Sperrung, Löschung, Ablauf und Review je Identitätstyp fest.
3. HR-, Lieferanten- und IT-Prozesse werden mit Kontenanlage und -beendigung verbunden.
4. Namenskonventionen, eindeutige IDs und Verantwortlichkeiten verhindern Verwechslung.
5. Geteilte Konten werden vermieden oder als Ausnahme mit Zusatzkontrollen geführt.
6. Identitätsreviews prüfen verwaiste, inaktive, doppelte, privilegierte und externe Identitäten.
7. Findings führen zu Sperrung, Korrektur, Ausnahme oder Managemententscheidung.

Starke Evidenz:

- Identitätstypen- und Lifecycle-Modell,
- Joiner-/Mover-/Leaver-Nachweise,
- Kontenexporte aus kritischen Systemen,
- Reviewliste mit Entscheidungen,
- Nachweis gesperrter oder gelöschter Konten,
- technische Konten mit Owner, Zweck und Ablauf,
- Ausnahme- und Risikoakzeptanzlog.

### Fortgeschritten

Ziel: Identitäten werden als kontrollierter, messbarer und integrierter Governance-Baustein betrieben.

1. Zentrale Identitätsquelle, SSO, IAM, PAM, MDM und relevante Fachsysteme sind risikobasiert integriert.
2. Externe und technische Identitäten haben Ablaufdaten, automatische Wiedervorlage oder Rezertifizierung.
3. Privilegierte und Break-Glass-Identitäten werden besonders überwacht und regelmäßig getestet.
4. Maschinenidentitäten, API-Tokens, Zertifikate und Secrets werden mit Rotation, Ablauf und Owner geführt.
5. Auffällige Identitätsereignisse fließen in Monitoring und Incident Triage ein.
6. Kennzahlen zeigen verwaiste Konten, externe Identitäten, technische Konten, überfällige Reviews und Lifecycle-Zeiten.
7. Management entscheidet strukturelle Zielkonflikte, etwa Legacy-Sammelkonten, Tooling oder Ressourcen.

## Ablauf als Routine

1. **Identitätsbedarf entsteht:** neue Person, externe Rolle, technischer Zweck, System oder Schnittstelle.
2. **Anlass und Owner prüfen:** Geschäftsbedarf, Rolle, Vertrag, Systembezug oder technischer Zweck klären.
3. **Identität anlegen:** eindeutige ID, Typ, Startdatum, Owner, Ablauf oder Reviewdatum erfassen.
4. **Zugriff koppeln:** Berechtigungen über separate Zugriffssteuerungsroutine vergeben.
5. **Änderungen verarbeiten:** Rollenwechsel, Teamwechsel, Vertragsänderung oder Zweckänderung aktualisieren.
6. **Review durchführen:** inaktive, externe, privilegierte, technische und verwaiste Identitäten prüfen.
7. **Beenden:** Sperren, Löschen, Token widerrufen, Zertifikate rotieren oder Servicekonto ablösen.
8. **Abweichungen eskalieren:** nicht zuordenbare, geteilte oder kritische Identitäten behandeln.
9. **Verbessern:** Ursachen für verwaiste oder falsche Identitäten in HR-, Lieferanten- oder IT-Prozessen korrigieren.

## Entscheidungen

- Welche Quelle gilt für welche Identitätstypen als führend?
- Welche Identitäten dürfen ohne Ablaufdatum bestehen?
- Wie werden externe und technische Identitäten owned und reviewed?
- Welche Sammelkonten sind verboten, welche vorübergehend toleriert?
- Wann wird ein Identitätsproblem zum Incident?
- Welche Systeme müssen zuerst in Lifecycle-Reviews einbezogen werden?
- Welche Zielkonflikte zwischen Betrieb, Legacy-Systemen und Nachvollziehbarkeit gehen ins Management Review?

## Evidenz

### Starke Evidenz

- Identitätsmodell mit Typen, Ownern und Lifecycle-Regeln,
- HR-/Lieferantenereignisse mit IT-Tickets,
- Kontenexporte kritischer Systeme zum Reviewzeitpunkt,
- Reviewprotokolle mit Sperr-, Lösch- oder Korrekturentscheidungen,
- Nachweise für deaktivierte ehemalige oder verwaiste Konten,
- technische Identitäten mit Owner, Zweck, Ablauf und Rotation,
- Ausnahmeentscheidung für Sammel- oder Legacy-Konten,
- Managemententscheidung bei dauerhaftem Restrisiko.

### Schwache Evidenz

- Benutzerliste ohne Owner, Rolle oder Status,
- allgemeine IAM-Policy ohne Durchführung,
- manuelle Excel-Liste ohne Abgleich mit Systemen,
- Aussage „HR meldet Austritte“ ohne Ticket- oder Sperrnachweis,
- technische Konten mit sprechendem Namen, aber ohne Verantwortlichen.

### Evidenzlücken

- externe Identitäten ohne Vertragsende oder Owner,
- technische Konten ohne Zweck und Reviewdatum,
- Sammelkonten ohne Ausnahmeentscheidung,
- inaktive Konten ohne Sperrung,
- keine Verbindung zwischen Identität und Zugriff,
- keine Protokollierung kritischer Identitätsänderungen.

## Wirksamkeitsprüfung

Prüffragen:

- Sind kritische Identitäten eindeutig einer Person, Rolle, Organisation oder einem technischen Zweck zugeordnet?
- Werden Austritte, Rollenwechsel und Vertragsenden zuverlässig in Kontenänderungen übersetzt?
- Gibt es Reviews für externe, privilegierte und technische Identitäten?
- Werden verwaiste, inaktive oder doppelte Konten gefunden und bereinigt?
- Sind Sammelkonten nachvollziehbar begründet und zeitlich begrenzt?
- Werden Auffälligkeiten an Incident Response oder Management eskaliert?

Mögliche Kennzahlen:

- überfällige Identitätsreviews,
- Anzahl verwaister oder inaktiver Konten,
- externe Identitäten ohne Ablaufdatum,
- technische Konten ohne Owner,
- Zeit von Austritt bis Kontosperrung,
- Ausnahmequote für Sammelkonten,
- Anzahl korrigierter Identitätsfindings.

## BSIG-/NIS2-Anschluss

Identitätsmanagement ist anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Zugriffsschutz, Cyberhygiene, sichere Administration, Incident-Prävention, Lieferkettensicherheit und Governance. Für betroffene Organisationen sollte im Anforderungsregister geprüft werden, welche Identitätstypen, Systeme und Nachweise relevant sind.

Dieses Artefakt ersetzt keine rechtliche Prüfung von Beschäftigtendaten, Monitoring, Vertragsbeziehungen oder gesetzlichen Anforderungen.

## Grenzen

- Dieses Artefakt ist kein vollständiges IAM-, SSO- oder PAM-Architekturdesign.
- Es ersetzt keine Datenschutzprüfung für Protokollierung, Auswertung oder Beschäftigtendaten.
- Es trifft keine Zertifizierungs-, Konformitäts- oder Sicherheitsgarantie.
- Es enthält keine ISO-27002-Texte und keine Produktempfehlung.
- Identitätsmanagement ersetzt nicht die separate Entscheidung über konkrete Zugriffsrechte.

## Handoffs

- **HR-Handoff:** Eintritt, Rollenwechsel, Abwesenheit, Austritt, Stammdatenqualität.
- **Lieferanten-Handoff:** externe Identitäten, Vertragsbeginn, Vertragsende, Subdienstleister, Nachweise.
- **Zugriffssteuerungs-Handoff:** Berechtigungen, Rezertifizierung, privilegierte Rechte und Entzug.
- **IT-/Plattform-Handoff:** IAM, SSO, Verzeichnisdienste, lokale Konten, Servicekonten, Zertifikate, Tokens.
- **Datenschutz-/Legal-Handoff:** personenbezogene Auswertungen, Monitoring, Beschäftigtendaten, Vertragsfragen.
- **Incident-Handoff:** kompromittiertes Konto, unklare Identität, verdächtige Anmeldung, Missbrauchsverdacht.
- **Management-Handoff:** Legacy-Sammelkonten, Ressourcenbedarf, akzeptierte Restrisiken oder Toolentscheidung.
- **Audit-/Evidence-Handoff:** unvollständige Kontenlisten, fehlende Owner oder nicht nachvollziehbare Lifecycle-Entscheidungen.

## Typische Fehler

- Identitätsmanagement wird mit Berechtigungsmanagement verwechselt.
- Externe Personen werden wie interne Konten behandelt, aber ohne Vertragsende.
- Servicekonten bleiben dauerhaft aktiv, weil niemand sie besitzt.
- Sammelkonten werden aus Bequemlichkeit genutzt und nicht als Ausnahme geführt.
- HR-Daten, Lieferantenlisten und Systemkonten werden nicht abgeglichen.
- Reviews betrachten nur aktive Beschäftigte, nicht technische und privilegierte Identitäten.
- Konten werden gesperrt, aber Tokens, Zertifikate oder API-Schlüssel bleiben aktiv.

## Fiktives Mini-Beispiel

Ein fiktiver SaaS-Dienst wird für Kundenservice eingeführt. Neben internen Nutzern benötigt ein externer Implementierungspartner drei zeitlich begrenzte Konten und ein technisches API-Konto. Der Prozess Owner bestätigt Zweck und Laufzeit. IT legt die Identitäten mit Ablaufdatum an und koppelt Rechte an die Zugriffssteuerung. Beim Review nach Projektende werden zwei externe Konten deaktiviert; das API-Konto bleibt bestehen, erhält aber einen Service Owner, Rotationsdatum und eine Wiedervorlage.

Evidenz:

- Identitätsanlage mit Typ, Owner, Zweck und Ablauf,
- Lieferantenbezug für externe Konten,
- Reviewprotokoll nach Projektende,
- Deaktivierungsnachweis,
- API-Konto-Eintrag mit Owner und Rotationsdatum,
- offene Wiedervorlage für nächsten Review.
