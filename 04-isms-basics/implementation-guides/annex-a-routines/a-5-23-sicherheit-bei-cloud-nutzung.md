
# A.5.23 — Sicherheit bei Cloud-Nutzung

## Zweck

Cloud-Nutzung verändert Verantwortlichkeiten, technische Kontrolle und Abhängigkeiten. Diese Routine hilft, Cloud-Dienste nicht nur zu beschaffen oder technisch einzurichten, sondern sicher zu betreiben: mit klarem Zweck, freigegebenem Einsatz, Verantwortungsmodell, Konfigurationskontrolle, Monitoring, Änderungsbewertung und Exit-Überlegung.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Governance-Routine für Cloud-Dienste. Sie weiß, welche Cloud-Dienste genutzt werden, wofür sie eingesetzt sind, welche Daten und Prozesse betroffen sind, wer intern verantwortlich bleibt und wie Risiken, Konfigurationen, Änderungen, Nachweise und Ausnahmen gesteuert werden.

## Typische Risiken

- Wenn Cloud-Dienste ohne Freigabe oder Owner genutzt werden, entstehen Schatten-IT, unklare Datenablagen und ungesteuerte Zugriffe.
- Wenn das Verantwortungsmodell nicht verstanden wird, bleiben Sicherheitsaufgaben zwischen Anbieter und Organisation liegen.
- Wenn Cloud-Konfigurationen nicht geprüft werden, können Daten unbeabsichtigt öffentlich, zu breit zugänglich oder unzureichend protokolliert sein.
- Wenn SaaS-Dienste nicht im Asset- und Lieferantenmanagement erscheinen, fehlen Risiko- und Exit-Entscheidungen.
- Wenn Cloud-Änderungen des Anbieters nicht bewertet werden, verändern sich Schutzmaßnahmen unbemerkt.

## Trigger

- neuer Cloud-Dienst, neues Tenant, neues Konto, neue Subscription oder neue SaaS-Nutzung.
- Änderung von Datenklasse, Nutzerkreis, Schnittstellen, Region, Anbieterfunktion oder Adminmodell.
- Cloud-Fehlkonfiguration, Sicherheitsmeldung, Schwachstellenhinweis, Incident oder Auditfinding.
- Vertrags-, Architektur-, Betriebs- oder Lieferantenänderung.
- Einführung neuer Cloud-Plattformfunktionen, Automatisierung oder externer Integrationen.
- turnusmäßiger Cloud-Service-, Berechtigungs-, Konfigurations- oder Kostenreview.

## Rollen und Verantwortung

- **Cloud Service Owner / Fachbereich:** verantwortet Zweck, Geschäftsbedarf, Datenbezug und Nutzung.
- **Cloud-/Plattformteam:** setzt Architektur, Konfiguration, Monitoring und technische Leitplanken um.
- **ISMS-Owner / Security-Rolle:** definiert Mindestanforderungen, Risiko- und Reviewlogik.
- **IT-Betrieb / Identity Owner:** steuert Identitäten, Zugriffe, Protokollierung und Betriebsintegration.
- **Einkauf / Lieferantenmanagement:** hält Vertrags-, Anbieter- und Nachweisinformationen aktuell.
- **Datenschutz / Legal:** prüft personenbezogene Daten, Vertrags-, Standort-, Unterauftragnehmer- und Rechtsfragen.
- **Management:** entscheidet über strategische Cloud-Abhängigkeiten, Restrisiken, Ressourcen und Ausnahmen.

## Implementierung

### Minimalstart

Ziel: erlaubte Cloud-Nutzung sichtbar, verantwortlich und prüfbar machen.

1. Genutzte Cloud-Dienste im ISMS-Scope werden in einer einfachen Cloud-Service-Liste geführt.
2. Jeder Dienst erhält Owner, Zweck, Nutzergruppe, Datenklasse und Kritikalität.
3. Neue Cloud-Dienste benötigen eine dokumentierte Freigabe vor produktiver Nutzung.
4. Adminzugriffe, externe Zugriffe und Integrationen werden gesondert geprüft.
5. Mindestens Basiskontrollen werden festgelegt: MFA, Rollenmodell, Logging, Backup-/Exportfähigkeit, Vertragskontakt, Reviewtermin.
6. Abweichungen werden befristet dokumentiert und risikobasiert entschieden.

Minimaler Nachweis:

- Cloud-Service-Liste mit Ownern,
- Freigabe- oder Onboardingnachweis,
- Konfigurations- oder Zugriffsnachweis für kritische Dienste,
- dokumentierte Ausnahme,
- Reviewnotiz oder Maßnahmenlog.

### Solide Praxis

Ziel: Cloud-Sicherheit wird in Beschaffung, Architektur, Betrieb und Review integriert.

