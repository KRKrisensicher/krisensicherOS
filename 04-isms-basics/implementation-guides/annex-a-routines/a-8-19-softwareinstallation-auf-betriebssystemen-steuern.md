
# A.8.19 — Softwareinstallation auf Betriebssystemen steuern

## Zweck

Gesteuerte Softwareinstallation verhindert, dass ungeprüfte, veraltete oder nicht benötigte Software auf Endgeräten, Servern und Plattformen Angriffsfläche, Lizenz-/Betriebsrisiken oder Supportprobleme erzeugt. Entscheidend ist eine betreibbare Routine für Freigabe, Bereitstellung, Ausnahme und Entfernung.

## Control-Ziel in Repo-Sprache

Die Organisation legt fest, welche Software auf welchen Betriebssystemen installiert werden darf, über welche Wege Installation erfolgt, wer Freigaben und Ausnahmen verantwortet und wie nicht genehmigte oder riskante Software erkannt und behandelt wird. Die Routine verbindet Endpoint-/Servermanagement, Beschaffung, Lizenzsicht, Schwachstellenmanagement und Zugriffsschutz.

## Typische Risiken

- Wenn Nutzer oder Administratoren beliebige Software installieren, entstehen Schadsoftware-, Schwachstellen- und Datenabflussrisiken.
- Wenn Software aus ungeprüften Quellen bezogen wird, können manipulierte Pakete oder unerwünschte Zusatzkomponenten installiert werden.
- Wenn veraltete oder nicht mehr benötigte Software installiert bleibt, wächst die Angriffsfläche unbemerkt.
- Wenn Server und produktive Systeme manuell verändert werden, wird der Betriebszustand nicht mehr reproduzierbar.
- Wenn Fachbereiche Schatten-Tools installieren, entstehen Daten-, Support- und Lieferantenrisiken außerhalb der Governance.
- Wenn Ausnahmen nicht befristet sind, werden temporäre Installationen dauerhaft.

## Trigger

- neuer Arbeitsplatz, Server, Betriebssystem-Build, Standardimage oder Plattformdienst.
- Anfrage zur Installation neuer Software oder Erweiterung bestehender Software.
- neue Schwachstelle, Herstellerende, Lizenzänderung oder Softwareabkündigung.
- Malware-Fund, ungewöhnliche Prozessausführung oder nicht genehmigte Software im Inventar.
- Wechsel von Softwareverteilung, Endpoint Management, Paketquelle oder Cloud-Basisimage.
- neuer Dienstleister, Fachbereichstool oder SaaS-/Client-Komponente.
- regulärer Review von Softwareinventar, Allow-/Deny-Listen, Ausnahmen und Altsoftware.

## Rollen und Verantwortung

- **Endpoint-/Client Owner:** steuert Softwarekatalog, Standardimages, Paketierung und Installation auf Arbeitsplätzen.
- **Server-/Plattform Owner:** steuert Installationen, Images, Repositories und Konfigurationsmanagement auf Servern und Plattformen.
- **Service Owner / Fachbereich:** begründet Bedarf, fachliche Kritikalität und Nutzungszweck.
- **Security-Rolle / ISMS-Owner:** definiert Risikokriterien, Quellenanforderungen, Ausnahme- und Reviewlogik.
- **Einkauf / Lizenzmanagement:** prüft Bezugsweg, Lizenz-, Support- und Vertragsfragen ohne rechtliche Bewertung durch das Artefakt zu ersetzen.
- **Datenschutz-/Legal-Rolle:** prüft bei personenbezogener Verarbeitung, Vertrags- oder Nutzungsbedingungen die organisationsspezifischen Vorgaben.
- **Management:** entscheidet bei Restrisiken, Schatten-IT, Budgetbedarf oder Konflikten zwischen Fachbedarf und Sicherheitsanforderung.

## Implementierung

### Minimalstart

Ziel: Kritische Systeme und Arbeitsplätze erhalten Software über nachvollziehbare, freigegebene Wege.

1. Scope bestimmen: verwaltete Endgeräte, Server, Admin-Workstations, produktive Systeme und kritische Fachanwendungen.
2. Erlaubte Installationswege festlegen: Softwareverteilung, Paketmanager, freigegebene Repositories, Images oder IT-Serviceprozess.
3. Eine einfache Freigabelogik definieren: Zweck, Owner, Quelle, Kritikalität, Datenbezug, Supportstatus und Sicherheitsprüfung.
4. Nicht genehmigte Softwarefunde in einem Maßnahmenlog nachverfolgen.
5. Lokale Installationsrechte begrenzen, soweit praktikabel, und Ausnahmen dokumentieren.
6. Veraltete oder nicht benötigte Software priorisiert entfernen.

### Solide Praxis

Ziel: Softwareinstallation ist standardisiert, inventarisiert und mit Risiko- und Betriebsprozessen verbunden.

