from glob import glob
from os import path
import re

BRIEFS_DIR = 'briefs'
isis_pattern = re.compile(r'\bisi[sl]\b', flags=re.IGNORECASE)
date_pattern = re.compile(r'20\d\d-\d\d-\d\d')
filenames = glob(path.join(BRIEFS_DIR, '*.html'))

def date_sorter(url):
    dates = date_pattern.findall(url)
    if dates:
        return dates[0]
    return 0 # If no date, assume earlier

results = []
for fname in filenames:
    with open(fname, 'r') as rf:
        txt = rf.read()
        if isis_pattern.search(txt):
            results.append(fname)
results.sort(key=date_sorter)
# Print all undated urls + earliest dated one
for result in results:
    print(result)
    if date_pattern.search(result):
        break

# I'm getting briefs/the-press-office-2013-10-31-press-briefing-press-secretary-jay-carney-10312013.html
