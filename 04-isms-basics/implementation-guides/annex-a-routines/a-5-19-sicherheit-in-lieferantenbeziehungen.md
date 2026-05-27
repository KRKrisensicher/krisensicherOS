
# A.5.19 — Sicherheit in Lieferantenbeziehungen

## Zweck

Lieferantenbeziehungen erzeugen Sicherheitsabhängigkeiten: externe Dienste verarbeiten Informationen, betreiben Systeme, liefern Software, haben Zugriff auf Umgebungen oder beeinflussen die Verfügbarkeit kritischer Prozesse. Diese Routine sorgt dafür, dass solche Beziehungen nicht nur beschafft, sondern risikobasiert ausgewählt, betrieben, reviewed und beendet werden.

Der Kern ist eine Lieferanten-Governance, die Sicherheitsrisiken vor, während und nach der Zusammenarbeit sichtbar hält: Wer ist kritisch? Welche Zugriffe, Daten und Dienste sind betroffen? Welche Nachweise liegen vor? Welche Probleme werden eskaliert?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Routine zur Sicherheitssteuerung von Lieferanten und Dienstleistern. Sie verbindet Beschaffung, Fachverantwortung, Informationssicherheit, Datenschutz, Legal, Betrieb und Management zu einem gemeinsamen Umgang mit Lieferantenrisiken.

## Typische Risiken

- Wenn ein Dienstleister Zugriff auf Systeme oder Daten erhält, ohne risikobasiert bewertet zu sein, entstehen unerkannte Angriffs- und Abhängigkeitsflächen.
- Wenn kritische Lieferanten nicht inventarisiert sind, fehlen Owner, Reviewtermine und Eskalationswege.
- Wenn Sicherheitsanforderungen erst nach Vertragsabschluss geklärt werden, sind Nachverhandlungen schwierig oder teuer.
- Wenn Leistungs- oder Sicherheitsprobleme nicht in Reviews einfließen, bleibt die tatsächliche Lieferantenlage unsichtbar.
- Wenn Subdienstleister oder Cloud-Abhängigkeiten nicht betrachtet werden, entstehen blinde Flecken in der Lieferkette.
- Wenn Offboarding fehlt, bleiben Zugänge, Datenkopien oder Schnittstellen nach Vertragsende aktiv.

## Trigger

- neuer Lieferant, neuer Dienst, Proof of Concept, Ausschreibung oder Vertragsverlängerung.
- Änderung von Leistungsumfang, Datenarten, Systemzugriff, Standort, Subdienstleister oder Betriebsmodell.
- Sicherheitsereignis, Schwachstelle, Ausfall, Serviceproblem oder Auditfinding beim Lieferanten.
- turnusmäßiger Lieferantenreview oder Managementfrage zu kritischen Abhängigkeiten.
- geänderte Risikolage, neue regulatorische Betroffenheit oder neuer Schutzbedarf.
- Beendigung, Kündigung, Migration oder Wechsel eines Lieferanten.
- externe Anfrage, Kundenanforderung oder interne Prüfung zur Lieferantensteuerung.

## Rollen und Verantwortung

- **Service Owner / Fachverantwortlicher:** bewertet Geschäftsbedarf, Kritikalität und Leistungserwartung.
- **Einkauf / Vendor Management:** steuert Auswahl, Register, kommerzielle Abstimmung und Lieferantenkommunikation.
- **ISMS-Owner / Security-Rolle:** definiert Sicherheitsbewertung, Mindestnachweise, Reviewlogik und Risikohandling.
- **IT-/Plattform Owner:** bewertet technische Integration, Zugriff, Schnittstellen, Betrieb und Offboarding.
- **Datenschutz / Legal:** prüft personenbezogene Daten, Vertragsfragen, Datenschutzrollen, Klauseln und rechtliche Risiken.
- **BCM-/Krisenrolle:** bewertet Abhängigkeiten für kritische Prozesse und Notfallfähigkeit.
- **Management:** entscheidet über kritische Lieferanten, akzeptierte Restrisiken, Budget, Alternativen und Eskalationen.

## Implementierung

### Minimalstart

Ziel: kritische Lieferanten sichtbar, verantwortet und reviewfähig machen.