1. Cloud-Dienste werden nach Einsatzmodell, Kritikalität, Datenbezug und Verantwortungsmodell klassifiziert.
2. Mindestanforderungen werden pro Diensttyp festgelegt: Identität, Zugriff, Verschlüsselung, Logging, Backup, Schnittstellen, Adminrechte, Monitoring, Incident-Kontakt.
3. Cloud-Onboarding verbindet Einkauf, Datenschutz, ISMS, IT und Fachbereich.
4. Konfigurationsreviews prüfen kritische Einstellungen, öffentliche Freigaben, privilegierte Rollen, Protokollierung und Integrationen.
5. Anbieteränderungen, neue Funktionen und Sicherheitsmeldungen werden bewertet.
6. Ergebnisse fließen in Risikoregister, Maßnahmenlog, Lieferantenreview und Management Review.

Starke Evidenz:

- freigegebene Cloud-Service- und Risikoklassifikation,
- dokumentiertes Verantwortungsmodell,
- Konfigurations- und Berechtigungsreviews,
- Nachweise zu Logging, Backup, Export oder Wiederherstellung,
- Lieferanten- und Vertragsnachweise,
- Maßnahmen und Risikoentscheidungen bei Abweichungen.

### Fortgeschritten

Ziel: Cloud-Nutzung wird durch Leitplanken, Automatisierung und Lagebild gesteuert.

1. Cloud-Governance ist mit Identitätsmanagement, Assetinventar, Ticketing, SIEM/Monitoring und Schwachstellenmanagement verbunden.
2. Baselines, Landing Zones, Policy-as-Code oder vergleichbare Leitplanken verhindern häufige Fehlkonfigurationen.
3. Kritische Abweichungen erzeugen Alerts, Tickets oder Freigabeworkflows.
4. Cloud-Risiken werden mit Kosten, Abhängigkeit, Resilienz, Datenflüssen und Exit-Fähigkeit betrachtet.
5. Management erhält Kennzahlen zu Schatten-IT, kritischen Fehlkonfigurationen, offenen Cloud-Ausnahmen, privilegierten Zugriffen und strategischen Abhängigkeiten.

## Ablauf als Routine

1. **Cloud-Bedarf entsteht:** Fachbereich, IT oder Projekt möchte einen Dienst nutzen oder erweitern.
2. **Onboarding erfassen:** Zweck, Daten, Nutzer, Kritikalität, Schnittstellen und Anbieterinformationen dokumentieren.
3. **Risiko und Verantwortung klären:** interne Aufgaben, Anbieterleistungen, Daten- und Betriebsrisiken bewerten.
4. **Mindestanforderungen prüfen:** Identität, Zugriff, Logging, Backup, Verschlüsselung, Adminmodell, Incident-Kontakt und Exit.
5. **Freigabe oder Auflagen entscheiden:** produktive Nutzung erlauben, begrenzen, nacharbeiten oder ablehnen.
6. **Betrieb integrieren:** Monitoring, Review, Support, Changes und Lieferantenkontakt einbinden.
7. **Regelmäßig prüfen:** Konfiguration, Zugriffe, Anbieteränderungen, Nachweise und offene Ausnahmen reviewen.
8. **Verbessern:** Findings in Baselines, Beschaffung, Schulung oder technische Leitplanken zurückspielen.

## Entscheidungen

- Welche Cloud-Dienste dürfen ohne zentrale Prüfung genutzt werden und welche nicht?
- Welche Datenklassen und Prozesse sind für bestimmte Cloud-Dienste zulässig?
- Welche Sicherheitsaufgaben liegen beim Anbieter, welche bleiben intern?
- Welche Mindestkonfigurationen sind für produktive Nutzung erforderlich?
- Wer darf Adminrechte, externe Freigaben oder Integrationen genehmigen?
- Wann braucht es Exit-Plan, Backup, Zweitanbieter oder Managemententscheidung?

## Evidenz

### Starke Evidenz

- Cloud-Service-Register mit Owner, Zweck, Datenklasse und Kritikalität,
- dokumentierte Freigabe mit Risiko- und Verantwortungsbewertung,
- Konfigurationsreview kritischer Einstellungen,
- Berechtigungsreview für Admins und externe Zugriffe,
- Logging-/Monitoring-/Backup-Nachweise,
- Maßnahmenlog mit validierter Behebung,
- Managemententscheidung zu Ausnahmen oder strategischen Abhängigkeiten.

### Schwache Evidenz

- Cloud-Policy ohne Liste tatsächlicher Dienste,
- Anbieterzertifikat ohne Bezug zum genutzten Dienst und Scope,
- Screenshot einzelner Einstellungen ohne Reviewentscheidung,
- Kostenliste als Ersatz für Assetinventar,
- pauschales Vertrauen auf Standardeinstellungen.

### Evidenzlücken

- Cloud-Dienst ohne Owner oder Freigabe,
- unbekannte Datenklasse oder Nutzergruppe,
- kein Verständnis des Verantwortungsmodells,
- fehlende Protokollierung oder Zugriffsnachweise,
- offene Fehlkonfiguration ohne Maßnahme,
- keine Exit- oder Wiederherstellungsüberlegung für kritische Dienste.

