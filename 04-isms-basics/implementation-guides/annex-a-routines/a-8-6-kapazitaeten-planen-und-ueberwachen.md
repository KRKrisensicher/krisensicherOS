
# A.8.6 — Kapazitäten planen und überwachen

## Zweck

Kapazitätsplanung und -überwachung sorgen dafür, dass wichtige Dienste nicht durch vorhersehbare Engpässe, Wachstum, Fehlkonfigurationen oder unerkannte Auslastung ausfallen. Der Kern ist nicht ein einzelnes Monitoring-Dashboard, sondern eine Routine, die technische Messwerte mit Servicekritikalität, Businessplanung, Change Management und Managemententscheidungen verbindet.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Routine für Kapazitäten kritischer Systeme, Plattformen, Netze, Speicher, Anwendungen, Lizenzen, Cloud-Ressourcen und Betriebsressourcen. Sie erkennt Trends, definiert Schwellen, plant Erweiterungen und eskaliert Zielkonflikte, bevor Verfügbarkeit, Sicherheit oder Servicequalität kippen.

## Typische Risiken

- Wenn Kapazitätsgrenzen unbemerkt erreicht werden, können Dienste ausfallen oder Sicherheitsfunktionen nicht mehr arbeiten.
- Wenn Wachstum, Kampagnen oder neue Kunden nicht in die Planung einfließen, werden Engpässe erst im Betrieb sichtbar.
- Wenn Log-, Backup- oder Monitoring-Speicher vollläuft, gehen Sicherheits- und Wiederherstellungsnachweise verloren.
- Wenn Cloud-Ressourcen unkontrolliert wachsen, entstehen Kostenrisiken oder Abschaltungen durch Limits.
- Wenn Lizenz-, Personal- oder Supportkapazitäten vergessen werden, können technische Maßnahmen nicht betrieben werden.
- Wenn Alerts ohne Owner laufen, werden Schwellenwerte ignoriert oder zu spät behandelt.

## Trigger

- neuer oder geänderter Service, neue Plattform, neues Datenvolumen oder neue Nutzergruppe.
- Businessereignis wie Kampagne, Migration, Standorterweiterung, Produktlaunch oder Kundenwachstum.
- Monitoring-Alert, Trendüberschreitung, wiederholte Performanceprobleme oder Incident.
- Änderung von Backup-, Logging-, Security-Monitoring- oder Aufbewahrungsanforderungen.
- Cloud-Limit, Lizenzgrenze, Vertragsänderung oder Lieferantenhinweis.
- Architektur-, Change- oder Releaseentscheidung mit Kapazitätswirkung.
- turnusmäßiger Review kritischer Dienste und Kapazitätskennzahlen.

## Rollen und Verantwortung

- **Service Owner / Application Owner:** bewertet Kritikalität, Nutzerbedarf, Serviceziele und Businessplanung.
- **IT-/Plattform Owner:** misst technische Kapazitäten, setzt Schwellen und plant Erweiterungen.
- **Cloud-/Infrastruktur Owner:** steuert Ressourcenlimits, Skalierung, Kosten und technische Reserven.
- **Security-Rolle / ISMS-Owner:** achtet auf Kapazitäten für Logging, Monitoring, Backup, Schutzsysteme und Incident Response.
- **BCM-/Notfallverantwortliche:** bewertet Auswirkungen auf kritische Prozesse und Wiederanlaufziele.
- **Finance / Einkauf:** klärt Budget, Lizenzen, Verträge und Beschaffungszeiten.
- **Management:** entscheidet bei Ressourcenbedarf, Akzeptanz von Engpässen, Priorisierung und Verfügbarkeitszielen.

## Implementierung

### Minimalstart

Ziel: kritische Kapazitätsrisiken sichtbar machen und nicht erst im Incident entdecken.

1. Die wichtigsten Dienste, Plattformen, Speicherorte, Netzverbindungen, Log-/Backup-Systeme und Cloud-Limits werden benannt.
2. Für jedes kritische Ziel gibt es einen Owner und eine einfache Messgröße.
3. Schwellenwerte werden definiert: Warnung, kritischer Bereich, Eskalation.
4. Regelmäßige Sichtung der Messwerte wird festgelegt, mindestens für produktive kritische Dienste.
5. Absehbare Erweiterungen, Kosten oder Beschaffungen werden im Maßnahmenlog nachgehalten.
6. Engpässe mit Risiko für Verfügbarkeit oder Sicherheit werden ins Management Review gegeben.

Minimaler Nachweis:

- Liste kritischer Kapazitätsobjekte mit Owner,
- Monitoring- oder Messwertauszug,
- definierte Schwellenwerte,
- Maßnahmen- oder Kapazitätslog,
- Entscheidung zu Erweiterung, Workaround oder akzeptiertem Restrisiko.

### Solide Praxis

