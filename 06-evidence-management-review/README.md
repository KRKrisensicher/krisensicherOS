<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# 06 Evidence & Management Review

Dieses Modul strukturiert Evidenz, Auditfragen, Findings, Remediation, Wirksamkeitsprüfung und Managemententscheidungen.

**Betriebslogik:** Sorgt dafür, dass Nachweise aus echter Governance-Arbeit entstehen und Management Reviews zu Entscheidungen führen.

## Start hier

1. Sammle vorhandene Nachweise mit [`templates/evidence-pack-index.md`](templates/evidence-pack-index.md).
2. Fordere fehlende Nachweise konkret über [`templates/evidence-request-list.md`](templates/evidence-request-list.md) an.
3. Prüfe Controls mit [`templates/control-test-plan.md`](templates/control-test-plan.md) und [`evals/quality-gates.md`](evals/quality-gates.md).
4. Dokumentiere Findings über [`templates/audit-finding-report.md`](templates/audit-finding-report.md) und Maßnahmen über [`templates/corrective-action-plan.md`](templates/corrective-action-plan.md).
5. Bereite Managemententscheidungen mit [`templates/management-review-agenda.md`](templates/management-review-agenda.md) und dem [`Decision Log`](../02-governance-operating-model/templates/decision-log.md) vor.

## Betriebsfluss

`Gap aus 03 → Risiko/Controls aus 04 → Evidence Request → Control Test/Finding → Corrective Action → Wirksamkeitsreview → Management Review → Decision Log`

## Wichtigste Artefakte

- [`workflows/evidence-management-review.yaml`](workflows/evidence-management-review.yaml) — Evidence-Pack- und Review-Workflow.
- [`workflows/audit-evidence-remediation-chain.yaml`](workflows/audit-evidence-remediation-chain.yaml) — Audit-Finding-Remediation-Kette.
- [`playbooks/evidence-pack-prep.md`](playbooks/evidence-pack-prep.md) — Evidence Pack vorbereiten.
- [`playbooks/management-review-prep.md`](playbooks/management-review-prep.md) — Management Review vorbereiten.
- [`playbooks/monthly-security-governance-review.md`](playbooks/monthly-security-governance-review.md) — regelmäßige Governance-Routine.

## Human Gates

Nachweisbewertung, Finding-Schwere, Risikoakzeptanz, Maßnahmenpriorisierung, Fristen, Managemententscheidungen und externe Kommunikation müssen menschlich geprüft und freigegeben werden.

## Typische Outputs

- Evidence Pack,
- Evidence Requests,
- Audit- oder Control-Test-Findings,
- Corrective Actions,
- Wirksamkeitsreview,
- Management-Review-Entscheidungen im Decision Log.
