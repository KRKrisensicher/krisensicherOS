<!-- kso:product-relevance
repo-scope: product
classification: setup-guidance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Setup: ChatGPT mit lokaler IDE

Stand: 2026-05-23

## Zweck

Dieses Setup ist für Einzelpersonen oder kleine Teams, die krisensicherOS mit ChatGPT und einer lokalen Arbeitsumgebung nutzen wollen.

ChatGPT darf nur verwendet werden, wenn die Organisation die Nutzung für die betroffenen Datenklassen freigegeben hat.

## Windows-first Werkzeugkasten

- Windows 10/11,
- VS Code oder kompatibler Editor,
- Git for Windows,
- lokaler krisensicherOS-Checkout oder ZIP-Download,
- ChatGPT Account passend zur Organisationsfreigabe,
- optional ChatGPT Desktop App oder VS-Code-Integration, sofern freigegeben.

## Schritt-für-Schritt unter Windows

1. Git for Windows installieren oder Repo als ZIP herunterladen.
2. Arbeitsordner anlegen, z. B. `C:\\Users\\<Name>\\Documents\\krisensicherOS`.
3. Repo öffnen:

   ```powershell
   git clone <repo-url> krisensicherOS
   cd krisensicherOS
   code .
   ```

4. Startdateien öffnen:
   - `README.md`
   - `01-orientation/getting-started/minimaler-nis2-start-in-5-artefakten.md`
   - `01-orientation/setup/README.md`
   - `templates/ki-nutzungsfreigabe-matrix.md`

5. KI-Freigabe prüfen: Matrix und ChatGPT-spezifische Prüftabelle müssen vor dem ersten Prompt geklärt sein.
6. Nur freigegebene, passende Inhalte in ChatGPT eingeben.
7. Outputs als Entwürfe behandeln und gegen Human Gates prüfen.

## Hartes Freigabe-Gate vor dem ersten Prompt

Ohne ausgefüllte [`../../templates/ki-nutzungsfreigabe-matrix.md`](../../07-ai-governance-agents/templates/ki-nutzungsfreigabe-matrix.md) **und** ohne die folgende ChatGPT-spezifische Prüftabelle wird dieser Pfad nicht genutzt. Dann wird nur die Freigabe vorbereitet; produktive Nutzung stoppt.

Vor der ersten ChatGPT-Nutzung dokumentieren:

| Prüffeld | Mindestklärung |
| --- | --- |
| Account-/Workspace-Typ | Persönlich, Team, Enterprise oder organisationsintern freigegeben? |
| Vertrags-/Adminfreigabe | Wer hat Nutzung und Datenklassen freigegeben? |
| Datenverwendung | Sind Training/Data-use-Einstellungen, Verlauf und Memory geklärt? |
| Uploads | Sind Datei-Uploads erlaubt oder nur Copy/Paste von freigegebenen Ausschnitten? |
| IDE-Kontext | Darf ChatGPT Projektdateien oder Editor-Kontext lesen? |
| Connectoren | Sind externe Connectoren deaktiviert oder freigegeben? |
| Logging/Löschung | Wer kennt Speicher-, Export- und Löschregeln? |
| Verbotene Inhalte | Secrets, Personendaten, Kundendaten, Vertragsdetails und lizenzpflichtige Normtexte ausgeschlossen? |

Bei unklarer Datenklasse, unklarem Accounttyp oder ungeklärter Datenverwendung: Stop und Freigabe klären.

## Sicherer Erstprompt

Stop: Diesen Prompt erst verwenden, wenn Freigabematrix und ChatGPT-spezifische Prüftabelle abgeschlossen sind.

```text
Du unterstützt mich mit krisensicherOS.

Kontext:
- Ich arbeite in einer lokalen Windows-Arbeitskopie.
- Nutze nur die Dateien, die ich dir gebe oder ausdrücklich beschreibe.
- Erzeuge keine Rechtsberatung, Datenschutzberatung, Konformitäts- oder Zertifizierungszusage.
- Markiere Annahmen, Lücken, Evidenzbedarf und menschliche Freigaben.
- Verarbeite nur Inhalte, deren Datenklasse für diese ChatGPT-Umgebung freigegeben ist. Fordere mich auf zu stoppen, wenn Input vertraulich, personenbezogen, kundenspezifisch, vertraglich, lizenzpflichtig oder ein Secret sein könnte.

Aufgabe:
Führe mich Schritt für Schritt durch den ersten NIS2-/ISMS-/Audit-Durchstich.

Gewünschter Output:
1. Welche Repo-Dateien ich öffnen soll.
2. Welche Fragen ich beantworten muss.
3. Welches Template ich zuerst ausfülle.
4. Welche Human Gates ich beachten muss.
5. Was ich danach prüfen soll.
```

## Nicht verwenden für

- ungeklärte vertrauliche Inhalte,
- personenbezogene Daten ohne Freigabe,
- Kundendaten, Vertragsdetails oder Secrets,
- lizenzpflichtige Normtexte,
- finale Rechts-, Datenschutz-, Risiko- oder Managemententscheidungen.

## Windows-Start präzisiert

Wenn noch keine konkrete Repo-URL verfügbar ist, nutze eine ZIP-Arbeitskopie oder eine intern bereitgestellte Kopie.

PowerShell-Beispiel mit Git:

```powershell
cd $HOME\Documents
git clone <freigegebene-repo-url> krisensicherOS
cd krisensicherOS
code .
```

`<freigegebene-repo-url>` muss durch die interne oder öffentliche freigegebene Repo-Adresse ersetzt werden.

## Human-Gates für ChatGPT-Outputs

| Output / Thema | Human Gate |
| --- | --- |
| Rechts-/Regulierungsbezug | Legal oder verantwortliche Fachrolle prüft |
| personenbezogene Daten | Datenschutzrolle prüft |
| Risikoakzeptanz | Management entscheidet |
| technische Evidenz | IT-/Systemowner prüft |
| Veröffentlichung oder externe Weitergabe | fachliche Freigabe vorab |
| unklare Datenklasse | Stop und Freigabe-/Handoff-Klärung |
