<!-- kso:product-relevance
repo-scope: product
classification: template
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->

# Risikoanalyse-Register

## Zweck

Diese Vorlage unterstützt Risikoanalysen im ISMS entlang der Logik:

```text
Risiko = Schwachstelle + Asset + Bedrohung
```

Sie ist kein Risikotool. Sie ist ein Registerschema, das in Markdown, Tabellenkalkulation, Ticketsystem oder GRC-Tool übernommen werden kann.

## Trigger

Nutzen, wenn:

- neue Risiken aus Incidents, Audits, Änderungen, Asset Reviews oder Workshops entstehen,
- bestehende Risiken überprüft werden,
- Maßnahmen abgeleitet oder mit einer Control-Taxonomie oder SoA verbunden werden,
- Brutto-, Netto- und Zielrisiken nachvollziehbar gemacht werden sollen.

## Nutzer

- ISB / CISO / ISMS-Owner,
- Asset Owner / Prozess Owner,
- Control Owner / Maßnahmenowner,
- Management Review-Facilitator,
- Reviewer oder interne Auditrolle.

## Arbeitsregeln

SoA optional: Wenn noch keine ISO-27001-SoA existiert, werden Control-Referenzen zunächst als interne Risk-Control Map geführt. Eine spätere ISO-27001-SoA braucht eine eigene lizenzkonforme Normgrundlage.


1. Kein Risiko ohne Asset, Schwachstelle und Bedrohung erfassen.
2. Vor der Bruttobewertung die aktuelle Maßnahmenlage darstellen; KI kann per Fragebogen vorbereiten, Owner bestätigen fachlich.
3. Bruttorisiko mit den Kriterien für Eintrittswahrscheinlichkeit und Schadensausmaß bewerten; vorhandene Maßnahmen werden als Kontext dokumentiert, senken den Bruttowert aber nicht automatisch.
4. Strategie wählen: Akzeptanz, Vermeidung, Transfer oder Minimierung mit Maßnahmen.
5. Maßnahmen planen und mit Control-/SoA-Einträgen, Ownern, Evidenz und Wirksamkeitsprüfung verbinden.
6. Netto-/Restrisiko nach Strategie und Maßnahmenplanung mit denselben Kriterien bewerten; bei noch nicht wirksamen Maßnahmen als Planwert markieren.
7. Bestätigtes Nettorisiko erst nach Umsetzung und Wirksamkeitsprüfung dokumentieren.

## Bewertungsskalen

Siehe [`04-isms-basics/risikomanagement-methodik.md`](../risikomanagement-methodik.md) für die verbindliche Arbeitslogik:

- Eintrittswahrscheinlichkeit: Maximalwert aus Erkennbarkeit, Ausnutzbarkeit und Verborgenheit.
- Schadensausmaß: Maximalwert aus Sachschaden, Personenschaden, finanziellem Verlust und immateriellem Schaden.
- Risikowert: Wahrscheinlichkeitsfaktor × Schadensfaktor.

## Registerfelder

