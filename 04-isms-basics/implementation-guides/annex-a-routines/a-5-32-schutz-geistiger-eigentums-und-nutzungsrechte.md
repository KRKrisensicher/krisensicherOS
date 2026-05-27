
# A.5.32 — Schutz geistiger Eigentums- und Nutzungsrechte

## Zweck

Diese Routine sorgt dafür, dass geistiges Eigentum, lizenzierte Inhalte, Software, Quellcode, Marken, Vorlagen, Trainingsmaterial, Datenbanken und vertraglich geregelte Nutzungsrechte nicht versehentlich verletzt, verloren, unbefugt genutzt oder unklar weitergegeben werden.

Der Kern ist nicht eine juristische Detailprüfung durch das ISMS, sondern eine belastbare Betriebslogik: Welche Rechte und Einschränkungen sind bekannt, wer darf was nutzen, wo entstehen Nachweise und wann braucht es Legal-, Einkauf- oder Management-Entscheidungen?

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Routine, mit der relevante Schutz- und Nutzungsrechte identifiziert, dokumentiert, kommuniziert, in Beschaffung und Betrieb berücksichtigt und bei Änderungen geprüft werden. Unsichere Rechtsfragen werden nicht durch Security entschieden, sondern an zuständige menschliche Rollen übergeben.

## Typische Risiken

- Wenn lizenzierte Software, Inhalte oder Daten ohne klare Nutzungsrechte eingesetzt werden, können Vertragsverletzungen, Kosten, Abschaltungen oder Reputationsschäden entstehen.
- Wenn Eigenentwicklungen, Konzepte oder Vorlagen ohne Schutz- und Veröffentlichungslogik geteilt werden, kann wertvolles Know-how unkontrolliert abfließen.
- Wenn Open-Source-Komponenten ohne Lizenz- und Herkunftsprüfung in Produkte einfließen, entstehen rechtliche, Lieferketten- und Wartungsrisiken.
- Wenn Dienstleister Arbeitsergebnisse, Quellcode oder Dokumentation ohne klare Rechteregelung liefern, bleibt unklar, wer sie ändern, weitergeben oder betreiben darf.
- Wenn Mitarbeitende fremde Materialien in Präsentationen, Trainings, Marketing oder KI-Workflows übernehmen, können Nutzungsgrenzen übersehen werden.

## Trigger

- neues Produkt, neuer Service, neue Software, neue Datenquelle oder neues Content-Asset.
- Einkauf, Verlängerung oder Kündigung von Software-, Daten-, Medien- oder Beratungsverträgen.
- Nutzung von Open Source, Drittbibliotheken, Templates, Bildern, Trainingsmaterial oder externen Wissensquellen.
- Veröffentlichung, Kundenübergabe, Repository-Freigabe oder externe Kommunikation.
- Sicherheitsereignis, Abfluss von Quellcode, unklare Datenweitergabe oder Lieferantenwechsel.
- Auditfinding, Kundenfrage, Lizenzprüfung oder interne Rechts-/Einkaufsanfrage.
- geplanter Review von kritischen Assets, Softwareinventar oder Lieferantenleistungen.

## Rollen und Verantwortung

- **Asset Owner / Product Owner:** kennt Zweck, Schutzbedarf und Nutzungskontext des betroffenen Assets.
- **Einkauf / Vendor Management:** hält Verträge, Lizenzmodelle, Nutzungsumfang und Verlängerungen nach.
- **Legal:** bewertet Rechte, Lizenzen, Veröffentlichungen, Vertragsklauseln und strittige Auslegungen.
- **IT-/Plattform Owner:** führt Software- und Toolinventar, technische Nutzung und Zugriffe.
- **Entwicklung / Engineering:** prüft Open-Source-, Dependency- und Code-Herkunft im Entwicklungsprozess.
- **Marketing / Kommunikation / Training:** nutzt Inhalte nur mit geklärter Herkunft, Freigabe und Nutzungsgrenze.
- **ISMS-Owner:** sorgt für Mindestlogik, Evidenzfähigkeit, Risikoverknüpfung und Handoffs.
- **Management:** entscheidet bei hohen Restrisiken, Ressourcenbedarf, Streitfällen oder strategischen Veröffentlichungen.

