import numpy as np

#np.zeros()
zeros_array = np.zeros(6)
print(zeros_array.shape)
print(zeros_array.size)
print(zeros_array.ndim)
print(zeros_array)

#np.ones()
ones_array = np.ones(6)
print(ones_array)

#empty() this is used instead over zeros is speed
#later on fill the arrays accordingly
array_from_empty = np.empty(4)
print(array_from_empty)

for item in array_from_empty:
    print(item - item + 1)

#random stuffs
new_item = [item * 2 for item in array_from_empty]
print(new_item)

print(array_from_empty)

array_from_empty[:] = [1, 3, 3, 4]
print(array_from_empty)