| Feld | Eintrag |
| --- | --- |
| Risiko-ID | R-001 |
| Status | neu / in Bewertung / in Behandlung / akzeptiert / geschlossen / Wiedervorlage |
| Scope / Bereich |  |
| Asset / Prozess / Service |  |
| Asset Owner |  |
| Schwachstelle |  |
| Bedrohung |  |
| Risikoszenario | Wenn [Bedrohung] die Schwachstelle [Schwachstelle] am Asset [Asset] ausnutzt, dann kann [Auswirkung] entstehen. |
| Auswirkung / Schadensbeschreibung |  |
| Quelle / Trigger | Incident / Audit / Änderung / Workshop / Asset Review / externe Meldung / Sonstiges |
| Erhebungsstatus aktuelle Maßnahmen | offen / per Fragebogen vorbereitet / durch Owner bestätigt / evidenzgeprüft |
| Aktuelle organisatorische Maßnahmen |  |
| Aktuelle technische Maßnahmen |  |
| Aktuelle personelle / prozessuale Maßnahmen |  |
| Aktuelle Krisenmanagement-/BCMS-/Incident-Response-Fähigkeiten |  |
| Evidenz aktueller Maßnahmen |  |
| Control-/SoA-Referenzen aktuell |  |
| KI-Fragebogen-Referenz | Link oder Ablageort; keine vertraulichen Volltexte in öffentliche Beispiele |
| Brutto: Erkennbarkeit | 1-5 |
| Brutto: Ausnutzbarkeit | 1-5 |
| Brutto: Verborgenheit | 1-5 |
| Brutto: Wahrscheinlichkeitsfaktor | max(Erkennbarkeit, Ausnutzbarkeit, Verborgenheit) |
| Brutto: Sachschaden | 1-5 |
| Brutto: Personenschaden | 1-5 |
| Brutto: finanzieller Verlust | 1-5 |
| Brutto: immaterieller Schaden | 1-5 |
| Brutto: Schadensfaktor | max(Sachschaden, Personenschaden, finanzieller Verlust, immaterieller Schaden) |
| Brutto: Risikowert / Kategorie | W × S / sehr gering bis sehr hoch |
| Strategie | Akzeptanz / Vermeidung / Transfer / Minimierung |
| Strategiebegründung | Warum diese Strategie? Welche Alternative wurde verworfen? |
| Transferziel, falls relevant | Versicherung / Outsourcing / Krisenmanagement / BCMS / anderes |
| Geplante Maßnahmen |  |
| Maßnahmen-IDs |  |
| Control-/SoA-Referenzen geplant |  |
| Maßnahmenwirkung erwartet | Eintrittswahrscheinlichkeit / Schadensausmaß / beides |
| Netto/Restrisiko: Bewertungsstatus | Planwert / bestätigt |
| Netto: Erkennbarkeit | 1-5 |
| Netto: Ausnutzbarkeit | 1-5 |
| Netto: Verborgenheit | 1-5 |
| Netto: Wahrscheinlichkeitsfaktor | max(...) |
| Netto: Sachschaden | 1-5 |
| Netto: Personenschaden | 1-5 |
| Netto: finanzieller Verlust | 1-5 |
| Netto: immaterieller Schaden | 1-5 |
| Netto: Schadensfaktor | max(...) |
| Netto: Risikowert / Kategorie | W × S / sehr gering bis sehr hoch |
| Bestätigtes Nettorisiko nach Wirksamkeitsprüfung | Wert / Kategorie / Datum |
| Entscheidung / Freigabe nötig | ja / nein; wer entscheidet? |
| Managemententscheidung / Akzeptanz | Referenz auf Entscheidungslog |
| Review-Kadenz | quartalsweise / jährlich / anlassbezogen |
| Nächster Review | Datum |
| Offene Fragen / Annahmen |  |

## Beispiel ohne echte Organisationsdaten

| Feld | Beispiel |
| --- | --- |
| Risiko-ID | R-001 |
| Asset / Prozess / Service | Fiktiver Cloud-Dateiaustausch |
| Schwachstelle | Externe Freigaben werden nicht regelmäßig überprüft. |
| Bedrohung | Ehemalige Projektbeteiligte oder externe Dritte greifen weiter auf Dateien zu. |
| Risikoszenario | Wenn externe Dritte bestehende Freigaben ausnutzen, können vertrauliche Projektdokumente unberechtigt offengelegt werden. |
| Brutto: Wahrscheinlichkeitsfaktor | 4 |
| Brutto: Schadensfaktor | 3 |
| Brutto: Risikowert / Kategorie | 12 / mittel |
| Vorhandene Maßnahmen | Manuelle Freigabe durch Projektleitung. |
| Netto: Risikowert / Kategorie | 9 / mittel |
| Behandlungsentscheidung | behandeln |
| Geplante Maßnahmen | Quartalsweiser Freigabenreview, Ablaufdatum für neue Freigaben, Stichprobe im Management Review. |
| Control-/SoA-Referenzen geplant | organisationsspezifische Control-ID, keine Normtexte kopieren. |
| Netto-/Restrisiko | 4 / gering, Planwert |

## Output

- bewertetes Risikoszenario,
- Brutto- und Netto-/Restrisikobewertung mit Planwert-/Bestätigungsstatus,
- Maßnahmen- und Control-/SoA-Bezug,
- offene Managemententscheidungen,
- Review- und Evidenzbedarf.

## Evidenz

Als Evidenz entstehen das Register selbst, Workshopnotizen, Control-/SoA-Mapping, Maßnahmenstatus, Entscheidungslog, Wirksamkeitsprüfungen und Management-Review-Auszüge.

## Grenzen

Diese Vorlage ersetzt keine Rechtsberatung, Datenschutzbewertung, Zertifizierungsprüfung oder Risikoakzeptanzentscheidung. Echte Organisations-, Personen- und Kundendaten gehören nur in freigegebene interne Arbeitsumgebungen.
