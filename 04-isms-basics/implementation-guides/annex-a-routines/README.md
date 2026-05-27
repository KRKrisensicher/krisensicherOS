# Anhang-A-Routinen in krisensicherOS-Sprache

Dieses Verzeichnis enthält 93 Control-Artefakte als operative Routinen. Sie orientieren sich an der Struktur des Anhangs A der ISO/IEC 27001:2022, übernehmen aber keine ISO-27002-Formulierungen und ersetzen keine lizenzierte Normarbeit.

## Qualitätsstatus

Die 93 Artefakte sind als **ausgearbeitete, intern geprüfte und human-review-pflichtige Routinen** angelegt. Sie sind keine Zertifizierungs-, Konformitäts-, Rechts- oder Datenschutzbewertung und ersetzen keine lizenzierte Normarbeit.

Arbeitsstatus wird außerhalb der Produktdateien geführt. Produktartefakte enthalten keine internen Batch-, Agenten- oder Reviewstatus-Blöcke.

Goldstandard-Lernbeispiele für menschliche Prüfung und Qualitätskalibrierung:

- `A.5.15 — Zugriffssteuerung als Governance-Routine` (`a-5-15-zugriffssteuerung-als-governance-routine.md`)
- `A.6.3 — Awareness, Schulung und Befähigung` (`a-6-3-awareness-schulung-und-befaehigung.md`)
- `A.8.8 — Technische Schwachstellen behandeln` (`a-8-8-technische-schwachstellen-behandeln.md`)

Für den praktischen Einstieg nutze zuerst:

- `Management Decision Pack` (`management-decision-pack.md`),
- `Workload-Matrix` (`workload-matrix.md`),
- `Mapping zu ISMS-Implementierungsleitfäden` (`control-guide-mapping.md`),
- `Statement of Applicability` (`statement-of-applicability.md`),
- `KI-Nutzung in Anhang-A-Routinen` (`ki-nutzung-in-anhang-a-routinen.md`).

Jedes Zielartefakt beschreibt:

- Anforderung in Repo-Sprache,
- Trigger,
- Ablauf / Implementierungsanregungen,
- Entscheidungen,
- Evidenz,
- BSIG-/NIS2-Bezug,
- Grenzen,
- Handoffs.

## Nutzung

Nutze diese Artefakte nicht als Pflichtliste zum mechanischen Abarbeiten. Starte aus Risiko, Scope und Betroffenheit. Wenn du neu beginnst, starte mit Scope, Risiko und den tatsächlich relevanten Routinen und überführe die ausgewählten Controls in die `SoA-Arbeitstabelle` (`statement-of-applicability.md`).

Markiere pro Kontrolle im Nutzer-ISMS:

```text
Nicht relevant / geplant / umgesetzt / wirksamkeitsgeprüft / Ausnahme / Managemententscheidung offen
```

## Artefakte


### Governance / Organisation

- A.5.1 — Organisatorische Leitplanken für Informationssicherheit (`a-5-1-organisatorische-leitplanken-fuer-informationssicherheit.md`)
- A.5.2 — Rollen und Zuständigkeiten für Informationssicherheit (`a-5-2-rollen-und-zustaendigkeiten-fuer-informationssicherheit.md`)
- A.5.3 — Trennung unverträglicher Aufgaben (`a-5-3-trennung-unvertraeglicher-aufgaben.md`)
- A.5.4 — Managementverantwortung im Sicherheitsbetrieb (`a-5-4-managementverantwortung-im-sicherheitsbetrieb.md`)
- A.5.5 — Kontakt zu zuständigen Behörden (`a-5-5-kontakt-zu-zustaendigen-behoerden.md`)
- A.5.6 — Kontakt zu Fachgruppen und Sicherheitsnetzwerken (`a-5-6-kontakt-zu-fachgruppen-und-sicherheitsnetzwerken.md`)
- A.5.7 — Beobachtung von Bedrohungen und Lageinformationen (`a-5-7-beobachtung-von-bedrohungen-und-lageinformationen.md`)
- A.5.8 — Sicherheit in Projekten und Veränderungen (`a-5-8-sicherheit-in-projekten-und-veraenderungen.md`)
- A.5.9 — Inventar von Informationen und unterstützenden Assets (`a-5-9-inventar-von-informationen-und-unterstuetzenden-assets.md`)
- A.5.10 — Zulässige Nutzung von Informationen und Assets (`a-5-10-zulaessige-nutzung-von-informationen-und-assets.md`)
- A.5.11 — Rückgabe von Assets bei Wechsel oder Austritt (`a-5-11-rueckgabe-von-assets-bei-wechsel-oder-austritt.md`)
- A.5.12 — Klassifizierung von Informationen (`a-5-12-klassifizierung-von-informationen.md`)
- A.5.13 — Kennzeichnung und Umgang mit Informationen (`a-5-13-kennzeichnung-und-umgang-mit-informationen.md`)
- A.5.14 — Informationsübertragung zwischen Parteien (`a-5-14-informationsuebertragung-zwischen-parteien.md`)
- A.5.15 — Zugriffssteuerung als Governance-Routine (`a-5-15-zugriffssteuerung-als-governance-routine.md`)
- A.5.16 — Identitätsmanagement (`a-5-16-identitaetsmanagement.md`)
- A.5.17 — Umgang mit Authentifizierungsinformationen (`a-5-17-umgang-mit-authentifizierungsinformationen.md`)
- A.5.18 — Review von Zugriffsrechten (`a-5-18-review-von-zugriffsrechten.md`)

