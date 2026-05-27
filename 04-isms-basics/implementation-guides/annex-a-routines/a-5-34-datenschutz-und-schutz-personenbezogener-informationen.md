
# A.5.34 — Datenschutz und Schutz personenbezogener Informationen

## Zweck

Diese Routine verbindet Informationssicherheit mit dem Schutz personenbezogener Informationen. Sie hilft Organisationen, personenbezogene Daten nicht nur als Rechts- oder Datenschutzthema zu behandeln, sondern als betrieblichen Schutzbereich mit Ownern, Datenflüssen, Zugriffen, technischen Maßnahmen, Evidenz und klaren Handoffs.

Der Kern ist keine Datenschutzberatung durch das ISMS, sondern eine belastbare Zusammenarbeit: Security macht Risiken, Systeme, Zugriffe und Schutzmaßnahmen sichtbar; Datenschutz und verantwortliche Fachrollen bewerten Rechtsgrundlagen, Betroffenenrechte und Pflichten.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der personenbezogene Informationen in Prozessen, Systemen, Dienstleistern und Sicherheitsmaßnahmen erkannt, geschützt, reviewed und bei Änderungen an Datenschutz, Legal, Fachbereich oder Management übergeben werden. Schutzbedarf, Zugriff, Protokollierung, Weitergabe, Löschung und Incident-Fähigkeit bleiben nachvollziehbar.

## Typische Risiken

- Wenn personenbezogene Daten in Systemen oder Schattenprozessen unbekannt bleiben, können Schutzmaßnahmen, Löschung und Incident-Bewertung nicht greifen.
- Wenn Zugriffe auf Beschäftigten-, Kunden- oder Nutzungsdaten zu breit sind, entstehen Vertraulichkeits- und Missbrauchsrisiken.
- Wenn Logs, Monitoring oder KI-Tools personenbezogene Daten verarbeiten, ohne Datenschutzklärung, entstehen Governance- und Vertrauensrisiken.
- Wenn Dienstleister personenbezogene Informationen verarbeiten, aber technische und organisatorische Schutzpunkte nicht nachverfolgt werden, bleiben Lieferkettenrisiken offen.
- Wenn Lösch-, Sperr- oder Aufbewahrungslogiken nicht mit Systembetrieb verbunden sind, werden Daten zu lange, zu kurz oder widersprüchlich gehalten.
- Wenn ein Sicherheitsereignis personenbezogene Informationen betrifft, aber Handoffs unklar sind, verzögern sich Bewertung, Entscheidung und Kommunikation.

## Trigger

- neuer oder geänderter Prozess mit Beschäftigten-, Kunden-, Nutzer-, Bewerber- oder Kontaktdaten.
- neues System, SaaS-Tool, KI-Tool, Schnittstelle, Datenexport oder Reporting.
- Änderung von Datenklasse, Schutzbedarf, Zugriffen, Protokollierung oder Aufbewahrung.
- Dienstleisterwechsel, neue Unterauftragnehmer, Cloud-Region oder Datenübermittlung.
- Sicherheitsereignis, Datenabflussverdacht, Fehlversand, Fehlberechtigung oder verlorenes Gerät.
- Auditfinding, Datenschutzanfrage, Managementfrage oder interne Prüfung.
- geplanter Review von Verarbeitungen, Zugriffen, Logs, Löschkonzepten oder Schutzmaßnahmen.

## Rollen und Verantwortung

- **Fachlicher Prozess Owner:** kennt Zweck, Datenarten, Nutzergruppen und Geschäftsbedarf der Verarbeitung.
- **Datenschutzrolle / DSB:** bewertet Datenschutzanforderungen, Rechtsgrundlagen, Betroffenenrechte, TOMs und Datenschutzfolgenfragen.
- **ISMS-Owner / Security-Rolle:** verbindet personenbezogene Informationen mit Schutzbedarf, Risiken, Controls, Incident-Fähigkeit und Evidenz.
- **IT-/Plattform Owner:** setzt Zugriff, Verschlüsselung, Logging, Backup, Löschung und technische Schutzmaßnahmen um.
- **HR / People-Funktion:** verantwortet Beschäftigtendatenprozesse und arbeitsbezogene Handoffs.
- **Einkauf / Vendor Management:** hält Dienstleister, Vertrags- und Nachweisbezüge nach.
- **Incident Response:** koordiniert technische Analyse und Handoffs bei Sicherheitsereignissen.
- **Management:** entscheidet Ressourcen, Restrisiken, Priorisierung und externe Kommunikation nach zuständiger Prüfung.

