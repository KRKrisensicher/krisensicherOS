
# A.5.26 — Reaktion auf Sicherheitsvorfälle

## Zweck

Reaktion auf Sicherheitsvorfälle sorgt dafür, dass ein bestätigter oder plausibler Sicherheitsvorfall koordiniert behandelt wird: eindämmen, untersuchen, entscheiden, kommunizieren, wiederherstellen und lernen. Ziel ist nicht Heldentum im Ausnahmezustand, sondern eine belastbare Routine, die Verantwortung, Evidenz und Human Gates unter Druck aufrechterhält.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Vorfallreaktionsroutine, mit der Sicherheitsvorfälle priorisiert, koordiniert, technisch und organisatorisch behandelt, dokumentiert, eskaliert und nachbereitet werden. Entscheidungen zu Eindämmung, Wiederanlauf, Kommunikation, Restrisiko und externen Stellen bleiben nachvollziehbar und menschlich verantwortet.

## Typische Risiken

- Wenn technische Teams ohne gemeinsame Leitung reagieren, entstehen widersprüchliche Maßnahmen und Beweise gehen verloren.
- Wenn zu spät eingedämmt wird, kann sich ein Angriff ausbreiten oder Daten weiter gefährden.
- Wenn zu schnell abgeschaltet wird, können kritische Dienste ohne Managemententscheidung ausfallen.
- Wenn Kommunikation nicht gesteuert wird, entstehen falsche, verfrühte oder rechtlich riskante Aussagen.
- Wenn Lessons Learned fehlen, wiederholen sich Ursachen und Reaktionslücken.

## Trigger

- Sicherheitsereignis wurde als Vorfall klassifiziert oder muss vorsorglich wie ein Vorfall behandelt werden.
- bestätigte oder vermutete Kompromittierung von Konto, System, Daten, Anwendung oder Dienstleister.
- Malware, Ransomware, Datenabflussverdacht, Cloud-Fehlkonfiguration, aktive Ausnutzung oder erheblicher Policy-Verstoß.
- Lieferantenincident mit Auswirkung auf eigene Dienste oder Daten.
- Vorfallübung, Tabletop oder Lessons-Learned-Review.
- Management-, Legal-, Datenschutz-, Kunden- oder Behördenfrage zu einem Vorfall.

## Rollen und Verantwortung

- **Incident Lead:** koordiniert Vorfallreaktion, Lagebild, Aufgaben, Entscheidungen und Eskalationen.
- **Technische Response-Rollen:** analysieren, isolieren, sichern Logs, setzen Eindämmung und Wiederherstellung um.
- **Service Owner / Fachbereich:** bewertet Geschäftsfolgen, Prioritäten und Wiederanlaufbedarf.
- **ISMS-Owner / Security-Rolle:** stellt Prozess, Evidenz, Risiko- und Lessons-Learned-Verbindung sicher.
- **Legal / Datenschutz:** prüft rechtliche, datenschutzrechtliche, vertragliche und Meldepflichtfragen.
- **Kommunikation / Management:** entscheidet und steuert freigegebene interne oder externe Kommunikation.
- **BCM-/Krisenrolle:** übernimmt oder unterstützt, wenn der Vorfall kritische Dienste, Krisenstab oder Notbetrieb betrifft.
- **Lieferantenmanagement:** koordiniert externe Anbieter, Managed Services, Forensik oder SaaS-Abhängigkeiten.

## Implementierung

### Minimalstart

Ziel: ein Vorfall wird geführt, dokumentiert und kontrolliert eskaliert.

1. Für jeden Vorfall wird ein Incident Lead benannt.
2. Ein Vorfallticket oder Lageprotokoll hält Zeitlinie, Fakten, Entscheidungen, Maßnahmen, Owner und Status fest.
3. Sofortmaßnahmen werden nach Risiko und Betriebswirkung entschieden: isolieren, sperren, sichern, beobachten, wiederherstellen.
4. Legal, Datenschutz, Management und Kommunikation werden bei definierten Kriterien eingebunden.
5. Nach Abschluss gibt es ein kurzes Lessons-Learned-Protokoll mit Maßnahmen.
6. Offene Punkte werden in Maßnahmen-, Risiko- oder Verbesserungslog überführt.

Minimaler Nachweis:

- Vorfallticket oder Lageprotokoll,
- benannter Incident Lead,
- Zeitlinie und Entscheidungslog,
- Maßnahmen mit Owner und Status,
- Handoff-Nachweise,
- Abschluss- und Lessons-Learned-Notiz.

### Solide Praxis

Ziel: Vorfallreaktion ist rollenbasiert, szenariobezogen und entscheidungsfähig.