1. Die Organisation erstellt ein Lieferantenregister für sicherheitsrelevante Dienste: Name, Service, Owner, Daten-/Systembezug, Kritikalität, Reviewdatum.
2. Neue Lieferanten werden vor Freigabe kurz bewertet: Welche Daten, Zugriffe, Dienste, Standorte und Abhängigkeiten sind betroffen?
3. Kritische Lieferanten erhalten einen benannten Service Owner und einen Security-Ansprechpartner.
4. Mindestnachweise werden angefordert oder begründet ersetzt: Sicherheitsbeschreibung, Zertifikats-/Prüfnachweis, Fragebogen, Vertragsanlage oder technische Beschreibung.
5. Offene Risiken werden im Maßnahmen- oder Risikoregister geführt.
6. Vertragsende oder Dienstleisterwechsel löst Offboarding von Zugängen, Daten und Schnittstellen aus.

Minimaler Nachweis:

- Lieferantenregister mit Kritikalität und Owner,
- einfache Sicherheitsbewertung vor Nutzung,
- Nachweis angefragter oder bewerteter Sicherheitsinformationen,
- Risiko- oder Maßnahmenlog,
- Offboarding-Check bei Ende der Beziehung.

### Solide Praxis

Ziel: Lieferantensteuerung wird risikobasiert in Beschaffung und Betrieb integriert.

1. Lieferanten werden nach Kritikalität klassifiziert: Zugang zu Informationen, Systemzugriff, Verfügbarkeitsrelevanz, Subdienstleister, Wiederherstellbarkeit.
2. Beschaffung startet Security-, Datenschutz- und Legal-Handoffs früh genug vor Vertragsabschluss.
3. Kritische Lieferanten werden regelmäßig reviewed: Leistung, Sicherheitsereignisse, Nachweise, offene Maßnahmen, Subdienstleisteränderungen, Exit-Fähigkeit.
4. Sicherheitsanforderungen werden mit A.5.20 in Lieferantenvereinbarungen überführt.
5. IT-Lieferkettenrisiken wie Software, Cloud, Managed Services oder Updates werden mit A.5.21 verbunden.
6. Lieferantenereignisse fließen in Incident Response, Schwachstellenmanagement, BCM und Management Review.
7. Ausnahmen erhalten Laufzeit, Kompensationsmaßnahmen und Entscheidung durch die passende Rolle.

Starke Evidenz:

- risikobasiertes Lieferantenregister,
- Bewertungsbogen oder Due-Diligence-Notiz,
- Reviewprotokolle kritischer Lieferanten,
- offene Maßnahmen und Eskalationen,
- Offboarding- oder Exit-Nachweise,
- Managemententscheidung bei kritischer Abhängigkeit oder Restrisiko.

### Fortgeschritten

Ziel: Lieferantenbeziehungen werden als laufendes Abhängigkeits- und Risikomanagement betrieben.

1. Lieferantenregister, Assetregister, Vertragsmanagement, BCM und Risikoanalyse sind miteinander verbunden.
2. Kritische Lieferanten erhalten definierte Sicherheits- und Resilienzkennzahlen, Reviewkalender und Eskalationspfade.
3. Subdienstleister, Konzentrationsrisiken, regionale Abhängigkeiten und Exit-Szenarien werden regelmäßig betrachtet.
4. Security-Ereignisse, Schwachstellenmeldungen und Leistungsprobleme werden in gemeinsame Verbesserungspläne überführt.
5. Management sieht entscheidungsfähige Informationen: kritische Abhängigkeiten, nicht erfüllte Anforderungen, Exit-Risiken, offene Ausnahmen und Ressourcenbedarf.
6. Lieferantenwechsel, Notfallbetrieb oder Exit werden bei kritischen Diensten geübt oder zumindest tabletop-basiert durchgespielt.

## Ablauf als Routine

