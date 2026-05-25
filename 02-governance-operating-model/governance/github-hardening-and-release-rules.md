<!-- kso:product-relevance
repo-scope: product
classification: product-governance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; release-readiness; security-gate
-->

# GitHub-Härtung und Release-Regeln

Dieses Dokument beschreibt die technischen Mindestregeln für das öffentliche GitHub-Repository von krisensicherOS.

## Branches

- `de/main` ist der Default Branch.
- `en/main` ist der gepflegte englische Sprachstand.
- `main` wird nicht verwendet und darf nicht wieder angelegt werden.

## Schutzregeln

Für `de/main` und `en/main` sollen GitHub Branch Protection oder Rulesets aktiv sein:

- Force Pushes verboten.
- Branch Deletion verboten.
- Pull Request oder expliziter Human Review vor Merge.
- Required Status Check: `quality-check`.
- Administrierende Personen sollen Schutzregeln nicht routinemäßig umgehen.

## Qualitätsgate

Vor Veröffentlichung oder Merge müssen mindestens laufen:

- GitHub Actions Workflow `krisensicherOS quality gate`,
- `git diff --check`,
- Prüfung auf Runtime-/Session-Marker,
- Prüfung auf Secrets und unsichere Konformitäts-/Zertifizierungsclaims.

## Identität und Push-Wege

- Pushes nach `git.kr.int` erfolgen ausschließlich mit dem AI Dev Bot.
- Pushes nach GitHub erfolgen ausschließlich mit dem GitHub-Token von `KRKerstan`.
- Commits sollen als `Rico Kerstan` / `KRKerstan` sichtbar sein, nicht als GitLab-, Runtime- oder KI-Kumpel-Identität.

## Security Features

GitHub Security Features sollen aktiviert werden, soweit der Plan und die Berechtigungen es erlauben:

- Dependabot Alerts,
- Dependabot Security Updates,
- Secret Scanning,
- Code Scanning nur leichtgewichtig und passend zum primär Markdown-/YAML-basierten Repo.

## Grenzen

Diese Regeln ersetzen keine fachliche Prüfung. Rechtsauslegung, Datenschutzbewertung, Risikoakzeptanz, externe Kommunikation und Veröffentlichung bleiben menschliche Human Gates.
