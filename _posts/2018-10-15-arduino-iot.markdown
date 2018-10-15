---
layout: post
title:  „Arduino Projekt zu Internet of Things“
date:   2018-10-15 08:00:00 +0100
categories: teach
---
# IoT-Projekt I: Kennenlernen des Arduino
Bevor wir mit IoT beginnen können, müssen wir zuerst einmal unsere Programmiersprache kennenlernen. Hierzu gibt es 19 Fragen, die ihr alle mit den (offline verfügbaren) Unterlagen — bis auf einen Link, der steht aber auch im folgenden — beantworten können solltet. Wir vergleichen nach 1 Stunde. Arbeitet mit einem Partner. Schreibt zu jeder Aufgabe ausreichend Stichpunkte auf, so dass ihr sie direkt beantworten könnt, wenn ich euch aufrufe.

## Einrichtung

2. Lass dir die Zeilennummern anzeigen. Wie geht das?
3. Folge der Beschreibung auf https://learn.adafruit.com/adafruit-feather-huzzah-esp8266/using-arduino-ide

## Grundlegende Syntax
1. Wofür werden Code-Einrückungen und -Ausrückungen gebraucht? Was ist die Syntax für die in Arduino? Was ist der Hotkey in der IDE? 
1. Was ist die Syntax für Kommentare, was der Hotkey?
2. Ladet das Beispiel `BareMinimum`. Was **muss** ein Arduino-Programm enthalten?
3. Wie binde ich Libraries ein? Gib drei Beispiele für Libraries.
4. AE: Was könnte Serial bedeuten?
5. Schreibe deine eigene Kurzreferenz zu den folgenden Befehlen. Schreibe alle Argumente, Aktionen und Ausgaben hin.
	6. `pinMode`
	7. `analogRead`
	7. `Serial.println`
	8. `delay`
	9. `digitalWrite`
	10. `analogWrite`

## Interface
1. Wo findet man Troubleshooting? Was könnte ich für ein falsches USB-A zu Micro-USB-Kabel benutzt haben, wenn das Hochladen nicht funktioniert?
2. Wie werden Arduino-Code-Dateien benannt (Tipp: drei Möglichkeiten)?
3. Finde die Sprachreferenz. Welche Schleifen gibt es in Arduino? Welche Typen gibt es, die es in C# nicht gibt?

## Bigger Picture
5. Was ist ein Bootloader?
6. Was ist der Unterschied zwischen analog und digital beim Arduino? Wie analog ist „analog“ beim Arduino?
7. Was ist in Arduino ein Bootloader? Wir hatten mit Linux auch einen Bootloader, GRUB. Was ist die Gemeinsamkeit?
8. Welche Sensoren nutzen die die Beispiele in „6.Sensors“?
8. Wie nennt man die Schreibweise der folgenden Begriffe: `analogRead`, `dataString`, `analogPin` (Tipp: Wüsentier)? AE: Wie sind die Namenskonventionen in C#?

## ESP8266
1. Öffne das Beispiel `ESP8266WiFi>WifiScan`. Was passiert hier?
2. Öffne das Beispiel `Hash > SHA1`. Was passiert hier? Warum sollte ein Kleinrechner einen Hash berechnen können?
3. Öffne das Beispiel `SD(esp8266)>Files`. Was passiert hier?

# IoT-Projekt II: Sensoren, Aktoren
Letzte Woche haben wir uns mit der Arduino IDE beschäftigt. Die dort erstellten *Sketches* (kurze Programmschnipsel) werden auf dem *Board*, einem Mikrokontroller ausgeführt.

Heute beschäftigen wir uns mit dem Board. Unser Board ist das „Adafruit Feather Huzzah!“. Hier ist „Adafruit“ der Hersteller, „Feather“ ist eine Platine und „Huzzah!“ die Bezeichnung für dieses konkrete Board. Der Chip auf dem Board ist der ESP8266, welcher ein wichtiges Unterscheidungsmerkmal zwischen unterschiedlichen Mikrokontrollern ist. 

Unsere Ziele sind: 

 - Die Hardwarekomponenten des Adafruit Feather Huzzah und des Breadboard benennen und deren Funktion erklären können
 - Analoge und digitale Aktoren und Sensoren benennen können.
 - Einen Schalterstromkreis „klassisch“ und mithilfe eines programmierbaren Mikrokontrollers einrichten.

