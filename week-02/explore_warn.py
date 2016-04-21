import csv

import requests
import pdfplumber

################################################################################
# Downloading

urls = [
    'http://www.edd.ca.gov/jobs_and_training/warn/WARN-Report-for-7-1-2015-to-03-25-2016.pdf',
    'http://www.edd.ca.gov/jobs_and_training/warn/WARNReportfor7-1-2014to06-30-2015.pdf',
    'http://www.edd.ca.gov/jobs_and_training/warn/WARN_Interim_041614_to_063014.pdf',
    'http://www.edd.ca.gov/jobs_and_training/warn/eddwarncn14.pdf',
    'http://www.edd.ca.gov/jobs_and_training/warn/eddwarncn13.pdf',
    'http://www.edd.ca.gov/jobs_and_training/warn/eddwarncn12.pdf'
]

filenames = []
for i, url in enumerate(urls):
    print('Downloading', url)
    resp = requests.get(url)
    filename = 'warn-{}.pdf'.format(i)
    with open(filename, 'wb') as save_file:
        save_file.write(resp.content)
    print('Saved to', filename)
    filenames.append(filename)

################################################################################
# CSV building + counting
total = 0

with open('warn-2012-2014.csv', 'w') as outfile:
    outcsv = csv.writer(outfile)
    outcsv.writerow(['Company Name', 'Location', 'Employees\nAffected',
                     'Layoff\nDate']) # Manually write header
    for filename in filenames[3:]:
        pdf = pdfplumber.open(filename)
        for i, page in enumerate(pdf.pages):
            print ('Extracting page', i + 1, 'from', filename)
            table = page.extract_table()
            for row in table:
                if i == 0: continue # Skip header on first page of each doc
                try:
                    total += int(row[2])
                except:
                    print('Couldn\'t get num employees from', row)
                outcsv.writerow(row)
print(total, 'employeed affected from 2012-2014 dataset')

# Don't count totals from here, because precalculated in pdf
# These pdfs don't seem to have their tables extracted as well...
with open('warn-2014-2016.csv', 'w') as outfile:
    outcsv = csv.writer(outfile)
    outcsv.writerow(['Notice Date', 'Effective', 'Received', 'Company', 'City',
                     'No. of Employees', 'Layoff/Closure']) # Manually write header
    for filename in filenames[:3]:
        pdf = pdfplumber.open(filename)
        for i, page in enumerate(pdf.pages):
            print ('Extracting page', i + 1, 'from', filename)
            table = page.extract_table()
            for row in table:
                if i == 0: continue # Skip header on first page of each doc
                outcsv.writerow(row)

print(total + 53454 + 61491 + 12896) # Add precalculated totals from 2014-2016
print('employees affected total')
