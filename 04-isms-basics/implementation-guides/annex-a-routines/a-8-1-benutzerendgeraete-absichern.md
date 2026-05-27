
# A.8.1 — Benutzerendgeräte absichern

## Zweck

Benutzerendgeräte sind tägliche Arbeitswerkzeuge und zugleich häufige Einfallstore. Diese Routine sorgt dafür, dass Laptops, Desktops, Smartphones, Tablets und vergleichbare Arbeitsgeräte nicht nur beschafft und ausgegeben, sondern sicher konfiguriert, betrieben, überwacht, aktualisiert, zurückgenommen und bei Abweichungen entschieden werden.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Sicherheitsroutine für Benutzerendgeräte im Scope. Jedes relevante Gerät hat Owner, Verwaltungsstatus, Basiskonfiguration, Schutzmaßnahmen, Update- und Rückgabeprozess; Ausnahmen sind befristet, begründet und risikobewertet.

## Typische Risiken

- Wenn Endgeräte ungepatcht oder unverwaltet bleiben, können bekannte Schwachstellen ausgenutzt werden.
- Wenn lokale Daten unverschlüsselt gespeichert werden, führt Verlust oder Diebstahl schnell zu Informationsabfluss.
- Wenn private oder nicht freigegebene Geräte produktiv genutzt werden, fehlen Kontrolle, Support und Nachweis.
- Wenn Schutzfunktionen deaktiviert oder nicht überwacht werden, bleibt Scheinsicherheit durch Toolinstallation.
- Wenn lokale Adminrechte, unsichere Software oder Schatten-IT entstehen, steigt die Angriffsfläche.
- Wenn Rückgabe und Offboarding nicht greifen, bleiben Daten, Tokens und Zugänge auf Geräten erhalten.

## Trigger

- neues Gerät, Ersatzgerät, BYOD-/COPE-/Leihgerät oder Rollout.
- Eintritt, Rollenwechsel, Austritt oder längere Abwesenheit.
- neues Betriebssystem, neue Standardsoftware, neue Datenklasse oder neue Arbeitsform.
- Schwachstelle, Malwarefund, EDR-/MDM-Alarm oder Sicherheitsereignis.
- Verlust, Diebstahl, Defekt oder Rückgabe eines Geräts.
- regulärer Endpoint-Compliance-Review oder Auditfinding.

## Rollen und Verantwortung

- **IT-/Workplace Owner:** betreibt Geräteverwaltung, Baseline, Rollout, Updates und Support.
- **Asset Owner / Führungskraft:** bestätigt geschäftlichen Bedarf und besondere Anforderungen.
- **ISMS-Owner / Security-Rolle:** definiert Sicherheitsmindestlogik, Ausnahmen, Review und Eskalation.
- **Nutzerinnen und Nutzer:** melden Verlust, Auffälligkeiten und Abweichungen; umgehen Schutzmaßnahmen nicht.
- **HR / People-Funktion:** liefert Eintritts-, Wechsel- und Austrittsereignisse.
- **Datenschutz / Legal:** prüft personenbezogene Geräte- und Monitoringdaten, BYOD-Fragen und Beschäftigtenbezug.
- **Management:** entscheidet bei Ausnahmen, Ressourcenkonflikten oder nicht tragbaren Restrisiken.

## Implementierung

### Minimalstart

Ziel: kritische Endgeräte inventarisieren, verwalten und mit Basisschutz betreiben.

1. Geräte im Scope werden mit Asset-ID, Nutzer/Zuordnung, Owner und Verwaltungsstatus erfasst.
2. Ein Mindeststandard legt fest: Verschlüsselung, Bildschirmsperre, Updatefähigkeit, Malware-/Endpoint-Schutz, zentrale Verwaltung und Rückgabepfad.
3. Neue Geräte werden nur mit Standard-Build oder freigegebener Konfiguration ausgegeben.
4. Verlust, Diebstahl und Malwarefund haben einen Melde- und Sperrprozess.
5. Offboarding löst Rückgabe, Sperrung und Datenbehandlung aus.
6. Ausnahmen werden befristet dokumentiert.

Minimaler Nachweis:

- Geräteinventar mit Verwaltungsstatus,
- Standard-Build- oder Baseline-Nachweis,
- Update-/Schutzstatus für Stichprobe,
- Verlust-/Incident- und Rückgabeprozess,
- Ausnahmeentscheidungen.

### Solide Praxis

Ziel: Endpoint-Sicherheit wird wiederholbar, risikobasiert und reviewfähig.