### Lieferanten / Abhängigkeiten

- A.5.19 — Sicherheit in Lieferantenbeziehungen (`a-5-19-sicherheit-in-lieferantenbeziehungen.md`)
- A.5.20 — Sicherheitsanforderungen in Lieferantenvereinbarungen (`a-5-20-sicherheitsanforderungen-in-lieferantenvereinbarungen.md`)
- A.5.21 — Sicherheit in der IT-Lieferkette (`a-5-21-sicherheit-in-der-it-lieferkette.md`)
- A.5.22 — Überwachung und Änderung von Lieferantendiensten (`a-5-22-ueberwachung-und-aenderung-von-lieferantendiensten.md`)
- A.5.23 — Sicherheit bei Cloud-Nutzung (`a-5-23-sicherheit-bei-cloud-nutzung.md`)

### Incident / Abweichung / Lernen

- A.5.24 — Vorbereitung auf Sicherheitsvorfälle (`a-5-24-vorbereitung-auf-sicherheitsvorfaelle.md`)
- A.5.25 — Bewertung und Entscheidung bei Sicherheitsereignissen (`a-5-25-bewertung-und-entscheidung-bei-sicherheitsereignissen.md`)
- A.5.26 — Reaktion auf Sicherheitsvorfälle (`a-5-26-reaktion-auf-sicherheitsvorfaelle.md`)
- A.5.27 — Lernen aus Sicherheitsvorfällen (`a-5-27-lernen-aus-sicherheitsvorfaellen.md`)
- A.5.28 — Sichern von Beweisspuren (`a-5-28-sichern-von-beweisspuren.md`)

### Kontinuität / Krisenfähigkeit

- A.5.29 — Informationssicherheit bei Störungen und Krisen (`a-5-29-informationssicherheit-bei-stoerungen-und-krisen.md`)
- A.5.30 — IKT-Bereitschaft für Kontinuität (`a-5-30-ikt-bereitschaft-fuer-kontinuitaet.md`)

### Nachweise / Anforderungen / Reviews

- A.5.31 — Rechtliche und vertragliche Anforderungen erkennen (`a-5-31-rechtliche-und-vertragliche-anforderungen-erkennen.md`)
- A.5.32 — Schutz geistiger Eigentums- und Nutzungsrechte (`a-5-32-schutz-geistiger-eigentums-und-nutzungsrechte.md`)
- A.5.33 — Schutz von Aufzeichnungen und Nachweisen (`a-5-33-schutz-von-aufzeichnungen-und-nachweisen.md`)
- A.5.34 — Datenschutz und Schutz personenbezogener Informationen (`a-5-34-datenschutz-und-schutz-personenbezogener-informationen.md`)
- A.5.35 — Unabhängige Überprüfung der Informationssicherheit (`a-5-35-unabhaengige-ueberpruefung-der-informationssicherheit.md`)
- A.5.36 — Einhaltung interner Regeln und Sicherheitsvorgaben (`a-5-36-einhaltung-interner-regeln-und-sicherheitsvorgaben.md`)
- A.5.37 — Dokumentierte Betriebsregeln für Informationsverarbeitung (`a-5-37-dokumentierte-betriebsregeln-fuer-informationsverarbeitung.md`)

