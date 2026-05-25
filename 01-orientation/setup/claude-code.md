<!-- kso:product-relevance
repo-scope: product
classification: setup-guidance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Setup: Claude Code für krisensicherOS

Stand: 2026-05-23

## Zweck

Dieses Setup ist für Repo-nahe Arbeit: Dokumentation, Templates, Skills, Playbooks, Workflows, Checks und strukturierte Änderungen im Git-Repo.

Die Anleitung ist **Windows-first** geschrieben. macOS/Linux sind möglich, aber nicht der primäre Einstieg.

## Varianten

| Variante | Geeignet für |
| --- | --- |
| Claude Code App | Nutzer, die eine geführte App-Erfahrung für Repo-Arbeit bevorzugen |
| Claude Code in VS Code | Nutzer, die direkt im Editor planen, ändern und diffen wollen |
| Claude Code CLI | technischere Nutzer, Automatisierung, Terminal-Workflows |

## Vorbedingungen

- Windows 10/11,
- Git for Windows,
- VS Code empfohlen,
- lokaler krisensicherOS-Checkout,
- freigegebener Anthropic-/Claude-Zugang oder freigegebener Provider,
- geklärte Datenklasse und KI-Nutzungsfreigabe.

## Read-only-Erstlauf und App-Sicherheitscheck

Für KI-kritische Organisationen beginnt Claude Code immer lesend.

Vor dem ersten Prompt prüfen:

- Ist ausschließlich der freigegebene Repo-Ordner geöffnet?
- Wurde nicht versehentlich `C:\Users\<Name>`, das Benutzerprofil, ein Root-Laufwerk, OneDrive komplett oder ein vertraulicher SharePoint-Sync-Ordner geöffnet?
- Enthält der Ordner keine echten Kunden-, Personen-, Vertrags-, Incident-, System- oder Secret-Daten?
- Sind zusätzliche Ordner, Connectoren oder Integrationen deaktiviert oder freigegeben?
- Ist klar, ob die App Dateien ändern darf oder zunächst nur lesen soll?

Read-only-Erstprompt:

```text
Arbeite zunächst nur lesend.
Führe keine Dateiänderungen, keine Shell-Kommandos mit Schreibwirkung, keine Git-Aktionen und keine externen Veröffentlichungen aus.
Lies README.md, AGENTS.md, CLAUDE.md, 01-orientation/setup/README.md und 06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md.
Lies nur die ausdrücklich genannten Dateien im geöffneten Repo-Ordner.
Erkläre mir danach den sicheren Arbeitsplan und die Stop-Punkte.
```

## Variante 1: Claude Code App unter Windows

1. Claude Code App gemäß Herstelleranleitung installieren.
2. Mit dem freigegebenen Organisationskonto anmelden.
3. Lokalen Arbeitsordner öffnen, z. B.:

   ```text
   C:\Users\<Name>\Documents\krisensicherOS
   ```

4. Sicherstellen, dass die App nur auf den gewünschten Projektordner zugreift.
5. Startdateien in der App bzw. im Projektkontext öffnen:
   - `README.md`
   - `AGENTS.md`
   - `CLAUDE.md`
   - `01-orientation/setup/README.md`
   - `06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md`

6. Read-only-Erstprompt aus dem Abschnitt oben nutzen. Nicht mit Änderungsaufgaben starten.

## Variante 2: Claude Code in VS Code unter Windows

1. Git for Windows installieren.
2. VS Code installieren.
3. Repo klonen:

   ```powershell
   git clone <repo-url> krisensicherOS
   cd krisensicherOS
   code .
   ```

4. Claude Code Extension installieren, sofern organisationsseitig freigegeben.
5. Im Projektkontext dieselben Startdateien lesen lassen.
6. Änderungen nur nach Plan und Diff durchführen lassen.

## Variante 3: Claude Code CLI unter Windows

1. Terminal öffnen: PowerShell oder Windows Terminal.
2. In das Repo wechseln:

   ```powershell
   cd C:\Users\<Name>\Documents\krisensicherOS
   ```