1. Gerätegruppen werden nach Einsatz, Datenzugriff und Risikoprofil unterschieden.
2. MDM/Endpoint-Management erzwingt oder prüft zentrale Einstellungen und Sicherheitsstatus.
3. Patch- und Updateprozesse haben Fristen, Monitoring und Eskalation.
4. Lokale Adminrechte, nicht freigegebene Software und Geräte ohne Managementstatus werden regelmäßig geprüft.
5. Remote-Arbeit, externe Mitarbeitende und Sondergeräte erhalten eigene Regeln.
6. Verlust, Diebstahl, Malware oder Compliance-Abweichungen werden mit Incident Response verbunden.
7. Kennzahlen und offene Risiken fließen in ISMS- und Management Review.

Starke Evidenz:

- Endpoint-Inventar mit Management- und Compliance-Status,
- Baseline-/Konfigurationsnachweise,
- Patch- und Updateberichte,
- Tickets zu Abweichungen und Behebung,
- Nachweise zu Verlust/Remote-Wipe/Sperrung,
- Reviewprotokolle zu Ausnahmen und Adminrechten.

### Fortgeschritten

Ziel: Endgeräte werden als aktiver Teil von Detektion, Zero-Trust-Logik und Resilienz betrieben.

1. Gerätegesundheit beeinflusst Zugriff auf Anwendungen oder Daten.
2. EDR-/XDR-Signale, Schwachstellenstatus und Identitätsdaten werden in Triage und Incident Response eingebunden.
3. Rollen- und Risikoprofile steuern Härtung, Softwarekatalog und Updatefrequenz.
4. Automatisierung behebt Standardabweichungen oder isoliert kompromittierte Geräte.
5. Geräte-Lifecycle, Beschaffung, Rückgabe, Entsorgung und Wiederverwendung sind integriert.
6. Management erhält entscheidungsfähige Kennzahlen: unmanaged devices, kritische Patchlücken, Ausnahmen, lokale Adminrechte und Incidentmuster.

## Ablauf als Routine

1. **Gerätebedarf entsteht:** Neueinstellung, Ersatz, Projekt, Sonderrolle oder Defekt.
2. **Gerät vorbereiten:** Asset-ID, Standard-Build, Verschlüsselung, Schutzfunktionen, Managementprofil.
3. **Ausgabe dokumentieren:** Zuordnung, Nutzerinformation, Meldeweg und Rückgabepflicht.
4. **Betrieb überwachen:** Patchstatus, Schutzstatus, Abweichungen, lokale Adminrechte und nicht freigegebene Geräte.
5. **Abweichung behandeln:** Ticket, Behebung, Sperrung, Ausnahme oder Incident-Triage.
6. **Rollen- und Austrittsereignisse verarbeiten:** Rückgabe, Neuaufsetzung, Sperrung und Datenbehandlung.
7. **Review durchführen:** Stichproben und Kennzahlen prüfen, Muster verbessern, Risiken eskalieren.

## Entscheidungen

- Welche Gerätetypen und Nutzungsmodelle sind im Scope?
- Welche Mindestkonfiguration gilt für welche Rolle und Datenklasse?
- Wann ist BYOD oder Sonderhardware zulässig und wer akzeptiert das Risiko?
- Welche Abweichungen führen zu Sperrung, Remediation oder Managemententscheidung?
- Wie schnell müssen kritische Updates und Schutzstatusabweichungen behandelt werden?
- Welche Monitoringdaten dürfen wie ausgewertet werden?

## Evidenz

### Starke Evidenz

- aktuelles Geräteinventar mit Owner und Managementstatus,
- Baseline- und Rolloutnachweise,
- Patch-/Compliance-Berichte mit Behebungsstatus,
- Tickets für Abweichungen, Malware, Verlust oder Diebstahl,
- Nachweis zu Rückgabe, Wipe oder Sperrung,
- Ausnahmeentscheidungen mit Ablaufdatum,
- Managemententscheidung bei systematischen Lücken.

### Schwache Evidenz

- allgemeine Endgeräte-Policy ohne technische Nachweise,
- Tool-Screenshot ohne Scope und Datum,
- Inventarliste ohne Management- oder Patchstatus,
- Aussage „alle Geräte sind verschlüsselt“ ohne Stichprobe,
- Einzelticket ohne Verbindung zu Review oder Maßnahmenlog.

### Evidenzlücken

- unbekannte oder unverwaltete Geräte im Zugriff auf Unternehmensdaten,
- keine Verbindung zwischen HR-Ereignissen und Geräterückgabe,
- Schutzsoftware installiert, aber nicht überwacht,
- lokale Adminrechte ohne Review,
- BYOD oder externe Geräte ohne Freigabe und Datenbehandlung.

