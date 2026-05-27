
# A.5.17 — Umgang mit Authentifizierungsinformationen

## Zweck

Authentifizierungsinformationen sind alles, womit Identitäten nachgewiesen oder Zugriffe ausgelöst werden können: Passwörter, Passphrases, MFA-Token, Recovery-Codes, API-Schlüssel, Zertifikate, SSH-Schlüssel, Service-Account-Secrets und vergleichbare Geheimnisse.

Diese Routine sorgt dafür, dass solche Informationen nicht beiläufig erzeugt, geteilt, gespeichert, kopiert oder vergessen werden. Der Kern ist eine sichere Betriebslogik über den gesamten Lebenszyklus: Ausgabe, Nutzung, Aufbewahrung, Rotation, Widerruf, Wiederherstellung und Behandlung von Verdachtsfällen.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Routine für Authentifizierungsinformationen von Menschen, Diensten und Maschinenidentitäten. Sie legt fest, welche Geheimnisse erlaubt sind, wo sie gespeichert werden dürfen, wer sie verwaltet, wann sie geändert oder entzogen werden und wie Verdachtsfälle behandelt werden.

## Typische Risiken

- Wenn Passwörter, Tokens oder Schlüssel in Chats, Tickets, Repositories oder Tabellen landen, können unberechtigte Personen Zugriff auf Systeme und Daten erhalten.
- Wenn Service-Account-Secrets keinen Owner haben, bleiben sie nach Projektende aktiv und werden bei Rollenwechseln nicht widerrufen.
- Wenn Recovery-Codes oder Break-Glass-Zugänge unkontrolliert liegen, kann ein Notfallzugang zum Normalzugang werden.
- Wenn Zugangsdaten zwischen Personen geteilt werden, sind Handlungen nicht mehr einer verantwortlichen Identität zuordenbar.
- Wenn kompromittierte Authentifizierungsinformationen nicht schnell rotiert werden, kann ein Sicherheitsereignis verlängert oder verschärft werden.
- Wenn MFA, Passwortmanager oder Secret-Management nur informell genutzt werden, entstehen Ausweichwege ohne Evidenz.

## Trigger

- neues Konto, neuer Adminzugang, neuer Dienst, neue API, neues Zertifikat oder neuer Schlüssel.
- Eintritt, Rollenwechsel, Austritt oder Ende eines Dienstleisterzugriffs.
- Verdacht auf kompromittierte Zugangsdaten, Phishing, Token-Leak, Repository-Fund oder Incident.
- Einführung oder Änderung von MFA, Passwortmanager, Secret-Management, Zertifikatsverwaltung oder IAM-Prozess.
- Ablaufdatum, Rotationsfrist oder geplanter Review von Servicekonten und Maschinenidentitäten.
- Auditfinding, Schwachstellenfund oder technische Änderung an Authentifizierungsverfahren.
- Notfallzugriff, Wiederherstellung eines Kontos oder Nutzung eines Break-Glass-Verfahrens.

## Rollen und Verantwortung

- **Identity-/IAM-Owner:** definiert technische Authentifizierungsverfahren, Kontoarten und Entzugslogik.
- **IT-/Plattform Owner:** setzt Passwort-, MFA-, Secret-, Schlüssel- und Zertifikatsanforderungen technisch um.
- **Asset Owner / Service Owner:** verantwortet Authentifizierungsinformationen für Anwendungen, Schnittstellen und Servicekonten.
- **ISMS-Owner / Security-Rolle:** definiert Mindestlogik, Reviewanforderungen, Ausnahmebehandlung und Incident-Handoff.
- **Führungskraft / Prozess Owner:** bestätigt Geschäftsbedarf bei besonderen Zugängen oder geteilten Funktionsrisiken.
- **HR / Einkauf:** liefert Eintritts-, Wechsel-, Austritts- und Vertragsende-Trigger.
- **Datenschutz / Legal:** prüft personenbezogene Auswertungen, Beschäftigtenbezug, Vertrags- und Nachweisanforderungen.
- **Management:** entscheidet bei dauerhaftem Restrisiko, nicht umsetzbaren Mindestanforderungen oder Ressourcenbedarf.

