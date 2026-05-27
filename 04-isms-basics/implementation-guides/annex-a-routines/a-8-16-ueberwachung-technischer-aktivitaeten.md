
# A.8.16 — Überwachung technischer Aktivitäten

## Zweck

Überwachung technischer Aktivitäten macht sicherheitsrelevantes Verhalten in Systemen, Netzen, Anwendungen, Cloud-Umgebungen und administrativen Abläufen rechtzeitig sichtbar. Der Fokus liegt nicht auf Dauerbeobachtung um ihrer selbst willen, sondern auf klaren Use Cases, zulässigen Auswertungen, Reaktion auf Auffälligkeiten und entscheidungsfähiger Steuerung.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der ausgewählte technische Aktivitäten überwacht, Auffälligkeiten bewertet, Reaktionen ausgelöst und blinde Flecken verbessert werden. Monitoring ist dabei mit Protokollierung, Incident Response, Zugriffsschutz, Datenschutz-/Legal-Prüfung und Managemententscheidungen verbunden.

## Typische Risiken

- Wenn technische Aktivitäten nicht überwacht werden, bleiben Angriffe, Fehlkonfigurationen oder Missbrauch bis zum Schaden unentdeckt.
- Wenn Monitoring ohne definierte Use Cases läuft, entstehen viele Meldungen ohne Reaktion und relevante Signale gehen unter.
- Wenn Alarmregeln nicht gepflegt werden, passen sie nicht zu neuen Systemen, Bedrohungen oder Geschäftsprozessen.
- Wenn niemand für Triage verantwortlich ist, werden Warnungen zwar erzeugt, aber nicht bewertet.
- Wenn Monitoring in Beschäftigten- oder Kundendaten eingreift, ohne dass Grenzen und Zwecke geprüft wurden, entstehen rechtliche und Vertrauensrisiken.
- Wenn externe Dienste außerhalb des Monitorings bleiben, entsteht ein falsches Lagebild.

## Trigger

- neues oder geändertes kritisches System, Netzwerksegment, Cloud-Konto, Identitätsdienst oder SaaS-Dienst.
- neuer Monitoring-Treffer, Incident, Beinahevorfall oder Lessons Learned.
- neue Schwachstelle, Bedrohungslage oder Angriffsindikator.
- Änderung von Rollen, privilegierten Konten, Schnittstellen oder Datenklassen.
- Einführung oder Anpassung von SIEM, EDR, NDR, Cloud Security Monitoring oder Betriebsmonitoring.
- regulärer Review von Use Cases, Alarmqualität, Reaktionszeiten und blinden Flecken.
- Auditfinding, Kundenanforderung oder Managementfrage zur Detektionsfähigkeit.

## Rollen und Verantwortung

- **Security Operations / Security-Rolle:** definiert Monitoring-Use-Cases, Triage-Kriterien, Eskalationswege und Qualitätsreview.
- **IT-/Plattform Owner:** stellt Telemetrie, Sensoren, Agenten, Logweiterleitung und technische Betriebsfähigkeit bereit.
- **Service Owner / Application Owner:** bewertet fachlichen Kontext, Kritikalität und zulässige Reaktionsmaßnahmen.
- **Incident-Response-Rolle:** übernimmt bestätigte Verdachtsfälle und führt Untersuchung oder Eindämmung.
- **Datenschutz-/Legal-Rolle:** prüft Zwecke, Grenzen und Auswertungen bei personenbezogenen oder beschäftigtenbezogenen Daten.
- **Lieferantenmanagement:** klärt Monitoring-Schnittstellen, Meldungen und Verantwortlichkeiten bei externen Diensten.
- **Management:** entscheidet bei fehlender Abdeckung, Ressourcenbedarf, akzeptierten Risiken oder Zielkonflikten.

## Implementierung

### Minimalstart

Ziel: Die wichtigsten technischen Aktivitäten kritischer Systeme werden mit klarer Reaktion überwacht.

1. Kritische Monitoring-Bereiche benennen: Identität, privilegierte Aktionen, Internet-exponierte Systeme, Malware-/EDR-Meldungen, Backup-Fehler, Cloud-Admin-Aktivitäten, Netzwerkzugänge.
2. Für jeden Bereich festlegen: Signalquelle, Owner, Alarmkriterium, Triage-Rolle und Eskalationsweg.
3. Eine kleine Anzahl relevanter Use Cases starten, statt viele ungeprüfte Alarme zu aktivieren.
4. Meldungen in einem Ticket-, Incident- oder Reviewlog nachverfolgen.
5. False Positives, nicht bearbeitete Alarme und fehlende Quellen im Review sichtbar machen.
6. Datenschutz-/Legal-Handoff festlegen, bevor personenbezogene Auswertungen regelmäßig genutzt werden.

### Solide Praxis

Ziel: Monitoring wird wiederholbar, risikobasiert und mit Incident Response verbunden.

