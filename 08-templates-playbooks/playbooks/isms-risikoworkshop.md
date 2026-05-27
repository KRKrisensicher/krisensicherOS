
# Playbook: ISMS-Risikoworkshop

## Zweck

Dieses Playbook führt durch einen kompakten Risikoworkshop, der Risiken identifiziert, nach Brutto-/Netto-Methodik bewertet, Maßnahmen ableitet und Control-/SoA-Mappings vorbereitet.

Der Workshop erzeugt betreibbare Entscheidungen und Evidenz. Er ersetzt kein Risikotool und keine Managemententscheidung.

## Trigger

- quartalsweiser ISMS-Risikoworkshop,
- wesentliche Änderungen an Assets, Prozessen, Dienstleistern oder Bedrohungslage,
- Incident, Auditfinding oder Nichtkonformität,
- Vorbereitung Management Review,
- Control-/SoA-Review oder Maßnahmenpriorisierung.

## Teilnehmer

- ISB / CISO / ISMS-Owner als Moderator,
- betroffene Asset Owner und Prozess Owner,
- Control Owner / Maßnahmenowner,
- bei Bedarf Datenschutz, Recht, Einkauf, IT-Betrieb oder Managementvertretung,
- optional Agentenunterstützung für Strukturierung, Mapping und Protokollentwurf.

## Vorbereitung

SoA optional: Wenn noch keine eigene ISO-27001-SoA vorhanden ist, nutzt der Workshop zunächst eine interne Risk-Control Map. Eine spätere SoA-Erstellung erfolgt separat auf Basis lizenzkonformer ISO-27001-Nutzung.


1. Scope und Nicht-Scope festlegen.
2. Aktuelles Risikoanalyse-Register öffnen.
3. Aktuelle Risk-Control Map / SoA-Erweiterung öffnen.
4. Neue Trigger sammeln: Incidents, Audits, Changes, Schwachstellen, Dienstleisteränderungen, Managementfragen.
5. Offene Maßnahmen und überfällige Reviews markieren.
6. Entscheidungspunkte vorbereiten: Akzeptanz, Ressourcen, Vermeidung, Übertragung, Scope-Fragen.

## Dialogischer Risikowizard

Für Einzelrisiken oder kleine Workshops kann der Risikoprozess als geführter Wizard durchgeführt werden. Der Wizard nutzt den Skill [`isms-risk-analysis`](../../07-ai-governance-agents/skills/isms-risk-analysis/SKILL.md) und hält den Stand in [`templates/risikoanalyse-session-state.md`](../templates/risikoanalyse-session-state.md) fest.

Arbeitsregeln:

- Der Moderator stellt maximal 1-3 Fragen gleichzeitig.
- Jede Antwort wird einem Feld im Session State zugeordnet.
- Fehlende Pflichtfelder werden vor der nächsten Phase geklärt.
- Unklare Aussagen werden als Annahme markiert und später bestätigt oder verworfen.
- Jede Phase endet mit einer kurzen Zusammenfassung: ausgefüllt, offen, Annahmen, Human Gates, nächste Frage.

Phasen:

1. Session starten oder fortsetzen.
2. Risiko als Schwachstelle + Asset + Bedrohung beschreiben.
3. Aktuelle Maßnahmenlage erheben.
4. Bruttorisiko bewerten.
5. Strategie wählen oder als Entscheidung vorbereiten.
6. Maßnahmen und Control-/SoA-Mapping planen.
7. Netto-/Restrisiko bewerten.
8. Reporting erzeugen.

## Ablauf

### 1. Einstieg und Scope bestätigen

- Welche Assets, Prozesse oder Services betrachten wir?
- Was bleibt heute bewusst außerhalb des Scopes?
- Welche Entscheidungen können im Workshop vorbereitet, aber nicht final getroffen werden?

### 2. Risiken formulieren

Für jedes Risiko prüfen:

```text
Risiko = Schwachstelle + Asset + Bedrohung
```

Pflichtsatz:

```text
Wenn [Bedrohung] die Schwachstelle [Schwachstelle] am Asset [Asset] ausnutzt,
dann kann [Auswirkung] entstehen.
```

Unklare Einträge werden als Hypothese markiert und nicht als belastbar bewertet.

### 3. Aktuelle Maßnahmenlage erheben

Vor der Bewertung wird die aktuelle Lage sichtbar gemacht. Das kann per [`templates/risikoanalyse-fragebogen.md`](../templates/risikoanalyse-fragebogen.md) und KI-gestützter Strukturierung vorbereitet werden.

