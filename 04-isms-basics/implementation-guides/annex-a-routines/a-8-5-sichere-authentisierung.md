
# A.8.5 — Sichere Authentisierung

## Zweck

Sichere Authentisierung sorgt dafür, dass Personen, Dienste und Maschinenidentitäten verlässlich nachweisen müssen, wer oder was sie sind, bevor Zugriff auf Systeme, Daten oder Funktionen entsteht. Der Wert liegt nicht in einer Passwortregel allein, sondern in einer betriebenen Routine für Authentisierungsverfahren, MFA, Ausnahmen, technische Konten, Recovery und Review.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Authentisierungsroutine für Nutzerkonten, privilegierte Konten, externe Zugriffe, Servicekonten, Schnittstellen und kritische Anwendungen. Authentisierung wird risikobasiert geplant, technisch umgesetzt, regelmäßig geprüft und bei Schwächen oder Vorfällen verbessert.

## Typische Risiken

- Wenn einfache oder wiederverwendete Geheimnisse für kritische Zugriffe genügen, können kompromittierte Zugangsdaten direkt zu Systemzugriff führen.
- Wenn MFA nur teilweise eingeführt ist, bleiben privilegierte, externe oder Cloud-Zugriffe angreifbar.
- Wenn Recovery- und Reset-Prozesse schwach sind, kann ein Angreifer Authentisierung über den Support umgehen.
- Wenn Servicekonten, API-Schlüssel oder Tokens ohne Owner laufen, entstehen dauerhafte verdeckte Zugänge.
- Wenn Ausnahmen nicht befristet sind, wird schwache Authentisierung zur Normalität.
- Wenn Authentisierungsereignisse nicht überwacht werden, bleiben Brute-Force, Credential Stuffing oder ungewöhnliche Logins unbemerkt.

## Trigger

- neues System, neuer Cloud-Dienst, neue Anwendung, neue Schnittstelle oder neuer Remote-Zugriff.
- Einführung oder Änderung von MFA, Single Sign-on, Passwortmanager, Identity Provider oder Privileged-Access-Lösung.
- neue privilegierte Rolle, externer Zugriff, Dienstleisterkonto oder Servicekonto.
- Kontokompromittierung, verdächtige Logins, Phishing-Welle oder Credential-Leak.
- Reset-, Recovery- oder Supportprozess wird geändert.
- Auditfinding, Schwachstellenbefund oder Monitoring-Treffer.
- turnusmäßiger Review kritischer Authentisierungsverfahren und Ausnahmen.

## Rollen und Verantwortung

- **IAM-/Identity Owner:** verantwortet Identitätsquelle, Authentisierungsverfahren, MFA-Logik und technische Policies.
- **IT-/Plattform Owner:** setzt Authentisierung in Systemen, Cloud-Diensten und Anwendungen um.
- **Service Owner / Application Owner:** bewertet Schutzbedarf, Nutzergruppen und Ausnahmebedarf.
- **Security-Rolle / ISMS-Owner:** definiert Mindestlogik, Reviewanforderungen, Monitoring- und Eskalationspunkte.
- **Support / Service Desk:** betreibt Reset- und Recovery-Prozesse mit klaren Prüfschritten.
- **HR / Lieferantenmanagement:** liefert Eintritts-, Austritts- und Vertragsereignisse für Konten.
- **Datenschutz / Legal:** prüft personenbezogene Login-Auswertungen, Beschäftigtendaten und vertragliche Fragen.
- **Management:** entscheidet bei Kosten, Nutzerakzeptanz, Ausnahmequoten oder nicht tragbaren Restrisiken.

## Implementierung

### Minimalstart

Ziel: kritische Zugriffe nicht allein von schwachen Geheimnissen abhängig machen.

1. Kritische Systeme, Cloud-Dienste, Remote-Zugänge, Adminzugriffe und externe Zugriffe werden im Scope benannt.
2. Für diese Zugriffe wird MFA oder ein gleichwertig begründetes stärkeres Verfahren geplant und umgesetzt.
3. Passwort- und Geheimnisregeln werden auf realistische Nutzung, Sperrung, Wiederverwendung und sichere Ablage ausgerichtet.
4. Reset- und Recovery-Prozesse erhalten dokumentierte Prüfschritte.
5. Servicekonten, API-Schlüssel und Tokens erhalten Owner, Zweck und Ablauf- oder Reviewdatum.
6. Ausnahmen werden befristet, begründet und reviewed.

Minimaler Nachweis:

- Scope kritischer Authentisierungsziele,
- MFA-/Authentisierungsstatus je Zielgruppe,
- dokumentierter Reset- oder Recovery-Ablauf,
- Servicekonto-/Tokenliste mit Owner,
- Ausnahmeentscheidungen mit Wiedervorlage.

### Solide Praxis

