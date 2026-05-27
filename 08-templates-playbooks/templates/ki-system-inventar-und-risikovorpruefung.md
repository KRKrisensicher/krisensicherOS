
# KI-System-Inventar und Risikovorprüfung

## Zweck

Diese Vorlage erfasst KI-Systeme, KI-Funktionen oder KI-Use-Cases als Arbeitsinventar. Sie hilft, Datenklassen, Verantwortlichkeiten, menschliche Aufsicht und offene Handoffs sichtbar zu machen.

Sie ersetzt keine Rechtsberatung, Datenschutzbewertung, EU-AI-Act-Klassifizierung, technische Sicherheitsprüfung oder Managemententscheidung.

## Trigger

Nutze diese Vorlage, wenn:

- ein neues KI-System beschafft, aktiviert oder pilotiert wird,
- eine vorhandene Anwendung neue KI-Funktionen erhält,
- Cloud-KI, M365 Copilot, lokale KI oder ein Fachverfahren mit KI genutzt werden soll,
- eine KI-Nutzung in NIS2-, ISMS-, Datenschutz-, Lieferanten- oder Management-Review-Arbeit relevant wird,
- unklar ist, welche Human Gates nötig sind.

## Rollen

- Fachlicher System- oder Prozessowner,
- IT-/Security-Owner,
- KI-/Tool-Owner,
- Datenschutz,
- Legal / Vertragsmanagement,
- Management bei Risiko-, Budget- oder Freigabeentscheidung.

## Inventar

| Feld | Eintrag |
| --- | --- |
| Inventar-ID |  |
| System / Dienst / KI-Funktion |  |
| Anbieter / Betreiber |  |
| Interne verantwortliche Rolle |  |
| Fachlicher Zweck |  |
| Betroffener Prozess |  |
| Nutzergruppe |  |
| Einsatzstatus | Idee / Pilot / produktiv / ausgesetzt / außer Betrieb |
| Einsatzort | Cloud / M365 / lokale KI / Fachanwendung / eingebettet / unklar |
| Externe Abhängigkeiten |  |
| Vertrags-/Lieferantenbezug | nein / ja / unklar |
| Quelle / Referenz |  |

## Vorprüfung

| Prüffeld | Arbeitsannahme | Owner | Human Gate |
| --- | --- | --- | --- |
| Rolle der Organisation | nutzt / betreibt / integriert / stellt bereit / unklar |  | Legal/Management |
| Datenklasse | öffentlich / intern / vertraulich / personenbezogen / besonders schutzbedürftig / unklar |  | Datenschutz/Security |
| Personenbezug | nein / ja / unklar |  | Datenschutz |
| Betroffene Personengruppen | keine / Beschäftigte / Kunden / Bürger / Lieferanten / unklar |  | Datenschutz/Legal |
| Entscheidungsnähe | assistierend / empfehlend / priorisierend / automatisierend / unklar |  | Fachowner/Legal |
| Wirkung auf Personen | keine / gering / relevant / hoch / unklar |  | Legal/Datenschutz/Management |
| Kritikalität für Prozess | niedrig / mittel / hoch / kritisch / unklar |  | IT/Security/Management |
| Sicherheitsrelevanz | nein / ja / unklar |  | Security |
| Menschliche Aufsicht definiert | ja / nein / unklar |  | Fachowner/Management |
| Logging / Nachvollziehbarkeit | vorhanden / teilweise / fehlt / unklar |  | IT/Security |
| Redaction oder Datenminimierung nötig | nein / ja / unklar |  | Datenschutz/Security |
| Freigegebene KI-Umgebung vorhanden | ja / nein / eingeschränkt / unklar |  | KI-/IT-Owner |
| Handoff nötig | Legal / Datenschutz / Management / IT-Security / Lieferant / keines / unklar |  | jeweilige Rolle |

## Menschliche Aufsicht

| Frage | Antwort |
| --- | --- |
| Wer darf Eingaben freigeben? |  |
| Wer prüft KI-Ausgaben fachlich? |  |
| Wer darf KI-Ausgaben übernehmen oder verwerfen? |  |
| Wann muss gestoppt werden? |  |
| Wie werden Fehler, Beschwerden oder Auffälligkeiten gemeldet? |  |
| Wann wird die Freigabe überprüft? |  |

## Risiken und offene Fragen

| Thema | Beobachtung | Entscheidung nötig? | Owner | Frist |
| --- | --- | --- | --- | --- |
| Daten / Datenschutz |  |  |  |  |
| Recht / EU-AI-Act-Rolle |  |  |  |  |
| Security / Missbrauch |  |  |  |  |
| Lieferant / Vertrag |  |  |  |  |
| Prozesswirkung |  |  |  |  |
| Nachweise / Logging |  |  |  |  |

## Handoff-Entscheidung

| Zielrolle | Frage | Kontext | benötigte Rückmeldung | Status |
| --- | --- | --- | --- | --- |
| Legal |  |  |  | offen |
| Datenschutz |  |  |  | offen |
| Management |  |  |  | offen |
| IT/Security |  |  |  | offen |
| Lieferanten-/Vertragsmanagement |  |  |  | offen |

## Output

- Inventareintrag für ein KI-System oder einen KI-Use-Case,
- Datenklassen- und Einsatzannahme,
- markierte Human Gates,
- offene Fragen für Legal, Datenschutz, Management, IT/Security oder Lieferantenmanagement,
- Decision-Log-Eintrag mit nächstem Schritt.

## Qualitätsgates

- Keine echten Personen-, Kunden-, Vertrags- oder Systemgeheimnisse in öffentliche Beispiele eintragen.
- Keine finale Rechts-, Datenschutz- oder EU-AI-Act-Einordnung behaupten.
- Datenklasse und menschliche Aufsicht sind bekannt oder als offen markiert.
- Kritische oder unklare Nutzung führt zu Handoff, nicht zu automatischer Freigabe.
- Entscheidungen werden im [`decision-log.md`](decision-log.md) dokumentiert.