1. Monitoring-Use-Cases werden nach Risiko, Assetkritikalität und erwarteter Reaktion priorisiert.
2. Alarmregeln haben Owner, Zweck, Datenquellen, Schwellwerte, Triage-Schritte und Eskalationskriterien.
3. Triage-Ergebnisse werden dokumentiert: bestätigt, harmlos, Fehlalarm, technische Störung, Verbesserungsbedarf.
4. Reaktionszeiten und Übernahme in Incident Response sind definiert.
5. Use Cases werden nach Incidents, Schwachstellen, Architekturänderungen und neuen Diensten aktualisiert.
6. Monitoring-Ausfälle, fehlende Agenten oder Datenquellen werden als Betriebsabweichungen behandelt.
7. Regelmäßige Reviews betrachten Alarmqualität, blinde Flecken, Workload und Entscheidungsbedarf.

### Fortgeschritten

Ziel: Überwachung liefert ein belastbares technisches Lagebild und unterstützt schnelle, angemessene Reaktion.

1. Log-, EDR-, Netzwerk-, Cloud-, Identitäts- und Anwendungssignale werden korreliert.
2. Use Cases werden mit Threat Intelligence, Angriffspfaden, Schwachstellenlage und kritischen Geschäftsservices verbunden.
3. Automatisierte Reaktionen sind risikobasiert begrenzt und haben menschliche Freigabe- oder Reviewpunkte, wo Auswirkungen erheblich sein können.
4. Detection Engineering pflegt Regeln, Tests, Tuning und Versionshistorie.
5. Übungen und Purple-Team-nahe Tests prüfen, ob relevante Aktivitäten erkannt und bearbeitet werden.
6. Kennzahlen zeigen nicht nur Alarmvolumen, sondern Abdeckung, Qualität, Reaktionsfähigkeit und offene Entscheidungen.
7. Lieferanten- und SaaS-Signale fließen in das Lagebild ein, soweit vertraglich und technisch möglich.

## Ablauf als Routine

1. **Use Case auswählen:** Risiko, Asset und erwartete Reaktion bestimmen.
2. **Datenquelle prüfen:** Log, Agent, Sensor oder Lieferantenmeldung auf Verfügbarkeit und Qualität prüfen.
3. **Regel einrichten:** Alarmkriterium, Schwellwert, Kontext und Owner festlegen.
4. **Triage definieren:** erste Prüfung, Priorität, Eskalationsweg und Dokumentation beschreiben.
5. **Betrieb beobachten:** Treffer, Fehlalarme, Ausfälle und nicht bearbeitete Meldungen nachverfolgen.
6. **Eskalieren:** bestätigte Verdachtsfälle an Incident Response oder Service Owner geben.
7. **Review durchführen:** Alarmqualität, blinde Flecken, neue Risiken und Workload bewerten.
8. **Verbessern:** Regel tunen, Datenquelle ergänzen, Playbook ändern oder Managemententscheidung vorbereiten.

## Entscheidungen

- Welche technischen Aktivitäten müssen überwacht werden, weil sie hohe Sicherheits- oder Betriebswirkung haben?
- Welche Alarme lösen sofortige Triage aus und welche nur Review oder Trendanalyse?
- Wer darf bei bestätigten Auffälligkeiten Systeme sperren, Konten deaktivieren oder Daten sichern?
- Wie werden False Positives, Alarmmüdigkeit und knappe Security-Kapazitäten gesteuert?
- Welche Monitoring-Lücken werden akzeptiert, kompensiert oder priorisiert geschlossen?
- Welche Auswertungen benötigen Datenschutz-/Legal-Prüfung oder Beteiligung weiterer Gremien?
- Welche externen Dienste müssen Meldungen liefern und wie wird deren Qualität bewertet?

## Evidenz

### Starke Evidenz

- priorisierte Liste von Monitoring-Use-Cases mit Owner, Datenquelle und Reaktion,
- Alarmregel- oder Detection-Dokumentation mit Änderungsverlauf,
- Tickets oder Incident-Nachweise aus Monitoring-Treffern,
- Reviewprotokolle zu False Positives, blinden Flecken und Regelanpassungen,
- Nachweise zu Monitoring-Abdeckung kritischer Systeme,
- Übungs- oder Testnachweise zur Erkennungsfähigkeit,
- Managemententscheidungen zu Ressourcen, akzeptierten Lücken oder Tooling.

### Schwache Evidenz

- Dashboard-Screenshot ohne Use-Case- und Reaktionsbezug,
- große Alarmstatistik ohne Triage-Qualität,
- Tool ist gekauft, aber keine Quellen oder Owner sind benannt,
- generische Alarmregeln ohne Anpassung an kritische Services,
- Meldungen werden per E-Mail verteilt, aber nicht nachverfolgt,
- Lieferant verspricht Monitoring, ohne Nachweis oder Reporting.