## Implementierung

### Minimalstart

Ziel: Kritische Rechte und Nutzungsgrenzen sichtbar machen.

1. Die wichtigsten Kategorien werden benannt: Software, Quellcode, Dokumente, Designs, Daten, Trainingsmaterial, Marken, externe Inhalte.
2. Für kritische Assets wird ein Owner festgelegt.
3. Beschaffung oder Nutzung neuer externer Inhalte läuft über einen einfachen Check: Herkunft, Zweck, Nutzungsumfang, Ablageort, Freigabe.
4. Veröffentlichungen und Kundenübergaben erhalten einen Legal-/Owner-Check, wenn Rechte oder Vertraulichkeit unklar sind.
5. Open-Source- und Drittkomponenten werden mindestens in einer Liste oder im Entwicklungswerkzeug nachvollziehbar erfasst.
6. Unklare Fälle werden gestoppt, bis Legal, Einkauf oder Management entschieden hat.

Minimaler Nachweis:

- Liste kritischer Assets und Software mit Owner,
- Lizenz- oder Vertragsreferenz,
- Freigabe für Nutzung oder Veröffentlichung,
- Dependency-/Open-Source-Liste für relevante Produkte,
- dokumentierte Klärung bei Ausnahmen oder Unsicherheit.

### Solide Praxis

Ziel: Rechteklärung wird Teil von Beschaffung, Entwicklung, Content-Erstellung und Übergaben.

1. Nutzungsrechte werden im Asset-, Software- oder Vertragsregister mit Owner, Scope, Laufzeit und Einschränkungen geführt.
2. Beschaffungs-, Entwicklungs- und Veröffentlichungsprozesse enthalten klare Checkpunkte.
3. Open-Source-Komponenten werden nach Lizenztyp, Herkunft, Wartungsstatus und Produktbezug bewertet.
4. Dienstleisterverträge klären Rechte an Arbeitsergebnissen, Quellcode, Dokumentation, Konfigurationen und Wiederverwendung.
5. Schulung oder Kurzleitfaden erklärt, welche fremden Inhalte nicht einfach übernommen werden dürfen.
6. Abweichungen, unklare Rechte oder fehlende Nachweise werden als Risiko oder Maßnahme nachverfolgt.
7. Kritische Bestände werden regelmäßig reviewed, etwa bei Vertragsverlängerung oder Produktrelease.

Starke Evidenz:

- Rechte-/Lizenzregister mit Ownern,
- Einkaufs- oder Vertragschecklisten,
- Open-Source- und Dependency-Auswertungen,
- Freigaben vor Veröffentlichung oder Kundenübergabe,
- dokumentierte Klärungen mit Legal/Einkauf,
- Maßnahmenlog zu ungeklärten oder abgelaufenen Rechten.

### Fortgeschritten

Ziel: Rechte- und Nutzungsschutz ist in Tooling, Produktsteuerung und Governance integriert.

1. Softwareinventar, Vertragsregister, SBOM-/Dependency-Tools und Release-Prozess sind verbunden.
2. Lizenz- oder Herkunftsrisiken erzeugen Tickets, Blocks oder Reviewpflichten vor produktiver Nutzung.
3. Kritische interne Assets werden klassifiziert und mit Zugriff, Vertraulichkeit und Veröffentlichungsregeln verbunden.
4. Nutzung von KI-Tools, externen Wissensquellen und Content-Plattformen wird über Datenklasse, Rechte und Freigabepfade gesteuert.
5. Kennzahlen zeigen ungeklärte Rechte, überfällige Lizenzreviews, nicht zuordenbare Software und offene Drittkomponentenrisiken.
6. Management entscheidet über strategische Veröffentlichungen, Open-Source-Freigaben oder akzeptierte Restrisiken.

## Ablauf als Routine

