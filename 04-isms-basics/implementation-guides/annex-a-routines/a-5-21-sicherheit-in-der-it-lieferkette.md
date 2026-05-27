
# A.5.21 — Sicherheit in der IT-Lieferkette

## Zweck

IT-Lieferketten bestehen aus Software, Hardware, Cloud-Diensten, Managed Services, Bibliotheken, Images, Updates, Integrationen, Supportzugängen und Subdienstleistern. Sicherheitsprobleme entstehen nicht nur beim direkten Lieferanten, sondern auch durch vorgelagerte Komponenten, Build- und Updatewege oder versteckte Abhängigkeiten.

Diese Routine sorgt dafür, dass IT-Lieferkettenrisiken sichtbar, bewertet, vertraglich und technisch gesteuert sowie bei Änderungen oder Vorfällen nachverfolgt werden.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine zur Steuerung sicherheitsrelevanter IT-Lieferketten. Sie erkennt kritische IT-Abhängigkeiten, bewertet Komponenten und Anbieter, verfolgt Schwachstellen und Änderungen, definiert Nachweise und verbindet Lieferantenmanagement, Architektur, Betrieb, Entwicklung, BCM und Incident Response.

## Typische Risiken

- Wenn Softwarekomponenten, Bibliotheken oder Container-Images unbekannt sind, können Schwachstellen nicht zugeordnet und behandelt werden.
- Wenn Updates oder Artefakte aus unsicheren Quellen bezogen werden, können manipulierte Komponenten in produktive Systeme gelangen.
- Wenn Managed-Service- oder Cloud-Abhängigkeiten nicht verstanden werden, bleiben Subdienstleister, Supportzugänge und Betriebsorte blinde Flecken.
- Wenn Hardware, Firmware oder Appliances ohne Sicherheits- und Updatebetrachtung beschafft werden, entstehen langlebige technische Risiken.
- Wenn Lieferanten-Schwachstellenmeldungen nicht verarbeitet werden, bleiben betroffene Produkte oder Dienste ungepatcht.
- Wenn Exit- und Ersatzfähigkeit fehlen, wird eine Lieferkettenstörung schnell zum Verfügbarkeits- oder Krisenthema.

## Trigger

- neue Software, Bibliothek, Plattform, Cloud-Service, Hardware, Appliance, Managed Service oder Integrationskomponente.
- Änderung von Version, Bezugsquelle, Build-Pipeline, Updatekanal, Subdienstleister oder Betriebsmodell.
- Schwachstellenmeldung, Herstellerhinweis, Security Advisory, kompromittierter Anbieter oder Incident.
- Beschaffung, Architekturentscheidung, Make-or-buy-Entscheidung oder Vertragsverlängerung.
- Release, Deployment, größere Migration oder technische Standardisierung.
- Auditfinding, Penetrationstest, Dependency-Scan oder SBOM-/Inventarfund.
- BCM-Review, Krisenübung oder Managementfrage zu kritischen IT-Abhängigkeiten.

## Rollen und Verantwortung

- **IT-/Plattform Owner:** verantwortet eingesetzte Plattformen, Komponenten, Updatekanäle und technische Betriebsrisiken.
- **Entwicklung / Product Owner:** verantwortet Softwareabhängigkeiten, Libraries, Container, CI/CD und Releaseentscheidungen.
- **Architekturrolle:** bewertet strategische Abhängigkeiten, Standardisierung, Ersatzfähigkeit und technische Schulden.
- **Einkauf / Vendor Management:** verbindet IT-Lieferkettenanforderungen mit Lieferantenregister und Vereinbarungen.
- **ISMS-Owner / Security-Rolle:** definiert Bewertungslogik, Schwachstellen-Handoff, Nachweise, Ausnahmen und Reporting.
- **BCM-/Krisenrolle:** bewertet Verfügbarkeits- und Wiederanlaufrisiken kritischer IT-Abhängigkeiten.
- **Datenschutz / Legal:** prüft personenbezogene Daten, Vertragsfragen, Subdienstleister und rechtliche Risiken.
- **Management:** entscheidet bei kritischer Abhängigkeit, nicht ersetzbaren Komponenten, Ressourcenbedarf oder akzeptiertem Restrisiko.

## Implementierung

### Minimalstart

Ziel: die kritischsten IT-Lieferkettenabhängigkeiten sichtbar und reaktionsfähig machen.

