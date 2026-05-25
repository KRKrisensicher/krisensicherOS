<!-- kso:product-relevance
repo-scope: product
classification: product-governance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; reusable-governance-asset; human-gate-aware
-->

# Produktrelevanz-Prozess

## Grundregel

Default ist **Arbeitsrepo**.

Eine Datei darf nur im Produktrepo bleiben, wenn sie explizit als produktrelevant gekennzeichnet ist und die Kriterien unten erfüllt. Beim Anlegen oder Ändern einer Datei muss diese Einstufung erneut geprüft werden.

Arbeitsrepo-Dateien werden nicht gelöscht, nur weil sie nicht produktrelevant sind. Sie werden mit `repo-scope: workrepo` gekennzeichnet und in ein eigenes Arbeitsrepo auf `git.kr.int` überführt. Das Produktrepo enthält später nur `repo-scope: product`-Artefakte.

## Pflicht-Tag

Jede Datei im Arbeitsstand muss im Dateiinhalt einen `kso:product-relevance`-Tag tragen.

- `repo-scope: product` bedeutet: darf in den Produktrepo-Export.
- `repo-scope: workrepo` bedeutet: bleibt im Arbeitsrepo, darf nicht in den Produktrepo-Export.

Mindestfelder:

```text
kso:product-relevance
repo-scope: product | workrepo
classification: <Artefaktklasse>
decision: keep | move-to-workrepo | remove
review-required-on-change: true
criteria: <erfüllte Kriterien>
```

Für Markdown wird ein HTML-Kommentar genutzt. Für YAML, Shell und Gitignore werden Kommentarzeilen genutzt. Für Dateien ohne Kommentarformat darf der Tag am Ende als Klartext-Metadatenblock stehen.

## Entscheidungskriterien für `repo-scope: product`

Eine Datei ist nur produktrelevant, wenn sie mindestens diese Kriterien erfüllt:

1. **Public-safe**
   - keine internen Workspace-, Runtime-, Chat-, Token-, Personen-, Kunden- oder Organisationsdaten,
   - keine privaten Arbeitsnotizen oder Reviewspuren.

2. **Produktnutzen**
   - hilft Nutzerorganisationen direkt bei KI-unterstützter Security Governance,
   - oder ist nötig, um das Produktrepo nutzbar, prüfbar, sicher oder portabel zu halten.

3. **AI-assisted Governance Fit**
   - unterstützt Agenten, Skills, Templates, Workflows, Playbooks, Governance-Routinen, Human Gates oder Setup freigegebener KI-Nutzung,
   - ist kein manueller Alternativpfad ohne KI-Produktbezug.

4. **Wiederverwendbarkeit**
   - ist generisch genug für öffentliche Nutzung,
   - nutzt fiktive Beispiele,
   - enthält keine echten Kundenspezifika.

5. **Claim-Safety**
   - keine Rechtsberatung,
   - keine Datenschutzberatung,
   - keine Konformitäts-, Zertifizierungs- oder Sicherheitszusage,
   - keine Managemententscheidung durch Agenten.

6. **Lizenz- und Quellenklarheit**
   - keine lizenzpflichtigen Normtexte,
   - keine vertraulichen Vertragsinhalte,
   - öffentliche Quellen nur als Referenzanker oder eigene Zusammenfassung.

7. **Human Gates**
   - menschliche Prüfung, Freigabe, Risikoakzeptanz und externe Kommunikation bleiben sichtbar bei verantwortlichen Rollen.

## Typische Entscheidungen

### `repo-scope: product`

Beispiele:

- README, Setup- und Getting-Started-Dokumente,
- öffentliche Agentenprofile,
- Skills,
- Templates,
- Workflows,
- Playbooks,
- Qualitäts- und Governance-Regeln,
- fiktive Beispiele,
- QS-Skripte, die den Produktstand schützen.

### `repo-scope: workrepo`

Beispiele:

- interne Brainstormings,
- persönliche Notizen,
- Agenten-Session-Memory,
- Review- und QS-Zwischenberichte,
- Roadmaps, die nicht für Nutzer bestimmt sind,
- Mirror-/Release-Technik,
- lokale Probe- und Reparaturskripte,
- Dateien mit privaten Workspace-Details.

Diese Dateien dürfen nicht in den Produktrepo-Export. Sie bleiben bis zur Repo-Trennung erhalten und werden in das eigene Arbeitsrepo auf `git.kr.int` übernommen.

## Pflichtprüfung beim Anlegen oder Ändern

Vor Abschluss jeder Änderung:

1. Hat jede neue oder geänderte Datei einen `kso:product-relevance`-Tag?
2. Ist `repo-scope: product` wirklich begründet oder gehört die Datei ins Arbeitsrepo?
3. Wäre eine Produktdatei auch ohne internen Projektkontext für Nutzer verständlich?
4. Enthält eine Produktdatei keine privaten, vertraulichen, personenbezogenen oder lizenzpflichtigen Inhalte?
5. Unterstützt eine Produktdatei KI-unterstützte Governance und Human Gates?
6. Bleiben `repo-scope: workrepo`-Dateien vom Produktrepo-Export ausgeschlossen?
7. Läuft das GitHub Actions Quality Gate ohne Tag- oder Linkfehler?

## Eskalation

Wenn eine Datei nicht eindeutig produktrelevant ist, bleibt sie im Arbeitsrepo. Produktaufnahme erfolgt erst nach expliziter Begründung und Prüfung.

## Zielbild Repo-Trennung

- Produktrepo auf `git.kr.int`: nur produktrelevante Artefakte mit `repo-scope: product`.
- Arbeitsrepo auf `git.kr.int`: interne Arbeitsstände, Reviews, Roadmaps, Release-Technik und Provenienz mit `repo-scope: workrepo`.
- GitHub-Veröffentlichung erfolgt ausschließlich aus dem geprüften Produktrepo-Stand, nicht aus dem Arbeitsrepo.

Vorgeschlagener Arbeitsrepo-Name: `krisensicher/krisensicher-os-workrepo`.

Vor Anlage des Arbeitsrepos klären:

1. Zielnamespace auf `git.kr.int`.
2. Repo-Name.
3. Sichtbarkeit und Berechtigungen.
4. Ob Historie vollständig übernommen oder initial als neuer Arbeitsrepo-Snapshot gestartet wird.
5. Welche Remotes lokal gesetzt werden.
