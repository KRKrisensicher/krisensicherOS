
# A.6.1 — Sicherheitsprüfung vor Beschäftigung oder Beauftragung

## Zweck

Sicherheitsprüfungen vor Beschäftigung oder Beauftragung helfen, vertrauensrelevante Rollen bewusst zu besetzen und offensichtliche Eignungs-, Integritäts- oder Rollenkonflikte vor dem Zugriff auf schützenswerte Informationen zu klären.

Der Kern ist eine verhältnismäßige, rechtlich geklärte und rollenbezogene Prüfroutine — nicht pauschales Misstrauen und keine ungeprüfte Datensammlung.

## Control-Ziel in Repo-Sprache

Die Organisation legt fest, für welche Rollen vor Beginn einer Tätigkeit welche Sicherheitsprüfung angemessen, zulässig und erforderlich ist. Die Routine verbindet Rollenrisiko, HR-/Beschaffungsprozess, Datenschutz-/Legal-Review, Entscheidung, Dokumentation und Ausnahmebehandlung.

## Typische Risiken

- Wenn Personen mit Zugriff auf kritische Systeme ohne geeignete Vorprüfung starten, können ungeklärte Interessenkonflikte oder Täuschungen unentdeckt bleiben.
- Wenn Prüfungen pauschal und ohne Rechts-/Datenschutzklärung erfolgen, entstehen Datenschutz-, Arbeitsrechts- oder Reputationsrisiken.
- Wenn externe Rollen nicht einbezogen werden, erhalten Dienstleisterzugänge ohne vergleichbare Vertrauensbasis.
- Wenn Ergebnisse nicht entscheidungsfähig dokumentiert werden, bleiben Ausnahmen und Restrisiken unklar.
- Wenn Sicherheitsprüfung und Zugriffserteilung getrennt laufen, können Personen vor Abschluss notwendiger Klärungen produktiv arbeiten.

## Trigger

- geplante Einstellung, Beauftragung oder Einsatz externer Mitarbeitender.
- Besetzung einer Rolle mit privilegiertem Zugriff, sensiblen Daten, Sicherheits-, Finanz-, HR-, Betriebs- oder Entwicklungsverantwortung.
- Wechsel in eine höher kritische Rolle.
- neuer Dienstleister mit Personen im Zugriff auf Systeme, Standorte oder Informationen.
- geänderte Risikoanalyse, Rollenklassifizierung oder rechtliche Rahmenprüfung.
- Auditfinding, Vorfall oder Managemententscheidung zur Vertrauensprüfung.

## Rollen und Verantwortung

- **HR / People-Funktion:** integriert die Prüflogik in Recruiting, Onboarding und Rollenwechsel.
- **Hiring Manager / Führungskraft:** bewertet Rollenbedarf, Kritikalität und Startvoraussetzungen.
- **ISMS-Owner / Security-Rolle:** definiert risikobasierte Kriterien, Mindestanforderungen und Eskalationspunkte.
- **Legal / Datenschutz:** prüft Zulässigkeit, Verhältnismäßigkeit, Informationspflichten, Aufbewahrung und externe Nachweise.
- **Einkauf / Lieferantenmanagement:** stellt Anforderungen an Dienstleisterrollen und Nachweise im Beauftragungsprozess sicher.
- **Management:** entscheidet über Ausnahmen, Restrisiken oder Ressourcenkonflikte.

## Implementierung

### Minimalstart

Ziel: Kritische Rollen starten nicht ohne geklärte Sicherheitsprüfung.

1. Die Organisation benennt Rollen, bei denen vor Beginn eine Sicherheitsprüfung notwendig sein kann.
2. HR, ISMS-Owner und Legal/Datenschutz klären, welche Prüfungen für diese Rollen zulässig und angemessen sind.
3. Der Recruiting- oder Beauftragungsprozess enthält einen Checkpunkt vor Zugriffserteilung.
4. Ergebnisse werden minimal dokumentiert: Prüfung erfolgt, Entscheidung, Datum, Rolle, verantwortliche Stelle.
5. Ausnahmen werden befristet, begründet und vor produktivem Zugriff entschieden.

Minimaler Nachweis:

- Rollenliste mit Prüfkategorie,
- geklärte Prüflogik mit Legal-/Datenschutz-Hinweis,
- Check im Onboarding- oder Beauftragungsprozess,
- Entscheidung vor Zugriffserteilung,
- Ausnahmeentscheidung mit Wiedervorlage.

### Solide Praxis