1. Vorfallkategorien und Schweregrade steuern Eskalation, Kommunikationsbedarf und Managementeinbindung.
2. Response-Playbooks beschreiben typische Maßnahmen für Kontokompromittierung, Malware, Datenabflussverdacht, Cloud-Vorfall, Lieferantenincident und Ausfall kritischer Dienste.
3. Beweissicherung, Logexporte und technische Änderungen werden kontrolliert dokumentiert.
4. Kommunikation erfolgt nur über freigegebene Rollen und mit Human Review.
5. Wiederherstellung wird mit Service Ownern, Change, BCM und Risikoentscheidung abgestimmt.
6. Lessons Learned führen zu konkreten Verbesserungen in Detektion, Zugriff, Schwachstellenbehandlung, Schulung, Lieferantensteuerung oder BCM.

Starke Evidenz:

- Incident-Klassifikation und Schweregrad,
- Lage- und Entscheidungsprotokoll,
- technische Analyse- und Maßnahmenreferenzen,
- Freigaben für Kommunikation oder kritische Maßnahmen,
- Wiederherstellungs- und Validierungsnachweise,
- Lessons-Learned-Maßnahmen mit Owner und Frist,
- Managemententscheidung bei hohem Restrisiko.

### Fortgeschritten

Ziel: Vorfallreaktion ist in Security Operations, Krisenmanagement und Management Reporting integriert.

1. Incident-Ticketing, Monitoring, Assetdaten, Kommunikationskanäle und Maßnahmenmanagement sind verbunden.
2. Lagebild, technische Fakten, Geschäftsfolgen und Entscheidungsbedarf werden regelmäßig synchronisiert.
3. Forensik-, Rechts-, Kommunikations- und Dienstleisterunterstützung sind vorbereitet und vertraglich bzw. organisatorisch abrufbar.
4. Vorfälle werden nach Abschluss mit Ursachenanalyse, Kontrollverbesserung und Wirksamkeitsprüfung nachverfolgt.
5. Kennzahlen zeigen Reaktionsfähigkeit: Zeit bis Eindämmung, Zeit bis Wiederherstellung, offene Lessons Learned, wiederkehrende Ursachen, Eskalationsqualität.

## Ablauf als Routine

1. **Vorfall übernehmen:** Triage übergibt an Incident Lead mit Fakten, Schweregrad und offenen Fragen.
2. **Lagebild aufbauen:** betroffene Assets, Daten, Nutzer, Geschäftsprozesse, Lieferanten und erste Auswirkung erfassen.
3. **Sofortmaßnahmen entscheiden:** Konten sperren, Systeme isolieren, Logs sichern, Zugriff begrenzen, Monitoring erhöhen oder Betrieb stabilisieren.
4. **Handoffs auslösen:** Legal, Datenschutz, Management, Kommunikation, BCM, Lieferanten oder Forensik einbinden.
5. **Untersuchen und eindämmen:** Ursache, Umfang, Ausbreitung und aktive Bedrohung klären; Maßnahmen kontrolliert umsetzen.
6. **Wiederherstellen:** Dienste geordnet zurückführen, Validierung durchführen, Restrisiken entscheiden.
7. **Kommunizieren:** nur freigegebene, abgestimmte Informationen intern oder extern weitergeben.
8. **Abschließen:** Status, Entscheidungen, Evidenz, Restpunkte und Lessons Learned dokumentieren.
9. **Verbessern:** Maßnahmen in ISMS, Technik, Schulung, Lieferantensteuerung oder BCM nachverfolgen.

## Entscheidungen

- Welche Sofortmaßnahmen sind verhältnismäßig und wer darf sie freigeben?
- Wann wird isoliert, abgeschaltet, weiterbetrieben oder wiederhergestellt?
- Welche Informationen sind belastbar genug für Management oder externe Kommunikation?
- Wann braucht es externe Forensik, Anbietereskalation oder Krisenstab?
- Welche Restrisiken bleiben nach Eindämmung oder Wiederanlauf offen?
- Wann ist ein Vorfall abgeschlossen und wer bestätigt das?

## Evidenz

### Starke Evidenz

- Incident-Ticket mit Zeitlinie, Rollen und Status,
- dokumentierte Schweregrad- und Eskalationsentscheidung,
- Entscheidungslog für Eindämmung, Wiederherstellung und Kommunikation,
- technische Nachweise zu Sperrung, Isolation, Analyse, Patch, Restore oder Validierung,
- Legal-/Datenschutz-/Management-Handoff-Nachweise,
- Abschlussbericht oder Lessons-Learned-Notiz,
- Maßnahmenverfolgung nach Vorfall.

### Schwache Evidenz

- Chatprotokoll ohne konsolidierte Entscheidungen,
- technische Screenshots ohne Zeitlinie oder Owner,
- Abschlussmeldung ohne Ursachen- oder Maßnahmenbezug,
- Kommunikationsentwurf ohne Freigabenachweis,
- Lessons Learned ohne Verantwortliche oder Fristen.

### Evidenzlücken

- kein Incident Lead,
- keine Zeitlinie,
- keine dokumentierten Sofortentscheidungen,
- technische Änderungen ohne Nachvollziehbarkeit,
- Legal-/Datenschutz-Handoff fehlt trotz Datenbezug,
- Wiederherstellung ohne Validierung,
- keine Nachbereitung oder Maßnahmenverfolgung.

