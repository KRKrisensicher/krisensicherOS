
# A.5.28 — Sichern von Beweisspuren

## Zweck

Sichern von Beweisspuren sorgt dafür, dass relevante Informationen nach einem Sicherheitsereignis nachvollziehbar, geschützt und verwertbar erhalten bleiben. Gemeint sind nicht nur „Logs kopieren“, sondern klare Entscheidungen: Welche Spuren sind relevant, wer darf sie sichern, wie bleiben Integrität und Vertraulichkeit erhalten, und wann müssen Legal, Datenschutz oder externe Spezialisten übernehmen?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der digitale und organisatorische Spuren bei Sicherheitsereignissen identifiziert, gesichert, dokumentiert, geschützt und kontrolliert weitergegeben werden. Die Routine unterstützt interne Aufklärung, Risikobewertung, Lessons Learned und — falls erforderlich — menschlich geprüfte rechtliche oder vertragliche Schritte.

## Typische Risiken

- Wenn Logs, Systeme oder Geräte vorschnell bereinigt werden, gehen wichtige Spuren verloren.
- Wenn Beweise unsystematisch gesammelt werden, sind Herkunft, Zeitpunkt, Vollständigkeit oder Veränderungsfreiheit nicht nachvollziehbar.
- Wenn zu viele Daten kopiert werden, entstehen unnötige Datenschutz-, Geheimhaltungs- oder Zugriffsrisiken.
- Wenn Zugriff auf Beweisspuren nicht begrenzt wird, können sensible Inhalte unkontrolliert verbreitet werden.
- Wenn Dienstleister oder Cloud-Anbieter nicht eingebunden werden, verfallen verfügbare Protokolle oder Exportfristen.
- Wenn rechtliche Bewertung behauptet statt eingeholt wird, entstehen Scheinsicherheit und Fehlentscheidungen.

## Trigger

- Sicherheitsvorfall oder begründeter Verdacht auf Kompromittierung, Datenabfluss, Manipulation oder Missbrauch.
- Incident Owner fordert Spurensicherung für Analyse, Wiederherstellung oder Entscheidungsfindung an.
- Hinweis auf mögliche rechtliche, vertragliche, versicherungsbezogene oder meldebezogene Relevanz.
- bevor ein betroffenes System neu installiert, bereinigt, abgeschaltet oder überschrieben wird.
- Anforderung durch Legal, Datenschutz, Management, Forensikdienstleister oder interne Prüfung.
- Übung oder Review zeigt Lücken bei Logaufbewahrung, Zugriff oder Beweissicherung.

## Rollen und Verantwortung

- **Incident Owner:** entscheidet im Incident-Prozess, welche Spurensicherung benötigt wird und koordiniert Prioritäten.
- **Forensik-/Security-Rolle:** definiert Sicherungsmethode, dokumentiert Kette der Übergaben und schützt Integrität.
- **IT-Betrieb / Plattformteam:** stellt Systeme, Logs, Snapshots, Backups oder Geräte kontrolliert bereit.
- **Asset Owner / Service Owner:** bewertet fachliche Kritikalität und Betriebsfolgen der Sicherung.
- **Datenschutz / Legal:** prüft personenbezogene Daten, Rechtsfragen, externe Weitergabe, Aufbewahrung und Kommunikation.
- **Lieferantenmanagement:** koordiniert Cloud-, SaaS-, Managed-Service- oder Dienstleisterspuren.
- **Management:** entscheidet bei Ressourcen, externer Beauftragung, Zielkonflikten oder risikoreicher Herausgabe.

## Implementierung

### Minimalstart

Ziel: Relevante Spuren bei kritischen Ereignissen nicht verlieren und nachvollziehbar behandeln.