1. **Neues oder geändertes Asset entsteht:** Software, Inhalt, Code, Datenquelle, Vorlage, Dienstleisterleistung oder Veröffentlichung.
2. **Owner bestimmen:** fachliche Verantwortung und Nutzungskontext klären.
3. **Herkunft und Rechte erfassen:** Quelle, Vertrag, Lizenz, Nutzungszweck, Laufzeit und Einschränkungen dokumentieren.
4. **Risiko bewerten:** Vertraulichkeit, Weitergabe, Produktbezug, Kundenauswirkung und rechtliche Unsicherheit einordnen.
5. **Freigeben oder eskalieren:** normale Nutzung bestätigen, Einschränkungen setzen oder Legal/Einkauf/Management einbeziehen.
6. **Technisch und organisatorisch umsetzen:** Ablage, Zugriff, Kennzeichnung, Dependency Management, Vertragsreferenz oder Veröffentlichungsfreigabe.
7. **Nachweis ablegen:** Entscheidung, Quelle, Scope und Reviewdatum bleiben nachvollziehbar.
8. **Review durchführen:** bei Release, Vertragsänderung, Lieferantenwechsel, Auditfinding oder geplantem Turnus.

## Entscheidungen

- Welche Asset-Kategorien sind für den Start kritisch genug?
- Welche Nutzungen brauchen Legal-, Einkaufs- oder Managementfreigabe?
- Welche Open-Source-Lizenztypen, Content-Quellen oder Plattformen sind zulässig, eingeschränkt oder verboten?
- Wie wird mit ungeklärter Herkunft, fehlenden Verträgen oder abgelaufenen Lizenzen umgegangen?
- Welche internen Materialien dürfen extern veröffentlicht, geteilt oder in KI-Tools verarbeitet werden?
- Wer akzeptiert Restrisiken, wenn Klärung nicht rechtzeitig möglich ist?

## Evidenz

### Starke Evidenz

- aktuelles Software-, Asset- oder Rechteinventar mit Owner,
- Vertrags- oder Lizenzreferenzen mit Nutzungsumfang,
- Freigabeprotokolle für Releases, Veröffentlichungen oder Kundenübergaben,
- Open-Source-/Dependency-Liste mit Bewertung,
- Nachweise über entfernte, ersetzte oder geklärte Komponenten,
- dokumentierte Ausnahmen mit Laufzeit, Risiko und Wiedervorlage,
- Managemententscheidung bei strategischer Veröffentlichung oder akzeptiertem Restrisiko.

### Schwache Evidenz

- allgemeine Copyright-Policy ohne betriebliche Checks,
- Softwareliste ohne Lizenz- oder Ownerbezug,
- Screenshots aus Tools ohne Bewertung,
- pauschale Aussage „Legal prüft bei Bedarf“ ohne Trigger,
- veraltete Vertragsablage ohne Bezug zu tatsächlich genutzten Assets.

### Evidenzlücken

- externe Inhalte ohne Herkunftsnachweis,
- Produktabhängigkeiten ohne Lizenz- oder Wartungsstatus,
- Dienstleister-Arbeitsergebnisse ohne Rechteklärung,
- Veröffentlichungen ohne Freigabe,
- abgelaufene oder überschrittene Lizenznutzung ohne Entscheidung,
- Nutzung sensibler interner Inhalte in KI- oder Cloud-Tools ohne Freigabe.

## Wirksamkeitsprüfung

Prüffragen:

- Kann für kritische Software, Inhalte und Arbeitsergebnisse nachvollzogen werden, wer sie nutzen darf und warum?
- Sind Open-Source- und Drittkomponenten vor Release sichtbar und bewertet?
- Werden Veröffentlichungen, Kundenübergaben und KI-Nutzungen bei unklaren Rechten gestoppt oder eskaliert?
- Sind Verträge, Lizenzen und tatsächliche Nutzung miteinander verbunden?
- Führen Findings zu Korrekturen, Ersatz, Lizenzanpassung oder Managemententscheidung?
- Verstehen relevante Rollen, wann Legal oder Einkauf einzubeziehen ist?

