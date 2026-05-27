
# A.5.3 — Trennung unverträglicher Aufgaben

## Zweck

Trennung unverträglicher Aufgaben verhindert, dass einzelne Personen oder Rollen kritische Handlungen ohne ausreichende Gegenkontrolle planen, ausführen, freigeben und prüfen können. Der Kern ist nicht Misstrauen gegenüber Menschen, sondern robuste Prozessgestaltung gegen Fehler, Missbrauch, Interessenkonflikte und unbemerkte Machtkonzentration.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine Routine, mit der kritische Kombinationen von Aufgaben, Rechten und Entscheidungen erkannt, bewertet, getrennt oder kompensiert werden. Wo Trennung nicht möglich ist, werden Ausnahmen bewusst entschieden, überwacht und befristet.

## Typische Risiken

- Wenn eine Person Änderung, Freigabe und Produktivsetzung allein kontrolliert, können Fehler oder Manipulation unentdeckt bleiben.
- Wenn Adminrechte und fachliche Genehmigungsrechte zusammenfallen, entstehen unkontrollierte Machtkonzentrationen.
- Wenn kleine Teams keine Kompensationsmaßnahmen definieren, werden unvermeidbare Rollenkonflikte unsichtbar.
- Wenn Rollenwechsel nicht geprüft werden, können alte und neue Rechte gefährliche Kombinationen bilden.
- Wenn Dienstleister Umsetzung und Kontrolle zugleich übernehmen, fehlt unabhängige Steuerung.
- Wenn Notfallrechte nicht nachgeprüft werden, werden temporäre Ausnahmen dauerhaft.

## Trigger

- neue oder geänderte Rollen, Berechtigungsgruppen, Workflows oder Genehmigungswege.
- Rollenwechsel, Eintritt, Austritt oder Vertretungsregelung.
- neues System, neuer Prozess, neue Anwendung oder neuer Dienstleisterzugriff.
- Einführung privilegierter Rechte, Notfallzugriffe oder technischer Konten.
- Auditfinding, Fraud-Hinweis, Sicherheitsereignis oder Verdacht auf unzulässige Handlungskette.
- turnusmäßiger Berechtigungs-, Rollen- oder Prozessreview.
- organisatorische Engpässe, bei denen Trennung praktisch nicht vollständig möglich ist.

## Rollen und Verantwortung

- **Prozess Owner:** identifiziert kritische Prozessschritte und unverträgliche Aufgaben im Fachprozess.
- **Asset / Information Owner:** bewertet Schutzbedarf und Risiko bei Aufgabenkombinationen.
- **IT-/Plattform Owner:** liefert Rollen-, Gruppen- und Rechteinformationen und setzt technische Trennung um.
- **ISMS-Owner / Security-Rolle:** definiert Bewertungslogik, Mindestanforderungen, Review und Eskalation.
- **Führungskraft:** verantwortet Rollenzuschnitt, Vertretungen und Umsetzung im Team.
- **Interne Prüfung / Audit-Rolle:** prüft kritische Kombinationen, Nachweise und Kompensationsmaßnahmen.
- **Management:** entscheidet über nicht auflösbare Konflikte, Ressourcen und Risikoakzeptanz.

## Implementierung

### Minimalstart

Ziel: Kritische Aufgabenkonflikte in den wichtigsten Prozessen sichtbar machen.

1. Die Organisation benennt besonders kritische Prozesse: Zahlungen, Produktivänderungen, Zugriffsgenehmigung, Beschaffung, Kundendaten, Security-Monitoring.
2. Prozess Owner beschreiben je Prozess die kritischen Schritte: beantragen, genehmigen, ausführen, prüfen, protokollieren.
3. Offensichtlich unverträgliche Kombinationen werden markiert.
4. Bestehende Rollen und Rechte werden dagegen geprüft.
5. Nicht trennbare Fälle erhalten Kompensationsmaßnahme, Review oder Managemententscheidung.
6. Bei Rollenwechseln wird eine Konfliktprüfung ausgelöst.

Minimaler Nachweis:

- Liste kritischer Prozesse und Aufgaben,
- einfache Konfliktmatrix,
- Review einer Stichprobe kritischer Rollen,
- dokumentierte Ausnahme mit Kompensation,
- Managemententscheidung bei nicht auflösbarem Konflikt.

### Solide Praxis