1. Festlegen, wer im Incident-Fall Spurensicherung anordnen darf.
2. Eine kurze Checkliste erstellen: betroffene Systeme, Logs, Zeitfenster, Geräte, Accounts, Kommunikationsdaten, Dienstleister.
3. Vor Bereinigung oder Wiederherstellung prüfen, ob ein Snapshot, Logexport oder Gerätesicherung nötig ist.
4. Vor Massendatenexporten eine Datensparsamkeitsentscheidung treffen: Welche Daten sind für den Zweck erforderlich, welche können ausgeschlossen oder später nachgezogen werden?
5. Jede Sicherung dokumentieren: was, wann, durch wen, von welchem System, mit welcher Methode, wo abgelegt, wer hat Zugriff.
6. Beweisspuren in einem geschützten Ablagebereich mit begrenztem Zugriff speichern.
7. Legal-/Datenschutz-Handoff auslösen, wenn personenbezogene, vertragliche oder externe Verwertungsfragen berührt sind.
8. Für gesicherte Spuren einen Owner für Aufbewahrung, Zugriffreview und Löschentscheidung benennen.

Minimaler Nachweis:

- Spurensicherungs-Checkliste,
- Sicherungsprotokoll,
- geschützter Ablage- oder Ticketnachweis,
- Zugriffsliste,
- Handoff- oder Freigabenotiz.

### Solide Praxis

Ziel: Spurensicherung wird in Incident Response, Logging und Dienstleistersteuerung integriert.

1. Relevante Beweisquellen werden vorab inventarisiert: zentrale Logs, Endpunkte, Cloud-Dienste, IAM, Mail, Netzwerk, Backups, Tickets.
2. Aufbewahrungsfristen und Exportmöglichkeiten kritischer Logs sind bekannt.
3. Sicherungen werden mit Hashwert, Zeitbezug, Bearbeitungsschritten und Übergaben dokumentiert.
4. Jede Kopie, Analyseweitergabe, externe Weitergabe oder Rückgabe wird als Chain-of-Custody-Ereignis mit Zweck, Freigabe, Empfänger, Zeitpunkt und Ablagebezug protokolliert.
5. Zugriff auf gesicherte Spuren folgt Need-to-know und wird regelmäßig reviewed.
6. Aufbewahrung, Löschung und Wiedervorlage werden mit Owner, Frist und Entscheidungsgrund dokumentiert.
7. Dienstleisterverträge und Kontaktwege enthalten praktikable Unterstützung für Logexporte und Incident-Fälle.
8. Nach jedem relevanten Einsatz wird geprüft, ob Spuren fehlten oder zu spät gesichert wurden.

### Fortgeschritten

Ziel: Beweisspuren sind technisch verfügbar, kontrolliert verwertbar und krisenfest handhabbar.

1. Kritische Systeme liefern zentrale, manipulationserschwerende Logs mit abgestimmter Zeitbasis.
2. Incident-Playbooks enthalten fallbezogene Sicherungswege für Endpunkte, Cloud, SaaS, Identitäten und Netzwerk.
3. Automatisierte Workflows frieren relevante Daten kontrolliert ein, ohne unnötig große Datenmengen zu erzeugen.
4. Externe Forensik, Legal, Datenschutz und Kommunikation sind in Eskalationswegen vorbereitet.
5. Zugriff, Weitergabe, Löschung und Aufbewahrung von Beweisspuren werden in Reviews geprüft.
6. Übungen testen, ob Spuren unter Zeitdruck gesichert und nachvollziehbar übergeben werden können.

## Ablauf als Routine

1. **Verdacht entsteht:** Incident Triage erkennt mögliche Relevanz von Spuren.
2. **Scope festlegen:** betroffene Systeme, Accounts, Zeitfenster, Datenarten und Dienstleister bestimmen.
3. **Sicherungsbedarf entscheiden:** interne Analyse, Wiederherstellung, rechtliche Prüfung, Versicherung oder externe Forensik.
4. **Sicherung durchführen:** Logexport, Snapshot, Image, Backupkopie, Mail-/IAM-Auszug oder Konfigurationsstand sichern.
5. **Integrität und Herkunft dokumentieren:** Zeitpunkt, Quelle, Methode, verantwortliche Person, Speicherort, Hash oder vergleichbare Kontrollinformation.
6. **Chain-of-Custody führen:** Kopien, Analysen, Übergaben, externe Weitergaben, Rückgaben und Löschentscheidungen nachvollziehbar protokollieren.
7. **Zugriff begrenzen:** Ablage schützen, Zugriffe protokollieren, Weitergabe freigeben lassen und Zugriff regelmäßig reviewen.
8. **Handoff prüfen:** Legal, Datenschutz, Dienstleister, Management oder Forensik einbinden.
9. **Auswertung trennen:** Analyseergebnisse dokumentieren, Originalspuren möglichst unverändert halten.
10. **Nachbereiten:** fehlende Logs, zu kurze Aufbewahrung oder unklare Zuständigkeiten als Maßnahmen erfassen.

