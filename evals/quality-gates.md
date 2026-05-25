<!-- kso:product-relevance
repo-scope: product
classification: quality-evaluation
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; product-safety; release-readiness
-->

# krisensicherOS Qualitätsgates v1.0

Stand: 2026-05-23

Diese Gates gelten für öffentliche Repo-Artefakte: Agentenprofile, Skills, Templates, Playbooks, Workflows, Beispiele, Adapter, Quellenregister und Dokumentation.

## 1. Universal Gates

### U1 — Public-Safe Gate

Prüffragen:

- Enthält das Artefakt echte Personen-, Kunden- oder Organisationsdaten?
- Enthält es private Workspace-, Chat-, Runtime- oder interne Agentendetails?
- Enthält es Secrets, Tokens, Zugangsdaten oder technische Interna?
- Enthält es vertrauliche Vertragsinhalte oder lizenzpflichtige Normtexte?

Pass-Kriterium:

- Nur fiktive Beispiele, öffentliche Quellen, Metadaten, eigene Zusammenfassungen oder leere Nutzerfelder.

Stop-Kriterium:

- Jede echte oder vertrauliche Information, die nicht ausdrücklich für Veröffentlichung freigegeben ist.

### U2 — Claim-Safety Gate

Prüffragen:

- Behauptet das Artefakt Rechtsberatung, Datenschutzberatung oder verbindliche Auslegung?
- Behauptet es NIS2-Konformität, ISO-Zertifizierungsfähigkeit oder Sicherheitsgarantie?
- Klingt es so, als könne ein Agent menschliche Verantwortung übernehmen?

Pass-Kriterium:

- Grenzen sind sichtbar; menschliche Prüfung und Entscheidung bleiben explizit.

Stop-Kriterium:

- Jede Konformitäts-, Zertifizierungs-, Rechts- oder Sicherheitsgarantie.

### U3 — Betriebslogik-Gate

Prüffragen:

- Wer nutzt das Artefakt?
- Wann wird es ausgelöst?
- Welche Inputs braucht es?
- Welche Schritte führt es aus?
- Welcher Output entsteht?
- Welche Evidenz entsteht?
- Wer reviewed es und in welcher Kadenz?

Pass-Kriterium:

- Das Artefakt ist in einer echten Governance-Routine nutzbar.

Stop-Kriterium:

- Reine Dokumentenvorlage ohne Rolle, Trigger, Entscheidung, Evidenz oder Review.

### U4 — Empowerment-Gate

Prüffragen:

- Hilft das Artefakt Nutzern, eigene Fähigkeiten aufzubauen?
- Erklärt es Entscheidungen, Grenzen und Prüfpunkte?
- Vermeidet es Beratungsabhängigkeit oder Agentenmagie?

Pass-Kriterium:

- Nutzer können das Artefakt nachvollziehen, anpassen und kritisch prüfen.

Stop-Kriterium:

- Blackbox-Output ohne Lern-, Prüf- oder Anpassungsmöglichkeit.

### U5 — Workload-Gate

Prüffragen:

- Reduziert das Artefakt Arbeit oder erhöht es Entscheidungsfähigkeit?
- Erzeugt es unnötige Meetings, Listen oder Reviews?
- Sind Owner und Nutzen klar?

Pass-Kriterium:

- Aufwand ist begründet und operativ nützlich.

Stop-Kriterium:

- Bürokratie ohne Risikoreduktion, Evidenznutzen oder Entscheidungsbezug.

### U6 — Portabilitäts-Gate

Prüffragen:

- Ist das kanonische Artefakt toolneutral?
- Sind Claude-, Codex-, OpenClaw-, Hermes- oder andere Adapter nur Ableitungen?
- Enthält das Artefakt keine privaten Pfade, lokalen Accounts oder Runtime-Details?

Pass-Kriterium:

- Fachlogik lebt im kanonischen Artefakt; Adapter bleiben dünn.

Stop-Kriterium:

- Fachlogik nur in einem Tool-Adapter oder mit nicht portablen Annahmen.

## 2. Artefakt-spezifische Gates