## Implementierung

### Minimalstart

Ziel: die gefährlichsten Geheimnisse sichtbar machen und unsichere Ablagen stoppen.

1. Die Organisation legt fest, welche Authentifizierungsinformationen im Scope sind: Nutzerpasswörter, MFA, Adminzugänge, Servicekonten, API-Keys, Zertifikate und Recovery-Codes.
2. Für kritische Systeme und Servicekonten wird ein Owner benannt.
3. Zugangsdaten dürfen nicht in Chat, E-Mail, Tickets, Code-Repositories oder ungeschützten Dateien abgelegt werden.
4. Für Menschen wird ein Passwortmanager oder ein gleichwertig freigegebener Speicherweg festgelegt.
5. Für technische Secrets gibt es mindestens ein Register mit Owner, Zweck, Speicherort, Ablauf oder Reviewdatum.
6. Verdacht auf Offenlegung löst sofort Rotation, Sperrung oder Incident-Triage aus.
7. Notfallzugänge werden separat dokumentiert und nach Nutzung reviewed.

Minimaler Nachweis:

- Regel oder Kurzstandard für Umgang mit Authentifizierungsinformationen,
- Liste kritischer Servicekonten, Schlüssel oder Zertifikate mit Owner,
- Nachweis freigegebener Speicherwege,
- Ticket zur Rotation oder Sperrung bei Verdacht,
- Reviewnotiz für Notfallzugänge.

### Solide Praxis

Ziel: Geheimnisse werden über ihren Lebenszyklus gesteuert.

1. Authentifizierungsinformationen werden nach Typ und Kritikalität klassifiziert: persönliche Zugänge, privilegierte Zugänge, technische Secrets, Zertifikate, Recovery-Mittel.
2. MFA wird risikobasiert für kritische Zugriffe, externe Zugriffe und privilegierte Rollen eingeführt oder begründet ausgenommen.
3. Servicekonten und Maschinenidentitäten erhalten Owner, Zweck, minimale Rechte, Rotationslogik und Deprovisioning-Trigger.
4. Secret-Scanning, Repository-Regeln oder manuelle Kontrollen prüfen typische Leckage-Orte.
5. Ausnahmen werden befristet, begründet und mit Kompensationsmaßnahmen geführt.
6. Joiner-/Mover-/Leaver-Prozesse lösen Prüfung oder Widerruf betroffener Authentifizierungsinformationen aus.
7. Wiederkehrende Findings führen zu Verbesserungen bei Tooling, Schulung oder Prozessdesign.

Starke Evidenz:

- Secret-/Servicekonto-Register,
- Passwortmanager- oder Secret-Management-Nutzung mit Scope,
- MFA-Abdeckungsübersicht für kritische Zugriffe,
- Rotations- und Widerrufstickets,
- Secret-Scanning-Ergebnisse mit Maßnahmen,
- Ausnahmeentscheidungen mit Ablaufdatum.

### Fortgeschritten

Ziel: Authentifizierungsinformationen werden technisch überwacht und eng mit IAM, DevOps und Incident Response verbunden.

1. Secret-Management, IAM, CI/CD, Cloud-Plattformen und Monitoring sind integriert.
2. Kurzlebige Tokens, Just-in-time-Privilegien oder automatische Rotation reduzieren langlebige Geheimnisse.
3. Zertifikate, SSH-Schlüssel, API-Keys und Servicekonten werden automatisiert inventarisiert und auf Ablauf überwacht.
4. Leaks in Repositories, Artefakten, Logs oder Tickets erzeugen Alerts und vordefinierte Reaktionsschritte.
5. Break-Glass-Zugänge werden regelmäßig getestet, versiegelt, protokolliert und nach jeder Nutzung reviewed.
6. Management erhält entscheidungsfähige Kennzahlen zu offenen Risiken, überfälligen Rotationen, nicht zuordenbaren Secrets und Ausnahmequoten.

## Ablauf als Routine

