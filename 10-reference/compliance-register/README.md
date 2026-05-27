
# Compliance Register

Dieser Ordner ist die Vorlage für ein organisationsspezifisches Compliance-Register.

## Zweck

krisensicherOS enthält fest verdrahtete öffentliche Referenzquellen unter [`../knowledge/`](../knowledge/). Zusätzlich brauchen Organisationen Raum für eigene Vorgaben:

- lizenzpflichtige Normen, z. B. ISO/IEC 27001,
- Kundenverträge,
- Lieferantenanforderungen,
- interne Policies,
- branchenspezifische Vorgaben,
- Auditfeststellungen,
- Versicherungsanforderungen,
- behördliche Auflagen,
- Konzernvorgaben.

Dieses Register liefert dafür eine Struktur, aber keine echten Organisationsdaten.

## Wichtige Regel

In das öffentliche krisensicherOS-Repo gehören keine echten Compliance-Vorgaben einer Organisation.

Nutzer sollen diese Struktur in ihr eigenes privates Arbeitsrepo kopieren und dort befüllen.

## Was darf hier im öffentlichen Repo liegen?

Erlaubt:

- leere Templates,
- fiktive Beispiele,
- Metadaten-Schemata,
- Mapping-Felder,
- Anleitung für Agentenarbeit.

Nicht erlaubt:

- echte Verträge,
- echte Kundenvorgaben,
- echte Auditberichte,
- ISO-Normtexte,
- vertrauliche Kontrollkataloge,
- personenbezogene Daten,
- Zugangsdaten oder interne URLs.

## Empfohlene Registerstruktur beim Nutzer

```text
compliance-register/
├── README.md
├── sources.yaml
├── mappings/
│   ├── requirements-to-controls.yaml
│   ├── requirements-to-evidence.yaml
│   └── requirements-to-routines.yaml
├── notes/
│   └── README.md
└── private-sources/
    └── README.md
```

`private-sources/` gehört in Nutzerumgebungen normalerweise in `.gitignore`, wenn dort vertrauliche oder lizenzpflichtige Inhalte abgelegt werden.

## Registerfelder

Jede Quelle sollte mindestens enthalten:

- `id`
- `title`
- `type`
- `owner`
- `source_location`
- `license_or_confidentiality`
- `applicability`
- `obligations_summary`
- `mapping_status`
- `review_frequency`
- `human_owner`
- `agent_usage_allowed`
- `notes`

## Agentenregel

Agenten dürfen aus Registereinträgen Arbeitsstrukturen ableiten:

- Fragenlisten,
- Mapping-Vorschläge,
- Kontrollbezüge,
- Evidenzbedarfe,
- Review-Routinen,
- Entscheidungsvorlagen.

Agenten dürfen nicht:

- vertrauliche Inhalte veröffentlichen,
- lizenzpflichtige Normtexte reproduzieren,
- verbindliche Rechts- oder Vertragsauslegung behaupten,
- menschliche Freigaben ersetzen.

## Dateien

- [`sources.example.yaml`](sources.example.yaml) — fiktives Beispiel für Registereinträge.
- [`../templates/compliance-source-register.md`](../../08-templates-playbooks/templates/compliance-source-register.md) — Markdown-Template für einzelne Quellen.