1. Die Organisation benennt kritische IT-Dienste, zentrale Softwareprodukte, Cloud-/Managed-Services und internetnahe Komponenten im Scope.
2. Für jede kritische Abhängigkeit werden Owner, Lieferant, Zweck, Daten-/Systembezug, Updateweg und Kontakt erfasst.
3. Schwachstellen- und Herstellerhinweise für kritische Komponenten werden abonniert oder über Dienstleister eingefordert.
4. Neue kritische Komponenten werden vor Nutzung kurz bewertet: Bezugsquelle, Supportstatus, Updatefähigkeit, Zugriff, Subdienstleister und Exit-Relevanz.
5. Offene Schwachstellen, unsichere Updatewege oder nicht ersetzbare Komponenten werden im Maßnahmen- oder Risikoregister geführt.
6. Bei Lieferkettenvorfällen gibt es einen Incident-Handoff und eine Liste potenziell betroffener Dienste.

Minimaler Nachweis:

- Register kritischer IT-Abhängigkeiten,
- Owner und Kontakt je Abhängigkeit,
- Nachweis zu Schwachstellen-/Herstellerinformationen,
- Bewertungsnotiz für neue kritische Komponenten,
- Maßnahmen- oder Risikoeintrag bei offenen Lieferkettenrisiken.

### Solide Praxis

Ziel: IT-Lieferkettenrisiken werden in Architektur, Beschaffung, Entwicklung und Betrieb integriert.

1. IT-Abhängigkeiten werden nach Kritikalität klassifiziert: produktionskritisch, internet-exponiert, identitätsnah, datenintensiv, schwer ersetzbar oder privilegiert.
2. Software- und Komponenteninventare werden risikobasiert aufgebaut: Produkte, Versionen, Libraries, Container, Images, Appliances, Firmware und SaaS-Dienste.
3. Bezugs- und Updatewege werden festgelegt: vertrauenswürdige Quellen, Signaturen, Repositories, Freigaben, Test- und Rollback-Verfahren.
4. Schwachstellenmanagement verbindet Lieferantenmeldungen, Dependency-Scans, Herstellerhinweise und Assetbezug.
5. Vereinbarungen mit Lieferanten adressieren Sicherheitsanforderungen aus A.5.20: Meldungen, Nachweise, Subdienstleister, Änderungen, Support und Exit.
6. Kritische Abhängigkeiten werden in BCM, Notfallplanung und Management Review sichtbar gemacht.
7. Ausnahmen wie unsupported Software, nicht patchbare Appliances oder fehlende SBOM werden befristet und risikobewertet.

Starke Evidenz:

- IT-Abhängigkeits- oder Komponentenregister,
- Bewertungslogik für Kritikalität und Lieferkettenrisiken,
- Nachweise zu Update- und Bezugswegen,
- Schwachstellen- und Advisory-Tickets mit Assetbezug,
- Lieferantenanforderungen oder Vertragsreferenzen,
- BCM-/Exit-Betrachtung für kritische Abhängigkeiten,
- Ausnahmeentscheidungen mit Ablaufdatum.

### Fortgeschritten

Ziel: IT-Lieferketten werden kontinuierlich überwacht und in sichere Entwicklung, Plattformbetrieb und Resilienzsteuerung eingebunden.

1. SBOM, Dependency-Scanning, Container-Scanning, Artifact-Repositories, CMDB und Ticketing sind integriert.
2. Build- und Release-Pipelines prüfen Herkunft, Integrität, Signaturen, Policies und bekannte Schwachstellen automatisiert oder halbautomatisch.
3. Kritische Cloud-, SaaS- und Managed-Service-Abhängigkeiten werden mit Subdienstleister-, Standort-, Support- und Exit-Informationen verfolgt.
4. Lieferkettenereignisse erzeugen Lagebilder: betroffene Assets, Services, Kundenprozesse, Schwachstellenstatus und Kommunikationsbedarf.
5. Technische Standards reduzieren Abhängigkeiten von nicht unterstützten Komponenten, unkontrollierten Repositories oder individuellen Ausnahmen.
6. Management sieht Konzentrationsrisiken, nicht ersetzbare Komponenten, Lieferantenabhängigkeiten, technische Schulden und Investitionsbedarf.

## Ablauf als Routine

