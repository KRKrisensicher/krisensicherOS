<!-- kso:product-relevance
repo-scope: product
classification: implementation-guide-module
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->

# 01 — Kontext, Scope und Betroffenheit

## Zweck

Dieses Modul macht sichtbar, für welchen Organisationsausschnitt das ISMS betrieben wird und welche externen Anforderungen als Arbeitsannahme relevant sein könnten.

## Referenzrahmen

- ISO/IEC 27001:2022 — Abschnitte 4.1 bis 4.4.
- BSIG § 28: <https://www.gesetze-im-internet.de/bsig_2025/__28.html>
- BSIG Anlage 1: <https://www.gesetze-im-internet.de/bsig_2025/anlage_1.html>
- BSIG Anlage 2: <https://www.gesetze-im-internet.de/bsig_2025/anlage_2.html>
- EnWG § 5c bis § 5e bei Energiebezug.

## Nutzer und Rollen

- ISMS Owner,
- Geschäftsleitung,
- Fachbereichs- und Service Owner,
- Legal/Rechtsfunktion,
- Datenschutz,
- NIS2 Scope Precheck Analyst.

## Trigger

- ISMS-Neustart,
- neue Organisationseinheit, Service, Standort oder Lieferkette,
- NIS2-/BSIG-Vorabprüfung,
- wesentliche Änderung im Geschäftsmodell,
- Audit- oder Kundenanforderung.

## Ablauf

1. Organisationsprofil erfassen: Leistungen, Standorte, Services, Kunden, kritische Prozesse.
2. Start-Scope festlegen: was ist drin, was bewusst nicht?
3. Interessierte Parteien als Entscheidungsumfeld erfassen: Leitung, Kunden, Aufsicht, Lieferanten, Mitarbeitende.
4. Vorab-Betroffenheit prüfen: Sektor, Einrichtungsart, Größe, Spezialregime.
5. Offene Rechtsfragen an Legal übergeben.
6. Scope-Entscheidung im Decision Log dokumentieren.

## Entscheidungen

| Entscheidung | Optionen | Human Gate |
| --- | --- | --- |
| Start-Scope | eng / mittel / erweitert | Geschäftsleitung |
| BSIG-Arbeitsannahme | möglicher Treffer / unklar / derzeit kein Treffer | Legal |
| Energie-Spezialprüfung | nötig / nicht nötig / offen | Legal + Fachowner |
| Scope-Erweiterung | jetzt / später / nicht | Management |

## Evidenz

- Scope Canvas,
- Organisations- und Serviceübersicht,
- Betroffenheitsfragebogen,
- Legal-Handoff,
- Decision Log,
- Liste offener Annahmen.

## Review

Mindestens prüfen bei neuen Services, M&A, Auslagerung, Standortänderung, neuen Schwellenwerten, Sektorwechsel, Incident oder Managemententscheidung.

## BSIG-/NIS2-Bezug

Dieses Modul verbindet ISMS-Scope mit NIS2-/BSIG-Vorablogik. Das Ergebnis bleibt eine Arbeitsannahme und muss rechtlich geprüft werden.

## Grenzen

Keine Feststellung, ob eine Organisation betroffen oder nicht betroffen ist. Keine Rechtsauslegung.

## Handoffs

- an `nis2-scope-precheck-analyst`,
- an Legal/Rechtsanwalt,
- an Management Review bei Scope- oder Ressourcenfragen.
