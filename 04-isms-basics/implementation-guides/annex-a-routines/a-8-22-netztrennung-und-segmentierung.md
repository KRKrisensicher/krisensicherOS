
# A.8.22 — Netztrennung und Segmentierung

## Zweck

Netztrennung und Segmentierung begrenzen, welche Systeme, Nutzergruppen, Dienste und Umgebungen miteinander kommunizieren dürfen. Die Routine reduziert Ausbreitungswege, schützt besonders kritische Bereiche und macht bewusste Übergänge sichtbar.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Segmentierungslogik für Netze, Cloud-Umgebungen, Administrationsbereiche, Entwicklungs-/Test-/Produktionsumgebungen, kritische Systeme und externe Zugänge. Segmentgrenzen, erlaubte Verbindungen, Owner, Ausnahmen und Reviews sind dokumentiert und technisch nachvollziehbar.

## Typische Risiken

- Wenn alle Systeme in flachen Netzen erreichbar sind, kann sich ein kompromittiertes Gerät schnell auf kritische Dienste auswirken.
- Wenn Produktions-, Test- und Administrationsbereiche nicht getrennt sind, können Fehler oder kompromittierte Konten sensible Systeme erreichen.
- Wenn Drittzugänge oder IoT-/OT-nahe Systeme im gleichen Netz wie Kernsysteme liegen, entstehen schwer kontrollierbare Ausbreitungswege.
- Wenn Segmentierungsregeln nicht reviewed werden, bleiben temporäre Verbindungen dauerhaft bestehen.
- Wenn Cloud- und On-Premises-Segmentierung unterschiedlich gesteuert werden, entstehen inkonsistente Schutzgrenzen.

## Trigger

- neues System, neue Umgebung, neuer Standort, neue Cloud-Landing-Zone oder neue Produktions-/OT-nahe Komponente.
- Einführung oder Änderung von Adminzugängen, Dienstleisterzugängen, Remote-Wartung oder kritischen Datenflüssen.
- Incident, Malwarefund, laterale Bewegung, Schwachstellenfinding oder Penetrationstest-Ergebnis.
- Architekturreview, Netzwerkreview, Risikoanalyse oder Managemententscheidung.
- Zusammenlegung, Migration oder Rückbau von Netzen und Umgebungen.
- turnusmäßiger Review von Segmenten, Übergängen und Ausnahmen.

## Rollen und Verantwortung

- **Netzwerk-/Plattform Owner:** plant und betreibt Segmentgrenzen, Firewall-Regeln, Routing, Cloud-Netzwerke und technische Validierung.
- **Service Owner / Asset Owner:** beschreibt Schutzbedarf, Datenflüsse und legitime Kommunikationswege.
- **Security-Architektur / ISMS-Owner:** definiert Segmentierungsprinzipien, Risikologik, Ausnahmen und Reviewanforderungen.
- **Change Owner:** stellt sicher, dass Segmentierungsänderungen getestet, dokumentiert und rückbaubar sind.
- **Entwicklung / Product Owner:** klärt Anforderungen zwischen Entwicklungs-, Test- und Produktionsumgebungen.
- **Facility / OT-Verantwortliche:** werden einbezogen, wenn Gebäude-, Produktions- oder Spezialnetze betroffen sind.
- **Management:** entscheidet bei Aufwand, Verfügbarkeitskonflikt, Legacy-Abhängigkeit oder akzeptiertem Restrisiko.

## Implementierung

### Minimalstart

Ziel: die wichtigsten Schutzgrenzen sichtbar machen und kritische Übergänge prüfen.

1. Die Organisation benennt kritische Segmente: Benutzer, Server, Administration, Internet-exponierte Systeme, Gäste/WLAN, Entwicklung/Test, Produktion, Backup, Cloud und Dienstleisterzugänge.
2. Für jedes Segment werden Zweck, Owner und grober Schutzbedarf beschrieben.
3. Erlaubte Verbindungen zwischen kritischen Segmenten werden in einer einfachen Matrix oder Regelübersicht festgehalten.
4. Besonders riskante Übergänge wie Adminzugriff, Drittzugriff, Internetbezug oder Produktivdatenzugriff werden priorisiert reviewed.
5. Temporäre oder pauschale Verbindungen werden befristet, begründet oder zurückgebaut.

Minimaler Nachweis:

- Segmentübersicht mit Ownern,
- Kommunikationsmatrix für kritische Übergänge,
- Tickets oder Changes für Segmentregeln,
- Reviewnotiz zu riskanten Übergängen,
- Ausnahmen mit Ablaufdatum und Entscheidung.

### Solide Praxis

Ziel: Segmentierung wird als Architektur- und Betriebsstandard wiederholbar angewendet.

