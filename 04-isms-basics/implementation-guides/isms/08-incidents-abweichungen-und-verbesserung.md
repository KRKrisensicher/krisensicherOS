<!-- kso:product-relevance
repo-scope: product
classification: implementation-guide-module
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->

# 08 — Incidents, Abweichungen und Verbesserung

## Zweck

Dieses Modul verbindet Sicherheitsereignisse, Abweichungen, Findings und Lessons Learned mit ISMS-Verbesserung.

## Referenzrahmen

- ISO/IEC 27001:2022 — Abschnitte 8, 9.1 und 10.
- BSIG § 32: <https://www.gesetze-im-internet.de/bsig_2025/__32.html>
- BSIG § 30 bei möglicher Betroffenheit.

## Nutzer und Rollen

- Incident Owner,
- ISMS Owner,
- ISB/CISO,
- Service Owner,
- Legal/Datenschutz,
- Management,
- Corrective Action Owner.

## Trigger

- Security Event,
- bestätigter Incident,
- Beinahevorfall,
- interne Abweichung,
- Audit-/Review-Finding,
- Meldeprüfung,
- Lessons Learned.

## Ablauf

1. Signal erfassen und Fakten von Annahmen trennen.
2. Incident- oder Abweichungstyp einordnen.
3. Meldepfad prüfen lassen: BSIG, DSGVO, Vertrag, Kunde, Sektorregel.
4. Sofortmaßnahmen und Owner festlegen.
5. Ursachen- und Wirkungsperspektive nach Stabilisierung prüfen.
6. Verbesserungsmaßnahme ins Backlog übernehmen.
7. Reviewtermin für Wirksamkeit setzen.

## Entscheidungen

| Entscheidung | Optionen | Human Gate |
| --- | --- | --- |
| Eskalation nötig? | ja / nein / unklar | Incident Owner |
| Meldeprüfung nötig? | ja / nein / unklar | Legal/Datenschutz |
| Krisenstab aktivieren? | ja / nein / vorbereiten | Management |
| Verbesserungsmaßnahme | sofort / geplant / verworfen | ISMS Owner / Management |

## Evidenz

- Incident- oder Abweichungsnotiz,
- Zeitlinie,
- Meldepfad-Prüfnotiz,
- Maßnahmenliste,
- Decision Log,
- Lessons-Learned-Protokoll,
- Wirksamkeitsreview.

## Review

Prüfen, ob aus Ereignissen konkrete Verbesserungen entstehen: Maßnahme, Owner, Frist, Evidenz, Review.

## BSIG-/NIS2-Bezug

§ 32 BSIG ist bei möglicher Betroffenheit ein wichtiger Referenzanker für Meldeprüfungen. Dieses Modul stellt keine Meldepflicht fest, sondern bereitet die Prüfung vor.

## Grenzen

Keine Live-Krisenleitung, keine Feststellung einer Meldepflicht, keine externe Kommunikation ohne Freigabe.

## Handoffs

- an Incident-Eskalationsplaybook,
- an Legal/Datenschutz,
- an Management/Krisenstab,
- an Corrective Action Planning.
