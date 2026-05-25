<!-- kso:product-relevance
repo-scope: product
classification: product-governance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; product-safety; release-readiness
-->

# Contributing to krisensicherOS

Danke für dein Interesse an krisensicherOS.

Dieses Repo soll Organisationen befähigen, Security Governance, NIS2-Readiness, ISMS, BCMS und Krisenfähigkeit selbst betreibbar aufzubauen.

## Grundsätze

Beiträge sollen:

- konkrete Governance-Arbeit erleichtern,
- Rollen, Routinen, Evidenz und Entscheidungen klarer machen,
- Nutzerorganisationen befähigen statt abhängig machen,
- public-safe und portabel bleiben,
- keine Rechts- oder Zertifizierungsversprechen erzeugen.

## Gute Beiträge

Geeignet sind zum Beispiel:

- Agentenprofile mit klarer Zuständigkeit und Grenzen,
- Skills mit Inputs, Ablauf, Outputs und Verification,
- Templates mit Betriebslogik,
- Workflows mit Handoffs und Freigabepunkten,
- Evals und Qualitätsgates,
- fiktive Beispiele,
- Dokumentation, die Nutzer zum eigenen Aufbau befähigt.

## Nicht geeignet

Nicht einreichen:

- echte Kundendaten oder personenbezogene Daten,
- vertrauliche Vertragsinhalte,
- ISO- oder andere lizenzpflichtige Normtexte,
- ungeprüfte Rechtsauslegungen,
- Aussagen wie „konform“, „rechtssicher“, „zertifizierungsfähig“ oder ähnliche Garantien,
- generische Policy-Texte ohne Rollen, Trigger, Evidenz und Review,
- tool-spezifische Fachlogik in kanonischen Profilen.

## Artefakt-Checkliste

Vor einem Beitrag bitte prüfen:

- Welches Problem löst das Artefakt?
- Wer nutzt es?
- Wann wird es ausgelöst?
- Welche Inputs braucht es?
- Welcher Ablauf entsteht?
- Welcher Output entsteht?
- Welche Evidenz entsteht?
- Welche Grenzen und Human-Review-Punkte gibt es?
- Welche Agenten, Skills oder Templates sind betroffen?

## Struktur

- Agentenprofile: `07-ai-governance-agents/agents/`
- Öffentliche Zielrepo-Agenten: `07-ai-governance-agents/agents/public/`
- Skills: `07-ai-governance-agents/skills/`
- Templates: `templates/`
- Playbooks: `playbooks/`
- Workflows: `workflows/`
- Qualitätsgates: `06-evidence-management-review/evals/`
- Standards: `docs/standards/`

## Review-Erwartung

Jeder Beitrag sollte mindestens auf Public-Safety, Claim-Safety, Betriebslogik, Portabilität und Empowerment geprüft werden.
