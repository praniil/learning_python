import numpy as np

#define a structured data type
dt = np.dtype([('id', 'i4'), ('name', 'U10'), ('score', 'f4')])

#create an array
data = np.array([(1, 'Alice', 80), (2, 'Bob', 90.0)], dtype=dt)

print(data)

#nested fields
nested_dtype = np.dtype([('name', 'U10'), ('grades', [('math', 'i4'), ('science', 'i4')])])
data2 = np.array([('Alice', (90, 85)), ('Bob', (79, 99))], dtype= nested_dtype)
print(data2)

print(data2['name'])
print(data2[0])
print(data2[1]['grades'])

data2[0]['name'] = 'Pranil'
print(data2['name'])