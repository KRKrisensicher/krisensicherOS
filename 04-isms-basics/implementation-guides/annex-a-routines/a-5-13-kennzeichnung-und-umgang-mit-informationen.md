
# A.5.13 — Kennzeichnung und Umgang mit Informationen

## Zweck

Kennzeichnung und Umgang mit Informationen übersetzen Klassifizierung in sichtbares Verhalten. Menschen, Teams und Systeme sollen erkennen können, wie Informationen zu behandeln sind: wo sie abgelegt werden, wer sie teilen darf, welche Kanäle zulässig sind, wie sie gedruckt, transportiert, archiviert oder entsorgt werden.

Der Kern ist nicht ein hübsches Label auf Dokumenten, sondern eine alltagstaugliche Handhabungsroutine, die Fehlversand, falsche Ablage, ungeeignete Tools und unklare Verantwortlichkeiten reduziert.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine nachvollziehbare Routine für Kennzeichnung und Handhabung klassifizierter Informationen. Die Routine verbindet Informationsklassen, konkrete Umgangsregeln, Toolunterstützung, Schulung, Stichproben, Ausnahmebehandlung und Handoffs an Datenschutz, Legal, IT, Lieferantenmanagement und Incident Response.

## Typische Risiken

- Wenn vertrauliche Informationen nicht erkennbar gekennzeichnet sind, werden sie versehentlich über falsche Kanäle geteilt.
- Wenn Labels keine Handlungsfolgen haben, behandeln Beschäftigte alle Informationen gleich.
- Wenn Umgangsregeln zu kompliziert sind, entstehen Umgehungen wie private Ablagen, Schatten-IT oder unkontrollierte Kopien.
- Wenn physische Unterlagen, Ausdrucke oder Besprechungsnotizen vergessen werden, bleiben Schutzmaßnahmen auf digitale Dokumente beschränkt.
- Wenn externe Parteien Labels nicht verstehen, können Informationen trotz interner Regeln falsch verarbeitet werden.

## Trigger

- Einführung oder Änderung eines Klassifizierungsmodells.
- neue Dokumentenvorlagen, Kollaborationstools, Datenräume, DMS, E-Mail- oder Cloud-Plattformen.
- neue Informationsart, Datenablage, Prozessdokumentation oder externe Weitergabe.
- Fehlversand, falsche Ablage, Fund von Papierunterlagen, Datenabfluss oder Incident.
- Auditfinding, Kundenanforderung oder Lieferantenanforderung.
- Migration, Archivierung, Entsorgung oder größere Bereinigungsaktion.
- turnusmäßige Stichprobe zur Label- und Umgangsqualität.

## Rollen und Verantwortung

- **Information Owner / Prozess Owner:** legt fest, wie Informationen der eigenen Klasse gekennzeichnet und behandelt werden.
- **ISMS-Owner / Security-Rolle:** definiert Mindestlogik, Schulung, Stichproben und Eskalation.
- **IT-/Plattform Owner:** unterstützt Labels, Berechtigungen, Freigaben, DLP, Druck- oder Sharing-Einstellungen.
- **Fachbereiche:** wenden Kennzeichnung und Umgangsregeln in Dokumenten, Tickets, Ablagen, Meetings und Kommunikation an.
- **Datenschutz / Legal:** prüft personenbezogene Daten, Geheimhaltungsverpflichtungen, externe Hinweise und Streitfälle.
- **Einkauf / Lieferantenmanagement:** stellt sicher, dass externe Parteien Umgangsanforderungen verstehen und bestätigen.
- **Management:** entscheidet bei Zielkonflikten zwischen Nutzbarkeit, Kosten, Tooling und Schutzbedarf.

## Implementierung

### Minimalstart

Ziel: Kritische Informationen erkennbar und im Alltag handhabbar machen.

1. Die Organisation legt für jede Informationsklasse einfache Umgangsregeln fest: Ablage, Teilen, Versand, Druck, Besprechung, Entsorgung.
2. Kritische Dokumenttypen oder Informationsarten erhalten klare Kennzeichnungsbeispiele.
3. Vorlagen oder Kopf-/Fußzeilen werden für häufig genutzte Dokumente angepasst, soweit sinnvoll.
4. Fachbereiche erhalten eine kurze Entscheidungshilfe: „Wenn diese Information so eingestuft ist, dann nutze diesen Umgang.“
5. Fehlende oder falsche Kennzeichnung wird in Stichproben erfasst und korrigiert.
6. Ausnahmen werden begründet und zeitlich begrenzt.

Minimaler Nachweis:

- Umgangsmatrix je Informationsklasse,
- Kennzeichnungsbeispiele oder Vorlagen,
- Kommunikations- oder Schulungsnachweis,
- Stichprobenliste mit Korrekturen,
- Ausnahmeentscheidung bei abweichendem Umgang.

