<!-- kso:product-relevance
repo-scope: product
classification: setup-guidance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Setup: Microsoft 365 Copilot

Stand: 2026-05-23

## Zweck

Dieses Setup ist für Organisationen, die mit Microsoft 365 arbeiten und Copilot tenantseitig administriert nutzen.

Copilot ist nur geeignet, wenn Berechtigungen, Sensitivity Labels, DLP, SharePoint-/OneDrive-Strukturen und Nutzerfreigaben geprüft sind.

## Geeignet für

- Word-, Excel-, PowerPoint-, Teams-, Outlook- und SharePoint-Arbeit,
- Management-Review-Notizen,
- Strukturierung von Governance-Dokumenten,
- Auditfragen und Maßnahmenlisten,
- Organisationen mit vorhandener M365-Governance.

## Vorbedingungen

- Microsoft 365 Copilot Lizenz oder freigegebene Copilot-Variante,
- Admin-Konfiguration im Microsoft 365 Admin Center,
- zuständige Admin-/Owner-Rolle,
- geprüfte SharePoint-/Teams-Berechtigungen,
- Sensitivity Labels und DLP-Regeln,
- klare Regel, welche krisensicherOS-Artefakte Copilot verarbeiten darf.

## Empfohlene SharePoint-Struktur

```text
krisensicherOS/
├── 01 Orientierung
├── 02 Compliance Register
├── 03 Audit und Evidence
├── 04 Management Review
├── 05 Dokumente in Arbeit
├── 06 Review und Freigabe
└── 99 Archiv
```

## Schritt-für-Schritt

1. Tenant- und Lizenzfreigabe prüfen.
2. Berechtigungen bereinigen: keine unnötig breiten SharePoint-/Teams-Zugriffe.
3. Sensitivity Labels und DLP-Regeln prüfen.
4. krisensicherOS-Arbeitsbibliothek anlegen.
5. Nur freigegebene Artefakte hochladen.
6. Arbeitsregel dokumentieren:

```text
Copilot darf krisensicherOS-Artefakte zusammenfassen, Fragen ableiten und Entwürfe vorbereiten.
Copilot darf keine Rechtsberatung, Datenschutzbewertung, Risikoakzeptanz oder Managemententscheidung treffen.
Vertrauliche Quellen und lizenzpflichtige Normen werden nur als Metadaten oder eigene Zusammenfassungen genutzt.
```

## Beispielprompt für Word

```text
Erstelle aus diesen Notizen einen strukturierten Governance-Dokumententwurf.

Nutze diese Struktur:
1. Zweck
2. Scope und Nicht-Scope
3. Rollen
4. Ablauf / Routine
5. Evidenz
6. Review
7. Grenzen
8. offene Entscheidungen

Markiere Annahmen und Lücken. Erzeuge keine Rechtsberatung oder Konformitätszusage.
```

## Beispielprompt für Teams

```text
Fasse dieses Meeting als Governance-Review-Notiz zusammen.

Output:
- Entscheidungen
- offene Fragen
- Risiken
- Maßnahmen mit Owner und Frist
- benötigte Evidenz
- Punkte für Management Review

Markiere, wo menschliche Freigabe nötig ist.
```

## Tenant-, Rollen- und Szenario-Check

Vor einem M365-Copilot-Pilot klären:

| Prüffeld | Mindestklärung |
| --- | --- |
| Aktivierung | Ist Copilot tenantweit oder gruppenbasiert aktiviert? |
| Szenarien | Welche Apps/Szenarien sind freigegeben: Word, Excel, Teams, Outlook, SharePoint? |
| Pilotgruppe | Welche Benutzergruppen dürfen Copilot für krisensicherOS nutzen? |
| Admin-Rollen | AI Administrator, SharePoint Admin, Compliance Admin, Security Admin oder gleichwertige Rollen beteiligt? |
| Fachlicher Owner | Wer verantwortet die krisensicherOS-Arbeitsbibliothek fachlich? |
| Human Gate | IT-Systemowner, CISO/ISB und bei sensiblen Daten Legal/Datenschutz geben frei. |

## Datenzugriff vor Copilot-Pilot prüfen

