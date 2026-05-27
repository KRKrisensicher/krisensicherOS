
# A.8.31 — Trennung von Entwicklungs-, Test- und Produktivumgebungen

## Zweck

Die Trennung von Entwicklungs-, Test- und Produktivumgebungen verhindert, dass unfertiger Code, Testdaten, Debug-Zugriffe, Experimente oder fehlerhafte Änderungen den produktiven Betrieb gefährden. Sie schützt zugleich vor Datenabflüssen und vor stillen Abkürzungen zwischen Entwicklung und Betrieb.

Der Kern ist nicht „es gibt drei Umgebungen“, sondern eine betriebene Grenze: Wer darf wohin? Welche Daten dürfen genutzt werden? Wie gelangen Änderungen kontrolliert von Entwicklung über Test in Produktion? Wie werden Ausnahmen entschieden?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Routine, mit der Umgebungen, Datenflüsse, Zugriffe, Deploymentwege und Ausnahmen zwischen Entwicklung, Test, Staging und Produktion gesteuert werden. Ziel ist eine klare Trennung von Experiment, Prüfung und produktivem Betrieb.

## Typische Risiken

- Wenn Entwickler direkten Produktionszugriff haben, können unbeabsichtigte oder unfreigegebene Änderungen produktive Dienste stören.
- Wenn produktive Daten ungeschützt in Testumgebungen genutzt werden, können Vertraulichkeits- und Datenschutzrisiken entstehen.
- Wenn Test- und Produktivsysteme dieselben Zugangsdaten, Schlüssel oder Schnittstellen verwenden, können Fehlkonfigurationen echte Daten oder Dienste betreffen.
- Wenn Deployments Umgebungsgrenzen umgehen, fehlen Abnahme, Rollback und Nachvollziehbarkeit.
- Wenn Testumgebungen schwächer geschützt sind, können sie als Einstieg in produktionsnahe Systeme dienen.
- Wenn Notfallzugriffe nicht dokumentiert werden, wird die Trennung im Alltag ausgehöhlt.

## Trigger

- neues System, neue Anwendung, neue Plattform oder neue CI/CD-Pipeline.
- Änderung an Architektur, Hosting, Netzwerksegmentierung oder Cloud-Konten.
- Einführung oder Änderung von Entwicklungs-, Test-, Staging- oder Produktionsumgebungen.
- Nutzung produktiver oder produktionsnaher Daten außerhalb der Produktion.
- Release, Hotfix, Notfalländerung oder Rollback.
- Auditfinding, Incident, Fehl-Deployment oder Datenabflussverdacht.
- turnusmäßiger Review von Umgebungen, Zugängen und Deploymentwegen.

## Rollen und Verantwortung

- **Product Owner / Service Owner:** entscheidet fachlichen Bedarf an Umgebungen, Testtiefe und Go-live.
- **Entwicklungsteam:** nutzt Entwicklungs- und Testumgebungen gemäß Freigaben und liefert deploybare Änderungen.
- **IT-/Plattform Owner:** betreibt Umgebungen, Segmentierung, Identitäten, Secrets, Pipelines und Produktionszugänge.
- **Change-/Release Owner:** steuert Übergang von Test nach Produktion, Abnahme, Rollback und Nachweise.
- **Security-Rolle / ISMS-Owner:** definiert Mindesttrennung, Reviewlogik, Ausnahmebehandlung und Risikohandoff.
- **Datenschutz / Legal:** prüft personenbezogene oder vertrauliche Daten in Test- und Entwicklungsumgebungen.
- **Management:** entscheidet dauerhafte Ausnahmen, Ressourcenbedarf oder akzeptierte Betriebsrisiken.

## Implementierung

### Minimalstart

Ziel: produktive Systeme und produktive Daten werden von Entwicklung und Test nachvollziehbar abgegrenzt.

1. Kritische Anwendungen und Plattformen im Scope erhalten eine einfache Umgebungsübersicht: Entwicklung, Test, Staging, Produktion oder begründete Abweichung.
2. Für jede Umgebung werden Owner, Zweck, Datenklasse, Zugriffsgruppen und Deploymentweg benannt.
3. Direkte Änderungen in Produktion werden auf definierte Rollen und Notfälle beschränkt.
4. Produktive Daten in Test werden vermieden oder nur nach Freigabe, Schutzmaßnahme und Wiedervorlage genutzt.
5. Secrets, Zugangsdaten und Schnittstellen werden je Umgebung getrennt geführt.
6. Ausnahmen werden dokumentiert: Grund, Laufzeit, Risiko, Kompensation und Entscheidung.

Minimaler Nachweis:

- Umgebungsübersicht für kritische Systeme,
- Zugriffs- und Rollennachweise je Umgebung,
- dokumentierter Deployment- oder Change-Weg,
- Entscheidung zu Testdaten,
- Ausnahme- oder Notfallzugriffsprotokoll.

### Solide Praxis

Ziel: Umgebungen sind technisch, organisatorisch und prozessual getrennt.