Ziel: Aufgabentrennung wird in Rollenmodell, Zugriff und Prozessreviews eingebaut.

1. Konfliktregeln werden für zentrale Systeme und Prozesse definiert.
2. Zugriffsanträge prüfen nicht nur Einzelrechte, sondern gefährliche Kombinationen.
3. Rollenreviews betrachten Adminrechte, Freigaberechte, Vertretungen, Dienstleister und technische Konten.
4. Kompensationsmaßnahmen werden konkret festgelegt: Vier-Augen-Freigabe, nachgelagerter Review, Logging, Bericht, zeitliche Begrenzung.
5. Ausnahmen werden befristet und mit Risikoentscheidung geführt.
6. Findings aus Incident, Audit oder Kontrolle fließen in Konfliktregeln zurück.

### Fortgeschritten

Ziel: Konflikte werden laufend erkannt und entscheidungsfähig gesteuert.

1. IAM-, Ticket-, Workflow- oder GRC-Daten unterstützen Konflikterkennung.
2. Kritische Kombinationen lösen Alerts, zusätzliche Genehmigungen oder Pflichtreviews aus.
3. Notfallrechte und Just-in-time-Zugriffe werden nachträglich überprüft.
4. Dienstleisterhandlungen werden mit interner Freigabe und unabhängiger Kontrolle verbunden.
5. Management sieht nicht nur Konfliktzahlen, sondern nicht auflösbare Zielkonflikte und Ressourcenbedarf.
6. Organisationsdesign, Rollenmodell und Automatisierung reduzieren wiederkehrende Konflikte.

## Ablauf als Routine

1. **Kritischen Prozess auswählen:** anhand Risiko, Schutzbedarf, Finanzwirkung, Datenklasse oder Incident-Historie.
2. **Aufgaben zerlegen:** beantragen, freigeben, ausführen, prüfen, überwachen, ändern.
3. **Konflikte definieren:** Welche Kombination darf nicht ohne Kontrolle bei einer Rolle liegen?
4. **Rollen und Rechte prüfen:** Personen, Gruppen, Dienstleister, technische Konten und Vertretungen einbeziehen.
5. **Behandeln:** trennen, Rechte ändern, zweite Freigabe einbauen oder Kompensation definieren.
6. **Ausnahmen entscheiden:** befristet, begründet, risikobewertet und mit Wiedervorlage.
7. **Review durchführen:** Rollenwechsel, neue Systeme und regelmäßige Stichproben prüfen.
8. **Verbessern:** Konfliktregeln, Rollenmodell oder Prozesse anpassen.

## Entscheidungen

- Welche Prozesse und Systeme sind für Aufgabentrennung kritisch?
- Welche Kombinationen sind nicht akzeptabel, welche nur mit Kompensation?
- Wann reicht Vier-Augen-Prinzip, wann braucht es technische Trennung?
- Wer darf eine Ausnahme akzeptieren und wie lange?
- Wie wird Trennung in kleinen Teams realistisch umgesetzt?
- Welche Dienstleisterhandlungen benötigen unabhängige interne Kontrolle?

## Evidenz

### Starke Evidenz

- Konfliktmatrix für kritische Prozesse oder Systeme,
- Rollen- und Berechtigungsexporte zum Reviewzeitpunkt,
- Reviewprotokoll mit Entscheidung je Konflikt,
- Nachweise umgesetzter Rechteänderungen oder Prozessanpassungen,
- dokumentierte Kompensationsmaßnahmen mit Owner,
- Ausnahmeentscheidungen mit Ablaufdatum,
- Managemententscheidung bei strukturell nicht trennbaren Aufgaben.

### Schwache Evidenz

- allgemeine Aussage „Vier-Augen-Prinzip gilt“ ohne Prozessbezug,
- Organigramm ohne Rechte- oder Aufgabenanalyse,
- Zugriffsliste ohne Konfliktbewertung,
- mündliche Vertretungsregel ohne Nachweis,
- Toolregel ohne Review der Treffer.

### Evidenzlücken

- keine definierten kritischen Kombinationen,
- Admin- und Freigaberechte nicht gemeinsam geprüft,
- Notfallrechte ohne nachgelagerten Review,
- kleine Teams ohne dokumentierte Kompensation,
- Dienstleister führt aus und kontrolliert selbst,
- Ausnahmen ohne Laufzeit oder Risikoakzeptanz.