1. **Bedarf entsteht:** Konto, API, Dienst, Zertifikat, Notfallzugang oder technische Integration wird benötigt.
2. **Typ bestimmen:** persönliche Identität, privilegierter Zugriff, technisches Secret, Recovery-Mittel oder Maschinenidentität.
3. **Owner und Zweck festlegen:** fachlicher und technischer Verantwortlicher, Systembezug und Laufzeit klären.
4. **Sicheren Speicherweg wählen:** Passwortmanager, Secret-Manager, Zertifikatsverwaltung oder freigegebene Alternative nutzen.
5. **Mindestschutz umsetzen:** MFA, minimale Rechte, Ablaufdatum, Rotation, Zugriffsbeschränkung und Protokollierung passend festlegen.
6. **Nutzung dokumentieren:** nicht das Geheimnis selbst, sondern Owner, Zweck, Speicherortklasse, Ablauf und Reviewdatum erfassen.
7. **Review durchführen:** aktive, ablaufende, geteilte, verwaiste oder ungewöhnliche Authentifizierungsinformationen prüfen.
8. **Bei Verdacht handeln:** sperren, rotieren, Logs prüfen, Incident-Handoff auslösen und Lessons Learned dokumentieren.
9. **Verbessern:** wiederholte Lecks oder Ausnahmen in Prozess, Tooling und Schulung zurückspielen.

## Entscheidungen

- Welche Authentifizierungsinformationen sind für den Minimalstart kritisch genug?
- Welche Speicherwege sind freigegeben und welche ausdrücklich verboten?
- Wo ist MFA verpflichtend, wo gibt es befristete Ausnahmen?
- Wie lange dürfen technische Secrets, Zertifikate oder Schlüssel gültig sein?
- Wer darf Notfallzugänge verwahren, nutzen und nachträglich reviewen?
- Welche Funde werden als Incident behandelt und welche als reguläre Korrektur?
- Wann braucht eine Ausnahme Managemententscheidung statt technischer Einzelfreigabe?

## Evidenz

### Starke Evidenz

- aktuelles Register kritischer Servicekonten, API-Keys, Zertifikate oder SSH-Schlüssel mit Owner,
- Nachweis freigegebener Secret- und Passwortspeicher,
- MFA-Abdeckung für kritische und privilegierte Zugriffe,
- Rotations-, Sperr- oder Widerrufsnachweise,
- Secret-Scanning-Findings mit dokumentierter Behandlung,
- Reviewprotokolle zu Notfallzugängen,
- Managemententscheidung bei dauerhaftem Restrisiko.

### Schwache Evidenz

- allgemeine Passwortregel ohne Nachweis der Nutzung,
- Screenshot einzelner MFA-Einstellungen ohne Scope,
- veraltete Servicekonto-Liste ohne Owner,
- Ticketkommentar „Passwort geändert“ ohne Bezug zum betroffenen Secret,
- Policy, die unsichere Ablagen verbietet, ohne Kontrolle typischer Ablageorte.

### Evidenzlücken

- technische Secrets ohne Owner oder Ablaufdatum,
- Zugangsdaten in Code, Tickets, Chat oder Dateien ohne Behandlung,
- geteilte Konten ohne Ausnahmeentscheidung,
- Break-Glass-Zugang ohne Test oder Nutzungsreview,
- ausgeschiedene Personen oder Dienstleister mit bekannten Secrets,
- keine Incident-Triage bei Verdacht auf Offenlegung.

## Wirksamkeitsprüfung

Prüffragen:

- Sind kritische Authentifizierungsinformationen inventarisiert, verantwortet und reviewfähig?
- Werden unsichere Ablageorte technisch oder organisatorisch erkannt?
- Können kompromittierte Secrets schnell gesperrt oder rotiert werden?
- Sind Servicekonten und Maschinenidentitäten mit minimalen Rechten und Owner geführt?
- Sind MFA-Ausnahmen befristet und nachvollziehbar entschieden?
- Wird jede Nutzung von Notfallzugängen nachträglich geprüft?
- Führen wiederholte Lecks zu Prozess- oder Toolverbesserungen?

Mögliche Kennzahlen:

