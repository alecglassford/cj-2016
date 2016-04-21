import csv
from collections import Counter

################################################################################

with open('breach_report.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    total = 0
    for row in reader:
        affected = row["Individuals Affected"]
        try:
            total += int(affected)
        except ValueError:
            print(affected, 'is not an integer')
    print(total, 'total individuals affected')

################################################################################

with open('breach_report.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    individuals_per_year = Counter()
    for row in reader:
        try:
            year = int(row["Breach Submission Date"][-4:])
        except ValueError:
            print("Couldn't extract year from", row["Breach Submission Date"])
            continue
        try:
            affected = int(row["Individuals Affected"])
        except ValueError:
            print("Couldn't extract year from", row["Individuals Affected"])
            continue
        individuals_per_year[year] += affected
    print(individuals_per_year)
    print('{},{}'.format('year', 'individuals affected'))
    for year in sorted(individuals_per_year.keys()):
        print('{},{}'.format(year, individuals_per_year[year]))


################################################################################

physical_words = ['paper', 'film']
electronic_words = ['network', 'server', 'computer', 'desktop', 'laptop', 'electronic']

def is_physical(location):
    location = location.lower()
    for word in physical_words:
        if word in location:
            return True
    return False

def is_electronic(location):
    location = location.lower()
    for word in electronic_words:
        if word in location:
            return True
    return False

with open('breach_report.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    counts = Counter()
    for row in reader:
        try:
            affected = int(row["Individuals Affected"])
        except ValueError:
            print("Couldn't extract year from", row["Individuals Affected"])
            continue
        location = row["Location of Breached Information"]
        if is_physical(location):
            counts['physical'] += affected
        if is_electronic(location):
            counts['electronic'] += affected
    print(counts)
