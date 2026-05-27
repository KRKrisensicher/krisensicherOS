
# A.8.4 — Zugriff auf Quellcode und Entwicklungsartefakte steuern

## Zweck

Quellcode, Build-Skripte, Repositories, Artefaktablagen, Container-Images, CI/CD-Konfigurationen und Entwicklungsdokumentation sind nicht nur technische Arbeitsmittel. Sie können Geschäftslogik, Schwachstellen, Zugangsdatenfragmente, Architekturwissen und Manipulationsmöglichkeiten enthalten.

Diese Routine sorgt dafür, dass Zugriff auf Entwicklungsartefakte bewusst vergeben, getrennt, überprüft und entzogen wird. Der Kern ist nicht „Repository privat“, sondern eine nachvollziehbare Steuerung: Wer darf Code lesen, ändern, mergen, bauen, veröffentlichen oder Artefakte abrufen — und warum?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Zugriffsroutine für Quellcode und Entwicklungsartefakte. Sie verbindet Repository-Scope, Rollen, Schutzbedarf, Freigaben, technische Berechtigungen, Review, Ausnahmen und Handoffs zu Secure Development, IAM, Lieferantenmanagement und Incident Response.

## Typische Risiken

- Wenn ehemalige Mitarbeitende oder Dienstleister Repository-Zugriff behalten, können Code, Geheimnisse oder Architekturwissen abfließen.
- Wenn Schreib-, Merge- oder Release-Rechte zu breit vergeben sind, können fehlerhafte oder manipulierte Änderungen in produktive Artefakte gelangen.
- Wenn CI/CD-Tokens, Deploy-Keys oder Artefaktzugriffe nicht gesteuert werden, entstehen verdeckte privilegierte Zugänge.
- Wenn externe Entwickler ohne klare Trennung arbeiten, können Mandanten-, Kunden- oder Produktgrenzen verletzt werden.
- Wenn Open-Source-, Fork- oder Mirror-Workflows ungeklärt sind, können vertrauliche Entwicklungsstände öffentlich oder unkontrolliert geteilt werden.
- Wenn Rechte nicht reviewed werden, wachsen Berechtigungen über Rollenwechsel und Projektende hinaus.

## Trigger

- neues Repository, neue Build-Pipeline, neue Artefaktablage oder neuer Entwicklungsdienst.
- neues Produkt, neues Projektteam, externer Entwicklungsauftrag oder Open-Source-Veröffentlichung.
- Eintritt, Rollenwechsel, Projektende oder Austritt von Entwicklern, Admins oder Dienstleistern.
- Änderung von Branching-, Review-, Release- oder Deployment-Prozessen.
- Sicherheitsereignis, kompromittierter Entwickleraccount, verdächtiger Commit oder Secret-Leak.
- Auditfinding, Schwachstellenbefund oder Lieferantenwechsel.
- turnusmäßiger Review kritischer Repositories, Adminrechte und Maschinenidentitäten.

## Rollen und Verantwortung

- **Product Owner / Service Owner:** bewertet fachlichen Bedarf und Kritikalität des Codes oder Artefakts.
- **Repository Owner / Tech Lead:** verantwortet Berechtigungsmodell, Branch-Schutz, Reviewregeln und Teamzugänge.
- **Plattform-/DevOps Owner:** betreibt Repository-Plattform, CI/CD, Artefaktablage, Tokens und technische Kontrollen.
- **Security-Rolle / ISMS-Owner:** definiert Mindestanforderungen, Reviewlogik, Ausnahmebehandlung und Eskalation.
- **Entwicklungsteam:** beantragt Zugriffe nachvollziehbar und meldet Auffälligkeiten oder falsche Berechtigungen.
- **HR / Projektmanagement:** liefert Eintritts-, Rollenwechsel-, Projektende- und Austrittsereignisse.
- **Einkauf / Lieferantenmanagement:** steuert externe Entwicklungszugriffe und Vertragsende.
- **Management:** entscheidet bei Restrisiken, Ressourcenkonflikten oder dauerhaft nicht trennbaren Rechten.

## Implementierung

### Minimalstart

Ziel: kritische Repositories und Entwicklungsartefakte sichtbar und zugriffsgesteuert betreiben.

1. Kritische Repositories, CI/CD-Projekte und Artefaktablagen werden mit Owner benannt.
2. Zugriff wird in Leserechte, Schreibrechte, Merge-/Adminrechte, Release-Rechte und technische Identitäten unterschieden.
3. Neue Zugriffe werden per Ticket oder nachvollziehbarer Freigabe vergeben.
4. Externe Zugriffe und Adminrechte werden separat markiert.
5. Projektende, Rollenwechsel und Austritt lösen eine Rechteprüfung aus.
6. Mindestens quartalsweise werden kritische Repositories, Adminrechte, Deploy-Keys und Tokens reviewed.

Minimaler Nachweis:

