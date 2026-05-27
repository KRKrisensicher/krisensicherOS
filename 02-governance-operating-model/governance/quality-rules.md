
# Qualitätsregeln

## Zweck

Diese Qualitätsregeln gelten für krisensicherOS-Artefakte: Agentenprofile, Skills, Templates, Playbooks, Workflows, Beispiele, Quellenregister und Dokumentation.

## 1. Kein Artefakt ohne Betriebslogik

Jede Vorlage, jeder Skill, jedes Playbook und jeder Workflow muss beantworten:

- Wer nutzt es?
- Wann wird es genutzt?
- Wofür wird es genutzt?
- Welche Inputs braucht es?
- Welche Schritte führt es aus?
- Welche Entscheidung unterstützt es?
- Welche Evidenz entsteht?
- Wer prüft oder gibt frei?
- Wann wird reviewed?

## 2. Keine Compliance-Floskeln

Unklare Begriffe werden operationalisiert:

- „regelmäßig“ → konkrete Frequenz oder Trigger
- „angemessen“ → Kriterien und Entscheidungsspielraum
- „sicherstellen“ → Rolle, Kontrolle, Evidenz und Review
- „zeitnah“ → Zeitfenster oder Eskalationspunkt
- „relevant“ → Scope, Risiko oder Entscheidungsbezug

## 3. Keine Scheinsicherheit

Artefakte dürfen keine Rechts-, Datenschutz-, Audit-, Sicherheits- oder Zertifizierungsgarantie suggerieren.

Zulässig sind:

- Fragen,
- Prüfpunkte,
- Arbeitsannahmen,
- Evidenzbedarf,
- Entscheidungsoptionen,
- Handoffs an menschliche Rollen.

Nicht zulässig sind:

- verbindliche Rechtsauslegung,
- Datenschutzbewertung als Agentenentscheidung,
- Konformitätsbestätigung,
- Zertifizierungszusage,
- Sicherheitsgarantie,
- Risikoakzeptanz ohne verantwortliche Person.

## 4. CISO-/ISB-Zeit schützen

Routinearbeit soll vorbereitet, komprimiert oder geprüft werden. Management- und Verantwortungsentscheidungen müssen sichtbar bleiben.

Ein Artefakt ist nur wertvoll, wenn es mindestens eines verbessert:

- Entscheidungsfähigkeit,
- Evidenzqualität,
- Priorisierung,
- Handoff-Klarheit,
- Review-Fähigkeit,
- operative Umsetzung.

## 5. Verantwortung bleibt menschlich

Agenten entlasten, strukturieren und prüfen. Sie ersetzen keine Verantwortungsübernahme.

Immer menschlich bleiben:

- rechtliche Bewertung,
- Datenschutzbewertung,
- Vertragsauslegung,
- Risikoakzeptanz,
- Managemententscheidung,
- externe Kommunikation,
- Veröffentlichung.

## 6. Governance statt Dokumentation

Dokumente sind Nebenprodukte funktionierender Routinen, nicht das Ziel.

Ein Dokument ohne Owner, Trigger, Output, Evidenz und Review ist nicht fertig.

## 7. Public-safe by default

Öffentliche Artefakte enthalten:

- fiktive Beispiele,
- öffentliche Quellenreferenzen,
- Metadaten,
- eigene Zusammenfassungen,
- leere Nutzerfelder.

Öffentliche Artefakte enthalten nicht:

- echte Kundendaten,
- personenbezogene Daten,
- vertrauliche Vertragsinhalte,
- Secrets,
- private Runtime-/Workspace-Details,
- lizenzpflichtige Normtexte.

## 8. Toolneutralität

Kanonische Fachlogik liegt im Repo:

- `agents/public/`,
- `skills/`,
- `templates/`,
- `playbooks/`,
- `workflows/`,
- `evals/`,
- `governance/`.

Adapter dürfen ausführen, aber keine abweichende Fachlogik erzeugen.

## 9. Reviewpflicht

Neue oder geänderte Artefakte werden gegen `07-ai-governance-agents/evals/quality-gates.md` und den Reviewprozess geprüft.

Mindestnachweis:

- Public-Safety geprüft,
- Claim-Safety geprüft,
- Betriebslogik geprüft,
- Workload geprüft,
- Handoffs geprüft,
- Human Gates sichtbar.
