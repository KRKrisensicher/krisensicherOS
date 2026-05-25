<!-- kso:product-relevance
repo-scope: product
classification: playbook
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-operating-asset; claim-safe
-->

# NIS2 Incident- und Melde-Triage

## Situation / Trigger

Nutzen, wenn ein Sicherheitsereignis, technisches Signal, Dienstleisterhinweis, Schwachstellenfund oder Ausfall möglicherweise NIS2-relevant sein könnte.

Dieses Playbook ist für Readiness, Übung und Erststrukturierung gedacht. Es ersetzt keine Live-Incident-Response, keine Rechtsberatung, keine Datenschutzbewertung und keine behördliche Meldungsentscheidung.

## Ziel

Innerhalb der ersten Lagepunkte soll klar werden:

- was bekannt ist,
- was nur Annahme ist,
- welche Dienste, Systeme, Datenklassen und Organisationseinheiten betroffen sein könnten,
- ob eine NIS2-/BSIG-/Spezialregime-Meldeprüfung erforderlich ist,
- wer rechtlich, fachlich und kommunikativ entscheiden muss,
- welche Evidenz für 24h-/72h-/Abschlusslogik vorbereitet werden muss.

## Rollen

| Rolle | Aufgabe | Entscheidung? |
| --- | --- | --- |
| Incident Owner | führt Triage, koordiniert Lagepunkte, hält Decision Log aktuell | Eskalation intern ja, externe Meldung nein ohne Freigabe |
| Technische Fachrolle | liefert Fakten zu Systemen, Logs, Zeitraum, betroffenen Diensten | keine rechtliche Entscheidung |
| Service Owner | bewertet Auswirkung auf Dienst, Nutzer, Kunden, Betrieb | fachliche Auswirkungsbewertung |
| ISB/CISO | bewertet Security-Schwere, Priorität und Maßnahmenbedarf | Security-Eskalation |
| Legal/Rechtsanwalt | prüft Meldepflichten, Betroffenheit, externe Kommunikation | rechtliche Freigabe |
| Datenschutz | prüft personenbezogene Daten und DSGVO-Meldepfad | Datenschutzfreigabe |
| Kommunikation | bereitet interne/externe Kommunikation vor | Versand nur nach Freigabe |
| Management/Krisenstab | entscheidet Ressourcen, Risikoakzeptanz, Kunden-/Behördenkommunikation | Managemententscheidung |

## Quellenanker

- NIS2-Richtlinie: <https://eur-lex.europa.eu/eli/dir/2022/2555/oj?locale=de>
- BSIG: <https://www.gesetze-im-internet.de/bsig_2025/>
- BSIG § 32 Meldepflichten: <https://www.gesetze-im-internet.de/bsig_2025/__32.html>
- BSIG § 36 Rückmeldungen des Bundesamtes: <https://www.gesetze-im-internet.de/bsig_2025/__36.html>
- EnWG § 5d bei Energiebezug: <https://www.gesetze-im-internet.de/enwg_2005/__5d.html>
- Durchführungsverordnung (EU) 2024/2690: <https://eur-lex.europa.eu/eli/reg_impl/2024/2690/oj?locale=de>
- BSI NIS2 für IT/TK und Durchführungsverordnung: <https://www.bsi.bund.de/DE/Themen/Regulierte-Wirtschaft/NIS-2-regulierte-Unternehmen/Sektorspezifische-NIS-2-Informationen/NIS-2-fuer-IT-und-TK/NIS-2-fuer-IT-und-TK_node.html>

## Triage-Prinzipien

1. Fakten und Annahmen trennen.
2. Uhrzeit der Kenntniserlangung dokumentieren.
3. Keine externe Kommunikation ohne Freigabe.
4. Rechts-/Datenschutz-/Sektorprüfung früh einschalten.
5. Meldefähigkeit vorbereiten, ohne Meldepflicht zu behaupten.
6. Evidenz sichern, aber keine forensische Bewertung durch Agenten behaupten.
7. Nach jedem Lagepunkt Decision Log aktualisieren.

## Ablauf: erste 0 bis 30 Minuten

| Schritt | Frage | Output | Owner |
| --- | --- | --- | --- |
| Signal erfassen | Was wurde wann durch wen erkannt? | Incident-Signalnotiz | Incident Owner |
| Kenntniszeitpunkt markieren | Wann begann interne Kenntnis? | Zeitanker für Meldeprüfung | Incident Owner + Legal |
| Fakten/Annahmen trennen | Welche Beobachtungen sind bestätigt? | Faktenliste / Annahmenliste | Technische Fachrolle |
| Scope vorläufig setzen | Welche Dienste/Systeme/Standorte/Datenklassen sind betroffen? | vorläufiger Scope | Service Owner |
| Sofort-Eskalation prüfen | Besteht Gefahr für kritische Dienste, Betrieb, Vertraulichkeit, Integrität oder Verfügbarkeit? | Eskalationsentscheidung intern | ISB/CISO |

## Ablauf: erste 30 bis 90 Minuten

| Schritt | Frage | Output | Owner |
| --- | --- | --- | --- |
| Betroffenheitskontext prüfen | Ist die Organisation möglicherweise wichtige/besonders wichtige Einrichtung oder Spezialregime? | Verweis auf Vorab-Betroffenheitsprüfung | NIS2 Scope Precheck Analyst + Legal |
| Meldepfad prüfen | BSIG, EnWG, DORA, DSGVO, Vertrag oder Kunde betroffen? | Meldepfad-Matrix | Legal/Datenschutz |
| Schwere vorläufig bewerten | Gibt es erhebliche Auswirkungen, kritische Dienste, Nutzerbetroffenheit, Ausfallzeit, Daten-/Systemkompromittierung? | Severity-Arbeitsannahme | ISB/CISO + Service Owner |
| Durchführungsverordnung prüfen | DNS/TLD/Cloud/RZ/CDN/MSP/MSSP/Online-Marktplatz/Suchmaschine/Social Network/Vertrauensdienst betroffen? | 2024/2690-Prüfnotiz | Legal + Fachowner |
| Kommunikationslage setzen | Wer darf intern/extern was sagen? | Kommunikationsfreigabe oder Stop | Management/Kommunikation |