## Entscheidungen

- Welche Ereignisse benötigen formale Spurensicherung?
- Welche Systeme und Logs sind für typische Szenarien kritisch?
- Wie wird verhindert, dass Wiederherstellung wichtige Spuren überschreibt?
- Wer darf Beweisspuren einsehen, kopieren oder extern weitergeben?
- Wie lange werden gesicherte Spuren aufbewahrt, wer ist Owner und wer entscheidet Löschung?
- Welche Kopien, Übergaben oder externen Weitergaben sind zulässig und wie werden sie freigegeben?
- Wann ist externe Forensik oder rechtliche Bewertung erforderlich?
- Wie wird zwischen schneller Betriebswiederherstellung, Datensparsamkeit und Beweiserhalt priorisiert?

## Evidenz

### Starke Evidenz

- Incident-Ticket mit Sicherungsentscheidung,
- Sicherungsprotokoll mit Quelle, Zeitpunkt, Methode und Verantwortlichen,
- Integritätsnachweis oder Hashwert, soweit angemessen,
- geschützte Ablage mit Zugriffsbeschränkung,
- Chain-of-Custody-Protokoll zu Kopien, Analysen, Übergaben, Zugriffen und Weitergaben,
- Übergabeprotokoll an Legal, Datenschutz, Forensik oder Dienstleister,
- Aufbewahrungs-, Lösch- und Zugriffreview-Entscheidung,
- Reviewnotiz zu fehlenden Spuren und Verbesserungsmaßnahmen.

### Schwache Evidenz

- Screenshots ohne Zeit- und Quellenbezug,
- kopierte Logdateien ohne Herkunftsdokumentation,
- Chatnachricht „Logs gesichert“ ohne Ablage- oder Zugriffsnachweis,
- ungeschützte Ablage in allgemeinen Teamordnern,
- pauschale Aussage, der Dienstleister habe alles gespeichert.

### Evidenzlücken

- keine Kriterien für Spurensicherung,
- Logs werden überschrieben, bevor sie exportiert werden,
- kein Nachweis, wer Beweisspuren gesehen oder weitergegeben hat,
- keine Klärung personenbezogener Inhalte,
- keine vertraglich nutzbaren Logexporte bei Cloud-/SaaS-Diensten,
- Originaldaten werden während der Analyse verändert.

## Wirksamkeitsprüfung

Prüffragen:

- Kann bei einem relevanten Incident nachvollzogen werden, welche Spuren gesichert wurden und warum?
- Sind kritische Logquellen bekannt und rechtzeitig verfügbar?
- Bleiben Herkunft, Integrität, Zugriff, Kopien, Analysen und Weitergabe nachvollziehbar?
- Ist die Zeitbasis kritischer Logquellen synchronisiert oder zumindest als Zeitreferenz nachvollziehbar dokumentiert?
- Werden personenbezogene, vertrauliche oder vertragliche Fragen vor Massendatenexport, Analyse oder Weitergabe geprüft?
- Werden Aufbewahrung, Löschung und Zugriffreview gesicherter Spuren nachgehalten?
- Werden fehlende Spuren nach Incidents in Maßnahmen überführt?
- Ist der Ablauf unter Krisen- und Wiederherstellungsdruck realistisch nutzbar?

Mögliche Kennzahlen:

- Anteil relevanter Incidents mit Sicherungsprotokoll,
- Logquellen mit bekannter Aufbewahrungsdauer,
- Zeit bis Sicherung kritischer Spuren,
- Anzahl fehlender oder unvollständiger Logquellen,
- offene Maßnahmen aus Spurensicherungsreviews,
- nicht genehmigte Zugriffe auf Beweisspuren,
- überfällige Aufbewahrungs-/Löschreviews gesicherter Spuren.