1. Umgebungen werden nach Kritikalität und Produktivnähe klassifiziert.
2. Netzwerk, Identitäten, Secrets, Logging, Datenbanken, Cloud-Konten und Schnittstellen werden getrennt oder kontrolliert gekoppelt.
3. Deployments erfolgen über definierte Pipeline-, Change- oder Release-Schritte mit Prüfung und Freigabe.
4. Produktionszugriffe werden gesondert genehmigt, protokolliert und reviewed.
5. Testdatenmanagement legt fest, wann synthetische, anonymisierte, maskierte oder produktive Daten zulässig sind.
6. Staging- und Testumgebungen erhalten angemessene Schutzmaßnahmen, wenn sie produktionsnah sind.
7. Umgebungsreviews prüfen regelmäßig Zugänge, Datenbestände, Secrets, Schnittstellen und Abweichungen.

Starke Evidenz:

- Umgebungs- und Datenflussdiagramm,
- Rollenkonzept je Umgebung,
- Pipeline-/Release-Protokolle,
- Produktionszugriffsreviews,
- Testdatenfreigaben,
- Secret-/Konfigurationsnachweise ohne Offenlegung geheimer Werte,
- Ausnahmeentscheidungen mit Ablaufdatum.

### Fortgeschritten

Ziel: Trennung ist in Plattform, Automatisierung und Governance eingebaut.

1. Infrastructure-as-Code, Policy-as-Code oder Plattformstandards erzwingen Umgebungsgrenzen.
2. CI/CD-Pipelines trennen Build, Test, Approval, Deployment und Rollback technisch nachvollziehbar.
3. Produktionszugriffe laufen über Just-in-time-, Break-glass- oder Privileged-Access-Verfahren mit Review.
4. Datenmaskierung, synthetische Daten und automatisierte Bereinigung reduzieren Testdatenrisiken.
5. Abweichungen werden über Monitoring, Cloud-Policy, Konfigurationschecks oder Auditlogs erkannt.
6. Management sieht entscheidungsfähige Kennzahlen zu direkten Produktionszugriffen, Umgehungen, Testdatenrisiken und überfälligen Ausnahmen.

## Ablauf als Routine

1. **Umgebungsbedarf entsteht:** neues System, Feature, Testbedarf, Plattformwechsel oder Releaseprozess.
2. **Scope festlegen:** Zweck, Kritikalität, Datenklasse und Produktivnähe der Umgebung bestimmen.
3. **Grenzen gestalten:** Zugriffe, Netzwerk, Secrets, Daten, Schnittstellen und Deploymentwege trennen.
4. **Freigaben definieren:** wer darf entwickeln, testen, abnehmen, deployen und im Notfall eingreifen?
5. **Daten steuern:** Testdatenbedarf prüfen und Schutzmaßnahme festlegen.
6. **Änderungen überführen:** Entwicklung, Test, Abnahme, Release und Rollback nachvollziehbar durchführen.
7. **Ausnahmen behandeln:** Notfallzugriffe, direkte Produktionsänderungen oder produktive Testdaten befristen und reviewen.
8. **Wirksamkeit prüfen:** Zugriffslisten, Deploymentprotokolle, Umgebungsabweichungen und Testdatenbestände prüfen.
9. **Verbessern:** Findings in Plattformstandard, Change-Prozess oder Testdatenmanagement zurückspielen.

## Entscheidungen

- Welche Systeme benötigen getrennte Entwicklungs-, Test-, Staging- und Produktionsumgebungen?
- Welche Abweichungen sind für kleine Systeme vertretbar und wie werden sie kompensiert?
- Wer darf direkten Produktionszugriff haben und unter welchen Bedingungen?
- Welche Daten dürfen in Test- oder Entwicklungsumgebungen genutzt werden?
- Welche Deploymentwege dürfen Produktion verändern?
- Wann blockiert fehlende Trennung einen Go-live?
- Welche technischen Schulden bei Umgebungen müssen ins Management Review?

## Evidenz

### Starke Evidenz

- aktuelle Umgebungsübersicht mit Ownern und Datenklassen,
- Rollen- und Zugriffsmodell je Umgebung,
- Release-, Change- oder Pipeline-Nachweise,
- Protokolle direkter Produktionszugriffe und Reviews,
- Testdatenentscheidungen mit Schutzmaßnahmen,
- technische Nachweise für getrennte Secrets, Konten oder Konfigurationen,
- dokumentierte Ausnahmen mit Risikoentscheidung und Ablaufdatum.

### Schwache Evidenz

- Architekturdiagramm ohne Zugriff- oder Datenbezug,
- Aussage „Prod und Test sind getrennt“ ohne Nachweis,
- Screenshots einzelner Cloud-Ressourcen ohne Scope,
- Pipeline existiert, kann aber manuell umgangen werden,
- Testdatenregel ohne tatsächlichen Datenreview,
- Adminzugriffe ohne Nutzungsauswertung.

### Evidenzlücken