3. Claude Code CLI gemäß Herstelleranleitung starten.
4. Vor Änderungen immer Plan anfordern.
5. Nach Änderungen lokal prüfen:

   ```powershell
   git diff --check
   git status --short
   ```

## Änderungs-Prompt mit Sicherheitsgrenzen

```text
Aufgabe: Ergänze oder ändere <konkretes Artefakt>.

Regeln:
- Folge AGENTS.md, CLAUDE.md und 06-evidence-management-review/06-evidence-management-review/evals/quality-gates.md.
- Keine Rechtsberatung, Datenschutzberatung, Konformitäts- oder Zertifizierungszusage.
- Nutze fiktive Beispiele.
- Keine echten Organisations-, Kunden-, Personen-, Vertrags-, Incident- oder Systemdaten.
- Zeige erst den Plan.
- Ändere danach nur die nötigen Dateien.
- Zeige anschließend den Diff und nenne die geprüften Qualitätsgates.
```

## Typische Aufgaben

- README konsolidieren,
- Setup-Dokumente ergänzen,
- Templates schärfen,
- Skills unter `07-ai-governance-agents/skills/<name>/SKILL.md` erstellen,
- Workflows aktualisieren,
- Link- und Claim-Safety-Checks vorbereiten.

## Stop-Punkte

Claude Code darf nicht eigenständig:

- veröffentlichen, pushen, taggen oder releasen,
- Lizenz- oder Disclaimer-Änderungen durchführen,
- echte Organisationsdaten in öffentliche Beispiele schreiben,
- rechtliche oder datenschutzrechtliche Bewertungen finalisieren,
- Managemententscheidungen oder Risikoakzeptanz treffen.

## Windows-Selbsttest

PowerShell im lokalen krisensicherOS-Repo-Ordner öffnen, z. B.:

```powershell
cd C:\Users\<Name>\Documents\krisensicherOS
```

Danach prüfen:

```powershell
git --version
code --version
git status --short
```

Wenn `git status --short` unerwartete Änderungen zeigt: stoppen und zuerst klären, ob diese Änderungen bewusst sind.

Empfohlener Arbeitsort für den Pilot ist eine lokale oder intern freigegebene Arbeitskopie, nicht das gesamte Benutzerprofil und nicht ein ungeprüfter Sync aller Unternehmensdaten.

## Branch-, Diff- und Commit-Regeln

Vor Änderungen:

```powershell
git status --short
git switch -c setup-pilot/<kurzer-name>
```

Regeln:

- nur auf freigegebenem Arbeitsbranch arbeiten,
- keine Änderungen bei unklarem Arbeitsbaum,
- Plan vor Änderung zeigen lassen,
- Diff nach Änderung prüfen,
- keine Commits ohne menschliche Freigabe,
- keine Pushes, Tags, Releases oder Veröffentlichungen ohne explizite Freigabe.

Wenn lokale Commits im Pilot erlaubt sind, muss die verantwortliche Rolle das vorher ausdrücklich entscheiden. Diese strengere Pilotregel hat Vorrang vor allgemeinen Hinweisen in `CLAUDE.md`.

## Minimaler Quality-Gate-Nachweis nach Änderungen

Nach Änderungen soll Claude Code mindestens berichten:

| Gate | Prüffrage |
| --- | --- |
| U1 Public-Safe | Enthält der Output echte Organisations-, Personen-, Kunden-, Vertrags- oder Systemdaten? |
| U2 Claim-Safety | Enthält der Output Rechts-, Datenschutz-, Konformitäts-, Zertifizierungs- oder Sicherheitszusagen? |
| U3 Betriebslogik | Sind Owner, Trigger, Ablauf, Evidenz und Review klar? |
| U4 Empowerment | Befähigt das Artefakt Nutzer oder erzeugt es unnötige Abhängigkeit? |
| U5 Workload | Ist der Aufwand für Mittelstand realistisch? |
| U6 Portabilität | Bleibt das Artefakt toolneutral und adapterfähig? |
| A7 Adapter-Gate | Falls toolbezogen: bleibt Fachlogik im Source-of-Truth und nicht im Adapter versteckt? |
