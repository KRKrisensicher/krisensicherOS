
# A.8.2 — Privilegierte Rechte steuern

## Zweck

Privilegierte Rechte erlauben tiefgreifende Änderungen an Systemen, Daten, Identitäten und Sicherheitsfunktionen. Diese Routine sorgt dafür, dass solche Rechte nicht nebenbei entstehen, sondern gezielt beantragt, begründet, begrenzt, überwacht, reviewed und bei Bedarf entzogen werden.

## Control-Ziel in Repo-Sprache

Die Organisation betreibt eine eigene Steuerung für privilegierte Rechte. Admin-, Root-, Superuser-, Cloud-, Datenbank-, Security-, Netzwerk-, CI/CD- und Notfallrechte werden mit Owner, Zweck, Genehmigung, technischer Umsetzung, Protokollierung, Review und Ausnahmebehandlung geführt.

## Typische Risiken

- Wenn privilegierte Rechte dauerhaft und breit vergeben werden, kann ein kompromittiertes Konto großen Schaden verursachen.
- Wenn Adminrechte nicht von Alltagskonten getrennt werden, steigt das Risiko durch Phishing, Malware oder Fehlbedienung.
- Wenn Notfall- oder Break-Glass-Konten nicht geprüft werden, bleiben Hintertüren oder unerkannte Nutzung möglich.
- Wenn Dienstleister privilegierte Zugänge ohne Begrenzung erhalten, fehlen Kontrolle und Verantwortlichkeit.
- Wenn Protokollierung oder Review fehlen, werden Missbrauch, Fehlkonfigurationen und zu weitgehende Rechte spät erkannt.

## Trigger

- neuer Adminbedarf, neues System, neue Plattform, neue Cloud- oder SaaS-Administration.
- Rollenwechsel, Eintritt, Austritt oder Ende eines Dienstleistereinsatzes.
- Sicherheitsereignis, Verdacht auf Kontokompromittierung oder auffällige Adminaktivität.
- Änderung von Rollenmodell, Berechtigungsgruppen, PAM-/IAM-Tooling oder Notfallzugängen.
- Auditfinding, Schwachstelle, Penetrationstest oder Managementfrage.
- turnusmäßiger Review privilegierter Rechte.

## Rollen und Verantwortung

- **System-/Service Owner:** bestätigt Bedarf, Kritikalität und fachliche Berechtigung.
- **IT-/Plattform Owner:** setzt Rechte technisch um und stellt Protokolle oder Exporte bereit.
- **Security-Rolle / ISMS-Owner:** definiert Mindestanforderungen, Reviewfrequenz, Eskalationslogik und Ausnahmebehandlung.
- **Führungskraft / Prozess Owner:** bestätigt Rollenbezug und Trennung von Aufgaben.
- **Lieferantenmanagement:** steuert privilegierte Zugänge externer Administratoren.
- **Datenschutz / Legal:** prüft personenbezogene Protokolle, Dienstleister- und Beschäftigtenthemen.
- **Management:** entscheidet bei dauerhaften Ausnahmen, fehlender Trennung, Ressourcenmangel oder akzeptiertem Restrisiko.

## Implementierung

### Minimalstart

Ziel: die kritischsten privilegierten Rechte sichtbar und reviewfähig machen.

1. Kritische Adminrechte werden identifiziert: Identitätsplattform, zentrale Server, Cloud, Netzwerk, Security-Tools, Datenbanken und Kernanwendungen.
2. Jedes privilegierte Konto erhält Owner, Zweck, Nutzer/Verantwortlichen und Gültigkeit.
3. Neue Rechte werden nur per Antrag/Ticket mit fachlicher Freigabe vergeben.
4. Adminrechte werden getrennt von Alltagskonten betrachtet und mindestens für kritische Systeme regelmäßig reviewed.
5. Austritt, Rollenwechsel und Dienstleisterende lösen Entzug oder Prüfung aus.
6. Notfallkonten werden inventarisiert und Nutzung wird nachträglich geprüft.

Minimaler Nachweis:

- Liste privilegierter Konten/Gruppen im kritischen Scope,
- Anträge und Freigaben,
- Reviewprotokoll mit Entscheidungen,
- Nachweis über entzogene Rechte,
- Ausnahme- oder Break-Glass-Dokumentation.

### Solide Praxis

Ziel: privilegierte Rechte werden begrenzt, überwacht und mit Risikoentscheidungen verbunden.

