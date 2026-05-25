<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# krisensicherOS 🛡️

krisensicherOS ist ein offenes, deutschsprachiges Produktrepo für **KI-unterstützte Security Governance**: NIS2-Readiness, ISMS-Basics, Krisenfähigkeit, Evidenzarbeit und Management Reviews als betreibbare Routinen statt Dokumentenfriedhof.

Das Repo enthält öffentliche Agentenprofile, Skills, Templates, Workflows und Playbooks. Es ist für Organisationen gedacht, die KI freigegeben haben oder eine KI-Freigabe gezielt vorbereiten wollen.

**Klarstellung:** Ohne freigegebene KI-Umgebung ist krisensicherOS kein sinnvoller Betriebsmodus. Organisationen können einzelne Vorlagen lesen oder die KI-Freigabe vorbereiten, aber der Produktnutzen entsteht durch KI-unterstützte Arbeit mit Human Gates.

## In 15 Minuten starten

1. Öffne [`docs/getting-started/README.md`](docs/getting-started/README.md) und wähle einen Anwenderpfad.
2. Für den kleinsten NIS2-Start nutze den [`5-Artefakte-Schnellstart`](docs/getting-started/minimaler-nis2-start-in-5-artefakten.md).
3. Wenn du schon weißt, was du brauchst, springe direkt zu den [`Anwenderpfaden`](docs/getting-started/anwenderpfade.md) oder [`Artefaktpaketen`](docs/getting-started/artefaktpakete.md).

## Fünf schnelle Anwenderpfade

- **NIS2 starten:** Scope, Registereintrag, Gap, Evidence Requests und Decision-Log-Handoff.
- **ISMS starten:** Scope, Risiken, Maßnahmenroutinen, Evidence Pack und Reviewtermin.
- **Evidence/Management Review aufbauen:** Nachweise bündeln und Managemententscheidungen vorbereiten.
- **Incident-/Melde-Readiness üben:** Eskalation, Triage und Human Gates trainieren.
- **EU-AI-Act-Readiness starten:** KI-Systeme inventarisieren, Rollenfragen markieren und Legal-/Datenschutz-/Management-Handoffs vorbereiten.

Details stehen in [`docs/getting-started/anwenderpfade.md`](docs/getting-started/anwenderpfade.md).

## Minimaler Startablauf

1. Wähle einen Pfad oder ein Paket aus [`docs/getting-started/`](docs/getting-started/README.md).
2. Prüfe die KI-Freigabe mit [`templates/ki-nutzungsfreigabe-matrix.md`](templates/ki-nutzungsfreigabe-matrix.md).
3. Wähle genau eine freigegebene KI-Umgebung aus [`docs/setup/README.md`](docs/setup/README.md).
4. Nutze höchstens ein Artefaktpaket aus [`docs/getting-started/artefaktpakete.md`](docs/getting-started/artefaktpakete.md).
5. Markiere Human Gates für Management, Risikoakzeptanz, Recht, Datenschutz und externe Kommunikation.

## Mission

krisensicherOS hilft, Compliance-Arbeit in Rollen, Routinen, Nachweise und Managemententscheidungen zu übersetzen.

Produkt-Guardrail: krisensicherOS baut nur Bausteine, die Entscheidungsfähigkeit, Evidenzfluss oder Betriebsroutine erhöhen. Was nur Dokumentenmenge, Berateroptik oder Scheinkonformität erzeugt, bleibt draußen. Siehe [`docs/product/was-wir-bewusst-nicht-bauen.md`](docs/product/was-wir-bewusst-nicht-bauen.md).

## Kernthese

KI kann Dokumentation, Mapping und Nachweisarbeit beschleunigen. Verantwortung bleibt bei den zuständigen Rollen.

Der Nutzen entsteht, wenn Governance im Betrieb sichtbar wird:

- Verantwortung klären,
- Entscheidungen vorbereiten,
- Risiken priorisieren,
- Nachweise aus echter Arbeit erzeugen,
- Management einbinden,
- Krisenfähigkeit üben,
- Sicherheitsroutinen dauerhaft betreiben.

Agenten bereiten vor. Menschen prüfen, entscheiden und verantworten.

## Für wen ist krisensicherOS?

krisensicherOS richtet sich an:

- CISOs,
- ISBs / Informationssicherheitsbeauftragte,
- Sicherheitsverantwortliche,
- Governance-/Risk-/Compliance-Verantwortliche,
- KRITIS-nahe Organisationen,
- regulierte Mittelständler,
- kommunale und öffentliche Einrichtungen.

Voraussetzung ist eine geklärte oder gezielt vorbereitete KI-Nutzung für passende Datenklassen.

## Was krisensicherOS anders macht