1. **Bedarf entsteht:** Fachbereich, IT oder Projekt will einen Lieferanten nutzen oder ändern.
2. **Vorprüfung durchführen:** Daten, Zugriff, Kritikalität, Subdienstleister, Verfügbarkeit und Exit-Relevanz erfassen.
3. **Kritikalität einstufen:** Standardlieferant, sicherheitsrelevant, kritisch oder strategisch abhängig.
4. **Handoffs auslösen:** Security, Datenschutz, Legal, IT, BCM und Einkauf je nach Risiko einbinden.
5. **Nachweise bewerten:** Fragebogen, Zertifikate, Sicherheitskonzept, technische Beschreibung, Auditbericht oder alternative Evidenz prüfen.
6. **Entscheiden:** freigeben, Anforderungen nachschärfen, Ausnahme befristen, Managemententscheidung einholen oder Nutzung stoppen.
7. **Betreiben und reviewen:** Leistung, Sicherheitsereignisse, Änderungen, Nachweise und offene Maßnahmen regelmäßig prüfen.
8. **Änderungen steuern:** neue Zugriffe, Datenarten, Subdienstleister oder Standorte neu bewerten.
9. **Beenden:** Zugänge entziehen, Datenrückgabe/-löschung nachverfolgen, Schnittstellen deaktivieren und Lessons Learned dokumentieren.

## Entscheidungen

- Welche Lieferanten sind sicherheitsrelevant oder kritisch?
- Welche Mindestinformationen müssen vor Nutzung vorliegen?
- Wann darf ein Lieferant trotz offener Sicherheitsfragen starten?
- Wer akzeptiert Lieferantenrisiken und für welchen Zeitraum?
- Welche Lieferanten brauchen regelmäßige Reviews oder Managementsicht?
- Welche Exit- oder Ersatzoptionen sind für kritische Dienste erforderlich?
- Wie werden Subdienstleisteränderungen und Sicherheitsereignisse behandelt?

## Evidenz

### Starke Evidenz

- aktuelles Lieferantenregister mit Owner, Kritikalität, Daten-/Systembezug und Reviewdatum,
- dokumentierte Sicherheitsbewertung vor Nutzung,
- geprüfte Lieferantennachweise oder begründete Ersatzbewertung,
- Reviewprotokolle mit Maßnahmen und Entscheidungen,
- Nachweise über Offboarding, Zugangsentzug und Daten-/Schnittstellenbehandlung,
- Eskalationen und Managemententscheidungen bei kritischen Abhängigkeiten,
- Verknüpfung zu Risiko-, Maßnahmen-, Incident- oder BCM-Register.

### Schwache Evidenz

- reine Kreditorenliste ohne Sicherheitsbezug,
- Zertifikat eines Lieferanten ohne Scopeprüfung,
- Fragebogen ohne Bewertung oder Maßnahmen,
- Vertrag im Archiv ohne verantwortlichen Service Owner,
- Lieferantenreview als Einkaufsroutine ohne Sicherheits- oder Verfügbarkeitsfragen.

### Evidenzlücken

- kritische SaaS- oder Managed-Service-Lieferanten fehlen im Register,
- kein Owner für Lieferantenrisiko,
- keine Bewertung vor produktiver Nutzung,
- Subdienstleister unbekannt oder nicht verfolgt,
- Vertragsende ohne Nachweis zu Zugangsentzug und Datenbehandlung,
- offene Sicherheitsanforderungen ohne Eskalation.

## Wirksamkeitsprüfung

Prüffragen:

- Sind sicherheitsrelevante und kritische Lieferanten vollständig genug identifiziert?
- Ist für jeden kritischen Lieferanten klar, welcher Service, welche Daten und welche Zugriffe betroffen sind?
- Werden Security-, Datenschutz-, Legal- und BCM-Handoffs vor relevanten Entscheidungen ausgelöst?
- Führen Reviews zu Maßnahmen, Eskalationen oder bewussten Risikoentscheidungen?
- Werden Lieferantenänderungen und Subdienstleisteränderungen erneut bewertet?
- Ist Offboarding bei Vertragsende nachweisbar?
- Erkennt das Management kritische Abhängigkeiten und Exit-Risiken?

Mögliche Kennzahlen:

- Anteil kritischer Lieferanten mit aktuellem Review,
- Lieferanten ohne Owner oder Kritikalität,
- offene Maßnahmen je kritischem Lieferanten,
- überfällige Nachweise oder Reviews,
- Sicherheitsereignisse mit Lieferantenbezug,
- offene Offboarding-Punkte nach Vertragsende,
- kritische Lieferanten ohne dokumentierte Exit-Überlegung.