1. Privilegientypen werden klassifiziert: dauerhafte Adminrechte, zeitlich begrenzte Rechte, Notfallrechte, Service-/Automationskonten, externe Adminzugänge.
2. Für kritische Tätigkeiten werden starke Authentisierung, rollenbasierte Gruppen und getrennte Konten genutzt.
3. Rechte werden nach Least-Privilege-Logik und Aufgabentrennung geprüft, ohne operative Arbeitsfähigkeit blind zu blockieren.
4. Privilegierte Aktivitäten werden angemessen protokolliert und bei Auffälligkeiten triagiert.
5. Externe Adminzugänge sind befristet, vertragsbezogen und technisch begrenzt.
6. Ausnahmen erhalten Ablaufdatum, Kompensationsmaßnahme und Risikoentscheidung.

Starke Evidenz:

- Privilegienregister mit Typ, Owner, Zweck und Gültigkeit,
- Rollen-/Gruppenkatalog für Adminrechte,
- Rezertifizierungsprotokolle,
- Nachweise zu MFA, getrennten Konten oder PAM-Mechanismen,
- Protokollreview oder auffällige Aktivitätsauswertung,
- Ausnahmeentscheidungen mit Wiedervorlage.

### Fortgeschritten

Ziel: privilegierte Rechte werden dynamisch, überprüfbar und detektionsfähig gesteuert.

1. Just-in-time- oder zeitlich begrenzte Privilegien ersetzen dauerhafte Adminrechte, wo sinnvoll.
2. PAM/IAM, Ticketing, Assetkritikalität und Protokollierung sind miteinander verbunden.
3. Adminsessions für kritische Systeme werden risikobasiert aufgezeichnet oder kontrolliert.
4. Risikoindikatoren wie ungewöhnliche Zeiten, neue Zielsysteme oder Massenänderungen lösen Triage aus.
5. Break-Glass-Prozesse werden getestet und nach Nutzung reviewed.
6. Management sieht überfällige Reviews, dauerhafte Hochrisikorechte, externe Adminzugänge und nicht umsetzbare Trennungskonflikte.

## Ablauf als Routine

1. **Privilegienbedarf entsteht:** Systembetrieb, Projekt, Incident, Dienstleister oder Notfall.
2. **Antrag erfassen:** Person/Konto, Zielsystem, Zweck, Zeitraum, Rechteumfang und Risiko.
3. **Fachlich und technisch prüfen:** Owner, Aufgabenbezug, Trennungskonflikt, Alternativen und Schutzmaßnahmen.
4. **Genehmigen und umsetzen:** Rechte begrenzen, authentisieren, protokollieren und dokumentieren.
5. **Nutzen und überwachen:** Aktivitäten, Abweichungen und Notfallnutzung prüfen.
6. **Review durchführen:** bestätigen, reduzieren, entziehen oder eskalieren.
7. **Ausnahmen steuern:** befristet, begründet, mit Kompensation und Wiedervorlage.
8. **Verbessern:** Muster in Rollenmodell, Tooling, Schulung oder Architektur zurückspielen.

## Entscheidungen

- Welche Rechte gelten als privilegiert und kritisch genug für Sondersteuerung?
- Welche Rechte dürfen dauerhaft sein, welche nur zeitlich begrenzt?
- Wann sind getrennte Admin-Konten, MFA, PAM oder Sessionkontrolle erforderlich?
- Wer darf Notfallkonten nutzen und wer prüft die Nutzung?
- Welche Trennungskonflikte sind nicht akzeptabel, welche brauchen Managemententscheidung?
- Wie werden externe Adminzugänge begrenzt und beendet?

## Evidenz

### Starke Evidenz

- aktuelles Privilegienregister oder Gruppenexport mit Ownern,
- genehmigte Anträge mit Zweck und Laufzeit,
- technische Nachweise zu Umsetzung, MFA oder getrennten Konten,
- Reviewprotokolle mit Entzug/Korrektur,
- Protokollauswertungen oder Sessionnachweise für kritische Aktivitäten,
- Break-Glass-Test oder Nutzungsreview,
- Managemententscheidung bei dauerhaften Ausnahmen.

### Schwache Evidenz

- allgemeine Admin-Policy ohne konkrete Rechteübersicht,
- Screenshot einer Admin-Gruppe ohne Owner oder Reviewdatum,
- Toolbehauptung „PAM vorhanden“ ohne Nutzung und Review,
- Protokolle ohne Auswertung,
- pauschale Dienstleisterkonten ohne Vertrags- oder Personenbezug.

### Evidenzlücken

