# Reviewmethodik für Anhang-A-Routinen

## Zweck

Diese Methodik beschreibt, wie die 93 Anhang-A-orientierten Routinen fachlich verbessert und geprüft werden. Sie verhindert, dass aus den Artefakten eine schnelle Template-Masse wird.

## Reviewprinzipien

1. **Betriebslogik vor Textmenge:** Eine kurze, klare Routine ist besser als ein langer Absatz ohne Owner, Trigger und Evidenz.
2. **Risiko vor Checkliste:** Controls werden aus Risiken, Abhängigkeiten und Entscheidungsbedarf erklärt.
3. **Evidenz vor Behauptung:** Jede Anleitung muss zeigen, welche Nachweise im Betrieb entstehen.
4. **Human Gates sichtbar:** Recht, Datenschutz, Risikoakzeptanz, Managemententscheidung und externe Kommunikation bleiben menschlich verantwortet.
5. **Normtext-sicher:** Keine ISO-27002-Formulierungen übernehmen, eng paraphrasieren oder als Ersatztext liefern.
6. **Mittelstandstauglich:** Minimalstart muss ohne großes GRC-Tool funktionieren.
7. **Skalierbar:** Fortgeschrittene Praxis darf Tooling, Automatisierung und Kennzahlen nutzen, aber nicht voraussetzen.

## Arbeitsablauf je Control

### Schritt 1: Control-Profil erstellen

Für jede Kontrolle wird zuerst ein Profil erfasst:

```text
Control-ID:
Arbeitstitel:
Control-Familie:
Hauptzweck:
Primäre Risiken:
Betroffene Rollen:
Typische Trigger:
Mögliche Evidenz:
NIS2-/BSIG-Anschluss:
Kritische Handoffs:
Typische Fehlmuster:
```

### Schritt 2: Betriebsroutine schreiben

Die Routine wird entlang realer Arbeit formuliert:

- Wer merkt, dass etwas zu tun ist?
- Wer prüft den Sachverhalt?
- Wer entscheidet Scope, Ausnahme oder Restrisiko?
- Wer setzt um?
- Wo entsteht Evidenz?
- Wann wird reviewed?
- Was passiert bei Abweichung?

### Schritt 3: Evidenzdesign prüfen

Für jedes Artefakt wird geprüft:

- Ist Evidenz aus natürlicher Arbeit ableitbar?
- Gibt es mindestens einen Nachweis für Durchführung?
- Gibt es mindestens einen Nachweis für Review oder Entscheidung?
- Gibt es eine klare Ablage- oder Registerlogik?
- Sind Ausnahmen nachvollziehbar?

### Schritt 4: Handoffs schärfen

Handoffs werden nicht generisch belassen. Sie müssen benennen, wann und warum übergeben wird.

Beispiel:

```text
Legal-/Datenschutz-Handoff auslösen, wenn personenbezogene Daten in Logs, Zugriffsauswertungen oder Monitoring-Auswertungen verarbeitet werden.
```

Besser als:

```text
Bei Bedarf Datenschutz einbeziehen.
```

### Schritt 5: Mini-Beispiel ergänzen

Jedes Artefakt erhält ein fiktives, public-safe Mini-Beispiel. Das Beispiel muss zeigen:

- Ausgangslage,
- Trigger,
- minimale Umsetzung,
- Evidenz,
- offene Entscheidung oder Reviewpunkt.

### Schritt 6: Review-Gate getrennt dokumentieren

Das Review-Gate wird ausschließlich in der internen Trackingdatei geführt. Produktartefakte enthalten keine internen Status-, Reviewstatus-, Agenten- oder Batch-Hinweise.

Für die Reviewsteuerung werden intern festgehalten:

- fachlich ausgearbeitet: ja/nein,
- gegen Qualitätsstandard geprüft: ja/nein,
- Normtext-Safety geprüft: ja/nein,
- Claim-Safety geprüft: ja/nein,
- Human-Review erforderlich: ja.

## Rollen im Review

- **Autor:** erstellt oder überarbeitet die Routine.
- **Control-Evidence-Reviewer:** prüft Evidenzfähigkeit und Reviewlogik.
- **CISO/ISB-Persona:** prüft Verständlichkeit, Workload und praktischen Nutzen.
- **Quality/Safety-Reviewer:** prüft Public-Safety, Claim-Safety und Normtext-Safety.
- **Human Reviewer:** entscheidet, ob das Artefakt produktreif ist.

## Definition der Qualitätsstufen

### Draft Scaffold

Struktur vorhanden, aber noch nicht fachlich tief geprüft.

### Ausgearbeitet

Routine enthält Risiken, Trigger, Rollen, Reifegrade, Evidenz, Handoffs und typische Fehler.

### Reviewfähig

Artefakt ist gegen Qualitätsstandard geprüft und kann von Rico / menschlichem Reviewer fachlich gelesen werden.

### Produktreif

Artefakt wurde menschlich freigegeben, bleibt claim-safe und enthält keine Normtextnähe.

## Stichprobenlogik

Nach jeder Bearbeitungswelle werden mindestens geprüft:

- ein leicht verständliches Control,
- ein rechtlich/datenschutzsensibles Control,
- ein technisches Control,
- ein lieferanten- oder abhaengigkeitsbezogenes Control,
- ein Control mit hoher Scheinkontroll-Gefahr.

## Abbruchkriterien

Bearbeitung stoppen, wenn:

- Normtextnähe entsteht,
- Rechts- oder Datenschutzbewertung behauptet wird,
- echte Organisationsdaten auftauchen,
- eine Kontrolle als Zertifizierungsgarantie wirkt,
- Evidenz nur Papier ohne Betrieb ist,
- der Workload für einen Minimalstart unrealistisch wird.