### Menschen / Befähigung / Arbeitsverhältnis

- A.6.1 — Sicherheitsprüfung vor Beschäftigung oder Beauftragung (`a-6-1-sicherheitspruefung-vor-beschaeftigung-oder-beauftragung.md`)
- A.6.2 — Sicherheitsverantwortung in Arbeits- und Auftragsverhältnissen (`a-6-2-sicherheitsverantwortung-in-arbeits-und-auftragsverhaeltnissen.md`)
- A.6.3 — Awareness, Schulung und Befähigung (`a-6-3-awareness-schulung-und-befaehigung.md`)
- A.6.4 — Umgang mit Regelverstößen (`a-6-4-umgang-mit-regelverstoessen.md`)
- A.6.5 — Sicherheitsaufgaben bei Wechsel oder Austritt (`a-6-5-sicherheitsaufgaben-bei-wechsel-oder-austritt.md`)
- A.6.6 — Vertraulichkeits- und Geheimhaltungsvereinbarungen (`a-6-6-vertraulichkeits-und-geheimhaltungsvereinbarungen.md`)
- A.6.7 — Sicheres Arbeiten außerhalb kontrollierter Standorte (`a-6-7-sicheres-arbeiten-ausserhalb-kontrollierter-standorte.md`)
- A.6.8 — Meldung von Sicherheitsereignissen durch Beschäftigte (`a-6-8-meldung-von-sicherheitsereignissen-durch-beschaeftigte.md`)

### Physische Sicherheit

- A.7.1 — Physische Sicherheitsbereiche (`a-7-1-physische-sicherheitsbereiche.md`)
- A.7.2 — Physischer Zutritt (`a-7-2-physischer-zutritt.md`)
- A.7.3 — Schutz von Räumen und Gebäuden (`a-7-3-schutz-von-raeumen-und-gebaeuden.md`)
- A.7.4 — Physische Sicherheitsüberwachung (`a-7-4-physische-sicherheitsueberwachung.md`)
- A.7.5 — Schutz vor physischen und umweltbedingten Gefahren (`a-7-5-schutz-vor-physischen-und-umweltbedingten-gefahren.md`)
- A.7.6 — Arbeiten in geschützten Bereichen (`a-7-6-arbeiten-in-geschuetzten-bereichen.md`)
- A.7.7 — Aufgeräumte Arbeitsplätze und Bildschirme (`a-7-7-aufgeraeumte-arbeitsplaetze-und-bildschirme.md`)
- A.7.8 — Platzierung und Schutz von Geräten (`a-7-8-platzierung-und-schutz-von-geraeten.md`)
- A.7.9 — Schutz von Assets außerhalb des Standorts (`a-7-9-schutz-von-assets-ausserhalb-des-standorts.md`)
- A.7.10 — Umgang mit Speichermedien (`a-7-10-umgang-mit-speichermedien.md`)
- A.7.11 — Versorgungs- und Infrastrukturdienste (`a-7-11-versorgungs-und-infrastrukturdienste.md`)
- A.7.12 — Schutz von Verkabelung (`a-7-12-schutz-von-verkabelung.md`)
- A.7.13 — Instandhaltung von Geräten (`a-7-13-instandhaltung-von-geraeten.md`)
- A.7.14 — Sichere Entsorgung oder Wiederverwendung von Geräten (`a-7-14-sichere-entsorgung-oder-wiederverwendung-von-geraeten.md`)

### Technischer Betrieb