## Implementierung

### Minimalstart

Ziel: Personenbezogene Informationen im ISMS-Scope sind sichtbar und erhalten klare Handoffs.

1. Die wichtigsten Prozesse und Systeme mit personenbezogenen Informationen werden gelistet.
2. Für jeden Eintrag werden Owner, Datenkategorien, betroffene Personengruppen, Dienstleister und Schutzbedarf grob erfasst.
3. Kritische Zugriffe werden überprüft: Admins, Fachrollen, externe Rollen und technische Konten.
4. Sicherheitsmaßnahmen werden zugeordnet: Zugriffsschutz, MFA, Verschlüsselung, Backup, Logging, Lösch-/Sperrpfad, Incident-Meldeweg.
5. Unklare Rechts-, Datenschutz- oder Löschfragen werden nicht im ISMS entschieden, sondern an Datenschutz/Legal übergeben.
6. Sicherheitsereignisse mit möglichem Personenbezug erhalten einen festen Datenschutz-Handoff.

Minimaler Nachweis:

- Prozess-/Systemliste mit personenbezogenen Informationen,
- Owner und Schutzbedarf,
- Zugriffsstichprobe für kritische Systeme,
- Handoff-Nachweis an Datenschutz bei offenen Fragen,
- Incident-Checkpunkt für personenbezogene Informationen.

### Solide Praxis

Ziel: Datenschutz- und Security-Routinen arbeiten wiederholbar zusammen.

1. Verarbeitungsübersichten, Assetinventar, Risikoregister und Maßnahmenlog werden miteinander referenziert.
2. Neue Systeme und Prozessänderungen durchlaufen einen Security-/Datenschutz-Check vor produktiver Nutzung.
3. Protokollierung, Monitoring und Auswertungen werden auf Personenbezug und Zweckbindung geprüft.
4. Dienstleister mit personenbezogenen Informationen werden mit Sicherheitsnachweisen und Datenschutz-Handoffs nachverfolgt.
5. Lösch-, Sperr- und Aufbewahrungsanforderungen werden in Betrieb, Backup, Archivierung und Anwendungen übersetzt.
6. Zugriffreviews berücksichtigen besonders sensible Daten, Beschäftigtendaten und externe Zugriffe.
7. Incidents, Fehlberechtigungen und Findings führen zu Maßnahmen im ISMS und Datenschutzprozess.

Starke Evidenz:

- referenzierte Verarbeitungs-/Asset-/Risikoeinträge,
- Security-/Datenschutz-Checklisten für Änderungen,
- Zugriffreviews für Systeme mit Personenbezug,
- technische Nachweise für Schutzmaßnahmen,
- Dienstleister- und Vertragsreferenzen,
- Incident-Handoff-Protokolle,
- Maßnahmenlog zu Datenschutz-/Security-Findings.

### Fortgeschritten

Ziel: Personenbezogener Informationsschutz ist in Architektur, Tooling und Lagebild integriert.

1. Datenflüsse, Datenklassifizierung, Assetinventar und Schutzmaßnahmen sind für kritische Prozesse verbunden.
2. Privacy- und Security-by-Design-Checks sind Teil von Produktentwicklung, Beschaffung, Cloud- und KI-Freigaben.
3. Sensible personenbezogene Daten erhalten stärkere Zugriffskontrolle, Protokollierung, Verschlüsselung, Pseudonymisierung oder Segmentierung, soweit fachlich entschieden.
4. Monitoring erkennt auffällige Zugriffe, Massenexporte oder Fehlkonfigurationen und führt zu Incident-Triage.
5. Lösch- und Aufbewahrungsanforderungen werden technisch nachvollziehbar getestet.
6. Management erhält entscheidungsfähige Informationen zu Restrisiken, überfälligen Maßnahmen, Dienstleisterthemen und Ressourcenbedarf.

## Ablauf als Routine

