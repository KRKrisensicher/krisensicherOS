<!-- kso:product-relevance
repo-scope: product
classification: product-module
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# ISMS-Risikomanagement-Methodik

## Zweck

Diese Methodik beschreibt, wie Organisationen Informationssicherheitsrisiken im ISMS identifizieren, bewerten, behandeln, mit Maßnahmen und Control-/SoA-Referenzen verbinden und regelmäßig steuern können. Eine vollständige SoA setzt eigene lizenzkonforme ISO-27001-Grundlagen oder eine organisationsspezifische Control-Taxonomie voraus.

Sie ist bewusst kein Risikotool. krisensicherOS liefert die Arbeitslogik, Vorlagen und Reviewpunkte, damit Nutzerorganisationen Risikoanalysen in ihren eigenen Registern, Ticketsystemen, Dokumentenablagen oder GRC-Tools betreiben können.

## Grundsatz

Ein Risiko wird in krisensicherOS als Zusammenspiel aus drei Elementen beschrieben:

```text
Risiko = Schwachstelle + Asset + Bedrohung
```

Ein Eintrag im Risikoregister ist erst bewertbar, wenn alle drei Elemente benannt sind:

- **Asset:** betroffener Informationswert, Prozess, Service, System, Standort, Rolle oder Dienstleister.
- **Schwachstelle:** Eigenschaft, Lücke oder Zustand, durch den ein Schaden möglich wird.
- **Bedrohung:** Ereignis, Akteur, Fehler, Ausfall, Missbrauch oder Umweltbedingung, die die Schwachstelle ausnutzen kann.

Beispielstruktur, ohne echte Organisationsdaten:

```text
Wenn [Bedrohung] die Schwachstelle [Schwachstelle] am Asset [Asset] ausnutzt,
dann kann [Auswirkung] entstehen.
```

## Dialogischer Risikoprozess

Der Risikoprozess kann als geführter Frageprozess durchgeführt werden. Dafür nutzt krisensicherOS den Skill `isms-risk-analysis` und den Session State `templates/risikoanalyse-session-state.md`.

Der Wizard arbeitet phasenweise:

1. Session starten oder fortsetzen.
2. Risiko als Schwachstelle + Asset + Bedrohung beschreiben.
3. Aktuelle Maßnahmenlage mit Fragebogen erheben.
4. Bruttorisiko bewerten.
5. Strategie als Human Gate vorbereiten.
6. Maßnahmen und Control-/SoA-Mapping planen.
7. Netto-/Restrisiko bewerten.
8. Reporting erzeugen.

Jede Phase erzeugt verwertbare Felder für Risikoanalyse-Register, Risk-Control Map / spätere SoA, Entscheidungslog und Risikoreport.

## Rollen und Verantwortung

| Rolle | Verantwortung im Risikoprozess |
| --- | --- |
| Management / Geschäftsleitung | Risikokriterien freigeben, Ressourcen entscheiden, Risikoakzeptanz und Restrisiken verantworten. |
| ISB / CISO / ISMS-Owner | Prozess steuern, Methodik pflegen, Workshops moderieren, Berichtswesen vorbereiten, Control-/SoA- und Maßnahmenmapping sicherstellen. |
| Asset Owner / Prozess Owner | Risiken melden, bewerten oder fachlich bestätigen, Maßnahmen vorschlagen und Wirksamkeit beurteilen. |
| Control Owner / Maßnahmenowner | Maßnahmen umsetzen, Evidenz erzeugen, Umsetzungsstatus und Wirksamkeit melden. |
| Reviewer / Auditrolle | Nachvollziehbarkeit, Evidenz, offene Entscheidungen und Wirksamkeitsprüfung hinterfragen. |

Agenten können strukturieren, fragen, mappen und Vorschläge vorbereiten. Risikoakzeptanz, Ressourcenentscheidungen und Freigaben bleiben menschliche Entscheidungen.

## Prozessüberblick