1. **Abhängigkeit entsteht oder ändert sich:** neue Komponente, Lieferant, Version, Updateweg, Cloud-Service oder Build-Schritt.
2. **Einordnen:** Kritikalität, Datenbezug, Exposition, Privilegien, Supportstatus, Subdienstleister und Ersatzfähigkeit bewerten.
3. **Owner festlegen:** fachliche, technische und Lieferantenverantwortung zuordnen.
4. **Nachweise und Anforderungen prüfen:** Sicherheitsinformationen, Support, Updatefähigkeit, Schwachstellenkommunikation, Vereinbarungen und Bezugsweg bewerten.
5. **Freigabe oder Ausnahme entscheiden:** nutzen, nachschärfen, kompensieren, befristen, eskalieren oder ablehnen.
6. **Betrieb überwachen:** Advisories, Scans, Versionen, Updates, Subdienstleisteränderungen und offene Maßnahmen verfolgen.
7. **Schwachstellen behandeln:** Findings mit A.8.8 verbinden, priorisieren, patchen, kompensieren oder eskalieren.
8. **Incident-Handoff auslösen:** bei kompromittierter Lieferkette, aktiver Ausnutzung oder möglicher Betroffenheit kritischer Dienste.
9. **Verbessern:** Architekturstandards, Beschaffungskriterien, CI/CD-Regeln, Lieferantenanforderungen oder Exit-Pläne anpassen.

## Entscheidungen

- Welche IT-Abhängigkeiten sind kritisch genug für ein vertieftes Lieferkettenreview?
- Welche Komponenten müssen inventarisiert oder mit SBOM/Dependency-Informationen unterstützt werden?
- Welche Bezugsquellen, Repositories und Updatewege sind erlaubt?
- Wann darf unsupported oder schwer patchbare Technologie weiterbetrieben werden?
- Welche Schwachstellen- oder Lieferantenmeldungen lösen Incident-Triage aus?
- Welche Lieferantenanforderungen gehören in Vereinbarungen?
- Welche Abhängigkeiten brauchen Exit-, Ersatz- oder Notfallplanung?

## Evidenz

### Starke Evidenz

- aktuelles Register kritischer IT-Abhängigkeiten mit Owner, Version/Service, Lieferant und Kritikalität,
- Komponenten-, SBOM-, Dependency- oder Assetinformationen für relevante Systeme,
- dokumentierte Bewertung neuer kritischer Komponenten,
- Nachweise zu freigegebenen Bezugs- und Updatewegen,
- Advisory-, Scan- oder Schwachstellentickets mit Behandlung,
- Lieferantenvereinbarungen oder Anforderungsreferenzen,
- BCM-/Exit-Bewertungen für kritische Abhängigkeiten,
- Managemententscheidung bei nicht akzeptablen oder nicht kurzfristig behebbaren Risiken.

### Schwache Evidenz

- Softwareliste ohne Version, Owner oder Einsatzort,
- Lieferantenzertifikat ohne Bezug zur konkreten Komponente,
- Dependency-Scan ohne Triage oder Assetbezug,
- pauschale Aussage „Updates kommen vom Hersteller“ ohne Prozessnachweis,
- Architekturentscheidung ohne Betrachtung von Support, Exit oder Bezugsweg.

### Evidenzlücken

- kritische Komponenten ohne Owner,
- unbekannte Versionen oder Build-Artefakte,
- keine Verarbeitung von Hersteller- oder Lieferantenmeldungen,
- unsichere oder nicht dokumentierte Repositories,
- unsupported Technologie ohne Risikoentscheidung,
- Subdienstleister und Managed-Service-Abhängigkeiten unbekannt,
- kein Incident-Handoff bei Lieferkettenverdacht.

## Wirksamkeitsprüfung

Prüffragen:

- Sind die wichtigsten IT-Lieferkettenabhängigkeiten bekannt und verantwortet?
- Können kritische Komponenten betroffenen Services und Ownern zugeordnet werden?
- Werden neue oder geänderte Komponenten vor produktiver Nutzung bewertet?
- Sind Bezugs- und Updatewege ausreichend gesteuert?
- Werden Lieferanten- und Herstellerhinweise in Schwachstellenmanagement überführt?
- Sind unsupported oder schwer ersetzbare Komponenten als Risiko sichtbar?
- Sind kritische Abhängigkeiten in BCM, Exit-Planung und Management Review enthalten?

Mögliche Kennzahlen:

- Anteil kritischer Dienste mit dokumentierten IT-Abhängigkeiten,
- Komponenten ohne Owner oder Version,
- offene Lieferketten-Schwachstellen nach Kritikalität,
- unsupported Komponenten im Scope,
- überfällige Updates oder Advisories,
- kritische Abhängigkeiten ohne Exit-Bewertung,
- Lieferkettenereignisse mit abgeschlossener Betroffenheitsanalyse.

