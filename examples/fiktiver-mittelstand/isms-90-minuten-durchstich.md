<!-- kso:product-relevance
repo-scope: product
classification: public-example
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# ISMS-90-Minuten-Durchstich: fiktiver Mittelstand

## Zweck

Dieses Beispiel zeigt kompakt, wie ein Minimum Viable ISMS als Betriebsroutine gestartet werden kann. Es ist vollständig fiktiv und enthält keine echten Organisations-, Kunden-, Personen-, Vertrags-, Incident- oder Systemdaten.

Keine Rechtsberatung, Datenschutzberatung, Konformitätsbewertung, Zertifizierungszusage oder Sicherheitsgarantie.

## Fiktiver Scope

**Organisation:** fiktiver mittelständischer Dienstleister.

**Start-Scope:** digitaler Kundenservice, internes Betriebsteam, Änderungsprozess, Backup-/Restore-Routine und ein zentraler SaaS-Dienstleister.

**Nicht im Start-Scope:** vollständige Unternehmensgruppe, alle Standorte, alle Lieferanten, vollständige Audit- oder Zertifizierungsfähigkeit.

**Template-Verweise:**

- [`../../templates/isms-scope-canvas.md`](../../templates/isms-scope-canvas.md)
- [`../../templates/rollenmatrix.md`](../../templates/rollenmatrix.md)
- [`../../templates/risikoregister-starter.md`](../../templates/risikoregister-starter.md)
- [`../../templates/soa-risk-control-map.md`](../../templates/soa-risk-control-map.md)

## 3 Risiken

| Risiko | Arbeitshypothese | Human Gate |
| --- | --- | --- |
| Restore-Fähigkeit ist nicht belastbar nachweisbar | Restore-Tests existieren informell, aber nicht reviewfähig gebündelt | Management bestätigt Review-Kadenz und akzeptiert/ändert Restrisiko |
| Änderungen am Kernservice sind nicht durchgängig nachvollziehbar | Change-Entscheidungen liegen verteilt in Tickets und Chatverläufen | Service Owner legt verbindliche Nachweisquelle fest |
| SaaS-Abhängigkeit ist operativ kritisch, aber nicht klar gesteuert | Ausfall- und Eskalationspfade sind nicht eindeutig dokumentiert | Einkauf/Service Owner/Legal prüfen Vertrags- und Eskalationsfragen |

## 3 Maßnahmenroutinen

| Routine | Trigger | Owner-Vorschlag | Evidenz |
| --- | --- | --- | --- |
| Monatlicher Restore-Nachweis | Monatsreview oder größere Änderung | Betriebsteamleitung | Testnotiz, Ergebnis, Abweichung, Maßnahme |
| Change-Review für Kernservice | Release oder Notfalländerung | Service Owner | Ticketlink, Freigabe, Rollback-Annahme, Nachtest |
| Lieferanten-Eskalationscheck | Quartalsreview oder Service-Störung | Vendor Owner | Kontakt-/Eskalationskarte, offene Punkte, Entscheidungsbedarf |

**Template-Verweise:**

- [`../../templates/control-evidence-map.md`](../../templates/control-evidence-map.md)
- [`../../templates/corrective-action-plan.md`](../../templates/corrective-action-plan.md)
- [`../../playbooks/monthly-security-governance-review.md`](../../playbooks/monthly-security-governance-review.md)

## 1 Managemententscheidung

**Entscheidungspunkt:** Wird der Start-Scope für die nächsten 90 Tage auf Restore-Fähigkeit, Change-Nachvollziehbarkeit und SaaS-Eskalation begrenzt?

**Optionen:**

- A: Scope begrenzen und monatlich reviewen.
- B: Scope erweitern, aber mehr Owner- und Evidenzaufwand einplanen.
- C: Start verschieben, bis Rollen und KI-Freigabe geklärt sind.

**Human Gate:** Management entscheidet Priorität, Ressourcen und akzeptierten Restrisiko-Rahmen. KI bereitet nur die Vorlage vor.

**Template:** [`../../templates/decision-log.md`](../../templates/decision-log.md)

## 1 Evidence Pack

**Evidence Pack:** `ISMS-Start-Kernservice-Q1`.

Hinweis: Keine echten Ticket-, Chat-, Kunden-, Personen-, Vertrags-, Incident- oder Systemdaten in dieses öffentliche Beispiel übernehmen. In echten Organisationen gehören solche Nachweise nur in freigegebene interne Ablagen.

| Inhalt | Zweck | Quelle |
| --- | --- | --- |
| Scope Canvas | Abgrenzung des Start-Scopes | `isms-scope-canvas.md` |
| Risikoregister-Auszug | drei Start-Risiken und Owner-Fragen | `risikoregister-starter.md` |
| Control-Evidence-Map | Routinen mit Nachweisen verbinden | `control-evidence-map.md` |
| Decision Log | Managemententscheidung dokumentieren | `decision-log.md` |
| Corrective Actions | Abweichungen in Maßnahmen überführen | `corrective-action-plan.md` |

**Template:** [`../../templates/evidence-pack-index.md`](../../templates/evidence-pack-index.md)

## 1 Reviewtermin

**Termin:** erster monatlicher Security-Governance-Review, fiktiv am nächsten Monatsende.

**Agenda:**

1. Scope bleibt passend oder muss angepasst werden.
2. Drei Risiken prüfen: Status, Owner, Evidenz, Entscheidungspunkt.
3. Maßnahmenroutinen bestätigen oder vereinfachen.
4. Evidence Pack auf Lücken prüfen.
5. Managemententscheidung für die nächsten 30 Tage vorbereiten.

**Templates und Playbooks:**

- [`../../templates/management-review-agenda.md`](../../templates/management-review-agenda.md)
- [`../../playbooks/management-review-prep.md`](../../playbooks/management-review-prep.md)
- [`../../implementierungsleitfaeden/isms/09-monitoring-management-review-und-entscheidungen.md`](../../implementierungsleitfaeden/isms/09-monitoring-management-review-und-entscheidungen.md)

## Definition of Done nach 90 Minuten

Fertig ist der Durchstich, wenn Scope, drei Risiken, drei Routinen, ein Decision-Log-Eintrag, ein Evidence-Pack-Index und ein Reviewtermin als Entwurf vorliegen und alle Human Gates markiert sind.
