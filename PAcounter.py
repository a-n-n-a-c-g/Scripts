import csv
import collections as c

m = []

r = csv.reader(open('log.csv','r'))
next(r) #skip headers
for z in r:
    m.append(z[11])
print(c.Counter(m))
