import numpy as np

a_type = np.dtype([('name', 'U10'), ('roll', 'i4'), ('id', 'i8'), ('hobby', 'S3')])     #number of fields 4
a_data = np.array([('Pranil', 29, 1, 'APGP'), ('AG', 16, 2, 'APGP'), ('AKG', 16, 2, 'APGP')], dtype=a_type)

b_type = np.dtype([('name', 'U10'), ('roll', 'i4'), ('id', 'i8'), ('hobby', 'S3')])     #number of fields 4
b_data = np.array([('Bob', 2, 12, 'playing'), ('Oscar', 16, 2, 'watching football'), ('Alice', 1, 22, 'esports')], dtype=b_type)

b_data[:] = a_data
print(b_data)