Ziel: Kapazitätssteuerung wird planbar, trendbasiert und mit Change Management verbunden.

1. Kapazität wird je Dienst entlang relevanter Dimensionen betrachtet: CPU, Speicher, Netzwerk, Storage, Datenbank, Queue, Lizenzen, Cloud-Limits, Log-/Backup-Volumen.
2. Trends werden regelmäßig bewertet und mit Businessplanung, Roadmap und Changes abgeglichen.
3. Kapazitätswirkung wird Teil von Architektur-, Release- und Change-Reviews.
4. Alerts haben Owner, Reaktionsweg und Eskalationsschwelle.
5. Sicherheitsrelevante Kapazitäten wie Logging, EDR, SIEM, Backup und Updateverteilung werden gesondert betrachtet.
6. Maßnahmen unterscheiden kurzfristige Entlastung, dauerhafte Erweiterung, Architekturänderung und akzeptierte Begrenzung.
7. Management bekommt entscheidungsfähige Informationen zu Kosten, Verfügbarkeit und Restrisiko.

### Fortgeschritten

Ziel: Kapazität wird vorausschauend und serviceorientiert gesteuert.

1. Automatisierte Dashboards, Forecasts oder SLO-/SLA-Bezüge verbinden technische Trends mit Servicekritikalität.
2. Cloud- und Plattformlimits werden über IaC, Policies oder Budgetalarme kontrolliert.
3. Lasttests, Resilienztests und Wachstumsannahmen fließen in Roadmaps und BCM-Planung ein.
4. Kapazitätsdaten unterstützen Incident Triage, Problem Management und technische Schuldensteuerung.
5. Kritische Ressourcen werden auf Single Points of Capacity geprüft: Fachpersonal, Wartungsfenster, Lizenzen, Lieferzeiten.
6. Managemententscheidungen basieren auf Szenarien: investieren, begrenzen, verschieben, akzeptieren oder Architektur ändern.

## Ablauf als Routine

1. **Scope festlegen:** kritische Dienste, Plattformen, Sicherheitsfunktionen und Ressourcen bestimmen.
2. **Messgrößen definieren:** technische und organisatorische Kapazitäten je Dienst auswählen.
3. **Schwellen festlegen:** Warnung, kritischer Bereich, Eskalation und Zielzustand beschreiben.
4. **Daten sichten:** Monitoring, Kosten, Lizenzen, Tickets, Incidents und Businessplanung auswerten.
5. **Bewerten:** Trend, Serviceauswirkung, Sicherheitsauswirkung und Zeit bis Engpass einschätzen.
6. **Maßnahme planen:** Skalierung, Bereinigung, Optimierung, Beschaffung, Architekturänderung oder Limit akzeptieren.
7. **Umsetzen und nachweisen:** Change, Ticket, Budgetentscheidung oder Konfigurationsänderung dokumentieren.
8. **Reviewen:** Wirksamkeit prüfen und Schwellen, Forecasts oder Verantwortlichkeiten anpassen.
9. **Eskalieren:** Engpässe mit Verfügbarkeits-, Sicherheits- oder Kostenwirkung ins Management Review geben.

## Entscheidungen

- Welche Dienste und Sicherheitsfunktionen sind kapazitätskritisch?
- Welche Schwellenwerte lösen technische Reaktion, Service Owner Review oder Managemententscheidung aus?
- Welche Wachstumsannahmen sind realistisch und wer bestätigt sie?
- Wann wird skaliert, optimiert, begrenzt oder bewusst Risiko akzeptiert?
- Welche Kapazitäten sind budget-, lieferanten- oder personalabhängig?
- Wie werden Kostenrisiken in Cloud- und Lizenzmodellen gesteuert?

## Evidenz

### Starke Evidenz

- Scope kritischer Dienste und Kapazitätsobjekte mit Ownern,
- Monitoring- oder Trendberichte mit Datum und Schwellen,
- Alert- und Eskalationsregeln,
- Kapazitätsmaßnahmen mit Ticket, Change oder Budgetentscheidung,
- Nachweise zu Log-, Backup-, Security-Monitoring- und Cloud-Limits,
- Reviewprotokoll mit Bewertung und Entscheidung,
- Managemententscheidung bei Ressourcen- oder Verfügbarkeitskonflikt.

### Schwache Evidenz

- Dashboard ohne Owner oder Reviewroutine,
- technische Auslastungswerte ohne Servicebezug,
- pauschale Aussage „Cloud skaliert automatisch“ ohne Limitprüfung,
- Kapazitätsplanung nur für Server, aber nicht für Logs, Backups oder Lizenzen,
- Alertliste ohne Reaktionsweg,
- Budgetantrag ohne Risikobezug.

### Evidenzlücken