- A.8.1 — Benutzerendgeräte absichern (`a-8-1-benutzerendgeraete-absichern.md`)
- A.8.2 — Privilegierte Rechte steuern (`a-8-2-privilegierte-rechte-steuern.md`)
- A.8.3 — Zugriff auf Informationen einschränken (`a-8-3-zugriff-auf-informationen-einschraenken.md`)
- A.8.4 — Zugriff auf Quellcode und Entwicklungsartefakte steuern (`a-8-4-zugriff-auf-quellcode-und-entwicklungsartefakte-steuern.md`)
- A.8.5 — Sichere Authentisierung (`a-8-5-sichere-authentisierung.md`)
- A.8.6 — Kapazitäten planen und überwachen (`a-8-6-kapazitaeten-planen-und-ueberwachen.md`)
- A.8.7 — Schutz vor Schadsoftware (`a-8-7-schutz-vor-schadsoftware.md`)
- A.8.8 — Technische Schwachstellen behandeln (`a-8-8-technische-schwachstellen-behandeln.md`)
- A.8.9 — Konfigurationssteuerung (`a-8-9-konfigurationssteuerung.md`)
- A.8.10 — Informationen löschen (`a-8-10-informationen-loeschen.md`)
- A.8.11 — Datenmaskierung und Reduktion sensibler Anzeige (`a-8-11-datenmaskierung-und-reduktion-sensibler-anzeige.md`)
- A.8.12 — Verhinderung ungewollter Datenabflüsse (`a-8-12-verhinderung-ungewollter-datenabfluesse.md`)
- A.8.13 — Datensicherung (`a-8-13-datensicherung.md`)
- A.8.14 — Redundanz für kritische Informationsverarbeitung (`a-8-14-redundanz-fuer-kritische-informationsverarbeitung.md`)
- A.8.15 — Protokollierung (`a-8-15-protokollierung.md`)
- A.8.16 — Überwachung technischer Aktivitäten (`a-8-16-ueberwachung-technischer-aktivitaeten.md`)
- A.8.17 — Zeitsynchronisation (`a-8-17-zeitsynchronisation.md`)
- A.8.18 — Nutzung privilegierter Hilfsprogramme begrenzen (`a-8-18-nutzung-privilegierter-hilfsprogramme-begrenzen.md`)
- A.8.19 — Softwareinstallation auf Betriebssystemen steuern (`a-8-19-softwareinstallation-auf-betriebssystemen-steuern.md`)
- A.8.20 — Netzwerksicherheit (`a-8-20-netzwerksicherheit.md`)
- A.8.21 — Sicherheit von Netzwerkdiensten (`a-8-21-sicherheit-von-netzwerkdiensten.md`)
- A.8.22 — Netztrennung und Segmentierung (`a-8-22-netztrennung-und-segmentierung.md`)
- A.8.23 — Webfilterung und Zugriff auf externe Inhalte (`a-8-23-webfilterung-und-zugriff-auf-externe-inhalte.md`)
- A.8.24 — Kryptografische Verfahren einsetzen (`a-8-24-kryptografische-verfahren-einsetzen.md`)

### Entwicklung / Änderung / Tests

- A.8.25 — Sicherer Entwicklungslebenszyklus (`a-8-25-sicherer-entwicklungslebenszyklus.md`)
- A.8.26 — Sicherheitsanforderungen an Anwendungen (`a-8-26-sicherheitsanforderungen-an-anwendungen.md`)
- A.8.27 — Sichere Systemarchitektur und Engineering-Grundsätze (`a-8-27-sichere-systemarchitektur-und-engineering-grundsaetze.md`)
- A.8.28 — Sichere Programmierung (`a-8-28-sichere-programmierung.md`)
- A.8.29 — Sicherheitstests in Entwicklung und Abnahme (`a-8-29-sicherheitstests-in-entwicklung-und-abnahme.md`)
- A.8.30 — Ausgelagerte Entwicklung steuern (`a-8-30-ausgelagerte-entwicklung-steuern.md`)
- A.8.31 — Trennung von Entwicklungs-, Test- und Produktivumgebungen (`a-8-31-trennung-von-entwicklungs-test-und-produktivumgebungen.md`)
- A.8.32 — Änderungssteuerung (`a-8-32-aenderungssteuerung.md`)
- A.8.33 — Testinformationen schützen (`a-8-33-testinformationen-schuetzen.md`)
- A.8.34 — Schutz von Informationssystemen während Prüfungen (`a-8-34-schutz-von-informationssystemen-waehrend-pruefungen.md`)

## Qualitätstore

- Public-safe: keine echten Organisations-, Kunden-, Personen- oder Geheimdaten.
- Normtext-sicher: keine ISO-27002-Sprache kopieren oder nachbilden.
- Claim-safe: keine Zertifizierungs-, Konformitäts- oder Sicherheitsgarantie.
- Betriebsfähig: jedes Control braucht Owner, Trigger, Evidenz und Reviewpunkt.
- Human Gate: Risikoakzeptanz, Rechts-/Datenschutzfragen und Managemententscheidungen bleiben menschlich verantwortet.