- Welche organisatorischen, technischen und prozessualen Maßnahmen existieren bereits?
- Welche Incident-Response-, Krisenmanagement- oder BCMS-Fähigkeiten begrenzen den Schaden?
- Welche Maßnahmen werden tatsächlich betrieben?
- Welche Evidenz zeigt Umsetzung und Betrieb?
- Welche Control-/SoA-Referenzen gehören dazu?
- Welche Lücken oder ungeprüften Annahmen bleiben?

Die Maßnahmenlage wird fachlich durch Asset Owner oder ISB bestätigt. KI-Ergebnisse bleiben Vorarbeit.

### 4. Bruttorisiko bewerten

- Erkennbarkeit, Ausnutzbarkeit und Verborgenheit bewerten.
- Wahrscheinlichkeitsfaktor als Maximalwert bestimmen.
- Sachschaden, Personenschaden, finanziellen Verlust und immateriellen Schaden bewerten.
- Schadensfaktor als Maximalwert bestimmen.
- Brutto-Risikowert berechnen.

Die aktuelle Maßnahmenlage ist Kontext. Sie darf den Bruttowert nicht automatisch senken.

### 5. Strategie entscheiden oder vorbereiten

Ab Risikowert 7 wird eine Strategie vorbereitet:

- Akzeptanz,
- Vermeidung,
- Transfer, z. B. Versicherung, Outsourcing oder Übergabe bestimmter Bewältigungsanteile ins Krisenmanagement / BCMS,
- Minimierung mit Maßnahmen.

Risikoakzeptanz, Ressourcenfreigaben, Transfer und Vermeidung werden als Human Gates markiert und im Entscheidungslog vorbereitet.

### 6. Maßnahmen ableiten und planen

Für jede Maßnahme festlegen:

- Maßnahmen-ID,
- Risikoreferenz,
- Control-/SoA-Referenz,
- Owner,
- Wirkung auf Eintrittswahrscheinlichkeit, Schadensausmaß oder beides,
- Fälligkeit,
- Evidenzquelle,
- Wirksamkeitsprüfung,
- Netto-/Restrisikowirkung als Planwert,
- späterer Wirksamkeitsprüfpunkt.

### 7. Netto-/Restrisiko bewerten

- Bewertung nach gewählter Strategie und geplanten Maßnahmen durchführen.
- Dieselben Kriterien wie beim Bruttorisiko verwenden.
- Plausibel begründen, welche Faktoren sich warum verändern sollen.
- Markieren, ob die Bewertung Planwert oder bereits bestätigt ist.
- Bestätigtes Nettorisiko erst nach Umsetzung und Wirksamkeitsprüfung ausweisen.

### 8. Reporting und Managementinput erzeugen

Zum Abschluss festhalten:

- Top-Risiken nach Nettorisiko,
- neue oder geänderte Risikoakzeptanzen,
- überfällige Maßnahmen,
- Control-/SoA-Lücken,
- Ressourcen- oder Scope-Entscheidungen,
- nächste Reviews.

## Output

- aktualisiertes Risikoanalyse-Register,
- aktualisierte Risk-Control Map / SoA-Erweiterung,
- Maßnahmenliste oder Backlog-Einträge,
- Entscheidungslog-Einträge,
- Workshopnotiz als Evidenz,
- Management-Review-Input,
- optionaler Risikoreport als Markdown oder HTML.

## Qualitätscheck

- Kein Risiko ohne Asset, Schwachstelle und Bedrohung.
- aktuelle Maßnahmenlage vor der Bruttobewertung dokumentiert.
- Brutto- und Netto-/Restrisiko in der richtigen Reihenfolge dokumentiert.
- bestätigtes Nettorisiko nur nach Umsetzung und Wirksamkeitsprüfung ausgewiesen.
- Maßnahmen haben Owner, Fälligkeit, Evidenz und Wirksamkeitsprüfung.
- Control-/SoA-Bezug ist gepflegt oder als Lücke markiert.
- Menschliche Entscheidungen sind sichtbar und nicht durch Agenten ersetzt.

## Grenzen

Keine Rechtsberatung, keine Datenschutzberatung, keine Zertifizierungszusage, keine Risikoakzeptanz durch Agenten. Echte Organisationsdaten gehören nur in freigegebene interne Arbeitsumgebungen.