Die Risikobewertung erfolgt zweimal: erst als Bruttorisiko nach Beschreibung des Risikos und Darstellung der aktuellen Maßnahmenlage, danach als Netto-/Restrisiko nach Strategieentscheidung und Maßnahmenplanung.

1. **Scope klären:** ISMS-Anwendungsbereich, betrachtete Assets, Nicht-Scope und Bewertungshorizont festlegen.
2. **Risiko identifizieren und beschreiben:** Meldungen, Incidents, Audits, Änderungen, Asset Reviews, Schwachstellen, Anforderungen und Workshops auswerten.
3. **Risikoszenario formulieren:** Schwachstelle, Asset, Bedrohung und Auswirkung in einem prüfbaren Satz erfassen.
4. **Aktuelle Maßnahmenlage erheben:** Bestehende Controls, Routinen, organisatorische Praktiken, technische Schutzmaßnahmen, Krisen-/Notfallfähigkeiten und Evidenzquellen aufnehmen. Dieser Schritt kann durch KI-gestützte Fragebögen vorbereitet werden; fachliche Bestätigung bleibt bei Asset Owner und ISB.
5. **Bruttorisiko bewerten:** Risiko mit den Bewertungskriterien für Eintrittswahrscheinlichkeit und Schadensausmaß bewerten. Das Bruttorisiko beschreibt die inhärente Risikolage des Szenarios und wird trotz Erhebung der aktuellen Maßnahmen so dokumentiert, dass die ursprüngliche Risikoexposition sichtbar bleibt. Aktuelle Maßnahmen werden als Kontext erfasst, aber nicht zur Schönrechnung genutzt.
6. **Strategie wählen:** Akzeptanz, Vermeidung, Transfer oder Minimierung festlegen bzw. als Managemententscheidung vorbereiten. Transfer kann z. B. Versicherung, Outsourcing oder Übergabe bestimmter Bewältigungsanteile ins Krisenmanagement / BCMS bedeuten; Verantwortung und Restrisiko bleiben sichtbar.
7. **Maßnahmen planen:** Maßnahmen aus Schwachstelle, Asset, Bedrohung und gewünschter Wirkung ableiten; Control-/SoA-Bezug, Owner, Fälligkeit, Evidenz und Wirksamkeitsprüfung festlegen.
8. **Netto-/Restrisiko bewerten:** Nach vorhandenen und geplanten bzw. freigegebenen Maßnahmen das erwartete Restrisiko mit denselben Kriterien für Eintrittswahrscheinlichkeit und Schadensausmaß bewerten. Wenn Maßnahmen noch nicht umgesetzt oder nicht wirksamkeitsgeprüft sind, wird das Netto-/Restrisiko als Planwert markiert und später bestätigt oder korrigiert.
9. **Umsetzung und Wirksamkeit prüfen:** Maßnahmenstatus, Evidenz, tatsächliche Risikoänderung und Control-/SoA-Status reviewen.
10. **Berichten und entscheiden:** Top-Risiken, Restrisiken, Akzeptanzen, Transfers, überfällige Maßnahmen und Control-/SoA-Lücken in Reporting und Management Review überführen.

## Brutto-Netto-Logik

krisensicherOS unterscheidet zwei verpflichtende Bewertungen und einen Umsetzungsstatus:

| Bewertungsstand | Zeitpunkt | Bedeutung | Typischer Output |
| --- | --- | --- | --- |
| Bruttorisiko | Nach Risikobeschreibung und Erhebung der aktuellen Maßnahmenlage. | Inhärente Risikoexposition des Szenarios. Vorhandene Maßnahmen werden sichtbar gemacht, senken diesen Wert aber nicht automatisch. | Ausgangsrisiko, aktuelle Maßnahmenlage, Begründung der Relevanz. |
| Netto-/Restrisiko | Nach Strategieentscheidung und Maßnahmenplanung. | Restrisiko nach gewählter Strategie und Maßnahmenwirkung. Bei noch nicht umgesetzten Maßnahmen ist es ein Planwert. | Restrisiko, Strategie, Maßnahmen, Control-/SoA-Bezug, Entscheidungsvorlage. |
| Bestätigtes Nettorisiko | Nach Umsetzung und Wirksamkeitsprüfung. | Tatsächlich bestätigtes Restrisiko nach evidenzierter Maßnahmenwirkung. | Aktualisiertes Register, Wirksamkeitsnachweis, Management-Review-Input. |