## Wirksamkeitsprüfung

Prüffragen:

- Sind alle relevanten Endgeräte inventarisiert und einem Owner zugeordnet?
- Ist erkennbar, welche Geräte verwaltet, gepatcht und verschlüsselt sind?
- Werden kritische Abweichungen innerhalb definierter Fristen behandelt?
- Funktionieren Verlust-, Diebstahl- und Offboarding-Routinen?
- Werden Sondergeräte, externe Mitarbeitende und BYOD bewusst gesteuert?
- Führen wiederkehrende Endpoint-Probleme zu strukturellen Verbesserungen?

Mögliche Kennzahlen:

- Anteil verwalteter Geräte im Scope,
- Geräte mit kritischem Patchrückstand,
- Geräte ohne Verschlüsselungs- oder Schutzstatus,
- lokale Adminrechte je Risikogruppe,
- überfällige Rückgaben,
- offene Endpoint-Ausnahmen.

## BSIG-/NIS2-Anschluss

Endgerätesicherheit ist anschlussfähig an NIS2-orientierte Themen wie Cyberhygiene, Zugriffsschutz, Schwachstellenmanagement, Incident-Prävention, sichere Fernarbeit und Schutz kritischer Dienste. Der konkrete Bezug sollte im Anforderungsregister, im Assetmanagement und im Risikomanagement geprüft werden.

Dieses Artefakt ersetzt keine rechtliche oder datenschutzrechtliche Bewertung von Monitoring, BYOD oder Beschäftigtendaten.

## Grenzen

- Dieses Artefakt ist keine technische Hardening-Baseline und keine Produktempfehlung.
- Es ersetzt keine Datenschutzprüfung für Geräte- oder Verhaltensdaten.
- Es trifft keine Zertifizierungs-, Konformitäts- oder Sicherheitsgarantie.
- Es enthält keine vertraulichen Konfigurationsdetails oder echten Gerätedaten.
- Ein installiertes Tool ersetzt keine betriebene Review- und Entscheidungsroutine.

## Handoffs

- **HR-Handoff:** Eintritt, Rollenwechsel, Austritt, Rückgabe und externe Mitarbeitende.
- **Incident-Handoff:** Malware, Verlust, Diebstahl, kompromittiertes Gerät oder EDR-Alarm.
- **Vulnerability-/Patch-Handoff:** kritische Endgeräte-Schwachstellen, Updatefristen, Remediation.
- **Datenschutz-/Legal-Handoff:** BYOD, Monitoring, Beschäftigtendaten, Remote-Wipe-Fragen.
- **Asset-/Entsorgungs-Handoff:** Rückgabe, Wiederverwendung, Löschung oder Entsorgung.
- **Management-Handoff:** unmanaged devices, hohe Ausnahmequote, fehlende Ressourcen oder Risikoakzeptanz.
- **Audit-/Evidence-Handoff:** unvollständiger Scope, fehlende technische Nachweise oder ungeklärte Ausnahmen.

## Typische Fehler

- Endgerätesicherheit wird mit Toolinstallation verwechselt.
- Inventar, MDM und tatsächliche Nutzung passen nicht zusammen.
- Sondergeräte und externe Geräte bleiben außerhalb des Prozesses.
- Lokale Adminrechte wachsen stillschweigend.
- Patchstatus wird berichtet, aber überfällige Geräte werden nicht nachverfolgt.
- Verlustmeldungen und Offboarding sind organisatorisch unklar.
- Datenschutzfragen zu Monitoring oder BYOD werden zu spät geklärt.

## Fiktives Mini-Beispiel

Ein fiktiver Dienstleister stellt neue Laptops für ein Projektteam bereit. Das Workplace-Team rollt einen Standard-Build mit Verschlüsselung, Endpoint-Schutz und MDM-Profil aus. Im monatlichen Review fallen zwei Geräte mit deaktiviertem Schutzstatus auf. Für eines wird ein Supportticket erstellt, das andere gehört einem externen Mitarbeitenden ohne korrektes Managementprofil. Der Zugriff auf Projektdaten wird bis zur Klärung eingeschränkt und der externe Onboarding-Prozess angepasst.

Evidenz:

- Geräteinventar mit MDM-Status,
- Baseline-/Rolloutnachweis,
- Compliance-Report,
- Supportticket,
- Zugriffsentscheidung für externes Gerät,
- Maßnahme im Onboarding-Prozess.
