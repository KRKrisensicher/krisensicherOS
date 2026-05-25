<!-- kso:product-relevance
repo-scope: product
classification: implementation-guide-module
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->

# 04 — Schutzmaßnahmen als Betriebsroutinen

## Zweck

Dieses Modul macht aus Schutzmaßnahmen konkrete Arbeitsweisen. Eine Maßnahme ist erst dann nützlich, wenn Owner, Trigger, Ablauf, Evidenz, Eskalation und Review klar sind.

## Referenzrahmen

- ISO/IEC 27001:2022 — Abschnitte 6.1, 8.1 und Anhang A als Referenzanker.
- BSIG § 30 bei möglicher Betroffenheit.

## Nutzer und Rollen

- Control Owner,
- ISB/CISO,
- IT-/OT-/Service Owner,
- Prozessverantwortliche,
- Evidence Owner,
- interne Reviewrolle.

## Trigger

- Risiko erfordert Maßnahme,
- bestehende Maßnahme ist nicht evidenzierbar,
- technische oder organisatorische Änderung,
- Finding oder Incident,
- Management priorisiert Schutzbedarf.

## Ablauf

1. Maßnahme aus Risiko oder Arbeitsanforderung ableiten.
2. Betriebsroutine beschreiben: Zweck, Owner, Trigger, Schritte, Output.
3. Evidenzquelle bestimmen: Log, Ticket, Protokoll, Konfiguration, Reviewnotiz.
4. Eskalation definieren: Wann gilt die Routine als verletzt oder blockiert?
5. Reviewmethode festlegen: Stichprobe, Test, Review, technische Prüfung oder Managementbericht.
6. Maßnahme im Backlog und in der Risk-Control Map verknüpfen.

## Entscheidungen

| Entscheidung | Optionen | Human Gate |
| --- | --- | --- |
| Maßnahme verpflichtend? | ja / nein / pilotieren | ISMS Owner / Management |
| Umsetzung ausreichend? | ja / teilweise / nein | Control Owner + Reviewer |
| Ausnahme zulassen? | nein / befristet / mit Auflage | Risk Owner / Management |
| Evidenz ausreichend? | ja / lückenhaft / fehlt | Evidence Owner |

## Evidenz

- Control-Routine-Beschreibung,
- Maßnahmenbacklog,
- technische oder organisatorische Nachweise,
- Ausnahmeentscheidungen,
- Wirksamkeitsprüfungen,
- Reviewnotizen.

## Review

Prüffragen:

- Reduziert die Maßnahme ein benanntes Risiko?
- Wird sie tatsächlich ausgeführt?
- Gibt es verwertbare Evidenz?
- Sind Ausnahmen entschieden und befristet?
- Ist der Aufwand tragbar?

## BSIG-/NIS2-Bezug

Bei möglicher Betroffenheit können Schutzmaßnahmen helfen, Risikomanagementanforderungen in betriebliche Routinen zu übersetzen. Die konkrete rechtliche Relevanz bleibt zu prüfen.

## Grenzen

Keine Wiedergabe von ISO-Kontrolltexten, keine Sicherheitsgarantie, keine technische Architekturentscheidung ohne zuständige Fachrolle.

## Handoffs

- an IT/OT-Betrieb,
- an Service Owner,
- an Risk Owner,
- an Evidence Owner,
- an Management bei Ausnahmen oder Ressourcenbedarf.
