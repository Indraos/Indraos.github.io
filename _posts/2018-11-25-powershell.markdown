---
layout: post
title:  Powershell-Grundlagen
date:   2018-11-25 08:00:00 +0100
categories: teach
---
Die Power Shell wurde 2006 als Update für Windows Clients eingeführt und ist mittlerweile wichtiges Werkzeug für Administrator\*innen. Wir werden uns die Power Shell in 5 Bereichen ansehen

<!--more-->

 1. Grundlegende Software: Wir passen die Power Shell und das Integrated Scripting Environment an. Wir nutzen grundlegende Shortcuts für die Power Shell. Wir lernen, was Execution Policys für die Ausführung von Scripts bedeutet. 
 2. Syntax: Wir lernen, wie wir Variablen definieren, wie wir Alias definieren, die Syntax von Kontrollstrukturen, Klammerausdrücke (`()`, `$()`, `@()`, `@{}`), Strukturierung von Skripten (begin, process, end), die Syntax erweiterter Funktionen, Operatoren, wir können Pipeline-Ausgaben formatieren.
 3. Objektorientierung: Wir können begründen, was die Vorteile der Power Shell gegenüber einer normalen Shell ist. Wir können Objekt, Klasse, Methode, Statik, Konstruktor und Attribut definieren.
 4. Erweiterungen: Wir können Module selbst erstellen und einbinden.
 5. Remote-Wartung: Wir nutzen das bisher gelernte, um eine Fernwartung über das Netzwerk zu machen. 

## Grundlegende Software
Öffne die Power Shell mit `[windows] + r`, `[enter]` und dann `powershell`. Öffnet weiterhin das Power Shell Integrated Scripting Environment mir `[windows] + r`, `[enter]` und dann `powershell ise`. Um in die Einstellungen der Power Shell zu gelangen, klickt links oben am Fenster auf das Icon und drücke auf „Eigenschaften“. Die Einstellungen bei der ISE sind ein Menüpunkt.

> Beantworte die folgenden Fragen schriftlich: 1. Wie passe ich die Schriftart in der Power Shell an? Wie geht das in der ISE? 2. Funktioniert Copy-Paste in der Power Shell? 3. Wie erstelle ich ein neues Skript in der ISE? 4. Was brauche ich, um eine Remote-Registerkarte zu öffnen? In welcher Rolle könntet ihr eine solche Registerkarte brauchen?

Sollte es im folgenden einmal ein Problem in der Power Shell geben, dann könnt ihr den derzeit aktiven Prozess mit `[ctrl]` + `c` abbrechen.

> Erstellt ein Skript mit dem Inhalt `echo "Hallo Welt"` und speichert sie an einem beliebigen Ort unter dem Namen `hello_world.ps1`. `cd`t (also wechselt den aktuellen Ordner) zum Speicherort der Datei in der Konsole unten in der ISE und tippt `hel`. Ein Druck auf die Tabulator-Taste sollte `.\hello_world.ps1` hervorzaubern. Ein Enter gibt euch „Hallo Welt“ aus. Euer erstes Skript!
  
Es verbleibt, sich mit Execution Policies auseinander zu setzen. Programme, die wir auf der Power Shell ausführen können, enden mit `.ps1`. Diese können potenziell mächtig und damit auch potenziell schädlich sein. Es ist also im Interesse des Administrators, Kontrolle darüber zu haben, was der Computer ohne zu fragen ausführen soll.

> Tippt `Get-ExecutionPolicy` ein. 

Ihr solltet alle `Unrestricted` sehen. „Unrestricted“ bedeutet, dass alle Skripte ausgeführt werden, die die Person an der Power Shell ausführen möchte (dies ändert nichts daran, dass für Änderungen an bestimmten Ordnern Admin-Rechte benötigt werden). Eine andere, `RemoteSigned` fordert, dass Chips, die z.B. aus dem Internet herunter geladen wurden, oder allgemeiner von einem fremden Rechner stammen, digital signiert (also im Sinne von Kryptographie!) sein müssen, um ausgeführt zu werden.


## Syntax
Die Power Shell hat einen Funktionsumfang wie die „normale“ Konsole — und noch einiges mehr. Mit dem Teil, den ihr bereits ähnlich aus der normalen Konsole kennt, wollen wir heute beginnen.

### Variablem
Ihr könnt Variablen mit `$myvariable = 4` definieren. Variablennamen sollten alphanumerisch (also Zahl oder Buchstabe, aber keine Umlaute) sein und werden durch ein Dollarzeichen eingeleitet. In der "normalen" Konsole wurde dies mit `set` gemacht. Unsere Shell hat einen Großteil ihrer „Powers“ dadurch, dass sie Variablentypen ermöglicht. Diese Variablen können dann nicht mit irgendetwas „beschrieben“, sondern nur mit Daten, die von einer speziellen Form sind. Zum Beispiel wäre eine solche Form Text, also Abfolge von Zeichen (Datentyp String). Wenn wir Dezimalzahlen annehmen, können wir jede Zahl als TExt interpretieren, andersherum aber nicht. Das könnt ihr auch selbst sehen.

> Gib `[Int32]$a = 4` und dann `$a = „Hi“`. Beschreibt kurz auf deutsch den Inhalt der Fehlermeldung.

Wenn ihr Variablen ausgeben wollt, so tippt `$a` ein. Wenn ihr den Typen einer Variable wissen wollt, so tippt `$a.GetType()` ein. 

> Lasst euch den Typ von `$a` ausgeben.

Es gibt einige besondere Variablen, die immer definiert sind. Auf diese werden wir später zurückkommen.

