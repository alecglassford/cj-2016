import requests
from csv import DictReader
year = 2015 # Change to look at different year
url = 'http://stash.compjour.org/samples/stops-and-frisks/{}-nypd.csv'.format(year)
filename = '{}-nypd.csv'.format(year)

crimes = [  'contrabn',
            'pistol',
            'riflshot',
            'asltweap',
            'knifcuti',
            'machgun',
            'othrweap'  ]

resp = requests.get(url)
with open(filename, 'w') as f:
    f.write(resp.text)

with open(filename, 'r') as f:
    datarows = list(DictReader(f))

print ('Numbers for', year)

total = len(datarows)
print('Total number of stops:', total)

def innocent(row):
    for crime in crimes:
        if row[crime] != 'N':
            return False
    return True

num_innocent = 0
for row in datarows:
    if innocent(row):
        num_innocent +=1
print('Number/percent of people stopped who were totally innocent:',
        num_innocent, round(100 * num_innocent/float(total)), '%')

num_black = 0
for row in datarows:
    if row['race'] == 'B':
        num_black +=1
print('Number/percent of people stopped who were black:',
        num_black, round(100 * num_black/float(total)), '%')

num_hispanic = 0
for row in datarows:
    if row['race'] == 'P' or row['race'] == 'Q':
        num_hispanic +=1
print('Number/percent of people stopped who were Hispanic:',
        num_hispanic, round(100 * num_hispanic/float(total)), '%')

num_white = 0
for row in datarows:
    if row['race'] == 'W':
        num_white +=1
print('Number/percent of people stopped who were white:',
        num_white, round(100 * num_white/float(total)), '%')
