<!-- kso:product-relevance
repo-scope: product
classification: product-standard
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; product-safety; release-readiness
-->

# Codex-optimierter Agentenprofil-Standard

Stand: 2026-05-23

Dieser Standard beschreibt, wie Agentenprofile in krisensicherOS geschrieben werden, damit sie für Codex CLI und vergleichbare coding agents gut nutzbar sind.

## Ziel

Ein Agentenprofil soll nicht nur eine Rolle beschreiben, sondern Codex eine präzise Arbeitsanweisung geben:

- wann der Agent relevant ist,
- welche Inputs erwartet werden,
- wie gearbeitet wird,
- welche Outputs entstehen,
- welche Qualitätsgates vor Abschluss gelten,
- welche Grenzen nicht überschritten werden dürfen,
- an wen Ergebnisse übergeben werden.

## Profilstruktur

Jedes Profil nutzt diese Abschnitte:

1. `Kurzfassung für Codex CLI`
2. `Vault-Herkunft und Transformationslogik`
3. `Mandat`
4. `Primärhebel`
5. `Wann verwenden`
6. `Wann nicht verwenden`
7. `Eingangsdaten`
8. `Arbeitsmodus`
9. `Standard-Workflow`
10. `Typische Deliverables`
11. `Output-Format`
12. `Qualitätsgates`
13. `Grenzen und rote Linien`
14. `Schnittstellen und Handoffs`
15. `Beispiel-Prompts`
16. `Definition of Done`

## Codex-Optimierung

Codex CLI profitiert von expliziten, überprüfbaren Regeln. Deshalb gilt:

- Schreibe konkrete Handlungsanweisungen statt abstrakter Rollenlyrik.
- Nutze Checklisten, Stop-Regeln und Output-Verträge.
- Markiere Unsicherheiten und fehlende Inputs klar.
- Leite keine externen oder rechtlichen Zusicherungen ab.
- Beende Arbeit erst nach einem kurzen Qualitätscheck.
- Vermeide Tool- oder Runtime-spezifische Annahmen, sofern sie nicht im Adapter stehen.

## Mindest-Qualitätsgate für jedes Agentenergebnis

Jedes Ergebnis muss mindestens beantworten:

- Beobachtung: Was ist der relevante Befund?
- Risiko/Chance: Warum ist das wichtig?
- Empfehlung: Was sollte getan werden?
- Nächster Schritt: Was ist konkret als Nächstes zu tun?
- Grenze: Was kann dieses Ergebnis nicht leisten?

## Öffentliche Sicherheit

Agentenprofile dürfen keine privaten Workspace-Informationen, Tokens, Kundendaten oder personenbezogenen Beispiele enthalten. Beispiele müssen fiktiv sein.
