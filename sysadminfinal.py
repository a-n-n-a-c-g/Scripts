Teachers = ['Dale Rowe', 'Chia-Chi Teng', 'J Ekstrom', 'Barry Lunt', 'Richard Helps', 'Russel Havens' , 'Derek Hansen', 'Mike Miles', 'Val Hawkes']
print Teachers
sortedlistofteachers = sorted(Teachers, key=lambda x: x.split(" ")[-1])
print sortedlistofteachers
removedteachers = sortedlistofteachers[:len(sortedlistofteachers)-2]
print removedteachers