## Wirksamkeitsprüfung

Prüffragen:

- Wurde der Vorfall klar geführt und waren Rollen erreichbar?
- Sind Zeitlinie, Fakten, Entscheidungen und Maßnahmen nachvollziehbar?
- Wurden Eindämmung und Wiederherstellung risikobasiert entschieden?
- Wurden Legal, Datenschutz, Management, Kommunikation und BCM rechtzeitig eingebunden?
- Wurden technische Maßnahmen validiert?
- Haben Lessons Learned zu konkreten Verbesserungen geführt?
- Sind offene Restrisiken ins Risikoregister oder Management Review überführt?

Mögliche Kennzahlen:

- Zeit bis Incident Lead benannt,
- Zeit bis Eindämmungsentscheidung,
- Zeit bis Wiederherstellung kritischer Dienste,
- Anzahl offener Lessons-Learned-Maßnahmen,
- wiederkehrende Vorfallursachen,
- Vorfälle mit vollständigem Entscheidungslog,
- überfällige Nachbereitungsmaßnahmen.

## BSIG-/NIS2-Anschluss

Die Reaktion auf Sicherheitsvorfälle ist anschlussfähig an NIS2-orientierte Themen wie Incident Handling, Melde- und Eskalationsfähigkeit, Business Continuity, Risikomanagement, Lieferantensteuerung und Managementverantwortung. Ob ein konkreter Vorfall meldepflichtig ist oder welche externen Schritte erforderlich sind, muss organisationsspezifisch und rechtlich geprüft werden.

Dieses Artefakt ersetzt keine Rechtsberatung, Datenschutzberatung oder verbindliche Meldepflichtbewertung.

## Grenzen

- Kein Ersatz für professionelle Forensik, Rechtsberatung, Datenschutzbewertung oder Krisenkommunikation.
- Keine Garantie, dass Eindämmung oder Wiederherstellung erfolgreich ist.
- Keine Aussage zur rechtlichen Einordnung konkreter Vorfälle.
- Keine ISO-27002-Texte oder Zertifizierungszusage.
- Keine echten Vorfallsdaten, Logdaten, personenbezogenen Daten oder vertraulichen Kundendaten in öffentlichen Beispielen.

## Handoffs

- **Triage-Handoff:** Sicherheitsereignis wird als Vorfall oder vorsorglich als Vorfall übernommen.
- **Legal-/Datenschutz-Handoff:** Datenabflussverdacht, Personenbezug, Meldepflichtnähe, Beweissicherung, externe Kommunikation.
- **Kommunikations-Handoff:** interne Lageupdates, Kunden-/Partnerkommunikation, Öffentlichkeitsarbeit nur mit Freigabe.
- **BCM-/Krisen-Handoff:** kritische Dienstunterbrechung, Notbetrieb, Krisenstab, Wiederanlaufpriorisierung.
- **Change-/Betriebs-Handoff:** Isolation, Patch, Restore, Konfigurationsänderung, Rollback, Validierung.
- **Lieferanten-Handoff:** Anbieterincident, externe Forensik, Managed Service, Cloud- oder SaaS-Abhängigkeit.
- **Management-Handoff:** erhebliche Auswirkung, Restrisiko, Abschaltung, Wiederanlauf, Ressourcen oder externe Kommunikation.
- **Audit-/Evidence-Handoff:** fehlende Zeitlinie, unklare Entscheidungen, unvollständige Nachbereitung.

## Typische Fehler

- Technische Maßnahmen starten ohne gemeinsame Lageführung.
- Kommunikation erfolgt, bevor Fakten und Freigaben geklärt sind.
- Logs oder Beweisspuren werden durch hektische Änderungen überschrieben.
- Fachbereiche werden zu spät eingebunden und Wiederanlaufprioritäten fehlen.
- Vorfälle werden geschlossen, obwohl Restrisiken oder Ursachen offen sind.
- Lessons Learned bleiben als Bericht liegen und werden nicht umgesetzt.
- Management erhält technische Details, aber keine Entscheidungsvorlagen.

## Fiktives Mini-Beispiel

Ein fiktiver Dienstleister meldet verdächtige Aktivitäten in einem angebundenen Supportsystem. Die Organisation übernimmt den Fall als Sicherheitsvorfall. Der Incident Lead erstellt ein Lageprotokoll, der IT-Owner sperrt betroffene Integrationskonten, der Service Owner bewertet Geschäftsfolgen, Legal und Datenschutz prüfen mögliche Datenbetroffenheit. Nach technischer Validierung wird der Dienst eingeschränkt wieder freigegeben. Im Lessons-Learned-Termin wird beschlossen, Integrationskonten künftig monatlich zu reviewen.

Evidenz:

- Lieferantenmeldung,
- Incident-Lageprotokoll,
- Sperr- und Validierungsnachweise,
- Legal-/Datenschutz-Handoff,
- Wiederanlaufentscheidung,
- Lessons-Learned-Maßnahme mit Owner und Frist.