## Wirksamkeitsprüfung

Prüffragen:

- Sind die wichtigsten unverträglichen Aufgaben je kritischem Prozess definiert?
- Werden Rollenwechsel und neue Rechte auf Konflikte geprüft?
- Führen Reviews zu Rechteentzug, Prozessänderung oder Entscheidung?
- Sind Kompensationsmaßnahmen konkret und nachweisbar?
- Werden Notfall- und Dienstleisterzugriffe besonders betrachtet?
- Sieht Management strukturelle Konflikte, die operativ nicht lösbar sind?

Mögliche Kennzahlen:

- Anzahl kritischer Konflikte je Prozess oder System,
- überfällige Konfliktreviews,
- offene Ausnahmen ohne Wiedervorlage,
- Zeit bis Behebung kritischer Rollenkonflikte,
- Anteil Notfallrechte mit nachgelagertem Review,
- wiederkehrende Konflikte durch Rollenmodell oder Teamzuschnitt.

## BSIG-/NIS2-Anschluss

Aufgabentrennung ist anschlussfähig an NIS2-orientierte Governance, Risikomanagement, Zugriffsschutz, sichere Betriebsprozesse, Incident-Prävention und Managementaufsicht. Der konkrete Bezug sollte im Anforderungsregister, Risikoregister und bei kritischen Prozessen organisationsspezifisch geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung, keine Datenschutzprüfung und keine Aussage zu gesetzlicher Erfüllung.

## Grenzen

- Keine pauschale Vorgabe, welche Funktionen in jeder Organisation getrennt sein müssen.
- Keine Rechtsberatung zu Fraud, Haftung, Arbeitsrecht oder Mitbestimmung.
- Keine Zertifizierungs- oder Konformitätszusage.
- Keine vollständige IAM- oder Prozessdesign-Spezifikation.
- Kleine Organisationen brauchen oft Kompensation; das Artefakt erzeugt keine Scheinsicherheit durch unrealistische Trennung.

## Handoffs

- **Access-/IAM-Handoff:** Rollen, Gruppen, privilegierte Rechte, technische Konten, Rezertifizierung.
- **Prozess Owner-Handoff:** kritische Prozessschritte, Vier-Augen-Regeln, Freigabe- und Kontrollpunkte.
- **HR-Handoff:** Rollenwechsel, Vertretungen, Stellenzuschnitt und Abwesenheiten.
- **Vendor-Handoff:** Dienstleisterrechte, externe Freigaben, Kontrollnachweise.
- **Incident-Handoff:** Verdacht auf Missbrauch, Manipulation oder Umgehung von Kontrollen.
- **Management-Handoff:** nicht trennbare Aufgaben, Ressourcenengpass, akzeptiertes Restrisiko.
- **Audit-/Evidence-Handoff:** fehlende Konfliktregeln, lückenhafte Reviews oder schwache Kompensationen.

## Typische Fehler

- Aufgabentrennung wird nur im Finanzprozess betrachtet, nicht in IT- und Datenprozessen.
- Konflikte werden definiert, aber nicht gegen reale Berechtigungen geprüft.
- Kleine Teams verstecken Konflikte statt Kompensationen zu dokumentieren.
- Notfallrechte werden nach Nutzung nicht reviewed.
- Dienstleister erhalten breite Rechte ohne unabhängige Abnahme.
- Reviews erzeugen Listen, aber keine Entscheidungen.
- Ausnahmen bleiben dauerhaft, weil kein Ablaufdatum gesetzt wurde.

## Fiktives Mini-Beispiel

Ein fiktiver Onlinehändler prüft den Releaseprozess. Bisher kann dieselbe Person Code mergen, das Deployment freigeben und Produktivzugriff nutzen. Der Product Owner und Plattform Owner definieren eine Konfliktregel: Deployment-Freigabe und produktiver Adminzugriff werden getrennt. Für ein kleines Bereitschaftsteam wird eine befristete Ausnahme mit nachgelagertem Logreview eingerichtet.

Evidenz:

- Konfliktregel für den Releaseprozess,
- Berechtigungsexport der Deployment-Gruppe,
- Ticket zur Rechteänderung,
- Ausnahme für Bereitschaft mit Ablaufdatum,
- Logreview-Nachweis nach Notfalleinsatz.
