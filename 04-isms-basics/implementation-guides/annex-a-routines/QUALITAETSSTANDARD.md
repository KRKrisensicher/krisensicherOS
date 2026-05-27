
# Qualitätsstandard für Anhang-A-Routinen

## Zweck

Dieser Standard beschreibt, wie krisensicherOS aus den 93 Anhang-A-orientierten Controls hochwertige Umsetzungsartefakte macht: nicht als Normersatz, sondern als betriebliche Anleitung für Rollen, Routinen, Evidenz, Entscheidungen und Verbesserungen.

Die Artefakte sollen Organisationen helfen, von einer abstrakten Control-Referenz zu einer prüfbaren Arbeitsweise zu kommen. Sie dürfen keine ISO-27002-Formulierungen übernehmen, keine Zertifizierungsfähigkeit behaupten und keine Rechts- oder Datenschutzberatung ersetzen.

## Zielbild

Ein gutes Control-Artefakt beantwortet sieben praktische Fragen:

1. **Warum gibt es diese Kontrolle?** Welches Risiko, welche Fehlfunktion oder welcher Governance-Bruch wird adressiert?
2. **Wann wird sie relevant?** Welche Trigger lösen Arbeit, Review oder Entscheidung aus?
3. **Wer handelt?** Welche Rollen betreiben, prüfen, entscheiden oder eskalieren?
4. **Wie sieht die Routine aus?** Welche Schritte sind im Alltag realistisch umsetzbar?
5. **Welche Entscheidungen entstehen?** Welche Zielkonflikte, Ausnahmen, Ressourcenfragen oder Restrisiken müssen geklärt werden?
6. **Welche Evidenz ist belastbar?** Welche Nachweise zeigen Betrieb und Wirksamkeit, welche sind nur Papier?
7. **Wo sind Grenzen und Handoffs?** Wann braucht es Legal, Datenschutz, Management, Einkauf, HR, BCM, Incident Response, Audit oder technische Spezialisten?

## Nicht-Ziel

Die Artefakte sind ausdrücklich nicht:

- ISO-27002-Ersatztext,
- Zertifizierungsleitfaden,
- Rechtsgutachten,
- Datenschutzbewertung,
- Auditgarantie,
- technische Hardening-Baseline,
- vollständige Policy-Sammlung,
- mechanische Pflichtliste für jede Organisation.

## Qualitätskriterien pro Artefakt

### 1. Eigene Control-Interpretation

Das Artefakt beschreibt den Zweck des Controls in krisensicherOS-Sprache. Es darf Control-ID und eigene Arbeitstitel nutzen, aber keine lizenzpflichtigen Normformulierungen nachbilden.

Gute Qualität:

- beschreibt das zugrunde liegende Betriebsproblem,
- erklärt den Nutzen für Risiko-, Entscheidungs- und Evidenzfähigkeit,
- bleibt verständlich für CISO/ISB, Management, Fachbereich und Control Owner.

Schwache Qualität:

- klingt wie eine umformulierte Normanforderung,
- bleibt bei generischen Sätzen,
- nennt keine Betriebsroutine.

### 2. Risikobezug

Jedes Artefakt benennt typische Risiken, ohne eine Organisation zu erfinden. Risiken werden als Ausgangspunkt für die Ausgestaltung genutzt.

Mindeststruktur:

```text
Wenn [Bedrohung/Ereignis] auf [Schwachstelle] bei [Asset/Prozess/Rolle] trifft,
dann kann [Auswirkung] entstehen.
```

### 3. Triggerlogik

Jede Routine braucht konkrete Auslöser. Trigger verhindern, dass Controls nur jährlich als Papierübung betrachtet werden.

Typische Trigger:

- neuer Service, neues System, neuer Dienstleister,
- Rollenwechsel, Eintritt, Austritt,
- Risiko- oder Maßnahmenreview,
- Sicherheitsereignis oder Schwachstelle,
- Auditfeststellung oder interne Prüfung,
- Vertrags-, Architektur- oder Prozessänderung,
- Managemententscheidung,
- geplanter Reviewtermin.

### 4. Rollen- und Entscheidungslogik

Jedes Artefakt benennt mindestens:

- primären Owner,
- beteiligte Rollen,
- Reviewer,
- Eskalationspunkt,
- Entscheidungsgremium oder Management-Handoff, falls relevant.

Wichtig: Agenten dürfen vorbereiten, strukturieren und fragen. Risikoakzeptanz, Ressourcenentscheidung, Rechts-/Datenschutzbewertung und externe Kommunikation bleiben menschliche Entscheidungen.

### 5. Implementierung in drei Reifegraden

Jedes hochwertige Artefakt enthält drei Umsetzungsstufen:

- **Minimalstart:** kleinster nutzbarer Betriebsmodus mit Owner, Scope, Ablauf und Evidenz.
- **Solide Praxis:** wiederholbare Routine mit Register, Review, Ausnahmen, Maßnahmen und Wirksamkeitsprüfung.
- **Fortgeschritten:** Integration in Tools, Monitoring, Metriken, Automatisierung, Abhängigkeiten und Management Reporting.

Die Stufen sind keine Zertifizierungsreifegrade. Sie helfen bei Priorisierung und Workload-Steuerung.

### 6. Evidenzqualität

Evidenz wird nicht als Dokumentenablage verstanden, sondern als Nachweis einer betriebenen Routine.

Jedes Artefakt unterscheidet:

- **starke Evidenz:** zeigt tatsächliche Durchführung, Review, Entscheidung oder Wirksamkeit,
- **schwache Evidenz:** zeigt nur Absicht, veraltete Regel oder unklare Zuständigkeit,
- **fehlende Evidenz:** Entscheidung oder Betriebsroutine ist nicht nachvollziehbar.

### 7. Wirksamkeitsprüfung

Jedes Artefakt enthält Prüffragen, mit denen ein Reviewer erkennen kann, ob die Kontrolle mehr ist als Papier.

Gute Fragen prüfen:

- Aktualität,
- Abdeckung,
- Ausnahmebehandlung,
- Reaktionsfähigkeit,
- Nachvollziehbarkeit,
- tatsächliche Risikoänderung,
- Managemententscheidungen bei Zielkonflikten.

### 8. BSIG-/NIS2-Bezug

BSIG-/NIS2-Bezüge werden als Anschlussstellen beschrieben, nicht als Rechtsauslegung.

Zulässig:

- Mapping auf Themen wie Risikomanagement, Incident Handling, Business Continuity, Lieferkettensicherheit, Cyberhygiene, Schulung, Kryptografie, Zugriffsschutz, Schwachstellenmanagement, sichere Entwicklung.
- Hinweis auf notwendige organisationsspezifische Prüfung.

Nicht zulässig:

- verbindliche Aussage, dass eine Kontrolle eine konkrete gesetzliche Pflicht erfüllt,
- Rechtsberatung,
- Meldepflichtbewertung ohne Human Review,
- Scheinkonformität.

### 9. Typische Fehler

Jedes Artefakt benennt typische Fehlmuster. Das ist wichtig, weil Nutzer sonst Papierkontrollen bauen.

Beispiele:

- Policy vorhanden, aber niemand betreibt sie,
- Tool aktiv, aber keine Reviewroutine,
- Owner benannt, aber ohne Entscheidungskompetenz,
- Ausnahme dauerhaft, aber ohne Risikoakzeptanz,
- Evidenz liegt verstreut und ist nicht prüfbar,
- Management bekommt Kennzahlen ohne Entscheidungspunkt.

### 10. Handoffs

Jedes Artefakt definiert Handoffs, zum Beispiel:

- Legal / Datenschutz,
- HR / Betriebsrat,
- Einkauf / Vendor Management,
- IT-Betrieb / Plattformteam,
- Entwicklung / Product Owner,
- BCM / Krisenstab,
- Incident Response,
- Management Review,
- interne Prüfung / Audit,
- Evidence-Pack-Review.


## Reifemodell und Arbeitsstände

Produktartefakte führen keinen internen Arbeits-, Batch-, Agenten- oder Reviewstatus im Dokumentkörper. Nutzerorganisationen können eigene Umsetzungsstatus in ihrer SoA, ihrem Maßnahmenregister oder Evidence Pack führen. Interne Arbeitsstände des Repos gehören in Tracking- oder Reviewdateien außerhalb der Produktartefakte.

## Zielstruktur eines Goldstandard-Artefakts

```text
# A.x.y — Arbeitstitel

Zweck
Control-Ziel in Repo-Sprache
Typische Risiken
Trigger
Rollen und Verantwortung
Implementierung
  - Minimalstart
  - Solide Praxis
  - Fortgeschritten
Ablauf als Routine
Entscheidungen
Evidenz
  - starke Evidenz
  - schwache Evidenz
  - Evidenzlücken
Wirksamkeitsprüfung
BSIG-/NIS2-Anschluss
Grenzen
Handoffs
Typische Fehler
Fiktives Mini-Beispiel
```

## Review-Gate pro Artefakt

Vor Markierung als „reviewed“ muss jedes Artefakt diese Fragen bestehen:

```text
Public-safe: pass / notes / stop
Normtext-sicher: pass / notes / stop
Claim-safe: pass / notes / stop
Risikobezug klar: pass / notes / stop
Owner und Trigger klar: pass / notes / stop
Routine betreibbar: pass / notes / stop
Evidenz belastbar: pass / notes / stop
Wirksamkeitsprüfung möglich: pass / notes / stop
BSIG-/NIS2-Anschluss vorsichtig und plausibel: pass / notes / stop
Handoffs vollständig: pass / notes / stop
Workload angemessen: pass / notes / stop
Ergebnis: draft / reviewed / needs rework / stop
```

## Serienbearbeitung der 93 Artefakte

Die Bearbeitung erfolgt in Wellen:

1. **Goldstandard-Piloten:** A.5.15, A.6.3, A.8.8.
2. **Organisatorische Controls:** A.5.1 bis A.5.37.
3. **People Controls:** A.6.1 bis A.6.8.
4. **Physische Controls:** A.7.1 bis A.7.14.
5. **Technische und Entwicklungscontrols:** A.8.1 bis A.8.34.
6. **Konsistenzreview:** Begriffe, Rollen, Evidenztypen, NIS2-/BSIG-Anschluss, Handoffs.
7. **Finaler Claim- und Normtext-Safety-Check.**

## Definition of Done

Ein Artefakt ist erst „gut genug“, wenn es eine Organisation in die Lage versetzt,

- eine verantwortliche Rolle zu benennen,
- die Routine in bestehende Arbeit einzubauen,
- passende Evidenz zu erzeugen,
- offene Entscheidungen sichtbar zu machen,
- Risiken und Maßnahmen zu verknüpfen,
- Handoffs sauber auszulösen,
- und ohne Scheinkonformität zu arbeiten.
