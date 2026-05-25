<!-- kso:product-relevance
repo-scope: product
classification: template
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->

# KI-Nutzungsfreigabe-Matrix

## Zweck

Diese Vorlage klärt vor der Nutzung von KI-Systemen, welche Daten mit welcher KI-Umgebung verarbeitet werden dürfen und welche Schutzmaßnahmen nötig sind.

Sie ersetzt keine Datenschutzbewertung, keine Rechtsprüfung und keine organisationsinterne KI-Freigabe. Sie schafft ein Arbeitsartefakt für Human Review.

## Trigger

- ein Dokument, Interview, Evidence Pack oder Registereintrag soll mit KI verarbeitet werden,
- eine neue KI-Umgebung soll für krisensicherOS genutzt werden,
- Cloud-KI, M365 Copilot, lokale KI oder Redaction-Tools sollen eingesetzt werden.

## Rollen

- CISO/ISB oder GRC-Verantwortliche,
- Datenschutz / Legal für Reviewfragen,
- IT-/KI-Systemowner,
- Fachbereichsowner,
- Management bei Risiko- oder Freigabeentscheidung.

## Freigabetabelle

| Feld | Einstufung / Entscheidung | Owner | Human Gate |
| --- | --- | --- | --- |
| Arbeitszweck |  |  |  |
| Datenklasse | öffentlich / intern / vertraulich / personenbezogen / lizenzpflichtig |  |  |
| Enthält personenbezogene Daten? | nein / ja / unklar |  | Datenschutz-Handoff falls ja/unklar |
| Enthält Secrets oder Zugangsdaten? | nein / ja / unklar |  | Stop bis bereinigt |
| Enthält lizenzpflichtige Normtexte? | nein / ja / unklar |  | Stop bis geklärt |
| Erlaubte KI-Umgebung | freigegebene Cloud-KI / M365 Copilot / lokale KI / isolierte Umgebung / nicht freigegeben |  | Stop, wenn nicht freigegeben |
| Redaction/Maskierung erforderlich? | nein / ja / unklar |  |  |
| Optionales Redaction-Werkzeug | z. B. OpenAI Privacy Filter / anderes / nicht genutzt |  |  |
| Redaction geprüft? | nicht nötig / geprüft / offen |  | Human Review bei sensiblen Daten |
| Speicherort für Input/Output |  |  |  |
| Logging / Nachvollziehbarkeit |  |  |  |
| Freigabe für diesen Use Case | freigegeben / eingeschränkt / nicht freigegeben |  |  |


## Lokale KI: Betriebscheckliste verlinken

Wenn `lokale KI` oder ein lokales Redaction-Tool gewählt wird, muss zusätzlich `docs/setup/lokale-ki.md` geprüft werden. Dort werden Modell-/Checkpoint-Freigabe, Windows-Pilot, Speicherorte, Logging, Netzwerkbindung, Teamnutzung, Evaluation und Offboarding geklärt. Die zusammenfassende Übersicht liegt ergänzend in `docs/setup/ki-setups-bedienungsanleitung.md`.

## Redaction-Hinweis

PII-/Secret-Redaction-Werkzeuge wie OpenAI Privacy Filter können als zusätzliche Schutzschicht genutzt werden. Sie sind keine Anonymisierungsgarantie, keine Datenschutzbewertung und kein Compliance-Nachweis.

Vor produktiver Nutzung prüfen:

- Welche Kategorien werden erkannt?
- Welche lokalen Datenformate können übersehen werden?
- Wie werden False Positives und False Negatives geprüft?
- Wer entscheidet über Freigabe nach Redaction?
- Werden Eingaben, Ausgaben oder Logs gespeichert?

## Wenn keine KI-Freigabe vorliegt

Wenn keine KI-Freigabe vorliegt, wird krisensicherOS nicht produktiv genutzt. Diese Matrix dient dann nur dazu, die Freigabeentscheidung vorzubereiten:

- Use Case beschreiben,
- Datenklassen klären,
- erlaubte KI-Umgebung festlegen,
- verbotene Inhalte und Human Gates definieren,
- KI-Nutzung später erneut bewerten.

## Qualitätsgates

- Datenklasse ist bekannt oder als offen markiert.
- Verbotene Inhalte sind ausgeschlossen oder führen zu Stop.
- Erlaubte KI-Umgebung ist dokumentiert.
- Redaction wird nicht mit Anonymisierung verwechselt.
- Human Gates sind sichtbar.
- Output enthält keine Rechts-, Datenschutz-, Konformitäts- oder Zertifizierungszusage.