Ziel: Authentisierung wird risikobasiert, wiederholbar und reviewfähig betrieben.

1. Authentisierungsanforderungen werden nach Zugriffstyp unterschieden: Standardnutzer, privilegierte Nutzer, externe Nutzer, technische Identitäten, API-Zugriffe.
2. MFA-Abdeckung, Ausnahmen, Recovery-Ereignisse und verdächtige Logins werden regelmäßig ausgewertet.
3. Privilegierte Konten erhalten stärkere Verfahren, getrennte Nutzung oder zusätzliche Freigaben.
4. Maschinenidentitäten werden inventarisiert, rotiert und auf minimale Berechtigungen begrenzt.
5. Neue Anwendungen werden vor Produktivsetzung gegen die Authentisierungslogik geprüft.
6. Supportprozesse verhindern, dass Identitätsprüfung durch informelle Bestätigung ersetzt wird.
7. Findings fließen in Maßnahmenlog, Awareness, IAM-Verbesserungen oder Management Review.

### Fortgeschritten

Ziel: Authentisierung wird kontext- und risikobasiert gesteuert.

1. Identity Provider, Gerätevertrauen, Netzwerk-/Standortkontext und Risikoindikatoren werden für kritische Zugriffe berücksichtigt.
2. Privilegierte Aktivitäten nutzen zeitlich begrenzte Berechtigungen, stärkere Freigaben oder Sitzungsüberwachung, soweit angemessen.
3. Anomalien wie unmögliche Reise, ungewöhnliche Uhrzeit, neue Geräte oder gehäufte Fehlversuche lösen Triage aus.
4. Secrets, Tokens und Zertifikate werden zentral verwaltet, rotiert und in CI/CD oder Betriebsprozesse integriert.
5. Authentisierungskennzahlen werden in Security Monitoring, Incident Response und Management Reporting eingebunden.
6. Wiederkehrende Schwächen führen zu Architektur-, Tool- oder Prozessentscheidungen.

## Ablauf als Routine

1. **Authentisierungsbedarf entsteht:** neues System, neue Rolle, externer Zugriff, Servicekonto oder Änderung.
2. **Schutzbedarf einordnen:** Datenklasse, Exposition, Privilegierung, Nutzergruppe und Missbrauchsauswirkung bewerten.
3. **Verfahren festlegen:** MFA, SSO, Zertifikat, Token, Passwortmanager, Maschinenidentität oder Sonderprozess auswählen.
4. **Umsetzen:** technische Policy, Gruppen, Reset-Regeln, Token-Laufzeit und Logging konfigurieren.
5. **Nachweis erfassen:** Scope, Entscheidung, technische Umsetzung, Ausnahmen und Reviewdatum dokumentieren.
6. **Überwachen:** Fehlversuche, verdächtige Logins, Recovery-Fälle und Ausnahmen prüfen.
7. **Reviewen:** MFA-Abdeckung, Servicekonten, Tokens, privilegierte und externe Zugriffe regelmäßig bewerten.
8. **Verbessern oder eskalieren:** schwache Verfahren, hohe Ausnahmequote oder Ressourcenbedarf an Management oder Incident Response geben.

## Entscheidungen

- Welche Zugriffe benötigen zwingend stärkere Authentisierung?
- Welche Verfahren sind für welche Nutzergruppen praktikabel und wirksam?
- Wer darf Ausnahmen genehmigen und wie lange?
- Wie werden Recovery und Support gegen Social Engineering abgesichert?
- Welche technischen Identitäten brauchen Rotation, Ablaufdatum oder stärkere Schutzmechanismen?
- Welche Login-Auswertungen sind zulässig und datenschutzseitig zu klären?

## Evidenz

### Starke Evidenz

- aktueller Scope kritischer Systeme und Zugriffstypen,
- MFA- oder Authentisierungsabdeckung mit Datum,
- technische Policy-Exports oder Konfigurationsnachweise,
- dokumentierte Reset- und Recovery-Prüfschritte,
- Servicekonto-/Tokenregister mit Owner, Zweck, Rotation und Ablaufdatum,
- Reviewprotokolle zu Ausnahmen und privilegierten Zugriffen,
- Incident- oder Monitoring-Tickets zu auffälligen Loginereignissen,
- Managemententscheidung bei akzeptierten Restrisiken.

### Schwache Evidenz

- Passwortpolicy ohne technische Durchsetzung,
- MFA-Screenshot ohne Scope oder Zielgruppenbezug,
- pauschale Aussage „SSO vorhanden“ ohne Review,
- Liste technischer Konten ohne Owner,
- Reset-Prozess als informelle Service-Desk-Praxis,
- Kennzahl zu Loginfehlern ohne Auswertung oder Entscheidung.

### Evidenzlücken