| Variable | Beschreibung |
|:--|:--|
| `$args` | Dies ist eine Liste mit allen Eingaben von Funktionen (die schauen wir uns später an). |
| `$_` | Dies ist die letzte Eingabe der Konsole. |
| `$input` | Dies ist eine Liste mit allen Eingaben via einer Pipeline. |
| `$error` | Dieser enthält alle Fehlermeldungen (die wir uns auch später ansehen). |

> `$error` könnt ihr aber jetzt schon kennenlernen: Gebt ein `@(0/0)` (das ist die Rechnung Null geteilt durch Null) und danach `$error`.

### Operatoren
Es gibt in der Power Shell viele Operatoren. Da hauptsächlich die für Zahlen und logische für uns erst einmal wichtig sein werden, ist es sinnvoll eine Liste bei sich zu haben. Aktives auswendig lernen ist nicht sinnvoll, zumal aus dem Englischen sich viele ableiten lassen (ge = greater equal, lt = lower than, etc.).

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

Die Lösung der Aufgabe ist: 


``` powershell
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

### Funktionen
Heute wollen wir dieses Skript etwas erweitern.

> Wir wollen eine Funktion schreiben, die aus einer Liste von Zahlen alle mit mehr als fünf Teilern ausgibt. Sie soll für jede Zahl $b$ den Satz „Die Zahl $b$ hat mehr als fünf Teiler.“ ausgeben. 

Ein Teiler von einer Zahl $k$ ist eine Zahl $n$, so dass es eine Zahl $m$ gibt mit $k = m \cdot n$. Genug Mathe: Zum Beispiel sind die Teiler von $56$ die Zahlen $2$, $2$, $2$, $7$, da $56 = 2\cdot 2 \cdot 2 \cdot 7$. 

Um diese Aufgabe zu lösen, brauchen wir mehr von der Sprache PowerShell. Fragen, die wir auf jeden Fall beantworten müssen, sind:

 - Wie funktionieren Funktionen in der Powershell?
 - Wie arbeite ich mit Listen?
 - Wie kriege ich die Länge von Listen?
 - Wie mache ich eine Ausgabe?

#### Listen
Eine Liste ist eine sortierte, nicht indizierte Datenstruktur von Elementen. "Index" ist wie eine Zeilennummer in einer Tabelle (nur in allgemeineren Anwendungen). Dies wird oft unterschieden vom Array, wo man auf Elemente per Index zugreifen kann. Die Powershell macht diese Unterscheidung *nicht*, man kann auch auf Listen per Index zugreifen. Die Lang-Syntax um eine Liste von Integren zu erstellen wäre
```
[Int[]]$a = 1,2,3
```
Hierbei bedeuten die äußeren eckigen Klammern, dass innendrin der Typ der Variable steht, `Int`, dass es ein Integer sein soll und `[]`, dass es eine Liste von Integern sein soll. Die Kommata trennen Listenelemente voneinander.

Es würde einen Fehler geben, wenn wir hier einen String schreiben wollen, wie der Test `$a[1] = "Hello World"` zeigt. Wenn uns der Datentyp nicht sehr kümmert, so können wir auch
```
$b = 1, 2, 3
```
schreiben.

> Vergleiche `$a.GetType()` und `$b.GetType()`. In welcher Anwendung ist es sinnvoll, `$a` zu benutzen (bzw. seinen Datentyp) und wann, `$b`?

Um ein Element zu einer Liste hinzuzufügen, schreibt
```
$a += "neueselement"
```
> Was ist der Unterschied zwischen `$a = 1`, `$a += 1` und `[Int[]]$a = 1`, `$a += 1`?

> Finde heraus (mithilfe des Internets), wie du eine Liste von 3 Listen mit jeweils den Elementen $1, 2, 3$ anlegst. Es sollte also z.B. `$a[1][1] = 1`, `$a[1][2] = 2` und `$a[1][3] = 3` sein.

Um dir die Länge von einer Liste `$a` ausgeben zu lassen, tippe `$a.Length()`. Wenn man dafür sorgen möchte, dass ein String als Liste gelesen wird (also die Kommata nicht als Satzzeichen), so kann man den Text mit `@(...)` umschließen, z.B. statt `1,2,3` `@(1,2,3)`. Meistens rät die Powershell aber so, wie man es sich gedacht hat (also ob Kommata gerade Trenner in einer Liste sind oder nicht).
#### Hashtables
Manchmal (jedoch nicht für unsere Aufgabe oben) ist es interessant, eine Liste, deren Einträge mit z.B. Strings indiziert sind, zu definieren. Ein Beispiel wäre eine Liste, in der Städtenamen Einwohneranzahlen zugeordnet sind. Die Syntax hierfür ist
```
 HashTable$a = @{"Frankfurt" = 700000; "Stuttgart" = 1000000}
```
Der Typ ist also `HashTable` und der Unterschied der rechten Seite zu einer Liste ist, dass eine geschweifte statt einer runden Klammer die Definition umschließt.

> Lege eine Hashtable an, die Die Namen eurer Klasse als Keys und deren Alter als Values hat. 
> Probiert einmal `$a.GetType()` aus. Was ist der Typ einer Hashtable?

Sowohl Keys als auch Values können beliebige Typen sein (mehr über Typen gibt es nachte Woche).

Wir wollen uns nun aber wieder unseres Problems annehmen: Hierfür benötigen wir Funktionen.
### Funktionen
Ich packe die obige Lösung in eine Funktion. Dies sollte die Syntax überwiegend klären („GetDivisors“ heißt „finde die Teiler“)

```
function GetDivisors([Int] $a)
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
`function` ist ein sogenanntes **Keyword**, darf also nicht in anderen Kontexten verwendet werden. Mit der For-Schleife habt ihr euch bereits beschäftigt.

