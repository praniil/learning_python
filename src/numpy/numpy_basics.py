import array as arr
import numpy as np
from numpy import pi

array1 = arr.array('l', [1, 2, 3, 4])       #array is homogeneous i.e. can store only one kind of datatype
for i in array1:
    print(i)
print(type(array1))


np_array = np.arange(2, 10).reshape(2, 2, 2)
print(np_array)
print(np_array.ndim)
print(np_array.shape)
print(np_array.dtype)
print(np_array.size)
print(type(np_array))


# np_array1 = np.array([[1, 2, 3], ["pranil", "nil"]])    this throws error. inhomogeneous shape after 1 dimensions
np_array1 = np.array([(1, 2, 3), (3, 4, 5)], dtype= complex)
print(np_array1)
print(np_array1.shape)
print(np_array1.ndim)
print(np_array1.dtype)


array_between = np.linspace(0, 2 * pi, 9)    #gives 9 elements between 0 and 2

print(np.sin(array_between))

print(array_between)