1. **Änderung oder neuer Datenkontext entsteht:** Prozess, System, Tool, Export, Dienstleister, Logquelle oder Incident.
2. **Personenbezug erkennen:** Datenarten, betroffene Gruppen, Zweck und Datenfluss grob erfassen.
3. **Owner und Schutzbedarf klären:** Fachbereich, Systemverantwortung, Sicherheitsrolle und Datenschutzrolle verbinden.
4. **Schutzmaßnahmen prüfen:** Zugriff, Verschlüsselung, Logging, Backup, Löschung, Dienstleister, Monitoring und Incident-Pfad.
5. **Handoffs auslösen:** Datenschutz/Legal bei Rechtsgrundlage, Betroffenenrechten, Aufbewahrung, Auswertung, Übermittlung oder hoher Sensibilität.
6. **Umsetzen und nachweisen:** Maßnahmen in Tickets, Konfigurationen, Freigaben oder Registereinträgen dokumentieren.
7. **Reviewen:** Zugriff, Datenfluss, Dienstleister, Löschung und Ereignisse regelmäßig oder triggerbasiert prüfen.
8. **Eskalieren:** ungeklärte Restrisiken, Ressourcenlücken oder Vorfälle ins zuständige Entscheidungsformat geben.

## Entscheidungen

- Welche Prozesse und Systeme mit personenbezogenen Informationen sind kritisch?
- Welche Datenarten benötigen zusätzliche Schutzmaßnahmen?
- Welche Rollen dürfen personenbezogene Daten einsehen, exportieren oder auswerten?
- Welche Protokollierung oder Überwachung ist nötig und datenschutzseitig geklärt?
- Welche Dienstleister, Cloud-Regionen oder Schnittstellen benötigen Review?
- Wie werden Löschung, Aufbewahrung, Backup und Archivierung zusammengebracht?
- Wann wird ein Sicherheitsereignis an Datenschutz, Legal, Management oder Kommunikation übergeben?

## Evidenz

### Starke Evidenz

- Prozess-/Systemübersicht mit Personenbezug, Owner und Schutzbedarf,
- referenzierte Datenschutz- und Security-Checks,
- Zugriffreview und Nachweis korrigierter Rechte,
- technische Schutz- und Konfigurationsnachweise,
- Dienstleister- und Vertragsreferenzen mit Sicherheitsbezug,
- Lösch-/Sperr- oder Aufbewahrungsnachweise,
- Incident-Handoff mit Datenschutzbewertung durch zuständige Rolle,
- Managemententscheidung bei akzeptiertem Restrisiko oder Ressourcenlücke.

### Schwache Evidenz

- allgemeine Datenschutzerklärung ohne System- oder Betriebsbezug,
- Assetliste ohne Datenarten oder Owner,
- TOM-Dokument ohne Nachweis der Umsetzung,
- Zugriffsliste ohne Reviewentscheidung,
- pauschale Aussage „DSB ist informiert“ ohne offenen Punkt oder Entscheidung,
- Schulungsnachweis ohne Bezug zu konkreten Rollen und Datenprozessen.

### Evidenzlücken

- unbekannte Datenflüsse oder Schattenexporte,
- keine Verbindung zwischen Verarbeitung, System und Schutzmaßnahme,
- externe Dienstleister ohne Security-/Datenschutz-Handoff,
- Logs mit Personenbezug ohne geklärten Zweck und Zugriff,
- Löschanforderungen nicht technisch umgesetzt oder getestet,
- Incident-Prozess ohne Datenschutz-Checkpunkt.

## Wirksamkeitsprüfung

Prüffragen:

- Sind die wichtigsten personenbezogenen Informationen im ISMS-Scope bekannt und einem Owner zugeordnet?
- Sind Zugriff, Export, Protokollierung und Dienstleister für kritische Daten regelmäßig reviewed?
- Werden Datenschutz-Handoffs bei Änderungen und Incidents tatsächlich ausgelöst?
- Gibt es Nachweise, dass Schutzmaßnahmen technisch umgesetzt und nicht nur beschrieben sind?
- Sind Lösch-, Sperr- und Aufbewahrungsanforderungen im Betrieb nachvollziehbar?
- Werden Findings in Maßnahmen, Risikoentscheidungen oder Managemententscheidungen übersetzt?

Mögliche Kennzahlen:

- Anteil kritischer Systeme mit Personenbezug und Owner,
- überfällige Security-/Datenschutz-Checks,
- offene Maßnahmen zu personenbezogenen Informationen,
- kritische Zugriffsabweichungen,
- Dienstleister mit offenem Nachweisstatus,
- Incidents mit dokumentiertem Datenschutz-Handoff.

## BSIG-/NIS2-Anschluss

Der Schutz personenbezogener Informationen ist anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Incident Handling, Zugriffsschutz, Lieferkettensicherheit, sichere Beschaffung, Cyberhygiene und Managementaufsicht. Der konkrete Bezug sollte organisationsspezifisch im Anforderungsregister, Datenschutzprozess und ISMS-Risikoregister geprüft werden.

Dieses Artefakt ersetzt keine Datenschutzberatung, keine Rechtsberatung und keine verbindliche Bewertung von Melde-, Informations- oder Dokumentationspflichten.

## Grenzen

- Keine Rechts- oder Datenschutzberatung und keine Aussage zur Rechtmäßigkeit einer Verarbeitung.
- Keine Bewertung von Betroffenenrechten, Rechtsgrundlagen, Meldepflichten oder internationalen Übermittlungen durch das Artefakt.
- Keine Zertifizierungs-, Konformitäts- oder Sicherheitszusage.
- Keine ISO-27002-Texte oder Normersatzformulierung.
- Keine echten personenbezogenen Daten, Kundeninformationen oder Geheimdaten in öffentlichen Beispielen.

## Handoffs

- **Datenschutz-Handoff:** neue oder geänderte Verarbeitung, Logs/Monitoring, Auswertungen, Löschung, Betroffenenrechte, Incident mit Personenbezug.
- **Legal-Handoff:** Vertrags-, Haftungs-, Melde-, Kommunikations- oder Übermittlungsfragen.
- **HR-Handoff:** Beschäftigtendaten, Rollenwechsel, Schulung, Monitoring mit Arbeitsbezug.
- **IT-/Plattform-Handoff:** technische Schutzmaßnahmen, Zugriff, Verschlüsselung, Backup, Löschung, Logging.
- **Einkaufs-/Vendor-Handoff:** Dienstleister, SaaS, Unterauftragnehmer, Nachweise und Sicherheitsanforderungen.
- **Incident-Handoff:** Verdacht auf Datenabfluss, Fehlberechtigung, Fehlversand, kompromittiertes Konto.
- **Management-Handoff:** Ressourcen, Restrisiken, Priorisierung, externe Kommunikation nach zuständiger Prüfung.
- **Audit-/Evidence-Handoff:** fehlende Nachweise, unklare Owner, nicht prüfbare Maßnahmen.

## Typische Fehler

- Datenschutz wird als separates Dokumententhema behandelt und nicht mit Systembetrieb verbunden.
- TOMs sind beschrieben, aber technische Umsetzung und Review fehlen.
- Logs und Reports enthalten personenbezogene Daten, ohne dass Zugriff und Zweck geklärt sind.
- Löschkonzepte ignorieren Backups, Archive oder SaaS-Exporte.
- Dienstleister werden vertraglich geführt, aber Sicherheitsnachweise nicht nachverfolgt.
- Sicherheitsereignisse werden technisch bearbeitet, ohne Datenschutz-Handoff.
- KI- oder Analysewerkzeuge werden mit personenbezogenen Daten getestet, bevor Freigabe und Datenklasse geklärt sind.

## Fiktives Mini-Beispiel

Ein fiktiver Fachbereich möchte ein neues SaaS-Tool für Supportanfragen einsetzen. Der Prozess Owner erfasst, dass Kundennamen, E-Mail-Adressen und Ticketinhalte verarbeitet werden. IT prüft MFA, Rollen, Exportfunktionen und Logging. Datenschutz bewertet die Verarbeitung und offene Vertragsfragen. Einkauf hält den Dienstleisterbezug nach. Vor Produktivstart wird eine Zugriffsmatrix freigegeben; ein offener Löschpunkt bleibt als Maßnahme mit Wiedervorlage im ISMS-Log.

Evidenz:

- Systemeintrag mit Personenbezug und Owner,
- Security-/Datenschutz-Check,
- Zugriffsmatrix,
- Dienstleisterreferenz,
- Maßnahmenticket zum Löschpunkt,
- Freigabeprotokoll vor Produktivstart.
