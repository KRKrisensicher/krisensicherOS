<!-- kso:product-relevance
repo-scope: product
classification: product-governance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; product-safety; release-readiness
-->

# Release-Checkliste

## Zweck

Diese Checkliste bereitet einen öffentlichen Release Candidate von krisensicherOS vor. Sie löst keine Veröffentlichung aus.

Push, Tagging, Release, Public-Schaltung oder externe Kommunikation brauchen immer explizite menschliche Freigabe.

## Release Candidate Gates

### 1. Produkt-Scope

- [ ] README erklärt Zweck, Zielgruppen, KI-Voraussetzung und Grenzen.
- [ ] krisensicherOS ist klar als KI-unterstütztes Governance-Repo positioniert.
- [ ] Es gibt keinen vollwertigen Produktpfad ohne KI-Nutzung.
- [ ] Freigabevorbereitung für KI-Nutzung ist nur Randnotiz / Vorlage, kein alternativer Betriebsmodus.
- [ ] Zentrale Ordner sind vorhanden und verlinkt.
- [ ] Agenten, Skills, Templates, Playbooks, Workflows und Evals sind auffindbar.

### 2. Public-Safety

- [ ] Keine echten Personen-, Kunden- oder Organisationsdaten.
- [ ] Keine Telefonnummern, E-Mail-Adressen, Zugangsdaten oder Secrets.
- [ ] Keine privaten Runtime-, Chat-, Workspace- oder Tool-Metadaten.
- [ ] Keine internen Arbeits-, Review-, Persona-, Briefing-, Roadmap-, Queue- oder Release-Notizen.
- [ ] Beispiele sind klar fiktiv.

### 3. Quellen- und Lizenzgrenzen

- [ ] Öffentliche Quellen werden nur als Referenzanker oder eigene Zusammenfassung genutzt.
- [ ] Keine ISO- oder sonstigen lizenzpflichtigen Normtexte.
- [ ] Keine vertraulichen Vertragsinhalte.
- [ ] Compliance-Register trennt öffentliche, interne, vertrauliche und lizenzpflichtige Inhalte.

### 4. Claim-Safety

- [ ] Keine Rechtsberatung.
- [ ] Keine Datenschutzberatung.
- [ ] Keine Konformitäts-, Zertifizierungs- oder Sicherheitszusage.
- [ ] Keine Managemententscheidung durch Agenten.
- [ ] Human Gates sind sichtbar.

### 5. Artefakt-Gates

- [ ] Agentenprofile erfüllen den öffentlichen Profilstandard und Manifestabgleich.
- [ ] Skills erfüllen `07-ai-governance-agents/standards/skill-standard-v1.0.md`.
- [ ] Templates enthalten Zweck, Trigger, Nutzer, Input, Ablauf, Output, Evidenz, Grenzen und Review.
- [ ] Playbooks enthalten Situation, Ziel, Rollen, Ablauf, Entscheidungen, Eskalation, Outputs, Nachbereitung und Lessons Learned.
- [ ] Workflows enthalten Trigger, Agenten, Skills, Templates, Schritte, Stop-/Freigabepunkte, Outputs und Qualitätsgates.
- [ ] Beispiele erfüllen Public-Safety, Claim-Safety und Fiktions-Gate.

### 6. Technische QS

Mindestkommando im Arbeitsstand:

```bash
GitHub Actions `quality-check` oder lokales Review der relevanten Qualitätsregeln
```

Zusätzlich prüfen:

- Arbeitsbaum und Staging-Status,
- lokale Links,
- Manifest vs. Agentenprofile,
- keine privaten Dateien im Export,
- keine Secret-, PII-, Normtext- oder Runtime-Marker,
- keine gelöschten internen Dateien versehentlich weiter im Produktstand.

### 7. Veröffentlichungsfreigabe

- [ ] Zielrepo / Zielorganisation bestätigt.
- [ ] Release-Name oder Tag bestätigt.
- [ ] QS-Ergebnis geprüft.
- [ ] Diff geprüft.
- [ ] Veröffentlichung separat freigegeben.

## Harte Blocker

Release oder Veröffentlichung blockieren bei:

- fehlender Veröffentlichungsgenehmigung,
- fehlendem Zielrepo oder Zielaccount,
- rechtlich ungeklärter Lizenz-/Disclaimer-Änderung,
- echten oder vertraulichen Daten,
- Secrets,
- lizenzpflichtigen Normtexten,
- überzogenen Compliance- oder Sicherheitsclaims,
- ungeklärtem Scope-Bruch,
- internen Arbeitsartefakten im Produktstand.

## Definition of Done

Ein Release Candidate ist vorbereitet, wenn:

- alle Gates geprüft sind,
- offene Blocker dokumentiert sind,
- keine unbeabsichtigten privaten oder vertraulichen Inhalte enthalten sind,
- QS-Ergebnisse nachvollziehbar sind,
- Veröffentlichung separat freigegeben werden kann.
