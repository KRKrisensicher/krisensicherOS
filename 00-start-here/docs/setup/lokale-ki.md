
# Setup: Lokale KI ohne Cloud

Stand: 2026-05-23

## Zweck

Dieses Setup ist für Organisationen oder Einzelpersonen, die KI lokal betreiben oder testen wollen, ohne Inhalte an Cloud-KI zu senden.

Lokale KI ist nicht automatisch sicher. Sie ist ein betreibbares System mit Owner, Zugriffskontrolle, Modellfreigabe, Logging, Evaluation und Offboarding.

## Windows-first Kandidaten

| Werkzeug | Geeignet für |
| --- | --- |
| LM Studio | GUI, lokale Modelltests, OpenAI-kompatible lokale API |
| Jan | einfacher lokaler Desktop-Chat |
| GPT4All | niedrigschwellige lokale Chat-/Dokumentennutzung |
| Ollama | lokale Modell-API, Entwickler-Workflows, Kombination mit Open WebUI/Continue |
| Open WebUI | self-hosted Teamoberfläche, meist mit Ollama |
| Continue | IDE-/Repo-Assistent mit lokaler oder hybrider Modellanbindung |

## Einstieg für Windows-Nutzer

Grundregel: **erst Modell-/Checkpoint-Freigabe dokumentieren, dann herunterladen, installieren oder `ollama pull` ausführen.**

1. Mit LM Studio oder Jan starten, wenn eine einfache GUI benötigt wird.
2. Mit Ollama starten, wenn lokale APIs oder Entwickler-Workflows nötig sind.
3. Für Teamnutzung Open WebUI nur mit Betriebsowner und Zugriffskonzept einsetzen.
4. Für Repo-Arbeit Continue mit Ollama oder LM Studio prüfen.

## Beispiel: LM Studio

1. LM Studio installieren.
2. Modell-/Checkpoint-Freigabe dokumentieren.
3. Geeignetes freigegebenes Modell herunterladen.
4. Lokalen Chat testen.
5. Optional lokalen Server aktivieren.
6. Nur freigegebene Datenklassen verwenden.
7. Outputs gegen Human Gates prüfen.

## Beispiel: Ollama

```powershell
# erst nach Modell-/Checkpoint-Freigabe
ollama pull <freigegebenes-modell:version>
ollama run <freigegebenes-modell:version>
```

Vor `pull` dokumentieren: Quelle, Modellname, Version, Checkpoint/Hash, Lizenz, Speicherort, Zweck und Owner-Freigabe.

Empfehlung:

- einfache Governance-Texte: 7B–14B Instruct-Modell,
- Code/Repo: Coder-Modell,
- längere Dokumente: Modell mit größerem Kontextfenster.

## Betriebscheckliste

| Prüffeld | Mindestklärung |
| --- | --- |
| Systemowner | Wer betreibt lokale KI, Modellserver oder Redaction-Komponenten? |
| Zweck / Scope | Für welche Aufgaben darf das System genutzt werden? |
| Datenklassen | Welche Daten dürfen verarbeitet werden? Welche sind verboten? |
| Zugriff | Wer darf nutzen, administrieren und Logs sehen? |
| Modellfreigabe | Welche Modelle/Checkpoints sind erlaubt? Wer gibt Änderungen frei? |
| Patch / Update | Wer aktualisiert App, Runtime, Container, Modelle und Abhängigkeiten? |
| Logging | Welche Eingaben, Outputs, Metadaten oder Fehlerlogs werden gespeichert? |
| Speicherorte | Wo liegen Modelle, Prompts, Uploads, Vektordatenbanken, Exporte und Backups? |
| Evaluation | Wie werden False Positives, False Negatives und Domäneneignung geprüft? |
| Offboarding | Wie werden Nutzer, Modelle, Daten und Logs entfernt oder archiviert? |
| Human Review | Wer prüft kritische Outputs vor Weitergabe oder Entscheidung? |

## Redaction-Tools

OpenAI Privacy Filter oder vergleichbare Werkzeuge können als Hilfsschicht geprüft werden. Im lokalen „ohne Cloud“-Setup dürfen solche Werkzeuge nur genutzt werden, wenn sie tatsächlich lokal betrieben werden oder wenn für einen cloudbasierten Datenfluss eine explizite Freigabe für die betroffene Datenklasse vorliegt.

Vor Nutzung klären:

- Wo liegen Modellgewichte und Checkpoints?
- Werden Eingaben oder Redaction-Ergebnisse gespeichert?
- Welche Label-Kategorien werden erkannt und welche nicht?
- Gibt es Tests mit deutschen, domänenspezifischen und organisationsnahen Beispielen?
- Wer entscheidet, ob Redaction-Ergebnisse ausreichend für den konkreten Zweck sind?

Redaction ersetzt keine Datenklassifizierung, keine Datenschutzbewertung und keine menschliche Freigabe.

## Modell-/Checkpoint-Freigabe

Vor dem Download oder Wechsel eines Modells dokumentieren:

| Prüffeld | Mindestklärung |
| --- | --- |
| Quelle / Registry | Woher stammt das Modell? |
| Modellname / Version | Welche konkrete Version wird genutzt? |
| Checkpoint / Hash / Quantisierung | Welche Datei/Variante wurde freigegeben? |
| Lizenz | Darf das Modell für den vorgesehenen Zweck genutzt werden? |
| Speicherort | Wo liegen Modell, Cache und Konfiguration? |
| Zweck | Für welche Aufgaben ist das Modell freigegeben? |
| Owner-Freigabe | Wer hat Nutzung und Wechsel freigegeben? |

Modellwechsel, neue Quantisierung oder neuer Checkpoint gelten als neue Freigabe.

## Windows-Pilot-Checkliste

Vor lokaler Nutzung unter Windows prüfen:

- Läuft ein lokaler Server nur auf `127.0.0.1` oder ist er im Netzwerk erreichbar?
- Wo liegen Modellcache, Chatverläufe, Uploads, Exporte, Vektordatenbanken und Backups?
- Sind Adminrechte für Installation oder Betrieb nötig?
- Werden lokale App-Logs, Fehlerlogs oder Telemetriedaten geschrieben?
- Ist Netzwerkzugriff blockiert, eingeschränkt oder bewusst freigegeben?
- Werden Arbeitsdaten im Benutzerprofil, in OneDrive, in einer zentralen Ablage oder in einem Projektordner gespeichert?
- Ist klar, wer Daten löschen, exportieren oder sichern darf?

Unklare Speicherorte oder unklare Netzwerkbindung führen zu Stop; produktive Nutzung startet erst nach Betriebsfreigabe oder ausschließlich mit öffentlichen/fiktiven Testdaten.

## Mindestentscheidung zu Logging und Speicherorten

Vor Pilotstart müssen mindestens Speicherorte für Modelle, Prompts, Uploads, Chatverläufe, Exporte, Vektordatenbanken, Logs und Backups dokumentiert sein.

Wenn nicht klar ist, was gespeichert wird oder wer Zugriff auf Logs hat, darf nur mit öffentlichen oder fiktiven Daten getestet werden.

## Teamnutzung / Open WebUI Gate

Teamoberflächen wie Open WebUI erst einsetzen, wenn geklärt ist:

- Rollenmodell: Nutzer, Admin, Owner, Log-Zugriff,
- Authentisierung und Zugriffsentzug,
- Trennung von Projekten und Datenräumen,
- Lösch- und Exportrechte,
- Umgang mit geteilten Chats,
- Umgang mit RAG-Daten und Vektordatenbanken,
- Reviewprozess für neue Nutzer, Modelle und Wissenssammlungen.

Ohne diese Klärung bleibt lokale KI auf Einzelplatz-Pilot mit fiktiven oder öffentlichen Daten begrenzt.

## Redaction im lokalen Setup

Redaction-Tools dürfen im lokalen Setup nur genutzt werden, wenn Betriebsmodus, Datenfluss, Speicherorte, Logging und Modell-/Checkpoint-Ablage nachweislich geklärt sind.

Ein cloudbasiertes Redaction-Tool ist kein Bestandteil eines „ohne Cloud“-Setups, sofern keine explizite Freigabe für diese Datenklasse vorliegt.

## Mindest-Evaluation vor produktiver Nutzung

Vor produktiver Nutzung mindestens 5–10 fiktive oder domänentypische Testfälle prüfen:

- Zusammenfassung ohne erfundene Fakten,
- Halluzination bei unvollständigen Inputs,
- falsche Sicherheits- oder Konformitätsaussage,
- Rechts-/Datenschutzclaim,
- Secret-Erkennung,
- Redaction-False-Negative,
- deutsche Fachbegriffe und Abkürzungen,
- Umgang mit widersprüchlichen Dokumenten,
- klare Markierung von Annahmen und Human Gates.