- keine Übersicht über produktionsnahe Testumgebungen,
- gemeinsame Secrets oder Konten über Umgebungen hinweg,
- produktive Daten in Test ohne Freigabe,
- direkte Produktionsänderungen ohne Change-Nachweis,
- keine Reviews privilegierter Produktionszugriffe,
- Ausnahmen ohne Ablaufdatum oder Managemententscheidung.

## Wirksamkeitsprüfung

Prüffragen:

- Kann für kritische Systeme nachvollzogen werden, welche Umgebungen existieren und wozu?
- Sind produktive Zugriffe, Daten und Secrets von Entwicklung und Test getrennt?
- Werden Änderungen über definierte Release- oder Change-Wege in Produktion gebracht?
- Sind direkte Produktionszugriffe selten, begründet und reviewed?
- Werden produktive Daten in Testumgebungen vermieden oder angemessen entschieden?
- Sind produktionsnahe Testumgebungen ähnlich geschützt wie ihr Risiko es verlangt?
- Werden Umgehungen und Ausnahmen nachverfolgt und reduziert?

Mögliche Kennzahlen:

- Anteil kritischer Systeme mit aktueller Umgebungsübersicht,
- Anzahl direkter Produktionszugriffe je Zeitraum,
- überfällige Umgebungs- oder Zugriffsreviews,
- Testumgebungen mit produktiven Daten,
- offene Ausnahmen zur Umgebungstrennung,
- fehlgeschlagene oder rückgerollte Releases wegen Umgebungsabweichungen.

## BSIG-/NIS2-Anschluss

Die Trennung von Entwicklungs-, Test- und Produktivumgebungen ist anschlussfähig an NIS2-orientierte Themen wie sichere Entwicklung, Änderungssteuerung, Zugriffsschutz, Cyberhygiene, Schutz produktiver Dienste und Risikomanagement. Der konkrete Bezug sollte über Anforderungsregister, Assetkritikalität und Datenklassifizierung geprüft werden.

Dieses Artefakt ersetzt keine rechtliche oder datenschutzrechtliche Bewertung.

## Grenzen

- Dieses Artefakt ist kein detailliertes Netzwerk-, Cloud- oder CI/CD-Design.
- Es ersetzt keine Datenschutzprüfung für produktive Daten in Testumgebungen.
- Es garantiert keine Verfügbarkeit, Sicherheit oder Konformität.
- Es enthält keine ISO-27002-Texte und keine geheimen Konfigurationswerte.
- Es darf nicht als ausreichend gelten, wenn die Umgebungsgrenzen technisch umgangen werden können und niemand es prüft.

## Handoffs

- **Change-/Release-Handoff:** Überführung in Produktion, Notfalländerung, Rollback oder fehlende Abnahme.
- **Access-Handoff:** direkte Produktionszugriffe, Adminrechte, externe Entwickler oder technische Konten.
- **Datenschutz-/Legal-Handoff:** produktive oder personenbezogene Daten in Test, Logging, Maskierung, Aufbewahrung oder Drittzugriffe.
- **Architektur-/Plattform-Handoff:** Segmentierung, Cloud-Konten, CI/CD, Secrets, Schnittstellen und Umgebungsstandard.
- **Incident-Handoff:** Fehl-Deployment, Datenabfluss aus Test, kompromittierte Testumgebung oder unautorisierte Produktionsänderung.
- **Management-Handoff:** dauerhafte Ausnahmen, fehlende Plattformressourcen, technische Schulden oder Go-live trotz Trennungsmängeln.
- **Audit-/Evidence-Handoff:** unklare Umgebungsliste, fehlende Reviewnachweise oder nicht prüfbare Deploymentwege.

## Typische Fehler

- Testumgebungen enthalten Produktionsdaten, werden aber wie harmlose Spielwiesen behandelt.
- Entwickler haben dauerhafte Adminrechte auf Produktion, weil es schneller ist.
- Pipeline und Change-Prozess existieren, werden aber bei Hotfixes regelmäßig umgangen.
- Secrets werden zwischen Umgebungen kopiert.
- Staging ist produktionsnah, aber deutlich schwächer geschützt.
- Umgebungen werden angelegt, aber nie wieder bereinigt.
- Management sieht Releasegeschwindigkeit, aber nicht die Risiken aus Abkürzungen.

## Fiktives Mini-Beispiel

Ein fiktiver Online-Dienst betreibt Entwicklung, Staging und Produktion in getrennten Cloud-Konten. Beim Review fällt auf, dass Staging eine Kopie produktiver Kundendaten enthält. Der Plattform Owner stoppt neue Kopien, der Product Owner bestätigt den Testbedarf und Datenschutz wird zur Schutzbewertung einbezogen. Das Team entscheidet auf synthetische Testdaten umzustellen. Bis dahin wird die Staging-Umgebung stärker abgeschottet und die Ausnahme mit Ablaufdatum dokumentiert.

Evidenz:

- Umgebungsübersicht,
- Reviewfinding zu Staging-Daten,
- Entscheidung zum Testdatenwechsel,
- temporäre Schutzmaßnahme,
- Ausnahme mit Wiedervorlage,
- aktualisierte Testdatenregel.
