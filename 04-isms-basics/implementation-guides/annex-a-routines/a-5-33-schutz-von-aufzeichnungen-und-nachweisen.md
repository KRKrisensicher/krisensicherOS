
# A.5.33 — Schutz von Aufzeichnungen und Nachweisen

## Zweck

Diese Routine sorgt dafür, dass geschäfts-, sicherheits- und nachweisrelevante Aufzeichnungen nicht zufällig entstehen, verstreut liegen oder ungeprüft verändert werden. Sie schützt Nachweise so, dass Entscheidungen, Reviews, Vorfälle, Audits und Managementfragen nachvollziehbar bleiben.

Der Kern ist nicht maximale Dokumentenmenge, sondern belastbare Evidenz: Welche Aufzeichnung ist wichtig, wer ist verantwortlich, wie lange wird sie benötigt, wie wird sie geschützt und wann darf sie gelöscht oder archiviert werden?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine für Erstellung, Ablage, Schutz, Zugriff, Aufbewahrung, Integrität, Wiederauffindbarkeit und geordnete Löschung relevanter Aufzeichnungen. Dabei werden rechtliche, vertragliche, Datenschutz- und Geschäftsanforderungen über zuständige menschliche Rollen geklärt.

## Typische Risiken

- Wenn Sicherheitsnachweise nachträglich nicht auffindbar sind, können Entscheidungen, Vorfälle oder Reviews nicht belegt werden.
- Wenn Aufzeichnungen unkontrolliert verändert werden können, verliert Evidenz ihre Aussagekraft.
- Wenn sensible Nachweise zu breit zugänglich sind, entstehen Vertraulichkeits- und Datenschutzrisiken.
- Wenn Aufbewahrungsfristen unklar sind, werden Nachweise zu früh gelöscht oder unnötig lange gehalten.
- Wenn Protokolle, Freigaben und Ausnahmen nur in persönlichen Postfächern liegen, ist die Organisation abhängig von Einzelpersonen.
- Wenn automatisierte Logs und manuelle Dokumente nicht verbunden sind, bleiben Lücken im Ereignis- oder Entscheidungsverlauf.

## Trigger

- neuer Prozess, neues System, neues Register, neuer Dienstleister oder neuer Nachweistyp.
- Audit, interne Prüfung, Kundenanforderung, Managementfrage oder Nachweisanfrage.
- Sicherheitsereignis, Datenschutzvorfallverdacht, Eskalation oder Lessons Learned.
- Änderung von Aufbewahrungs-, Vertrags-, Legal- oder Datenschutzanforderungen.
- Migration, Archivierung, Systemabschaltung oder Wechsel der Ablageplattform.
- geplanter Review von Evidence Packs, Logs, Freigaben, Ausnahmen oder Managemententscheidungen.
- Rollenwechsel oder Austritt von Personen mit Nachweisverantwortung.

## Rollen und Verantwortung

- **Record Owner / Prozess Owner:** legt fest, welche Aufzeichnungen entstehen, wofür sie benötigt werden und wer sie pflegt.
- **ISMS-Owner:** definiert Mindestanforderungen für Sicherheitsnachweise, Reviewlogik und Evidence Packs.
- **IT-/Plattform Owner:** stellt Ablage, Backup, Zugriff, Protokollierung und technische Schutzmaßnahmen bereit.
- **Legal:** bewertet rechtliche Aufbewahrung, Beweisbedarf, Vertragsanforderungen und Löschsperren.
- **Datenschutz:** prüft personenbezogene Inhalte, Speicherbegrenzung, Zugriffsbedarf und Löschlogik.
- **Fachbereiche:** erzeugen fachliche Freigaben, Entscheidungen, Reviews und Betriebsnachweise.
- **Interne Prüfung / Audit:** prüft Nachvollziehbarkeit, Vollständigkeit und Evidenzqualität.
- **Management:** entscheidet bei Ressourcenbedarf, Aufbewahrungs-/Löschkonflikten oder akzeptierten Evidenzlücken.

## Implementierung

### Minimalstart

Ziel: Die wichtigsten Nachweise sind auffindbar, geschützt und verantwortet.

1. Kritische Nachweistypen werden benannt: Policies, Freigaben, Risikoentscheidungen, Ausnahmen, Zugriffsreviews, Incident-Nachweise, Lieferantennachweise, Schulungsnachweise.
2. Für jeden Nachweistyp wird ein Owner und ein Ablageort festgelegt.
3. Zugriff wird auf Rollen begrenzt, die Nachweise erstellen, prüfen oder entscheiden müssen.
4. Änderungen an kritischen Nachweisen bleiben nachvollziehbar, etwa über Versionierung, Ticket oder Protokoll.
5. Ein einfacher Review prüft regelmäßig, ob Nachweise vorhanden, aktuell und wiederauffindbar sind.
6. Unklare Aufbewahrung oder Löschung wird an Legal/Datenschutz eskaliert.

Minimaler Nachweis:

- Nachweistypenliste mit Owner,
- definierter Ablageort,
- Zugriffs- oder Rollenübersicht,
- Reviewnotiz zur Auffindbarkeit,
- dokumentierte Klärung offener Aufbewahrungs- oder Löschfragen.

### Solide Praxis

Ziel: Records Management und ISMS-Evidenz werden wiederholbar betrieben.

1. Ein Nachweisregister beschreibt Zweck, Owner, Schutzbedarf, Aufbewahrung, Zugriff, Format und Reviewfrequenz.
2. Kritische Nachweise erhalten Versionierung, Änderungsprotokoll oder Freigabestatus.
3. Aufzeichnungen werden nach Vertraulichkeit und Integritätsbedarf klassifiziert.
4. Evidence Packs werden pro Prozess, Control oder Auditfrage zusammengestellt, ohne Originalnachweise unkontrolliert zu kopieren.
5. Archivierung, Löschung und Sperrung werden mit Legal und Datenschutz abgestimmt.
6. Systemabschaltungen und Migrationen enthalten einen Records-Check.
7. Findings führen zu Korrekturen im Ablage-, Zugriff- oder Erstellungsprozess.

Starke Evidenz:

- Nachweisregister,
- Ablage- und Zugriffskonzept,
- Versionierungs- oder Änderungsnachweise,
- Reviewprotokolle zu Evidenzqualität,
- Archivierungs- oder Löschentscheidungen,
- Evidence Pack mit Quellenverweisen,
- Maßnahmenlog zu Evidenzlücken.

### Fortgeschritten

Ziel: Nachweise sind in Governance, Betrieb und Auditfähigkeit integriert.

1. Ticketing, GRC, DMS, SIEM, IAM, Schulungs- und Lieferantenprozesse liefern Nachweise strukturiert und referenzierbar.
2. Wichtige Entscheidungen erhalten eindeutige Referenzen, Owner, Ablaufdatum und Risiko-/Control-Bezug.
3. Integrität und Zugriff kritischer Nachweise werden technisch überwacht oder regelmäßig geprüft.
4. Retention- und Löschregeln werden automatisiert unterstützt, aber nur nach geklärter fachlicher Verantwortung angewendet.
5. Evidence Packs zeigen nicht nur Dokumente, sondern Durchführung, Review, Entscheidung und Verbesserung.
6. Management erhält entscheidungsfähige Sicht auf Evidenzlücken, überfällige Reviews und nicht prüfbare Prozesse.

## Ablauf als Routine

1. **Nachweistyp entsteht oder ändert sich:** neuer Prozess, Review, Entscheidung, Incident, Auditfrage oder Systemlog.
2. **Zweck bestimmen:** Wofür wird der Nachweis benötigt und welche Entscheidung oder Prüfung unterstützt er?
3. **Owner und Ablage festlegen:** Verantwortlichkeit, Speicherort, Zugriff und Schutzbedarf klären.
4. **Erstellungslogik definieren:** Format, Mindestinhalt, Freigabe, Versionierung und Referenzen festlegen.
5. **Schützen:** Zugriff, Integrität, Backup, Archivierung und Vertraulichkeit umsetzen.
6. **Reviewen:** Stichprobe auf Vollständigkeit, Aktualität, Lesbarkeit, Wiederauffindbarkeit und Entscheidungstauglichkeit.
7. **Lücken behandeln:** fehlende, unklare oder veraltete Nachweise korrigieren oder als Risiko eskalieren.
8. **Aufbewahrung klären:** Löschung, Archivierung oder Sperrung nach fachlicher, Legal- und Datenschutzprüfung steuern.

## Entscheidungen

- Welche Aufzeichnungen sind geschäfts-, sicherheits- oder auditkritisch?
- Welche Nachweise müssen veränderungssicher, versioniert oder besonders zugriffsgeschützt sein?
- Wer darf Nachweise erstellen, ändern, prüfen, exportieren oder löschen?
- Welche Aufbewahrungs- und Löschregeln gelten pro Nachweistyp?
- Welche Evidenzlücken sind tolerierbar, welche müssen ins Management Review?
- Wie werden Nachweise aus Tools, E-Mails, Tickets und Dokumenten zusammengeführt?

## Evidenz

### Starke Evidenz

- Nachweisregister mit Owner, Zweck, Schutzbedarf und Reviewdatum,
- definierte Ablageorte und Zugriffsgruppen,
- Versionierungs-, Freigabe- oder Änderungsprotokolle,
- Stichprobenreview mit Findings und Maßnahmen,
- nachvollziehbare Archivierungs-, Lösch- oder Sperrentscheidungen,
- Evidence Packs mit Quellen, Datum und Verantwortlichen,
- Managemententscheidung zu kritischen Evidenzlücken.

### Schwache Evidenz

- unsortierte Dokumentenablage ohne Owner,
- Screenshots ohne Datum, Quelle oder Kontext,
- alte Policies ohne Freigabestatus,
- Exportlisten ohne Schutzbedarf oder Zugriffskontrolle,
- Nachweise ausschließlich in persönlichen Postfächern,
- pauschale Backup-Aussage ohne Wiederauffindbarkeit kritischer Records.