- kritische Dienste ohne Kapazitätsmessung,
- keine Schwellenwerte oder Eskalationspunkte,
- keine Verbindung zur Businessplanung,
- volle Log- oder Backup-Speicher ohne Entscheidung,
- Cloud-Limits oder Lizenzgrenzen unbekannt,
- wiederholte Performance-Incidents ohne Ursachenanalyse.

## Wirksamkeitsprüfung

Prüffragen:

- Sind kritische Dienste und Sicherheitsfunktionen kapazitätsseitig im Scope?
- Können Owner erkennen, wann ein Engpass ein Service- oder Sicherheitsrisiko wird?
- Werden Trends vor dem Incident bewertet und behandelt?
- Gibt es Nachweise, dass Alerts zu Entscheidungen oder Maßnahmen führen?
- Sind Log-, Backup-, Monitoring- und Cloud-Kapazitäten berücksichtigt?
- Werden Ressourcen- und Budgetkonflikte rechtzeitig ins Management gegeben?

Mögliche Kennzahlen:

- Anteil kritischer Dienste mit definierten Kapazitätsschwellen,
- überfällige Kapazitätsmaßnahmen,
- Anzahl kritischer Schwellenüberschreitungen,
- Zeit bis Engpass nach Forecast,
- Kapazitätsbedingte Incidents,
- Log-/Backup-Speicherreichweite,
- Cloud-Limit- oder Lizenzgrenzen mit Eskalationsstatus.

## BSIG-/NIS2-Anschluss

Kapazitätsplanung und -überwachung sind anschlussfähig an NIS2-orientierte Themen wie Betriebssicherheit, Aufrechterhaltung kritischer Dienste, Business Continuity, Incident-Prävention, Monitoring und Risikomanagement. Der konkrete Bezug sollte im Anforderungsregister, in BCM-Unterlagen und im Management Review organisationsspezifisch geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung und keine Verfügbarkeits- oder Konformitätszusage.

## Grenzen

- Dieses Artefakt ist kein Performance-Engineering-Handbuch.
- Es ersetzt keine technische Architektur-, Lasttest- oder Cloud-Kostenanalyse.
- Es garantiert keine Verfügbarkeit und keine Einhaltung externer Serviceziele.
- Es trifft keine rechtliche Aussage zu konkreten Pflichten.
- Keine vertraulichen Betriebs-, Kosten- oder Kundendaten in öffentlichen Beispielen.

## Handoffs

- **Change-Handoff:** Skalierung, Architekturänderung, Wartungsfenster, Test- und Rollbackbedarf.
- **BCM-Handoff:** Kapazitätsengpass betrifft kritischen Geschäftsprozess oder Wiederanlaufziel.
- **Security-Handoff:** Logging, Monitoring, Backup, EDR, SIEM oder Schutzsysteme laufen kapazitätsseitig an Grenzen.
- **Finance-/Einkauf-Handoff:** Budget, Lizenzgrenzen, Cloud-Kosten, Beschaffungszeiten oder Vertragslimits.
- **Management-Handoff:** Restrisiko, Priorisierung, Kosten-/Verfügbarkeitskonflikt oder bewusste Leistungsbegrenzung.
- **Incident-/Problem-Handoff:** wiederholte Performance- oder Verfügbarkeitsstörungen durch Engpässe.
- **Audit-/Evidence-Handoff:** fehlende Schwellen, nicht nachvollziehbare Kapazitätsentscheidungen oder unvollständiger Scope.

## Typische Fehler

- Monitoring existiert, aber niemand bewertet Trends.
- Kapazität wird nur für produktive Server betrachtet, nicht für Logging, Backup oder Lizenzen.
- Cloud-Skalierung wird angenommen, obwohl Limits, Kosten oder Architektur begrenzen.
- Alerts erzeugen Lärm und keine Entscheidung.
- Businesswachstum erreicht IT erst nach dem Engpass.
- Kapazitätsmaßnahmen werden als rein technische Tickets behandelt und nicht priorisiert.
- Management erhält Auslastungsdiagramme ohne Entscheidungsfrage.

## Fiktives Mini-Beispiel

Ein fiktiver Online-Dienst plant eine Marketingkampagne. Der Service Owner informiert das Plattformteam über erwartetes Nutzerwachstum. Ein Trendbericht zeigt, dass Datenbank-Storage und Logspeicher in sechs Wochen kritisch werden. Das Plattformteam erstellt zwei Changes: Storage-Erweiterung und Anpassung der Logaufbewahrung. Finance gibt Budget frei; der ISMS-Owner dokumentiert, dass Security-Logs nicht gekürzt, sondern auf günstigerem Speicher ausgelagert werden.

Evidenz:

- Kapazitäts-Scope für den Dienst,
- Trendbericht mit Schwellen,
- Change-Tickets,
- Budgetentscheidung,
- Reviewnotiz zur Logaufbewahrung.