## Wirksamkeitsprüfung

Prüffragen:

- Sind alle produktiv genutzten Cloud-Dienste im Scope erfasst?
- Können Owner erklären, welche internen Sicherheitsaufgaben trotz Cloud-Nutzung verbleiben?
- Werden kritische Konfigurationen und Adminrechte regelmäßig geprüft?
- Werden neue Cloud-Dienste vor Nutzung bewertet?
- Werden Anbieteränderungen, Sicherheitsmeldungen und Integrationen nachverfolgt?
- Gibt es Nachweise für Backup, Export oder Wiederherstellung, soweit für den Dienst relevant?
- Erkennt das Management kritische Cloud-Abhängigkeiten und Ausnahmen?

Mögliche Kennzahlen:

- Cloud-Dienste mit aktuellem Owner und Review,
- ungeprüfte oder nicht freigegebene Cloud-Dienste,
- offene kritische Fehlkonfigurationen,
- Anzahl privilegierter Cloud-Accounts,
- überfällige Cloud-Ausnahmen,
- kritische Dienste ohne Exit- oder Wiederherstellungsnachweis.

## BSIG-/NIS2-Anschluss

Cloud-Sicherheit ist anschlussfähig an NIS2-orientierte Themen wie Risikomanagement, Lieferkettensicherheit, Zugriffsschutz, Incident-Fähigkeit, Business Continuity, sichere Beschaffung und technische Cyberhygiene. Der konkrete Bezug sollte organisationsspezifisch im Anforderungsregister und Risikoregister geprüft werden.

Dieses Artefakt ersetzt keine rechtliche, datenschutzrechtliche oder vertragsrechtliche Bewertung der Cloud-Nutzung.

## Grenzen

- Keine Cloud-Architekturvorgabe, Hardening-Baseline oder Anbieterempfehlung.
- Keine Rechts- oder Datenschutzberatung und keine Aussage zur Zulässigkeit konkreter Datenverarbeitung.
- Keine Zertifizierungs-, Konformitäts- oder Sicherheitsgarantie.
- Keine Nutzung echter Tenant-, Kunden-, Personen- oder Vertragsdaten in öffentlichen Beispielen.
- Kein Ersatz für technische Cloud-Security-Reviews, Penetrationstests oder Incident Response.

## Handoffs

- **Einkauf-/Lieferanten-Handoff:** neuer Anbieter, Vertragsänderung, Sicherheitsnachweis, Unterauftragnehmer, Serviceänderung.
- **Datenschutz-/Legal-Handoff:** personenbezogene Daten, internationale Bezüge, Vertragsfragen, Protokollierung, Betroffenen- oder Meldepflichtnähe.
- **Identity-/Access-Handoff:** Adminrechte, externe Benutzer, Gastzugriffe, technische Konten, Federation.
- **Architektur-/Plattform-Handoff:** Landing Zone, Netzwerk, Verschlüsselung, Backup, Logging, Schnittstellen.
- **Incident-Handoff:** Cloud-Fehlkonfiguration, kompromittiertes Konto, Anbieterincident, Datenabflussverdacht.
- **BCM-Handoff:** Ausfall kritischer Cloud-Dienste, Wiederherstellung, Exit, Konzentrationsrisiko.
- **Management-Handoff:** strategische Abhängigkeit, Restrisiko, Budget, Ausnahme oder Anbieterwechsel.

## Typische Fehler

- Cloud wird als reine Lieferantenfrage behandelt, obwohl interne Konfiguration entscheidend ist.
- SaaS-Dienste werden nicht als Assets und Lieferantendienste geführt.
- Standardkonfigurationen werden ungeprüft übernommen.
- Adminrechte und Integrationen wachsen ohne Review.
- Logging wird aktiviert, aber niemand wertet kritische Ereignisse aus.
- Datenschutz oder Legal werden erst nach produktiver Nutzung eingebunden.
- Management sieht Cloud-Kosten, aber nicht Cloud-Risiken und Abhängigkeiten.

## Fiktives Mini-Beispiel

Ein fiktiver Fachbereich möchte ein neues Kollaborationstool nutzen. Vor dem Rollout wird ein Cloud-Onboarding ausgefüllt: Zweck, Nutzerkreis, Datenklasse, Anbieter, Adminmodell und Schnittstellen. Das Plattformteam prüft MFA, externe Freigaben und Logging. Datenschutz und Legal klären prüfungsbedürftige Punkte. Die Nutzung wird mit Auflage freigegeben: externe Freigaben nur durch benannte Owner und Review nach drei Monaten.

Evidenz:

- Cloud-Onboardingformular,
- Freigabeentscheidung mit Auflagen,
- Konfigurationsnachweis,
- Reviewtermin,
- Maßnahmenlog für offene Punkte.