### Solide Praxis

Ziel: Kennzeichnung und Umgang werden systematisch in Prozesse und Tools eingebaut.

1. Labels sind mit konkreten Toolregeln verbunden: Sharing, Download, externe Freigabe, Verschlüsselung, DLP oder Speicherort.
2. Physische Informationen werden berücksichtigt: Ausdrucke, Whiteboards, Besprechungsunterlagen, Versand, Aktenvernichtung.
3. Externe Weitergabe enthält klare Hinweise, erwarteten Umgang und bei Bedarf vertragliche oder fachliche Freigaben.
4. Falsch gekennzeichnete oder falsch behandelte Informationen werden als Findings mit Ursache und Maßnahme betrachtet.
5. Awareness und Onboarding enthalten praktische Beispiele aus den Fachbereichen.
6. Reviews prüfen nicht nur Labels, sondern tatsächliche Handhabung.

Starke Evidenz:

- Umgangsregeln mit Handlungsfolgen,
- konfigurierte Tool- oder Plattformregeln,
- Vorlagen und Beispiele,
- Stichprobenprotokolle mit Korrekturen,
- Nachweise zu physischer Entsorgung oder sicherem Versand,
- externe Freigabe- oder Vertragsnachweise.

### Fortgeschritten

Ziel: Umgangsregeln werden technisch unterstützt und kontinuierlich verbessert.

1. Sensitivity Labels, DLP, Data Rooms, Rechteverwaltung oder Verschlüsselung unterstützen die Handhabung dort, wo sie Nutzen stiften.
2. Automatische Hinweise oder Blockaden werden mit Ausnahmeprozessen und Owner-Entscheidungen verbunden.
3. Externe Kollaborationsräume werden je Informationsklasse vorkonfiguriert.
4. Fehlversand- und DLP-Ereignisse fließen in Incident Triage, Schulung und Prozessverbesserung ein.
5. Kennzahlen zeigen Labelabdeckung, Fehlkennzeichnungen, blockierte oder freigegebene Ausnahmen und wiederkehrende Fehlmuster.
6. Management erhält Entscheidungen zu Toolinvestitionen, Nutzbarkeitskonflikten und akzeptierten Restrisiken.

## Ablauf als Routine

1. **Information wird erstellt oder empfangen:** Dokument, Datensatz, Ticket, Export, Ausdruck oder Meetingunterlage.
2. **Klasse prüfen:** vorhandene Klassifizierung, Informationsart oder Owner-Entscheidung heranziehen.
3. **Kennzeichnen:** Label, Metadatum, Vorlage, Ordnerregel oder begleitender Hinweis setzen.
4. **Umgang wählen:** Ablage, Zugriff, Versand, Druck, externe Freigabe, Archivierung oder Entsorgung gemäß Klasse durchführen.
5. **Weitergabe prüfen:** Empfänger, Zweck, Kanal, Berechtigung und externe Anforderungen kontrollieren.
6. **Nachweis erzeugen:** Freigabe, Ticket, Tool-Log, Stichprobe oder Entsorgungsnachweis ablegen.
7. **Abweichung behandeln:** falsches Label, ungeeigneter Kanal, fehlende Freigabe oder Incident melden und korrigieren.
8. **Verbessern:** Beispiele, Toolregeln oder Schulung anhand von Findings aktualisieren.

## Entscheidungen

- Welche Informationsklassen benötigen sichtbare Labels und welche werden über Ablage oder Systemkontext gesteuert?
- Welche Umgangsregeln sind verpflichtend, welche empfohlen?
- Welche Kanäle sind für welche Informationsklassen zulässig?
- Wer darf externe Freigaben oder Abweichungen genehmigen?
- Wann wird ein Fehlumgang als Incident behandelt?
- Welche technischen Kontrollen sind hilfreich, ohne Arbeit unverhältnismäßig zu blockieren?
- Wie werden physische Unterlagen und hybride Arbeitsweisen abgedeckt?

## Evidenz

### Starke Evidenz

- Umgangsmatrix mit klaren Handlungsfolgen,
- Beispiele für korrekt gekennzeichnete Dokumenttypen,
- Toolkonfigurationen für Labels, Sharing oder DLP,
- Freigaben für externe Weitergabe,
- Stichproben mit konkreten Korrekturen,
- Nachweise zu sicherer Entsorgung oder Versand,
- Lessons Learned aus Fehlversand oder falscher Ablage.

### Schwache Evidenz

- Labelrichtlinie ohne Beispiele,
- Dokumente mit Label, aber ohne technische oder organisatorische Folgen,
- Screenshot einer Toolfunktion ohne Nutzungsnachweis,
- allgemeine Schulung ohne Bezug zu Fachbereichsinformationen,
- Ablageordner mit Namen „vertraulich“ ohne Zugriffskontrolle.

