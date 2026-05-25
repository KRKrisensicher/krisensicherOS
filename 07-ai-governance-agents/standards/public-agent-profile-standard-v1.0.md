<!-- kso:product-relevance
repo-scope: product
classification: product-standard
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; product-safety; release-readiness
-->

# Public Agent Profile Standard v1.0

Stand: 2026-05-23

Dieser Standard gilt für alle öffentlichen Zielrepo-Agenten unter `07-ai-governance-agents/agents/public/`.

## Zweck

Öffentliche Agentenprofile müssen mindestens die Qualität der internen krisensicherOS-Projektagenten erreichen, aber für Nutzerorganisationen portabel bleiben.

Sie sollen Organisationen befähigen, eigene Compliance-, Security-Governance-, NIS2-, ISMS- und BCMS-Arbeit agentisch aufzubauen, ohne Verantwortung, Rechtsprüfung oder Managemententscheidungen an Agenten auszulagern.

## Pflichtstruktur

Jedes Profil enthält:

1. YAML-Frontmatter
2. Kurzfassung für Codex CLI
3. Identity & Operating Voice
4. Mandat
5. Primärhebel
6. Wann verwenden
7. Wann nicht verwenden
8. Eingangsdaten
9. Arbeitsmodus
10. Standard-Workflow
11. Typische Deliverables
12. Output-Format
13. Success Metrics
14. Qualitätsgates
15. Mini-Beispiel
16. Anti-Patterns
17. Grenzen und rote Linien
18. Schnittstellen und Handoffs
19. Handoff-Protokoll
20. Beispiel-Prompts
21. Definition of Done

## Zusätzliche Pflicht für öffentliche Nutzeragenten

Öffentliche Agenten müssen zusätzlich sichtbar machen:

- **Human-in-the-loop:** Wer muss prüfen, entscheiden oder freigeben?
- **Passende Skills:** Welche Skills sollte der Agent verwenden, sobald sie vorhanden sind?
- **Output-Artefakte:** Welche Repo-Artefakte entstehen oder werden genutzt?
- **Handoff-Zwangspunkte:** Wann muss an andere Agenten übergeben werden?
- **Portabilität:** Keine tool-spezifischen Befehle im kanonischen Profil.
- **Arbeitsentlastung:** Welche Arbeit wird reduziert oder entscheidungsfähiger gemacht?

## Rote Linien

Kein öffentliches Profil darf:

- Rechtsberatung behaupten,
- Datenschutzberatung behaupten,
- NIS2-Konformität bestätigen,
- ISO-Zertifizierungsfähigkeit bestätigen,
- Managemententscheidungen ersetzen,
- echte Kundendaten oder vertrauliche Vertragsdaten verlangen,
- ISO-Normtexte oder lizenzpflichtige Inhalte reproduzieren,
- Agenten als Ersatz für interne Verantwortliche positionieren.

## Review-Gates

Vor Merge eines öffentlichen Agentenprofils prüfen:

- Frontmatter vollständig,
- Mandat eng und unterscheidbar,
- Nicht-Zuständigkeit klar,
- Inputs/Outputs konkret,
- Success Metrics prüfbar,
- Qualitätsgates vorhanden,
- Mini-Beispiel vorhanden,
- Handoff-Protokoll ausführbar,
- Human-in-the-loop sichtbar,
- keine privaten Workspace-Details,
- keine Tool-Adapter-Logik,
- keine Scheinsicherheit,
- Beitrag zur Befähigung der Nutzerorganisation klar.

## Manifest-Regel

Jedes Profil in `07-ai-governance-agents/agents/public/*.md` muss in `07-ai-governance-agents/agents/manifest.yaml` referenziert sein.

Jeder Manifest-Eintrag muss mindestens enthalten:

- `name`
- `path`
- `family`
- `purpose`
- `use_when`
- `do_not_use_when`
- `handoffs_to`
- `human_review_required_for`
- `adapters`

## Adapter-Regel

Claude Code, Codex, OpenClaw, Hermes oder andere Adapter dürfen öffentliche Profile exportieren oder referenzieren. Sie dürfen keine abweichende Fachlogik enthalten.
