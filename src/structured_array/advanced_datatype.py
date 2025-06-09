import numpy as np

dt = np.dtype([
    ('position', [('x', 'f4'), ('y', 'f4')]),
    ('velocity', 'f4')
])

dt2 = np.dtype([('a', 'i1'), ('b', 'i4')], align = True)

data = np.array([((2, 3), 45), ((3, 4), 10)], dtype=dt)
print(data[0])
print(data[1])
print(data['position'])
print(data['velocity'])

data2 = np.array([(2, 3), (2, 5)], dtype=dt2)
print(data2)

dt3 = np.dtype([('name', 'U10'), ('sport', 'U10'), ('score', 'i4')])
data3 = np.array([('Alice', 'Basketball', 10), ('Bob', 'Football', 4)], dtype=dt3)
#sorting
sorted_data3 = np.sort(data3, order='score')

print(data3)
print(sorted_data3)

#filtering
score_greater_than_4 = data3[data3['score'] > 4]
print(score_greater_than_4)

#iteration
for row in data3:
    print(row['name'], row['score'])
    
    