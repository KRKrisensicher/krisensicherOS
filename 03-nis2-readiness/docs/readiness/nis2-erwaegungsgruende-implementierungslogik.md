
# NIS2-Erwägungsgründe: Implementierungslogik für Readiness

Stand: 2026-05-25

## Zweck

Diese Auswertung übersetzt die Erwägungsgründe der NIS2-Richtlinie in praktische Implementierungsfragen. Sie ist keine Rechtsauslegung und ersetzt keine Prüfung durch qualifizierte juristische Beratung.

Die NIS2-Richtlinie ist als Text hier verlinkt: <https://eur-lex.europa.eu/eli/dir/2022/2555/oj?locale=de>

## Warum die Erwägungsgründe wichtig sind

Die Erwägungsgründe erklären, welche Problemstellung die Richtlinie lösen soll. Für krisensicherOS werden daraus keine Rechtsclaims abgeleitet, sondern Implementierungsprinzipien:

- breite, sektorübergreifende Resilienz statt isolierter IT-Checkliste,
- risikobasierte Sicherheitsmaßnahmen statt rein formaler Dokumentation,
- Managementverantwortung statt Delegation ins Technikteam,
- Lieferketten- und Dienstleisterbezug,
- Meldefähigkeit und Krisenkommunikation,
- europäische Mindestharmonisierung bei nationaler Umsetzung,
- Aufsicht, Nachweisfähigkeit und wirksame Governance.

## Umsetzungsfelder aus den Erwägungsgründen

### 1. Einheitliches Mindestniveau

Implementierungsfrage:

- Gibt es eine gemeinsame Mindestlogik für Risikoanalyse, Maßnahmen, Evidenz, Review und Managemententscheidung?

Nötige Artefakte:

- Scope- und Einrichtungsartenprüfung,
- Risikomanagement-Routine,
- Maßnahmenbacklog,
- Evidence-Pack-Struktur,
- Management-Review-Routine.

### 2. Kritische und wichtige Dienste

Implementierungsfrage:

- Welche Leistungen, Standorte, Systeme, Datenflüsse und Drittanbieter tragen zur Erbringung wesentlicher oder wichtiger Dienste bei?

Nötige Artefakte:

- Service-/Prozessinventar,
- Abhängigkeitskarte,
- Lieferanten-/Dienstleisterregister,
- Business-Impact-Notiz,
- technische Asset- und Systemlandkarte als interne, nicht öffentliche Evidenz.

### 3. Risikomanagement als Betriebsroutine

Implementierungsfrage:

- Wird Risiko regelmäßig bewertet, priorisiert, behandelt und auf Wirksamkeit geprüft?

Nötige Artefakte:

- Risikoanalyse-Methodik,
- Risikoregister,
- Maßnahmenverfolgung,
- Wirksamkeitsprüfung,
- Managemententscheidung bei Restrisiko.

### 4. Incident- und Meldefähigkeit

Implementierungsfrage:

- Kann die Organisation Sicherheitsvorfälle erkennen, bewerten, eskalieren und fristgerecht melden?

Nötige Artefakte:

- Incident-Triage-Regel,
- Melde- und Eskalationsmatrix,
- Rollenkarte für 24/72-Stunden-/Follow-up-Logik,
- Kommunikationsfreigaben,
- Übungs- und Lessons-Learned-Protokolle.

### 5. Lieferkette und Dienstleister

Implementierungsfrage:

- Werden unmittelbare Anbieter, IT-Dienstleister, Cloud-/MSP-/MSSP-Abhängigkeiten und kritische Komponenten gesteuert?

Nötige Artefakte:

- Lieferantenregister,
- Kritikalitätsbewertung,
- Mindestanforderungen an Dienstleister,
- Nachweis-/Review-Routine,
- Exit-/Fallback-Überlegungen.

### 6. Managementverantwortung und Schulung

Implementierungsfrage:

- Gibt es eine verantwortliche Geschäftsleitungsroutine mit Wissen, Entscheidungsfähigkeit, Budget- und Priorisierungslogik?

Nötige Artefakte:

- Management-Review-Agenda,
- Schulungsnachweis Geschäftsleitung,
- Entscheidungslog,
- Risikoakzeptanzprozess,
- Ressourcen- und Maßnahmenentscheidung.

### 7. Nachweisbarkeit und Aufsicht

Implementierungsfrage:

- Kann die Organisation zeigen, welche Maßnahmen gelten, wer sie betreibt, wann sie geprüft wurden und welche Evidenz entsteht?

Nötige Artefakte:

- Evidence-Pack-Index,
- Kontroll- und Routinenbeschreibung,
- Reviewkalender,
- Findings-/Remediation-Prozess,
- Freigabe- und Änderungslog.

### 8. Digitale Dienste und Durchführungsverordnung (EU) 2024/2690

Implementierungsfrage:

- Fällt die Organisation in eine der von der Durchführungsverordnung adressierten digitalen Einrichtungsarten?

Wenn ja, muss NIS2-Readiness zusätzlich auswerten:

- technische und methodische Mindestanforderungen an Risikomanagementmaßnahmen,
- Kriterien für erhebliche Sicherheitsvorfälle,
- Nachweisfähigkeit der Risiko- und Maßnahmenprozesse,
- Schulung/Sensibilisierung,
- sektor- oder dienstspezifische Schwellenwerte für Incident-Bewertung.

## Praktischer Readiness-Schluss

Für tatsächliche Implementierung reicht kein Fragebogen allein. Nötig sind mindestens:

1. Vorab-Betroffenheitsprüfung mit Rechtsprüfungs-Hinweis.
2. Quellenregister mit NIS2, BSIG, Anlagen, EnWG und Durchführungsverordnung.
3. Service-/Sektor-/Einrichtungsarten-Mapping.
4. Risikomanagement- und Incident-Routine.
5. Lieferketten- und Dienstleisterroutine.
6. Evidence-Pack-Struktur.
7. Management-Review mit Entscheidungen und Schulungsnachweis.
8. Anwaltliche bzw. zuständige Rechtsprüfung der Betroffenheit und Pflichten.
