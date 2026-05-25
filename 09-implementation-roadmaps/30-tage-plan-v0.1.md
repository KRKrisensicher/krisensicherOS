<!-- kso:product-relevance
repo-scope: product
classification: product-module
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# 30-Tage-Produkt- und Release-Roadmap v0.1

Dieser Plan ist **keine Nutzer-Implementierungsanleitung**. Er dokumentiert, wie krisensicherOS als offenes Produktrepo in einer frühen v0.1-Phase aufgebaut wurde. Für Nutzer-Durchstiche nutze stattdessen die Beispiele unter [`examples/`](examples/) und den Einstieg in [`01-orientation/getting-started/`](../01-orientation/getting-started/README.md).

## Zweck

Der Plan bleibt im Repo, damit nachvollziehbar ist, welche Produktlogik hinter der ersten Struktur stand: kein Dokumentenfriedhof, sondern ein agentisch nutzbares Betriebssystem für CISO-/ISB-Arbeit.

## Woche 1 — Fundament und Positionierung

**Ziel:** Klarer Rahmen, erste Struktur, keine Floskeln.

- README finalisieren
- Repo-Struktur anlegen
- Governance-Qualitätsregeln dokumentieren
- Disclaimer und Nicht-Ziele formulieren
- Modulbeschreibungen für alle Hauptordner erstellen
- erste Template-/Playbook-Liste priorisieren

**Ergebnis:** Orientierung, Scope und Qualitätsmaßstab stehen.

## Woche 2 — Governance Operating Model und NIS2-Readiness

**Ziel:** Erste operative Kernmodule nutzbar machen.

- Governance Operating Model Canvas erstellen
- Rollen-/RACI-Template erstellen
- NIS2-Gap-Assessment-Worksheet erstellen
- Maßnahmen-Priorisierungsmatrix erstellen
- Entscheidungslog und Evidenzlogik ergänzen

**Ergebnis:** Eine Organisation kann ihren Governance-Start und NIS2-Readiness-Status strukturiert erfassen.

## Woche 3 — Agenten und Skills

**Ziel:** Agentisches Supportteam arbeitsfähig beschreiben.

- Start-Agenten als Rollenprofile ausarbeiten
- Start-Skills im Mindestformat ausarbeiten
- Human-in-the-loop-Regeln dokumentieren
- Qualitätskriterien je Skill ergänzen
- Beispiel-Workflows für NIS2 Gap, Evidence Review und Management Review erstellen

**Ergebnis:** Agenten und Skills sind als wiederholbare Arbeitsabläufe nutzbar.

## Woche 4 — Playbooks, Beispiele, Release-Härtung

**Ziel:** v0.1 veröffentlichungsfähig machen.

- Incident-Eskalationsplaybook erstellen
- Management-Review-Playbook erstellen
- Evidence-Pack-Review-Playbook erstellen
- fiktive Beispiele unter [`examples/`](examples/) anlegen
- Repo-Governance und Beitragsregeln ergänzen
- Qualitätsreview gegen v0.1-Regeln durchführen
- Release Notes vorbereiten

**Ergebnis:** v0.1 ist als offenes Startsystem nutzbar und anschlussfähig für Beratung, Community und Weiterentwicklung.

## Definition of Done v0.1

- Jedes Kernmodul hat Zweck, Betriebslogik und erste Artefakte.
- Jede Vorlage beantwortet: Wer nutzt sie, wann, wofür, mit welcher Entscheidung?
- Keine Vorlage verspricht Rechts- oder Zertifizierungssicherheit.
- Agentenrollen haben klare Grenzen.
- Skills sind als Arbeitsabläufe beschrieben.
- README erklärt die Kategorie „agentische Sicherheits-Governance“ verständlich.
- Ein neuer Nutzer kann in weniger als 30 Minuten erkennen, wie er mit krisensicherOS startet.
