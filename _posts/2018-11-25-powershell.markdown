---
layout: post
title:  Powershell-Grundlagen
date:   2018-11-25 08:00:00 +0100
categories: teach
---
# Power Shell
Die Power Shell wurde 2006 als Update für Windows Clients eingeführt und ist mittlerweile wichtiges Werkzeug für Administrator\*innen. Wir werden uns die Power Shell in 5 Bereichen ansehen: 

 - Grundlegende Software: Wir passen die Power Shell und das Integrated Scripting Environment an. Wir nutzen grundlegende Shortcuts für die Power Shell. Wir lernen, was Execution Policys für die Ausführung von Scripts bedeutet. 
 - Syntax: Wir lernen, wie wir Variablen definieren, wie wir Alias definieren, die Syntax von Kontrollstrukturen, Klammerausdrücke (`()`, `$()`, `@()`, `@{}`), Strukturierung von Skripten (begin, process, end), die Syntax erweiterter Funktionen, Operatoren sowie Umleitung von Ausgaben (`>`, `>>`, `2>`, `2>>`), wir können Pipeline-Ausgaben formatieren.
 - Objektorientierung: Wir können begründen, was die Vorteile der Power Shell gegenüber einer normalen Shell ist. Wir können Objekt, Klasse, Methode, Statik, Konstruktor und Attribut definieren.
 - Erweiterungen: Wir können Module, Snapins, Assemblys installieren und neue Module mithilfe von Find-Module finden.
 - Remote-Wartung: Wir nutzen das bisher gelernte, um eine Fernwartung über das Netzwerk zu machen. 

##  Einstieg in die Power Shell
Öffne die Power Shell mit `[windows] + r`, `[enter]` und dann `powershell`. Öffnet weiterhin das Power Shell Integrated Scripting Environment mir `[windows] + r`, `[enter]` und dann `powershell ise`. Um in die Einstellungen der Power Shell zu gelangen, klicke links oben am Fenster auf das Icon und drücke auf „Eigenschaften“. Die Einstellungen bei der ISE sind ein Menüpunkt.

> Beantworte die folgenden Fragen schriftlich, ich schaue mir die Antworten am Ende an: 1. Wie passe ich die Schriftart in der Power Shell an? Wie geht das in der ISE 2. Funktioniert Copy-Paste in der Power Shell? 3. Wie erstelle ich ein neues Skript in der ISE? 4. Was brauche ich, um eine Remote-Registerkarte zu öffnen? In welcher Rolle könntet ihr eine solche Registerkarte brauchen.

Sollte es im folgenden einmal ein Problem in der Power Shell geben, dann könnt ihr den derzeit aktiven Prozess mit `[ctrl]` + `c`. 

> > Erstellt ein Skript mit dem Inhalt `echo "Hallo Welt"` und speichert sie an einem beliebigen Ort unter dem Namen `hello_world.ps1`. `cd`t zum Speicherort der Datei in der Konsole unten in der ISE und tippt `hel`. Ein Druck auf die Tabulator-Taste sollte `.\hello_world.ps1` hervorzaubern. Ein Enter gibt euch „Hallo Welt“ aus. Euer erstes Skript.
  
Es verbleibt, sich mit Execution Policies auseinander zu setzen. Programme, die wir auf der Power Shell ausführen können, enden mit `.ps1`. Diese können potenziell mächtig und damit auch potenziell schädlich sein. Es ist also im Interesse des Administrators, Kontrolle darüber zu haben, was der Computer ohne zu fragen ausführen soll.

> Tippt `Get-ExecutionPolicy` ein. 

Ihr solltet alle `Unrestricted` sehen.  „Unrestricted“ bedeutet, dass alle Skripte ausgeführt werden, die die Person an der Power Shell ausführen möchte (dies ändert nichts daran, dass für Änderungen an bestimmten Ordnern Admin-Rechte benötigt werden). Eine andere, `RemoteSigned` fordert, dass Chips, die z.B. aus dem Internet herunter geladen wurden, oder allgemeiner von einem fremden Rechner stammen, digital signiert (also im Sinne von Kryptographie!) sein müssen, um ausgeführt zu werden.


## Syntax 1
Die Power Shell hat einen Funktionsumfang wie die „normale“ Konsole (fortan cmd) — und noch einiges mehr. Mit dem Teil, den ihr bereits os ähnlich aus der normalen Konsole kennt, wolle wir uns heute anschauen.

### Variablem
Ihr könnt Variablen mit `$myvariable = 4` definieren. Variablennamen sollten alphanumerisch sein und werden durch ein Dollarzeichen eingeleitet. In cmd wurde dies mit `set` gemacht. Unsere Shell hat einen Großteil ihrer „Powers“ dadurch, dass sie Dateitypen ermöglicht. Diese Variablen können dann nicht mit irgendetwas „beschrieben“, sondern nur einem Dateityp.

> Gib `[Int32]$a = 4` und dann `$a = „Hi“`. Beschreibt schriftlich, was die Fehlermeldung euch sagt.

Wenn ihr Variablen ausgeben wollt, so tippt `$a` ein. Wenn ihr den Typen einer Variable wissen wollt, so tippt `$a.GetType()` ein. 

> Macht das mit eurer obigen Variable `$a`. 

Es gibt einige besondere Variablen, die immer definiert sind.

