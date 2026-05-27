
# Minimaler NIS2-Start in 5 Artefakten

## Zweck

Dieser Pfad reduziert krisensicherOS auf den kleinsten sinnvollen KI-unterstützten Durchstich.

Er ist für CISO/ISB-Teams, Sicherheitsverantwortliche und GRC-Rollen gedacht, die NIS2 pragmatisch starten müssen, aber keine große Compliance-Maschinerie aufbauen wollen.

## Vorab-Gate: KI-Freigabe

krisensicherOS setzt eine freigegebene KI-Nutzung voraus.

Bevor Inhalte in ein KI-System eingegeben werden:

1. Datenklasse bestimmen: öffentlich, intern, vertraulich, personenbezogen, lizenzpflichtig.
2. Erlaubte KI-Umgebung festlegen: freigegebene Cloud-KI, M365 Copilot, Claude Code, lokale KI oder isolierte Umgebung.
3. Verbotene Inhalte ausschließen: echte Kundendaten, Personendaten, Secrets, Vertragsdetails, lizenzpflichtige Normtexte.
4. Human Gate setzen: KI-Output ist Entwurf, nicht Entscheidung.
5. Freigabe in [`../../templates/ki-nutzungsfreigabe-matrix.md`](../../../08-templates-playbooks/templates/ki-nutzungsfreigabe-matrix.md) oder einer gleichwertigen internen Regel dokumentieren.

Wenn keine KI-Freigabe vorliegt: stoppen. Dann kann nur die Freigabe vorbereitet werden; krisensicherOS wird noch nicht produktiv genutzt.

## Wobei KI helfen darf

KI darf helfen bei:

- Strukturierung,
- Zusammenfassung freigegebener Inhalte,
- Formulierung von Entwürfen,
- Erzeugen von Fragen,
- Vergleich mit eigenen Zusammenfassungen,
- Vorbereitung von Evidenz- und Entscheidungslogik.

KI darf nicht:

- Rechtsberatung leisten,
- Datenschutzbewertung treffen,
- Konformität bestätigen,
- Managemententscheidungen treffen,
- vertrauliche oder lizenzpflichtige Inhalte unkontrolliert verarbeiten.

## Die 5 Artefakte

### 1. Managementauftrag und Entscheidungsfrage

**Datei:** `templates/decision-log.md`

Kläre zuerst:

- Was soll NIS2 in den nächsten 30 Tagen konkret erreichen?
- Welche Managemententscheidung ist nötig?
- Welche Ressourcen, Prioritäten oder Risikoakzeptanzen sind offen?
- Wer ist fachlich verantwortlich?

Minimaler Output:

```text
Entscheidungsfrage: Welche drei NIS2-Handlungsfelder priorisieren wir im ersten Durchstich?
Owner: Geschäftsführung / CISO-ISB / Fachbereich
Benötigte Evidenz: Registereintrag, Gap-Worksheet, erste Evidence Requests
Frist: <Datum>
Human Gate: Managemententscheidung
```

### 2. Compliance-Register-Eintrag

**Datei:** `templates/compliance-source-register.md`

Erfasse eine Quelle oder Anforderung als Referenz und eigene Zusammenfassung.

Nicht tun:

- keine Normtexte kopieren,
- keine rechtliche Auslegung behaupten,
- keine vertraulichen Vertragsinhalte in öffentliche Artefakte übernehmen.

Minimaler Output:

```text
Quelle / Referenz: <öffentliche Quelle oder interner Registerverweis>
Eigene Zusammenfassung: <kurze Arbeitszusammenfassung>
Betroffener Bereich: <Prozess / Control / Rolle>
Owner-Frage: Wer verantwortet die Routine?
```

### 3. NIS2-Gap-Worksheet

**Datei:** `templates/nis2-gap-worksheet.md`

Übersetze die Quelle in einen ersten Gap.

Minimaler Output:

```text
Soll-Zustand: <eigene Zusammenfassung>
Ist-Zustand: <bekannter Stand>
Gap: <fehlende Rolle, Routine, Evidenz oder Entscheidung>
Auswirkung: <operative Relevanz>
Nächster Schritt: <Evidence Request oder Managementfrage>
```

### 4. Evidenzanfrage

**Datei:** `templates/evidence-request-list.md`

Fordere nur Evidenz an, die für die nächste Entscheidung wirklich gebraucht wird.

Regel für den ersten Durchstich:

- maximal drei Requests pro Owner,
- vorhandene Evidenz zuerst,
- keine neuen Dokumente verlangen, wenn bestehende Nachweise genügen,
- Aufwand schätzen,
- Vertraulichkeit prüfen.

Minimaler Output:

```text
Benötigte Evidenz: <konkreter Nachweis>
Zweck: <welche Frage beantwortet die Evidenz?>
Owner: <Rolle>
Aufwand: niedrig / mittel / hoch
Reuse: vorhandene Evidenz nutzbar? ja/nein/offen
```

### 5. Entscheidungslog und Management-Review-Handoff

**Datei:** `templates/decision-log.md`

Führe die Ergebnisse in eine Entscheidungsvorlage zurück.

Minimaler Output:

```text
Entscheidungspunkt: <Priorisierung / Ressourcen / Risikoakzeptanz>
Optionen: <Option A/B/C>
Evidenzlage: <was liegt vor, was fehlt?>
Empfehlung zur Entscheidungsvorbereitung: <keine Entscheidung durch KI>
Owner: <Managementrolle>
```

## 60-Minuten-Ablauf

1. 10 Minuten: KI-Freigabe prüfen.
2. 10 Minuten: Managementfrage formulieren.
3. 15 Minuten: eine Quelle / Anforderung registrieren.
4. 15 Minuten: einen Gap erfassen.
5. 10 Minuten: maximal drei Evidence Requests und einen Decision-Log-Eintrag erstellen.

## Was bewusst nicht passiert

Im Minimalstart werden nicht:

- alle NIS2-Themen vollständig bewertet,
- alle Policies geschrieben,
- alle Controls getestet,
- alle Fachbereiche befragt,
- Konformität behauptet,
- Datenschutz- oder Rechtsfragen entschieden.

## Definition of Done

Der Minimalstart ist abgeschlossen, wenn:

- die KI-Nutzung für die verwendeten Daten und Tools freigegeben ist,
- eine Managementfrage dokumentiert ist,
- eine Quelle oder Anforderung erfasst ist,
- ein Gap sichtbar ist,
- maximal drei konkrete Evidence Requests vorliegen,
- ein Decision-Log- oder Management-Review-Handoff existiert,
- Human Gates markiert sind.

## Nächster Schritt

Wenn der Minimalstart tragfähig ist, weiter mit:

- `docs/getting-started/30-60-90-minuten-nutzungspfad.md`,
- `workflows/audit-evidence-remediation-chain.yaml`,
- `templates/legal-datenschutz-handoff.md`, sobald rechtliche oder Datenschutzfragen auftauchen.
