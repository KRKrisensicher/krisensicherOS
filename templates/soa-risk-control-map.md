<!-- kso:product-relevance
repo-scope: product
classification: template
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->

# Risk-Control Map / SoA-Erweiterung

## Zweck

Diese Vorlage verbindet Risiken, vorhandene und geplante Maßnahmen, Control-Referenzen, Evidenz und Entscheidungen. Sie hilft, Risikoanalysen nicht als isolierte Liste zu betreiben, sondern mit dem Maßnahmen- und Kontrollsystem des ISMS zu verknüpfen.

Wenn eine Organisation eine ISO-27001-Statement-of-Applicability (SoA) erstellt, kann diese Vorlage als SoA-Erweiterung genutzt werden. krisensicherOS liefert jedoch keine ISO-27001-Controls und keine Normtexte. Für eine ISO-27001-SoA braucht die Organisation eine eigene lizenzkonforme Normgrundlage und fachliche Freigabe.

## Trigger

Nutzen, wenn:

- ein Risiko bewertet oder neu bewertet wurde,
- Maßnahmen aus einem Risiko abgeleitet werden,
- eine interne Control-Taxonomie oder eine spätere SoA gepflegt, aktualisiert oder für ein Review vorbereitet wird,
- vorhandene Maßnahmen belegt oder geplante Maßnahmen priorisiert werden sollen.

## Nutzer

- ISB / CISO / ISMS-Owner,
- Risk Owner / Asset Owner,
- Control Owner,
- Management Review-Facilitator,
- interne Audit- oder Reviewrolle.

## Arbeitslogik

1. Risiko aus dem Risikoanalyse-Register referenzieren.
2. Vorhandene Maßnahmen identifizieren, die das bestätigte Nettorisiko tatsächlich reduzieren.
3. Geplante Maßnahmen identifizieren, die das Netto-/Restrisiko als Planwert erreichen sollen.
4. Control-/SoA-Referenzen mit Status und Begründung pflegen.
5. Evidenzquelle und Wirksamkeitsprüfung festlegen.
6. Offene Entscheidungen in das Entscheidungslog überführen.

## Mappingfelder

| Feld | Eintrag |
| --- | --- |
| Mapping-ID | M-001 |
| Risiko-ID | R-001 |
| Risikoszenario Kurzfassung |  |
| Asset / Prozess / Service |  |
| Schwachstelle |  |
| Bedrohung |  |
| Netto-Risikowert / Kategorie |  |
| Netto-/Restrisiko | Planwert / bestätigt |
| Control-/SoA-ID | organisationsspezifische ID, Control-Cluster oder SoA-Referenz |
| Control-/SoA-Status | umgesetzt / geplant / teilweise umgesetzt / nicht anwendbar / verworfen |
| Begründung der Control-/SoA-Entscheidung | Warum ist die Maßnahme relevant, geplant, nicht anwendbar oder verworfen? |
| Maßnahme / Control-Routine |  |
| Wirkung auf Risiko | Eintrittswahrscheinlichkeit / Schadensausmaß / beides / keine direkte Wirkung |
| Wirkungserwartung | Welche Bewertung soll sich verändern und warum? |
| vorhandene oder geplante Maßnahme | vorhanden / geplant |
| Maßnahmen-ID / Ticket / Backlog-Link |  |
| Maßnahmenowner |  |
| Evidenzquelle | Protokoll, Ticket, Konfiguration, Reviewnotiz, Testnachweis, Schulungsnachweis usw. |
| Evidenzqualität | vollständig / teilweise / fehlt / nicht geprüft |
| Wirksamkeitsprüfung | Methode, Zeitpunkt, Reviewer |
| Entscheidung nötig | Risikoakzeptanz / Ressourcen / Scope / Ausnahme / keine |
| Entscheidungslog-Referenz |  |
| Review-Kadenz | monatlich / quartalsweise / jährlich / anlassbezogen |
| Nächster Review |  |

## Control-/SoA-Entscheidungslogik

| Status | Verwendung | Mindestbegründung |
| --- | --- | --- |
| umgesetzt | Maßnahme ist vorhanden, betrieben und evidenzierbar. | Welche Routine erzeugt welche Evidenz? |
| geplant | Maßnahme ist entschieden oder vorgeschlagen, aber noch nicht wirksam. | Welches Risiko soll reduziert werden, wer entscheidet Ressourcen, bis wann? |
| teilweise umgesetzt | Maßnahme existiert, deckt aber Scope, Evidenz oder Wirkung nur teilweise ab. | Welche Lücke bleibt, welches Restrisiko entsteht? |
| nicht anwendbar | Control passt nicht zum Scope, Asset oder Risikoszenario. | Warum nicht anwendbar, wer hat das geprüft? |
| verworfen | Maßnahme wurde bewusst nicht verfolgt. | Warum verworfen, welche Risikoakzeptanz oder Alternative existiert? |

## Ableitung von Maßnahmen

Eine Maßnahme ist gut formuliert, wenn sie alle Fragen beantwortet:

- Welche Schwachstelle wird reduziert?
- Welche Bedrohung wird verhindert, erschwert, erkannt oder begrenzt?
- Welches Asset oder welcher Prozess ist betroffen?
- Senkt die Maßnahme Eintrittswahrscheinlichkeit, Schadensausmaß oder beides?
- Welche Evidenz zeigt Umsetzung?
- Welche Prüfung zeigt Wirksamkeit?
- Welche Control-/SoA-Referenz wird dadurch gepflegt?

## Output

- nachvollziehbare Verbindung von Risiko, Maßnahme, Control-/SoA-Referenz und Evidenz,
- Liste geplanter Maßnahmen mit Ownern und Entscheidungspunkten,
- sichtbare Control-/SoA-Lücken und nicht belegte Kontrollen,
- Input für Management Review und Maßnahmenpriorisierung.

## Grenzen

Diese Vorlage ersetzt keine Normauslegung, keine Zertifizierungsberatung und keine Risikoakzeptanz. Lizenzpflichtige Normtexte werden nicht übernommen. ISO-27001-Referenzen bleiben IDs, eigene Kurzbeschreibungen oder organisationsspezifische Mappings auf Basis der lizenzierten Norm.
