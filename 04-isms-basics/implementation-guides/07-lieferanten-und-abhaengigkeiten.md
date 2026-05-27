
# 07 — Lieferanten und Abhängigkeiten

## Zweck

Dieses Modul macht Lieferanten, Dienstleister, Plattformen und sonstige Abhängigkeiten als Teil des ISMS steuerbar.

## Referenzrahmen

- ISO/IEC 27001:2022 — Abschnitte 4.3, 6.1, 8.1, 9 und Anhang A als Referenzanker.
- BSIG § 30 und § 32 bei möglicher Betroffenheit.
- EnWG § 5c bis § 5e bei Energiebezug.

## Nutzer und Rollen

- Service Owner,
- Einkauf / Vendor Management,
- ISMS Owner,
- Risk Owner,
- Legal,
- Datenschutz,
- Incident Owner.

## Trigger

- neuer Lieferant,
- kritischer Dienstleister,
- Outsourcing oder Cloud-/MSP-/MSSP-Bezug,
- Vertragsänderung,
- Lieferantenincident,
- fehlende Nachweise.

## Ablauf

1. Lieferanten- und Abhängigkeitsregister pflegen.
2. Kritikalität bestimmen: Service, Datenklasse, Ausfallwirkung, Ersatzbarkeit.
3. Sicherheits- und Nachweisanforderungen als eigene Arbeitsfragen formulieren.
4. Vertrags-, Datenschutz- und Meldepflichten an Legal/Datenschutz übergeben.
5. Evidenz und Reviewtermin festlegen.
6. Exit-, Notfall- oder Ersatzlogik prüfen, falls kritisch.

## Entscheidungen

| Entscheidung | Optionen | Human Gate |
| --- | --- | --- |
| Kritikalität | kritisch / relevant / gering / unklar | Service Owner |
| Nachweise ausreichend? | ja / teilweise / nein | Evidence Owner |
| Vertragslücke akzeptieren? | nein / befristet / Managemententscheid | Legal + Management |
| Eskalation bei Lieferantenincident | intern / Kunde / Behörde prüfen | Incident Owner + Legal |

## Evidenz

- Lieferantenregister,
- Kritikalitätsbewertung,
- Nachweis- und Vertragsreferenzen,
- Risikoentscheidung,
- Reviewprotokoll,
- Incident- oder Eskalationsnotizen.

## Review

Mindestens bei Vertragsverlängerung, Scope-Änderung, neuem Service, Incident, Nachweislücke oder jährlichem Lieferantenreview.

## BSIG-/NIS2-Bezug

NIS2-/BSIG-nahe Organisationen müssen Lieferkettenrisiken besonders sauber steuern. Dieses Modul bereitet Risiko-, Nachweis- und Meldehygiene vor, ohne Pflichten verbindlich auszulegen.

## Grenzen

Keine Vertragsprüfung, keine Datenschutzprüfung, keine Bewertung eines Lieferanten als „sicher“.

## Handoffs

- an Einkauf/Vendor Management,
- an Legal/Datenschutz,
- an Incident-Triage,
- an Management bei kritischen Abhängigkeiten.