Regel: Maßnahmen senken das bestätigte Nettorisiko erst, wenn sie umgesetzt, betrieben und plausibel wirksamkeitsgeprüft sind. Vorher bleibt die Netto-/Restrisikobewertung ein Planwert.

## KI-gestützte Erhebung der aktuellen Maßnahmenlage

KI kann die Risikoanalyse vorbereiten, indem sie aus einem Fragebogen Hinweise auf vorhandene Maßnahmen, fehlende Evidenz, SoA-Bezüge und mögliche Maßnahmenoptionen strukturiert. Sie darf aber keine Risikoakzeptanz treffen und keine Wirksamkeit behaupten.

Mindestfragen an Asset Owner oder Prozess Owner:

- Welches Asset, welcher Prozess oder Service ist betroffen?
- Welche Schwachstelle macht das Risiko möglich?
- Welche Bedrohung kann diese Schwachstelle ausnutzen?
- Welche organisatorischen, technischen oder personellen Maßnahmen gibt es bereits?
- Welche Maßnahmen werden tatsächlich regelmäßig betrieben?
- Welche Evidenz zeigt, dass diese Maßnahmen existieren und funktionieren?
- Welche SoA-/Control-Einträge sind betroffen oder geplant?
- Welche Lücken, Ausnahmen oder Abhängigkeiten sind bekannt?
- Welche Krisenmanagement-, BCMS- oder Incident-Response-Fähigkeiten begrenzen den Schaden?
- Welche Entscheidungen braucht das Management?

Die Antworten werden als Arbeitsgrundlage in das Risikoanalyse-Register und die SoA Risk-Control Map überführt.

## Eintrittswahrscheinlichkeit

Die Eintrittswahrscheinlichkeit bezieht sich vor allem auf die risikoauslösende Schwachstelle. Bewertet werden drei Aspekte. Der Wahrscheinlichkeitsfaktor ist der höchste Wert aus den drei Aspekten, nicht der Durchschnitt.

| Aspekt | Wert 1 sehr gering | Wert 2 gering | Wert 3 mittel | Wert 4 hoch | Wert 5 sehr hoch |
| --- | --- | --- | --- | --- | --- |
| Erkennbarkeit der Schwachstelle | Nur für Experten erkennbar. | Nur für einen Teil der Mitarbeitenden erkennbar. | Für Mitarbeitende erkennbar. | Für Laien erkennbar. | Offensichtlich. |
| Ausnutzbarkeit der Schwachstelle | Ausnutzung erfordert hohen Aufwand, umfangreiche Hilfsmittel und Spezialkenntnisse. | Ausnutzung erfordert hohen Aufwand und fortgeschrittene Hilfsmittel. | Ausnutzung ist mit fortgeschrittenen Hilfsmitteln möglich. | Ausnutzung ist mit einfachen Hilfsmitteln möglich. | Ausnutzung ist ohne Hilfsmittel oder sogar versehentlich möglich. |
| Verborgenheit der Ausnutzung | Ausnutzung wird sofort und vollständig erkannt. | Ausnutzung wird innerhalb eines Tages und vollständig erkannt. | Ausnutzung wird vor Auslieferung, Wirksamwerden oder innerhalb eines Monats vollständig erkannt. | Ausnutzung wird erst durch Dritte oder vor Ablauf eines Quartals erkannt. | Ausnutzung wird nur zufällig, später als nach einem Quartal oder gar nicht erkannt. |