Ziel: Sicherheitsprüfung ist risikobasiert, wiederholbar und mit Zugriffen verbunden.

1. Rollen werden nach Zugriff, Datenklasse, Privilegien, Außenwirkung und Abhängigkeit klassifiziert.
2. Für jede Prüfkategorie sind zulässige Nachweise, Verantwortliche, Fristen und Aufbewahrungsregeln definiert.
3. Externe Mitarbeitende und Dienstleisterrollen werden in die gleiche Rollenlogik eingebunden.
4. Startfreigabe, Zugriffserteilung und Schulungs-/Verpflichtungsschritte sind miteinander verknüpft.
5. Unvollständige Prüfungen lösen kontrollierte Einschränkung, Eskalation oder Verschiebung des Starts aus.
6. Der Prozess wird regelmäßig anhand von Stichproben und Findings verbessert.

Starke Evidenz:

- Rollen- und Prüfkategorien,
- Prozessnachweis mit Gate vor Zugriffserteilung,
- Freigabe- oder Eskalationsentscheidung,
- Dienstleisteranforderung für eingesetzte Personen,
- Stichprobenreview,
- dokumentierte Ausnahmen mit Ablaufdatum.

### Fortgeschritten

Ziel: Vertrauensprüfung ist Teil des Workforce-, Lieferanten- und Access-Governance-Modells.

1. HR-System, Lieferanten-Onboarding und IAM-Startfreigaben nutzen dieselben Rollen- und Risikokategorien.
2. Kritische Rollen erhalten zusätzliche Human Gates vor privilegiertem Zugriff.
3. Änderungen an Rollenrisiko oder rechtlichem Rahmen führen zu Review der Prüflogik.
4. Kennzahlen zeigen offene Prüfungen, Ausnahmen, verspätete Startfreigaben und kritische Rollen ohne Nachweis.
5. Management bewertet Zielkonflikte zwischen schnellem Staffing, Schutzbedarf und rechtlich zulässiger Prüfung.

## Ablauf als Routine

1. **Rollenbedarf entsteht:** Einstellung, Beauftragung oder Rollenwechsel.
2. **Kritikalität bestimmen:** Zugriff, Daten, Privilegien, Standort- oder Prozessverantwortung bewerten.
3. **Prüfanforderung ableiten:** nur geklärte, verhältnismäßige und rollenbezogene Prüfungen nutzen.
4. **Prüfung durchführen oder Nachweis einholen:** HR, Dienstleister oder berechtigte Stelle bearbeitet den Check.
5. **Entscheidung treffen:** Start freigeben, einschränken, verschieben oder eskalieren.
6. **Zugriff koppeln:** produktiver Zugriff erfolgt erst nach erforderlicher Freigabe oder dokumentierter Ausnahme.
7. **Nachweis ablegen:** nur notwendige Metadaten und Entscheidungen gemäß geklärter Aufbewahrung dokumentieren.
8. **Reviewen:** Stichproben, Ausnahmen und Findings in Prozessverbesserungen überführen.

## Entscheidungen

- Welche Rollen sind prüfrelevant und warum?
- Welche Prüfungen sind für welche Rolle angemessen, zulässig und erforderlich?
- Welche Informationen dürfen gespeichert werden und wie lange?
- Was passiert, wenn eine Prüfung nicht rechtzeitig abgeschlossen ist?
- Wer darf eine Ausnahme vor Start oder Zugriff genehmigen?
- Welche Anforderungen gelten für externe Mitarbeitende und Dienstleister?

## Evidenz

### Starke Evidenz

- Rollenklassifizierung mit Prüfkategorie,
- dokumentierte Legal-/Datenschutzklärung der Prüflogik,
- Onboarding- oder Beauftragungscheck mit Entscheidung vor Zugriff,
- Nachweis, dass Zugriffserteilung an Freigabe gekoppelt ist,
- Ausnahme mit Grund, Laufzeit und Risikoentscheidung,
- Stichprobenprotokoll mit Korrekturmaßnahmen.

### Schwache Evidenz

- pauschale Aussage „Background Checks werden gemacht“ ohne Rollenbezug,
- Kopien sensibler Nachweise ohne geklärte Notwendigkeit,
- HR-Checkliste ohne Verbindung zu Zugriffen,
- Dienstleistervertrag ohne Nachweis für eingesetzte Personen,
- alte Prüfvorgabe ohne Reviewdatum.

### Evidenzlücken

