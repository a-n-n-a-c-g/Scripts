Teachers = ['First1 Last1', 'First2 Last2', 'First3 Last3', 'First4 Last4', 'First5 Last5', 'First6 Last6' , 'First7 Last7', 'First8 Last8', 'First9 Last9']
print Teachers
sortedlistofteachers = sorted(Teachers, key=lambda x: x.split(" ")[-1])
print sortedlistofteachers
removedteachers = sortedlistofteachers[:len(sortedlistofteachers)-2]
print removedteachers
