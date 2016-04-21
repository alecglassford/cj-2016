import csv
import re
from xml.etree import ElementTree

import requests

url = 'https://fortress.wa.gov/esd/warnrss/'
desc_pattern = re.compile(r'(.*)\(\s*(.*)\)\s*will lay off (\d+)\s*employees, effective (.*)<br>.*Date of Notification: (.*)<\/font>')

resp = requests.get(url)
root = ElementTree.fromstring(resp.text[3:]) # some weird Unicode char at front
channel = root[0]
total = 0
with open('warn_wa.csv', 'w') as outfile:
    outcsv = csv.writer(outfile)
    outcsv.writerow(['Company', 'Location', 'Num Employees', 'Date of Effect',
                     'Date of Notification']) # Header
    for item in channel.findall('item'):
        desc = item.find('description')
        match = desc_pattern.search(desc.text)
        if match:
            outcsv.writerow(match.groups())
            try:
                total += int(match.group(3))
            except:
                print('Could not extract num employees from', desc.text)
        else:
            print('Could not extract info from', desc.text)
print (total, 'individuals affected')
