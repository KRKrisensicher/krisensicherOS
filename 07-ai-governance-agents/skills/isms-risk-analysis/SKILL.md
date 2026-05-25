---
name: isms-risk-analysis
version: 1.0.0
description: "Führt durch ISMS-Risikoanalyse: Szenario, Bewertung, Strategie, Maßnahmen, SoA-Bezug und Reporting."
category: governance
inputs:
  - scope
  - asset-or-process
  - vulnerability
  - threat
  - current-measures
  - evidence-sources
outputs:
  - risk-analysis-session-state
  - risk-register-entry
  - soa-risk-control-map-entry
  - measure-backlog
  - decision-log-items
  - risk-report-input
requires_human_review: true
---

<!-- kso:product-relevance
repo-scope: product
classification: agent-skill
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->


# isms-risk-analysis

## Zweck

Dieser Skill führt Nutzer dialogisch durch eine ISMS-Risikoanalyse. Er stellt schrittweise Fragen, bis genug Informationen vorliegen, um Risiko, aktuelle Maßnahmenlage, Bruttorisiko, Strategie, Maßnahmen, Control-/SoA-Bezug, Netto-/Restrisiko und Reporting-Input nachvollziehbar zu dokumentieren.

Er ist kein Risikotool und trifft keine Risikoentscheidung. Er strukturiert Vorarbeit für verantwortliche Menschen.

## Wann verwenden

Nutze den Skill bei:

- neuer oder geänderter Risikoanalyse im ISMS,
- Risikoworkshops,
- Control-/SoA-Review mit Risikobezug,
- Maßnahmenableitung aus Risiken,
- Vorbereitung von Risikoreporting oder Management Review,
- Fortsetzung einer unterbrochenen Risikoanalyse anhand eines Session-State.

## Wann nicht verwenden

Nicht verwenden für:

- Risikoakzeptanz anstelle des Managements,
- Rechts- oder Datenschutzberatung,
- Zertifizierungs-, Konformitäts- oder Sicherheitszusagen,
- automatisierte Wirksamkeitsbestätigung ohne Evidenz,
- Verarbeitung vertraulicher Inhalte in öffentlichen Beispielen,
- Reproduktion lizenzpflichtiger Normtexte.

## Leitprinzipien

- SoA optional: Wenn keine eigene ISO-27001-SoA vorhanden ist, wird zunächst eine Risk-Control Map gepflegt. ISO-27001-Referenzen setzen lizenzkonforme Normnutzung und fachliche Freigabe voraus.

- Ein Risiko ist erst bewertbar, wenn **Schwachstelle + Asset + Bedrohung** getrennt benannt sind.
- Der Skill stellt **nur die nächste sinnvolle Frage**, statt den Nutzer mit allen Fragen auf einmal zu überladen.
- Unklare Antworten werden als **Annahme** oder **offene Frage** markiert.
- KI darf strukturieren und vorschlagen; Owner müssen fachlich bestätigen.
- Risikoakzeptanz, Transfer, Vermeidung und Ressourcen sind Human Gates.
- Bestätigtes Nettorisiko erst nach Umsetzung und Wirksamkeitsprüfung ausweisen.

## Benötigte Artefakte

Primäre Artefakte im Repo:

- `04-isms-basics/risikomanagement-methodik.md`
- `templates/risikoanalyse-fragebogen.md`
- `templates/risikoanalyse-session-state.md`
- `templates/risikoanalyse-register.md`
- `templates/soa-risk-control-map.md`
- `templates/risikoreport.md`
- `templates/risikoreport-html.html`
- `templates/decision-log.md`
- `playbooks/isms-risikoworkshop.md`
- `workflows/isms-risk-to-soa.yaml`

## Dialogischer Ablauf

### Phase 0: Session starten oder fortsetzen

Prüfe, ob bereits ein Session-State existiert.

Wenn ja:
- offene Pflichtfelder identifizieren,
- letzte Human Gates und Annahmen prüfen,
- mit der nächsten offenen Phase fortsetzen.

Wenn nein:
- neuen Session-State nach `templates/risikoanalyse-session-state.md` anlegen oder gedanklich führen.

Output: `risk-analysis-session-state`.

### Phase 1: Scope und Risiko beschreiben

Ziel: Risiko als prüfbares Szenario formulieren.