1. Softwarekataloge unterscheiden Standardsoftware, freigegebene Zusatzsoftware, eingeschränkte Software und verbotene Software.
2. Installationen erfolgen über zentrale Verteilung, Paketquellen, Build-Pipelines oder Infrastructure-as-Code statt manueller Einzeländerungen.
3. Softwareinventar wird regelmäßig mit Freigaben, Lizenzen, Schwachstellen und Supportstatus abgeglichen.
4. Neue Software wird vor Freigabe risikobasiert geprüft: Quelle, Hersteller, Berechtigungen, Auto-Update, Datenflüsse, Abhängigkeiten.
5. Ausnahmen haben Owner, Begründung, Laufzeit, Kompensationsmaßnahme und Wiedervorlage.
6. Server- und produktive Systemänderungen sind mit Change Management verbunden.
7. Schatten-IT-Funde führen zu Fachbereichsgespräch, Risikobewertung und Entscheidung statt nur zu Löschung.

### Fortgeschritten

Ziel: Softwareinstallation ist automatisiert kontrolliert, reproduzierbar und in Security Operations integriert.

1. Endpoint- und Servermanagement erzwingen erlaubte Installationspfade und blockieren nicht freigegebene Quellen oder Ausführungen.
2. Application Control, Paket-Signaturen, Repository-Governance und Baseline-Images reduzieren Manipulations- und Wildwuchsrisiken.
3. Softwareinventar ist mit Schwachstellenmanagement, Assetmanagement, Lizenzsicht und EDR/Monitoring verbunden.
4. Golden Images, Container-Basisimages und Server-Builds sind versioniert, getestet und reviewfähig.
5. Installation auf produktiven Systemen erfolgt über Change, Pipeline oder Konfigurationsmanagement mit Rollback-Möglichkeit.
6. Erkennung nicht genehmigter Software erzeugt Tickets oder Security-Triage.
7. Managementberichte zeigen Altsoftware, Schatten-IT, Ausnahmequote, technische Schulden und Ressourcenbedarf.

## Ablauf als Routine

1. **Bedarf oder Fund entsteht:** Softwareanfrage, neuer Build, Inventarfund, Schwachstelle oder Fachbereichsbedarf.
2. **Bewerten:** Zweck, Quelle, betroffene Systeme, Datenbezug, Berechtigungen, Supportstatus und Risiken prüfen.
3. **Entscheiden:** freigeben, ablehnen, befristet erlauben, ersetzen oder entfernen.
4. **Bereitstellen:** kontrollierter Installationsweg mit Version, Quelle und Owner.
5. **Nachweisen:** Installation, Freigabe, Ausnahme oder Entfernung dokumentieren.
6. **Überwachen:** Inventar, Schwachstellen, nicht genehmigte Funde und End-of-Life-Status prüfen.
7. **Eskalieren:** ungeklärte Schatten-IT, hohe Risiken oder Fachkonflikte an Management oder passende Handoffs geben.
8. **Verbessern:** Softwarekatalog, Paketquellen, Rechte und Build-Prozesse anpassen.

## Entscheidungen

- Welche Betriebssysteme und Systemklassen sind im Scope der Installationssteuerung?
- Welche Installationsquellen sind erlaubt und welche werden blockiert?
- Welche Software braucht Security-, Datenschutz-, Lizenz- oder Architekturreview vor Freigabe?
- Wer darf lokale Installationen oder temporäre Ausnahmen genehmigen?
- Wie werden Fachbereichsbedarf und Sicherheits-/Betriebsrisiko gegeneinander entschieden?
- Wann wird Software entfernt, ersetzt oder in eine verwaltete Bereitstellung überführt?
- Welche Schatten-IT-Risiken werden akzeptiert, kompensiert oder eskaliert?

## Evidenz

### Starke Evidenz

- Softwarekatalog oder Allow-/Deny-Logik mit Owner und Reviewdatum,
- Freigaben für neue Software mit Zweck, Quelle, Version und Risikobewertung,
- Nachweise aus Softwareverteilung, Paketmanager, MDM/Endpoint Management oder Konfigurationsmanagement,
- Inventarabgleich mit nicht genehmigten Funden und Maßnahmen,
- Ausnahmen mit Begründung, Laufzeit und Wiedervorlage,
- Change-Nachweise für Installationen auf produktiven Systemen,
- Entfernungsnachweise für veraltete oder riskante Software.

### Schwache Evidenz

- allgemeine IT-Richtlinie ohne Installationsweg und Kontrolle,
- manuelle Excel-Liste ohne Inventarabgleich,
- „Adminrechte nur für IT“ ohne Prüfung tatsächlicher Installationen,
- Softwareverteilungsscreenshot ohne Freigabe- oder Scopebezug,
- Lizenzliste ohne Sicherheits- und Supportstatus,
- Ausnahme per Chatnachricht ohne Ablaufdatum.

### Evidenzlücken

- keine Übersicht installierter Software auf kritischen Systemen,
- unklare Installationsquellen,
- lokale Adminrechte ohne Begrenzung oder Review,
- keine Behandlung nicht genehmigter Software,
- kein Prozess für End-of-Life- oder veraltete Software,
- Fachbereichstools ohne Owner, Vertrag oder Datenbezug,
- produktive Server werden manuell verändert, ohne Change-Nachweis.