## BSIG-/NIS2-Anschluss

Sicherheit in der IT-Lieferkette ist anschlussfähig an NIS2-orientierte Themen wie Lieferkettensicherheit, sichere Beschaffung und Entwicklung, Schwachstellenmanagement, Cyberhygiene, Business Continuity, Incident-Fähigkeit und Governance über wesentliche technische Abhängigkeiten.

Für BSIG-/NIS2-Betroffenheit sollte die Organisation im Anforderungsregister prüfen, welche IT-Abhängigkeiten, Lieferantenklassen, Nachweise und Managemententscheidungen relevant sind. Dieses Artefakt ersetzt keine rechtliche Auslegung, Vertragsprüfung oder verbindliche Prüfung der Anwendbarkeit.

## Grenzen

- Dieses Artefakt ist keine vollständige Secure-Supply-Chain-Architektur und keine Tool-Empfehlung.
- Es ersetzt keine technische Produktprüfung, Codeanalyse, Hardwareprüfung oder Cloud-Sicherheitsbewertung.
- SBOM, Scanner oder Zertifikate ersetzen keine organisationsspezifische Risikoentscheidung.
- Keine Rechtsberatung, keine Datenschutzberatung, keine Zertifizierungszusage.
- Keine ISO-27002-Texte und keine echten Lieferanten-, Komponenten-, Schwachstellen- oder Kundendaten in Beispielen.

## Handoffs

- **Beschaffungs-/Vendor-Handoff:** neue IT-Lieferanten, Supportstatus, Anforderungen, Nachweise und Vertragsreferenzen.
- **Architektur-Handoff:** Plattformentscheidungen, Standardisierung, Ersatzfähigkeit, technische Schulden und Konzentrationsrisiken.
- **Entwicklungs-/DevOps-Handoff:** Dependencies, SBOM, CI/CD, Artefaktquellen, Container, Build- und Release-Regeln.
- **IT-Betriebs-Handoff:** Updates, Firmware, Appliances, Cloud-Dienste, Managed Services und Monitoring.
- **Schwachstellen-Handoff:** Advisories, Dependency-Findings, Herstellerhinweise und aktive Ausnutzung.
- **Incident-Handoff:** kompromittierter Anbieter, manipulierte Komponente, verdächtiges Update oder mögliche Betroffenheit kritischer Dienste.
- **BCM-/Krisen-Handoff:** nicht ersetzbare Komponenten, kritische Ausfälle, Exit-Szenarien und Notfallbetrieb.
- **Datenschutz-/Legal-Handoff:** personenbezogene Daten, Subdienstleister, Vertragsfragen oder Informationspflichten.
- **Management-Handoff:** unsupported Technologie, kritische Abhängigkeit, Ressourcenbedarf, akzeptiertes Restrisiko oder strategischer Wechsel.

## Typische Fehler

- Lieferkette wird nur als Lieferantenliste verstanden, nicht als Komponenten-, Update- und Build-Abhängigkeit.
- Dependency-Scans laufen, aber Findings werden keinem Service Owner zugeordnet.
- Kritische Appliances oder Firmware werden im Schwachstellenprozess vergessen.
- Updates werden aus Komfortquellen bezogen, ohne Herkunft und Integrität zu prüfen.
- Unsupported Software bleibt produktiv, weil sie im Fachprozess nicht sichtbar ist.
- Subdienstleister und Managed-Service-Abhängigkeiten werden nur in Datenschutzlisten geführt, aber nicht technisch bewertet.
- Management sieht einzelne Schwachstellen, aber keine Konzentrations- oder Exit-Risiken.

## Fiktives Mini-Beispiel

Ein fiktiver Plattformbetreiber nutzt eine Open-Source-Bibliothek in einem Kundenportal. Ein Dependency-Scan meldet eine kritische Schwachstelle. Der Product Owner ordnet die Bibliothek dem Portal zu, der Plattform Owner prüft Exposition und Updatefähigkeit. Das Update wird über die CI/CD-Pipeline getestet und ausgerollt. Parallel stellt das Team fest, dass für zwei weitere kritische Bibliotheken keine Owner im Komponentenregister hinterlegt sind. Diese Lücke geht als Maßnahme in den nächsten Architekturreview.

Evidenz:

- Dependency-Finding mit Komponentenbezug,
- Zuordnung zum Kundenportal,
- Update- und Testticket,
- Release-Nachweis,
- Komponentenregister-Lücke,
- Maßnahme für Architekturreview.