> Lasst euch die folgenden Variablen einmal ausgeben.

| Variable | Beschreibung |
|:--|:--|
| `$args` | Dies ist eine Liste mit allen Eingaben von Funktionen (die schauen wir uns später an). |
| `$_` | Dies ist die letzte Eingabe der Konsole. |
| `$input` | Dies ist eine Liste mit allen Eingaben via einer Pipeline. |
| `$error` | Dieser enthält alle Fehlermeldungen (die wir uns auch später ansehen). |

### Operatoren
Es gibt in der Power Shell viele Operatoren. Da hauptsächlich die für Zahlen und logische für uns erst einmal wichtig sein werden, machen wir hier eine Liste.

| Operator | Beschreibung |
|:--|:--|
| `$a -gt $b` | `$a` ist größer als `$b`. |
| `$a -ge $b` | `$a` ist größer oder gleich als `$b`. |
| `$a -lt $b` | `$a` ist kleiner `$b`. |
| `$a -le $b` | `$a` ist kleiner gleich `$b`. |
| `$a -eq $b` | `$a` ist gleich `$b`. |
| `$a -ne $b` | `$a` ist nicht gleich `$b`. |
| `$a -and $b` | `$a` und `$b` sind `True`. |
| `$a -or $b` | `$a` oder `$b` sind `True`. |
| `$a -xor $b` | `$a` xor `$b` sind `True`. |
| `!$a` | `$a` ist `False`. |

### Kontrollstrukturen
Es gibt auch For-, While-, Do-While- und Do-Until-Schleifen, If-Then-Else- oder Case-Statements in der Powershell.

