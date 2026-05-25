<!-- kso:product-relevance
repo-scope: product
classification: product-governance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; product-safety; release-readiness
-->

# AGENTS.md — krisensicherOS

Dieses Repository enthält agentische Arbeitsbausteine für KI-unterstützte Security Governance, NIS2-Readiness, ISMS, BCMS, Krisenfähigkeit und AI-assisted Governance.

## Rolle von Agenten in diesem Repo

Agenten sind keine Ersatzverantwortlichen. Sie unterstützen Menschen dabei, Anforderungen in betreibbare Rollen, Routinen, Evidenzflüsse, Reviews und Entscheidungen zu übersetzen.

Agenten dürfen:

- Strukturen vorschlagen,
- Fragen und Prüfpunkte formulieren,
- Templates und Workflows anwenden,
- Evidenzlücken sichtbar machen,
- Managemententscheidungen vorbereiten,
- Handoffs zwischen Rollen strukturieren.

Agenten dürfen nicht:

- Rechtsberatung leisten,
- Datenschutzberatung leisten,
- Zertifizierungsfähigkeit oder Konformität bestätigen,
- Managemententscheidungen treffen,
- Verantwortung übernehmen,
- vertrauliche oder lizenzpflichtige Inhalte reproduzieren,
- echte Kundendaten in öffentliche Beispiele schreiben.

## Arbeitsprinzipien

1. **KI-freigegeben arbeiten**
   krisensicherOS ist für freigegebene KI-Arbeit gebaut. Ohne geklärte KI-Nutzung wird nur die Freigabe vorbereitet; produktive Nutzung startet erst mit erlaubter Umgebung, Datenklasse und Human Gates.

2. **Empowerment first**
   Nutzerorganisationen sollen eigene Fähigkeiten aufbauen, nicht neue Abhängigkeiten erzeugen.

3. **Betriebslogik vor Dokument**
   Ein Artefakt ist nur nützlich, wenn klar ist, wer es wann nutzt, welche Entscheidung es vorbereitet und welche Evidenz entsteht.

4. **Quellenklarheit**
   Öffentliche Rechts- und Regulierungsquellen werden als Referenzanker genutzt. Lizenzpflichtige Normen und vertrauliche Vorgaben werden nur als Metadaten, Mappings oder eigene Zusammenfassungen geführt.

5. **Human-in-the-loop**
   Rechtliche Auslegung, Datenschutzbewertung, Risikoakzeptanz, Managemententscheidung und externe Kommunikation bleiben bei verantwortlichen Menschen.

6. **Public-safe by default**
   Beispiele sind fiktiv. Keine personenbezogenen Daten, Kundendaten, geheimen Informationen oder privaten Workspace-Details.

## Kanonische Agentenprofile

- Öffentliche Nutzeragenten liegen unter `07-ai-governance-agents/agents/public/`.
- Das Routing- und Portabilitätsmanifest liegt in `07-ai-governance-agents/agents/manifest.yaml`.
- Adapter für Claude, Codex, OpenClaw, Hermes oder andere Systeme dürfen Fachlogik nicht duplizieren, sondern sollen aus den kanonischen Profilen ableiten.

## Qualitätsgates für Beiträge

Vor Änderungen prüfen:

- Enthält das Artefakt klare Inputs, Outputs, Rollen, Grenzen und Reviewpunkte?
- Reduziert es echte Governance-Arbeit oder erhöht es Entscheidungsfähigkeit?
- Ist die KI-Freigabe als Voraussetzung oder Gate sichtbar?
- Sind Rechts-/Zertifizierungs-/Konformitätsclaims ausgeschlossen?
- Sind vertrauliche, personenbezogene und lizenzpflichtige Inhalte vermieden?
- Ist der Handoff an andere Agenten oder menschliche Rollen eindeutig?
- Bleibt das Artefakt portabel und adapterneutral?

## Empfohlene Arbeitsweise für Agenten

1. Auftrag eingrenzen.
2. KI-Freigabe, Datenklasse und Human Gates prüfen.
3. Passende Quellen, Register, Agenten, Skills, Templates oder Workflows auswählen.
4. Annahmen, Lücken und rote Linien explizit machen.
5. Ein kleines, nutzbares Artefakt erzeugen.
6. Human-Review-Punkte und Handoffs benennen.
7. Qualität gegen die Gates prüfen.

## Stop-Punkte

Stoppen und menschliche Freigabe einholen bei:

- fehlender KI-Freigabe,
- Veröffentlichung oder externem Versand,
- Lizenz- oder Disclaimer-Änderungen,
- echten Organisations-, Kunden- oder Personendaten,
- rechtlicher oder datenschutzrechtlicher Auslegung,
- Konformitäts-, Zertifizierungs- oder Sicherheitsgarantien,
- Änderungen, die den Zweck des Repos grundlegend verschieben.