### Evidenzlücken

- keine Übersicht kritischer Nachweistypen,
- unklare Aufbewahrung oder Löschpraxis,
- fehlende Änderungsnachvollziehbarkeit,
- keine Reviewnachweise,
- Evidence Packs ohne Originalquellen,
- ungeschützte personenbezogene oder vertrauliche Nachweise,
- Systemmigration ohne Records-Übernahme.

## Wirksamkeitsprüfung

Prüffragen:

- Können kritische Nachweise innerhalb angemessener Zeit gefunden und verstanden werden?
- Ist nachvollziehbar, wer einen Nachweis erstellt, geprüft oder geändert hat?
- Sind Vertraulichkeit, Integrität und Verfügbarkeit der wichtigsten Nachweise angemessen gesteuert?
- Gibt es Aufbewahrungs- und Löschentscheidungen mit Legal-/Datenschutz-Handoff?
- Zeigen Evidence Packs tatsächliche Durchführung und Entscheidung, nicht nur Absicht?
- Werden Evidenzlücken als Maßnahmen oder Risiken nachverfolgt?

Mögliche Kennzahlen:

- Anteil kritischer Nachweistypen mit Owner und Ablageort,
- überfällige Evidenzreviews,
- offene Evidenzlücken nach Kritikalität,
- Nachweise mit unklarem Aufbewahrungsstatus,
- Wiederauffindungszeit in Stichproben,
- Anzahl unkontrollierter persönlicher Ablagen für kritische Nachweise.

## BSIG-/NIS2-Anschluss

Der Schutz von Aufzeichnungen und Nachweisen ist anschlussfähig an NIS2-orientierte Governance, Risikomanagement, Incident Handling, Lieferkettensicherheit, Managementaufsicht und Nachweisfähigkeit. Der konkrete Bezug sollte über ein Anforderungsregister und die organisationsspezifische Nachweisstrategie geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung von Aufbewahrungsfristen, Beweisfragen, Datenschutzpflichten oder Meldepflichten.

## Grenzen

- Keine Rechts- oder Datenschutzberatung.
- Keine Aussage, dass vorhandene Dokumente Konformität oder Sicherheit belegen.
- Kein Ersatz für Records-Management-, Archivierungs- oder DMS-Konzept.
- Keine ISO-27002-Texte oder Zertifizierungszusage.
- Keine echten Kunden-, Personen-, Vertrags- oder Geheimdaten in öffentlichen Beispielen.

## Handoffs

- **Legal-Handoff:** Aufbewahrung, Löschsperre, Vertragsnachweise, Streitfälle, Beweisbedarf.
- **Datenschutz-Handoff:** personenbezogene Nachweise, Speicherbegrenzung, Auskunfts-/Löschbezug, Zugriffsbeschränkung.
- **IT-/Plattform-Handoff:** DMS, Backup, Logging, Versionierung, Zugriffsrechte, Migration.
- **Incident-Handoff:** Sicherung vorfallrelevanter Nachweise und Schutz vor Veränderung.
- **Audit-/Evidence-Handoff:** Evidence Pack, Stichprobe, fehlende oder schwache Nachweise.
- **Management-Handoff:** nicht behebbare Evidenzlücken, Ressourcenbedarf, Aufbewahrungs-/Löschkonflikte.

## Typische Fehler

- Nachweise werden nur für Audits gesammelt und nicht als Betriebsartefakt geführt.
- Kritische Entscheidungen liegen in Chatverläufen oder persönlichen E-Mails.
- Evidence Packs kopieren sensible Daten unnötig breit.
- Löschung wird technisch automatisiert, ohne fachliche, Legal- oder Datenschutzklärung.
- Versionen und Freigaben sind nicht unterscheidbar.
- Logs werden aufbewahrt, aber niemand kann sie einer Entscheidung oder Untersuchung zuordnen.
- Ablageorte ändern sich bei Toolwechseln, ohne Records-Migration.

## Fiktives Mini-Beispiel

Ein fiktiver Dienstleister bereitet ein internes ISMS-Review vor. Dabei fällt auf, dass Ausnahmen, Berechtigungsreviews und Lieferantennachweise in unterschiedlichen Teamordnern liegen. Der ISMS-Owner erstellt ein Nachweisregister, benennt Owner und legt einen Evidence-Pack-Ordner mit Quellenverweisen an. Datenschutz prüft, dass keine unnötigen personenbezogenen Details kopiert werden. Eine fehlende Ausnahmeentscheidung wird als Maßnahme ins Review gegeben.

Evidenz:

- Nachweisregister,
- definierter Evidence-Pack-Ablageort,
- Zugriffsgruppe,
- Reviewnotiz mit Evidenzlücke,
- Maßnahmenticket zur fehlenden Ausnahmeentscheidung.
