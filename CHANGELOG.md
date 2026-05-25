<!-- kso:product-relevance
repo-scope: product
classification: product-governance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; product-safety; release-readiness
-->

# Changelog

Alle relevanten Änderungen an krisensicherOS werden hier dokumentiert.

Dieses Projekt orientiert sich an einem einfachen, menschenlesbaren Changelog. Vor dem ersten öffentlichen Release können Struktur und Inhalte noch wechseln.

## Unreleased

- ISMS-Umsetzungsleitfaden ergänzt: Module für Nutzung/Grenzen, Scope, Rollen, Risikosteuerung, Schutzmaßnahmen, Kompetenz/Nachweise, Betrieb, Lieferanten, Incidents, Management Review und interne Prüfungen. Produkttext referenziert ISO/IEC 27001 und relevante BSIG-/NIS2-Anker, ohne Normtexte zu übernehmen.
- ISO/IEC-27001-Anforderungslandkarte ergänzt: Abschnittsreferenzen werden in krisensicherOS-Sprache als Routinen, Entscheidungspunkte, Evidenzspuren, Reviews und Human Gates übersetzt; ohne Normtextübernahme.
- Anwendernutzbarkeit geschärft: Getting-Started-Navigation, Anwenderpfade, Artefaktpakete, ISMS-90-Minuten-Durchstich und reduziertes Agentenrouting ergänzt; Mittelstands-CISO-QS durchgeführt und Should-Fixes umgesetzt.
- EU-AI-Act-Readiness-Starter ergänzt: KI-System-Inventar, Vorprüfungsworkflow, Getting-Started-Pfad und Handoff-Logik ohne Rechts- oder Konformitätszusage.

### Added

- Adapter-Navigation unter `adapters/` ergänzt.
- Claude-CLI-Adapter mit Source-of-Truth-Regeln, Claude-CLI-Kommandonutzung, Projektkonfigurationsgrenzen und QS-Gate ergänzt.
- Microsoft-365-Copilot-Adapter für SharePoint Agents und Copilot Studio ergänzt, inklusive Knowledge-Source-Grenzen, Human Gates und SharePoint-Agent-Instructions.
- NIS2-Primärquellenanker, Erwägungsgründe-Auswertung, Vorab-Betroffenheitsfragebogen, Workflow und Agent `nis2-scope-precheck-analyst` ergänzt; Ergebnis erzwingt Rechtsanwalt-/Legal-Prüfung.
- NIS2 Incident-/Melde-Triage-Playbook mit 24h-/72h-/Abschlusslogik sowie Geschäftsleitungs-Schulung und Management-Review-Routine ergänzt.

### Changed

- Produktpositionierung geschärft: krisensicherOS ist ein Repo für KI-unterstützte Security Governance und setzt eine freigegebene KI-Nutzung voraus.
- Setup-Dokumentation auf freigegebene KI-Umgebungen fokussiert: ChatGPT, Microsoft 365 Copilot, Claude Code und lokale KI.
- Freigabepfad als Randnotiz geklärt: Wenn noch keine KI-Freigabe vorliegt, dient die Freigabematrix nur zur Vorbereitung; produktive Nutzung stoppt.
- Interne Arbeits-, Review-, Persona-, Roadmap-, Briefing-, Release- und Queue-Artefakte aus dem Produktrepo entfernt.
- `AGENTS.md` runtime-clean gemacht und auf öffentliche Agentenprofile ausgerichtet.
- README, Getting-Started- und Setup-Dokumentation konsistent auf KI-Freigabe, Human Gates und Produktgrenzen ausgerichtet.
- Lokales QS-Skript `scripts/quality-check.sh` gehärtet: private Runtime-Dateien, interne Arbeitsartefakte, Runtime-Marker, Secret-Indikatoren, lokale Markdown-Links und No-KI-Produktpfade werden geprüft.

### Security / Governance

- Keine Veröffentlichung, kein Push, kein Tag und kein externer Versand ohne explizite Freigabe.
- KI-Nutzung bleibt an Datenklasse, Toolfreigabe, Betriebsverantwortung und Human Gates gebunden.
- Redaction-Tools sind nur Schutzschichten, keine Anonymisierungsgarantie, Datenschutzbewertung oder Compliance-Nachweis.
- Rechtsberatung, Datenschutzberatung, Konformitäts-, Zertifizierungs- und Sicherheitszusagen bleiben ausgeschlossen.
- Lizenzpflichtige Normtexte, vertrauliche Vertragsinhalte, personenbezogene Daten, Kundendaten und Secrets bleiben harte Stop-Punkte.

## v1.0.0-rc.1 — vorbereitet

### Added

- 5-Artefakte-Schnellstart für den kleinsten sinnvollen NIS2-Durchstich.
- 30/60/90-Minuten-Nutzungspfad für den ersten krisensicherOS-Durchstich.
- Setup-Anleitungen für freigegebene KI-Arbeitsumgebungen.
- Öffentliche Agentenprofile unter `agents/public/`.
- Agenten-Rollenmodell und Manifest für Compliance- und Security-Governance-Arbeit.
- Skills für Governance Operating Model, NIS2-Gap-Assessment, ISMS, Audit, Evidence Requests, Corrective Actions, Management Reviews und Tabletop-Übungen.
- Templates für Register, Gaps, Evidenz, Entscheidungen, Risiken, Findings, Maßnahmen, Reviews und KI-Freigabe.
- Workflows für Governance Operating Model, NIS2-Readiness, ISMS, Evidence Management und Audit-/Remediation-Ketten.
- Feste öffentliche Referenzquellenstruktur unter `knowledge/`.
- Compliance-Register-Struktur unter `compliance-register/`.
- Hinweis zur lizenzkonformen Nutzung von ISO-Normen und vergleichbaren Standards.
- Empowerment-first Prompt-Bibliothek.

### Changed

- README auf v1.0-Navigation, Produktgrenzen und KI-unterstützten Einstieg geschärft.
- Produkt-Guardrail `docs/product/was-wir-bewusst-nicht-bauen.md` ergänzt: keine Scheinkonformität, keine Normtext-Nachbildung, keine Template-Masse und keine KI-Magie ohne Human Gates.
- Normen-/KI-Lizenzgrenzen in README und Legal-Doku geschärft: keine Normdokumente in Repo, Prompts, RAG, Embeddings oder KI-Systeme ohne passende Lizenz.
- Mittelstands-Fallstudie zur durchgängigen Kette von Gap über Evidence Request, Corrective Action, Wirksamkeitsprüfung und Managemententscheidung geschärft.

### Security / Governance

- Apache-2.0-Lizenz ergänzt.
- Governance-, Review- und Qualitätsregeln ergänzt.
- Claims, lizenzpflichtige Normtexte, personenbezogene Daten und vertrauliche Inhalte als harte Stop-Punkte definiert.
