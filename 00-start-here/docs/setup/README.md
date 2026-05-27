
# Setup-Einstieg für krisensicherOS

## Kernaussage

krisensicherOS setzt eine freigegebene KI-Nutzung voraus.

Ohne freigegebene KI-Umgebung ist krisensicherOS kein sinnvoller Betriebsmodus. Organisationen können die KI-Freigabe vorbereiten, aber nicht produktiv mit krisensicherOS arbeiten.

## Vorab: KI-Freigabe klären

Nutze [`../../templates/ki-nutzungsfreigabe-matrix.md`](../../../08-templates-playbooks/templates/ki-nutzungsfreigabe-matrix.md), um mindestens festzulegen:

- welche Datenklassen verarbeitet werden dürfen,
- welche KI-Umgebung freigegeben ist,
- welche Inhalte verboten sind,
- wer Outputs prüft,
- welche Human Gates gelten.

Wenn diese Punkte nicht geklärt sind: stoppen, Freigabe vorbereiten, keine produktive Nutzung.

## Welche Anleitung soll ich öffnen?

| Freigegebene Umgebung | Einstieg |
| --- | --- |
| ChatGPT ist für passende Datenklassen freigegeben | [`chatgpt-lokale-ide.md`](chatgpt-lokale-ide.md) |
| Microsoft 365 Copilot ist tenantseitig freigegeben | [`m365-copilot.md`](m365-copilot.md) |
| Claude Code soll für Repo-Arbeit genutzt werden | [`claude-code.md`](claude-code.md) |
| Lokale KI ohne Cloud-Übertragung ist freigegeben oder soll technisch pilotiert werden | [`lokale-ki.md`](lokale-ki.md) |
| Mehrere Reifegrade oder Team-Setup vergleichen | [`ki-setups-bedienungsanleitung.md`](ki-setups-bedienungsanleitung.md) |

## 15-Minuten-Entscheidung

1. Starte mit [`../getting-started/minimaler-nis2-start-in-5-artefakten.md`](../getting-started/minimaler-nis2-start-in-5-artefakten.md).
2. Prüfe die KI-Freigabe mit [`../../templates/ki-nutzungsfreigabe-matrix.md`](../../../08-templates-playbooks/templates/ki-nutzungsfreigabe-matrix.md).
3. Wähle genau ein Setup-Dokument für den Pilot.
4. Prüfe Outputs immer über Human Gates, bevor sie intern entschieden oder extern weitergegeben werden.

## Gemeinsame Regeln für alle Setups

- Keine Rechtsberatung, Datenschutzberatung, Konformitäts-, Zertifizierungs- oder Sicherheitszusage.
- Keine Managemententscheidung oder Risikoakzeptanz durch KI oder Agenten.
- Keine vertraulichen, personenbezogenen, kundenspezifischen, vertraglichen oder lizenzpflichtigen Inhalte in nicht freigegebene KI-Umgebungen.
- Lizenzpflichtige Normen nur als Metadaten, Referenzen oder eigene Zusammenfassungen nutzen.
- Redaction-Tools sind Hilfsschichten, keine Anonymisierungsgarantie und kein Compliance-Nachweis.

## Windows-first Hinweis

Die Setup-Dokumente sind primär für Windows-Arbeitsplätze beschrieben. macOS/Linux werden nur dort erwähnt, wo sie für Entwickler- oder lokale KI-Setups relevant sind.