## BSIG-/NIS2-Anschluss

Spurensicherung ist anschlussfähig an NIS2-orientierte Themen wie Incident Handling, Nachvollziehbarkeit, Krisenreaktion, Risikomanagement und Governance von Sicherheitsereignissen. Je nach Organisation kann sie auch Nachweis-, Vertrags-, Versicherungs- oder Meldeprozesse unterstützen.

Dieses Artefakt trifft keine rechtliche Aussage zur Verwertbarkeit von Beweisen, zu Meldepflichten oder zu Aufbewahrungspflichten. Diese Punkte benötigen Human Review durch qualifizierte Rollen.

## Grenzen

- Dieses Artefakt ist kein forensisches Fachhandbuch und keine rechtliche Beweiswürdigungsanleitung.
- Es ersetzt keine Datenschutz-, Legal-, arbeitsrechtliche oder strafprozessuale Bewertung.
- Es garantiert keine gerichtliche Verwertbarkeit.
- Es darf nicht zu übermäßiger Sammlung personenbezogener oder vertraulicher Daten führen.
- Öffentliche Beispiele enthalten keine echten Vorfallsdaten, Kundendaten oder geheimen technischen Details.

## Handoffs

- **Incident-Handoff:** Spurensicherung als Teil der Triage, Eindämmung und Wiederherstellung.
- **Legal-Handoff:** externe Verwertung, Strafanzeige, Vertragsstreit, Versicherung, behördliche Kommunikation oder Meldepflichtverdacht.
- **Datenschutz-Handoff:** personenbezogene Logs, Beschäftigtendaten, Kommunikationsinhalte oder mögliche Datenschutzverletzung.
- **Forensik-Handoff:** komplexe Kompromittierung, hohe Schadenswirkung, Manipulationsverdacht oder fehlende interne Fähigkeit.
- **Lieferanten-Handoff:** Cloud-/SaaS-Logs, Managed Services, Gerätehersteller oder externe Betriebsleistungen.
- **Management-Handoff:** Zielkonflikt zwischen Beweiserhalt, Wiederherstellung, Kosten, Reputation oder Betriebsdruck.
- **Evidence-Handoff:** Ablage, Zugriff, Aufbewahrung und Review der Nachweise.

## Typische Fehler

- Systeme werden neu installiert, bevor Logs oder Snapshots gesichert sind.
- Beweisspuren landen in ungeschützten Projektordnern.
- Nur technische Teams entscheiden über Weitergabe, ohne Legal-/Datenschutzprüfung.
- Screenshots ersetzen strukturierte Sicherung und Dokumentation.
- Dienstleister-Logs werden erst angefragt, wenn sie bereits verfallen sind.
- Originaldaten werden während der Analyse verändert.
- Kopien und Übergaben werden nicht als Chain-of-Custody-Ereignisse dokumentiert.
- Aufbewahrung und Löschung bleiben offen, weil kein Owner benannt ist.
- Die Organisation sammelt zu viel und schafft dadurch neue Datenschutz- und Geheimhaltungsrisiken.

## Fiktives Mini-Beispiel

Ein fiktiver Handelsbetrieb entdeckt ungewöhnliche Anmeldungen im Adminportal. Vor dem Zurücksetzen des Servers exportiert der Plattform Owner Authentifizierungslogs, erstellt einen Snapshot und dokumentiert Quelle, Zeitraum, Hashwert und Ablageort. Der Zugriff wird auf Incident Owner, Security-Rolle und Legal begrenzt. Ein SaaS-Dienstleister wird innerhalb der Logaufbewahrungsfrist um ergänzende Login-Daten gebeten. Im Review zeigt sich, dass ein weiterer Cloud-Dienst nur sieben Tage Logs vorhält; dies wird als Maßnahme im Lieferantenreview aufgenommen.

Evidenz:

- Sicherungsentscheidung im Incident-Ticket,
- Logexport- und Snapshot-Protokoll,
- Hash-/Ablagenachweis,
- Zugriffsliste,
- Dienstleisteranfrage,
- Maßnahme zur Logaufbewahrung im Lieferantenreview.