1. Segmentierungsprinzipien werden festgelegt: Schutzbedarf, Funktion, Exposition, Umgebung, Administrationsbedarf und Vertrauensgrenze.
2. Neue Systeme erhalten bei Architektur- oder Change-Review eine Segmentzuordnung.
3. Verbindungen zwischen Segmenten benötigen Zweck, Owner, Protokoll, Quelle/Ziel, Laufzeit und Reviewdatum.
4. Netzwerk-, Cloud- und Identitätskontrollen werden kombiniert betrachtet, damit Segmentierung nicht nur auf IP-Regeln beruht.
5. Segmentierungsreviews prüfen Altfreigaben, temporäre Regeln, Schattenverbindungen und Umgehungswege.
6. Findings aus Incidents, Schwachstellenmanagement und Penetrationstests führen zu Segmentierungsverbesserungen.

Starke Evidenz:

- Segmentierungsmodell oder Architekturprinzipien,
- aktuelle Segment- und Kommunikationsmatrix,
- genehmigte Regeländerungen mit Zweck und Owner,
- Testergebnisse oder Validierungen von Segmentgrenzen,
- Reviewprotokolle mit Rückbau- oder Korrekturentscheidungen,
- Risikoentscheidungen für Legacy- oder Ausnahmeverbindungen.

### Fortgeschritten

Ziel: Segmentierung wird überprüfbar, dynamisch und mit Detektion verbunden.

1. Segmentgrenzen werden durch automatisierte Regelanalysen, Cloud-Posture-Prüfungen, Flow-Logs oder Erreichbarkeitstests regelmäßig validiert.
2. Kritische Systeme nutzen zusätzliche Kontrollen wie getrennte Adminpfade, Just-in-time-Zugriff oder stärkere Identitätsprüfung.
3. Mikrosegmentierung oder softwaredefinierte Policies werden dort eingesetzt, wo klassische Netzgrenzen nicht ausreichen.
4. Segmentierungsverletzungen, unerwartete Verbindungen oder neue exponierte Pfade erzeugen Alerts oder Reviewtickets.
5. Management sieht Risikoentwicklung: kritische Übergänge, Legacy-Ausnahmen, flache Netze, Umsetzungsaufwand und technische Schulden.

## Ablauf als Routine

1. **Segmentierungsbedarf entsteht:** neues System, Änderung, Finding, Incident oder Review.
2. **Schutzbedarf und Funktion bestimmen:** Daten, Servicekritikalität, Nutzergruppe, Umgebung und Exposition einordnen.
3. **Segment zuordnen:** bestehendes Segment nutzen oder neue Schutzgrenze begründen.
4. **Kommunikation definieren:** notwendige Quellen, Ziele, Protokolle, Laufzeit und Owner festhalten.
5. **Risiko prüfen:** Ausbreitungswege, Adminzugriff, Drittzugriff, Legacy-Abhängigkeit und Umgehungswege bewerten.
6. **Technisch umsetzen:** Firewall, Routing, Cloud-Policy, Identitätskontrolle oder Zugriffspfad ändern.
7. **Validieren:** Erreichbarkeit, Blockierung, Logging und Betriebswirkung testen.
8. **Reviewen und bereinigen:** Altregeln, temporäre Verbindungen und Ausnahmen prüfen.
9. **Eskalieren:** nicht trennbare kritische Bereiche oder hohe Aufwände ins Management Review geben.

## Entscheidungen

- Welche Segmente sind für den Minimalstart unverzichtbar?
- Welche Systeme dürfen direkt miteinander kommunizieren und warum?
- Welche Übergänge benötigen zusätzliche Authentisierung, Monitoring oder Genehmigung?
- Welche Legacy-Verbindungen werden akzeptiert, kompensiert oder abgebaut?
- Wie wird Segmentierung in Cloud-, Entwicklungs- und Produktionsumgebungen einheitlich gesteuert?
- Wann rechtfertigt Risiko einen Architekturumbau oder Investition?

## Evidenz

### Starke Evidenz

- aktuelles Segmentierungsmodell mit Ownern und Schutzbedarf,
- Kommunikationsmatrix mit Zweck, Quelle, Ziel, Protokoll und Reviewdatum,
- Changes für Segmentierungsregeln und Cloud-Policies,
- Testergebnisse zu erlaubten und blockierten Verbindungen,
- Reviewprotokolle mit Rückbauentscheidungen,
- Incident- oder Schwachstellen-Lessons-Learned mit Segmentierungsmaßnahmen,
- Managemententscheidung bei nicht umsetzbarer Trennung.

### Schwache Evidenz

- Netzwerkdiagramm ohne Datenflüsse oder Regelbezug,
- Firewall-Export ohne Segmentlogik,
- „VLAN vorhanden“ ohne Review der erlaubten Übergänge,
- Architekturfolie ohne technischen Abgleich,
- pauschale Trennung von Produktion und Test ohne Zugriffsnachweis.

### Evidenzlücken