## Wirksamkeitsprüfung

Prüffragen:

- Sind erlaubte Installationswege für Endgeräte, Server und produktive Systeme definiert?
- Gibt es einen aktuellen Softwarekatalog oder eine vergleichbare Freigabelogik?
- Werden nicht genehmigte Installationen erkannt und behandelt?
- Sind lokale Installationsrechte begrenzt und Ausnahmen nachvollziehbar?
- Werden Schwachstellen, Supportende und nicht mehr benötigte Software in Entscheidungen einbezogen?
- Sind produktive Änderungen reproduzierbar und mit Change Management verbunden?
- Werden Fachbereichsbedarfe entschieden statt in Schatten-IT verdrängt?

Mögliche Kennzahlen:

- Anteil verwalteter Installationen,
- Anzahl nicht genehmigter Softwarefunde,
- offene Ausnahmen und überfällige Reviews,
- Systeme mit veralteter oder nicht unterstützter Software,
- Zeit von Softwareanfrage bis Entscheidung,
- entfernte riskante Software pro Reviewzyklus,
- produktive Installationen ohne Change-Bezug.

## BSIG-/NIS2-Anschluss

Gesteuerte Softwareinstallation ist anschlussfähig an NIS2-orientierte Themen wie Cyberhygiene, Schwachstellenmanagement, sichere Konfiguration, Zugriffsschutz, Lieferketten- und Dienstleistersteuerung sowie technische Risikobehandlung. Der konkrete Bezug sollte im Anforderungsregister, im Asset- und Softwareinventar sowie im Change- und Risikomanagement organisationsspezifisch geprüft werden.

Dieses Artefakt ersetzt keine rechtliche Bewertung von Lizenz-, Vertrags-, Datenschutz- oder Nachweispflichten.

## Grenzen

- Dieses Artefakt ist keine Lizenzberatung und keine vollständige Endpoint-Hardening-Baseline.
- Es ersetzt keine technische Analyse einzelner Softwareprodukte, Paketquellen oder Lieferkettenrisiken.
- Vollständige Blockierung jeder Nutzerinstallation kann fachlich unpraktisch sein; Ziel ist risikobasierte Steuerung.
- Keine Zertifizierungs-, Konformitäts- oder Sicherheitsgarantie.
- Keine Nutzung echter Inventare, Kundendaten, Lizenzschlüssel oder Geheimnisse in öffentlichen Beispielen.

## Handoffs

- **Schwachstellenmanagement-Handoff:** installierte Software ist verwundbar, veraltet oder nicht mehr unterstützt.
- **Change-Handoff:** Installation oder Entfernung betrifft produktive Systeme, Services oder Rollback-Fähigkeit.
- **Einkauf-/Lizenz-Handoff:** Bezugsweg, Vertrag, Support, Lizenz oder Herstellerbeziehung ist ungeklärt.
- **Datenschutz-/Legal-Handoff:** Software verarbeitet personenbezogene Daten, sendet Telemetrie oder hat unklare Nutzungsbedingungen.
- **Incident-Handoff:** nicht genehmigte Software, Malwareverdacht oder manipulierte Pakete werden entdeckt.
- **Management-Handoff:** Fachbereich benötigt riskante Software, Schatten-IT ist verbreitet oder Tooling/Ressourcen fehlen.
- **Audit-/Evidence-Handoff:** Freigaben, Inventar oder Entfernungsnachweise sind lückenhaft.

## Typische Fehler

- Softwareinstallation wird nur über lokale Adminrechte betrachtet, nicht über Quellen, Freigabe und Inventar.
- Server werden manuell verändert und verlieren ihren reproduzierbaren Betriebszustand.
- Standardsoftware wird freigegeben, aber nie auf Supportende oder Schwachstellen geprüft.
- Fachbereichsbedarf wird blockiert, ohne eine sichere Alternative zu entscheiden.
- Ausnahmen werden dauerhaft, weil kein Reviewdatum existiert.
- Schatten-IT wird nur technisch gelöscht, ohne Ursache und Risiko zu klären.
- Management sieht Lizenzkosten, aber keine Sicherheits- und Betriebsrisiken aus Softwarewildwuchs.

## Fiktives Mini-Beispiel

Ein fiktiver Fachbereich möchte ein lokales Analysewerkzeug auf mehreren Notebooks installieren. Der Endpoint Owner prüft Quelle, Updateweg und benötigte Rechte; die Datenschutzrolle wird eingebunden, weil Dateien mit personenbezogenen Daten verarbeitet werden könnten. Die Software wird zunächst für fünf Nutzer befristet über die Softwareverteilung bereitgestellt. EDR und Inventar prüfen die Installation, nach sechs Wochen bewertet der Service Owner Nutzen und Risiken. Eine nicht freigegebene Alternativsoftware auf zwei Geräten wird entfernt und als Schatten-IT-Fund im Maßnahmenlog dokumentiert.
