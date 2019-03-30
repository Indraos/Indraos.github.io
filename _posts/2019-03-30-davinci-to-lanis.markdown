---
layout: post
title:  Schnittstelle Davinci-Lanis
date:   2019-03-30 08:00:00 +0100
categories: teach
---
Der nachfolgende Eintrag stellt ein Skript für die Umwandlung eines Excel-Exports der Stundenplan-Management-Software in die Schulverwaltungssoftware Lanis vor. Installation, Anwendung und Inkonstistenzen der Formate werden behandelt.
<!--more-->
## Vorbereitungen
Wir nehmen die Ausführung auf einem Windows-Rechner an. Das Skript benötigt die Installation von [Python 3](https://www.python.org/downloads/windows/) (auf der Website hinter dem Link auf Latest Python 3 Release - Python X.X.X, wobei X jeweils eine beliebige Zahl ist). Danach benötigt das Skript einige Erweiterungen von Python, welche Sie installieren können, indem Sie (mit Administrator\*innen-Rechten) eine [Powershell öffnen](https://praxistipps.chip.de/windows-powershell-als-administrator-starten-so-gehts_99831) und dort eingeben:

```
pip install xlrd pandas numpy
```
Sollte `pip` nicht funktionieren, versuchen Sie

```
pip3 install xlrd pandas numpy
```
## Schnittstelle
### Export aus Davinci
Exportieren Sie vie Ansicht "Veranstaltungen" als `.xls`-Datei und speichern Sie die Datei im selben Ordner wie die Datei hinter diesem [Link](/assets/code/davinci_to_lanis.py). Merken Sie sich den Dateinamen der `.xls`-Datei. Nehmen wir etwa an, die Datei heiße `20190330.xls` (für das heutige Datum).
### Umwandlung
Nun [öffnen Sie abermals eine Powershell](https://praxistipps.chip.de/windows-powershell-als-administrator-starten-so-gehts_99831) und geben ein
```
python davinci_to_lanis.py 20190330.xls
```
Ersetzen Sie hier den Dateinamen `20190330.xls` durch den Dateinamen, den Ihre Datei hat. Sollte es mit der obigen Eingabe einen Fehler geben, versuchen Sie
```
python3 davinci_to_lanis.py 20190330.xls
```
### Import in Lanis
Die erschienene `output.csv`-Datei sollte auf Lanis unter der Administration der Funktion "Mein Tag" hochgeladen werden.

## Begrenzungen des Werkzeugs
Davinci kann beliebige Kalenderwochen hinterlegen, in denen Unterricht stattfinden soll, Lanis ist auf A- bzw. B-Wochen beschränkt. Daher wählt das Skript die folgende Näherung: 

> Wenn ab der aktuellen Woche die kommenden drei Wochen eine Unterrichtsstunde so stattfindet, als fände sie nie statt, bzw. als fände sie immer oder in geraden/ungeraden-Wochen statt, dann wird sie als nicht stattfindend, immer stattfindend bzw. A- oder B-Wochen-Unterricht gekennzeichnet.

Konkret heißt das, dass wenn jetzt eine ungerade Woche ist, und diese Woche und übernächste Woche der Unterricht nicht stattfindet, er aber nächste Woche stattfindet, dass der Unterricht als B-Wochen-Unterricht angenommen wird, da er im betrachteten Unterricht in geraden Wochen stattfindet, also per Konvention als B-Wochen-Unterricht betrachtet wird. 

Solange Lanis keine Funktionalität für Blockunterricht bereitstellt wird es nicht möglich sein, eine verlustfreie Umwandlung von Davinci in Lanis vorzunehmen.