- keine Owner für Segmente,
- unbekannte Verbindungen zwischen kritischen Bereichen,
- Adminpfade nicht getrennt oder nicht dokumentiert,
- Dritt- und Remote-Zugänge außerhalb der Segmentierungslogik,
- temporäre Freigaben ohne Ablauf,
- Cloud-Security-Groups nicht im Review enthalten.

## Wirksamkeitsprüfung

Prüffragen:

- Sind kritische Segmente, Schutzgrenzen und Owner bekannt?
- Gibt es eine nachvollziehbare Kommunikationsmatrix für kritische Übergänge?
- Werden Segmentierungsregeln vor Umsetzung risikobasiert geprüft?
- Wurden Segmentgrenzen technisch validiert, nicht nur beschrieben?
- Werden temporäre und Legacy-Verbindungen reduziert oder entschieden?
- Fließen Incident- und Schwachstellenbefunde in Segmentierungsmaßnahmen ein?

Mögliche Kennzahlen:

- Anteil kritischer Segmente mit aktueller Kommunikationsmatrix,
- Anzahl Übergänge ohne Owner oder Zweck,
- überfällige temporäre Segmentfreigaben,
- validierte Segmentgrenzen im Reviewzeitraum,
- offene Legacy-Ausnahmen,
- Findings zu unerwarteter Erreichbarkeit.

## BSIG-/NIS2-Anschluss

Netztrennung und Segmentierung sind anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Cyberhygiene, Zugriffsschutz, Incident-Begrenzung, sichere Architektur, Business Continuity und Schutz kritischer Dienste. Die konkrete Einordnung sollte organisationsspezifisch im Anforderungsregister, in Risikoanalysen und Architekturreviews erfolgen.

Dieses Artefakt ersetzt keine rechtliche Bewertung und keine verbindliche Prüfung der Anwendbarkeit.

## Grenzen

- Dieses Artefakt ist kein vollständiges Netz- oder Cloud-Architekturdesign.
- Segmentierung ersetzt nicht Patchmanagement, Zugriffsschutz, Monitoring oder Incident Response.
- Technische Trennung kann Verfügbarkeit, Betrieb und Support beeinflussen und braucht Change-Steuerung.
- Datenschutz- oder arbeitsrechtliche Fragen können entstehen, wenn Segmentierungslogs personenbezogen ausgewertet werden.
- Keine Zertifizierungszusage und keine Normtextübernahme.

## Handoffs

- **Architektur-Handoff:** neue Schutzgrenzen, Cloud-Landing-Zones, Zero-Trust- oder Mikrosegmentierungsentscheidungen.
- **Change-Handoff:** Regeländerungen, Routing, Security Groups, VPN- oder Adminpfade.
- **Incident-Handoff:** laterale Bewegung, Malwareausbreitung, unerwartete Segmentdurchlässigkeit.
- **Schwachstellen-Handoff:** kritische Systeme, die wegen Schwachstellen stärker getrennt oder kompensiert werden müssen.
- **Entwicklungs-Handoff:** Trennung von Entwicklung, Test, Produktion und CI/CD-Zugriffen.
- **BCM-Handoff:** Segmentierung beeinflusst Wiederanlauf, Notbetrieb oder kritische Dienstabhängigkeiten.
- **Management-Handoff:** Legacy-Ausnahmen, Investitionsbedarf, Risikoakzeptanz oder Betriebszielkonflikt.

## Typische Fehler

- Segmentierung wird mit VLAN-Namen verwechselt und nicht als erlaubte Kommunikation gesteuert.
- Produktions- und Testumgebungen sind formal getrennt, teilen aber Adminzugänge oder Datenpfade.
- Cloud-Segmentierung wird nicht mit On-Premises-Regeln zusammengeführt.
- Ausnahmen entstehen für Projekte und bleiben dauerhaft.
- Segmentgrenzen werden nie technisch getestet.
- Admin- und Backupnetze werden vergessen.
- Management erhält keine Entscheidung zu teuren Legacy-Trennungen.

## Fiktives Mini-Beispiel

Ein fiktives Softwareunternehmen stellt fest, dass Testsysteme direkten Zugriff auf eine produktive Datenbank haben. Der Product Owner bestätigt, dass dieser Zugriff nur während einer Migration gebraucht wurde. Der Plattform Owner entfernt die Regel, richtet für künftige Tests anonymisierte Daten in einer getrennten Umgebung ein und dokumentiert die Änderung im Segmentierungsreview. Eine offene Ausnahme für ein Legacy-Reporting wird befristet ins Management Review gegeben.

Evidenz:

- aktualisierte Kommunikationsmatrix,
- Change-Ticket zum Entfernen der Regel,
- Testnachweis der blockierten Verbindung,
- Reviewnotiz zur Datenbereitstellung,
- befristete Ausnahme für Legacy-Reporting.