### A1 — Agentenprofil-Gate

Zusätzlich prüfen:

- YAML-Frontmatter vollständig,
- Mandat klar unterscheidbar,
- `Wann verwenden` und `Wann nicht verwenden` vorhanden,
- Inputs/Outputs konkret,
- Success Metrics prüfbar,
- Grenzen und rote Linien vorhanden,
- Handoff-Protokoll ausführbar,
- Human-in-the-loop sichtbar,
- Manifest-Eintrag vorhanden.

### A2 — Skill-Gate

Zusätzlich prüfen:

- `SKILL.md` vorhanden,
- Zweck und Scope klar,
- Inputs, Ablauf, Outputs und Verification definiert,
- menschliche Freigaben benannt,
- Beispiel ohne echte Daten,
- kein Ersatz für Rechts-, Datenschutz- oder Managemententscheidung.

### A3 — Template-Gate

Zusätzlich prüfen:

- Trigger, Nutzer, Input, Ablauf, Output, Evidenz und Grenzen vorhanden,
- Felder sind operativ nützlich,
- keine leeren Formularfriedhöfe,
- klare Hinweise für Anpassung und Review.

### A4 — Playbook-Gate

Zusätzlich prüfen:

- Szenario und Ziel klar,
- Rollen und Eskalationen definiert,
- Entscheidungs- und Kommunikationspunkte enthalten,
- After-Action-/Lessons-Learned-Schritt vorhanden,
- keine Live-Incident-Anmaßung.

### A5 — Workflow-Gate

Zusätzlich prüfen:

- Workflow verbindet Agenten, Skills, Templates, Register und Freigaben,
- Stop-/Eskalationspunkte enthalten,
- Inputs/Outputs je Schritt klar,
- menschliche Entscheidungen nicht automatisiert,
- Handoff-Protokoll ausführbar.

### A6 — Beispiel-Gate

Zusätzlich prüfen:

- Beispiel ist vollständig fiktiv,
- keine realistischen Kundennamen, Telefonnummern, Domains oder Einzeldaten,
- Annahmen sind als Annahmen markiert,
- Beispiel zeigt gute Nutzung, nicht perfekte Scheinsicherheit.

### A7 — Adapter-Gate

Zusätzlich prüfen:

- Adapter verweist auf kanonische Quelle,
- keine abweichende Fachlogik,
- keine privaten Pfade oder lokalen Workspace-Annahmen,
- tool-spezifische Hinweise sind minimal und rein technisch.

### A8 — Quellen-/Register-Gate

Zusätzlich prüfen:

- öffentliche Quellen sind als Referenzanker dokumentiert,
- lizenzpflichtige Normen nur als Metadaten/Verweise/Mappings,
- vertrauliche Vorgaben nur als redigierte Zusammenfassung oder privater Nutzerinhalt,
- Owner, Status, Review-Frequenz und zulässige Agentennutzung sind markiert.

## 3. Ergebnisstufen

- **pass** — Artefakt erfüllt Gates.
- **pass with notes** — Artefakt ist nutzbar, aber offene menschliche Prüfung oder Verbesserung ist dokumentiert.
- **stop** — Artefakt darf nicht veröffentlicht oder genutzt werden, bevor der markierte Punkt geklärt ist.

## 4. Prüfnachweis-Vorlage

```text
Artefakt:
Artefakttyp:
Geprüfte Gates:
Pass:
Pass with notes:
Stop-Punkte:
Korrekturen:
Menschliche Prüfung erforderlich:
Ergebnis:
```

## 5. Harte Stop-Punkte

Immer stoppen bei:

- echten Personen-, Kunden- oder Organisationsdaten,
- Secrets oder Zugangsdaten,
- vertraulichen Vertragsinhalten,
- lizenzpflichtigen Normtexten,
- Rechts- oder Datenschutzberatung,
- Konformitäts-, Zertifizierungs- oder Sicherheitsgarantien,
- externer Veröffentlichung ohne Freigabe,
- Lizenz- oder Disclaimer-Änderung ohne Freigabe.
