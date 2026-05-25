<!-- kso:product-relevance
repo-scope: product
classification: setup-guidance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Praxisanleitung: KI-Setups für krisensicherOS

Stand: 2026-05-23

## Zweck

Diese Anleitung ist die zusammenfassende Übersicht für die krisensicherOS-Setups. Für die praktische Nutzung gibt es einzelne Setup-Dokumente:

- [`README.md`](README.md) — Einstieg und Setup-Auswahl,
- [`chatgpt-lokale-ide.md`](chatgpt-lokale-ide.md) — ChatGPT mit lokaler IDE,
- [`m365-copilot.md`](m365-copilot.md) — Microsoft 365 Copilot,
- [`claude-code.md`](claude-code.md) — Claude Code App, VS Code und CLI,
- [`lokale-ki.md`](lokale-ki.md) — lokale KI ohne Cloud.

krisensicherOS setzt eine freigegebene KI-Nutzung voraus. Ohne KI-Freigabe wird nur die Freigabe vorbereitet; produktive Nutzung startet erst mit einer erlaubten KI-Umgebung und klaren Human Gates.

Die Setup-Beschreibungen sind primär Windows-first formuliert. macOS/Linux werden nur dort erwähnt, wo sie für Entwickler- oder lokale KI-Setups relevant sind.

Ziel ist nicht „KI einschalten und hoffen“, sondern eine kontrollierte Arbeitsweise mit Datenregeln, Human Gates, Prompts und überprüfbaren Artefakten.

## Wenn du nur 15 Minuten hast: sichere Setup-Entscheidung

| Situation | Sicherer Start | Nächster Schritt |
| --- | --- | --- |
| Keine KI-Freigabe | Stop | `templates/ki-nutzungsfreigabe-matrix.md` als Freigabevorlage nutzen; keine produktive Nutzung |
| Freigegebene Cloud-KI vorhanden | KI nur mit erlaubten Datenklassen | `templates/ki-nutzungsfreigabe-matrix.md` ausfüllen |
| Microsoft 365 Copilot ist tenantseitig freigegeben | M365-Pfad mit SharePoint-/Berechtigungsprüfung | Datenzugriff, Sensitivity Labels und Owner klären |
| Lokale KI geplant | Pilot mit Betriebsowner | Betriebscheckliste für lokale KI und Redaction-Tools ausfüllen |
| Vertrauliche, personenbezogene oder lizenzpflichtige Inhalte | Stop / Handoff | Legal-/Datenschutz-Handoff; keine Verarbeitung in ungeklärten KI-Umgebungen |

## Pflicht-Gate vor jeder KI-Nutzung

Bevor ChatGPT, Microsoft 365 Copilot, Claude Code, lokale KI oder Redaction-Tools genutzt werden, muss die KI-Nutzung freigegeben sein.

Nutze dafür `templates/ki-nutzungsfreigabe-matrix.md` oder eine gleichwertige organisationsinterne Regel.

Mindestentscheidung:

- Datenklasse: öffentlich, intern, vertraulich, personenbezogen oder lizenzpflichtig,
- erlaubte KI-Umgebung: freigegebene Cloud-KI, M365 Copilot, lokale KI oder isolierte Umgebung,
- verbotene Inhalte: Personendaten, Secrets, Kundendaten, Vertragsdetails, lizenzpflichtige Normtexte,
- optionaler Redaction-Schritt, z. B. OpenAI Privacy Filter oder vergleichbare Werkzeuge,
- Human Gate für Review und Freigabe.

Redaction ist keine Anonymisierungsgarantie und ersetzt keine Datenschutzbewertung.

## Recherchebasis

Für diese Anleitung wurden öffentlich verfügbare Hersteller- und Projektdokumentationen geprüft:

- OpenAI Help: ChatGPT Work with Apps / VS Code Extension — ChatGPT kann über die macOS-App mit unterstützten Apps und VS Code arbeiten; VS Code nutzt die `openai.chatgpt` Extension.
- Microsoft Learn: Microsoft 365 Copilot Admin/Scenarios — Copilot-Szenarien werden über Microsoft 365 Admin Center / Copilot Control System und Rollen wie AI Administrator gesteuert.
- Claude Code Docs: VS Code Extension — Claude Code bietet eine VS-Code-Extension und CLI, mit Plan Review, Diffs, Dateikontext und Projektarbeit.
- Ollama — lokales Ausführen offener Modelle, optional Cloud-Erweiterung.
- LM Studio — lokale Modelle, GUI, OpenAI-kompatible API, SDK/CLI.
- Jan — freies Open-Source-Desktop-Tool als lokaler ChatGPT-Ersatz.
- GPT4All — lokaler/private Chatbot-Fokus.
- Open WebUI — self-hosted, offline-fähige Weboberfläche, unterstützt Ollama und OpenAI-kompatible APIs.
- Continue — KI-gestützte Entwicklungs-/Review-Workflows und Checks im Repo-Kontext.

## Grundentscheidung: welches Setup für wen?

| Setup | Geeignet für | Nicht ideal für |
| --- | --- | --- |
| ChatGPT + lokale IDE | Einzelpersonen, schnelle Dokument-/Codearbeit, niedrige Einstiegshürde | streng vertrauliche Daten ohne Freigaberegel |
| Microsoft 365 Copilot | Organisationen mit M365, Word/Excel/Teams/SharePoint-Arbeit | Repo-nahe Agentenarbeit ohne M365-Governance |
| Claude Code | Repo-Arbeit, strukturierte Änderungen, Coding-Agenten, Docs-as-Code | reine Office-Nutzer ohne Git/IDE |
| Lokale KI mit LM Studio/Jan/GPT4All | einfache lokale Chat-/Dokumentenarbeit, Datenschutzsensibilität | komplexe Repo-Agenten ohne zusätzliche Tools |
| Ollama + Open WebUI | lokaler Teambetrieb, API, RAG, Self-hosting | Nutzer ohne technische Betreuung |
| Ollama/LM Studio + Continue | lokale oder hybride Entwickler-Workflows | reine Office-Prozesse |

## Gemeinsame Sicherheitsregeln

Vor jedem Setup festlegen:

1. Datenklasse: öffentlich, intern, vertraulich, personenbezogen oder lizenzpflichtig.
2. Erlaubte KI: Cloud, lokal, M365-Tenant oder Projektkonto.
3. Output-Grenzen: keine Rechtsberatung, keine Datenschutzberatung, keine Konformitäts- oder Zertifizierungszusage.
4. Human Gates: zuständige Person für Prüfung, Entscheidung und Freigabe.
5. Ablage: Ort für Dokumente, Register, Evidence Packs und Decision Logs.
6. Normtexte: lizenzpflichtige Inhalte nur als Metadaten, Referenzen oder eigene Zusammenfassungen.


## Setup A: ChatGPT mit lokaler IDE

### Für wen?

Für Nutzer, die ohne komplexe lokale KI-Infrastruktur starten wollen und krisensicherOS als Repo, Dokumentenbasis oder Promptbibliothek nutzen.

### Minimaler Werkzeugkasten

- ChatGPT Account passend zur Organisationsfreigabe.
- ChatGPT Desktop App, wenn App-/IDE-Integration genutzt werden soll.
- VS Code oder kompatibler Editor.
- Git.
- Lokale Kopie des krisensicherOS-Repos.

### Schritt-für-Schritt

1. **Repo lokal ablegen**

   ```bash
   git clone <repo-url> krisensicherOS
   cd krisensicherOS
   ```

2. **VS Code öffnen**

   ```bash
   code .
   ```

3. **ChatGPT-Integration einrichten**

   - In VS Code Extensions öffnen.
   - Nach `ChatGPT` bzw. `openai.chatgpt` suchen.
   - Extension installieren, sofern in der Organisation freigegeben.
   - Bei VS-Code-Forks ggf. VSIX gemäß OpenAI-Hilfe installieren.

4. **Arbeitsordner prüfen**

   Relevante Startdateien:

   - `README.md`
   - `07-ai-governance-agents/README.md`
   - `agents/public/role-model.md`
   - `skills/README.md`
   - `templates/README.md`
   - `workflows/README.md`
   - `governance/review-process.md`

