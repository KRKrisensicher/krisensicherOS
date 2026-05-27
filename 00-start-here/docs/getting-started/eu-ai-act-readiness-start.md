
# EU-AI-Act-Readiness starten

## Zweck

Dieser Einstieg hilft, KI-Nutzung in einer Organisation sichtbar zu machen und als Governance-Routine vorzubereiten.

Er ersetzt keine Rechtsberatung, Datenschutzberatung, verbindliche EU-AI-Act-Einordnung oder Konformitätsbewertung. Das Ergebnis ist ein Inventar- und Handoff-Artefakt für verantwortliche Menschen.

## Wann nutzen?

Nutze diesen Pfad, wenn:

- KI-Systeme, KI-Funktionen oder KI-Dienste im Unternehmen genutzt werden,
- Cloud-KI, M365 Copilot, Fachanwendungen mit KI-Funktionen oder lokale KI eingeführt werden,
- unklar ist, wer fachlich, technisch oder rechtlich verantwortlich ist,
- Datenklassen, Personenbezug oder menschliche Aufsicht noch nicht geklärt sind,
- Legal, Datenschutz, Management oder IT/Security eine strukturierte Vorprüfung brauchen.

## 15-Minuten-Start

Öffne nur diese Artefakte:

1. [`../../templates/ki-nutzungsfreigabe-matrix.md`](../../../08-templates-playbooks/templates/ki-nutzungsfreigabe-matrix.md)
2. [`../../templates/ki-system-inventar-und-risikovorpruefung.md`](../../../08-templates-playbooks/templates/ki-system-inventar-und-risikovorpruefung.md)
3. [`../../templates/legal-datenschutz-handoff.md`](../../../08-templates-playbooks/templates/legal-datenschutz-handoff.md)
4. [`../../templates/decision-log.md`](../../../08-templates-playbooks/templates/decision-log.md)

Nach 15 Minuten sollte klar sein:

- welches KI-System oder welcher KI-Use-Case betrachtet wird,
- wer fachlicher Owner ist,
- welche Datenklasse betroffen ist,
- ob Personenbezug, vertrauliche Inhalte oder externe Anbieter eine Rolle spielen,
- welche menschliche Prüfung nötig ist,
- welche Entscheidung offen bleibt.

## Leitfragen

### 1. Was ist das KI-System oder der KI-Use-Case?

- Name oder Arbeitsbezeichnung,
- Anbieter oder interne Lösung,
- fachlicher Zweck,
- betroffener Prozess,
- Nutzergruppe.

### 2. Welche Rolle hat die Organisation?

Nur als Arbeitsannahme erfassen, nicht final bewerten:

- beschafft oder nutzt die Organisation ein KI-System?
- betreibt oder konfiguriert sie es selbst?
- integriert sie es in eigene Leistungen?
- stellt sie es anderen zur Verfügung?

Finale Rollen- und Pflichtenbewertung ist ein Legal-/Management-Handoff.

### 3. Welche Daten und Entscheidungen sind betroffen?

- Datenklasse: öffentlich, intern, vertraulich, personenbezogen, besonders schutzbedürftig oder unklar,
- Entscheidungsnähe: assistierend, empfehlend, priorisierend, automatisierend,
- Auswirkung auf Personen, Kunden, Beschäftigte, Sicherheit, Verfügbarkeit oder kritische Prozesse,
- Protokollierung und Nachvollziehbarkeit.

### 4. Welche menschliche Aufsicht gibt es?

- Wer prüft Eingaben?
- Wer prüft Ergebnisse?
- Wer darf Ergebnisse übernehmen?
- Wer stoppt bei Fehlern, Bias, Halluzinationen, Datenschutzrisiken oder Sicherheitsrisiken?
- Wer entscheidet über Freigabe, Einschränkung oder Nichtnutzung?

## Minimaler Output

- ein Eintrag im KI-System-Inventar,
- eine Datenklassen- und Freigabeannahme,
- ein Legal-/Datenschutz-Handoff bei offenen Fragen,
- ein Decision-Log-Eintrag mit Owner, nächstem Schritt und Reviewtermin.

## Anschluss an krisensicherOS

- Für erlaubte KI-Umgebungen: [`../../templates/ki-nutzungsfreigabe-matrix.md`](../../../08-templates-playbooks/templates/ki-nutzungsfreigabe-matrix.md)
- Für Governance-Entscheidungen: [`../../templates/decision-log.md`](../../../08-templates-playbooks/templates/decision-log.md)
- Für rechtliche oder datenschutzrechtliche Fragen: [`../../templates/legal-datenschutz-handoff.md`](../../../08-templates-playbooks/templates/legal-datenschutz-handoff.md)
- Für Ablaufsteuerung: [`../../workflows/eu-ai-act-readiness-precheck.yaml`](../../../08-templates-playbooks/workflows/eu-ai-act-readiness-precheck.yaml)
- Für Betriebsregeln von Agenten: [`../../07-ai-governance-agents/`](../../../07-ai-governance-agents/)

## Stop-Punkte

Stoppen und menschliche Freigabe einholen bei:

- finaler EU-AI-Act-Rollen- oder Risikoklassifizierung,
- Rechts- oder Datenschutzbewertung,
- Einsatz mit personenbezogenen, vertraulichen oder besonders schutzbedürftigen Daten,
- KI-Ausgaben mit Wirkung auf Personen oder wesentliche Geschäftsprozesse,
- externer Kommunikation, Kundenzusage oder Anbieterfreigabe,
- Managemententscheidung über Einführung, Einschränkung oder Risikoakzeptanz.

## Grenzen

Dieser Starter macht KI-Nutzung sichtbar und vorbereitet entscheidbare Fragen. Er bestätigt keine EU-AI-Act-Konformität, keine Zulässigkeit, keine Datenschutzkonformität und keine technische Sicherheit.