- kritische Systeme außerhalb des Identity Providers,
- externe oder privilegierte Konten ohne MFA,
- Servicekonten ohne Verantwortliche und Rotation,
- Ausnahmen ohne Ablaufdatum,
- Recovery-Prozess ohne Identitätsprüfung,
- keine Triage auffälliger Authentisierungsereignisse.

## Wirksamkeitsprüfung

Prüffragen:

- Sind kritische, externe und privilegierte Zugriffe durch angemessene Authentisierung geschützt?
- Ist nachvollziehbar, welche Systeme nicht im zentralen Verfahren hängen und warum?
- Werden Ausnahmen befristet reviewed und reduziert?
- Sind Servicekonten, API-Schlüssel und Tokens einem Owner zugeordnet?
- Ist der Reset-/Recovery-Prozess gegen Missbrauch geprüft?
- Werden auffällige Loginereignisse in Monitoring oder Incident Triage überführt?

Mögliche Kennzahlen:

- MFA-Abdeckung kritischer Zugriffe,
- Anzahl und Alter von Ausnahmen,
- privilegierte Konten ohne stärkeres Verfahren,
- Servicekonten ohne Owner oder Ablaufdatum,
- verdächtige Loginereignisse mit Triage,
- Recovery-Fälle nach Kanal und Ergebnis,
- überfällige Tokenrotationen.

## BSIG-/NIS2-Anschluss

Sichere Authentisierung ist anschlussfähig an NIS2-orientierte Themen wie Zugriffsschutz, Cyberhygiene, sichere Administration, Incident-Prävention und Schutz kritischer Dienste. Organisationen sollten den konkreten Bezug im Anforderungsregister, in der Risikoanalyse und in der technischen Architekturprüfung festlegen.

Dieses Artefakt ersetzt keine Rechtsberatung, Datenschutzprüfung oder verbindliche Bewertung der Anwendbarkeit.

## Grenzen

- Dieses Artefakt ist kein Produktvergleich für MFA-, IAM- oder PAM-Lösungen.
- Es ersetzt kein vollständiges Zugriffskonzept und keine technische Architekturprüfung.
- Es trifft keine verbindliche Aussage zu gesetzlichen Pflichten oder Zertifizierungsfähigkeit.
- Login- und Verhaltensauswertungen benötigen geeignete menschliche Prüfung.
- Keine ISO-27002-Texte, keine echten Zugangsdaten, keine geheimen Konfigurationsdetails.

## Handoffs

- **IAM-Handoff:** Rollenmodell, Identitätsquelle, MFA, Kontenlebenszyklus, technische Identitäten.
- **Incident-Handoff:** kompromittierte Zugangsdaten, verdächtige Logins, MFA-Fatigue, Credential Stuffing.
- **Service-Desk-Handoff:** Reset, Recovery, Identitätsprüfung und Social-Engineering-Schutz.
- **Datenschutz-/Legal-Handoff:** personenbezogene Login-Auswertungen, Beschäftigtenmonitoring, externe Identitäten.
- **Entwicklungs-/DevOps-Handoff:** API-Schlüssel, Secrets, Zertifikate, CI/CD-Authentisierung.
- **Management-Handoff:** hohe Ausnahmequote, Kosten-/Nutzbarkeitskonflikte, nicht abdeckbare Legacy-Systeme.
- **Audit-/Evidence-Handoff:** fehlende Scope-Abdeckung, fehlende Ausnahmereviews, unvollständige Tokenregister.

## Typische Fehler

- MFA wird nur für einige Cloud-Dienste aktiviert und dann als vollständig betrachtet.
- Recovery-Prozesse sind schwächer als die normale Anmeldung.
- Servicekonten werden wie normale Nutzer behandelt.
- Tokens und API-Schlüssel laufen unbegrenzt.
- Ausnahmen werden aus Komfortgründen dauerhaft.
- Login-Alerts werden erzeugt, aber niemand triagiert sie.
- Passwortregeln erhöhen Aufwand, ohne reale Angriffswege zu reduzieren.

## Fiktives Mini-Beispiel

Ein fiktiver Hersteller führt für sein Kundenportal SSO ein. Beim Review stellt der Identity Owner fest, dass Administratoren MFA nutzen, aber drei externe Supportkonten und mehrere API-Tokens ohne Ablaufdatum existieren. Der Service Owner bestätigt zwei externe Konten als nicht mehr erforderlich. Sie werden entfernt; für die übrigen Konten wird MFA aktiviert. API-Tokens erhalten Owner, Zweck, Rotationstermin und einen Eintrag im Maßnahmenlog.

Evidenz:

- Scope des Kundenportals,
- MFA-Abdeckungsübersicht,
- Ticket zum Entzug externer Konten,
- Tokenregister mit Rotationstermin,
- Reviewentscheidung des Service Owners.