5. **Ersten sicheren Prompt verwenden**

   ```text
   Du unterstützt mich mit krisensicherOS.

   Kontext:
   - Ich arbeite in einem lokalen Repo.
   - Nutze nur die Dateien, die ich dir gebe oder im Projektkontext öffne.
   - Erzeuge keine Rechtsberatung, Datenschutzberatung, Konformitäts- oder Zertifizierungszusage.
   - Markiere Annahmen, Lücken und menschliche Freigaben.

   Aufgabe:
   Führe mich Schritt für Schritt durch den ersten NIS2-/ISMS-/Audit-Durchstich.

   Gewünschter Output:
   1. Welche Repo-Dateien ich öffnen soll.
   2. Welche Fragen ich beantworten muss.
   3. Welches Template ich zuerst ausfülle.
   4. Welche Human Gates ich beachten muss.
   5. Was ich danach prüfen soll.
   ```

### Prompts für typische Arbeiten

#### Compliance-Register starten

```text
Nutze krisensicherOS als Arbeitsrahmen.

Ziel: Ich möchte einen ersten Compliance-Registereintrag erstellen.

Nutze diese Struktur:
- Quelle / Referenz
- Typ der Vorgabe
- Owner
- Vertraulichkeit / Lizenz
- eigene Zusammenfassung
- mögliche Governance-Routine
- Evidenzbedarf
- menschliche Prüfung

Grenzen:
Keine Rechtsberatung, keine Vertragsauslegung, keine Normtext-Reproduktion.
Frage nach fehlenden Informationen, statt sie zu erfinden.
```

#### Dokumenten-Gap-Analyse

```text
Rolle: document-gap-analyst.

Vergleiche das folgende Dokument oder die folgende Zusammenfassung mit den Anforderungen, die ich angebe.

Output:
- Document Gap Matrix
- fehlende Inhalte
- widersprüchliche Inhalte
- veraltete Inhalte
- nicht evidenzfähige Aussagen
- Änderungsbedarf
- Owner-/Reviewfragen

Grenzen:
Keine finale Rechts- oder Konformitätsbewertung. Markiere Annahmen und Human Gates.
```

#### Auditfragebogen erstellen

```text
Rolle: internal-audit-planner.

Erstelle aus den folgenden Anforderungen einen internen Auditfragebogen.

Für jede Anforderung:
- Referenz / Kriterium
- Audit-Leitfrage
- erwartete Evidenz
- mögliche Interviewrolle
- passende Prüfmethode
- Bewertungshinweis
- Human Gate

Nutze keine Normtexte. Arbeite nur mit meinen Zusammenfassungen und Referenzen.
```

## Setup B: Microsoft 365 Copilot

### Für wen?

Für Organisationen, die bereits mit Word, Excel, PowerPoint, Teams, Outlook, SharePoint und OneDrive arbeiten und Copilot im M365-Tenant administriert nutzen.

### Vorbedingungen

- Microsoft 365 Copilot Lizenz oder freigegebene Copilot-Variante.
- Admin-Konfiguration im Microsoft 365 Admin Center.
- Zuständige Rollen, z. B. AI Administrator oder entsprechende Admin-Rolle.
- Berechtigungen, DLP, Sensitivity Labels und SharePoint-/OneDrive-Governance geprüft.

### Schritt-für-Schritt für Admin/Owner

1. **Lizenz und Tenant-Freigabe prüfen**

   - Ist Microsoft 365 Copilot für die Organisation verfügbar?
   - Welche Apps/Szenarien sind aktiviert?
   - Wer darf Copilot nutzen?

2. **Datenzugriff prüfen**

   - SharePoint-/Teams-Berechtigungen bereinigen.
   - Sensitivity Labels und DLP-Regeln prüfen.
   - Keine Copilot-Nutzung auf ungeprüften vertraulichen Bereichen erlauben.

3. **krisensicherOS-Arbeitsbibliothek anlegen**

   Empfohlene SharePoint-Struktur:

   ```text
   krisensicherOS/
   ├── 01 Orientierung
   ├── 02 Compliance Register
   ├── 03 Audit und Evidence
   ├── 04 Management Review
   ├── 05 Dokumente in Arbeit
   └── 99 Archiv
   ```

4. **Kernartefakte hochladen**

   - ausgewählte README-Dateien,
   - Rollenmodell,
   - relevante Templates,
   - Qualitätsgates,
   - Reviewprozess.

