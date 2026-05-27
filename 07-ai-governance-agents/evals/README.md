
# Evals und Qualitätsgates

Dieser Ordner enthält Prüfroutinen für krisensicherOS-Artefakte.

Ziel ist nicht formale Bürokratie, sondern verlässliche Qualität: Jedes Artefakt soll public-safe, fachlich begrenzt, betreibbar, portabel und empowerment-orientiert sein.

## Prüfebenen

1. **Public-Safety**  
   Keine echten Personen-, Kunden-, Organisations-, Secret- oder privaten Workspace-Daten.

2. **Claim-Safety**  
   Keine Rechtsberatung, Datenschutzberatung, Zertifizierungs-, Konformitäts- oder Sicherheitsgarantien.

3. **Betriebslogik**  
   Rollen, Trigger, Inputs, Ablauf, Outputs, Evidenz, Entscheidungen und Reviews sind klar.

4. **Empowerment**  
   Das Artefakt stärkt interne Fähigkeiten und erzeugt keine unnötige Beratungs- oder Agentenabhängigkeit.

5. **Portabilität**  
   Kanonische Artefakte bleiben tool- und adapterneutral.

6. **Handoff-Fähigkeit**  
   Zuständigkeiten, menschliche Prüfpunkte und Agentenübergaben sind nachvollziehbar.

## Nutzung

Vor Abschluss eines Artefakts:

1. passenden Artefakttyp identifizieren,
2. Gates aus `quality-gates.md` anwenden,
3. Stop-Punkte markieren,
4. Korrekturen durchführen,
5. Ergebnis mit kurzem Prüfnachweis abschließen.

## Minimaler Prüfnachweis

```text
Artefakt:
Gates geprüft:
Feststellungen:
Korrekturen:
Offene menschliche Prüfung:
Ergebnis: pass / pass with notes / stop
```

## Stop bedeutet

Ein Stop ist kein Fehler, sondern ein Sicherheitsmechanismus. Stoppen, wenn ein Artefakt menschliche Entscheidung, rechtliche Prüfung, Datenschutzprüfung, Lizenzprüfung, echte Daten oder Veröffentlichung berührt.