> Lege eine Tabelle mit drei Spalten an: Schleife, Syntax, Beschreibung. Lies dir hierzu den [Artikel](https://en.wikiversity.org/wiki/PowerShell/Loops) durch. Ergänze für jedes Kontroll-Statement einen Eintrag. Tipp: Schaue dir insbesondere die Lernvideos an, falls du nicht verstehst. 

Wir enden mit einer größeren Aufgabe: 

> Legt ein Skript an, welches in der ersten Zeile `$a = 36` hat. Wir wollen bestimmen, ob `$a` einen Teiler ungleich Eins hat, also es eine Zahl gibt, deren Vielfaches `36` ist (das stimmt natürlich, aber euer Programm sollte auch für andere Werte von `$a` funktionieren). Nutzt hierfür Kontrollstrukturen, Variablen und Operatoren. Die Ausgabe sollte `True` oder `False` sein.

Das nächste Mal geht es mit verschiedenen Klammerausdrücken und Funktionen weiter. Danach werden wir beginnen, objektorientiert zu arbeiten. 

+++

Heute beschäftigen wir uns mit Klammerausdrücken und Funktionen. Da die Aufgabe beim letzten Mal schwer gefallen ist, gibt es hier einmal eine Lösung. 

```
$a = 36
for($i=2; $i*$i -le $a; $i++)
{
	if($a % $i -eq 0)
	{
		echo "Die Zahl hat einen Teiler:"
		echo $i
		return
	}
}
echo "Die Zahl hat keine Teiler außer 1 und "
echo $a
```

Vollziehe die Lösung Zeile für Zeile nach. Wir wollen diese Funktion etwas schöner machen und eine weitergehende Aufgabe machen:

> Wir wollen eine Funktion schreiben, die aus einer Liste von Zahlen alle mit mehr als fünf Teilern ausgibt. Sie soll für jede Zahl `$b` den Satz „Die Zahl ? hat mehr als fünf Teiler.“ ausgeben. 

Ein Teiler von einer Zahl $k$ ist eine Zahl $n$, so dass es eine Zahl $m$ gibt mit $k = m \cdot n$. Genug Mathe: Zum Beispiel sind die Teiler von $56$ die Zahlen $2$, $2$, $2$, $7$, da $56 = 2\cdot 2 \cdot 2 \cdot 7$. 

Um diese Aufgabe zu lösen, brauchen wir mehr von der Sprache PowerShell. 

## Syntax 2
Wir brauchen: 

 - Funktionen
 - Wie arbeite ich mit Listen?
 - Wie kriege ich die Länge von Listen?
 - Wie mache ich eine Ausgabe

Fangen wir erst einmal mit verschiedenen Arten von Listen an
### Listen
Eine Liste ist eine sortierte, nicht indizierte Datenstruktur von Elementen. Dies wird oft unterschieden vom Array, wo man auf Elemente per Index zugreifen kann. Die Powershell macht diese Unterscheidung *nicht*. Die Lang-Syntax um ein typisiertes Array von Integren zu erstellen wäre
```
[int32[]]$a = @(1,2,3)
```
Der Datentyp ist eine Liste von `int32`s und wir gehen sicher, dass in der Variable nur solche Arrays stehen können. Es würde einen Fehler geben, wenn wir hier einen String schreiben wollen. Das können wir mit
```
$a[1] = "Hello World"
```
bewerkstelligen.  Wie bei vielem gibt es eine Kurzform, wenn wir die Programmiersprache (in unserem Fall also die Power Shell) herausfinden lassen wollen, was der Typ ist. Statt des obigen Codes reicht es, 
```
$a = 1, 2, 3
```
zu schreiben. Um ein Element zu einer Liste hinzuzufügen, schreibt
```
$a += "neueselement"
```

> Aufgabe finde heraus (mithilfe des Internets), wie du eine Liste von 3 Listen mit jeweils den Elementen $1, 2, 3$ anlegst. Es sollte also z.B. `$a[1][1] = 1`, `$a[1][2] = 2` und `$a[1][3] = 3` sein.

Um mir die Länge von einer Liste `$a` ausgeben zu lassen, kann ich `$a.Length()` tippen.
## Hashtables
Manchmal (jedoch nicht für unsere Aufgabe oben) ist es interessant, eine Liste, deren Einträge mit z.B. Strings indiziert sind, zu definieren. Ein Beispiel wäre eine Liste, in der Städtenamen Einwohneranzahlen zugeordnet sind. Die Syntax hierfür ist
```
 HashTable$a = @{"Frankfurt" = 700000; "Stuttgart" = 1000000}
```
> Lege eine Hashtable an, die Die Namen eurer Klasse als Keys und deren Alter als Values hat. 
> Probiert einmal `$a.GetType()` aus. Was ist der Typ von einer Hashtable?

Sowohl Keys als auch Values können beliebige Typen sein (mehr über Typen gibt es nachte Woche).
## Erweiterte Funktionen
Wir wollen uns nun aber wieder unseres Problems annehmen: Hierfür benötigen wir Funktionen. In der Powershell gibt es zwei Arten von Funktionen: „normale“ und „erweiterte“ (*extended functions*). Wir beginnen mit Funktionen
### Funktionen
Ich packe die obige Lösung in eine Funktion. Dies sollte die Syntax überwiegend klären („GetDivisors“ heißt „finde die Teiler“)

```
function global:GetDivisors([Int] $a)
{
	for($i=2; $i*$i -le $a; $i++)
	{
		if($a % $i -eq 0)
		{
			return True
		}
	}
	return False
}
```

Das Wort `global` sagt, dass diese Funktion überall zur Verfügung steht. Dies ist zwar verpflichtend, ihr macht aber gerade keinen Fehler, wenn ihr es erst einmal überall scheint und euch keine Gedanken macht.

> Schreibe mit einem Partner neben alle Zeilen einen Kommentar. Durchlauft das Programm händisch (schreibt auf, welche Rechnungen der Computer macht) für `$a$ = 5`.

 > Schreibe eine Funktion, für das obige Problem. Dabei hilft dir, deine Teilerfunktion wieder zu benutzen, in einer weiteren Variablen die Teiler aber zu zählen und eine `foreach`-Schleife zu nutzen. Arbeite mit einem Partner.

Die Funktion `GetDivisors` kann ich in der Shell dann als `GetDivisors(5)` aufrufen. Häufig ist aber gewünscht, die Funktionen wie eine normale Kommandozeilenfunktion wie `cd` oder auch `ls` zu nutzen. Das geht auch — mithilfe sogenannter „erweiterter Funktionen“. Deren Syntax ist wie folgt:

```
function write-Value{
[CmdletBinding()]
 Param([Parameter(Mandatory=$true)] [Int] $a)
 for($i=2; $i*$i -le $a; $i++)
	{
		if($a % $i -eq 0)
		{
			return True
		}
	}
	return False
}
```

Hier gibt es anstatt einer Variablen ein `Param`-Statement. In diesem kann man Parameter deklarieren, auch in ganz normalen Skripten (probiert es einmal bei einem eurer alten Skripte aus — es macht das Testen viel einfacher). `[CmdletBinding()]` ist notwendig: Damit sagt man der Shell, dass sie die einfach so (ohne Klammern) hintereinander geschriebenen Wörter als Argumente behandeln soll. 

> Schreibe deine Funktion als erweiterte Funktion um.
## Begin, Process, End
Es gibt als Alternative zu Funktionen auch einen sehr schönen, schnellen Mechanismus, um mit Listeneingaben zu arbeiten. Dies nennt man `begin`, `process` und `end`. Ich gebe euch ein Beispiel für eine Funktion, die einen String einliest und danach die Anzahl der Elemente in einer Liste ausgibt, die diesen String enthalten.
  
```
param([String] $a)
begin{
	$a = Read-Host -Prompt 'Bitte geben Sie ein Zeichen ein.'
	$count = @()
}
process{
	$numbers += $_.Contains($a).ToInt()
}
end{
	echo "Der Mittelwert ist:"
	echo $numbers
}
```
Aufrufen können wir dieses Skript mit `echo @(„wort1“,“wort2“,“wort3“) | ./script.ps1`, wobei `script.ps1` der Name des Skripts ist.

Schauen wir uns an, was das tut. In `begin` fragen wir den User nach einem Zeichen. Dieser wird immer vor den anderen beiden Blöcken *einmal* ausgeführt. In `process` gibt es eine Variable `$_`. Der `process`-block wird für jedes Element in der Eingabe — in diesem Fall die Liste `@(„wort1“,“wort2“,“wort3“)` — einmal ausgeführt. Der `end`-Block wird einmal ausgeführt.

> Schreibe deine bisherige (erweiterte) Funktion in eine `begin`-`process`-`end`-Struktur um. 


### Unterausdruck auswerten/formatierte Ausgabe
Wir wollen am Schluss noch einen Ausdruck auswerten. Dies geht mit `a ist $($a + 4), und das ist gut so`. Hier wird der Wert von `$a` um vier erhöht (`($a+4)` nennt man auch *Unterausdruck*) und dann als Teil des Strings ausgegeben.

> Nutze die Auswertung von Unterausdrücken, um das Ergebnis deiner Aufgabe ausgeben zu lassen.

+++

## Kleine Programmieraufgaben
Wir haben bisher gesehen: Variablen, Kontrollstrukturen, Funktionen und erweiterte Funktionen. Heute wollen wir ein wenig üben. Nutze den Benutzernamen auf deinem Zettel (behalte ihn, es gibt keine Passwort-Vergessen-Funktion, und wir werden den Account noch benutzen!), um dich bei projecteuler.net anzumelden. Das Ziel für **jeden** von euch ist, heute die Aufgaben 1, 3 und 4 zu lösen. Wer gut zurecht kommt, kann Aufgaben 2 angehen. Arbeite mit einem Partner zusammen. Ich sage nach jeweils 15 Minuten, dass ihr wechseln sollt. Ich gebe euch jeweils eine Präzisierung der Aufgabe und Teilaufgaben, die euch bei der Lösung unterstützen.

Warum machen wir das? Warum langweilige Zahlen, die niemand braucht? Zahlen haben den Vorteil, dass Aufgaben sehr klar formuliert werden und ihr hier alle Programmierkonstrukte benötigt, die ihr bisher gelernt habt. Und: Eine Liste von Files verhält sich beim Iterieren auch nicht anders als eine Liste von Zahlen. 
### Aufgabe 1
Schreibe eine **erweiterte Funktion**, die als Eingabe eine Zahl $n$ nimmt und die Summe aller Vielfachen von 3 und 5 kleiner als diese Zahl ausgibt. 

Tipps:
1. Schreibe eine Funktion `isMultiple`, die dir für eine Zahl ausgibt, ob sie ein Vielfaches von drei oder 5 ist (Eingabe: `Int`, Ausgabe `Bool`)
2. Schreibe eine Funktion `listMultiples`, die dir für eine Zahl die Liste aller Vielfachen von 3 oder 5 ausgibt.
3. Nutze eine `foreach`-Schleife und eine Variable `sum`, um die Summe aller Listenelemente zu berechnen.

## Aufgabe 3
Schreibe eine **Funktion**, die für eine Zahl $n$ den größten Teiler ausgibt.

Tipps:
1. Schreibe eine Funktion `divideOut`, der ihr zwei Zahlen $t$ (für *Teiler*) und $n$ gebt. Wenn $n$ durch $t$ teilbar ist, so gebt $\frac{n}{t}$, `True` zurück, sonst $t$, `False`. 
2. Nutze eine Schleife für $i$ von $2$ bis $n$ und wende immer wieder `divideOut(n, i)` an. Hierbei nutzt ihr für $n$ immer wieder die Ausgabe von `divideOut`. speichert in einer variable immer, wenn `divideOut` `True` zurück gibt.
3. Warum funktioniert das Verfahren aus 2?

### Aufgabe 4
Schreibe ein **Skript** welches das größte Palindrom ausgibt, welches von zweistelligen Zahlen gebildet wird.

Tipps: 
1. Schreibe eine Funktion `isPalindrome(n)`, die `True` genau dann zurück gibt, wenn $n$ ein Palindrom ist. 
2. Schreibe ein Skript, welches mit zwei For-Schleifen alle Paare durchläuft, jeweils die Zahlen multipliziert und testet, ob ein Palindrom vorliegt speichert immer das aktuell größte Palindrom in einer Variablen und gebt es aus. 
3. Könnt ihr 2 auch mit einer Schleife, die maximal $\frac{n^2}{2}$ Multiplikationen braucht, schaffen? Versucht es!

### Aufgabe 2
Schreibe eine **erweiterte Funktion**, die die Summe aller Fibonacci-Zahlen kleiner gleich $n$ ausgibt.

Tipps: 
1. Schreibe eine Funktion `sumLast`, die eine Liste `$a` bekommt und ein Element anhängt, was die summe der letzten beiden Einträge von `$a` summiert.
2. Nutze eine While-Schleife, und wende auf die Liste `1, 2` wiederholt `sumLast` an, um eine Liste aller Fibonacci-Zahlen kleiner $n$ zu bekommen.
3. Nutze wie in Aufgabe 1 eine `foreach`-Schleife, um die Summe aller dieser Zahlen zu bekommen. 

Wir haben heute einfache Programmieraufgaben gelöst. Nutze für dich auch gerne projecteuler.net weiter. Die Aufgaben werden allerdings schnell relativ schwer.

Um einen Eindruck davon zu bekommen, wie ihr in der Abschlussprüfung Code aufschreiben könnt, lest euch bitte aus dem Wikipedia-Artikel zu [Pseudocode](https://de.wikipedia.org/wiki/Pseudocode) die Abschnitte zu „Verwendung“ und „Aussehen und Stilrichtungen“ durch.

+++ 

# Pseudocode, Drills
Heute beschäftigen wir uns mit Pseudocode, einer Möglichkeit, wie man Algorithmen aufschreiben kann, und lösen in kleineren Schritten die Aufgaben von letzter Woche.

Ziele: 
 - Ihr könnt zwei Stile von Pseudocode erkennen und die damit verbundenen Programmiersprachen benennen.
 - Ihr könnt kleine Programmieraufgaben in Pseudocode schreiben.
 - Ihr wendet Kontrollstrukturen in Drills an.

*Pseudocode* ist eine Form, Algorithmen darzustellen. Vier Möglichkeiten, einen solchen darzustellen sind unter https://en.wikipedia.org/wiki/Pseudocode#Syntax zu finden. Eine weitere (und platz- sowie zeitsparendere) Möglichkeit ist die folgende (aus einem Vorlesungsskript, welches ich schön gemacht habe):
![](/Users/AndreasHaupt/Downloads/pseudocode.png)

*Aufgabe*: Schreibe eine Funktion, die die ersten n Fibonacci-Zahlen zurückgibt, in Pseudocode nach dem Stil C. Schreibe ihn um in Pascal-Stil und den Stil von mir. Eine leere Liste erhaltet ihr mit `[]` und an eine Liste `$a` hängt ihr ein Element `b` mit `a.append(b)` an. 

*Drills*, einfache Programmieraufgaben, die häufig wenig eigenen Denkanteil erfordern, helfen ungemein dabei, Sicherheit zu gewinnen. Löse den folgenden Drill aus Bjarne Stroustrups „Programming in C++: Principles and Practice“. Nutze hierfür alte Mitschriften und das Internet. Jede der Aufgaben sollte in unter 5min zu lösen sein. Falls nicht: Rufe mich.

Gehe durch diesen Drill Schritt für Schritt. Versuchen Sie nicht, durch Überspringen von Schritten zu es zu beschleunigen. Teste jeden Schritt, indem du mindestens drei Wertepaare eingeben - mehr Werte sind besser.

1. Schreibe ein Programm, das aus einer while-Schleife besteht, die (bei jedem Schleifendurchlauf) zwei `int`s einliest und dann ausgibt. Das Programm endet, wenn ein abschließendes '|' eingegeben wird.
2. Ändern Sie das Programm, um „Kleinerer Wert:“ gefolgt vom kleineren Wert auszugeben, „Größerer Wert:“ gefolgt von dem größeren Wert.
3. Erweitern Sie das Programm, so dass es „die Zahlen sind gleich“ genau dann schreibt, wenn die Zahlen gleich sind.
4. Ändere das Programm so, dass es `float`s  statt `int`s verwendet.
5. Ändere das Programm so, dass es nach der bisherigen Ausgabe, welches das größere und kleinere ist „die Nummern sind fast gleich“ ausgibt, wenn die beiden Zahlen sich um weniger als ein Hundertstel unterscheiden.
6. Ändere nun den Schleifenkörper so, dass er jedes Mal nur ein `double` anzeigt und abfragt. Definiere zwei Variablen, um zu verfolgen, welcher der bisher kleinste und welcher der bisher größte Wert ist. Nach jedem Schleifendurchlauf drucke den eingegebenen Wert. Wenn er der bisher kleinste ist, schreibe „kleinster Wert bisher“ nach der Zahl. Wenn es das größte bisher ist, schreibe „größter Wert“ hinter die Zahl.
7. Füge eine Einheit zu jedem Double hinzu: Zulässige Eingabewerte sind 10cm, 2,5mm, 5km oder 3,33m ein. Akzeptieren Sie die vier Einheiten: cm, m, km, mm. Die Umrechnungsfaktoren google, falls sie dir nicht bekannt sind. Lies die Buchstaben in einen `String`. Es sollten 12 m (mit einem Abstand zwischen der Zahl und der Einheit) und 12m (ohne Leerzeichen) beides als Eingabewerte möglich sein.
8. Verwerfe Werte ohne Einheiten oder mit "illegalen" Darstellungen von Einheiten wie y, yard, Meter, km und Gallonen, gib also eine Fehlermeldung aus.
9. Verfolge Sie die Summe der eingegebenen Werte (sowie die kleinste und die größte) und die Anzahl der eingegebenen Werte. Wenn die Schleife endet, drucken Sie die kleinste, die größte, die Anzahl der Werte und die Summe der Werte. Beachte, dass, um die Summe zu speichern, du eine Einheit für diese Summe festlegen musst. Benutze Meter.
10. Bewahre alle eingegebenen Werte (in Meter umgewandelt) in einer Liste auf. Drucke diese Werte am Ende aus.
11. Bevor Du die Werte aus dem Vektor druckst, sortiere (damit werden sie in aufsteigender Reihenfolge ausgegeben).

Tipps: 

 - Ausgabe geht mit `echo`
 - Eingabe geht mit `Read-Host` und gegebenenfalls der Option `-Prompt „Dieser Text wird gedruckt`
 - Für sortieren pipe in `Sort-Object` 

*Aufgabe*: Schreibe für die Teilaufgaben zu Aufgabe 1 einen Pseudocode in C-Stil, Pascal-Stil und dem oben gegebenen Stil und implementiere sie. 

Heute haben wir uns mit Pseudocode beschäftigt und noch etwas weiter geübt. Nächste Woche starten wir mit Objektorientierung.  

+++

# Objektorientierung
Wir haben bisher Code unstrukturiert geschrieben. Das heißt, wir definieren Variablen und arbeiten mit ihnen als Datentypen, die vordefiniert sind. Die Powershell ist mächtiger als eine normale Shell, da sie es erlaubt, eigene Datentypen zu definieren.

Allgemein können wir Programme strukturieren mithilfe von

 - Funktionen: Wir betrachten unser Programm als eine Verkettung von kleineren Operationen, die auf Daten arbeiten. Hier ist der *Algorithmus im Zentrum*.
 - Daten: Wir geben unseren Daten *Bedeutung*, indem wir sie zusammenfügen, wenn es Sinn macht und Operationen auf Daten mit den Daten verknüpfen. Unterschiedliche Daten können miteinander kommunizieren, indem sie sich Nachrichten zusenden. Hier ist die *Datenstruktur im Zentrum*.

**Aufgabe 1**: Ist die Powershell nach deiner Erfahrung hier eher funktionen-basiert (man sagt auch *funktional*) oder eher daten-basiert (man sagt auch objektorientiert)? Tipp: Inwiefern hat `|` eine besondere Bedeutung für diese Unterscheidung?

Wir wollen etwas genauer die daten-basierte Brille aufsetzen und dies anhand Daten über Server in einem Unternehmen machen.

*Aufgabe 2* Vervollständige beim Lesen den Glossar am Ende dieser Einheit. Definiere alle gefetteten Begriffe.

Zusammengefasste Daten, die bestimmte Operationen erlauben, heißen **Objekte** in der Sprechweise der sogenannten **objektorientierten Programmierung** (OOP). Die Daten, die zusammengefasst werden, sind genau die, die nötig sind für bestimmte Aufgaben — alle anderen werden weggelassen. Das nennt man **Abstraktion**. Die einzelnen Werte, die zusammengefasst werden, heißen **Attribute** (oder **Felder** in C#). 

In der OOP stehen Objekte im Zentrum des Programmierens. In objektorientierten Programmiersprachen gilt 

> Alles ist ein Objekt.

Das heißt, alles, mit dem gearbeitet wird, wird als eine Zusammenfassung von Daten betrachtet. Das gilt auch für die Powershell. Wenn wir einen `string` eingeben, dann enthält er eine Kodierung der Buchstaben aus denen er besteht und erlaubt den Zugriff auf das $i$-te Zeichen sowie das Verketten von Strings — unter anderem. Solche Operationen auf Objekten nennt man **Methoden**. Daten, die zu einem Objekt gehören, nennt man **Attribute**.

Wir haben auch **Datentypen** kennengelernt. Datentypen sind wie Baupläne von Objekten: Sie erlauben bestimmte Operationen (die Methoden des Datentyps) und speichern die Daten auf dieselbe Weise ab (denkt z.B. an IEEE-754-Floats). OOP kennt einen eigenen Begriff für Datentyp: **Klasse**. Eine Variable von einem bestimmten Datentyp nennt OOP eine **Instanz** des Datentyps/der Klasse.

**Aufgabe 3**: Entscheide jeweils, ob Objekt oder Instanz: Herr Homms Auto, Opel Corsa, iPad, Float, 2, e-15

Schauen wir uns das beispielhaft in Powershell an. Zuerst welche Daten wollen wir nehmen, wenn wir Computer in einem Netzwerk verwalten wollen:

*Aufgabe 3* Mache eine Liste mit Daten, die sinnvoll von Rechnern in einem Netzwerk gespeichert werden sollten und jeweils, welchen Datentyp sie haben sollen. Müssen die Variablen sogar nach einem bestimmten Muster aufgebaut sein (wo steht das @ in einer Mailadresse?[^Wie wir solche Strukturen machen, werden wir in einer weiteren Stunde betrachten). 

Ich nehme einen Namen, eine Marke, einen Zuletzt-Online-Zeitstempel und eine Seriennummer. Dann sieht die Klasse so aus. 

```ps1
class Computer
{
	 # Properties
	 [string]$Name
	 [string]$Marke
	 [DateTime]$zuletztonline
	 [Int]$Seriennummer
}
```
**Keywords** sind in Programmiersprachen Abfolgen, die keine Variablennamen und keine Datentypen-Namen sein dürfen. Ein Beispiel hierfür ist **`class`**. Dieses zeigt an, dass das nächste Wort der Name einer neuen Klasse ist, deren Daten und Methoden im nachfolgenden Block definiert werden. Du kannst ein neues Element vom Datentyp kreieren, indem du schreibst

```
> $meinComputer = [Computer]::new()
```

und die einzelnen Variablen setzen, indem du schreibst (die Powershell schaut nicht auf Groß- und Kleinschreibung)

```
$meinComputer.name="Herr Haupts Computer"
$meinComputer.marke="Apple"
$meinComputer.seriennummer = 123
```

*Aufgabe 4* Schreibe deine eigene Klasse und teste sie aus, indem du bestimmte Werte setzt. Erhältst du eine Fehlermeldung, wenn du versuchst, einen Sting in die Seriennummer zu speichern? Welche Werte akzeptiert `$zuletztonline` überhaupt?

Nun zu Methoden: Die ergänzte Klasse sieht so aus.

```ps1
class Server
{
 # Properties
 [string]$Computername
 [vendor]$Vendor
 [string]$Model
 [dateTime]$LastEchoReply
 # Methods
 [string]GetBasicInfo()
 {
	 if ($this.LastEchoReply -eq 0)
	 {
		 return "$($this.Computername) (Last seen: never)"
	 }
	 else
	 {
		 return "$($this.Computername) (Last seen: $($this.LastEchoReply))"
	 }
 }
 [void]RunPingTest()
 {
	 $this.LastEchoReply = $(
	 if (Test-Connection –ComputerName $this.computername
	 -Count 1 -Quiet) {Get-Date}
	 else { Get-Date -Date 0 })
 }
}
```

*Aufgabe 5* Schreibe zwei Methoden für deine Klasse.

Es ist eine Frage, wie man neue Objekte erzeugt. Bei `int` oder anderen vorher eingebauten Datentypen war es `[int]$a=1`. Bei Objekten eines komplexeren Datentyps ist das Problem: Es reicht nicht, nur einen Wert anzugeben. Daher geben wir eine Funktion an, die alle notwendigen Attributwerte nimmt und setzt. Eine solche Funktion heißt **Konstruktor**.

```ps1
class Server
{
 # Properties
 [string]$Computername
 [vendor]$Vendor
 [string]$Model
 [dateTime]$LastEchoReply
 # Methods
 [string]GetBasicInfo()
 {
	 if ($this.LastEchoReply -eq 0)
	 {
		 return "$($this.Computername) (Last seen: never)"
	 }
	 else
	 {
		 return "$($this.Computername) (Last seen: $($this.LastEchoReply))"
	 }
 }
 [void]RunPingTest()
 {
	 $this.LastEchoReply = $(
	 if (Test-Connection –ComputerName $this.computername
	 -Count 1 -Quiet) {Get-Date}
	 else { Get-Date -Date 0 })
 }
 # Constructor
 Server($computername)
 {
	 $this.Computername = $Computername
	 $this.RunPingTest()
 }
}
```

*Aufgabe 6* Schreibe einen Konstruktor für deine Klasse und teste sie.

Schließlich kann es noch passieren, dass wir Attribute speichern wollen, die alle Objekte einer Klasse treffen. Ein Beispiel eines Attributs wäre die Anzahl aller Objekte von diesem Typ. Ein Beispiel für solche Methoden sind die Methoden des Datentyps `math` (von der ihr die Funktion `[math]::abs()` in den Drills kennengelernt habt). Diese Methoden und Attribute heißen **statisch**, da sie nicht davon abhängen, von welchem Objekt aus sie ausgeführt werden. Diese erstellen wir wie folgt:

```
class Server
{
	# Properties
	[string]static $username
	…
	# Methods
	[string]static GetNewuserName([string]$name)
	{
		…
	}
	…
}
```

Bestimmte Dinge gibt es hier nicht — diese schauen wir uns an, wenn wir sehen, wie das .NET-Framework in Powershell genutzt werden kann:
 - Das Geheimnisprinzip/die Datenkapselung[^Das besagt, dass auf die Daten von außen nicht direkt zugegriffen werden kann, sondern nur mittels Funktionen, die diese auslesen oder setzen, sogenannte Setter- und Getter-Methoden.]
 - Sichtbarkeit[^`private`-Methoden und `public`-Methoden]
 - Beziehungen zwischen Objekten[^Nutze ich andere Objekte in einem Objekt, zum Beispiel `Computer`, die in einem Datentyp `Netzwerk` zusammengefasst sind]
 - Vererbung[^Datentypen, die „spezieller“ sind als andere. Funktionen, die mit unterschiedlich speziellen Datentypen funktionieren heißen „polymorph“.]
 - Ereignisse[^Sobald bestimmte Dinge eintreten — z.B. ein Klick auf einen Button in einer GUI — passiert etwas.]

| Begriff | Definition |
|:--|:--|
| Objekte | |
| OOP | |
| Abstraktion | |
| Attribute | |
| Methoden | |
| Attribute | |
| Datentypen/Klasse | |
| Instanz | |
| Keywords | |
| **`class`** | |
| Konstruktor | |


## Fehlerbehandlung
Wenn in einer Arbeit ein Fehler passiert, schreibt man Tickets, diese Tickets werden von bestimmten Personen abgefangen und bearbeitet. Das ist relativ ordentlich. Ohne Tickets hingegen weniger: Wenn ich ein System habe, wo ich nur bei der Abgabe meiner Aufgabe einen Fehler reporten kann, dann wird es chaotisch und langsam. Nehmen wir noch ein konkreteres Beispiel: Ich möchte gerne auf eine Datenbank zugreifen, um eine bestimmte Sache auszulesen. Wenn die Datenbank nicht existiert, möchte ich gerne in diesem Moment, dass die Person, die die Datenbank nicht angelegt hat, eine böse Mail kriegt.

Dieses langsame System im Programmieren korrespondiert zu „Fehler-Codes“. Das sind Zahlen, die eine Funktion zurück gibt. Meistens heißt $0$, dass alles gut gegangen ist und ein Wert ungleich $0$, dass etwas schief gegangen ist. Der genaue Wert bestimmt, welcher Fehler. Das ist auch der Grund, warum in vielen Programmiersprachen die Main-Funktion immer eine `int` zurück gibt: Das ist der Fehler-Code.

Eine bessere Variante wären Tickets. In einem bestimmten Bereich des Unternehmens können Tickets geschrieben werden, die an anderer Stelle abgearbeitet werden. In Code sind die Bereiche, die Tickets an dieselbe Stelle schicken, in einem `Try`-Block eingebunden, ein direkt danach folgender `Catch`-Block definiert, wie die „Tickets“ (in Programmiersprachen heißen diese **Exceptions**) zu behandeln sind.

Aufgabe 1: Lies den [Artikel](https://www.vexasoft.com/blogs/powershell/7255220-powershell-tutorial-try-catch-finally-and-error-handling-in-powershell) und beantworte dabei die folgenden Fragen:

 1. Warum ist es blöd, wenn der Fehler, dass die Datenbank nicht da ist, keine Sonderbehandlung erfährt? Was würde passieren?
 2. Was ist ein non-terminating error?
 3. Mit welcher Code-Zeile kann ich non-terminating errors wie terminating errors behandeln?
 4. In welcher Variable liegt der Text des Fehlers?
 5. Finde im Internet eine Liste mit Exceptions, die die Powershell kennt.
 6. Wofür ist der Log-Eintrag am Ende von „Finally“ wichtig?

Als kleine Anfügung: Wenn ihr die Ausgabe von einem Befehl `befehl` auf die Konsole in eine Datei `out.txt` umleiten wollt, so könnt ihr schreiben `befehl >> out.txt`, falls ihr den Text an die Datei anhängen wollt — gut für Logs — oder `Befehl > out.txt`, falls ihr die Datei überschreiben wollt. Es gibt mehr Funktionalität (teilweise ist es wichtig, nur bestimmte Informationen zu haben), die ihr in den Microsoft [Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_redirection?view=powershell-6) nachlesen könnt.

Aufgabe 2: Erweitert die Klasse vom letzten Mal um eine Fehlerbehandlung. Falls ihr bisher keine Methode habt, die Text in eine Datei schreibt, so fügt diese hinzu (diese könnte später z.B. die installierte Software halten). Nutzt entsprechende Try-Catch-Blöcke für Fehler, die auftreten können und deren Nichtbehandlung schädlich für das System sein könnte.

Die Analogie mit Tickets krankt bisher darin, dass ihr in eurem Code bisher noch keine eigenen Tickets „schreiben“ könnt — das müssen die vorimplementierten Operationen machen. Die Funktionalität, Tickets zu schreiben ist `Throw`, und wird in anderen Programmiersprachen häufig genutzt. Das schauen wir uns aber hier nicht an.

## Formatierte Ausgabe

Für Administration von Computersystemen ist es wichtig, Dinge übersichtlich auszugeben. Die Powershell gibt hier viel Kontrolle. 

Aufgabe 1 Lies den [Artikel](https://docs.microsoft.com/de-de/powershell/scripting/getting-started/cookbooks/using-format-commands-to-change-output-view?view=powershell-6) und beantworte die folgenden Fragen:

 1. Beschreibe in je einem Satz, wie die Attribute eines Objekts bei `Format-Wide`, `Format-Table` und `Format-List` ausgegeben werden. 
 2. Warum kann ich bei `Format-Wide` nur eine Property angeben, bei den anderen beiden jedoch eine Liste von Attributen?
 3. Mache eine Liste mit allen Parametern (diese beginnen mit einem Minus) im Code des Artikels vorkommen. Erläutere die Bedeutung in jeweils einem Satz.

Ich gebe noch ein Beispiel für Gruppierung: Wenn ich ein System baue, in dem ich Rechner verwalte, macht es sehr Sinn, die Linux-Rechner in einer anderen Tabelle als die Windows-Rechner anzuzeigen. Dennoch möchte ich sie gerne jeweils als `Computer`-Objekt speichern. Dann kann ich `-GroupBy OperatingSystem` nutzen.

Aufgabe 2 Erweitere deine Klasse um eine Ausgabefunktionalität: Die Methode `print` soll eine Gruppierte `Format-Table`-Ausgabe machen.

## Erweiterung der Powershell

Lest den folgenden Text zusammen (10min)

Heute soll es um Erweiterungen gehen. Dass wir gerne Funktionen aus einem bestimmten Bereich nutzen wollen, haben wir schon in Linux (Paket-Installation) und Kryptographie (Namespaces) gesehen. Zwei Gründe sprechen dafür, dass man immer etwas tun muss, um bestimmte Befehle nutzen zu können. 

 1. Alle Funktionen immer im kompilierten Code mit einzubauen bedeutet, dass der Code riesig und die Kompilierunug langsam ist und
 2. vielleicht noch wichtiger: Es gäbe Namenskonflikte: eine Funktion namens „Print“ gibt es vermutlich in vielen Programmen. 

Daher installieren wir unterschiedliche Arten von weiterem Code. Das Ziel der heutigen Stunde ist, dass ihr euch drei historisch entwickelte Formen, weiteren Code einzubinden, zu zweit anschaut, und dann jeweils in eine Dreiergruppe geht, um gemeinsam ein paar Fragen zu beantworten.

Aufgabe 1 (25min) Teilt euch möglichst gleichmäßig in drei Gruppen auf. Gruppe 1 liest 

Wir können Module, Snapins, Assemblys installieren und neue Module mithilfe von Find-Module finden.



Als Abschluss folgt eine Remote-Wartung als Projekt.
