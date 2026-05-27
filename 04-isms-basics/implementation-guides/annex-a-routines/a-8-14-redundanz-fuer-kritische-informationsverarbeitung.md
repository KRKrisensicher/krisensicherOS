
# A.8.14 — Redundanz für kritische Informationsverarbeitung

## Zweck

Redundanz für kritische Informationsverarbeitung sorgt dafür, dass zentrale Dienste bei Ausfall einzelner Komponenten, Standorte, Provider oder Abhängigkeiten weiterlaufen oder kontrolliert umschalten können. Der Kern ist nicht „alles doppelt“, sondern eine bewusste Entscheidung: Welche Verarbeitung ist kritisch, welche Redundanz ist nötig, wie wird sie getestet, und welches Restrisiko bleibt akzeptiert?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der kritische Informationsverarbeitung identifiziert, Redundanzanforderungen festgelegt, technische und organisatorische Umsetzungswege entschieden, Failover-Fähigkeit getestet und Abweichungen eskaliert werden. Die Routine verbindet Architektur, Betrieb, BCM, Monitoring, Lieferanten, Kosten und Managemententscheidungen.

## Typische Risiken

- Wenn kritische Dienste auf einzelnen Servern, Leitungen, Standorten oder Personen hängen, kann ein Einzelausfall den Geschäftsbetrieb unterbrechen.
- Wenn Redundanz zwar aufgebaut, aber nie getestet wird, scheitert Umschaltung im Ernstfall an Konfiguration, Datenstand oder Rollenklärung.
- Wenn Abhängigkeiten wie Identitätsdienste, DNS, Netzwerk, Schlüsselmanagement oder externe Provider fehlen, wirkt die Redundanz nur auf dem Papier.
- Wenn Redundanzanforderungen nicht mit RTO/RPO und BCM abgestimmt sind, wird entweder zu wenig oder unnötig teuer gebaut.
- Wenn aktive und redundante Komponenten gleich kompromittierbar sind, schützt Redundanz nicht vor Cyber- oder Fehlkonfigurationsszenarien.

## Trigger

- neuer oder geänderter kritischer Service, Prozess, Standort, Provider oder Architekturbaustein.
- Änderung von RTO/RPO, Kritikalität, Kundenanforderung, BCM-Annahme oder Risikobewertung.
- Incident, Ausfall, Beinaheausfall, Performanceproblem oder Failover-Fehlschlag.
- Cloud-/Rechenzentrums-, Netzwerk-, Strom-, Identitäts- oder Lieferantenänderung.
- neue Abhängigkeit durch SaaS, API, Plattformdienst, Datenbank, Messaging oder Automatisierung.
- BCM-Übung, Notfalltest, Auditfinding oder Managementfrage zur Resilienz.
- turnusmäßiger Architektur- und Redundanzreview.

## Rollen und Verantwortung

- **Service Owner / Fachbereich:** legt Kritikalität, Ausfalltoleranz und Priorität des Dienstes fest.
- **Architektur-/Plattform Owner:** entwirft Redundanz, Abhängigkeiten, Failover- und Rückfallwege.
- **IT-Betrieb / Operations:** betreibt Monitoring, Umschaltung, Tests, Kapazität und Betriebsdokumentation.
- **BCM-Verantwortliche:** verbindet Redundanz mit Notbetrieb, Wiederanlaufreihenfolge und Krisenübungen.
- **Security-Rolle / ISMS-Owner:** prüft Sicherheitsrisiken, Kompromittierungsszenarien, Evidenz und Eskalation.
- **Lieferantenmanagement:** klärt Provider-Redundanz, SLAs, Abhängigkeiten und Nachweise.
- **Management:** entscheidet über Zielkonflikte zwischen Kosten, Resilienz, Komplexität und akzeptiertem Restrisiko.

## Implementierung

### Minimalstart

Ziel: kritische Einzelausfallpunkte erkennen und bewusst behandeln.

1. Die Organisation benennt die wichtigsten kritischen Dienste und Informationsverarbeitungen im ISMS-/BCM-Scope.
2. Für jeden Dienst werden zentrale Abhängigkeiten dokumentiert: Anwendung, Datenbank, Identität, Netzwerk, Standort, Provider, Schlüssel, Personenrolle.
3. Single Points of Failure werden markiert und priorisiert.
4. Für die kritischsten Abhängigkeiten wird entschieden: redundant auslegen, manuell überbrücken, akzeptieren oder ersetzen.
5. Ein einfacher Failover- oder Wiederanlauftest wird geplant und dokumentiert.
6. Nicht geschlossene Redundanzlücken werden mit Risiko, Owner und Wiedervorlage festgehalten.

Minimaler Nachweis:

- Liste kritischer Dienste mit Owner,
- Abhängigkeits- und Single-Point-of-Failure-Übersicht,
- Entscheidung je kritischer Lücke,
- Test- oder Übungsnachweis,
- Management- oder Risikoakzeptanz bei offenen Lücken.

### Solide Praxis

Ziel: Redundanz wird mit Architektur, Betrieb und BCM wiederholbar gesteuert.