5. **Arbeitsregel in Teams/SharePoint dokumentieren**

   ```text
   Copilot darf krisensicherOS-Artefakte zusammenfassen, Fragen ableiten und Entwürfe vorbereiten.
   Copilot darf keine Rechtsberatung, Datenschutzbewertung, Risikoakzeptanz oder Managemententscheidung treffen.
   Vertrauliche Quellen und lizenzpflichtige Normen werden nur als Metadaten oder eigene Zusammenfassungen genutzt.
   ```

### Prompts für M365 Copilot

#### Word: Dokument aus Rohmaterial strukturieren

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

#### Excel: Auditfragen strukturieren

```text
Erstelle aus dieser Tabelle einen Auditfragebogen.

Spalten:
- Anforderung / Referenz
- Control / Thema
- Audit-Leitfrage
- Prüfmethode
- erwartete Evidenz
- Owner
- Bewertungshinweis
- offene Human-Gate-Frage

Nutze nur die vorhandenen Zusammenfassungen, keine Normtexte ergänzen.
```

#### Teams: Meeting zusammenfassen

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

## Setup C: Claude Code

### Für wen?

Für Repo-nahe Arbeit: Dokumentation, Skills, Templates, Playbooks, Workflows, Checks und strukturierte Änderungen im Git-Repo.

### Minimaler Werkzeugkasten

- VS Code 1.98 oder höher.
- Claude Code Extension oder Claude Code CLI.
- Anthropic Account oder freigegebener Provider.
- Git.
- Lokaler krisensicherOS-Checkout.

### Schritt-für-Schritt

1. **VS Code installieren und Repo öffnen**

   ```bash
   git clone <repo-url> krisensicherOS
   cd krisensicherOS
   code .
   ```

2. **Claude Code installieren**

   - In VS Code Extensions nach `Claude Code` suchen.
   - Installieren.
   - Anmelden.
   - Alternativ CLI im Terminal nutzen, wenn Extension nicht verfügbar ist.

3. **Projektkontext lesen lassen**

   Erster Prompt:

   ```text
   Lies README.md, AGENTS.md, governance/review-process.md und evals/quality-gates.md.

   Danach erkläre mir:
   - wie dieses Repo arbeitet,
   - welche Stop-Punkte gelten,
   - welche Dateien ich für meinen ersten Workflow nutzen soll.

   Führe keine Änderungen aus, bevor du mir den Plan gezeigt hast.
   ```

4. **Änderungen immer mit Plan und Diff**

   Prompt:

   ```text
   Aufgabe: Ergänze ein neues Template für <Thema>.

   Regeln:
   - Folge templates/README.md und evals/quality-gates.md.
   - Keine Rechtsberatung, keine Datenschutzberatung, keine Konformitätszusage.
   - Nutze fiktive Beispiele.
   - Zeige erst den Plan.
   - Ändere dann nur die nötigen Dateien.
   - Führe danach einen Struktur- und Claim-Safety-Check aus.
   ```

### Typische Claude-Code-Aufgaben

- neue Skills unter `skills/<name>/SKILL.md`,
- Templates ergänzen,
- Workflows aktualisieren,
- Link- und Strukturchecks,
- README konsolidieren,
- Release-Checkliste vorbereiten.

## Setup D: Lokale KI ohne Cloud

### Für wen?

Für Organisationen oder Einzelpersonen, die sensible Inhalte nicht an Cloud-KI senden wollen oder zuerst lokal experimentieren möchten.

### Kandidaten

#### Ollama

Gut für:

- Entwickler,
- lokale API,
- schnelle Modelltests,
- Kombination mit Open WebUI oder Continue.

Typischer Start erst nach Modell-/Checkpoint-Freigabe:

```bash
ollama pull <freigegebenes-modell:version>
ollama run <freigegebenes-modell:version>
```

Vor `pull` dokumentieren: Quelle, Modellname, Version, Checkpoint/Hash, Lizenz, Speicherort, Zweck und Owner-Freigabe.

Empfehlung:

- für einfache Governance-Texte: 7B–14B Instruct-Modell,
- für Code/Repo: Coder-Modell,
- für längere Dokumente: Modell mit größerem Kontextfenster.

#### LM Studio

Gut für:

- Nutzer, die GUI statt Terminal wollen,
- lokale Modellverwaltung,
- OpenAI-kompatible lokale API,
- Tests mit verschiedenen Modellen.

