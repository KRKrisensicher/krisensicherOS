
# Risikoanalyse-Fragebogen

## Zweck

Dieser Fragebogen unterstützt die Erhebung der aktuellen Maßnahmenlage vor der Bruttobewertung und bereitet die spätere Strategie-, Maßnahmen- und Netto-/Restrisikobewertung vor.

Er kann durch KI ausgewertet werden, damit Antworten strukturiert in das Risikoanalyse-Register und die Risk-Control Map / SoA-Erweiterung überführt werden. Die fachliche Bestätigung bleibt bei Asset Owner, ISB/CISO und ggf. Management.

## Nutzung mit KI

SoA optional: Fragen zu Control-/SoA-Bezügen können zunächst auf eine interne Control-Taxonomie zielen. ISO-27001-SoA-Bezüge dürfen nur auf Basis einer eigenen lizenzierten Normgrundlage finalisiert werden.


KI darf:

- Antworten clustern,
- fehlende Informationen markieren,
- Schwachstelle, Asset und Bedrohung in ein Risikoszenario überführen,
- Hinweise auf bestehende Maßnahmen und Evidenzquellen strukturieren,
- mögliche Control-/SoA-Bezüge als Hypothesen markieren,
- Maßnahmenoptionen vorschlagen.

KI darf nicht:

- Risikoakzeptanz entscheiden,
- Wirksamkeit ohne Evidenz behaupten,
- Rechts- oder Datenschutzbewertungen ersetzen,
- vertrauliche Inhalte in öffentliche Artefakte übernehmen.

## Fragebogen

### 1. Risiko- und Scopebeschreibung

| Frage | Antwort |
| --- | --- |
| Welcher Prozess, Service, Standort, Dienstleister oder welches System ist betroffen? |  |
| Welches Asset oder welcher Informationswert ist betroffen? |  |
| Wer ist Asset Owner oder fachlicher Owner? |  |
| Welche Schwachstelle, Lücke oder unsichere Eigenschaft macht das Risiko möglich? |  |
| Welche Bedrohung kann diese Schwachstelle ausnutzen? |  |
| Welche Auswirkung wäre realistisch? |  |
| Welche Annahmen sind noch unklar? |  |

### 2. Aktuelle Maßnahmenlage

| Frage | Antwort |
| --- | --- |
| Welche organisatorischen Maßnahmen existieren bereits? |  |
| Welche technischen Maßnahmen existieren bereits? |  |
| Welche personellen oder prozessualen Maßnahmen existieren bereits? |  |
| Welche Detektions-, Monitoring- oder Reviewmechanismen existieren? |  |
| Welche Incident-Response-, Krisenmanagement- oder BCMS-Fähigkeiten begrenzen den Schaden? |  |
| Welche Maßnahmen werden regelmäßig betrieben und nicht nur dokumentiert? |  |
| Welche Maßnahmen sind informell, ungeprüft oder abhängig von Einzelpersonen? |  |

### 3. Evidenz und Control-/SoA-Bezug

| Frage | Antwort |
| --- | --- |
| Welche Nachweise zeigen, dass die aktuellen Maßnahmen existieren? |  |
| Welche Nachweise zeigen, dass die Maßnahmen wirksam betrieben werden? |  |
| Welche Control-/SoA-IDs oder Control-Cluster sind betroffen? |  |
| Welche Control-/SoA-Einträge fehlen, sind geplant oder unklar? |  |
| Welche Evidenzlücken bestehen? |  |

### 4. Bruttobewertung vorbereiten

| Frage | Antwort |
| --- | --- |
| Wie erkennbar ist die Schwachstelle ohne Schönrechnung durch Maßnahmen? Wert 1-5 mit Begründung. |  |
| Wie ausnutzbar ist die Schwachstelle ohne Schönrechnung durch Maßnahmen? Wert 1-5 mit Begründung. |  |
| Wie verborgen wäre eine Ausnutzung ohne Schönrechnung durch Maßnahmen? Wert 1-5 mit Begründung. |  |
| Welcher Sachschaden wäre plausibel? Wert 1-5 mit Begründung. |  |
| Welcher Personenschaden wäre plausibel? Wert 1-5 mit Begründung. |  |
| Welcher finanzielle Verlust wäre plausibel? Wert 1-5 mit Begründung. |  |
| Welcher immaterielle Schaden wäre plausibel? Wert 1-5 mit Begründung. |  |

### 5. Strategieoptionen

| Frage | Antwort |
| --- | --- |
| Kann das Risiko akzeptiert werden? Wenn ja, warum und durch wen? |  |
| Kann das Risiko vermieden werden, z. B. durch Abschalten, Prozessänderung oder Scope-Änderung? |  |
| Kann das Risiko transferiert werden, z. B. Versicherung, Outsourcing, Krisenmanagement oder BCMS? |  |
| Kann das Risiko durch Maßnahmen minimiert werden? |  |
| Welche Entscheidung braucht Management, ISB, Asset Owner oder ein anderes Gremium? |  |

### 6. Maßnahmenplanung und Restrisiko

| Frage | Antwort |
| --- | --- |
| Welche Maßnahme reduziert welche Schwachstelle? |  |
| Welche Maßnahme verhindert, erschwert, erkennt oder begrenzt welche Bedrohung? |  |
| Welche Maßnahme senkt Eintrittswahrscheinlichkeit, Schadensausmaß oder beides? |  |
| Wer ist Maßnahmenowner? |  |
| Bis wann soll die Maßnahme umgesetzt werden? |  |
| Welche Evidenz entsteht aus Umsetzung und Betrieb? |  |
| Wie wird Wirksamkeit geprüft? |  |
| Welche Netto-/Restrisikobewertung ist nach Maßnahmenplanung plausibel? |  |
| Ist diese Bewertung Planwert oder bereits bestätigt? |  |

## KI-Ausgabeformat

```text
1. Risikoszenario:
2. Aktuelle Maßnahmenlage:
3. Evidenzlage und Lücken:
4. Bruttobewertungsvorschlag mit Begründung:
5. Strategieoptionen:
6. Maßnahmenvorschläge mit Control-/SoA-Bezug:
7. Netto-/Restrisikobewertungsvorschlag:
8. Human Gates / offene Entscheidungen:
9. Reporting-Hinweise:
```

## Output

- strukturierte Vorarbeit für das Risikoanalyse-Register,
- offene Fragen an Owner,
- Maßnahmen- und Control-/SoA-Mapping-Hypothesen,
- Entscheidungsbedarf für Management Review.
