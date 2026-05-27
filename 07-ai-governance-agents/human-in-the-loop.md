
# Human-in-the-loop für krisensicherOS-Agenten

## Zweck

Dieses Dokument beschreibt, welche Entscheidungen bei der Nutzung von krisensicherOS-Agenten immer bei Menschen bleiben und wie Agentenarbeit kontrolliert in Governance-Routinen eingebettet wird.

Agenten strukturieren, prüfen und bereiten vor. Sie übernehmen keine Verantwortung.

## Grundregel

Jeder Agentenoutput braucht mindestens eine verantwortliche menschliche Rolle, wenn daraus eine Entscheidung, Freigabe, externe Aussage oder Änderung an realen Governance-Routinen entsteht.

## Human Gates

### H1 — Scope Gate

Vor Beginn klären Menschen:

- betroffene Organisationseinheit, Services oder Prozesse,
- Nicht-Scope,
- zulässige Daten und Quellen,
- gewünschter Output,
- verantwortlicher Owner.

### H2 — Source Gate

Menschliche Prüfung ist erforderlich bei:

- rechtlicher Anwendbarkeit,
- regulatorischer Auslegung,
- Kunden- oder Lieferantenvertragsauslegung,
- Datenschutzbewertung,
- lizenzpflichtigen Normen,
- unklarer Vertraulichkeit.

Agenten dürfen Quellen referenzieren, mappen und Fragen vorbereiten. Sie entscheiden nicht verbindlich über Bedeutung oder Pflicht.

### H3 — Risk Gate

Menschliche Prüfung ist erforderlich bei:

- Risikoakzeptanz,
- Priorisierung mit Ressourcenwirkung,
- Abweichungen von bestehenden Policies,
- wesentlichen Restrisiken,
- Eskalation an Management oder Gremien.

### H4 — Evidence Gate

Menschliche Prüfung ist erforderlich, wenn Evidenz:

- unvollständig oder veraltet ist,
- widersprüchlich ist,
- vertrauliche Informationen enthält,
- Grundlage für externe Aussagen oder Managemententscheidungen werden soll.

### H5 — Output Gate

Vor Nutzung oder Weitergabe prüfen Menschen:

- Sind Scope, Annahmen und Grenzen sichtbar?
- Sind Claims begrenzt?
- Gibt es keine Rechts-, Datenschutz-, Zertifizierungs- oder Konformitätszusage?
- Sind Owner, Review-Kadenz und nächster Schritt klar?
- Ist das Ergebnis public-safe oder nur intern nutzbar?

### H6 — External Gate

Immer menschliche Freigabe vor:

- Veröffentlichung,
- Versand an Kunden, Behörden, Auditoren oder Versicherer,
- Git Push in öffentliche Repos,
- Release-Tags,
- offiziellen Management- oder Board-Unterlagen.

## Human Gate Matrix

| Situation | Agent darf | Mensch muss |
| --- | --- | --- |
| neue Quelle | Metadaten erfassen, Fragen ableiten | Anwendbarkeit und Auslegung prüfen |
| NIS2-/ISMS-Gap | Lücke strukturieren, Evidenzbedarf ableiten | Risiko und Priorität entscheiden |
| Evidence Pack | Vollständigkeit und Traceability prüfen | Eignung für Entscheidung freigeben |
| Management Review | Agenda, Optionen, Risiken vorbereiten | Entscheidung treffen |
| Incident Readiness | Eskalationslogik und Übung vorbereiten | Live-Entscheidungen führen |
| Datenschutzschnittstelle | Prüffragen und Handoff vorbereiten | Datenschutzbewertung verantworten |
| Vertragsanforderung | Anforderungen als Metadaten strukturieren | Vertragsauslegung verantworten |

## Stop-Punkte

Agentenarbeit stoppt, wenn:

- echte vertrauliche Daten in öffentliche Artefakte geraten könnten,
- lizenzpflichtige Normtexte reproduziert werden sollen,
- eine verbindliche Rechts- oder Datenschutzbewertung verlangt wird,
- ein Agent eine Managemententscheidung treffen soll,
- externe Kommunikation ohne Freigabe vorbereitet wird,
- ein Ergebnis wie eine Garantie, Zertifizierung oder Konformitätsbestätigung klingt.

## Definition of Done

Human-in-the-loop ist erfüllt, wenn:

- verantwortliche menschliche Rolle benannt ist,
- Human Gates im Workflow sichtbar sind,
- offene Entscheidungen nicht geglättet wurden,
- Output-Grenzen und Annahmen dokumentiert sind,
- Handoff an Management, Legal, Datenschutz, Owner oder Reviewer klar ist.
