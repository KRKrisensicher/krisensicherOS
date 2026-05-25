<!-- kso:product-relevance
repo-scope: product
classification: template
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->

# Risikoanalyse Session State

## Zweck

Diese Vorlage hält den Zustand einer geführten Risikoanalyse fest. Sie ermöglicht, den dialogischen Risikoprozess zu unterbrechen, später fortzusetzen und offene Fragen, Annahmen, Human Gates und Artefakt-Outputs nachvollziehbar zu halten.

Sie ist ein Arbeitszustand, kein finaler Risikobericht.

## Nutzung

- pro Risikoszenario eine Session-State-Datei oder einen Abschnitt führen,
- nach jeder Dialogphase aktualisieren,
- offene Pflichtfelder und Human Gates sichtbar halten,
- erst nach fachlicher Bestätigung in Register, Risk-Control Map / SoA-Erweiterung oder Report übernehmen.

## Statuskopf

| Feld | Eintrag |
| --- | --- |
| Session-ID | RS-001 |
| Risiko-ID | R-001 oder offen |
| Titel / Kurzname |  |
| Scope / Bereich |  |
| aktueller Prozessschritt | 0 Start / 1 Risiko / 2 Maßnahmenlage / 3 Brutto / 4 Strategie / 5 Maßnahmen+Controls/SoA / 6 Netto / 7 Reporting |
| Status | in Arbeit / wartet auf Owner / wartet auf Management / bereit für Review / abgeschlossen |
| letzte Aktualisierung | Datum |
| nächster Termin / Review | Datum |

## Phase 1: Risiko beschreiben

| Pflichtfeld | Wert | Status |
| --- | --- | --- |
| Asset / Prozess / Service |  | offen / Annahme / bestätigt |
| Asset Owner / fachlicher Owner |  | offen / Annahme / bestätigt |
| Schwachstelle |  | offen / Annahme / bestätigt |
| Bedrohung |  | offen / Annahme / bestätigt |
| Auswirkung |  | offen / Annahme / bestätigt |
| Risikoszenario | Wenn [Bedrohung] die Schwachstelle [Schwachstelle] am Asset [Asset] ausnutzt, dann kann [Auswirkung] entstehen. | offen / Annahme / bestätigt |

## Phase 2: Aktuelle Maßnahmenlage

| Maßnahmenfeld | Beschreibung | Evidenz | Status |
| --- | --- | --- | --- |
| organisatorische Maßnahmen |  |  | offen / Annahme / bestätigt / evidenzgeprüft |
| technische Maßnahmen |  |  | offen / Annahme / bestätigt / evidenzgeprüft |
| prozessuale / personelle Maßnahmen |  |  | offen / Annahme / bestätigt / evidenzgeprüft |
| Monitoring / Detektion / Review |  |  | offen / Annahme / bestätigt / evidenzgeprüft |
| Incident Response / Krisenmanagement / BCMS |  |  | offen / Annahme / bestätigt / evidenzgeprüft |
| Control-/SoA-Referenzen aktuell |  |  | offen / Annahme / bestätigt |

## Phase 3: Bruttorisiko

| Kriterium | Wert 1-5 | Begründung |
| --- | --- | --- |
| Erkennbarkeit |  |  |
| Ausnutzbarkeit |  |  |
| Verborgenheit |  |  |
| Wahrscheinlichkeitsfaktor | max(...) |  |
| Sachschaden |  |  |
| Personenschaden |  |  |
| finanzieller Verlust |  |  |
| immaterieller Schaden |  |  |
| Schadensfaktor | max(...) |  |
| Brutto-Risikowert / Kategorie | W × S |  |

## Phase 4: Strategie

| Feld | Eintrag |
| --- | --- |
| Strategieoptionen | Akzeptanz / Vermeidung / Transfer / Minimierung |
| empfohlene Strategie als Vorarbeit |  |
| Begründung |  |
| verworfene Optionen |  |
| Human Gate | wer muss entscheiden? |
| Entscheidungslog-Referenz |  |

## Phase 5: Maßnahmen und Control-/SoA-Mapping

| Maßnahme | Wirkung | Owner | Fällig | Control-/SoA-Bezug | Evidenz | Wirksamkeitsprüfung | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Eintrittswahrscheinlichkeit / Schadensausmaß / beides |  |  |  |  |  | geplant / in Umsetzung / umgesetzt / wirksamkeitsgeprüft |

## Phase 6: Netto-/Restrisiko

| Kriterium | Wert 1-5 | Begründung |
| --- | --- | --- |
| Bewertungsstatus | Planwert / bestätigt |  |
| Erkennbarkeit |  |  |
| Ausnutzbarkeit |  |  |
| Verborgenheit |  |  |
| Wahrscheinlichkeitsfaktor | max(...) |  |
| Sachschaden |  |  |
| Personenschaden |  |  |
| finanzieller Verlust |  |  |
| immaterieller Schaden |  |  |
| Schadensfaktor | max(...) |  |
| Netto-/Restrisikowert / Kategorie | W × S |  |
| Veränderung gegenüber Brutto |  |  |

## Phase 7: Reporting

| Reportfeld | Status / Inhalt |
| --- | --- |
| Top-Risiko relevant? | ja / nein |
| Managemententscheidung offen? |  |
| Maßnahmenstatus berichtspflichtig? |  |
| Control-/SoA-Lücke berichtspflichtig? |  |
| HTML-Report gewünscht? | ja / nein |
| Report-Referenz |  |

## Offene Fragen

| Frage | an wen | bis wann | Status |
| --- | --- | --- | --- |
|  |  |  | offen / beantwortet / eskaliert |

## Annahmen

| Annahme | Risiko bei falscher Annahme | Prüfung durch | Status |
| --- | --- | --- | --- |
|  |  |  | offen / bestätigt / verworfen |

## Human Gates

| Entscheidung | Entscheider | vorbereitet durch | Frist | Status |
| --- | --- | --- | --- | --- |
| Risikoakzeptanz |  |  |  | offen / entschieden |
| Transfer |  |  |  | offen / entschieden |
| Vermeidung |  |  |  | offen / entschieden |
| Ressourcen für Maßnahmen |  |  |  | offen / entschieden |
| Kriterienänderung |  |  |  | offen / entschieden |

## Artefakt-Übernahme

| Zielartefakt | Eintrag übernommen? | Referenz |
| --- | --- | --- |
| Risikoanalyse-Register | nein / ja |  |
| Risk-Control Map / SoA-Erweiterung | nein / ja |  |
| Maßnahmenliste / Backlog | nein / ja |  |
| Entscheidungslog | nein / ja |  |
| Risikoreport | nein / ja |  |

## Grenzen

Dieser Session State darf keine echten Kunden-, Personen- oder vertraulichen Organisationsdaten enthalten, wenn er als öffentliches Beispiel genutzt wird. Risikoakzeptanz und Managemententscheidungen bleiben Human Gates.