**Bewertungsregel:**

```text
Wahrscheinlichkeitsfaktor = max(Erkennbarkeit, Ausnutzbarkeit, Verborgenheit)
```

Diese Maximalwertlogik verhindert, dass eine sehr kritische Schwachstelleneigenschaft durch andere, weniger kritische Aspekte schöngerechnet wird.

## Schadensausmaß

Das Schadensausmaß beschreibt die mögliche Auswirkung des Risikos. Bewertet werden Sachschäden, Personenschäden, finanzielle Verluste und immaterielle Schäden. Der Schadensfaktor ist der höchste Wert aus den betrachteten Schadenskategorien.

| Wert | Bezeichnung | Sachschäden | Personenschäden | Finanzielle Verluste | Immaterielle Schäden |
| --- | --- | --- | --- | --- | --- |
| 1 | sehr gering | 0 bis 1.000 EUR | Leichte Verletzungen, durch Laien oder Ersthelfer behandelbar. | 0 bis 1.000 EUR | Vorfall wird nur intern zur Kenntnis genommen. |
| 2 | gering | 1.000 bis 10.000 EUR | Leichte Verletzungen mit ambulanter Behandlung; Ausfall nicht länger als drei Werktage. | 1.000 bis 10.000 EUR | Wahrnehmung im organisationsnahen Umfeld; einzelne negative Äußerungen. |
| 3 | mittel | 10.000 bis 100.000 EUR | Schwerere Verletzungen mit ambulanter Behandlung; Ausfall länger als drei Werktage. | 10.000 bis 100.000 EUR | Aktive Wahrnehmung durch Kunden, Lieferanten oder Partner; negative Konsequenzen werden angedroht. |
| 4 | hoch | 100.000 bis 1.000.000 EUR | Schwerere Verletzungen mit stationärer Behandlung. | 100.000 bis 1.000.000 EUR | Verlust einzelner Kunden, Partner oder Mitarbeitender. |
| 5 | sehr hoch | Über 1.000.000 EUR | Schwerste Verletzungen mit intensivmedizinischem Behandlungsbedarf oder schlimmer. | Über 1.000.000 EUR | Umfassende öffentliche Berichterstattung; Verlust mehrerer Kunden, Partner oder Mitarbeitender. |

**Bewertungsregel:**

```text
Schadensfaktor = max(Sachschaden, Personenschaden, finanzieller Verlust, immaterieller Schaden)
```

Organisationen dürfen Schwellenwerte an Größe, Branche und Risikotragfähigkeit anpassen. Die Anpassung muss freigegeben und im Entscheidungslog dokumentiert werden.

## Risikowert und Risikokategorie

```text
Risikowert = Wahrscheinlichkeitsfaktor × Schadensfaktor
```

| Risikowert | Kategorie | Grundlogik |
| --- | --- | --- |
| 1 bis 2 | sehr gering | In der Regel ohne weitere Behandlung akzeptabel, sofern dokumentiert. |
| 3 bis 6 | gering | In der Regel akzeptabel; Maßnahmen möglich, aber nicht zwingend. |
| 7 bis 12 | mittel | Behandlung, begründete Akzeptanz oder Managemententscheidung erforderlich. |
| 13 bis 19 | hoch | Behandlung priorisieren; Managementsichtbarkeit erforderlich. |
| 20 bis 25 | sehr hoch | Unverzüglich eskalieren; Managemententscheidung und Maßnahmenpfad erforderlich. |

Hinweis: Der Wert 20 wird als sehr hoch behandelt, weil er die Kombination aus maximalem Schaden mit hoher Wahrscheinlichkeit oder maximaler Wahrscheinlichkeit mit hohem Schaden abbildet.

## Strategieentscheidung und Behandlungsoptionen

Nach der Bruttobewertung wird eine Strategie gewählt oder als Managemententscheidung vorbereitet. Ab einem Risikowert von 7 muss das Risiko aktiv beurteilt werden. Zulässige Strategien:

