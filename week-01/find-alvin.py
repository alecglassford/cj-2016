import requests
from csv import DictReader
year = 2011 # Change to look at different year
url = 'http://stash.compjour.org/samples/stops-and-frisks/{}-nypd.csv'.format(year)
filename = '{}-nypd.csv'.format(year)

resp = requests.get(url)
with open(filename, 'w') as f:
    f.write(resp.text)

with open(filename, 'r') as f:
    datarows = list(DictReader(f))

def match_date(row):
    return row['datestop'] == '632011'

count = 0
for row in datarows:
    if match_date(row): count+=1
print(count)
