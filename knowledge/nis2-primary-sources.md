<!-- kso:product-relevance
repo-scope: product
classification: source-register-structure
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# NIS2-Primärquellen und Auswertungsanker

Stand: 2026-05-25

## Zweck

Diese Datei bündelt offizielle Referenzanker für NIS2-Readiness. Sie ersetzt keine Rechtsberatung und enthält keine verbindliche Betroffenheitsprüfung.

**Pflicht-Hinweis:** Jede Vorab-Einschätzung zur Betroffenheit muss durch eine qualifizierte Rechtsanwältin, einen qualifizierten Rechtsanwalt oder eine entsprechend zuständige Rechtsfunktion geprüft werden.

## Offizielle Quellen

### EU: NIS2-Richtlinie

- Richtlinie (EU) 2022/2555 — NIS2: <https://eur-lex.europa.eu/eli/dir/2022/2555/oj?locale=de>
- Nutzen: Begriffe, Ziele, Erwägungsgründe, Mindestanforderungen, Melde- und Aufsichtslogik.
- Arbeitsregel: Richtlinie als Referenzanker nutzen; nationale Umsetzung, Sektorregeln und Einzelfallprüfung separat prüfen.

### Deutschland: BSIG 2025

- BSIG, nichtamtliches Inhaltsverzeichnis: <https://www.gesetze-im-internet.de/bsig_2025/>
- § 28 BSIG — besonders wichtige und wichtige Einrichtungen: <https://www.gesetze-im-internet.de/bsig_2025/__28.html>
- Anlage 1 BSIG — Sektoren besonders wichtiger und wichtiger Einrichtungen: <https://www.gesetze-im-internet.de/bsig_2025/anlage_1.html>
- Anlage 2 BSIG — Sektoren wichtiger Einrichtungen: <https://www.gesetze-im-internet.de/bsig_2025/anlage_2.html>
- Nutzen: deutsche Vorab-Betroffenheitslogik, Kategorien, Sektor-/Einrichtungsarten, Schwellenlogik, Ausnahmen und Handoffs.

### Energie-Sektor: EnWG § 5c bis § 5e

Rico hatte „§ 5c bis 5e“ als Pflichtanker genannt. Im aktuellen offiziellen Fundstellenbild liegen diese Normen im EnWG und verweisen auf BSIG-Kategorien.

- § 5c EnWG — IT-Sicherheit im Anlagen-/Netz-/Energiedienstkontext: <https://www.gesetze-im-internet.de/enwg_2005/__5c.html>
- § 5d EnWG — Dokumentations-, Melde- und Registrierungspflichten: <https://www.gesetze-im-internet.de/enwg_2005/__5d.html>
- § 5e EnWG — Geschäftsleitungspflichten und Schulung: <https://www.gesetze-im-internet.de/enwg_2005/__5e.html>
- Nutzen: Speziallogik für Energieversorgungsnetze, Energieanlagen und digitale Energiedienste.

### BSI: FAQ und Betroffenheitsprüfung

- BSI NIS-2-Betroffenheitsprüfung: <https://www.bsi.bund.de/DE/Themen/Regulierte-Wirtschaft/NIS-2-regulierte-Unternehmen/NIS-2-Betroffenheitspruefung/nis-2-betroffenheitspruefung_node.html>
- BSI sektorspezifische FAQ: <https://www.bsi.bund.de/DE/Themen/Regulierte-Wirtschaft/NIS-2-regulierte-Unternehmen/NIS-2-FAQ/NIS-2-FAQ-sektorspezifisch/NIS-2-Sektorspezifische-FAQ_node.html>
- BSI NIS-2 für IT und TK / DurchführungsVO (EU) 2024/2690: <https://www.bsi.bund.de/DE/Themen/Regulierte-Wirtschaft/NIS-2-regulierte-Unternehmen/Sektorspezifische-NIS-2-Informationen/NIS-2-fuer-IT-und-TK/NIS-2-fuer-IT-und-TK_node.html>
- Nutzen: Plausibilisierung, Sektorhinweise, aktuelle BSI-Auslegungshinweise. Nicht als alleinige Rechtsgrundlage verwenden.

### EU: Durchführungsverordnung (EU) 2024/2690

- Durchführungsverordnung (EU) 2024/2690: <https://eur-lex.europa.eu/eli/reg_impl/2024/2690/oj?locale=de>
- PDF-Ansicht: <https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=OJ:L_202402690>
- Nutzen: technische und methodische Anforderungen an Risikomanagementmaßnahmen und Konkretisierung erheblicher Sicherheitsvorfälle für bestimmte digitale Einrichtungsarten.

Betroffene Einrichtungsarten nach BSI-Zusammenfassung:

- DNS-Diensteanbieter,
- TLD-Namenregister,
- Anbieter von Cloud-Computing-Diensten,
- Anbieter von Rechenzentrumsdiensten,
- Betreiber von Inhaltszustellnetzen,
- Managed Services Provider,
- Managed Security Services Provider,
- Anbieter von Online-Marktplätzen,
- Online-Suchmaschinen,
- Plattformen für Dienste sozialer Netzwerke,
- Vertrauensdiensteanbieter.

## Auswertungsreihenfolge

1. Organisations- und Leistungsprofil erfassen.
2. Sektor-/Einrichtungsart nach BSIG Anlage 1/2 vorprüfen.
3. Größen-, Umsatz- und Bilanzsummenlogik nach § 28 BSIG erfassen.
4. Sonderkategorien prüfen: kritische Anlagen, DNS/TLD, TK, Energie, Finanz/DORA, Telematik, Gebietskörperschaften.
5. Falls Energie: EnWG § 5c bis § 5e zusätzlich prüfen.
6. Falls digitale Infrastruktur/digitale Dienste/Vertrauensdienste: Durchführungsverordnung (EU) 2024/2690 zusätzlich auswerten.
7. BSI-Betroffenheitsprüfung und sektorspezifische FAQ als Plausibilisierung vor die abschließende menschliche Rechtsprüfung schalten.
8. Ergebnis nur als Arbeitsannahme ausgeben: „möglicherweise betroffen“, „nicht ausreichend belegbar“, „derzeit kein Treffer in den abgefragten Kriterien“.

## Verbotene Ausgabeformulierungen

Nicht ausgeben:

- „Sie sind NIS2-pflichtig.“
- „Sie sind nicht betroffen.“
- „Das ist rechtssicher.“
- „NIS2-Konformität ist gegeben.“
- „Keine anwaltliche Prüfung nötig.“

Erlaubt:

- „Die Vorab-Prüfung zeigt Indikatoren für eine mögliche Betroffenheit.“
- „Die Vorab-Prüfung zeigt derzeit keinen klaren Treffer; offene Punkte bleiben anwaltlich zu prüfen.“
- „Die Einordnung hängt von Rechtsauslegung, Konzern-/Partnerlogik, Einrichtungsart und tatsächlicher Tätigkeit ab.“
