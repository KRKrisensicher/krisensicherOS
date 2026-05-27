
# ISO-Normen lizenzkonform mit krisensicherOS nutzen

## Zweck

Viele Organisationen möchten krisensicherOS mit ISO/IEC 27001 oder anderen ISO-Normen verbinden. Das ist sinnvoll, aber lizenzrechtlich sensibel.

Dieser Leitfaden beschreibt, wie Nutzer ISO-Normen mit krisensicherOS verwenden können, ohne Normtexte unzulässig in das Repo zu kopieren.

## Grundsatz

ISO-Normen sind in der Regel urheberrechtlich geschützt und lizenzpflichtig.

krisensicherOS darf deshalb im öffentlichen Repo **keine ISO-Normtexte, Kontrolltexte, Tabellen, Anhänge oder längeren Auszüge** enthalten, sofern keine ausdrückliche Lizenz dafür besteht.

## Was erlaubt ist

Im Repo sind typischerweise zulässig:

- Verweise auf Normen als Metadaten,
- eigene Struktur- und Mapping-Felder,
- eigene Zusammenfassungen ohne Reproduktion geschützter Formulierungen,
- Fragen, die Nutzer beim Arbeiten mit ihrer lizenzierten Norm unterstützen,
- Templates für Mapping und Evidenz,
- Hinweise auf offizielle Bezugsquellen,
- fiktive Beispiele ohne Normtextübernahme.

Beispiel:

```yaml
source_id: iso-iec-27001-reference
source_type: standard-reference
source_location: interne lizenzierte Normbibliothek
agent_usage: metadata_only
```

## Was nicht ins öffentliche Repo gehört

Nicht aufnehmen:

- kopierte ISO-Kapitel,
- kopierte Annex-A-Control-Texte,
- Tabellen aus Normen,
- Screenshots oder Scans aus Normdokumenten,
- gekaufte PDF-Dateien,
- aus Kundenaudits übernommene Normauszüge,
- paraphrasierte Passagen, die faktisch den Normtext ersetzen,
- Normtexte in Prompts, Agenten-Kontexten, RAG-Systemen, Embeddings, Vektordatenbanken, Trainingsdaten oder sonstigen KI-Systemen ohne ausdrückliche passende Lizenz.

## Empfohlenes Vorgehen für Nutzer

1. **Norm lizenzkonform beschaffen**
   - Über ISO, DIN, Beuth/DIN Media oder eine andere zulässige Quelle.

2. **Norm nicht ins öffentliche Repo kopieren**
   - Auch nicht in `examples/`, `fixtures/`, Prompts oder Trainingsdaten.

3. **Privaten Ablageort dokumentieren**
   - Im eigenen, nicht öffentlichen Compliance-Register nur den Ablageort referenzieren.

4. **Eigene Mapping-Struktur nutzen**
   - Anforderungen werden intern auf Controls, Evidenz, Rollen und Routinen gemappt.

5. **Agenten nur mit erlaubtem Kontext versorgen**
   - Metadaten, eigene Zusammenfassungen und organisationsspezifische Mappings nutzen.
   - Keine vollständigen Normtexte in Agentenprompts kopieren, wenn die Lizenz das nicht ausdrücklich erlaubt.
   - Keine Normdokumente in RAG, Embeddings, Vektordatenbanken, Trainingsdaten, Assistants, Copilots oder lokale KI-Systeme laden, solange keine explizite KI-, Text-Mining-, Mehrnutzer- oder Plattformlizenz vorliegt.

6. **Menschliche Prüfung sicherstellen**
   - Agenten dürfen Mappings vorbereiten, aber nicht verbindlich bestätigen.

## Empfohlene Repo-Struktur beim Nutzer

```text
compliance-register/
├── sources.yaml
├── mappings/
│   ├── iso27001-to-controls.yaml
│   ├── iso27001-to-evidence.yaml
│   └── iso27001-to-routines.yaml
└── private-sources/          # normalerweise gitignored
    └── README.md             # keine Normtexte im öffentlichen Repo
```

## Beispiel für einen lizenzkonformen Registereintrag

```yaml
id: iso-iec-27001-reference
title: ISO/IEC 27001
type: standard-reference
source_location: Interne lizenzierte Normbibliothek
license_or_confidentiality: Lizenzpflichtig; keine Normtexte ins Repo kopieren
agent_usage_allowed: metadata_only
human_owner: ISB/CISO
mapping_status: in_progress
```

## Agentenregel

Agenten sollen bei ISO-Bezug immer prüfen:

- Wird hier Normtext reproduziert oder faktisch ersetzt?
- Ist der Inhalt nur Metadaten, eigene Zusammenfassung oder Mapping?
- Ist die Quelle lizenzpflichtig?
- Ist KI-, RAG-, Embedding-, Prompt- oder Text-Mining-Nutzung ausdrücklich lizenziert?
- Muss ein Mensch die Interpretation freigeben?

Wenn Zweifel bestehen, muss der Agent stoppen und menschliche Prüfung verlangen.

## Anbieter- und Lizenzhinweis

Günstige Bezugsquellen, Einzelplatz-, Mehrnutzer-, Intranet-, Abo- oder Standardsportalmodelle können sinnvoll sein. Der Kauf einer Norm bedeutet aber nicht automatisch, dass die Inhalte in ein Git-Repo, ein internes Agentensystem oder eine KI-Pipeline übernommen werden dürfen.

Für jede Organisation ist vor Nutzung zu klären:

1. Wer darf das Dokument lesen?
2. Darf es intern auf Server, Intranet oder Dokumentenmanagementsystem abgelegt werden?
3. Dürfen Inhalte in Prompts, RAG, Embeddings oder andere KI-Systeme eingegeben werden?
4. Sind abgeleitete Mappings ohne Normtext erlaubt?
5. Gilt die Nutzung nur für die eigene Organisation oder auch für Beratungs-/Kundenkontexte?

## Keine Rechtsberatung

Dieser Leitfaden ist keine Rechtsberatung. Organisationen müssen ihre konkrete Lizenzlage, Vertragsbedingungen und Nutzungsrechte selbst prüfen oder rechtlich prüfen lassen.