> Kommentiere den obigen Code zeilenweise.
> Durchlauft das Programm händisch (schreibt auf, welche Rechnungen der Computer macht) für `$a$ = 5`.
> Schreibe eine Funktion für die Aufgabe von Beginn dieser Sektion. Dabei hilft dir, die Funktion `GetDivisors` zu nutzen, in einer weiteren Variablen die Anzahl der Teiler zu zählen und eine `foreach`-Schleife zu nutzen.

Die Funktion `GetDivisors` kann ich in der Shell dann als `GetDivisors(5)` oder `GetDivisors 5` aufrufen. Wenn ich aber gerne meine Funktion automatisch auf eine Liste von Elementen anwenden möchte (indem ich die Funktion auf jedes Element einzeln anwende und das zurückgebe; wir lernen die sogenannte **Pipe** `|` später noch kennen), oder Langausgaben und Fehlerausgaben haben möchte, dann kriege ich das durch sogenannte CMD-lets/erweiterte Funktionen. Weiterhin haben Powershell-Funktionen oft sehr viele Mögliche Eingaben. Der folgende Code ist ein einfaches Beispiel für ein CMD-let (die Zeile `[CmdletBinding()]` macht das), welches die Eingaben anders und vielleicht übersichtlicher definiert. Mehr dazu weiter unten.

