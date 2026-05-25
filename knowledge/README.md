<!-- kso:product-relevance
repo-scope: product
classification: product-navigation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Wissensquellen

Dieser Ordner beschreibt die fest verdrahtete Referenzschicht von krisensicherOS.

## Zweck

Agenten sollen nicht frei „irgendwelche Compliance-Quellen“ annehmen, sondern mit klar benannten Quellenkategorien arbeiten:

1. **Hardwired Sources** — öffentliche Rechtsquellen und regulatorische Primärquellen, die krisensicherOS als feste Referenzanker kennt.
2. **Compliance Register** — organisationsspezifische Vorgaben, die Nutzer selbst ergänzen, z. B. Normen, Kundenverträge, interne Policies oder branchenspezifische Anforderungen.

## Grundregel

krisensicherOS speichert keine urheberrechtlich geschützten Normtexte, keine vertraulichen Vertragsinhalte und keine personenbezogenen Daten.

Das Repo darf enthalten:

- Quellen-Metadaten,
- offizielle Fundstellen,
- Verweisstrukturen,
- Mapping-Felder,
- Auswertungs- und Prompt-Logik,
- fiktive Beispiele.

Das Repo darf nicht enthalten:

- ISO-Normtexte,
- kostenpflichtige Normauszüge,
- vertrauliche Kundenverträge,
- echte organisationsspezifische Compliance-Vorgaben,
- Rechtsberatung oder verbindliche Auslegung.

## Dateien

- [`hardwired-sources.yaml`](hardwired-sources.yaml) — feste öffentliche Referenzanker.
- [`../compliance-register/README.md`](../compliance-register/README.md) — Anleitung für nutzereigene Compliance-Register.
- [`../docs/legal/iso-normen-lizenzkonform-nutzen.md`](../docs/legal/iso-normen-lizenzkonform-nutzen.md) — Hinweise zur lizenzkonformen Nutzung von ISO-Normen.
