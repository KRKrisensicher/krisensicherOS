<!-- kso:product-relevance
repo-scope: product
classification: product-standard
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; product-safety; release-readiness
-->

# Skill Standard v1.0

Stand: 2026-05-23

Dieser Standard gilt für alle krisensicherOS-Skills unter `07-ai-governance-agents/skills/<skill-name>/SKILL.md`.

## Zweck

Skills sind wiederholbare Arbeitsabläufe. Sie sind keine Wissensablagen, keine reinen Prompt-Sammlungen und keine Ersatzverantwortlichen.

Ein Skill soll Nutzerorganisationen befähigen, eine konkrete Governance-Aufgabe wiederholbar auszuführen: mit Inputs, Ablauf, Outputs, Evidenz, Grenzen und Verification.

## Pfad- und Namensregel

Jeder Skill liegt in einem eigenen Ordner:

```text
07-ai-governance-agents/skills/<skill-name>/SKILL.md
```

Der Skill-Name ist:

- klein geschrieben,
- kebab-case,
- fachlich konkret,
- nicht tool- oder provider-spezifisch.

## Pflichtstruktur für `SKILL.md`

Jeder Skill enthält diese Abschnitte:

1. YAML-Frontmatter
2. Zweck
3. Wann verwenden
4. Wann nicht verwenden
5. Eingangsdaten
6. Voraussetzungen
7. Ablauf
8. Output-Artefakte
9. Human-in-the-loop
10. Verification
11. Qualitätsgates
12. Handoffs
13. Grenzen und rote Linien
14. Beispiel
15. Definition of Done

## Frontmatter

```yaml
---
name: skill-name
version: 1.0.0
description: Kurzbeschreibung des wiederholbaren Arbeitsablaufs.
category: governance|nis2|isms|bcms|evidence|incident|management|quality
inputs:
  - input-name
outputs:
  - output-name
requires_human_review: true
---
```

## Abschnittsanforderungen

### Zweck

Beschreibt die konkrete Arbeitsaufgabe und den Nutzen.

Nicht ausreichend: „Hilft bei Compliance“.  
Gut: „Übersetzt Anforderungen in Rollen, Routinen, Entscheidungen und Evidenzflüsse.“

### Wann verwenden

Konkrete Trigger, bei denen der Skill sinnvoll ist.

### Wann nicht verwenden

Grenzen, rote Linien und Fälle, in denen andere Skills oder menschliche Prüfung nötig sind.

### Eingangsdaten

Liste der benötigten Inputs. Jeder Input soll sagen, ob er Pflicht, optional oder Annahme ist.

### Voraussetzungen

Benötigte Artefakte, Register, Rollen oder Entscheidungen.

### Ablauf

Schrittfolge mit operativer Logik. Jeder Schritt soll klar machen:

- was geprüft wird,
- welches Artefakt genutzt wird,
- welcher Output entsteht,
- wann gestoppt oder eskaliert wird.

### Output-Artefakte

Konkrete Zielartefakte, z. B.:

- Canvas,
- Worksheet,
- Review-Notiz,
- Registereintrag,
- Evidence Pack,
- Management Decision Brief,
- Maßnahmen-Backlog.

### Human-in-the-loop

Explizit benennen:

- wer prüfen muss,
- wer entscheiden muss,
- wann Freigabe erforderlich ist,
- welche Fragen nicht vom Skill beantwortet werden dürfen.

### Verification

Mindestens:

- Vollständigkeitscheck,
- Claim-Safety-Check,
- Public-Safety-Check,
- Betriebslogik-Check,
- Handoff-Check.

### Qualitätsgates

Verweis auf `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md` und relevante artefaktspezifische Gates.

### Handoffs

Welche Agenten, Skills oder menschlichen Rollen übernehmen danach?

### Grenzen und rote Linien

Immer enthalten:

- keine Rechtsberatung,
- keine Datenschutzberatung,
- keine Zertifizierungs- oder Konformitätsgarantie,
- keine Managemententscheidung,
- keine vertraulichen oder lizenzpflichtigen Inhalte reproduzieren,
- keine echten Kundendaten in öffentliche Beispiele.

### Beispiel

Ein kleines fiktives Beispiel mit sicherem, begrenztem Output.

### Definition of Done

Konkrete Kriterien, wann der Skill sauber abgeschlossen ist.

## Skill vs. Agent vs. Template vs. Workflow

- **Agent**: Rolle, Stimme, Mandat, Zuständigkeit, Grenzen.
- **Skill**: wiederholbarer Arbeitsablauf.
- **Template**: ausfüllbares Artefakt.
- **Workflow**: orchestriert Agenten, Skills, Templates, Register und Freigaben.

Ein Skill darf Agenten oder Templates nutzen, ersetzt sie aber nicht.

## Verification-Block Vorlage

```text
Verification:
- Public-Safety: pass / notes / stop
- Claim-Safety: pass / notes / stop
- Betriebslogik: pass / notes / stop
- Human Review: pass / notes / stop
- Handoffs: pass / notes / stop
- Ergebnis: pass / pass with notes / stop
```

## Minimalbeispiel Skeleton

```markdown
---
name: example-skill
version: 1.0.0
description: Wiederholbarer Arbeitsablauf für ...
category: governance
inputs:
  - scope
  - existing-evidence
outputs:
  - decision-brief
requires_human_review: true
---

# example-skill

## Zweck

...

## Wann verwenden

...

## Wann nicht verwenden

...

## Eingangsdaten

...

## Voraussetzungen

...

## Ablauf

1. ...

## Output-Artefakte

...

## Human-in-the-loop

...

## Verification

...

## Qualitätsgates

...

## Handoffs

...

## Grenzen und rote Linien

...

## Beispiel

...

## Definition of Done

...
```

## Review-Gate für neue Skills

Ein neuer Skill darf erst als fertig gelten, wenn:

- `SKILL.md` existiert,
- Pflichtstruktur vollständig ist,
- Inputs/Outputs konkret sind,
- Verification ausführbar ist,
- relevante Qualitätsgates referenziert sind,
- menschliche Freigaben sichtbar sind,
- Beispiel public-safe ist,
- keine Scheinsicherheit entsteht.
