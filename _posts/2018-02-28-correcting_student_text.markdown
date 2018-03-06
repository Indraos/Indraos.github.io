---
layout: post
title:  "Correcting Texts Using wdiff"
date:   2018-01-26 00:26:05 +0100
categories: learn
---
You would like to correct a lot of student texts that they handed in in as a digital text. They can't use office software as they work on their smartphones and do not have the necessary software. You do not want to use pdf, but plain text. 
<!--more-->
We describe a workflow to get text, correct text and get an html from which you can copy text to return to students.
# A Solution for UNIX systems
Assume the texts are in a directory `texts` and that your system has `pandoc`and `nano` installed. Start with
```bash
cd texts
mkdir old
mv *.txt old/
cp -r old/ new/
cd new
sublime *.txt
```
You can also replace `sublime` with your favorite editor. Correct the student text and save. Then run:
```bash
mkdir ../corrections
for FILE in *.txt
 do wdiff -w '<em>' -x '</em>' -y '<strike>' -z '</strike>' $FILE ../old/$FILE | pandoc -o ../corrections/$FILE.html
 done
```
Open the html files and paste the text. 