- Liste kritischer Repositories und Artefaktablagen mit Owner,
- Zugriffsantrag oder Freigabe,
- Berechtigungsexport zum Reviewzeitpunkt,
- Nachweis entzogener oder korrigierter Rechte,
- Ausnahme mit Ablaufdatum.

### Solide Praxis

Ziel: Zugriff auf Entwicklungsartefakte wird rollen- und risikobasiert gesteuert.

1. Repository- und Artefaktklassen werden nach Kritikalität, Exposition und Produktbezug unterschieden.
2. Standardrollen werden definiert: Reader, Contributor, Maintainer, Release Owner, Admin, CI/CD-Servicekonto.
3. Branch-Schutz, Reviewpflichten, Merge-Regeln und Release-Freigaben werden mit Berechtigungen verbunden.
4. Dienstleisterzugriffe werden befristet und an Auftrag, Projekt oder Vertrag gekoppelt.
5. Maschinenidentitäten erhalten Owner, Zweck, Berechtigungsumfang, Rotation und Ablaufdatum.
6. Secret-Scanning-, Commit-Signatur- oder Schutzmechanismen werden dort eingesetzt, wo Risiko und Tooling es rechtfertigen.
7. Reviewbefunde führen zu Entzug, Korrektur, Ausnahme oder Managemententscheidung.

### Fortgeschritten

Ziel: Quellcodezugriff wird in Secure Development, IAM und Lieferkette integriert.

1. Repository-Plattform, Identitätsquelle, Projektportfolio und Offboarding-Prozess sind verbunden.
2. Kritische Rechte werden automatisiert ausgewertet: Admins, externe Nutzer, inaktive Nutzer, nicht zuordenbare Tokens, öffentliche Repositories.
3. CI/CD-Rechte folgen Least-Privilege-Logik und werden über geschützte Umgebungen, getrennte Secrets und Freigabepfade gesteuert.
4. Auffällige Repository-Aktivitäten fließen in Security Monitoring und Incident Triage.
5. Open-Source-Veröffentlichungen und Code-Sharing durchlaufen eine eigene Freigaberoutine.
6. Management erhält entscheidungsfähige Kennzahlen zu Reviewabdeckung, überfälligen externen Zugängen, Adminrechten und Ausnahmequote.

## Ablauf als Routine

1. **Zugriffsbedarf entsteht:** neues Teammitglied, Dienstleister, Projekt, Tool, Pipeline oder Release-Verantwortung.
2. **Antrag erfassen:** Repository oder Artefakt, Rolle, Zweck, Dauer, Projektbezug und externer Status dokumentieren.
3. **Fachlich prüfen:** Owner bestätigt Bedarf, Schutzbedarf und geeignete Rolle.
4. **Sicherheitslogik prüfen:** Admin-, Release-, CI/CD-, externe oder öffentliche Zugriffe gesondert bewerten.
5. **Technisch umsetzen:** Plattformteam setzt Rechte, Gruppen, Branch-Schutz oder Token-Berechtigungen um.
6. **Nachweis ablegen:** Antrag, Entscheidung, Umsetzung und Ablaufdatum bleiben nachvollziehbar.
7. **Review durchführen:** Owner prüft kritische Rechte, externe Zugriffe, technische Identitäten und Auffälligkeiten.
8. **Korrigieren oder eskalieren:** unnötige Rechte entziehen, Ausnahmen befristen, Restrisiken entscheiden lassen.
9. **Lernen:** Findings in Rollenmodell, CI/CD-Design, Onboarding oder Lieferantensteuerung zurückführen.

## Entscheidungen

- Welche Repositories, Pipelines und Artefaktablagen sind kritisch genug für engere Steuerung?
- Wer darf lesen, schreiben, mergen, releasen, Secrets verwalten oder Adminrechte halten?
- Welche externen Zugriffe sind befristet zulässig?
- Wie werden technische Identitäten, Deploy-Keys und CI/CD-Tokens begrenzt?
- Welche Code- oder Artefaktfreigaben brauchen Security-, Legal- oder Management-Handoff?
- Wann wird ein Zugriffsvorfall zum Incident?

## Evidenz

### Starke Evidenz

- aktueller Repository-/Artefakt-Scope mit Ownern,
- Rollen- und Gruppenmodell für Entwicklungszugriffe,
- Zugriffsanträge mit Begründung und Freigabe,
- Berechtigungsexporte für kritische Repositories und CI/CD-Projekte,
- Reviewprotokolle mit Entscheidungen und Korrekturen,
- Nachweise entzogener externer oder privilegierter Rechte,
- Token-/Deploy-Key-Register mit Owner, Zweck und Ablaufdatum,
- Managemententscheidung bei akzeptierten Ausnahmen.

### Schwache Evidenz

- allgemeine Aussage „Repositories sind privat“ ohne Review,
- Screenshot einzelner Teammitglieder ohne Owner oder Datum,
- Repository-Policy ohne technische Umsetzung,
- Adminliste ohne Begründung,
- externe Zugänge ohne Projekt- oder Vertragsbezug,
- Secret-Scanning-Report ohne Behandlung der Findings.