- privilegierte Konten ohne zuordenbaren Verantwortlichen,
- ehemalige Beschäftigte oder Dienstleister mit Adminrechten,
- Break-Glass-Konten ohne Test und Nutzungsprüfung,
- Servicekonten mit übermäßigen Rechten,
- Ausnahmen ohne Ablaufdatum oder Risikoentscheidung.

## Wirksamkeitsprüfung

Prüffragen:

- Sind privilegierte Rechte für kritische Systeme vollständig sichtbar?
- Kann für ein Adminrecht erklärt werden, warum es existiert und wer es genehmigt hat?
- Werden Rollenwechsel, Austritt und Dienstleisterende zeitnah verarbeitet?
- Werden Notfall- und externe Adminzugänge gesondert geprüft?
- Führen Reviews zu tatsächlichem Entzug oder Reduktion?
- Werden auffällige Adminaktivitäten triagiert und eskaliert?

Mögliche Kennzahlen:

- Anzahl privilegierter Konten je kritischem System,
- überfällige Privilegienreviews,
- dauerhafte Hochrisikorechte,
- externe Adminzugänge ohne Ablaufdatum,
- Break-Glass-Nutzungen und Reviews,
- entzogene oder reduzierte Rechte je Review.

## BSIG-/NIS2-Anschluss

Steuerung privilegierter Rechte ist anschlussfähig an NIS2-orientierte Themen wie Zugriffsschutz, Cyberhygiene, Incident-Prävention, sichere Administration, Dienstleistersteuerung und Risikomanagement. Der konkrete Bezug sollte im Anforderungsregister, im Zugriffskonzept und im Management Review geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Prüfung und keine Datenschutzbewertung von Protokollierung oder Beschäftigtendaten.

## Grenzen

- Dieses Artefakt ist kein vollständiges IAM- oder PAM-Design.
- Es ersetzt keine technische Architekturprüfung und keine Datenschutzprüfung für Logging.
- Es verspricht keine Zertifizierungsfähigkeit oder gesetzliche Erfüllung.
- Es enthält keine vertraulichen Adminlisten oder produktiven Systemdetails.
- Ein PAM-Tool allein ist keine wirksame Governance-Routine.

## Handoffs

- **Access-/IAM-Handoff:** Rollenmodell, Joiner-Mover-Leaver, Gruppen und technische Konten.
- **Incident-Handoff:** kompromittiertes Konto, verdächtige Adminaktivität oder Notfallnutzung.
- **Lieferanten-Handoff:** externe Adminrechte, Vertragsende, Managed-Service-Zugang.
- **Datenschutz-/Legal-Handoff:** personenbezogene Protokolle, Session Recording, arbeitsrechtliche Fragen.
- **Change-/Operations-Handoff:** privilegierte Änderungen an kritischen Systemen.
- **Management-Handoff:** nicht umsetzbare Aufgabentrennung, dauerhafte Ausnahmen, Ressourcenbedarf.
- **Audit-/Evidence-Handoff:** fehlende Owner, lückenhafte Reviews oder unklare Break-Glass-Nutzung.

## Typische Fehler

- Adminrechte werden im allgemeinen Berechtigungsreview versteckt.
- Alltagskonten und Adminrollen sind nicht getrennt.
- Notfallkonten existieren, werden aber nie getestet oder reviewed.
- Dienstleisterzugänge bleiben nach Projektende aktiv.
- Protokollierung wird eingeschaltet, aber niemand prüft Auffälligkeiten.
- Ausnahmen für Legacy-Systeme werden dauerhaft und unsichtbar.
- Servicekonten werden vergessen, obwohl sie hohe Rechte haben.

## Fiktives Mini-Beispiel

Ein fiktives SaaS-Team prüft seine Cloud-Administratoren. Der Export zeigt acht Owner-Rechte, davon zwei für ehemalige Projektrollen und ein dauerhaftes Dienstleisterkonto. Der Service Owner bestätigt nur fünf aktive Bedarfe. Zwei Rechte werden entzogen, das Dienstleisterkonto wird auf zeitlich begrenzten Zugriff umgestellt. Für ein Break-Glass-Konto wird ein Test und ein monatlicher Nutzungsreview eingeführt.

Evidenz:

- Cloud-Admin-Export,
- Reviewentscheidung des Service Owners,
- Tickets zum Rechteentzug,
- neue Freigabe für Dienstleisterzugriff,
- Break-Glass-Testprotokoll,
- Management-Review-Punkt zur dauerhaften Privilegienreduktion.