- kritische Rollen ohne definierte Prüfkategorie,
- Zugriff wird vor Abschluss notwendiger Prüfung vergeben,
- externe Rollen fehlen im Prozess,
- keine Ausnahmeentscheidung bei unvollständiger Prüfung,
- keine Datenschutz-/Legal-Klärung der Prüfpraxis.

## Wirksamkeitsprüfung

Prüffragen:

- Sind prüfrelevante Rollen nachvollziehbar klassifiziert?
- Ist die Prüflogik rechtlich und datenschutzseitig menschlich geprüft?
- Wird produktiver Zugriff an die erforderliche Startfreigabe gekoppelt?
- Sind externe Mitarbeitende und Dienstleisterrollen abgedeckt?
- Sind Ausnahmen befristet und entschieden?
- Führen Stichproben zu Korrekturen im Prozess?

Mögliche Kennzahlen:

- kritische Rollen mit definierter Prüfkategorie,
- Starts mit abgeschlossener Prüfung vor Zugriff,
- offene oder verspätete Prüfungen,
- Ausnahmen nach Rolle und Laufzeit,
- externe Rollen ohne vollständigen Nachweis,
- Findings aus Stichproben.

## BSIG-/NIS2-Anschluss

Sicherheitsprüfungen vor Tätigkeitsbeginn sind anschlussfähig an NIS2-orientierte Governance, Risikomanagement, Zugriffsschutz, Lieferkettensteuerung und Sicherheitskultur. Der konkrete Umfang sollte über Rollenmodell, Anforderungsregister und Human Review geprüft werden.

Dieses Artefakt ersetzt keine arbeitsrechtliche, datenschutzrechtliche oder sonstige rechtliche Bewertung.

## Grenzen

- Keine Rechts- oder Datenschutzberatung und keine Empfehlung zu konkreten Prüfarten im Einzelfall.
- Keine pauschale Prüfung aller Personen ohne Rollen- und Verhältnismäßigkeitsbezug.
- Keine Speicherung sensibler Nachweise ohne geklärte Notwendigkeit und Aufbewahrung.
- Keine Zertifizierungs-, Konformitäts- oder Sicherheitsgarantie.
- Keine ISO-27002-Texte oder echten Personendaten.

## Handoffs

- **HR-Handoff:** Recruiting, Onboarding, Rollenwechsel, Startfreigabe und Aufbewahrungslogik.
- **Legal-/Datenschutz-Handoff:** Zulässigkeit, Verhältnismäßigkeit, Informationspflichten, Nachweisarten und Aufbewahrung.
- **Access-Handoff:** Zugriffserteilung, privilegierte Rechte und Startbeschränkungen.
- **Lieferanten-Handoff:** externe Personen, Subdienstleister, Nachweise und Vertragsbezug.
- **Management-Handoff:** Ausnahmen, schwer besetzbare Rollen, Restrisiko oder Zielkonflikt zwischen Staffing und Schutzbedarf.
- **Audit-/Evidence-Handoff:** fehlende Prüfkategorien, unklare Entscheidungen oder nicht nachvollziehbare Ausnahmen.

## Typische Fehler

- Sicherheitsprüfung wird pauschal statt rollenbezogen angewendet.
- HR prüft, aber IT vergibt Zugriffe unabhängig davon.
- Externe Mitarbeitende werden nicht gleichwertig betrachtet.
- Zu viele personenbezogene Details werden gespeichert, obwohl eine Ja-/Nein-Entscheidung reichen würde.
- Ausnahmen entstehen informell, damit ein Starttermin gehalten wird.
- Der Prozess wird nie gegen aktuelle Rollen, Risiken und Rechtslage reviewed.

## Fiktives Mini-Beispiel

Ein fiktives Unternehmen besetzt eine Administratorenrolle für zentrale Identitätsdienste. HR erkennt die Rolle als prüfrelevant, Legal und Datenschutz haben die zulässige Prüflogik bereits freigegeben. Vor Start wird der Check abgeschlossen und im Onboarding nur die Entscheidung „freigegeben am Datum“ dokumentiert. Die IAM-Freigabe verweist auf diesen Status. Für einen externen Spezialisten, der kurzfristig unterstützen soll, wird eine befristete Ausnahme mit eingeschränktem Zugriff und Managementfreigabe dokumentiert.

Evidenz:

- Rollenklassifizierung „kritische Adminrolle“,
- dokumentierter Prüfgate im Onboarding,
- Startfreigabe vor IAM-Zugriff,
- Ausnahmeentscheidung für externen Spezialisten,
- Wiedervorlage zur Ausnahme.
