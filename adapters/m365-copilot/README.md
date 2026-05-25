<!-- kso:product-relevance
repo-scope: product
classification: tool-adapter
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Microsoft 365 Copilot Adapter

## Zweck

Dieser Adapter beschreibt, wie krisensicherOS in Microsoft 365 Copilot, SharePoint Agents und Copilot Studio genutzt werden kann.

Er ist kein Ersatz für Tenant-Governance, Berechtigungsprüfung, Sensitivity Labels, DLP oder Human Review.

## Recherchebasis

Stand: 2026-05-25.

Geprüfte öffentliche Microsoft-Dokumentation:

- Microsoft Support: Microsoft 365 Copilot in SharePoint Help & Learning.
- Microsoft Support: Get started with agents in SharePoint.
- Microsoft Learn: Knowledge sources summary — Microsoft Copilot Studio.

Relevante Punkte:

- SharePoint Agents können Fragen zu Site-, Page- und Datei-Inhalten beantworten, auf die der Nutzer Berechtigungen hat.
- Es gibt ready-made Agents pro SharePoint-Site und custom-built Agents mit angepasstem Scope, Identität und Verhalten.
- Zum Interagieren ist eine Microsoft 365 Copilot Lizenz oder ein freigegebener Pay-as-you-go-Dienst für SharePoint Agents nötig.
- Zum Bearbeiten eines SharePoint Agents sind zusätzlich passende Bearbeitungsrechte auf der Site nötig.
- Custom Agents können Knowledge Sources, Sites, Pages, Files und angepasste Prompts nutzen.
- Copilot Studio Knowledge Sources können Enterprise-Daten, Websites und externe Systeme für generative Antworten nutzen.

## Adapter-Prinzip

Microsoft 365 Copilot arbeitet berechtigungs- und tenantnah. Deshalb gilt:

- krisensicherOS-Artefakte nur in geprüfte SharePoint-/Teams-Strukturen hochladen,
- keine ungeprüften Evidence Packs, Kundendaten, Personendaten, Vertragsdetails oder Normtexte in Copilot-Reichweite bringen,
- Berechtigungen vor Prompting bereinigen,
- Copilot-Outputs immer in Decision Logs, Review-Notizen oder Templates zurückführen,
- Entscheidungen bleiben bei verantwortlichen Menschen.

## Empfohlene M365-Struktur

```text
krisensicherOS/
├── 01 Orientierung
├── 02 Freigegebene Produktartefakte
├── 03 Compliance Register
├── 04 Audit und Evidence
├── 05 Management Review
├── 06 Review und Freigabe
└── 99 Archiv
```

Nur `02 Freigegebene Produktartefakte` wird als Wissensbasis für einen ersten Copilot-/SharePoint-Agent-Pilot genutzt.

## Vorbedingungen

Vor Nutzung klären:

- Microsoft 365 Copilot Lizenz oder freigegebener SharePoint-Agent-Dienst,
- Tenant-Freigabe durch zuständige Admin-/Owner-Rollen,
- Site Owner und fachlicher Owner,
- geprüfte SharePoint-/Teams-Berechtigungen,
- keine breiten Gruppen wie „Everyone except external users“ auf sensiblen Bibliotheken,
- Sensitivity Labels und DLP-/Retention-/Audit-Regeln,
- Datenklasse je Artefaktgruppe,
- Human Gates für Output-Prüfung.

## Geeignete Produktartefakte für den Pilot

Geeignet:

- `README.md`,
- `docs/getting-started/*`,
- `docs/setup/README.md`,
- `agents/public/role-model.md`,
- ausgewählte `templates/*.md`,
- ausgewählte `playbooks/*.md`,
- `governance/disclaimer.md`,
- `governance/quality-rules.md`.

Nicht geeignet für den ersten Copilot-Pilot:

- echte Evidence Packs,
- vertrauliche Kundendaten,
- personenbezogene Daten,
- Vertragsdetails,
- Secrets,
- lizenzpflichtige Normtexte,
- Workrepo-Artefakte mit `repo-scope: workrepo`.

## SharePoint Agent Setup

1. Freigegebene SharePoint-Site oder Bibliothek anlegen.
2. Berechtigungen auf Pilotgruppe begrenzen.
3. Sensitivity Label und DLP-/Audit-Regeln dokumentieren.
4. Nur freigegebene krisensicherOS-Produktartefakte hochladen.
5. Ready-made Agent nur nutzen, wenn Site-Scope sauber ist.
6. Für produktiven Pilot besser Custom Agent mit begrenzten Knowledge Sources anlegen.
7. Agent Purpose und Prompts aus `sharepoint-agent-instructions.md` übernehmen.
8. Testfragen nur mit fiktiven oder freigegebenen Inhalten stellen.
9. Antworten in `templates/decision-log.md`, `templates/evidence-request-list.md` oder Review-Notiz zurückführen.

## Copilot Studio Setup

Wenn Copilot Studio genutzt wird:

- Knowledge Sources auf freigegebene SharePoint-Bibliotheken oder geprüfte Websites begrenzen,
- generative Answers nur mit klarer Zweckbeschreibung nutzen,
- Authentifizierung und Zugriff über Microsoft-/Tenant-Regeln absichern,
- keine vertraulichen Quellen als globale Knowledge Source ohne fachliche Freigabe,
- Testfälle mit fiktiven Beispielen dokumentieren.

## Standardprompt für M365 Copilot

```text
Du unterstützt mich mit krisensicherOS.
Nutze nur die freigegebenen Dateien in dieser SharePoint-Bibliothek.
Erzeuge keine Rechtsberatung, Datenschutzberatung, Konformitäts-, Zertifizierungs- oder Sicherheitszusage.
Triff keine Managemententscheidung und akzeptiere kein Risiko.
Markiere Annahmen, Lücken, Evidenzbedarf und Human Gates.
Wenn Inhalte personenbezogen, vertraulich, kundenspezifisch, vertraglich, lizenzpflichtig oder ein Secret sein könnten: stoppe und fordere Freigabe.

Aufgabe:
<konkrete Aufgabe>

Output:
1. Kurzbefund.
2. Benötigte Evidenz.
3. Offene Entscheidungen.
4. Human Gates.
5. Geeignetes krisensicherOS-Template.
```

## Human Gates

| Zeitpunkt | Gate |
| --- | --- |
| Vor Upload | Datenklasse, Owner, Sensitivity Label und erlaubte KI-Umgebung geprüft |
| Vor Agent-Erstellung | Knowledge Sources und Berechtigungen geprüft |
| Vor Nutzung mit internen Daten | DLP, Audit Logging, Retention und Zugriff geprüft |
| Vor Weitergabe | Output fachlich geprüft |
| Vor Entscheidung | Management oder zuständige Rolle entscheidet |
| Vor externer Kommunikation | explizite Freigabe dokumentiert |

## Adapter-Qualitätsgate

Vor Abschluss eines M365-Copilot-Arbeitsschritts prüfen:

- Wurden nur `repo-scope: product`-Artefakte genutzt?
- Sind SharePoint-/Teams-Berechtigungen begrenzt?
- Sind Sensitivity Labels und DLP-/Audit-Regeln geklärt?
- Sind keine Workrepo-, Kunden-, Personen-, Vertrags-, Incident-, System- oder Secret-Daten eingebracht worden?
- Sind keine lizenzpflichtigen Normtexte verarbeitet worden?
- Sind Annahmen, Lücken, Evidenzbedarf und Human Gates markiert?
- Wurde Output in ein krisensicherOS-Template oder Review-Artefakt überführt?