| Strategie | Bedeutung | Human Gate |
| --- | --- | --- |
| Minimieren / Behandeln | Maßnahmen reduzieren Eintrittswahrscheinlichkeit, Schadensausmaß oder beide Faktoren. | Maßnahmenfreigabe durch betroffene Owner; Ressourcenentscheidung bei Bedarf. |
| Transfer / Übertragen | Auswirkungen oder Bewältigungsanteile werden auf Dritte übertragen, z. B. Versicherung, Outsourcing oder strukturierte Übergabe bestimmter Schadensbewältigung ins Krisenmanagement / BCMS. | Managementfreigabe und Vertrags-/Datenschutzprüfung, sofern relevant; Restrisiko bleibt sichtbar. |
| Akzeptieren | Restrisiko wird bewusst getragen, weil andere Strategien nicht angemessen sind. | Managemententscheidung; Begründung, Laufzeit und Reviewtermin dokumentieren. |
| Vermeiden | Prozess, Verarbeitung, System, Dienst oder Schritt wird beendet oder verändert. | Owner- und Managemententscheidung; Auswirkungen auf Betrieb prüfen. |

Sehr geringe und geringe Risiken können durch den Asset Owner akzeptiert werden, sofern die Organisation dies so freigegeben hat. Mittel, hoch und sehr hoch bewertete Risiken brauchen eine sichtbare Behandlung oder Managemententscheidung.

## Maßnahmenableitung

Maßnahmen werden nicht aus einer generischen Kontrollliste übernommen, sondern aus dem konkreten Risikoszenario abgeleitet:

1. Welche Schwachstelle soll reduziert oder beseitigt werden?
2. Welche Bedrohung soll verhindert, erschwert, erkannt oder begrenzt werden?
3. Welches Asset oder welcher Prozess soll geschützt werden?
4. Wirkt die Maßnahme auf Eintrittswahrscheinlichkeit, Schadensausmaß oder beides?
5. Welche bestehende oder geplante Maßnahme ist in der Control-Taxonomie oder SoA zu referenzieren?
6. Welche Evidenz zeigt später, dass die Maßnahme umgesetzt und wirksam ist?

Jede Maßnahme braucht mindestens:

- Maßnahmen-ID,
- Risikoreferenz,
- SoA-/Control-Referenz,
- Owner,
- Status,
- Fälligkeit,
- Evidenzquelle,
- Wirksamkeitsprüfpunkt,
- Entscheidungspunkt bei Blockern.

## ISO-27001- und SoA-Grenze

Eine Statement of Applicability (SoA) setzt voraus, dass die Organisation eine eigene, lizenzkonforme ISO/IEC-27001-Grundlage oder eine eigene Control-Taxonomie nutzt. krisensicherOS liefert deshalb keine ISO-27001-Controls, keine Annex-A-Texte und keine vollständige normative SoA.

krisensicherOS liefert nur die **SoA-fähige Arbeitsstruktur**:

- Risiken mit Maßnahmen und Control-Referenzen verbinden,
- vorhandene und geplante Maßnahmen begründen,
- Anwendbarkeit, Nicht-Anwendbarkeit oder Verwerfung dokumentieren,
- Evidenz und Wirksamkeitsprüfung verknüpfen,
- Lücken für Management Review sichtbar machen.

Wenn keine ISO-27001-SoA vorhanden ist, kann dieselbe Struktur zunächst als organisationsspezifische **Risk-Control Map** genutzt werden. Die spätere Überführung in eine SoA erfolgt durch fachlich verantwortliche Personen auf Basis der lizenzierten Norm und organisationsspezifischer Entscheidungen.

## Control-/SoA- und Maßnahmenmapping

Die SoA ist nicht nur eine Normtabelle. In krisensicherOS wird zunächst eine Risk-Control Map gepflegt; wenn eine ISO-27001-SoA organisationsspezifisch erstellt wurde, kann sie daran anschließen. Die Struktur verbindet Risiko, Entscheidung, Maßnahme, Routine und Evidenz.