Klassische Compliance-Arbeit produziert häufig Dokumente, Listen und Nachweisanfragen. krisensicherOS denkt anders:

> Governance muss betrieben werden, nicht abgeheftet.

Jedes Artefakt in diesem Repository muss beantworten:

1. Wer nutzt es?
2. Wann wird es genutzt?
3. Welche Entscheidung, Routine oder Eskalation unterstützt es?
4. Welche Evidenz entsteht daraus?
5. Wer bleibt verantwortlich?

## Wissensquellen und Compliance-Register

krisensicherOS arbeitet mit zwei Ebenen:

1. **Fest verdrahtete öffentliche Referenzquellen** wie NIS2-Richtlinie, BSIG, EnWG, DSGVO, BDSG und BSI-KritisV.
2. **Nutzereigene Compliance-Register** für Normen, Kundenverträge, interne Policies, Auditfeststellungen und branchenspezifische Vorgaben.

Wichtig: Lizenzpflichtige Normen wie ISO/IEC 27001 werden nicht als Normtext ins Repo übernommen. Das Repo stellt nur Metadaten-, Mapping- und Arbeitsstrukturen bereit. Siehe [`docs/legal/iso-normen-lizenzkonform-nutzen.md`](docs/legal/iso-normen-lizenzkonform-nutzen.md).

Gekaufte ISO-, DIN-, EVS-, BSI- oder sonstige Normdokumente dürfen nicht ohne passende Lizenz in dieses Repo, in Prompts, Agenten, RAG-Systeme, Embeddings, Vektordatenbanken oder sonstige KI-Systeme übernommen werden. Für krisensicherOS gilt: Normen extern lizenzkonform beschaffen und lesen, aber im Repo nur eigene Zusammenfassungen, IDs, Mappings, Entscheidungsfelder und public-safe Arbeitsstrukturen führen.

## v1.0-Scope

Version 1.0 fokussiert auf ein belastbares Grundsystem:

- NIS2-Readiness,
- Security-Governance-Grundsystem,
- ISMS-Basics,
- Incident- und Crisis-Readiness,
- KI-unterstützte Evidenz- und Management-Review-Arbeit,
- EU-AI-Act-Readiness als Inventar-, Vorprüfungs- und Handoff-Starter,
- Agenten und Skills für CISO-/ISB-Routinearbeit.

## Nicht-Ziele

krisensicherOS ist ausdrücklich nicht:

- Rechtsberatung,
- Datenschutzberatung,
- Zertifizierungsgarantie,
- vollständiger ISO-27001-Ersatz,
- manuelles Template-Repo ohne KI-Nutzung,
- Tool zur Verantwortungsautomatisierung,
- Sammlung beliebiger Policy-Vorlagen,
- Scheinsicherheit durch Checklisten,
- Ersatz für Managemententscheidungen, Risikoeigentümer oder Sicherheitsverantwortliche.

## Disclaimer

krisensicherOS stellt Arbeitsmittel, Strukturierungshilfen, Agentenrollen, Skills, Vorlagen und Playbooks bereit. Das Repo baut keine Governance für eine konkrete Organisation vor, sondern liefert Bausteine, die fachlich verantwortliche Personen organisationsspezifisch prüfen, anpassen und freigeben müssen. Die Inhalte ersetzen keine rechtliche Prüfung, keine Datenschutzprüfung, keine Zertifizierungsberatung, keine behördliche Auslegung und keine organisationsspezifische Risikoentscheidung.

Alle Ergebnisse müssen durch fachlich verantwortliche Personen geprüft, angepasst und freigegeben werden. Agenten können vorbereiten, strukturieren, prüfen und beschleunigen — sie übernehmen keine Verantwortung.

## Repo-Struktur v1.0

```text
01-orientation/
02-governance-operating-model/
03-nis2-readiness/
04-isms-basics/
05-incident-crisis-readiness/
06-evidence-management-review/
07-ai-governance-agents/
08-templates-playbooks/
09-implementation-roadmaps/
agents/public/
skills/
templates/
playbooks/
implementierungsleitfaeden/
examples/
docs/
governance/
knowledge/
compliance-register/
workflows/
prompts/
```

## Öffentliche Agenten

Die öffentlichen Agentenprofile liegen unter [`agents/public/`](agents/public/). Sie beschreiben Rollen, Grenzen, Inputs, Outputs, Human Gates und Handoffs für KI-unterstützte Governance-Arbeit.

Starte nicht mit allen Agenten gleichzeitig. Nutze zunächst [`agents/public/anwender-routing.md`](agents/public/anwender-routing.md) und wähle genau die Rolle, die für den nächsten Arbeitsschritt nötig ist.

## Skills, Templates, Workflows und Playbooks