Pflichtfelder:
- Scope / Bereich,
- Asset / Prozess / Service,
- Asset Owner oder fachlicher Owner,
- Schwachstelle,
- Bedrohung,
- Auswirkung.

Leitfragen:
- Welches Asset, welcher Prozess oder Service ist betroffen?
- Welche konkrete Schwachstelle macht das Risiko möglich?
- Welche Bedrohung kann diese Schwachstelle ausnutzen?
- Was wäre die plausible Auswirkung?

Wenn Nutzer unscharf antworten, nachtrennen:
- „Cloud ist unsicher“ → Welcher Cloud-Dienst? Welche Schwachstelle? Welche Bedrohung?
- „Ransomware“ → Welches Asset? Welche Schwachstelle ermöglicht den Angriff?

Output: Risikoszenario im Format:

```text
Wenn [Bedrohung] die Schwachstelle [Schwachstelle] am Asset [Asset] ausnutzt,
dann kann [Auswirkung] entstehen.
```

### Phase 2: Aktuelle Maßnahmenlage erheben

Ziel: aktuelle Controls, Routinen, Evidenz und Lücken sichtbar machen.

Leitfragen:
- Welche organisatorischen Maßnahmen existieren bereits?
- Welche technischen Maßnahmen existieren bereits?
- Welche prozessualen oder personellen Maßnahmen existieren bereits?
- Welche Incident-Response-, Krisenmanagement- oder BCMS-Fähigkeiten begrenzen den Schaden?
- Welche Maßnahmen werden tatsächlich regelmäßig betrieben?
- Welche Evidenz zeigt Umsetzung und Betrieb?
- Welche Control-/SoA-Referenzen sind betroffen?

Regel:
- Antworten als `bestätigt`, `Annahme`, `offen` oder `evidenzgeprüft` markieren.
- Ohne Owner-Bestätigung keine Wirksamkeit behaupten.

Output: Maßnahmenlagen-Snapshot und Evidenzlücken.

### Phase 3: Bruttorisiko bewerten

Ziel: Bruttorisiko mit denselben Kriterien bewerten, die später für Netto-/Restrisiko genutzt werden.

Bewerte Eintrittswahrscheinlichkeit:
- Erkennbarkeit,
- Ausnutzbarkeit,
- Verborgenheit.

Bewerte Schadensausmaß:
- Sachschaden,
- Personenschaden,
- finanzieller Verlust,
- immaterieller Schaden.

Regeln:
- Wahrscheinlichkeitsfaktor = Maximalwert aus Erkennbarkeit, Ausnutzbarkeit, Verborgenheit.
- Schadensfaktor = Maximalwert aus Sachschaden, Personenschaden, finanziellem Verlust, immateriellem Schaden.
- Risikowert = Wahrscheinlichkeitsfaktor × Schadensfaktor.
- Aktuelle Maßnahmenlage ist Kontext; sie senkt den Bruttowert nicht automatisch.

Output: Bruttowert, Kategorie, Begründung.

### Phase 4: Strategie wählen oder vorbereiten

Ziel: Behandlungsstrategie als Human Gate vorbereiten.

Optionen:
- Akzeptanz,
- Vermeidung,
- Transfer,
- Minimierung mit Maßnahmen.

Transfer kann bedeuten:
- Versicherung,
- Outsourcing,
- vertragliche Regelung,
- Übergabe bestimmter Bewältigungsanteile ins Krisenmanagement oder BCMS.

Leitfragen:
- Welche Strategie ist plausibel und warum?
- Welche Strategie ist ungeeignet und warum?
- Wer muss entscheiden?
- Welche Konsequenz hat Nicht-Handeln?

Output: Strategieoptionen, Empfehlung als Vorarbeit, Human Gate.

### Phase 5: Maßnahmen ableiten und Controls / SoA mappen

Ziel: Maßnahmen aus dem konkreten Risiko ableiten und mit Control-/SoA-Logik verbinden.

Leitfragen:
- Welche Maßnahme reduziert welche Schwachstelle?
- Welche Maßnahme verhindert, erschwert, erkennt oder begrenzt welche Bedrohung?
- Welche Maßnahme senkt Eintrittswahrscheinlichkeit, Schadensausmaß oder beides?
- Welcher Owner setzt sie um?
- Welche Evidenz entsteht?
- Wie wird Wirksamkeit geprüft?
- Welche Control-/SoA-ID oder welcher Control-Cluster ist betroffen?

