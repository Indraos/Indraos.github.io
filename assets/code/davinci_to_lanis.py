import sys # Um Argumente auf der Kommandozeile zu nutzen
import xlrd # für den Excel-Import
import pandas as pd # Für Tabellen-Manipulationen
import datetime as t # Für Kalenderwoche und Zeiten
import numpy # Für Vektorisierung

# definitions
weekdaytoind = {'Montag': 1, 'Dienstag': 2, 'Mittwoch': 3, 
                'Donnerstag': 4, 'Freitag': 5, 'Samstag': 6, 
                'Sonntag': 7} # Lanis Online-Kodierung der Wochentage
begintimetolesson = {t.time(7,30): 1, t.time(8,15): 2, t.time(9, 15): 3,
                     t.time(10,0): 4, t.time(11,0): 5, t.time(11,45): 6,
                     t.time(13,0): 7, t.time(13,45): 8, t.time(14,45): 9,
                     t.time(15,30): 10,t.time(16,30): 11,t.time(17,15): 12} # Stunden-Beginnzeiten zu Stunden
endtimetolesson = {t.time(8,15): 1, t.time(9,0): 2, t.time(10,0): 3, 
                   t.time(10,45): 4, t.time(11,45): 5, t.time(12,30): 6,
                   t.time(13,45): 7, t.time(14,30): 8, t.time(15,30): 9,
                   t.time(16,15): 10,t.time(17,15): 11,t.time(18,0): 12} # Stunden-Endzeiten zu Stunden
timestolesson = numpy.vectorize(lambda x,y: 
                                str(begintimetolesson[x]) + '-' + str(endtimetolesson[y]) 
                                if begintimetolesson[x] != endtimetolesson[y] 
                                else str(begintimetolesson[x])) # Funktion, die Einzelstunden und Doppelstunden 
                                                                # mit '-' oder als Einzelstunde passend darstellt.
ab = lambda x: 'A' if x%2 == 1 else 'B' # Kodierung der Wochen

def weeklists(x):
    """
    weeklists
    input: Formatierter String
    output: Liste
    Bringe formatierte Liste mit Bindestrichen in Liste
    """
    if str(x)[0] != '(': # 'Jede Woche'-Eintrag wird als Regelunterricht betrachtet
        return list(range(53))
    parseranges = lambda x: list(range(int(x.split('-')[0]),int(x.split('-')[1])+1)) if '-' in x else [int(x)]
    return sum(list(map(parseranges, x[1:-1].split(','))),[]) # Kriege eine Liste mit allen Wochen, 
                                                              # in denen Unterricht stattfindet

def weekstoab(x):
    '''
    weekstoab:
    input: Liste
    output: '', 'A', 'B' oder numpy.nan
    Nähert Unterricht in beliebigen Wochenzuteilungen durch A- und B-Wochen sowie Regelunterricht an.
    '''   
    kw = t.date.today().isocalendar()[1] # Kriege Kalenderwoche
    kw = min(y for y in range(54) if y not in holidays and y >= kw) # wird der Stundenplan in den Ferien aktualisiert, behandeln wir die Anfrage, als sei sie in der ersten Woche nach den Ferien gestellt.
    if kw+1 in holidays:   # in der letzten Schulwoche werden alle stattfindenden Stunden 
                           # als wöchentlich betrachtet, alle anderen als inexistent
        if kw in x:
            return ''
        else:
            return numpy.nan
    elif kw+2 in holidays:   
        if kw in x and kw+1 in x:
            return ''
        elif kw in x and kw+1 not in x:
            return ab(kw)
        elif kw not in x and kw+1 in x:
            return ab(kw+1)
        else:
            return numpy.nan
                           # in der vorletzten Schulwoche werden alle Stunden, die in beiden Wochen stattfinden als
                           # Regelunterricht betrachtet, Unterricht, der in genau einer Woche stattfindet als A-/B-Wochen-Unterricht
                           # und Unterricht, der in beiden Wochen nicht stattfindet als inexistent.
    else:
        if kw in x and  kw+1 not in x and kw+2 in x:
            return ab(kw)
        elif kw not in x and kw+1 in x and kw+2 not in x:
            return ab(kw+1)
        elif kw in x and kw+1 in x:
            return ''
        else:
            return numpy.nan
                           # alle anderen Wochen betrachten wir als ausreichend weit vor den Ferien. Diese werden als
                           # A-/B-Woche betrachtet, falls entweder der Unterricht in den nächsten drei Wochen wie
                           # Unterricht-kein Unterricht-Unterricht bzw. kein Unterricht-Unterricht-kein Unterricht ist.
                           # Falls die nächsten beiden Wochen Unterricht ist, so wird der Unterricht als Regelunterricht
                           # angenommen, sonst als nicht existent.
    
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

holidays = list(set(range(53)).difference(set(sum(df['Wochen'][df['Wochen']!='Jede Woche'].apply(weeklists),[]))))
df['Woche'] = df['Wochen'].apply(weeklists)
df['Woche'] = df['Woche'].apply(weekstoab)

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