```
function Write-Value 
{
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
Hier gibt es anstatt einer Variablen ein `Param`-Statement. In diesem kann man Parameter deklarieren, auch in ganz normalen Skripten (probiert es einmal bei einem eurer alten Skripte aus — es macht das Testen viel einfacher).
#### Begin, Process, End
Wenn die Eingabe einer Liste etwas komplizierter bearbeitet werden soll als eine Funktion einzeln auf jedes Element anzuwenden, so wird dies durch die Powershell auch ermöglicht. Die Blöcke `begin` (was soll passieren, bevor wir die Liste durchgehen), `process` (was wird mit jedem Element gemacht) und `end` (was wird gemacht, nachdem durch die Liste durchgegangen wurde) ermöglichen komplexere Verarbeitung. Ich gebe euch ein Beispiel für eine Funktion, die einen String einliest und danach die Anzahl der Elemente in einer Liste ausgibt, die diesen String enthalten.
``` ps
function Hash
{
	param([Int] $a)
	begin
	{
		for($i = 0; $i -lt 5; ++$i)
		{
			if($a % 2 -eq 0)
			{
				$a = $a/2
			} else {
				$a = 3*$a + 1
			}
		} 
	}
	process
	{
		return $a * $_
	}
	end
	{
		echo "The hash number was $a."
	}
}
```

Schauen wir uns an, was das tut. In `begin` machen wir eine Iteration,  um auf einen Werz zu kommen, der nicht so viel mehr mit dem Eingabewert zu tun hat (wir können uns das als sehr einfache Art einer Zufallszahl vorstellen). Dieser wird immer vor den anderen beiden Blöcken *einmal* ausgeführt. In `process` gibt es eine Variable `$_`, die mit `$a` multipliziert wird, was wir als eine sehr einfache Variante des Hashings verstehen können. Der `process`-block wird für jedes Element in der Eingabe — einmal ausgeführt. Der `end`-Block wird einmal ausgeführt. Ein Beispiel für eine Ausführung wäre 
```
> @(1,2,3,4,5) | Hash 4
2, 4, 6, 8, 10
```

> Schreibe deine bisherige Funktion in eine `begin`-`process`-`end`-Struktur um. 

### Unterausdruck auswerten/formatierte Ausgabe
Wir wollen am Schluss noch einen Ausdruck auswerten. Dies geht mit `a ist $($a + 4), und das ist gut so`. Hier wird der Wert von `$a` um vier erhöht (`($a+4)` nennt man auch *Unterausdruck*) und dann als Teil des Strings ausgegeben.

> Nutze die Auswertung von Unterausdrücken, um das Ergebnis deiner Aufgabe ausgeben zu lassen.

## Pseudocode, Drills
*Pseudocode* ist eine Form, Algorithmen darzustellen. Vier Möglichkeiten, einen solchen darzustellen sind unter https://en.wikipedia.org/wiki/Pseudocode#Syntax zu finden. Eine weitere (und platz- sowie zeitsparendere) Möglichkeit ist die folgende (aus einem Vorlesungsskript, welches ich schön gemacht habe):
![](/Users/AndreasHaupt/Downloads/pseudocode.png)

*Aufgabe*: Schreibe eine Funktion, die die ersten $n$ Fibonacci-Zahlen zurückgibt, in Pseudocode nach dem Stil C. Schreibe ihn um in Pascal-Stil und den Stil von mir. Eine leere Liste erhaltet ihr mit `[]` und an eine Liste `$a` hängt ihr ein Element `b` mit `a.append(b)` an. 

*Drills*, einfache Programmieraufgaben, die häufig wenig eigenen Denkanteil erfordern, helfen ungemein dabei, Sicherheit zu gewinnen. Löse den folgenden Drill aus Bjarne Stroustrups „Programming in C++: Principles and Practice“. Nutze hierfür alte Mitschriften und das Internet. Jede der Aufgaben sollte in unter 10min zu lösen sein. Falls nicht: Rufe mich.

Gehe durch diesen Drill Schritt für Schritt. Versuchen Sie nicht, durch Überspringen von Schritten zu es zu beschleunigen. Teste jeden Schritt, indem du mindestens drei Wertepaare eingeben - mehr Werte sind besser.

1. Schreibe ein Skript, das aus einer while-Schleife besteht, die (bei jedem Schleifendurchlauf) zwei `int`s einliest und dann ausgibt. Das Programm endet, wenn ein abschließendes '|' eingegeben wird.
2. Ändere das Skript, um „Kleinerer Wert:“ gefolgt vom kleineren Wert auszugeben, „Größerer Wert:“ gefolgt von dem größeren Wert.
3. Erweitere das Skript, so dass es „die Zahlen sind gleich“ genau dann schreibt, wenn die Zahlen gleich sind.
4. Ändere das Programm so, dass es `Float`s  statt `Int`s verwendet.
5. Ändere das Programm so, dass es nach der bisherigen Ausgabe, welches das größere und kleinere ist „die Nummern sind fast gleich“ ausgibt, wenn die beiden Zahlen sich um weniger als ein Hundertstel unterscheiden.
6. Ändere nun den Schleifenkörper so, dass er jedes Mal nur ein `double` anzeigt und abfragt. Definiere zwei Variablen, um zu verfolgen, welcher der bisher kleinste und welcher der bisher größte Wert ist. Nach jedem Schleifendurchlauf drucke den eingegebenen Wert. Wenn er der bisher kleinste ist, schreibe „kleinster Wert bisher“ nach der Zahl. Wenn es das größte bisher ist, schreibe „größter Wert“ hinter die Zahl.
9. Halte in Variablen die Summe der eingegebenen Werte (sowie die kleinste und die größte) und die Anzahl der eingegebenen Werte. Wenn die Schleife endet, drucken Sie die kleinste, die größte, die Anzahl der Werte und die Summe der Werte. Beachte, dass, um die Summe zu speichern, du eine Einheit für diese Summe festlegen musst. Benutze Meter.
10. Bewahre alle eingegebenen Werte (in Meter umgewandelt) in einer Liste auf. Drucke diese Werte am Ende aus.
11. Bevor Du die Werte aus dem Vektor druckst, sortiere (damit werden sie in aufsteigender Reihenfolge ausgegeben).

Tipps: 

 - Ausgabe geht mit `echo`
 - Eingabe geht mit `Read-Host` und gegebenenfalls der Option `-Prompt „Dieser Text wird gedruckt`
 - Für sortieren pipe in `Sort-Object` 

## Kleine Programmieraufgaben
Melde dich bei [projecteuler.net](https://projecteuler.net/) und schreibe dir deine Benutzer\*innen-Daten auf (es gibt keine Passwort-Vergessen-Funktion). Das sind mathematische Rätsel-Aufgaben. Warum machen wir das? Warum langweilige Zahlen, die niemand braucht? Zahlen haben den Vorteil, dass Aufgaben sehr klar formuliert werden und ihr hier alle Programmierkonstrukte benötigt, die ihr bisher gelernt habt. Und: Eine Liste von Files verhält sich beim Iterieren auch nicht anders als eine Liste von Zahlen. 
### Aufgabe 1
Schreibe eine **Funktion**, die als Eingabe eine Zahl $n$ nimmt und die Summe aller Vielfachen von 3 und 5 kleiner als diese Zahl ausgibt. 

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
Schreibe eine **Funktion**, die die Summe aller Fibonacci-Zahlen kleiner gleich $n$ ausgibt.

Tipps: 
1. Schreibe eine Funktion `sumLast`, die eine Liste `$a` bekommt und ein Element anhängt, was die summe der letzten beiden Einträge von `$a` summiert.
2. Nutze eine While-Schleife, und wende auf die Liste `1, 2` wiederholt `sumLast` an, um eine Liste aller Fibonacci-Zahlen kleiner $n$ zu bekommen.
3. Nutze wie in Aufgabe 1 eine `foreach`-Schleife, um die Summe aller dieser Zahlen zu bekommen. 

# Objektorientierung
Wir haben bisher Code unstrukturiert geschrieben. Das heißt, wir definieren Variablen und arbeiten mit ihnen als Datentypen, die vordefiniert sind. Die Powershell ist mächtiger als eine normale Shell, da sie es erlaubt, eigene Datentypen zu definieren.

Allgemein können wir Programme strukturieren mithilfe von

 - Funktionen: Wir betrachten unser Programm als eine Verkettung von kleineren Operationen, die auf Daten arbeiten. Hier ist der *Algorithmus im Zentrum*.
 - Daten: Wir geben unseren Daten *Bedeutung*, indem wir sie zusammenfügen, wenn es Sinn macht und Operationen auf Daten mit den Daten verknüpfen. Unterschiedliche Daten können miteinander kommunizieren, indem sie sich Nachrichten zusenden. Hier ist die *Datenstruktur im Zentrum*.

Die Powershell ist funktional dadurch, dass viele Befehle durch die Pipe `|` hintereinander gestellt werden können. Der Befehl `ls`, der eine Liste von Dateien und Ordnern im aktuellen Verzeichnis ausgibt, kann weiterereicht werden in einen Befehl, der es weiter verarbeitet, z.B. `ls | Format-Table`. Intern ist `Format-Table` nicht viel anders implementiert als wir es mit einem `begin`, `process`, `end` könnten. Wir können aber auch sehen, dass Powershell den datenbasierten Blick auch zulässt.

*Aufgabe 2* Vervollständige beim Lesen den Glossar am Ende dieser Einheit. Definiere alle gefetteten Begriffe.

Zusammengefasste Daten, die bestimmte Operationen erlauben, heißen **Objekte** in der Sprechweise der sogenannten **objektorientierten Programmierung** (OOP). Die Daten, die zusammengefasst werden, sind genau die, die nötig sind für bestimmte Aufgaben — alle anderen werden weggelassen. Das nennt man **Abstraktion**. Die einzelnen Werte, die zusammengefasst werden, heißen **Attribute** (oder **Felder** in C#). 

In der OOP stehen Objekte im Zentrum des Programmierens. In objektorientierten Programmiersprachen gilt 

> Alles ist ein Objekt.

Das heißt, alles, mit dem gearbeitet wird, wird als eine Zusammenfassung von Daten betrachtet. Das gilt auch für die Powershell. Wenn wir einen `String` eingeben, dann enthält er eine Kodierung der Buchstaben aus denen er besteht und erlaubt den Zugriff auf das $i$-te Zeichen sowie das Verketten von Strings — unter anderem. Solche Operationen auf Objekten nennt man **Methoden**. Daten, die zu einem Objekt gehören, nennt man **Attribute**.

Wir haben auch **Datentypen** kennengelernt. Datentypen sind wie Baupläne von Objekten: Sie erlauben bestimmte Operationen (die Methoden des Datentyps) und speichern die Daten auf dieselbe Weise ab (denkt z.B. an IEEE-754-Floats). OOP kennt einen eigenen Begriff für Datentyp: **Klasse**. Eine Variable von einem bestimmten Datentyp nennt OOP eine **Instanz** des Datentyps/der Klasse.

**Aufgabe 3**: Entscheide jeweils, ob Objekt oder Instanz: Auto mit Kennzeichen (X-YZ 234), Opel Corsa, iPad, Float, 2, e-15

Machen wir uns zuerst Gedanken, was für ein Datentyp uns interessiert.

*Aufgabe 3* Mache eine Liste mit Daten, die sinnvoll von Rechnern in einem Netzwerk gespeichert werden sollten und jeweils, welchen Datentyp sie haben sollen.

Ich nehme einen Namen, eine Marke, einen Zuletzt-Online-Zeitstempel und eine Seriennummer. Dann sieht die Klasse so aus. 

```ps1
class Computer
{
	 # Properties
	 [string]$Name
	 [string]$Marke
	 [DateTime]$ZuletztOnline
	 [Int]$Seriennummer
}
```
**Keywords** sind in Programmiersprachen Abfolgen, die keine Variablennamen und keine Datentypen-Namen sein dürfen. Ein Beispiel hierfür ist **`class`**. Dieses zeigt an, dass das nächste Wort der Name einer neuen Klasse ist, deren Daten und Methoden im nachfolgenden Block definiert werden. Du kannst ein neues Element vom Datentyp kreieren, indem du schreibst

```
> $meinComputer = [Computer]::new()
```

und die einzelnen Variablen setzen, indem du schreibst (die Powershell schaut nicht auf Groß- und Kleinschreibung)

```
$meinComputer.Name="Herr Haupts Computer"
$meinComputer.Marke="Apple"
$meinComputer.Seriennummer = 123
```

*Aufgabe 4* Schreibe deine eigene Klasse und teste sie aus, indem du bestimmte Werte setzt. Erhältst du eine Fehlermeldung, wenn du versuchst, einen Sting in die Seriennummer zu speichern? Welche Werte akzeptiert `$zuletztonline` überhaupt?

Nun zu Methoden: Die ergänze Klasse sieht wie folgt aus.

```ps1
class Server
{
 # Properties
 [string]$Name
 [string]$Marke
 [DateTime]$ZuletztOnline
 [Int]$Seriennummer
 # Methods
 [string]GetBasicInfo()
 {
	 if ($this.ZuletztOnline -eq 0)
	 {
		 return "$($this.Name) (Last seen: never)"
	 }
	 else
	 {
		 return "$($this.Name) (Last seen: $($this.ZuletztOnline))"
	 }
 }
 [void]RunPingTest()
 {
	 $this.ZuletztOnline = $(
	 if (Test-Connection –ComputerName $this.Name
	 -Count 1 -Quiet) {Get-Date}
	 else { Get-Date -Date 0 })
 }
}
```

*Aufgabe 5* Schreibe zwei Methoden für deine Klasse.

Es ist eine Frage, wie man neue Objekte erzeugt. Bei `Int` oder anderen vorher eingebauten Datentypen war es `[int]$a=1`. Bei Objekten eines komplexeren Datentyps ist das Problem: Es reicht nicht, nur einen Wert anzugeben. Daher geben wir eine Funktion an, die alle notwendigen Attributwerte nimmt und setzt. Eine solche Funktion heißt **Konstruktor**.

```ps1
class Server
{
 # Properties
 [string]$Name
 [string]$Marke
 [DateTime]$ZuletztOnline
 [Int]$Seriennummer
 # Methods
 [string]GetBasicInfo()
 {
	 if ($this.ZuletztOnline -eq 0)
	 {
		 return "$($this.Name) (Last seen: never)"
	 }
	 else
	 {
		 return "$($this.Name) (Last seen: $($this.ZuletztOnline))"
	 }
 }
 [void]RunPingTest()
 {
	 $this.ZuletztOnline = $(
	 if (Test-Connection –ComputerName $this.Name
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

Viele Dinge aus der Objektorientierung haben wir uns hier noch nicht angesehen. Diese werden wir uns auch erst später ansehen. Hier aber eine Liste für den Überblick.

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
Wenn in einer Arbeit ein Fehler passiert, schreibt man Tickets, diese Tickets werden von bestimmten Personen abgefangen und bearbeitet. Das ist relativ ordentlich. Ohne Tickets hingegen weniger: Wenn ich ein System habe, wo ich nur bei der Abgabe meiner Aufgabe einen Fehler an andere weiterleiten kann, dann wird es chaotisch und langsam. Nehmen wir noch ein konkreteres Beispiel: Ich möchte gerne auf eine Datenbank zugreifen, um eine bestimmte Sache auszulesen. Wenn die Datenbank nicht existiert, möchte ich gerne in diesem Moment, dass die Person, die die Datenbank nicht angelegt hat, eine böse Mail kriegt.

Dieses langsame System im Programmieren korrespondiert zu „Fehler-Codes“. Das sind Zahlen, die eine Funktion zurück gibt. Meistens heißt $0$, dass alles gut gegangen ist und ein Wert ungleich $0$, dass etwas schief gegangen ist. Der genaue Wert bestimmt, welcher Fehler. Das ist auch der Grund, warum in vielen Programmiersprachen die Main-Funktion immer eine `int` zurück gibt: Das ist ein Fehler-Code.

Eine bessere Variante wären Tickets. In einem bestimmten Bereich des Unternehmens können Tickets geschrieben werden, die an anderer Stelle abgearbeitet werden. In Code sind die Bereiche, die Tickets an dieselbe Stelle schicken, in einem `Try`-Block eingebunden, ein direkt danach folgender `Catch`-Block definiert, wie die „Tickets“ (in Programmiersprachen heißen diese **Exceptions**) zu behandeln sind.

> Lies den [Artikel](https://www.vexasoft.com/blogs/powershell/7255220-powershell-tutorial-try-catch-finally-and-error-handling-in-powershell) und beantworte dabei die folgenden Fragen:

 1. Warum ist es blöd, wenn der Fehler, dass die Datenbank nicht da ist, keine Sonderbehandlung erfährt? Was würde passieren?
 2. Was ist ein non-terminating error?
 3. Mit welcher Code-Zeile kann ich non-terminating errors wie terminating errors behandeln?
 4. In welcher Variable liegt der Text des Fehlers?
 5. Finde im Internet fünf Exceptions, die die Powershell kennt und erläutere, welchen Zustand sie beschreiben.
 6. Wofür ist der Log-Eintrag am Ende von `Finally` wichtig?

Als kleine Anfügung: Wenn ihr die Ausgabe von einem Befehl `befehl` auf die Konsole in eine Datei `out.txt` umleiten wollt, so könnt ihr schreiben `befehl >> out.txt`, falls ihr den Text an die Datei anhängen wollt — gut für Logs — oder `Befehl > out.txt`, falls ihr die Datei überschreiben wollt. Es gibt mehr Funktionalität (teilweise ist es wichtig, nur bestimmte Informationen zu haben), die ihr in den Microsoft [Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_redirection?view=powershell-6) nachlesen könnt.

> Erweitert die Klasse vom letzten Mal um eine Fehlerbehandlung. Falls ihr bisher keine Methode habt, die Text in eine Datei schreibt, so fügt diese hinzu (diese könnte später z.B. die installierte Software halten). Nutzt entsprechende Try-Catch-Blöcke für Fehler, die auftreten können und deren Nichtbehandlung schädlich für das System sein könnte.

Die Analogie mit Tickets krankt bisher darin, dass ihr in eurem Code bisher noch keine eigenen Tickets „schreiben“ könnt — das müssen die vorimplementierten Operationen machen. Die Funktionalität, Tickets zu schreiben ist `Throw`, und wird in anderen Programmiersprachen häufig genutzt. Das schauen wir uns aber hier nicht an.

## Formatierte Ausgabe

Für Administration von Computersystemen ist es wichtig, Dinge übersichtlich auszugeben. Die Powershell gibt hier viel Kontrolle. 

> Aufgabe 1 Lies den [Artikel](https://docs.microsoft.com/de-de/powershell/scripting/getting-started/cookbooks/using-format-commands-to-change-output-view?view=powershell-6) und beantworte die folgenden Fragen: 1. Beschreibe in je einem Satz, wie die Attribute eines Objekts bei `Format-Wide`, `Format-Table` und `Format-List` ausgegeben werden. 2. Warum kann ich bei `Format-Wide` nur eine Property angeben, bei den anderen beiden jedoch eine Liste von Attributen? 3. Mache eine Liste mit allen Parametern (diese beginnen mit einem Minus) im Code des Artikels vorkommen. Erläutere die Bedeutung in jeweils einem Satz.

Ich gebe noch ein Beispiel für `-GroupBy`, was in den Artikeln auftaucht: Wenn ich ein System baue, in dem ich Rechner verwalte, macht es sehr Sinn, die Linux-Rechner in einer anderen Tabelle als die Windows-Rechner anzuzeigen. Dennoch möchte ich sie gerne jeweils als `Computer`-Objekte speichern, also keine Objekte vom Typ z.B. `LinuxComputer` und `WindowsComputer` erstellen. Dann kann ich `-GroupBy OperatingSystem` nutzen.

> Erweitere deine Klasse um eine Ausgabefunktionalität: Die Methode `print` soll eine nach einer Methode gruppierte `Format-Table`-Ausgabe machen.

## Cmdlets
> Lest den [Blog-Eintrag](https://blogs.technet.microsoft.com/heyscriptingguy/2015/07/09/understanding-advanced-functions-in-powershell/) und beantwortet die folgenden Fragen. [^Erläuterung: (1) Ein **Tag** wird einer Funktion vorangestellt und gibt weitere Informationen; ihr seht, wie diese angewendet werden, unten im Blogbeitrag. (2) Folgt bitte dem Blog-Beitrag bei der Erstellung eines neuen Cmdlets, tippt also den Code ab (3) `CmdletBinding` gibt weitere Features, mehr dazu nach dieser Aufgabe (4) „mandatory“ heißt verpflichtend.] 1. Wer ist BB? 2. Was hat Microsoft Public Cloud Services: Setting up your business in the cloud mit dem Artikel zu tun? 3. Welche Aufgabe hat der Teil zwischen `<#` und `#>`.  4. Schreibt den Code einer Funktion, die zwei `int`s addiert. 5. Was bedeutet „Mandatory“? Was wäre ein Beispiel für einen nicht-mandatory Parameter? 6. Was bedeutet Position? 7. Warum ist dieser Blogeintrag nicht wirklich hilfreich? Welche Frage stellt ihr euch noch?

Wenn ihr `CmdletBinding` weglasst, könnt ihr die Funktion weiterhin ausführen, solange ihr die `Parameter`-Attribute weiter angebt (sonst weiß euer Programm nicht, wie ihr `-a` und `-b` nennt). `CmdletBinding` ermöglicht aber einige Funktionalitäten, die ihr unbedingt wollt, wenn ihr Funktionen schreibt: 

 - Pipeline-Input
 - Hilfe/Erläuterungen zum Code
 - Verbose-Output
 - Testläufe (also testen, was gelöscht würde, und es nur angeben).

Das schauen wir uns nicht weiter an, es ist aber wichtig, dass ihr wisst, dass diese Eigenschaften von Befehlen wichtige Stärken der Powershell sind.

> Erstellt nach dem Muster wie im Blogeintrag selbst Cmdlets zu folgenden Aufgaben. Ergänzt auch die Kommentare nach `<#`; wenn ihr nicht weiter wisst, schaut in eure alten Skripte. 1. Zwei Werte als Attribute einlesen (`int`) und `größerer Wert:` gefolgt von der größeren Zahl sowie `kleinerer Wert:` gefolgt von der kleineren Zahl ausgeben. 2. Ein Float einlesen, `True` (also `bool`) zurückgeben, falls es größer ist als 1.

## Module 

Jetzt soll es um Erweiterungen der Befehlsmöglichkeiten in der Powershell gehen. Dass wir gerne unser System um bestimmte Funktionalitäten erweitern möchten, haben wir schon in Linux (Paket-Installation) und für Kryptographie in C# (**Namespaces**) kennengelernt. Dort war es zum Beispiel ein Paket, welches eine graphische Oberfläche ermöglicht (Paket `i3` in Arch Linux), ein Interpreter für Python (`ipython`) bzw. Datentypen für asymmetrische Verschlüsselung (Namespace `System.Security.Cryptography`).

Zwei Gründe sprechen dafür, dass man immer aktiv als User etwas tun muss, um bestimmte Befehle nutzen zu können.

 1. Alle Funktionen immer im kompilierten Code mit einzubauen bedeutet, dass der Code riesig und die Kompilierunug langsam ist und, vielleicht noch wichtiger:
 2. Es gäbe Namenskonflikte: eine Funktion namens `print` gibt es vermutlich in vielen Programmen. 

Daher installieren wir unterschiedliche Arten von weiterem Code. Code installieren heißt, neue Funktionen und Datentypen zur Verfügung zu stellen, was uns die Arbeit erleichtert.

In der ersten Version der Powershell gab es hierfür die Möglichkeit, **Snap-Ins** zu nutzen (das sind die Befehle, die ihr auf der Powershell eingebt, wie etwa `Read-Input`, `Write-Output` a.k.a. `echo`). Da diese installiert werden müssen, benötigen sie hohe Rechte von euch (da ihr Code laufen lassen müsst, bevor ihr die Befehle überhaupt benutzen könnt) und sind daher für Administration teilweise nicht gut geeignet. Sie werden weniger und weniger und auf Grund von Rückwärtskompatibilität gewährleistet. Wir werden keine Snap-Ins bearbeiten.

> Kopiert den Code des `Add-TwoNumbers`-Cmdlets in eine neue Datei uns speichert es als `MyModule.ps1m` `Meine Dokumente\WindowsPowerShell\Modules\MyModule`. Dann tippt
```
Import-Module MyModule
Add-TwoNumbers 1 2
```
Was `3` zurück geben sollte. Falls es nicht klappt, nutzt google, um den richtigen Pfad für Module ausfindig zu machen.

Befehle in der Powershell sollten immer aus einer Verb-Nomen-Kombination bestehen, zum Beispiel `Write-Output`, `Read-Input` oder alle Befehle, die keine Kurzformen waren, die ihr bisher genutzt habt.

> Schreibt für folgende Tasks eine gute Powershell-Beschreibung. 1. Ihr fragt ab, welche Version eine Software hat. 2. Ihr brecht einen Druckbefehl ab 3. Ihr Gebt den aktuellen Nutzer aus 4. Ihr gebt den aktuellen Host aus 5. Ihr lest Input ein.

> Kopiert nun alle bisher geschriebenen Cmdlets in eine Datei, die ihr `MyModule.ps1m` nennt. 

Manchmal möchtet ihr gerne einen Alias setzen, also eine Kurzform, wie zum Beispiel `echo` für `Write-Output`. Das geht in eurem Skript, indem ihr hinzufügt (hier für die Beispiele `cd` und `echo`, die bereits in der Powershell definiert sind):
  
```
Set-Alias echo Write-Output
Set-Alias cd Set-Location
```

Wenn ihr spezifische Cmdlets/Funktionen/Aliasse exportieren wollt, so geht das so (wieder für das Beispiel von `cd` und `echo`) -- beachtet: `-Function` gilt für Funktionen wie Cmdlets.

```
Export-ModuleMember -Function Write-Output
Export-ModuleMember -Alias echo, cd
```

>Wählt ein Cmdlet und für zwei Funktionen Aliasse, die ihr exportieren möchtet.

# Kompetenzliste bis hier hin
 1. [ ] Ich kann den Unterschied von Powershell unnd ISE erläutern.
 2. [ ] Ich kann aus einer Fehlermeldung herauslesen, welches Problem mit der ExecutionPolicy vorliegt.
 1. [ ] Ich kann Typen und Ergebnisse von Ausdrücken angeben (Operatoren von Zahlentypen, Strings, Booleans, Listen, Hashtables) ausgeben. 
 2. [ ] Ich kann entscheiden, ob ein Befehl einen Typfehler auslösen wird.
 3. [ ] Ich kann korrekt Variablen mit bestimmten Inhalten deklarieren und definieren
 4. [ ] Ich kann eine sprachliche Beschreibung einer Schleife in PS-Code übersetzen
 5. [ ] Ich kann eine begin-process-end-Struktur in eine foreach-Schleife übersetzen
 6. [ ] Ich kann zu einer Funktion eine Auswertung ausgibt, die keinen Fehler ausgibt
 7. [ ] Ich kann Pseudocode mit einer Beispieleingabe selbst durchlaufen
 8. [ ] Ich kann die folgenden Begriffe definieren: Objekt, OOP, Abstraktion, Attribut, Methode, Datentyp, Klasse, Instanz, Keyword, `class`, Konstruktor, non-terminating error, terminating error.
 9. [ ] Ich kann entscheiden, ob etwas eine Klasse oder eine Intanz ist.
 10. [ ] Ich kann den Kopf von Methoden und Attributen in einer Klasse ergänzen.
 11. [ ] Ich kann von einer vorgegebenen Klasse Methoden aufrufen und Attribute setzen und abrufen.
 12. [ ] Ich kann anhand eines Codes erklären, wie fehlende Fehlerbehandlung zur Löschung einer Datenbank führen kann.
 13. [ ] Ich kann einer Ausgabe zuordnen, ob sie `Format-Wide`, `Format-List` oder `Format-Table` ist.
 14. [ ] Ich kann erklären, was die Zeilen einer CMDlet-Definition bedeuten.

## Beispielaufgaben
 1. Bitte oben nachlesen.
 2. Was sagt `.ps1 cannot be loaded because the execution of scripts is disabled on this system. Please see "get-help about_signing" for more details.`?
 3. Bitte gib den Typen und den Wert, den die Variable `$a` hat, nachdem die folgenden Befehle ausgeführt wurden. Gibt ERROR an, falls es unterwegs einen Fehler gibt: (a) `[HashTable]$b = {"Frankfurt": 25, "Darmstadt": 0}`, `$a = $b[Frankfurt]`. (b) `$b = 2`, `$a = 2*($b + 2)`, (c) `b = "Hallo"`, (d) `$a = " @(2*$b + 2)`, (e) `"4" -le "2"`, (f) `True -eq True`.
 4. Welcher der Folgenden Ausdrücke löst einen Typfehler aus? Gib kurz den Grund für den Fehler an. `[st] $a = "Hallo"`, `[Int]$a = 4,2`, `[Int]$a = 4.2`.
 5. Deklariere eine String-Variable mit dem Inhalt "Hallo".
 6. Eine While-Schleife soll fünfmal durchlaufen werden. Die Variable `$i` wird nicht in den sonstigen Berechnungen benötigt. Die Gleichung soll abgebrochen werden, falls eine Variable `$a` den Wert fünf hat. Füge am Beginn des Schleifenkörpers fünf Leerzeilen ein.
 7. (a) Übersetze den folgenden Code in eine `begin`-`process`-`end`-Struktur: 
    ```
    function funk1 {
	    "Process Start"
	    foreach ($obj in $args) { Write-Host Pipeline Object: $obj }
	    "Process End"
	}
	```
	(b) übersetze den folgenden Code in eine Struktur ohne `begin`-`process`-`end`: 
	```
	function funk2 {
	    begin    { "Process Start" }
	    process  { Write-Host Pipeline Object: $_ }
	    end      { "Process End" }
	}
	```
 8. Gib eine Anwendung der folgenden Funktion an, die keinen Fehler gibt `function Square([int]$a){ return $a*$a }`.
 9. Werte den folgenden Pseudocode für die Eingabe $n=5$ aus: 
     ```
     function fun(n):
      res = n; 
      for n=1 to n-1 do:
       res = res + n;
      return res;
     end function
     ```
 10. Bitte oben nachlesen
 11. Gib an, ob die folgenden Datentypen oder Objekte sind, oder weder noch: Hallo, 2, Int, "Do".
 12. Füge zur folgenden Klasse den Kopf einer Methode `Update`, die einen Integer nimmt und einen String zurückgibt sowie ein Int-Attribut `Installed` vom Typ `DateTime`: 
	 ```
	 class MyClass
	 {
	  ________________
	  ________________
	  {
	   ...
	  }
	  MyClass($Installed)
	  {
       $this.Computername = ___________
	  }
	 } 
	 ```
 13. Rufe in der obigen Klasse `Update` mit dem Wert `5` auf, rufe den Wert von `Installed` ab und setze ihn auf `0`. Nimm an, dass zuvor `$a = [MyClass]::new()` ausgeführt wurde.
 14. Was kann in der Verwendung des folgenden Codes falsch laufen? 
	 ```
	 $AuthorizedUsers= Get-Content \\ FileServer\HRShare\UserList.txt
	 $CurrentUsers=Get-ADGroupMember "Expenses Claimants"
	 Foreach($User in $CurrentUsers)
	 {
	  If($AuthorizedUsers -notcontains $User)
	  {
	   Remove-ADGroupMember -Identity "Expenses Claimants" -User $User
	  }
	 }
	 ```
 15. Ergebnis welchen Format-Befehls ist die folgende Ausgabe? 
	 ```
	 Id      : 2760
	 Handles : 1242
	 CPU     : 3.03125
	 Name    : powershell
	 Id      : 3448
	 Handles : 328
	 CPU     : 1.0625
	 Name    : powershell
	 ```
 16. Schreibe einen korrekten Aufruf (also einen, der keinen Fehler erzeugt) der Funktion `Write-LargerUnity`.
	 ```
	 function Write-LargerUnity
	 {
	  [CmdletBinding()]
	  [OutputType([int])]
	  Param([Parameter(Mandatory=$true, ValueFromPipelineByPropertyName=$true, Position=0)][int]$a)
	  if($a -gt 1){
	   return True
	  } else{
	  return False
	  }
	 }
	 ```