Vorgehen:

1. LM Studio installieren.
2. Modell suchen und herunterladen.
3. Chat testen.
4. Optional lokalen Server / OpenAI-kompatible API aktivieren.
5. Mit Continue, Open WebUI oder eigenen Tools verbinden.

#### Jan

Gut für:

- einfacher lokaler Desktop-Chat,
- Open-Source-Ansatz,
- Nutzer, die „lokales ChatGPT“ ohne viel Setup wollen.

Vorgehen:

1. Jan installieren.
2. lokales Modell laden.
3. Governance-Prompts aus dieser Anleitung nutzen.
4. Keine ungeprüften vertraulichen Daten in exportierte Beispiele übernehmen.

#### GPT4All

Gut für:

- einfache lokale Chat-Nutzung,
- private Wissens-/Dokumentenfragen,
- niedrige Einstiegshürde.

Nicht ideal für:

- komplexe Repo-Agentenarbeit,
- größere Team-Orchestrierung.

#### Open WebUI

Gut für:

- self-hosted Teamoberfläche,
- Ollama-Anbindung,
- RAG/Wissenssammlungen,
- lokale oder hybride Provider.

Typischer Start mit Docker, erst nach Versions-/Digest-Freigabe:

```bash
docker run -d -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:<freigegebene-version-oder-digest>
```

Nicht mit `:main` betreiben. Image-Version oder Digest, Updateprozess und Restart-Verhalten müssen durch den Betriebsowner freigegeben werden.

Danach im Browser öffnen:

```text
http://localhost:3000
```

#### Continue

Gut für:

- VS-Code-/IDE-nahe KI-Arbeit,
- lokale oder hybride Modelle,
- Repo-Checks,
- Coding- und Dokumentationsworkflows.

Empfehlung:

- Continue mit Ollama oder LM Studio verbinden.
- Für krisensicherOS eigene Checks definieren: Public-Safety, Claim-Safety, Secret-Scan, Betriebslogik.


## Betriebscheckliste für lokale KI und Redaction-Tools

Lokale KI ist nicht automatisch sicher. Sie ist ein betreibbares System und braucht Owner, Regeln und Kontrolle.

Vor produktiver Nutzung klären:

| Prüffeld | Mindestklärung |
| --- | --- |
| Systemowner | Wer betreibt Ollama, LM Studio, Open WebUI, Continue oder Redaction-Komponenten? |
| Zweck / Scope | Für welche Aufgaben darf das System genutzt werden? |
| Datenklassen | Welche Daten dürfen verarbeitet werden? Welche sind verboten? |
| Zugriff | Wer darf nutzen, administrieren und Logs sehen? |
| Modellfreigabe | Welche Modelle/Checkpoints sind erlaubt? Wer gibt Änderungen frei? |
| Patch / Update | Wer aktualisiert App, Runtime, Container, Modelle und Abhängigkeiten? |
| Logging | Welche Eingaben, Outputs, Metadaten oder Fehlerlogs werden gespeichert? |
| Speicherorte | Wo liegen Modelle, Prompts, Uploads, Vektordatenbanken, Exporte und Backups? |
| Redaction | Wird ein Tool wie OpenAI Privacy Filter eingesetzt? Wie wird es evaluiert? |
| Evaluation | Wie werden False Positives, False Negatives und Domäneneignung geprüft? |
| Offboarding | Wie werden Nutzer, Modelle, Daten und Logs entfernt oder archiviert? |
| Human Review | Wer prüft kritische Outputs vor Weitergabe oder Entscheidung? |

Für OpenAI Privacy Filter oder vergleichbare Redaction-Komponenten zusätzlich klären:

- Wo liegen Modellgewichte und Checkpoints?
- Werden Eingaben oder Redaction-Ergebnisse gespeichert?
- Welche Label-Kategorien werden erkannt und welche nicht?
- Gibt es Tests mit deutschen, domänenspezifischen und organisationsnahen Beispielen?
- Wer entscheidet, ob Redaction-Ergebnisse ausreichend für den konkreten Zweck sind?

Redaction bleibt eine Hilfsschicht. Sie ersetzt keine Datenklassifizierung, keine Datenschutzbewertung und keine menschliche Freigabe.

## Lokale KI: Hardware-Faustregeln

