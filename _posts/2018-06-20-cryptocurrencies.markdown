---
layout: post
title:  „Probleme, die Bitcoin löst“
date:   2018-04-25 08:00:00 +0100
categories: teach
---
# Cryptocurrencies
<!--more-->
## Auswertung des Schecksimulation

Eine Simulation mit Schecks bringt verschiedene Schwierigkeiten von Zahlungssystemen zutage: Geld muss immer durch die Zentrale Autorität ausgegeben werden! In einem ersten, unsicheren Modell sah die Zahlung wie folgt aus (Überweisung Alice an Bob): 

 1. Alice trägt einen Betrag und Bobs Namen in den Scheck ein, sowie, woher das Geld kommt.
 2.  Sie tütet den 
 3.  unterschriebenen Brief ein. 

Was könnte das Äquivalent im Digitalen sein? Trage die Begriffe Überweisungsdaten, digitale Signatur, verschlüsselten vorangegangenen Transaktionen, öffentlichen Schlüssel, Hash ein: 

## Der Digitale Ablauf
1. Alice schreibt den Betrag (die \_\_\_\_\_\_\_\_\_\_) und den \_\_\_\_\_\_\_\_\_\_ von Bob, sowie die bisherigen \_\_\_\_\_\_\_\_\_\_ des Coins ein.
2. Sie berechnet den \_\_\_\_\_\_\_\_\_\_ dieser Daten.
3. Sie hängt eine \_\_\_\_\_\_\_\_\_\_ an.

Wenn wir uns das zweite Szenario anschauen, dann sieht es so aus

1. Eine Überweisung von Alice an Bob besteht von einer Überweisung von Alice an die CA/Bank und einer von der CA an Bob. 
2. Man vertraut der CA. 


Schreibe den „Digitalen Ablauf“ von oben für den Ablauf mit einer CA analog.

1. \_\_\_\_\_\_\_\_\_\_
2. \_\_\_\_\_\_\_\_\_\_
3. \_\_\_\_\_\_\_\_\_\_


## Expertengruppe 1: Double Spending
Zwei Personen wollen sich etwas überweisen. Sie haben leider beide keinen Kontakt zu einer Bank, da die Bank gehackt wurde. Nun könnte A an B etwas überweisen und denselben Betrag an C, obwohl A diesen Betrag gar nicht mehr besitzt. Dieses Problem ist als **Double Spending** bekannt. Nehmen wir an, eine Gruppe von Personen tut sich zusammen. Denke dir zwei Möglichkeiten aus, wie diese Gruppe wieder einen funktionierenden Geldverkehr herstellen könnte — zuerst für dich alleine (und kurz) und danach in deiner Expertengruppe. 

---
--- 
--- 
---
--- 
--- 
---
--- 
--- 



## Expertengruppe 2: Eine Attacke durch Modifikation
Zwei Personen wollen sich etwas überweisen. Sie haben leider beide keinen Kontakt zu einer Bank, da die Bank gehackt wurde. Daher machen alle Menschen eine gemeinsame Liste aller Transaktionen, die getätigt wurden. Eine Person schreibt sich eigene Transaktionen in die Liste, die aber gar nicht stattgefunden haben. Dies ist eine **Attacke durch Modifikation**.  Denke dir zwei Möglichkeiten aus, wie diese Gruppe wieder einen funktionierenden Geldverkehr herstellen könnte — zuerst für dich alleine (und kurz) und danach in deiner Expertengruppe.


---
--- 
--- 
---
--- 
--- 
---
--- 
--- 



## Expertengruppe 3: Eine Attacke durch Neuschreiben
Zwei Personen wollen sich etwas überweisen. Sie haben leider beide keinen Kontakt zu einer Bank, da die Bank gehackt wurde. Daher machen alle Menschen eine gemeinsame Liste aller Transaktionen, die getätigt wurden. Nun kommt eine Person her, und behauptet, dass sie eigentlich die „richtige“ Liste hätte. Dies ist eine **Attacke durch Neuschreiben**. Denke dir zwei Möglichkeiten aus, wie diese Gruppe wieder einen funktionierenden Geldverkehr herstellen könnte — zuerst für dich alleine (und kurz) und danach in deiner Expertengruppe.

---
--- 
--- 
---
--- 
--- 
---
--- 
--- 


## Wie Bitcoin funktioniert
Beantworte die folgenden Leitfragen bei Lektüre des nachfolgenden Textes:

1. Was meint der Text, wenn es heißt „Unsere bisherige Geldwirtschaft basiert darauf, dass die Überweisungen immer über eine Bank getätigt werden.“? Antworte in drei Sätzen.
2. Was ist ein Block? 
3. Wofür braucht es einen Nonce?
4. Beschreibe, wie in der Blockchain die Attacke, für die Du Experte warst, verhindert wird.

Bitcoin hat zwei Strukturen: Zum einen einen eine Reihe von Überweisungen wie in Sektion 1 und im Scheckspiel betrachtet. Zum anderen ein gemeinsames Buch aller Überweisungen. Wir betrachten beide einzeln

Die Reihe von Überweisungen sieht aus wie oben: Jedes Stück Geld (denke: jeder Cent) hat einzeln einen Besitzer und besteht lediglich aus einem Binärstring. Möchte diese\*r seinen Coin weitergeben, so erstellt er einen neuen Binärstring wie folgt: Er nimmt den öffentlichen Schlüssel des nächsten Besitzers (dieser wird als Name für den neuen Besitzer benutzt) zusammen mit dem bisherigen Binärstring, hasht beide und hängt eine Signatur dieser Daten an, nachdem er verifiziert hat, dass er das Geld auch wirklich senden möchte. 

Wie wir gesehen haben: Hier benötigt der\*die Empfänger\*in großes Vertrauen, da der\*die Überweiser\*in einen Coin mehrmals ausgeben muss. Unsere bisherige Geldwirtschaft basiert darauf, dass die Überweisungen immer über eine Bank getätigt werden.

Die zweite Struktur ist eine Blockchain. Diese notiert Blöcke, die jeweils aus einer Reihe von Transaktionen in einem Zeitraum und einem Zeitstempel (also einer Uhrzeit) wann dieser Zeitraum ist, bestehen. Die Blockchain besteht zu jedem Zeitpunkt aus einem Binärstring. Wird ein neuer Block in die Blockchain (=„Kette von Blöcken“) notiert, so nimmt man den bisherigen Wert, hängt Zeitstempel und Transaktionen und eine weitere Zahl, genannt **Nonce** an. 

Die Nonce ist eine Zahl, die so gewählt sein muss, dass viele Nullen am Anfang des Ergebnisses stehen. Diese sorgt dafür, dass eine Attacke durch Neuschreiben und eine Attacke durch Modifikation nicht möglich sind: Die Nonce zu finden ist hart. Und für unterschiedliche Transaktionen muss die Nonce eine andere sein. Weiterhin müsste, wenn man eine eine Attacke durch Neuschreiben versucht, man selbst sehr schnell rechnen: Denn es ist für alle Beteiligten vorteilhaft, die Blockchain für wahr zu halten, in der am meisten gerechnet wird: Diese ist die „Wahrheit“. 

Ein Double Spending wird wie folgt verhindert: In einem einzigen neuen Block Double Spends (also zweifache Transaktionen) von keinem (außer dem\*der Betrüger\*in) geglaubt, also an dieser Blockchain nicht weitergerechnet wird (niemand möchte Double Spending erlauben, da es ihn\*sie selbst treffen könnte).