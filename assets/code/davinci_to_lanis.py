import sys # Um Argumente auf der Kommandozeile zu nutzen
import xlrd # für den Excel-Import
import pandas as pd # Für Tabellen-Manipulationen
import datetime as t # Für Kalenderwoche und Zeiten
import numpy # Für Vektorisierung

# definitions
weekdaytoind = {'Montag': 1, 'Dienstag': 2, 'Mittwoch': 3, 
                'Donnerstag': 4, 'Freitag': 5, 'Samstag': 6, 
                'Sonntag': 7}
begintimetolesson = {t.time(7,30): 1, t.time(8,15): 2, t.time(9, 15): 3,
                     t.time(10,0): 4, t.time(11,0): 5, t.time(11,45): 6,
                     t.time(13,0): 7, t.time(13,45): 8, t.time(14,45): 9,
                     t.time(15,30): 10,t.time(16,30): 11,t.time(17,15): 12}
endtimetolesson = {t.time(8,15): 1, t.time(9,0): 2, t.time(10,0): 3, t.time(10,45): 4,
                   t.time(11,45): 5, t.time(12,30): 6,t.time(13,45): 7, t.time(14,30): 8,
                   t.time(15,30): 9,t.time(16,15): 10,t.time(17,15): 11,t.time(18,0): 12}
timestolesson = numpy.vectorize(lambda x,y: 
                                str(begintimetolesson[x]) + '-' + str(endtimetolesson[y]) 
                                if begintimetolesson[x] != endtimetolesson[y] 
                                else str(begintimetolesson[x]))

def weekstoab(x):
    '''
    weekstoab:
    input: Formatierter String
    output: '', 'A', 'B' oder numpy.nan
    Falls diese und nächte Woche Unterricht ist, zeige an, als sei immer Unterricht.
    Falls in dieser Woche oder nächste Woche Unterricht ist und dort eine Abfolge von Unterricht-kein Unterricht-Unterricht
    beginnt, so schreibe A, falls die Kalenderwoche, in der Unterricht it, ungerade ist, und B, fals sie gerade ist.
    Sonst zeige an, es sei nie Unterricht.
    '''
    if not str(x)[0]=='(': # 'Jede Woche' mapped to empty Wochen entry
        return ''
    parseranges = lambda x: list(range(int(x.split('-')[0]),int(x.split('-')[1])+1)) if '-' in x else [int(x)]
    x = sum(list(map(parseranges, x[1:-1].split(','))),[])
    kw = t.date.today().isocalendar()[1] # get calendar week
    if not (kw in x or kw+1 in x): # if none of the next two weeks is a lesson, drop the lesson
        return numpy.nan
    elif kw in x and kw+1 in x: # if both of the next two weeks is lesson assume lesson is every week
            return ''
    elif min( (y for y in x if y in x and not y+1 in x and y+2 in x and y >= kw), default=numpy.nan) <= kw+1:
        return 'A' if min(y for y in x if y in x and not y+1 in x and y+2 in x and y >= kw)%2 else 'B'
    else:
        return numpy.nan
    
# load data
with open(sys.argv[1],'rb') as infile:
    df = pd.read_excel(infile)
    
# manipulation
df.dropna(subset=['Tag'], inplace=True) # keine Mitteilungen(=keine Zeit zugeordnet)
df.dropna(subset=['Klasse'], inplace=True) # keine Aufsichten(=keine Klasse)
df.dropna(subset=['Lehrer'], inplace=True) # keine Stunden ohne Lehrkraft
df.dropna(subset=['Raum'], inplace=True) # kein Unterricht ohne Raum

df = df.loc[df['Wochen'] != 'Einmalig'] # keine einmaligen Veranstaltungen
df['Lehrerkuerzel'] = df['Lehrer']
df['Kurs'] = df['Klasse']
df['Woche'] = df['Wochen'].apply(weekstoab)
df.dropna(subset=['Woche'], inplace=True) # Unterrichtseinheiten, die derzeit nicht stattfinden entfernen
df['Klassen'] = df['Klasse']
df['Id'] = range(0,df.index.size) # create index
df['Art'] = 'Stunde' # keine Aufsichten, nur Stunden
df['Wochentag'] = df['Tag'].apply(lambda x: weekdaytoind[x]) # coding weekday as number
df['Stunde'] = timestolesson(df['Von'], df['Bis']) # coding times as lessons
df = df[['Id','Art', 'Lehrerkuerzel','Fach','Kurs','Raum',
         'Wochentag','Stunde','Woche','Klassen']] # Spalten in Reihenfolge bringen

# write data
df.to_csv('output.csv', sep=';',index=False,header=True,encoding='utf-8')