Copilot verstärkt bestehende Berechtigungen. Vor Upload oder Prompting prüfen:

- keine ungeprüften vertraulichen Bereiche in Copilot-Reichweite,
- keine breiten Standardgruppen wie „Everyone except external users“ auf Governance-/Evidence-Bibliotheken,
- Gastzugriffe und externe Freigaben prüfen,
- vererbte Berechtigungen und alte Teams/Bibliotheken bereinigen,
- OneDrive-Sharing und persönliche Ablagen nicht als Governance-Ablage nutzen,
- getrennte Bibliothek für freigegebene krisensicherOS-Artefakte verwenden,
- keine produktiven Incident-, Kunden-, Personal- oder Vertragsdaten im Pilot ohne explizite Freigabe.

## Datenklasse und Upload-Gate

Vor Upload in SharePoint muss je Artefakt oder Artefaktgruppe die [`../../templates/ki-nutzungsfreigabe-matrix.md`](../../07-ai-governance-agents/templates/ki-nutzungsfreigabe-matrix.md) oder eine gleichwertige interne Regel geklärt sein.

Stop/Human Gate bei:

- personenbezogenen Daten,
- Secrets,
- vertraulichen Kunden- oder Vertragsdaten,
- lizenzpflichtigen Normtexten,
- unklarer Datenklasse,
- unklarer Berechtigungslage.

M365-spezifische Zusatzfragen vor Upload:

| Prüffeld | Mindestklärung |
| --- | --- |
| Speicherort | Welche SharePoint-Site, Bibliothek oder Teams-Struktur wird genutzt? |
| Gäste / externe Freigaben | Sind Gäste und externe Links geprüft oder deaktiviert? |
| Breite Gruppen | Sind Gruppen wie „Everyone except external users“ ausgeschlossen? |
| Copilot-/Graph-Reichweite | Welche Inhalte kann Copilot über Berechtigungen finden? |
| Retention / Audit Logging | Sind Aufbewahrung und Audit-Logging für den Pilot geklärt? |

## DLP-/Sensitivity-Mindestnachweis

Vor dem Pilot dokumentieren:

| Nachweis | Mindestinhalt |
| --- | --- |
| Label-Konfiguration | Welches Sensitivity Label gilt für die Arbeitsbibliothek oder Artefaktgruppe? |
| Policy Scope | Gilt die DLP-/Compliance-Policy für SharePoint, Teams und OneDrive im Pilot-Scope? |
| Modus | Block-, Warn- oder Audit-Modus geklärt? |
| Nachweisort | Screenshot, Export oder Admin-Notiz im Review-Ordner `06 Review und Freigabe` abgelegt? |
| Owner-Freigabe | IT-Systemowner und fachlicher Owner haben Prüfung im Decision Log bestätigt? |

## Human Gates im M365-Pfad

| Zeitpunkt | Gate |
| --- | --- |
| Vor Upload | Datenklasse, Owner und erlaubte KI-Umgebung geprüft |
| Vor Copilot-Nutzung | Berechtigungen, Sensitivity Labels und DLP geprüft |
| Vor interner Weitergabe | Output fachlich geprüft |
| Vor Managemententscheidung | verantwortliche Rolle entscheidet, nicht Copilot |
| Vor externer Nutzung | explizite Freigabe dokumentiert |

## Praktischer Windows-/Office-Ablauf

1. SharePoint-Site oder Bibliothek durch Owner anlegen lassen.
2. Owner-Gruppe und Bearbeitergruppe getrennt setzen.
3. Vererbte Berechtigungen, externe Freigaben und breite Gruppen prüfen.
4. Sensitivity Label anwenden und DLP-/Policy-Scope dokumentieren.
5. Nur freigegebene Startartefakte hochladen.
6. Eine nicht vertrauliche Testdatei hochladen.
7. Pilot in Word oder Teams mit Beispielprompt testen.
8. Ergebnis in `06 Review und Freigabe` ablegen.
9. Entscheidung, Annahme, Lücke oder Handoff in [`../../templates/decision-log.md`](../../02-governance-operating-model/templates/decision-log.md) oder Review-Notiz übertragen.