## Ablauf: 24h-/72h-/Abschlusslogik vorbereiten

Die konkrete Meldepflicht und Frist muss rechtlich geprüft werden. Dieses Playbook bereitet nur die Informationslogik vor.

| Lagepunkt | Zweck | Mindestinhalt als Arbeitslogik | Freigabe |
| --- | --- | --- | --- |
| Frühe Erstmeldung / 24h-Logik | schnelle Orientierung, ob ein erheblicher Sicherheitsvorfall vorliegen könnte | Kenntniszeitpunkt, betroffene Dienste, Verdacht auf böswillige/rechtswidrige Handlung, mögliche grenzüberschreitende Auswirkungen, Sofortmaßnahmen | Legal/Management |
| 72h-Logik | bestätigte oder aktualisierte Bewertung | Schweregrad, Auswirkungen, Kompromittierungsfaktoren, laufende Maßnahmen, offene Annahmen | Legal/Management |
| Zwischenmeldung | Statusaktualisierung bei neuer Lage oder Anforderung | neue Fakten, Maßnahmenstatus, Auswirkungsänderung | Incident Owner + Legal |
| Abschlusslogik | Zusammenfassung nach Stabilisierung | Beschreibung, Schwere/Auswirkung, wahrscheinliche Ursache, getroffene und laufende Abhilfemaßnahmen, grenzüberschreitende Auswirkungen falls relevant | Management/Legal |

## Meldepfad-Matrix

| Pfad | Prüffrage | Handoff | Status |
| --- | --- | --- | --- |
| BSIG/NIS2 | Mögliche wichtige/besonders wichtige Einrichtung und erheblicher Sicherheitsvorfall? | Legal/Rechtsanwalt, ISB/CISO | offen |
| EnWG Energie | Energieversorgungsnetz, Energieanlage oder digitaler Energiedienst nach EnWG § 5c? | Legal, Energie-Fachowner | offen |
| Durchführungsverordnung 2024/2690 | adressierte digitale Einrichtungsart und Kriterien für erheblichen Vorfall? | Legal, Service Owner | offen |
| DSGVO | personenbezogene Daten betroffen? | Datenschutz | offen |
| Vertrag/Kunde | vertragliche Meldepflichten oder Kundenkommunikation? | Legal, Account/Kommunikation | offen |
| Behörden/Öffentlichkeit | externe Meldung oder Pressekommunikation? | Management/Krisenstab | offen |

## Evidence Pack für Incident-Triage

| Evidenz | Zweck | Speicherort intern | Owner |
| --- | --- | --- | --- |
| Zeitlinie | Kenntnis, Lagepunkte, Entscheidungen |  | Incident Owner |
| Fakten-/Annahmenliste | Trennung belastbarer Informationen |  | Technische Fachrolle |
| Scope-Notiz | betroffene Dienste/Systeme/Datenklassen |  | Service Owner |
| Log-/Alert-Referenzen | technische Grundlage |  | Technische Fachrolle |
| Entscheidungslog | wer hat was wann entschieden |  | Incident Owner |
| Meldepfad-Prüfnotiz | Rechts-/Datenschutz-/Sektorprüfung |  | Legal/Datenschutz |
| Kommunikationsfreigaben | interne/externe Aussagen |  | Kommunikation/Management |
| Maßnahmenliste | Sofortmaßnahmen und Follow-up |  | ISB/CISO |

## Agentenunterstützung

| Agent | Nutzung | Grenze |
| --- | --- | --- |
| `incident-readiness-coach` | Triage-Fragen, Eskalationskarte, Übungslogik | keine Live-Krisenleitung |
| `nis2-scope-precheck-analyst` | Betroffenheitsindikatoren und Spezialregime strukturieren | keine Rechtsentscheidung |
| `control-evidence-architect` | Evidence Pack und Nachweislogik | keine Wirksamkeitsgarantie |
| `management-review-facilitator` | Entscheidungen, Optionen, Ressourcenbedarf | entscheidet nicht selbst |
| `agent-quality-and-safety-reviewer` | Claim-Safety, Human Gates, Stop-Punkte | keine fachliche Freigabe |

## Stop-Punkte

Sofort menschlich eskalieren bei:

- möglicher Meldepflicht,
- personenbezogenen Daten,
- kritischen Dienstauswirkungen,
- grenzüberschreitenden Auswirkungen,
- Kunden-/Behörden-/Pressekommunikation,
- unklarem Owner,
- Risikoakzeptanz oder Betriebsfortsetzungsentscheidung,
- rechtlicher oder datenschutzrechtlicher Auslegung.

## Output

- ausgefüllte Incident-Triage-Notiz,
- Meldepfad-Matrix,
- Decision Log,
- Evidence-Pack-Liste,
- Handoff an Legal/Datenschutz/Management,
- Lessons-Learned-Backlog.

## Grenzen

- keine Rechtsberatung,
- keine Datenschutzberatung,
- keine Feststellung einer Meldepflicht,
- keine Live-Incident-Response,
- keine externe Kommunikation ohne Freigabe,
- keine echten Incident-, Kunden-, Personen- oder Systemdaten in öffentlichen Beispielen.