- Anteil kritischer Servicekonten mit Owner und Reviewdatum,
- überfällige Rotationen oder Zertifikatsabläufe,
- Anzahl Secret-Leaks nach Quelle,
- Zeit bis Rotation nach Verdacht,
- MFA-Abdeckung kritischer Zugriffe,
- offene und überfällige Ausnahmen.

## BSIG-/NIS2-Anschluss

Der sichere Umgang mit Authentifizierungsinformationen ist anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Cyberhygiene, Zugriffsschutz, Incident-Prävention und Managementaufsicht über kritische technische Abhängigkeiten.

Für BSIG-/NIS2-Betroffenheit sollte die Organisation im Anforderungsregister prüfen, welche Systeme, Rollen, Nachweise und Handoffs relevant sind. Dieses Artefakt ersetzt keine rechtliche Auslegung und keine verbindliche Prüfung der Anwendbarkeit.

## Grenzen

- Dieses Artefakt ist kein vollständiges IAM-, Kryptografie- oder Secret-Management-Design.
- Es ersetzt keine Datenschutzprüfung für personenbezogene Logs, MFA-Auswertungen oder Beschäftigtendaten.
- Es enthält keine Vorgaben zu konkreten Passwortlängen, Algorithmen oder Herstellertools.
- Keine Rechtsberatung, keine Datenschutzberatung, keine Zertifizierungszusage.
- Keine ISO-27002-Texte, keine echten Zugangsdaten und keine vertraulichen technischen Details in Beispielen.

## Handoffs

- **IAM-/Access-Handoff:** neue Kontotypen, Rollenwechsel, Entzug, Rezertifizierung und privilegierte Rechte.
- **Incident-Handoff:** Verdacht auf Offenlegung, Phishing, Token-Leak, unautorisierte Nutzung oder unbekannte Secret-Funde.
- **DevOps-/Entwicklungs-Handoff:** Secrets in Code, CI/CD, Artefakten, Container-Images, Logs oder Build-Konfigurationen.
- **HR-/Einkauf-Handoff:** Austritt, Dienstleisterende, Rollenwechsel oder Wechsel von Schlüsselpersonen.
- **Datenschutz-/Legal-Handoff:** personenbezogene Protokollierung, Beschäftigtenbezug, Vertragsfragen oder Nachweisanforderungen.
- **Management-Handoff:** dauerhafte MFA-Ausnahmen, nicht behebbare Altverfahren, Ressourcenbedarf oder akzeptiertes Restrisiko.
- **Audit-/Evidence-Handoff:** unvollständiges Register, fehlende Rotationsnachweise oder nicht reviewte Notfallzugänge.

## Typische Fehler

- Die Organisation regelt Passwörter, vergisst aber API-Keys, Zertifikate und Servicekonten.
- Secrets werden in Tickets oder Chats geteilt, weil der sichere Übergabeweg unpraktisch ist.
- MFA wird eingeführt, aber Ausnahmen werden nie reviewed.
- Servicekonten gehören ehemaligen Projekten und niemand fühlt sich verantwortlich.
- Break-Glass-Zugänge werden getestet, aber die Nutzung wird nicht protokolliert oder reviewed.
- Rotation wird gefordert, aber ohne Owner, Frist oder Nachweis betrieben.
- Secret-Scanning meldet Funde, aber niemand entscheidet Behandlung und Risiko.

## Fiktives Mini-Beispiel

Ein fiktiver Softwaredienstleister findet bei einem Repository-Scan einen API-Key für ein Testsystem. Der Product Owner bestätigt den Systembezug, der Plattform Owner rotiert den Key und prüft Logs auf Nutzung. Im Maßnahmenlog wird festgehalten, dass CI/CD-Secrets künftig nur noch über den freigegebenen Secret-Manager eingebunden werden. Ein zweiter Fund betrifft ein altes Servicekonto ohne Owner; dieser Punkt geht mit Frist in den nächsten Access-Review.

Evidenz:

- Scan-Finding ohne Offenlegung des Secrets,
- Rotationsticket,
- Logprüfvermerk,
- aktualisierte CI/CD-Anweisung,
- Maßnahmenlog für verwaistes Servicekonto.