| Hardware | Sinnvoller Start |
| --- | --- |
| 16 GB RAM, keine starke GPU | kleine 3B–8B Modelle, kurze Aufgaben |
| 32 GB RAM | 7B–14B Modelle, Dokumentenarbeit begrenzt |
| 64 GB RAM oder Apple Silicon mit viel Unified Memory | größere Modelle, längere Dokumente |
| starke NVIDIA GPU | schnellere Inferenz, größere Modelle, Team-/API-Nutzung |

Wichtig: Lokale Modelle sind nicht automatisch besser oder sicherer. Sie reduzieren Cloud-Abfluss, brauchen aber trotzdem Datenklassifizierung, Protokollierung, Zugriffskontrolle und menschliche Prüfung.

## Empfohlenes v1.0-Setup nach Reifegrad

### Stufe 1 — Einfachster Start

- ChatGPT oder M365 Copilot
- krisensicherOS-Templates als Dateien
- keine vertraulichen Daten
- Human Gates manuell

### Stufe 2 — Repo-Arbeit

- VS Code
- Claude Code oder ChatGPT Work with Apps
- Git
- lokale Checks
- Arbeit über Skills/Templates/Workflows

### Stufe 3 — Datenschutzsensibler Pilot

- LM Studio oder Jan für lokalen Chat
- Ollama für lokale API
- keine Cloud-Datenübertragung
- manuelle Qualitätssicherung

### Stufe 4 — Teamfähiger Betrieb

- Open WebUI + Ollama/LM Studio/API
- M365 Copilot für Office-Arbeit
- Claude Code/Continue für Repo-Arbeit
- klare Rollen, Logs, Reviewprozess, Release-Gates

## Universal-Prompt für krisensicherOS

```text
Du arbeitest mit krisensicherOS.

Arbeitsregeln:
- Keine Rechtsberatung.
- Keine Datenschutzberatung.
- Keine Konformitäts-, Zertifizierungs- oder Sicherheitszusage.
- Keine Managemententscheidung.
- Nutze Quellen, Normen und Verträge nur als Referenzen, Metadaten oder eigene Zusammenfassungen.
- Markiere Annahmen, Lücken, Evidenzbedarf und Human Gates.
- Erzeuge Output mit Owner, Trigger, Ablauf, Evidenz, Review und nächstem Schritt.

Aufgabe:
<konkrete Aufgabe einfügen>

Input:
<Scope, Anforderungen, Rohmaterial oder Dokumente einfügen>

Gewünschter Output:
<Template, Skill-Output oder Reviewformat einfügen>
```

## Welche lokale KI kommt infrage?

Für krisensicherOS sind realistisch:

1. **Ollama** — beste Basis für lokale Modell-API und Entwickler-Workflows.
2. **LM Studio** — beste GUI für lokale Modelltests und lokale OpenAI-kompatible API.
3. **Jan** — einfacher Open-Source-Desktop-Chat.
4. **GPT4All** — einfacher privater lokaler Chat, gut für niedrigschwellige Nutzung.
5. **Open WebUI** — self-hosted Teamoberfläche für lokale/hybride Modelle.
6. **Continue** — IDE-/Repo-Assistent, besonders mit Ollama oder LM Studio.
7. **AnythingLLM** — relevant für lokale Wissensbasen/RAG, wenn Dokumentensammlungen im Vordergrund stehen.

Empfehlung für v1.0:

- **Nicht alles gleichzeitig unterstützen.**
- Primär dokumentieren: ChatGPT, M365 Copilot, Claude Code.
- Lokal als drei Pfade dokumentieren:
  - einfach: LM Studio oder Jan,
  - technisch: Ollama,
  - teamfähig: Ollama + Open WebUI,
  - IDE: Continue + Ollama/LM Studio.

## Definition of Done für ein Setup

Ein Setup ist einsatzbereit, wenn:

- Datenklassen und erlaubte KI festgelegt sind,
- Nutzer wissen, wo krisensicherOS-Artefakte liegen,
- ein Universal-Prompt vorhanden ist,
- mindestens ein End-to-End-Workflow getestet wurde,
- Human Gates dokumentiert sind,
- Outputs gegen Qualitätsgates geprüft werden,
- keine Veröffentlichung oder externe Weitergabe ohne Freigabe erfolgt.
