
# Risiken und Grenzen agentischer Governance-Arbeit

## Zweck

Dieses Dokument macht typische Risiken beim Einsatz von Governance-Agenten sichtbar und beschreibt Gegenmaßnahmen für krisensicherOS-Nutzerorganisationen.

## Zentrale Risiken

### 1. Scheinsicherheit

Risiko: Ein Agentenoutput klingt verbindlicher als er ist.

Gegenmaßnahmen:

- Claims explizit begrenzen,
- Annahmen und Lücken sichtbar lassen,
- `agent-quality-and-safety-reviewer` nutzen,
- Management- und Rechtsfragen menschlich prüfen.

### 2. Verantwortungsverschiebung

Risiko: Agenten werden faktisch als Entscheider behandelt.

Gegenmaßnahmen:

- Human Gates verpflichtend nutzen,
- Owner, Reviewer und Entscheider dokumentieren,
- Decision Log führen,
- Agentenoutputs nur als Vorbereitung behandeln.

### 3. Quellenmissbrauch

Risiko: lizenzpflichtige Normtexte, vertrauliche Verträge oder private Inhalte werden kopiert oder falsch genutzt.

Gegenmaßnahmen:

- Quellen nur als Metadaten oder eigene Zusammenfassung eintragen,
- Vertraulichkeit und Lizenzstatus je Registereintrag markieren,
- keine vertraulichen Inhalte in öffentliche Beispiele übernehmen,
- unklare Quellen stoppen und menschlich prüfen.

### 4. Datenschutz- und Personenbezug

Risiko: personenbezogene Daten werden unnötig in Agentenkontexte aufgenommen.

Gegenmaßnahmen:

- Datenminimierung,
- Pseudonymisierung oder fiktive Beispiele,
- Datenschutzschnittstellen an zuständige Rollen eskalieren,
- keine personenbezogenen Daten in öffentliche Artefakte.

### 5. Bürokratisierung

Risiko: Agenten erzeugen mehr Listen, Meetings und Dokumente, ohne Entscheidungen zu verbessern.

Gegenmaßnahmen:

- Workload-Gate nutzen,
- jedes Artefakt braucht Trigger, Owner, Output, Evidenz und Review,
- überflüssige Routinen streichen,
- Managementrelevanz prüfen.

### 6. Tool-Lock-in

Risiko: Fachlogik landet in einem einzelnen Toolprompt oder Adapter.

Gegenmaßnahmen:

- kanonische Artefakte im Repo pflegen,
- Adapter dünn halten,
- Handoffs und Workflows toolneutral beschreiben,
- Profile, Skills und Templates versionieren.

### 7. Veraltete Annahmen

Risiko: Quellen, Risiken oder Organisationsrealität ändern sich, aber Agenten arbeiten mit altem Stand.

Gegenmaßnahmen:

- Review-Frequenzen setzen,
- Registerstatus pflegen,
- Annahmen datieren,
- Evidence Packs regelmäßig prüfen.

## Risikobewertung vor Nutzung

Vor produktiver Nutzung prüfen:

| Frage | Pass | Stop |
| --- | --- | --- |
| Ist der Scope klar? | Scope und Nicht-Scope dokumentiert | unklarer oder zu breiter Scope |
| Sind Daten zulässig? | public-safe oder intern freigegeben | personenbezogen/vertraulich ohne Freigabe |
| Sind Quellen sauber? | Referenz, Metadaten oder eigene Zusammenfassung | Volltext lizenzpflichtiger oder vertraulicher Inhalte |
| Sind Human Gates sichtbar? | Owner/Reviewer/Entscheider benannt | Agent soll entscheiden |
| Ist Output nutzbar? | Routine, Evidenz, Entscheidung klar | nur Dokument ohne Betriebslogik |

## Harte Grenzen

Agenten dürfen nicht:

- Rechtsberatung leisten,
- Datenschutzberatung leisten,
- Managemententscheidungen treffen,
- Risikoakzeptanz erklären,
- Konformitäts-, Zertifizierungs- oder Sicherheitszusagen machen,
- vertrauliche oder lizenzpflichtige Inhalte öffentlich reproduzieren,
- echte Kundendaten in öffentliche Beispiele schreiben,
- externe Kommunikation ohne Freigabe versenden.

## Definition of Done

Risiken und Grenzen sind ausreichend behandelt, wenn:

- relevante Risiken identifiziert sind,
- Gegenmaßnahmen im Workflow sichtbar sind,
- Stop-Punkte klar sind,
- Human Gates benannt sind,
- Qualitätsgates angewendet wurden,
- offene Unsicherheiten nicht geglättet wurden.