### Evidenzlücken

- keine definierten Monitoring-Use-Cases,
- unklare Triage-Verantwortung,
- keine Prüfung von Alarmqualität und Fehlalarmen,
- unbekannte Abdeckung kritischer Systeme,
- keine Behandlung von Monitoring-Ausfällen,
- keine Datenschutz-/Legal-Prüfung bei sensiblen Auswertungen,
- bestätigte Auffälligkeiten ohne Incident- oder Maßnahmenhandoff.

## Wirksamkeitsprüfung

Prüffragen:

- Gibt es für die wichtigsten technischen Risiken konkrete Monitoring-Use-Cases?
- Werden Alarme tatsächlich triagiert und dokumentiert?
- Können kritische Systeme, privilegierte Aktionen und Identitätsereignisse überwacht werden?
- Wird Alarmqualität regelmäßig verbessert?
- Sind Monitoring-Ausfälle und fehlende Datenquellen sichtbar?
- Führen bestätigte Auffälligkeiten zu Incident Response, Maßnahmen oder Managemententscheidungen?
- Sind Auswertungszwecke und Grenzen für sensible Daten geklärt?

Mögliche Kennzahlen:

- Abdeckung kritischer Monitoring-Use-Cases,
- Anteil bearbeiteter Alarme innerhalb definierter Frist,
- bestätigte Sicherheitsereignisse aus Monitoring,
- False-Positive-Rate je Use Case,
- offene Monitoring-Lücken nach Kritikalität,
- Zeit von Signal bis Triage,
- Regelalter ohne Review.

## BSIG-/NIS2-Anschluss

Überwachung technischer Aktivitäten ist anschlussfähig an NIS2-orientierte Themen wie Detektion, Incident Handling, Cyberhygiene, Zugriffsschutz, Risikomanagement und Betriebsfähigkeit. Der konkrete Bezug sollte organisationsspezifisch im Anforderungsregister, im Incident-Response-Konzept und in der Risikoanalyse geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung von Überwachungsmaßnahmen, Beschäftigtendaten, Meldepflichten oder Nachweispflichten.

## Grenzen

- Dieses Artefakt ist kein SOC-Betriebshandbuch und keine technische SIEM-Regelbibliothek.
- Monitoring ersetzt keine Prävention, kein Schwachstellenmanagement und keine klare Incident-Verantwortung.
- Automatisierte Reaktionen brauchen klare Grenzen, Tests und menschliche Reviewpunkte.
- Keine Rechtsberatung, keine Datenschutzberatung, keine Zertifizierungszusage.
- Keine Nutzung echter Log-, Kunden-, Personen- oder Geheimdaten in öffentlichen Beispielen.

## Handoffs

- **Incident-Handoff:** bestätigter Verdacht, aktive Ausnutzung, Malware, Kontenmissbrauch oder erhebliche Anomalie.
- **Datenschutz-/Legal-Handoff:** personenbezogene Auswertung, Beschäftigtenbezug, Zweckänderung, Monitoring-Grenzen oder Herausgabe.
- **Plattform-/Service-Handoff:** fehlende Datenquelle, defekter Agent, falsch konfigurierte Regel oder betroffener Servicekontext.
- **Lieferanten-Handoff:** externe Dienste liefern keine ausreichenden Signale, Reports oder Eskalationswege.
- **Management-Handoff:** kritische Monitoring-Lücken, Ressourcenengpass, Toolentscheidung oder akzeptiertes Restrisiko.
- **Audit-/Evidence-Handoff:** Use Cases, Triage oder Reviews sind nicht nachvollziehbar.

## Typische Fehler

- Monitoring wird mit Toolkauf verwechselt.
- Es gibt viele Alarme, aber keine Triage-Verantwortung.
- Regeln werden nie an neue Systeme oder Bedrohungen angepasst.
- False Positives werden hingenommen, bis Teams Alarme ignorieren.
- Sensible Auswertungen starten ohne geklärten Zweck und Human Review.
- Lieferantenmeldungen bleiben außerhalb des Lagebilds.
- Management erhält Alarmmengen, aber keine Aussage zu Risiko, Abdeckung und Entscheidungsbedarf.

## Fiktives Mini-Beispiel

Ein fiktiver Dienstleister führt Cloud-Admin-Konten für seine Produktplattform ein. Der Trigger ist die neue privilegierte Rolle. Security und Plattformteam definieren einen Monitoring-Use-Case: Anmeldung ohne MFA, Rollenänderung und Zugriff aus ungewöhnlicher Region erzeugen ein Ticket zur Triage. Nach zwei Wochen zeigt der Review mehrere Fehlalarme wegen Dienstreise-IPs. Die Regel wird angepasst, Datenschutz prüft den Auswertungszweck, und eine offene Lücke bei einem SaaS-Admin-Log geht ins Lieferantenmanagement.