### Evidenzlücken

- keine Verbindung zur Klassifizierung,
- externe Weitergabe ohne Freigabe- oder Umgangsnachweis,
- physische Unterlagen nicht betrachtet,
- falsche Kennzeichnung wird nicht korrigiert,
- Ausnahmen ohne Owner, Laufzeit oder Risikoentscheidung.

## Wirksamkeitsprüfung

Prüffragen:

- Können Beschäftigte aus einem Label ableiten, was sie tun oder lassen müssen?
- Sind kritische Informationsarten in Vorlagen, Tools oder Ablagen erkennbar gesteuert?
- Werden Fehlkennzeichnungen und Fehlumgang entdeckt und korrigiert?
- Sind externe Empfänger und Kollaborationsräume angemessen eingebunden?
- Werden physische Informationen, Ausdrucke und Entsorgung berücksichtigt?
- Sind Ausnahmen nachvollziehbar und befristet?

Mögliche Kennzahlen:

- Anteil geprüfter Dokumente mit passendem Label,
- Anzahl Fehlkennzeichnungen je Bereich,
- Fehlversand- oder falsche Ablageereignisse,
- überfällige Korrekturmaßnahmen,
- Ausnahmequote bei externem Teilen,
- DLP-/Sharing-Ereignisse mit bestätigter Bewertung.

## BSIG-/NIS2-Anschluss

Kennzeichnung und Umgang mit Informationen sind anschlussfähig an NIS2-orientierte Risikomanagementmaßnahmen, Cyberhygiene, Zugriffsschutz, sichere Kommunikation, Lieferkettensicherheit, Incident Handling und Governance. Die konkrete Relevanz sollte in Risikoanalyse, Anforderungsregister und Management Review organisationsspezifisch geprüft werden.

Dieses Artefakt ersetzt keine rechtliche oder datenschutzrechtliche Bewertung von Informationsweitergabe, Überwachung oder Beschäftigtendaten.

## Grenzen

- Keine Rechts- oder Datenschutzberatung.
- Keine Zertifizierungs-, Konformitäts- oder Sicherheitsgarantie.
- Keine ISO-27002-Texte oder Normersatz.
- Labels allein sind keine Kontrolle, wenn Umgangsregeln nicht betrieben werden.
- Keine vertraulichen oder echten Organisationsbeispiele.

## Handoffs

- **Klassifizierungs-Handoff:** unklare oder fehlende Einstufung einer Informationsart.
- **IT-/Plattform-Handoff:** Labels, DLP, Sharing, Verschlüsselung, Vorlagen, Ablageregeln.
- **Datenschutz-/Legal-Handoff:** personenbezogene Daten, Geheimhaltungsverpflichtungen, externe Hinweise, Monitoring oder Streitfälle.
- **Lieferanten-Handoff:** externe Verarbeitung, Datenräume, Umgangsvorgaben, Rückgabe oder Löschung.
- **Incident-Handoff:** Fehlversand, falsche Veröffentlichung, unberechtigtes Teilen oder Verlust physischer Unterlagen.
- **Management-Handoff:** Zielkonflikte, Toolkosten, akzeptierte Ausnahmen oder wiederkehrende Fehlmuster.
- **Audit-/Evidence-Handoff:** fehlende Nachweise für Anwendung, Stichprobe oder Korrektur.

## Typische Fehler

- Labels werden eingeführt, aber niemand kennt die Handlungsfolgen.
- Alle vertraulichen Informationen dürfen weiter per Standard-E-Mail geteilt werden.
- Physische Unterlagen und Ausdrucke werden nicht geregelt.
- Externe Parteien sehen interne Labels, verstehen sie aber nicht.
- Toolblockaden erzeugen Schattenprozesse, weil Ausnahmen fehlen.
- Stichproben zählen nur Labels, nicht tatsächlichen Umgang.
- Fehlkennzeichnungen werden korrigiert, aber Ursachen nicht behoben.

## Fiktives Mini-Beispiel

Ein fiktiver Vertrieb nutzt Angebotsvorlagen mit dem Label „vertraulich“. Eine Stichprobe zeigt, dass Preislisten korrekt gekennzeichnet sind, aber über offene Projektordner geteilt werden. Der Information Owner entscheidet, dass Preislisten nur in einem eingeschränkten Datenraum liegen dürfen. IT passt die Vorlage und Ordnerberechtigungen an. Ein kurzer Teamimpuls erklärt, wann externe Freigaben erlaubt sind und wann Legal einzubeziehen ist.

Evidenz:

- Umgangsmatrix für vertrauliche Vertriebsunterlagen,
- Stichprobenprotokoll,
- korrigierte Ordnerberechtigungen,
- aktualisierte Vorlage,
- Teambriefing-Nachweis,
- offene Legal-Handoff-Regel für externe Sonderfälle.