- [`skills/`](skills/) — wiederholbare AgentSkills mit Ablauf, Output und Qualitätskriterien.
- [`templates/`](templates/) — Arbeitsvorlagen für Register, Gaps, Evidenz, Entscheidungen, Risiken und Reviews.
- [`workflows/`](workflows/) — Ablaufmodelle für agentische Governance-Routinen.
- [`playbooks/`](playbooks/) — konkrete Betriebs- und Übungsabläufe.
- [`implementierungsleitfaeden/`](implementierungsleitfaeden/) — praxisnahe Umsetzungshilfen, u. a. für ISMS-Rollen, Routinen, Evidenz und Reviews.

## Setup

krisensicherOS setzt eine freigegebene KI-Nutzung voraus. Die Setup-Dokumente helfen, eine geeignete Umgebung kontrolliert zu nutzen:

- [`docs/setup/README.md`](docs/setup/README.md) — Setup-Auswahl und Einstieg,
- [`docs/setup/chatgpt-lokale-ide.md`](docs/setup/chatgpt-lokale-ide.md) — ChatGPT mit lokaler IDE,
- [`docs/setup/m365-copilot.md`](docs/setup/m365-copilot.md) — Microsoft 365 Copilot,
- [`docs/setup/claude-code.md`](docs/setup/claude-code.md) — Claude Code App, VS Code und CLI,
- [`docs/setup/lokale-ki.md`](docs/setup/lokale-ki.md) — lokale KI ohne Cloud.

Wenn keine KI-Freigabe vorliegt, nutze nur die Freigabematrix als Vorbereitung: [`templates/ki-nutzungsfreigabe-matrix.md`](templates/ki-nutzungsfreigabe-matrix.md).

## Adapter

Tool-spezifische Adapter liegen unter [`adapters/`](adapters/). Sie erklären, wie krisensicherOS in konkreten KI-Oberflächen genutzt wird, ohne die fachliche Source-of-Truth zu duplizieren:

- [`adapters/codex/`](adapters/codex/) — Codex CLI,
- [`adapters/claude-cli/`](adapters/claude-cli/) — Claude Code CLI,
- [`adapters/m365-copilot/`](adapters/m365-copilot/) — Microsoft 365 Copilot, SharePoint Agents und Copilot Studio.

## Schneller Nutzungspfad

Für den ersten belastbaren Durchstich gibt es einen 30/60/90-Minuten-Pfad: [`docs/getting-started/30-60-90-minuten-nutzungspfad.md`](docs/getting-started/30-60-90-minuten-nutzungspfad.md).

Für direkte Einstiegssituationen gibt es zusätzlich vier Anwenderpfade und drei Artefaktpakete:

- [`docs/getting-started/anwenderpfade.md`](docs/getting-started/anwenderpfade.md)
- [`docs/getting-started/artefaktpakete.md`](docs/getting-started/artefaktpakete.md)

Für ISMS gibt es ein kompaktes fiktives Beispiel: [`examples/fiktiver-mittelstand/isms-90-minuten-durchstich.md`](examples/fiktiver-mittelstand/isms-90-minuten-durchstich.md).

Für die NIS2-Vorab-Betroffenheitsprüfung gibt es einen rechtlich begrenzten Fragebogen: [`templates/nis2-vorab-betroffenheitspruefung-fragebogen.md`](templates/nis2-vorab-betroffenheitspruefung-fragebogen.md). Das Ergebnis ist immer nur eine Arbeitsannahme und muss durch Rechtsanwalt/Legal geprüft werden.

Für NIS2-Readiness im Betrieb ergänzen [`playbooks/nis2-incident-melde-triage.md`](playbooks/nis2-incident-melde-triage.md) und [`playbooks/nis2-management-schulung-und-review.md`](playbooks/nis2-management-schulung-und-review.md) die Melde-/Incident-Fähigkeit und Managemententscheidungen.

## Beratungsanschluss ohne platte Werbung

krisensicherOS ist offen nutzbar. Beratung entsteht dort, wo Organisationen nicht noch mehr Dokumente brauchen, sondern beim Aufbau ihres eigenen KI-unterstützten Governance-Betriebssystems Unterstützung benötigen:

- Architektur des Governance Operating Models,
- Priorisierung unter Unsicherheit,
- Verantwortungsdesign,
- Management Alignment,
- Krisen- und Tabletop-Übungen,
- Stakeholder-Konflikte und interne Politik,
- Härtung der agentischen Arbeitsweise.

Das Ziel bleibt Self-Empowerment: Organisationen sollen Security Governance intern wirksam betreiben können.

## Lizenz

krisensicherOS steht unter der Apache License 2.0. Siehe [`LICENSE`](LICENSE).