## Die Hardwarekomponenten des Adafruit Feather Huzzah!
### Das Board
![](/pinout.png)
Wir können mit dem Feather Huzzah über sogenannte *Pins*/*Leads* interagieren. Dies sind mit Leitmetall verkleidete Löcher am Außenrand des Chips. Durch diese können wir grundlegende Ein- und Ausgabe (GPIO) mit dem Adafruit Huzzah! machen. Strom und Daten gibt es per USB-B, Energie alternativ auch durch eine Lithium-Batterie. Für uns sind ein paar Pins nur wichtig. Die anderen werden wir erst einmal nicht nutzen. 

 - GND: Steht für „Ground“ ist die niedrige Spannung im Stromkreis, ist die „Senke“ unseres Stromkreises und logisch die 0. Nennt man auch Minus-Pol
 - 3V: Genauer gesagt 3,3 Volt, ist unsere Spannung, der Pluspol.
 - 2, 4: Diese sind standardmäßig zu einer roten bzw. blauen LED auf dem Chip verbunden und können als Output genutzt werden, um zu testen, ob es funktioniert.

Weiterhin ist ADC ein analog-Input, den wir aber heute nicht brauchen werden.

Aufgabe: 

1. Beschrifte deine Arduino-Tüte
2. Schließe deinen Arduino an, suche den passenden Port in der Arduino-IDE
3. Gebe den unterstehenden Code in die Arduino-IDE ein und lade sie hoch.
4. Schreibt hinter jede Zeile des folgenden Programms einen Kommentar mit dem, was hier passiert.

``` cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);}
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);}
``` 
### Das Breadboard
![](breadboard.png)

Ein (solderless=ohne Löten) Breadboard ist ein gelöchertes (zumeist Plastik-)Brett, welches miteinander verbundene Klammern aus Leitern unter den Löchern hat. Es ermöglicht mithilfe sogenannte *Jump Wires* („Sprung-Kabel“) ohne Löten elektrische Schaltkreise schnell auszuprobieren. Vermutlich wurden solche Prototypen früher auf den Brotschneide-Brettchen hergestellt — dort könnte der Name herkommen. Das Breadboard hat Klammern, die in einem bestimmten Muster miteinander verbunden sind (siehe Bild oben). Links und rechts ist eine Reihe von sehr vielen Pins, die alle miteinander verbunden sind. Bei den meisten Breadboards steht hier „+“ und „-„ dabei — das ist nur ein Hinweis und nicht bindend. Das Breadboard möchte euch aber sagen: An „+“ kommt ein Jump Wire von den 3,3 Volt, und in dieser Reihe könnt ihr dann alle Jump Wires verbinden, die Strom brauchen. Das sieht dann etwa so aus:
![](dumme_steckplatine.png)
Das werden wir uns später noch anschauen. Die horizontalen Querverbindungen in der Mitte ermöglichen euch einfach Parallelschaltungen zu machen. Wer jetzt kein Elektrotechnik-Geek ist — alles ok wenn ihr davon nichts versteht. Wir brauchen Parallelschaltungen nur teilweise für unsere einzige Regel heute:
> Regel: **Nie** einen Verbraucher ohne Widerstand anschließen.

Aufgabe:

1. Platziere deinen Chip auf dem Breadboard (Man braucht Kraft **und** Feingefühl) wie auf dem Bild oben.
2. Hole dir eine LED, einen Schalter oder Sensor und ausreichend Jump Wires um den obigen Schaltkreis (oder so ähnlich) nachbauen zu können.
## Aktoren und Sensoren
Wir können elektronische Bauteile, die wir verwenden werden, in zwei Kategorien einteilen:
 
- *Sensoren* messen physikalische Größen wie Druck (Schalter, Drucksensor), Licht, Temperatur, Luftfeuchtigkeit, Höhe, Bewegung
- *Aktoren* setzen elektrische Signale um, um physikalische Größen zu verändern: Bewegung (Servo-motor), Temperatur (Heizstrahler), Licht (LED), Ton (Piezo-Bauteil).

Eine zweite Unterscheidung ist analog vs. digital. Digital nimmt zwei Werte an, analog mehr. 

Aufgaben:

1. Wie viele Werte nimmt in der Programmiersprache Arduino ein analoger Wert an?
2. Lege eine Tabelle wie die unten an. Sie hat vier Felder: analoge Sensoren, digitale Sensoren, analoge Aktoren, digitale Aktoren. Finde für jedes Feld fünf Einträge. Nutze das Internet hierfür.

|  | Sensor | Aktor |
|:--|:--|:--|
| analog |  |  |
| digital |  |  |

## Ein erster Gleichstromkreis
Wir wollen heute noch verstehen, wo ein einfacher Schaltkreis an seine Grenzen stößt und ein Mikrocontroller bereits seine Stärken ausspielen kann. Wir wollen den folgenden Stromkreis bauen:

![](schaltplan.png)

Wir leiten den Strom von 3,3 Volt über einen Schalter durch eine LED und einen Widerstand von 220 Ohm zum Ground. Soweit, so gut.
![](dumme_steckplatine.png)  
Aufgabe: 

1. Baut den obigen Schaltplan einmal auf.
2. Probiert den Schalter aus.
3. (Zusatzaufgabe) Tauscht Eure Schalter und probiert einen anderen aus.

## Ein schlauerer Gleichstromkreis
Aufgabe:

1. Ich möchte gerne, dass, wenn ich den Schalter drücke, das Licht erst eine Sekunde verzögert ausgeht (dasselbe könnte man mit 1min denken, z.B. für das Licht in der Garage). Wie könnte ich das mit einem Stromkreis realisieren?

Gar nicht so einfach. Es gibt aber eine einfachere Lösung. Und die nutzt, dass euer Mikrocontroller deutlich cleverer ist als ein einfacher Stromkreis. 
![](schlaue_steckplatine.png)
Aufgabe: 

1. Baut die obige Steckplatine auf.
2. Gebt den unterstehenden Code in die Arduino IDE ein und ladet ihn hoch. 
3. Schreibe hinter jede Zeile einen Kommentar, was hier passiert.
4. Findet und öffnet den „seriellen Monitor“. Was seht ihr hier.
5. Bisher geht bei euch das Licht aus, wenn ihr den Schalter drückt. Versucht das Verhalten umzukehren.

```  
int button = 4;
int led = 5
void setup() {
  Serial.begin(9600);
  pinMode(button,INPUT);
  pinMode(led,OUTPUT);}
void loop() {
  int sensorValue = digitalRead(button);
  Serial.println(sensorValue);
  delay(100);
  digitalWrite(led,sensorValue);}
```

## Einfache Elektronik vs. Mikrocontroller
Aufgabe: 

1. Was hat unser Ansatz mit Mikrocontrollern also für einen Vorteil? Schreibe mindestens 3 Sätze.

# IoT-Projekt III: Erweiterungen und Data Logging
In den letzten beiden Stunden haben wir uns mit der *Arduino IDE* und dem *Board* beschäftigt. Heute wollen wir uns mit Erweiterungen beschäftigen. Diese heißen häufig *Shields* (Schilde), weil sie so angebracht werden, dass sie die Elektronik auf dem Mikrocontroller abschirmen.

Unsere Ziele heute sind:

1. Ihr könnt verschiedene Erweiterungsmodule, die nicht mit klassischen Aktoren oder Sensoren zu erhalten sind, benennen. 
2. Ihr könnt in der Arduino-IDE eine Library einbinden.
3. Ihr könnt den Arduino die Uhrzeit anzeigen lassen. 
4. Ihr könnt die Begriffe Datalogging und Timestamping definieren.
5. Ihr könnt drei Klassen benennen, die im Data-Logging wichtig sind.  

## Erweiterungsmodule
Die Erweiterungsmodule der Adafruit Feather-Serie nennen sich „Wings“. Wir haben den „RTC+SD Wing“ vorliegen. *RTC* steht für „Real-Time Clock“. Arduino kennt zwar auch einen Zeit-Command, dieser wird aber immer wieder auf Null zurückgesetzt, wenn der Arduino neu an den Strom angeschlossen wird. Auf einer SD (*Secure Digital* Memory Card) können wir Daten speichern.
### Datalogging
Häufig ist es so, dass wir bestimmte Messungen nicht direkt an eine zentrale Einheit übertragen wollen, sondern dezentral speichern und nur gelegentlich auslesen wollen. Zum Beispiel bei Log-Dateien; oder — vor dem Internet-Zeitalter — bei Erdbebenmessgeräten: Du würdest nicht live in Logdateien schauen oder ein Erdbebenmessgerät permanent anschauen, sondern es erst einmal schreiben lassen, und später schauen.

Hierfür ist es sehr wichtig, Zeiten für Ereignisse mit zu speichern. *Datalogging* heißt, einen Bericht über alle Ereignisse, die ein Sensor in einem Zeitraum registriert, zu führen, und das mit jeweils einer Zeitangabe. Die Zeitangabe ist der sogenannte *Timestamp* (Zeitstempel). Unsere Erweiterung bietet neben einer Möglichkeit zur Datenspeicherung auch gleich eine Uhr für Timestamps.
 
### Andere Erweiterungen
Erweiterungsmodule von Mikrocontrollern zeichnen sich häufig durch eine erhöhte Komplexität oder Unhandlichkeit gegenüber einfachen Sensoren oder Aktoren aus. Dies kann an der schieren Größe liegen (LED-Matrix) oder an den Anforderungen an Berechnungen, die ein Chip benötigt (RTC, SD, GPS). 

Aufgabe: 

1. Suche dir 5 Wings für unsere Chips oder Shields für Arduino. Schreibe jeweils einen Satz, was diese tun und warum diese über „normale“ Sensoren und Aktoren hinausgehen.

## Libraries in Arduino
Die meisten Programmiersprachen sind *modular* aufgebaut. Wenn ihr z.B. eine Kryptographie-Bibliothek in C# nutzen wollt, so müsst ihr `using System.Security.Cryptography;` an den Anfang eurer Hauptdatei setzen, damit ihr (von anderen Menschen geschriebene) Algorithmen nutzen könnt. Das gibt es auch in Arduino. Nehmen wir als Beispiel die RTC-Library.

Aufgabe: 

1. Installiere die RTClib im Bibliotheksmanager (das ist ein Menüeintrag, nutze Google!)
2. Öffne den seriellen Monitor (auch ein Menüeintrag) und stelle auf Baud[^Die „Baud Rate“ (Baud-Frequenz, nach Émile Baudot, 1845-1903) gibt an, wie viele Symbole in einer Zeiteinheit übertragen werden. In diesem Fall 57.600 Symbole in einer Sekunde. Es wird für jedes Achtel einer $\frac{1}{57600}$-stel Sekunde gemessen, ob der gemessene Strom hoch genug ist, so dass eine 1 übertragen wurde — die herauskommende 8-Bit-Zahl wird als  Symbol interpretiert. Da die Datenübertragungsrate unseres Arduino konstant ist, wird Kauderwelsch herauskommen, wenn wir eine falsche Baud-Frequenz nutzen.] 57600. 

Der Code zum Einbinden und „Stellen“ der Uhr sieht so aus.

```
#include "RTClib.h"
RTC_PCF8523 rtc;
void setup(){
Serial.begin(57600);
rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));}
DateTime now = rtc.now();
```

Wir nutzen also einen `#include`-Befehl, um neue Klassen/Typen zu bekommen! Der Variablentyp `RTC_PCF8523` ist, bevor wir `RTClib.h` heruntergeladen haben (über den Library-Manager) und dem Programm gesagt haben, dass er diese Header-Datei lesen soll (mit `#include "RTClib.h“`) noch gar nicht da. `rtc` hat mehrere Methoden, mit und ohne Parameter. Die Frage, was `F` ist, wird [hier](https://www.baldengineer.com/arduino-f-macro.html).

## Mit dem Arduino eine Uhrzeit ausgeben lassen
Nun wollen wir uns die Uhrzeit des Arduino anzeigen lassen. Wir könnten unseren mit unserem Feather mit Kabeln verbinden, etwa so wie hier:

![](rtc.png)

Das ist aber sehr umständlich. Wir gehen einen einfacheren Weg und stecke den Feather einfach auf den Featherwing auf. Dann sind alle Pins in Kontakt.

![](rtc_stacked.png)



Aufgaben:

2. Schreibe den unterstehenden Code ab
3. Kommentiere, was in jeder Zeile passiert.
4. Erstelle eine Uhr, die nur Stunden und Minuten anzeigt, sich einmal pro Minute aktualisiert und nur 12 Stunden anzeigt (also 1:34 Uhr statt 13:34 Uhr)
5. Oben sind sehr viele `print`-Statements hintereinander. Finde im Internet zwei entgegengesetzte Meinungen: Eine, die das genau machen würde, mit einem Argument und eine, die eine andere Meinung vertritt.



```
#include "RTClib.h"
#include <Wire.h>
RTC_PCF8523 rtc;
void setup () {
  Serial.begin(57600);
  if (! rtc.begin()) {
    Serial.println("Couldn't find RTC");
    while (1);}
  if (! rtc.initialized()) {
    Serial.println("RTC is NOT running!");
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));}}
void loop () {
  DateTime now = rtc.now();
  Serial.print(now.day());
  Serial.print('.');
  Serial.print(now.month());
  Serial.print('.');
  Serial.print(now.year());
  Serial.print(',');
  Serial.print(now.hour());
  Serial.print(':');
  Serial.print(now.minute());
  Serial.print(':');
  Serial.println(now.second());
  delay(3000);}
```
  
Die Library „Wire.h“ erlaubt, externe Module über Jump Wires anzusteuern. 

## Wie sieht also Datalogging aus?
Mit dem obigen Schaltplan könnt ihr auch noch mehr.

Aufgaben: 

1. Lade den Code des Beispiels „CardInfo“ und setze in Zeile 36 `chipselect = 15`.
2. Erweitert euren Schaltplan, so dass er so wie unten aussieht. Anstatt die Kabel zwischen dem Feather Huzzah und dem Featherwing zu behalten könnt ihr auch die beiden Chips einfach aufeinander stapeln. Beobachtet, dass wir Pins miteinander verbunden haben, die bei Stapeln direkt aufeinander liegen.
2. Kopiere den nachfolgenden Code und lade ihn hoch.
3. Was tut der Code? Schreibe mindestens drei Sätze.

Hier einmal ohne Stapelung der Chips
![](rtc+sd_datalogging.png)
Hier einmal mit.
![](datalogger_stacked.png)
Ihr könnt gerne vor den Widerstand auch eine LED schalten, dann habt ihr Gewissheit, dass auch tatsächlich Strom fließt.

```
#include <SPI.h>
#include <SD.h>
#include "RTClib.h"
#include <Wire.h>
RTC_PCF8523 rtc;
void setup() {
  pinMode(16, INPUT); 
  Serial.begin(57600);
  if (!rtc.begin()) {
    Serial.println("Couldn't find RTC");
    while (1);}
  if (! rtc.initialized()) {
    Serial.println("RTC is NOT running!");
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));}
  if (!SD.begin(15)) {
    Serial.println("Card failed, or not present");
    while (1);}
  else 
    Serial.println("card initialized.");}  
void loop() {
  DateTime now = rtc.now();
  String dataString = "";
  dataString += String(now.unixtime());
  int sensorValue = digitalRead(16);
  dataString += "," + String(sensorValue);
  File dataFile = SD.open("datalog.txt", FILE_WRITE);
  if (dataFile) {
    dataFile.println(dataString);
    dataFile.close();
    Serial.println(dataString);}
  else {
    Serial.println("error opening datalog.txt");}
  delay(1000);
}
```

Wenn ihr erneut das Beispiel „CardInfo“ nutzt, seht ihr, dass ihr eine Datei `Datalog.txt` erstellt habt, die wächst. Habt ihr einen Micro-SD-Eingang an einem eurer Endgeräte, so könnt ihr die Datei auslesen, und z.B. mit einer Shall Einträge filtern.

Wir haben also gesehen: Einzelne Erweiterungen erlauben Anwendungen, die zu komplex für Sensoren und Aktoren wie wir sie bisher kennen sind — zum Beispiel Datalogging. Nächste Woche geht es weiter mit einem weiteren Modul: einem NFC-Sensor.


# IoT-Projekt IV: Normung/NFC
Letzte Woche haben wir uns mit *Datalogging* beschäftigt. Uns ging es darum, dass wir gerne eigenständigen Einheiten ermöglichen wollen, selbst Daten zu halten: Das haben wir mithilfe von Zeitstempeln (also Uhrzeiten, wann genau bestimmte Sensormesswerte angekommen sind) bewerkstelligt. 

Heute geht es um Standards/Normen.

Unsere Ziele sind:

 - Die physikalische Grundlage von NFC, kontaktloser Zahlung erklären können.
 - Die Vor- und Nachteile von Standardisierung im Kontext von Industrie und Arbeitswelt erörtern können und anhand eines Beispiels erläutern.
 - Ihr kennt die Struktur einer internationalen Norm.

# Was ist NFC und wie funktioniert es?
Near Field Communication ist ein RFID (=Radiofrequenz-Identifikation)-basierter Kommunikationsstandard. Gehen wir zuerst auf die physikalischen Grundlagen von RFID ein: Induktion. Wenn ihr einen Induktionskochtopf nutzt werdet ihr sehen, dass die Platte selbst nicht heiß ist, sondern nur das Metall in dem Top selbst heiß wird. Wärme ist Energie, und diese scheint nicht durch die (kalte) Platte durch Kontakt übertragen worden sein: Es muss durch etwas anderes passiert sein.

> Unterhalte dich mit deinem Partner bevor du weiterliest: Wie könnte die Energie übertragen werden?

Elektrische Felder sind den Gravitationsfeldern ähnlich (wenn auch ungleich stärker): Mit dem Abstand nimmt die übertragbare Energie ab, eine Spule an der einen Stelle kann „Elektronen zum tanzen bringen“ an einer anderen Stelle. Die Felder haben eine bestimmte Energie (was ungefähr dasselbe ist wie die Frequenz für Physik-Bewanderte unter euch) die zu Radiofrequenzen gehört.

Die Grundlage von NFC ist nun — und der Grund warum eure Kreditkarte (sollte sie einen NFC-Tag besitzen) nie leer geht — ist, dass sowohl Kommunikation als auch Energie über das Medium elektrisches Feld übertragen werden. Ein Kommunikationspartner in NFC, der keinen Strom selbst hat, sondern ihn von seinem Kommunikationspartner bekommt, heißt „passiv“. Der Chipleser heißt „aktiv“. 

 Das elektrische Feld nimmt aber sehr schnell ab mit steigendem Abstand. Daher bekommt NFC seinen Namen (**Near** Field Communication): Nur in wenigen Zentimetern Abstand kann die Kommunikation stattfinden. 

## Standards/Normen
Was sich in einer Industrie durchsetzt, heißt **Industriestandard**. Ein wenig formaler als das noch sind die von Fachleuten erarbeiteten und von bekannten Institutionen veröffentlichten **Normen**. Auch die technischen Grundlagen von NFC sind in einer **Norm** festgelegt (ISO 15693). Normen nach Brockhaus:

> Normung, in der Industrie die Vereinheitlichung von Benennungen, Kennzeichen, Formen, Größen, Abmessungen und Beschaffenheit von Industrieerzeugnissen. Ziel: Verringerung der Sortenzahlen, einfachere Lagerhaltung, Verbilligung der Herstellung, leichtere Ersatzbeschaffung und Austauschbarkeit. Normen sind verpflichtende Empfehlungen. Die Normungsarbeit in Deutschland wird vom Deutschen Institut für Normung e.V. DIN durchgeführt. In Europa bilden das Europäische Komitee für Normung (CEN) und das Europäische Komitee für Elektrotechnische Normung (CENELEC) die Gemeinsame Europäische Normeninstitution.

> Beantworte die folgenden Fragen mit einem Partner
> Welcher der Gründe für Normung, die im Enzyklopädie-Eintrag genannt werden, sind für Kommunikationsprotokolle am wichtigsten? 
> Was sind bekannte DIN-Normen, die ihr kennt?
> Recherchiere, was die größte Normungsorganisation der Welt ist.
> Was bedeutet ISO DIN EN mit einer Zahl dahinter?

Die größte Normungsinstitution der Welt ist die ISO(griechisch iso=gleich). Sie wurde 1947 gegründet und ist eine internationale Organisation, in der in der Regel Vereine Mitglieder sind, jedoch nur einer pro Land. Die Umsetzung von Normen ist in den Ländern freiwillig. Die ISO hat in sehr vielen wichtigen Bereichen Normen herausgegeben.

> Mache eine Liste mit 5 wichtigen ISO-Normen aus dem Internet.

Wir haben unten Gründe für Normen gesehen. Es stellt sich aber tatsächlich die Frage, warum es nicht für alles eine Norm gibt.

> Mache eine Mindmap, warum nicht alles normiert ist. Was sind Gründe dagegen? Stimmen diese Gründe wahrscheinlich/wahrscheinlich nicht/nicht für NFC?

## NFC als Norm
Schaue dir die Norm ISO18092 an und bearbeite die folgenden Aufgaben:

> In welcher Sektion finde ich Abkürzungen?
> Übersetze sinngemäß die Einleitung.
> Wie heißt der Typ von Diagramm in Figure 3?
> Erkläre Figure 3 in eigenen Worten. Lies nach, wenn dir Informationen fehlen.
> Wo ist erklärt, was eine UID ist?
> Was heißt in den Anhängen „normativ“ und „informativ“?

Jetzt habt ihr ein paar Bruchstücke der Norm verstanden, und in der Kürze der Zeit erschlägt sie. Wir wollen sie dennoch einmal vergleichen mit einer anderen Norm, die auch relevant werden könnte für euch: ISO17789 zu Cloud Computing.

> Fasst zusammen: Welche Inhalte/Sektionen gibt es in beiden? Was sind Gemeinsamkeiten? Was sind Unterschiede?


Wir haben uns also angeschaut, wie NFC technisch funktioniert, uns Gründe für Standardisierung angesehen und die Struktur einer internationalen Norm herausgearbeitet.

Nächstes Mal könnt ihr wieder basteln: Diesmal zum Teil im Internet und zum Teil selbst mit NFC.


Feedback Pollmeier: https://goo.gl/forms/4ZMMbR2E6Ta8ONCZ2
# IoT-Projekt V: NFC, Datenkapselung und erste Web-Schritte
Letzte Woche und im Vortrag haben wir uns mit Standardisierung beschäftigt, Industrie 3.0 und 4.0 kennengelernt und einen Demonstrator gesehen, der mit vielen Bauteilen vernetzte Einheiten in einer Fabrik veranschaulicht. 

Heute wollen wir kurz das Thema NFC abschließen und ein neues Kapitel aufschlagen: Internet.

Unsere Ziele sind:

 - Code zur Ansteuerung eines externen NFC-Moduls erklären können.
 - einen ESP8266 mit einem lokalen Access Point verbinden können.
 - Datenkapselung definieren und in Zusammenhang mit der Ansteuerung von Bauteilen des Arduino dessen Vorteile erklären können.


# NFC (mehr oder weniger) in Aktion
Wir haben uns letzte Woche bereits mit NFC als Standard beschäftigt. Die Norm gibt sehr genau Wellenlängen mit denen kommuniziert werden sollen an. Der folgende Code liest einen Tag:

```
#include <Wire.h>
#include <PN532_I2C.h>
#include <PN532.h>
#include <NfcAdapter.h>
PN532_I2C pn532_i2c(Wire);
NfcAdapter nfc = NfcAdapter(pn532_i2c);
void setup(void) {
    Serial.begin(9600);
    nfc.begin();}
void loop(void) {
    NfcTag tag = nfc.read();
    tag.print();
    delay(5000);}
```

Der Tag kann beliebige Binärstrings einer beschränkten Länge enthalten. Betrachten wir den Code genauer. Die Library `PN532` erlaubt, auf einen Chip zuzugreifen, den PN532, der NFC-Karten auslesen kann. Wire erlaubt, Sensoren anzusteuern, die über I2C funktionieren. Dies ist ein Datenbus, also eine Verbindung, über die Daten fließen. Sein Prinzip ist, dass eine Seite (in unserem Fall der Adafruit Feather) immer die Kommunikation initiiert, und die andere Seite (der PN532) immer zuhört. Dies nennt man auch *Master-Slave*. Die Zeile `PN532_I2C pn532_i2c(Wire);` erlaubt eine andere Pin-Zuordnung für diese Kommunikation als standardmäßig vorgesehen ist (indem wir `Wire` geben, nutzen wir aber die Standardwerte). Die Zeile `NfcAdapter nfc = NfcAdapter(pn532_i2c);` kreiert einen neuen NFC-Adapter als Objekt und gibt ihm das Chip-Objekt `pn532_i2c` mit. Den `nfc.begin()` heißt dann, dass die Kommunikation mit dem Chip aufgenommen wird. Interessant ist noch, dass ein Typ `NfcTag` genutzt wird. Dies ist sinnvoll, da ein Tag erst einmal keine leserlichen Daten geben muss und je nach Implementierung des NFC-Tags diese Daten unterschiedlich sein können. Bei einer Ausgabe in Klartext mittels `tag.read()` muss aber laut Standard ausgewertet werden. 

> Kommentiere den nachfolgenden Code ähnlich. Du wirst `NdefMessage` googeln müssen. Welche anderen Methoden als `addUriRecord` hat dieser Typ?

```
#include <Wire.h>
#include <PN532_I2C.h>
#include <PN532.h>
#include <NfcAdapter.h>
PN532_I2C pn532_i2c(Wire);
NfcAdapter nfc = NfcAdapter(pn532_i2c);
void setup() {
      Serial.begin(9600);
      nfc.begin();}
void loop() {
	Serial.println("\nPlace NFC tag.");
	if (nfc.tagPresent()) {
	    NdefMessage message = NdefMessage();
	    message.addUriRecord("http://google.de");
	    bool success = nfc.write(message);
	    if (success) Serial.println("Success.");       
	    else Serial.println("Write failed.");}
	delay(5000);
}
```
  
Dies ist erst einmal alles zu NFC-Tags. Es ist gut möglich, dass wir noch eine weitere Hardware-Komponente benötigen, um NFC zum Laufen zu bringen.

Schauen wir einmal zurück und bemerken ein Prinzip: Datenkapselung.
# Datenkapselung und Informationsversteckung im IoT-Projekt bisher
Es war immer sehr einfach, verschiedene Komponenten in Code anzusteuern. Wir müssen uns nicht anschauen, wie genau NFC funktioniert; der Typ `NFCAdapter` hat Methoden `begin()`, `tagpresent()` und `read()` die erlauben, typische Anfragen an einen NFC-Adapter zu stellen. Bei der Real-Time-Clock haben wir die Methoden `now()` und `unixtime()` genutzt, bei der SD-Karte `open()` und `close()`. Diese Anforderungen sollte man an alle sinnvollen NFC-Leser, Real-Time-Clocks und SD-Karten-Schreiber haben. Damit unsere User nicht von einer genauen internen Funktionsweise eines NFC-Lesers, einer Real-Time-Clock oder eines SD-Karten-Lesers ist, gibt es *Datenkapselung*.

> Aufgabe: Beantworte aus https://en.wikipedia.org/wiki/Information_hiding#Example_of_information_hiding die folgenden Fragen: Was ist ein Interface in diesem Text? Nenne mindestens drei Beispiele, die im Text genannt werden. Wo habt ihr bei der Arbeit mit solchen Interfaces zu tun? 

Datenkapselung ist eines der Prinzipien von *objektorientierter Programmierung*, welche euch noch viel begegnen wird. Alan Kay, der den Begriff „objektorientiert“ mit geprägt hat, hat die folgende Definition abgegeben. Beim Lesen, ersetze gerne „Klasse“ durch „Typ“ und „Objekt“ durch „Variable“, wenn es sich dann für dich leichter liest. Beantworte die folgenden Fragen:

> Welche Nachrichten haben Typen, die für Bauteile für den ESP stehen, gesendet und erhalten (2.)? Was mussten diese Variablen speichern (3.)? 

 1. Everything is an object.
 2. Objects communicate by sending and receiving messages (in terms of objects)
 3. Objects have their own memory (in terms of objects)

# ESP8266 mit lokalem Access Point verbinden und ihn als Access Point nutzen
Um unseren Werkzeugkasten zu komplettieren (abgesehen von analogen Sensoren und Aktoren), und um euch auf die Nutzung des Chips für ein echtes IoT-Projekt vorzubereiten, wollen wir erste Schritte ins Internet gehen. Als erstes: Der ESP8266 kann Informationen zur Verfügung stellen. 

> Kommentiere den nachfolgenden Code. Finde durch Googeln heraus, was die Zahlen 200 und 80 bedeuten. Was bedeutet `<h1>`? Was bedeutet `“text/html"` und was wären hier Alternativwerte?


```  
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
ESP8266WebServer server(80);
void handleRoot() {
  server.send(200, "text/html", "<h1>You are connected</h1>");
}
void setup() {
  Serial.begin(115200);
  WiFi.softAP("ESP-AccesPoint");
  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);
  server.on("/", handleRoot);
  server.begin();
}
void loop() {
  server.handleClient();
}
```

Verbindet euch mit dem Netzwerk „ESP“ (hiervon wird es mehrere geben) und besucht mit einem Browser `http://192.168.4.1`.

Wir wollen uns genauer anschauen, was die Zahlen bedeuten. Die Zahl 80 ist der *Port*, auf dem der Server sendet, die Zahl 200 ist der Statuscode, der sagt „alles in Ordnung“. 

> Lege eine Tabelle mit anderen Statuscodes und Ports an, die du bereits genutzt hast.

Heute haben wir zwei Stücke Code zum Lesen und Beschreiben von NFC-Karten betrachtet, Datenkapselung als Prinzip, welches die Arbeit mit unseren Mikrocontrollern so einfach macht identifiziert und das Internet angesteuert.

# IoT-Projekt VI: Web Server, Web Client, Sniffing
Letzte Woche haben wir uns mit NFC und den Vorzügen von Datenkapselung beschäftigt sowie einen ersten Access Point aufgebaut.

Heute wollen wir zwei Mikrocontroller miteinander kommunizieren lassen — über das Internet: Einer wird den Server spielen, einer wird den Client spielen. Ein Computer wird mithören. Vielleicht werden sie aneinander vorbeireden, vielleicht nicht. Wir haben am Ende in jedem Fall einiges gesehen, um Internetprotokoll genauer unter die Lupe zu nehmen.

Ablauf: 10min Plickers, 15min Definitionen, 45min Gruppenarbeit, 15min Vorstellung, 5min Abschluss

Unsere Ziele sind:

 - Web-Client, Web Server, Access Point definieren können.
 - Wiresharks Funktionsweise erklären können
 - Einen Anteil an einem ferngesteuerten System bauen.


Zuerst ein wenig Theorie, diesmal in Form eines Glossars.

## Wichtige Begriffe für Kommunikation in Netzwerken

 - Access Point: Wireless Access Point (englisch für drahtloser Zugangspunkt), auch Access Point (AP) oder Basisstation genannt, ist ein elektronisches Gerät, das als Schnittstelle für kabellose Kommunikationsgeräte fungiert. Endgeräte stellen per Wireless Adapter (Drahtlosadapter) eine drahtlose Verbindung zum Wireless Access Point her, der über ein Kabel mit einem fest installierten Kommunikationsnetz verbunden sein kann. Für gewöhnlich verbinden Wireless Access Points Notebooks und andere mobile Endgeräte mit eingebautem Wireless Adapter über ein Wireless Local Area Network (WLAN, Funknetz) mit einem Local Area Network (LAN) oder einem anderen kabelgebundenen Datennetz (Telefonnetz, Kabelfernsehnetz).
 - Web Server: The server component provides a function or service to one or many clients, which initiate requests for such services. Servers are classified by the services they provide. For example, a web server serves web pages and a file server serves computer files. A shared resource may be any of the server computer's software and electronic components, from programs and data to processors and storage devices. The sharing of resources of a server constitutes a service.
 - Web Client:  Ein Client (über englisch client aus lateinisch cliens wörtlich für „Kunde“) – auch clientseitige Anwendung, Clientanwendung oder Clientprogramm – bezeichnet ein Computerprogramm, das auf dem Endgerät eines Netzwerks ausgeführt wird und mit einem Server (Zentralrechner) kommuniziert. Man nennt auch ein Endgerät selbst, das Dienste von einem Server abruft, Client. Das Gegenstück zum Client ist das jeweilige Serverprogramm bzw. der Server selbst. 
 - Sniffing: A packet analyzer (also known as a packet sniffer) is a computer program or piece of computer hardware that can intercept and log traffic that passes over a digital network or part of a network. Packet capture is the process of intercepting and logging traffic. As data streams flow across the network, the sniffer captures each packet and, if needed, decodes the packet's raw data, showing the values of various fields in the packet, and analyzes its content according to the appropriate RFC or other specifications. A packet analyzer used for intercepting traffic on wireless networks is known as a wireless analyzer or WiFi analyzer. A packet analyzer can also be referred to as a network analyzer or protocol analyzer though these terms also have other meanings.


**Aufgabe**: Suche dir einen Partner. Übersetze einen Text deiner Wahl vom Englischen ins Deutsche, einen Diener Wahl vom Deutschen ins Englische. Nutze hierfür ein Etherpad unter der Adresse etherpad.wikimedia.org/p/bsgg-itm-deinname. Lasse danach deinen Partner deinen Text korrigieren. Sprecht über eure Korrekturen.

## Web Client, Web Server und Access Points
Heute arbeitet ihr in drei Gruppen. Die Aufgaben jeder Gruppe sind (45min):

1. Bringt den Code der Gruppe zum Laufen und ergänzt ihn um sinnvolle Ausgaben auf `Serial`
2. Definiert aus der Gruppe einen Verantwortlichen 
	3. für die Kommunikation mit der jeweils anderen Gruppe, 
	4. die das Ergebnis in einem Code Review vorstellen wird,
	5. die den Code entsprechend des Arduino Style Guide endabnehmen wird
3. Ihr macht ein Code Review. Kopiert ihn hierfür in einer kommentierten Fassung nach HackMD.io

Hier sind die einzelnen Gruppen
### Gruppe 1: Access Point und WireShark
Ihr richtet einen Feather Huzzah! als Access Point ein und snifft alle Verbindungen über dieses Netzwerk. Wir werden die Analyse eurer Ergebnisse nächste Stunde machen.

```c
#include <ESP8266WiFi.h>
const char *ssid = "ITM";
void setup() {
  Serial.begin(115200);
  WiFi.softAP(ssid);
  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);}
void loop() {}
```

Öffnet WireShark und monitort das Netzwerk. Nutzt hierfür auch Herrn Trautmanns Wissen. 

### Gruppe 2: Web Server
Ihr richtet den Adafruit Feather Huzzah! als Server ein, der ein Licht anmacht, wenn er eine Anfrage erhält.

```c
#include <ESP8266WiFi.h>
const char* ssid = "ITM";
WiFiServer server(80);
void setup() {
  Serial.begin(115200);
  pinMode(2, OUTPUT);
  digitalWrite(2, 0);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid);
  server.begin();
  Serial.println(WiFi.localIP()); //Gebt diese an die andere Gruppe
}
void loop() {
  WiFiClient client = server.available();
  if (!client || !client.available()) {
    return;
  }
  String req = client.readStringUntil('\r');
  Serial.println(req);
  client.flush();
  int val;
  if (req.indexOf("/gpio/0") != -1) { // "/gpio/0" is a substring of req
    val = 0;
  } else if (req.indexOf("/gpio/1") != -1) {// "/gpio/1" is a substring of req
    val = 1;
  } else {
    Serial.println("invalid request");
    return;
  }
  digitalWrite(2, val);
  client.flush();
  String s = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<!DOCTYPE HTML>\r\n<html>\r\nGPIO is now ";
  s += (val) ? "high" : "low";
  s += "</html>\n";
  client.print(s);
}
```

### Gruppe 3: Web Client
Ihr richtet einen Client ein, der eine Anfrage an einen Server schickt, je nachdem, ob ein Schalter gedrückt ist.

```c
#include <ESP8266WiFi.h>
const char* ssid  = "ITM";
const char* host = ""; //Bekommt ihr von der Gruppe "Server"
void setup() {
  pinMode(4, INPUT);
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println(WiFi.localIP());
}
void loop() {
  WiFiClient client; //Creates TCP connection
  if (!client.connect(host, 80)) {
    Serial.println("connection failed");
    delay(5000);
    return;
   }
  Serial.println("sending data to server");
  String value = static_cast<String>(digitalRead(4));
  value = "/gpio/" + value;
  client.println(value);
  Serial.println("receiving from server");
  while (client.available()) {
    char ch = static_cast<char>(client.read());
    Serial.print(ch);
  }
  client.stop();
  delay(300000);
}
```

Wir haben uns heute mit drei Rollen beschäftigt: Access Points, Web-Servern und Web-Clients — und wir haben Daten für nächstes Mal gesammelt. Dann beginnt die Netzwerk-Analyse.