1. Kritische Dienste erhalten Redundanzziele passend zu RTO/RPO, Datenkonsistenz und Betriebspriorität.
2. Architekturentscheidungen beschreiben aktive/aktive, aktive/passive, manuelle Umschaltung, Hot/Warm/Cold-Standby oder organisatorische Ersatzprozesse.
3. Redundante Komponenten werden überwacht, gepatcht, konfiguriert und kapazitiv geprüft wie produktive Komponenten.
4. Failover-Tests prüfen Umschaltung, Rückschaltung, Datenstand, Rollen, Kommunikation und Auswirkungen auf Nutzer.
5. Provider- und SaaS-Abhängigkeiten werden auf realistische Redundanz und Exit-/Workaround-Fähigkeit geprüft.
6. Findings aus Tests führen zu Maßnahmen, Architekturverbesserungen oder Managemententscheidungen.
7. Redundanz wird mit Backup, Incident Response, Change Management und BCM-Übungen verbunden.

Starke Evidenz:

- Servicekritikalitäts- und Redundanzmatrix,
- Architekturentscheidung mit Abhängigkeiten,
- Monitoring- und Kapazitätsnachweise,
- Failover-/Fallback-Testprotokolle,
- Maßnahmen aus fehlgeschlagenen Tests,
- Lieferantennachweise oder SLA-Bewertungen,
- Managemententscheidung zu nicht redundanten kritischen Abhängigkeiten.

### Fortgeschritten

Ziel: Kritische Informationsverarbeitung ist resilient, getestet und entscheidungsfähig steuerbar.

1. Redundanzdesign berücksichtigt Standorte, Regionen, Provider, Identität, DNS, Schlüssel, Netzwerk, Datenreplikation und Betriebsrollen.
2. Chaos-, Resilienz- oder Notfallübungen prüfen kontrolliert realistische Ausfall- und Kompromittierungsszenarien.
3. Automatisierte Failover-Mechanismen werden überwacht, begrenzt und regelmäßig mit Rückfallplan getestet.
4. Änderungen an kritischen Komponenten lösen eine Prüfung der Redundanz- und Failoverfähigkeit aus.
5. Metriken zeigen Verfügbarkeitslücken, Testabdeckung, Failover-Zeit, Datenabweichungen, offene Single Points of Failure und Anbieterabhängigkeiten.
6. Management erhält entscheidungsfähige Szenarien: Kosten der Redundanz, erwartete Ausfallwirkung, technische Schulden und akzeptiertes Restrisiko.

## Ablauf als Routine

1. **Kritische Verarbeitung bestimmen:** Service, Prozess, Daten, Nutzergruppen, Abhängigkeiten und BCM-Relevanz klären.
2. **Ausfallannahmen definieren:** Komponente, Standort, Provider, Netzwerk, Identität, Datenbank, Bedienfehler oder Cyberereignis betrachten.
3. **Redundanzbedarf entscheiden:** Ziel, Architekturvariante, organisatorischer Workaround oder Risikoakzeptanz festlegen.
4. **Umsetzen:** technische Redundanz, Ersatzprozess, Monitoring, Dokumentation und Rollen vorbereiten.
5. **Testen:** Failover, Fallback, Datenkonsistenz, Kommunikation, Berechtigungen und Zeitbedarf prüfen.
6. **Nachweis ablegen:** Testverlauf, Ergebnis, Abweichungen, Maßnahmen und offene Risiken dokumentieren.
7. **Reviewen:** nach Änderungen, Incidents, Übungen und turnusmäßig Abhängigkeiten aktualisieren.
8. **Eskalieren:** nicht erfüllte Ziele, hohe Kosten, technische Grenzen oder kritische Single Points of Failure ins Management geben.

## Entscheidungen

- Welche Informationsverarbeitung ist kritisch genug für technische Redundanz?
- Welche Ausfallzeit und welcher Datenverlust sind fachlich tragbar?
- Welche Architekturvariante passt zu Risiko, Kosten und Betriebsfähigkeit?
- Welche Abhängigkeiten müssen ebenfalls redundant oder überbrückbar sein?
- Wie oft und wie realistisch werden Failover und Rückfall getestet?
- Wann ist organisatorischer Notbetrieb ausreichend, wann nicht?
- Wer akzeptiert offene Single Points of Failure und für welchen Zeitraum?

## Evidenz

### Starke Evidenz

- aktueller Scope kritischer Dienste mit Ownern,
- Abhängigkeitsmodell inklusive Single Points of Failure,
- Redundanz- und Architekturentscheidungen,
- Monitoring- und Kapazitätsnachweise für primäre und redundante Komponenten,
- Failover-/Fallback-Testprotokolle mit Ergebnis und Dauer,
- Maßnahmenlog aus Tests oder Incidents,
- Managemententscheidung bei akzeptierten Redundanzlücken.

### Schwache Evidenz

- Architekturdiagramm ohne Kritikalitäts- oder RTO/RPO-Bezug,
- Provider-SLA ohne Prüfung eigener Abhängigkeiten,
- Aussage „hochverfügbar“ ohne Testnachweis,
- Redundanz nur für Server, aber nicht für Datenbank, Identität oder Netzwerk,
- Testprotokoll ohne Ergebnis, Zeitbedarf oder Maßnahmen.