Output:
- Maßnahmenbacklog,
- Risk-Control Map / SoA-Erweiterung,
- Entscheidungslog-Einträge.

### Phase 6: Netto-/Restrisiko bewerten

Ziel: Restrisiko nach Strategie und Maßnahmenplanung bewerten.

Nutze dieselben Kriterien wie in Phase 3:
- Erkennbarkeit,
- Ausnutzbarkeit,
- Verborgenheit,
- Sachschaden,
- Personenschaden,
- finanzieller Verlust,
- immaterieller Schaden.

Regeln:
- Markiere Netto-/Restrisiko als `Planwert`, wenn Maßnahmen noch nicht umgesetzt oder nicht wirksamkeitsgeprüft sind.
- Markiere als `bestätigt` erst nach Evidenz und Wirksamkeitsprüfung.
- Begründe jede Veränderung gegenüber Brutto.

Output: Netto-/Restrisikowert, Kategorie, Status, Begründung.

### Phase 7: Reporting erzeugen

Ziel: Ergebnisse für Workshop, Management Review oder Steuerungsgremium verdichten.

Reporting-Inhalte:
- Risikoszenario,
- aktuelle Maßnahmenlage,
- Brutto- und Netto-/Restrisiko,
- Strategie,
- Maßnahmenstatus,
- Control-/SoA-Bezug,
- Evidenzlage,
- offene Entscheidungen,
- nächste Reviews.

Output:
- `templates/risikoreport.md` befüllbar machen,
- optional HTML-Darstellung nach `templates/risikoreport-html.html` vorbereiten.

## Gesprächssteuerung

Arbeite mit kurzen, präzisen Fragen. Stelle maximal 1-3 Fragen gleichzeitig.

Wenn ein Pflichtfeld fehlt, frage zuerst danach.

Wenn eine Antwort mehrere Konzepte vermischt, trenne sie sichtbar:

```text
Ich lese daraus:
- Asset: ...
- Schwachstelle: ...
- Bedrohung: ...
Stimmt das so?
```

Wenn genug Informationen für eine Phase vorliegen:
- Phase kurz zusammenfassen,
- offene Annahmen markieren,
- nächste Phase ankündigen.

## Output-Format je Zwischenstand

```text
Stand:
- Phase:
- Ausgefüllt:
- Offen:
- Annahmen:
- Human Gate:
- Nächste Frage:
```

## Verification

Vor Abschluss prüfen:

```text
Verification:
- Risikoformel: pass / notes / stop
- Bewertungsreihenfolge: pass / notes / stop
- Brutto-Kriterien: pass / notes / stop
- Strategie-Human-Gate: pass / notes / stop
- Maßnahmenlogik: pass / notes / stop
- Control-/SoA-Mapping: pass / notes / stop
- Netto-/Restrisikostatus: pass / notes / stop
- Reportingfähigkeit: pass / notes / stop
- Public-Safety: pass / notes / stop
- Claim-Safety: pass / notes / stop
- Ergebnis: pass / pass with notes / stop
```

## Qualitätsgates

Anzuwenden aus `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md`:

- U1 Public-Safe Gate,
- U2 Claim-Safety Gate,
- U3 Betriebslogik-Gate,
- U4 Empowerment-Gate,
- U5 Workload-Gate,
- U6 Portabilitäts-Gate,
- A2 Skill-Gate.

## Handoffs

Typische Handoffs:

- an `control-evidence-architect`, wenn Evidenz- oder Control-Mapping vertieft werden muss,
- an `management-review-facilitator`, wenn Entscheidungen vorbereitet werden müssen,
- an `remediation-effectiveness-review`, wenn Maßnahmenwirksamkeit geprüft werden soll,
- an Datenschutz, Recht oder Einkauf, wenn Transfer, Verträge oder personenbezogene Daten betroffen sind.

## Grenzen

Dieser Skill leistet keine Rechtsberatung, keine Datenschutzberatung, keine Zertifizierungs- oder Konformitätszusage und keine Managemententscheidung.

Er darf keine vertraulichen Inhalte, echten Kundendaten oder lizenzpflichtigen Normtexte in öffentliche Artefakte übernehmen.
