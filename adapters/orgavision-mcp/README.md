<!-- kso:product-relevance
repo-scope: product
classification: tool-adapter
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Orgavision MCP Adapter

Dieser Adapter beschreibt, wie krisensicherOS-Artefakte mit der Orgavision MCP-Schnittstelle als Verteil- und Wissenszugang in Organisationen genutzt werden können.

## Einordnung

krisensicherOS erzeugt keine fertige Governance für eine konkrete Organisation. Es hilft, Rollen, Routinen, Evidenz, Reviews und Entscheidungen vorzubereiten. Nach fachlicher Prüfung können daraus freigegebene Organisationsinformationen entstehen: Prozessbeschreibungen, Rollenklärungen, Entscheidungslogiken, Evidence-Routinen, Management-Review-Vorlagen oder Schulungsinhalte.

Orgavision kann dafür als operativer Wissens- und Verteilkanal dienen. Die öffentlich beschriebene MCP-Schnittstelle verbindet in Orgavision hinterlegtes QM-/Organisationswissen mit KI-Werkzeugen, die das Model Context Protocol unterstützen. Laut Orgavision können angebundene KI-Systeme auf freigegebene Inhalte zugreifen, dabei Leserechte berücksichtigen und relevante Textausschnitte mit Quellenbezug zurückliefern.

Quelle: <https://www.orgavision.com/loesungen/zusatzmodule/mcp-schnittstelle>

## Nutzungsbild

1. krisensicherOS unterstützt die Erstellung oder Überarbeitung eines Governance-Artefakts.
2. Fachlich verantwortliche Personen prüfen Inhalt, Datenklasse, Zielgruppe, Owner, Reviewzyklus und Human Gates.
3. Nur freigegebene Inhalte werden in Orgavision oder einem vergleichbaren Managementsystem-/QM-Wissenssystem veröffentlicht.
4. Orgavision stellt diese Inhalte über Rollen, Leserechte, Handbuchstrukturen und optional MCP-gestützte KI-Abfragen bereit.
5. Mitarbeitende können freigegebene Informationen im Arbeitskontext finden und nutzen, statt Dokumente in isolierten Ablagen zu suchen.

## Geeignete Inhalte

Geeignet sind insbesondere:

- freigegebene Rollen- und Verantwortlichkeitsbeschreibungen,
- Prozess- und Routinebeschreibungen,
- Management-Review- und Evidence-Routinen,
- freigegebene FAQ- und Schulungsinhalte,
- Entscheidungslogiken und Eskalationswege,
- Verweise auf öffentliche Regulierungsquellen und interne Registereinträge.

Nicht geeignet sind:

- ungeprüfte KI-Entwürfe,
- echte Personen-, Kunden-, Vertrags-, Incident- oder Secret-Inhalte ohne passende Freigabe,
- lizenzpflichtige Normtexte oder normnahe Ersatztexte,
- Rechts-, Datenschutz-, Zertifizierungs- oder Konformitätszusagen,
- Inhalte ohne Owner, Reviewzyklus oder Zielgruppe.

## Human Gates vor Veröffentlichung

Vor der Veröffentlichung in Orgavision oder vor der Bereitstellung über MCP müssen geprüft sein:

1. **Owner:** Wer ist fachlich verantwortlich?
2. **Zielgruppe:** Wer darf die Information sehen und nutzen?
3. **Datenklasse:** Welche Inhalte dürfen in Orgavision und in angebundene KI-Abfragen gelangen?
4. **Freigabe:** Wer gibt Inhalt, Sprache und Verteilung frei?
5. **Reviewzyklus:** Wann wird der Inhalt überprüft?
6. **Grenzen:** Ist klar, dass die Information keine Rechtsberatung, Datenschutzberatung oder Konformitätszusage ersetzt?
7. **Leserechte:** Sind Orgavision-Rollen und Berechtigungen passend gesetzt?

## Prompt für den Start

```text
Nutze krisensicherOS, um ein freigegebenes Orgavision-/MCP-taugliches Artefakt vorzubereiten.

Kontext:
- Thema: <NIS2 / ISMS / Evidence Review / Incident Readiness / Management Review>
- Zielgruppe in der Organisation: <Rolle/Team>
- Geplanter Ablageort oder Handbuchbereich in Orgavision: <Bereich>
- Datenklasse: <öffentlich / intern / vertraulich nach Freigabe>

Arbeite in drei Schritten:
1. Stelle zuerst Klärungsfragen zu Owner, Zielgruppe, Leserechten, Human Gates und Reviewzyklus.
2. Erstelle danach einen public-safe bzw. freigabefähigen Entwurf mit klarer Betriebslogik.
3. Markiere alle Punkte, die vor Veröffentlichung in Orgavision menschlich geprüft werden müssen.

Keine Rechtsberatung, keine Datenschutzberatung, keine Konformitäts- oder Zertifizierungszusage. Keine echten Personen-, Kunden-, Vertrags-, Incident-, Secret- oder lizenzpflichtigen Norminhalte übernehmen.
```

## Adapter-Grenze

Dieser Adapter dokumentiert einen Integrations- und Betriebsansatz. Er ersetzt keine Orgavision-Konfiguration, keine Berechtigungsprüfung, keine Datenschutzbewertung und keine fachliche Freigabe. Die konkrete MCP-Einrichtung muss in der jeweiligen Orgavision- und KI-Umgebung durch berechtigte Administratoren erfolgen.