### Evidenzlücken

- keine Übersicht kritischer Repositories oder Artefaktablagen,
- keine Zuordnung technischer Identitäten,
- keine Prüfung nach Projektende oder Austritt,
- keine Trennung zwischen Lese-, Schreib-, Merge- und Release-Rechten,
- dauerhaft öffentliche oder externe Zugriffe ohne Entscheidung,
- keine Reviewnachweise für CI/CD- und Artefaktzugriffe.

## Wirksamkeitsprüfung

Prüffragen:

- Können kritische Repositories einem Owner und einem Berechtigungsmodell zugeordnet werden?
- Sind externe, privilegierte und technische Zugriffe besonders sichtbar?
- Werden Rechte nach Projektende, Rollenwechsel und Austritt zeitnah entzogen?
- Gibt es Nachweise, dass Reviews zu Korrekturen geführt haben?
- Sind Branch-, Merge- und Release-Regeln mit den Berechtigungen konsistent?
- Werden Secret-Leaks oder verdächtige Repository-Aktivitäten in Incident- oder Schwachstellenprozesse übergeben?

Mögliche Kennzahlen:

- Anteil kritischer Repositories mit Owner,
- überfällige Zugriffsreviews,
- Anzahl externer und privilegierter Zugriffe,
- inaktive Nutzer mit Zugriff,
- technische Identitäten ohne Ablaufdatum,
- korrigierte Rechte pro Review,
- offene Ausnahmen.

## BSIG-/NIS2-Anschluss

Die Steuerung von Quellcode- und Entwicklungsartefaktzugriffen ist anschlussfähig an NIS2-orientierte Themen wie sichere Entwicklung, Zugriffsschutz, Lieferkettensicherheit, Schwachstellenmanagement, Cyberhygiene und Incident-Prävention. Der konkrete Bezug sollte organisationsspezifisch im Anforderungsregister und in der Risikoanalyse geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung, keine Datenschutzprüfung und keine Aussage zur Anwendbarkeit einzelner Pflichten.

## Grenzen

- Dieses Artefakt ist kein vollständiges Secure-Development-Framework.
- Es ersetzt keine Codeanalyse, Architekturprüfung oder Lizenzprüfung.
- Es liefert keine verbindliche Vorgabe für konkrete Repository-Tools.
- Keine Zertifizierungs-, Konformitäts- oder Sicherheitsgarantie.
- Keine ISO-27002-Texte und keine vertraulichen Repository- oder Produktdetails in öffentlichen Beispielen.

## Handoffs

- **IAM-Handoff:** Rollenwechsel, Austritt, Gruppenmodell, privilegierte und technische Identitäten.
- **Secure-Development-Handoff:** Branch-Schutz, Reviews, Secrets, Build- und Release-Regeln.
- **Incident-Handoff:** verdächtige Commits, kompromittierte Accounts, Secret-Leak, unberechtigter Zugriff.
- **Lieferanten-Handoff:** externe Entwickler, Projektende, Vertragsbindung, Managed Development.
- **Legal-/Datenschutz-Handoff:** Open-Source-Veröffentlichung, personenbezogene Daten in Repositories, Lizenz- oder Geheimhaltungsthemen.
- **Management-Handoff:** dauerhafte Ausnahmen, nicht trennbare Release-Rechte, Ressourcenbedarf.
- **Audit-/Evidence-Handoff:** fehlende Reviewnachweise, nicht zuordenbare Tokens, unvollständiger Repository-Scope.

## Typische Fehler

- Repository-Zugriff wird wie normaler Dateizugriff behandelt.
- Adminrechte bleiben bei ehemaligen Tech Leads oder Dienstleistern aktiv.
- CI/CD-Tokens werden nicht als privilegierte Zugänge betrachtet.
- Branch-Schutz existiert, aber Maintainer können ihn ohne Review umgehen.
- Externe Entwickler werden projektweise eingeladen, aber nicht projektweise entfernt.
- Öffentliche Repositories, Forks oder Mirrors werden nicht in die Routine einbezogen.
- Management sieht nur Toolberichte, aber keine entscheidungsfähigen Restrisiken.

## Fiktives Mini-Beispiel

Ein fiktives Softwareteam beendet ein Kundenportal-Projekt mit einem externen Entwicklungspartner. Der Repository Owner zieht einen Berechtigungsexport, markiert externe Konten und findet zwei aktive Deploy-Keys ohne Owner. Das Plattformteam entfernt die externen Konten, ersetzt die Deploy-Keys durch ein befristetes Servicekonto und dokumentiert die Änderung im Ticket. Im nächsten Review entscheidet der Service Owner, dass Release-Rechte künftig monatlich geprüft werden.

Evidenz:

- Repository-Scope mit Owner,
- Berechtigungsexport,
- Ticket zum Entzug externer Zugänge,
- neues Servicekonto mit Zweck und Ablaufdatum,
- Reviewentscheidung zur Release-Rechteprüfung.