Mögliche Kennzahlen:

- Anteil kritischer Assets mit Owner und Rechtebezug,
- offene ungeklärte Lizenz- oder Herkunftsfälle,
- Releases mit Dependency-/Lizenzcheck,
- überfällige Vertrags- oder Lizenzreviews,
- Ausnahmen mit abgelaufener Wiedervorlage,
- nicht zuordenbare Softwareinstallationen.

## BSIG-/NIS2-Anschluss

Der Schutz geistiger Eigentums- und Nutzungsrechte ist anschlussfähig an NIS2-orientierte Governance, Lieferkettensicherheit, sichere Beschaffung, Asset Management, sichere Entwicklung und Schutz geschäftskritischer Informationen. Der konkrete Bezug sollte im Anforderungsregister, Vertragsmanagement und Risikoregister organisationsspezifisch geprüft werden.

Dieses Artefakt ersetzt keine Rechtsberatung und keine verbindliche Bewertung von Urheber-, Marken-, Lizenz- oder Vertragsfragen.

## Grenzen

- Keine Rechtsberatung, Lizenzbewertung oder Vertragsauslegung durch dieses Artefakt.
- Keine Zertifizierungs-, Konformitäts- oder Sicherheitszusage.
- Keine Übernahme lizenzpflichtiger Normtexte.
- Keine Nutzung echter Vertrags-, Kunden-, Personen- oder Geheimdaten in öffentlichen Beispielen.
- Kein Ersatz für Software Asset Management, SBOM-Programm oder juristische Prüfung.

## Handoffs

- **Legal-Handoff:** unklare Rechte, Lizenzbedingungen, Veröffentlichungen, Marken, Streitfälle, Open-Source-Fragen mit Produktwirkung.
- **Einkaufs-/Vendor-Handoff:** Beschaffung, Vertragslaufzeit, Nutzungsumfang, Lieferantenleistungen, Audit- oder Nachweisanfragen.
- **Entwicklungs-Handoff:** Open Source, Dependencies, Quellcode-Herkunft, Releasefreigaben.
- **Kommunikations-/Marketing-Handoff:** externe Inhalte, Bilder, Texte, Präsentationen, öffentliche Assets.
- **Datenschutz-Handoff:** Datenbanken, Trainingsdaten, KI-Nutzung oder personenbezogene Informationen in Inhalten.
- **Management-Handoff:** strategische Veröffentlichung, akzeptiertes Restrisiko, Kosten für Lizenzierung oder Ersatz.
- **Audit-/Evidence-Handoff:** fehlende Nachweise, unklare Inventare oder nicht prüfbare Freigaben.

## Typische Fehler

- Rechtefragen werden erst kurz vor Veröffentlichung oder Kundenübergabe gestellt.
- Open-Source-Komponenten werden technisch verwaltet, aber lizenz- und herkunftsseitig nicht bewertet.
- Dienstleister liefern Code oder Dokumente, ohne dass Nutzungsrechte klar dokumentiert sind.
- Interne Vorlagen werden extern geteilt, obwohl Vertraulichkeit oder Rechte unklar sind.
- Lizenzregister und tatsächliche Toolnutzung laufen auseinander.
- Unklare Fälle bleiben mündlich gelöst und sind später nicht prüfbar.

## Fiktives Mini-Beispiel

Ein fiktives Softwareteam möchte eine neue Bibliothek in ein Kundenportal aufnehmen. Der Product Owner erfasst Zweck und Produktbezug, Engineering dokumentiert Herkunft und Version, Legal prüft die Lizenz auf Nutzungsgrenzen. Die Bibliothek wird freigegeben, aber mit Review vor jedem Major-Update. Parallel wird eine ältere Komponente ersetzt, weil ihre Herkunft nicht nachvollziehbar ist.

Evidenz:

- Dependency-Eintrag mit Owner und Zweck,
- dokumentierte Lizenzklärung,
- Releasefreigabe,
- Ticket zum Ersatz der ungeklärten Komponente,
- Reviewtermin für Major-Updates.