Für jedes relevante Risiko wird geprüft:

- Welche vorhandenen Maßnahmen reduzieren das Nettorisiko?
- Welche geplanten Maßnahmen sollen das Netto-/Restrisiko als Planwert erreichen?
- Welche Control-Cluster, internen Control-IDs oder SoA-Einträge sind betroffen?
- Welche Maßnahme ist umgesetzt, geplant, verworfen oder nicht anwendbar?
- Welche Evidenz entsteht aus dem Betrieb der Maßnahme?
- Welche Risiken bleiben trotz Maßnahmen als Restrisiko bestehen?

Referenzen auf ISO 27001 oder andere lizenzpflichtige Normen dürfen nur als eigene Metadaten, IDs, Control-Titel oder organisationsspezifische Zusammenfassungen geführt werden. Keine Normtexte in öffentliche Artefakte kopieren.

## Reporting und Berichtsroutine

Reporting muss aus dem Risikoregister ableitbar sein. krisensicherOS unterstützt dafür Markdown-, Tabellen- und HTML-Ausgaben. Ein Report sollte mindestens enthalten:

- Scope, Berichtszeitraum und Bewertungsstand,
- Risikomatrix und verwendete Kriterien,
- Top-Risiken nach Brutto- und Netto-/Restrisiko,
- Strategie je Risiko: Akzeptanz, Vermeidung, Transfer oder Minimierung,
- offene Managemententscheidungen, Risikoakzeptanzen und Transfers,
- Maßnahmenstatus, überfällige Maßnahmen und Wirksamkeitsprüfungen,
- SoA-/Control-Mapping und Lücken,
- Änderungen seit dem letzten Review.

Für Management Reviews eignet sich eine HTML-Darstellung mit farbigen Risiko-Badges, Maßnahmenstatus und Entscheidungsboxen. Siehe `templates/risikoreport-html.html`.

## Review- und Berichtsroutine

| Routine | Mindestinhalt | Frequenz / Trigger |
| --- | --- | --- |
| Risikoworkshop | Neue Risiken, geänderte Risiken, Maßnahmenstatus, Control-/SoA-Lücken, Eskalationen. | Mindestens quartalsweise oder nach wesentlichen Änderungen. |
| Risiko-Review je Eintrag | Aktualität von Asset, Schwachstelle, Bedrohung, Brutto- und Netto-/Restrisikobewertung, Maßnahmen und Evidenz. | Mindestens jährlich oder anlassbezogen. |
| Maßnahmenreview | Überfällige Maßnahmen, Blocker, Evidenz, Wirksamkeit und Restrisiko-Planwert. | Monatlich oder passend zur Governance-Kadenz. |
| Management Review | Top-Risiken, Restrisiken, Akzeptanzen, Ressourcenbedarf, wesentliche SoA-Entscheidungen. | Mindestens jährlich und bei hohen / sehr hohen Risiken anlassbezogen. |

## Mindest-Evidenz

- aktuelles Risikoregister,
- Risk-Control-/SoA-Mapping,
- Maßnahmenliste mit Status und Ownern,
- Entscheidungslog für Risikoakzeptanzen und Kriterienänderungen,
- Review- oder Workshopnotizen,
- Nachweise zur Umsetzung und Wirksamkeit zentraler Maßnahmen,
- Management-Review-Auszug zu Top-Risiken und Restrisiken.

## Grenzen

- Diese Methodik ist ein Arbeitsmodell und keine Rechtsberatung.
- Sie ersetzt keine organisationsspezifische Risikoentscheidung.
- Sie bestätigt keine ISO-, NIS2- oder sonstige Konformität.
- Sie darf keine vertraulichen Kundendaten, personenbezogenen Daten oder lizenzpflichtigen Normtexte in öffentliche Beispiele übernehmen.
