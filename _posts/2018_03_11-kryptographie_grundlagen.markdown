---
layout: post
title:  "Productivity Software Helpers"
date:   2018-01-26 00:26:05 +0100
categories: learn
---

## Grundlagen
**Ziele**

 - Können den Unterschied von Typ und Objekt erklären
 - Können `using` auf zwei Weisen anwenden
 - Kennt die Bedeutung des Disposing für die Kryptographie

<!--more-->
### Typen
Typen sind die „Arten“ von Objekten in Programmiersprachen. Beispiele sind `int`, `string`, `uint` und `byte`. Standardmäßig sind Typen in Visual Studio (VS) blau eingefärbt und stehen vor Funktions- und Variablennamen. 
> a. Schreibe dir in einem Programm, welches du bisher geschrieben hast, alle Typennamen heraus und mache eine Strichliste, wie oft jeder Typ vorkommt.
> b. Fahre mit der Maus über die Typen und lies dir die Bedeutungen der Typen durch

### Namensräume
Ein Namensraum (=Namespace) ist ein Raum, innerhalb dessen Typen und Variablen eine Bedeutung bzw. dieselbe Bedeutung haben. Namensräume werden durch Blöcke von `{`, `}` (ab sofort nur noch „Blöcke“) begrenzt und können einen Namen mit dem `namespace`-Keyword kriegen. 
> Wo steht das `namespace`-Keyword in deinen bisherigen Programmen? Schreibe auf!
#### Typen
Grundsätzlich können nur Typen benutzt werden, die im aktuellen Namespace definiert werden.[^Das geht mit *Klassen*, was wir uns hier nicht anschauen. Manche Typen können auch benutzt werden, wenn sie nicht im aktuellen Namespace definiert werden. Stichwort ist: Klassen-Zugriffsmodifizierer (z.B. `public`, `private`, `internal`, `external`).] Hier bedeutet „im aktuellen Namespace“ alle Bereiche von Code, die man erreichen kann, ohne einen Block zu verlassen, den man vorher nicht betreten hat.
> Schaue dir das folgende Code-Stück an und markiere alle verschiedenen Namespaces.

```cs 
using System;

namespace Main
{
	class MainClass()
	{
		public static void Main()
		{
			int a = 4;
			int sum = 0; 
			for(int i = 0; i<=a; i++)
			{
				sum += i;
			}
			return sum;
		}
	}
	
}
```

Wir können mithilfe des `using` keywords andere Namespaces einbinden oder sogar Zusammenstellungen von Namensräumen, sogenannte „Assemblies“
> Schreibe dir aus drei alten Programmen heraus, welche `using`-Statements du benutzt hast. 

So können wir komplexe Typen aus anderen Namespaces nutzen.
#### Variablen
Auch Variablennamen leben in bestimmten Namespaces. Der Unterschied zwischen einer Variable und einem Typ ist wie der zwischen einem Tier und einer Tierart. Beide haben Namen: Knut, Eisbär. Knut war ein konkreter Eisbär, eine sogenannte Instanz. Eisbär ist der Typ von Knut.
> Im Folgenden Code, markiere in gelb alle Typnamen, in grün alle Variablennamen.

```cs
int a = 0;
string hello = "Hello"; 
using (int a = 4)
	int a = 5;
```

Namen von Variablen sind nur innerhalb des aktuellen Namespaces bekannt. Das hat Vorteile dahingehend, dass wir uns nicht darum kümmern müssen, was wir in bestimmten Blöcken deklarieren, da unser Programm ohnehin dort deklarierte Variablen „vergisst“.
> Was würde am folgenden Code richtig nervig werden, wenn es dieses Vergessen nicht gäbe

```cs
for(int i=0; i<=4; i++)
{
	Console.WriteLine("Hi");
}
``` 

Ähnlich wie wir am Anfang von Dateien andere Typen aufrufen können, können wir Variablen für einen kommenden Block deklarieren. Dies hat aber einen anderen Zweck als bei Typen: Wir wollen gerne, dass die Objekte nur für die Zeit des kommenden Blocks/in diesem Namespace existieren und danach auch wirklich aufgeräumt werden. 
> Überlege dir: Was muss vermutlich für Dateien gemacht werden, um Eingabe- und Ausgabe zu machen. Was entspricht hier dem „Aufräumen“?

Aufräumen ist gut für Ordnung. In Kryptographie ist Aufräumen aber unerlässlich: Wenn wir einen Schlüssel, den wir nicht mehr brauchen, einfach fallen lassen, dann kann ihn jemand bei genauem Absuchen des Bodens aufheben und damit Böse Dinge tun. Ähnlich ist es mit einfach so „vergessenem“ Speicher. Dieser ist nicht überschrieben. Außer man stellt mit `using` sicher, dass das Objekt verschwindet.
> Deklariere mit `using` eine Variable, die Du nur in einem Block benutzt.

### Methoden
Typen können Operationen/Funktionen haben, die auf ihnen operieren. Ein Beispiel kennt ihr schon `Console.WriteLine()`. `Console` ist ein Objekt, in gewisser Weise besonders, da das einzige seiner Art.[^d.h. es gibt kein anderes Tier von der Art `Console`. Solche Typen nennt man „statisch“.] Es hat eine Operation, die auf die Konsole etwas schreibt. Ein anderes Beispiel ist

```cs
int a = 4;
a.CompareTo(3);
```

Hier wird ausgegeben, wie sich `a` zu `3` verhält.
> Probiere den obigen Code aus. Dir werden alle zulässigen Methoden angezeigt. Probiere sie alle einmal mit Beispielen aus.

### Encoding
Ein Encoding ist eine Übersetzung von Bit-Arrays auf Zeichen. Es gibt hier sehr viele. In der Kryptographie wird das Encoding zumeist außen vor gelassen und direkt mit Bit- oder Byte-Arrays gearbeitet. 

> Fertige aus dem Internet eine Liste mit verschiedenen Encodings an. 