## BSIG-/NIS2-Anschluss

Sicherheit in Lieferantenbeziehungen ist anschlussfähig an NIS2-orientierte Themen wie Lieferkettensicherheit, Risikomanagement, Dienstleistersteuerung, Business Continuity, Incident-Fähigkeit und Managementaufsicht über wesentliche Abhängigkeiten.

Für BSIG-/NIS2-Betroffenheit sollte die Organisation im Anforderungsregister prüfen, welche Lieferanten, Dienste, Nachweise und Managemententscheidungen relevant sind. Dieses Artefakt ersetzt keine rechtliche Auslegung, Vertragsberatung oder verbindliche Prüfung der Anwendbarkeit.

## Grenzen

- Dieses Artefakt ist kein Vertragsmuster und keine Rechtsberatung.
- Es ersetzt keine Datenschutzprüfung, Auftragsverarbeitungsbewertung oder Verhandlung durch qualifizierte Rollen.
- Es trifft keine Aussage, dass ein Zertifikat oder Fragebogen ausreichende Sicherheit belegt.
- Keine Zertifizierungs-, Konformitäts- oder Sicherheitsgarantie.
- Keine ISO-27002-Texte und keine echten Lieferanten-, Kunden- oder Vertragsdaten in Beispielen.

## Handoffs

- **Einkauf-/Vendor-Management-Handoff:** Auswahl, Register, Lieferantenkommunikation, Vertragsverlängerung und Kündigung.
- **Legal-/Datenschutz-Handoff:** Vertragsgestaltung, personenbezogene Daten, Datenschutzrollen, Melde- und Informationspflichten.
- **Security-/ISMS-Handoff:** Sicherheitsbewertung, Nachweise, Ausnahmen, Risikoregister und Reviewlogik.
- **IT-/Access-Handoff:** technische Integration, Schnittstellen, Adminzugriffe, externe Konten und Offboarding.
- **BCM-/Krisen-Handoff:** kritische Abhängigkeiten, Ausfallrisiken, Exit-Szenarien und Notfallbetrieb.
- **Incident-Handoff:** Sicherheitsereignisse, Schwachstellenmeldungen oder Ausfälle mit Lieferantenbezug.
- **Management-Handoff:** kritische Abhängigkeit, nicht erfüllte Anforderungen, Restrisiko, Budget oder Exit-Entscheidung.
- **Audit-/Evidence-Handoff:** fehlende Nachweise, unklare Scopeprüfung oder nicht dokumentierte Reviews.

## Typische Fehler

- Lieferantensteuerung beginnt erst nach Vertragsunterschrift.
- Eine Kreditorenliste wird mit einem Sicherheitsregister verwechselt.
- Zertifikate werden gesammelt, aber ihr Scope wird nicht zum genutzten Service geprüft.
- Kritische Lieferanten haben keinen fachlichen Owner.
- Subdienstleister und Cloud-Abhängigkeiten bleiben außerhalb der Betrachtung.
- Sicherheitsprobleme werden als reine Servicequalität behandelt und nicht ins Risikomanagement überführt.
- Offboarding konzentriert sich auf Vertragsende, vergisst aber Zugänge, Datenkopien und Schnittstellen.

## Fiktives Mini-Beispiel

Ein fiktiver Mittelständler möchte ein neues SaaS-Tool für Kundenkommunikation nutzen. Der Fachbereich meldet den Bedarf an Einkauf und ISMS-Owner. Die Vorprüfung zeigt personenbezogene Daten, externe Konten und Abhängigkeit im Supportprozess. Der Lieferant wird als sicherheitsrelevant eingestuft. Vor Start werden Sicherheitsinformationen bewertet, Datenschutz und Legal eingebunden und offene Punkte in eine Vertragsanlage überführt. Nach sechs Monaten prüft der Service Owner Nutzung, offene Maßnahmen und Subdienstleisterhinweise.

Evidenz:

- Lieferantenregistereintrag mit Kritikalität,
- Sicherheitsvorprüfung,
- Nachweise und Bewertungsnotiz,
- Datenschutz-/Legal-Handoff,
- Maßnahmenlog,
- Reviewprotokoll nach sechs Monaten.