### Evidenzlücken

- unbekannte Single Points of Failure,
- kein Owner für kritische Abhängigkeiten,
- redundante Komponenten werden nicht gepatcht oder überwacht,
- Failover nie getestet,
- Rückschaltung unklar,
- SaaS- oder Providerabhängigkeit ohne Workaround,
- keine Managemententscheidung zu nicht wirtschaftlicher Redundanz.

## Wirksamkeitsprüfung

Prüffragen:

- Sind kritische Informationsverarbeitungen und ihre Abhängigkeiten aktuell bekannt?
- Gibt es Redundanzentscheidungen passend zu RTO/RPO und BCM-Annahmen?
- Wurden Failover und Rückfall realistisch getestet?
- Werden redundante Komponenten gleichwertig überwacht, gewartet und geschützt?
- Sind Provider-, Identitäts-, DNS-, Netzwerk- und Schlüsselabhängigkeiten berücksichtigt?
- Werden offene Single Points of Failure risikobewertet und entschieden?

Mögliche Kennzahlen:

- Anteil kritischer Dienste mit Redundanzentscheidung,
- offene Single Points of Failure,
- Failover-Testabdeckung,
- tatsächliche Umschaltzeit gegenüber Ziel,
- fehlgeschlagene oder eingeschränkte Tests,
- überfällige Maßnahmen aus Resilienztests,
- kritische Providerabhängigkeiten ohne Workaround.

## BSIG-/NIS2-Anschluss

Redundanz kritischer Informationsverarbeitung ist anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Business Continuity, Krisenfähigkeit, Incident Handling, Lieferkettenrisiken und Aufrechterhaltung kritischer Dienste. Der konkrete Bezug sollte über Anforderungsregister, BCM-Analyse, Risikoanalyse und Management Review organisationsspezifisch geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung der Betroffenheit, keine Verfügbarkeitsgarantie und keine branchenspezifische Pflichtprüfung.

## Grenzen

- Redundanz ersetzt keine Backups, kein Incident Response und kein BCM.
- Hochverfügbare Architektur kann Cyberereignisse oder Fehlkonfigurationen replizieren, wenn Schutzlogik fehlt.
- Dieses Artefakt ist kein technisches Referenzdesign für bestimmte Plattformen.
- Es garantiert keine Verfügbarkeit, Konformität oder Zertifizierungsfähigkeit.
- Es enthält keine ISO-27002-Texte und keine vertraulichen Architekturdetails.

## Handoffs

- **BCM-Handoff:** Kritikalität, RTO/RPO, Notbetrieb, Wiederanlaufreihenfolge und Übungen.
- **IT-/Architektur-Handoff:** Redundanzdesign, Abhängigkeiten, Failover, Monitoring, Kapazität und Rückschaltung.
- **Incident-Handoff:** Ausfall, Kompromittierung, Failover im Vorfall, technische Wiederherstellung.
- **Change-Handoff:** Änderungen an kritischen Komponenten, Providerwechsel, Netzwerk-/Identitätsänderungen.
- **Lieferanten-Handoff:** Provider-Redundanz, SLA, Ausfallkommunikation, Exit- oder Workaround-Fähigkeit.
- **Management-Handoff:** Kosten, Restrisiko, nicht redundante Abhängigkeiten, Zielkonflikte.
- **Audit-/Evidence-Handoff:** fehlende Testnachweise oder unklare Redundanzentscheidungen.

## Typische Fehler

- Redundanz wird auf Serverebene gebaut, aber zentrale Abhängigkeiten bleiben einfach.
- Failover wird nie geübt, weil Tests als zu riskant gelten.
- Redundante Komponenten werden schlechter gepatcht oder überwacht als Primärsysteme.
- Anbieter-SLAs werden mit eigener Wiederanlauffähigkeit verwechselt.
- Aktive/aktive Replikation übernimmt auch Fehler, Verschlüsselung oder Fehlkonfiguration.
- Management sieht Kosten der Redundanz, aber nicht die Ausfallwirkung der Lücke.
- Rückschaltung und Kommunikationswege fehlen im Test.

## Fiktives Mini-Beispiel

Ein fiktiver Logistikdienstleister stuft sein Tourenplanungssystem als kritisch ein. Die Abhängigkeitsanalyse zeigt, dass Anwendung und Datenbank redundant laufen, aber der zentrale Identitätsdienst ein Single Point of Failure ist. IT testet einen manuellen Notzugang für den Krisenbetrieb, BCM ergänzt den Notbetriebsplan und Management entscheidet über Budget für eine zweite Identitätsinstanz. Beim Failover-Test wird die Umschaltung dokumentiert; eine fehlende DNS-Anpassung wird als Maßnahme aufgenommen.

Evidenz:

- Kritikalitäts- und Abhängigkeitsübersicht,
- dokumentierter Single Point of Failure,
- Failover-Testprotokoll,
- BCM-Notbetriebsanpassung,
- Managemententscheidung zur Identitätsredundanz,
- Maßnahmenticket zur DNS-Korrektur.
