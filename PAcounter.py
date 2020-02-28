import csv
from collections import Counter

rules = []

with open('../log.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) #skip headers
    for row in reader:
        rules.append(row[11])
    print (Counter(rules))
