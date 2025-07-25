#element wise arithmetic operation
import numpy as np
a = np.arange(0, 4)
b = np.arange(4)
print(a - b)

c = np.array([[1, 2, 3], [4, 5, 6]]).reshape(3, 2)
print(c * 2)    #element wise product

d = np.array([5, 5, 5, 5])
print(d.ndim)
print(d.shape)
e = np.array([1])
print(e.shape)
print(d + e)    #should broadcast e into the shape 1, 4
print((d + e).shape)


#dot product
a1 = np.array([[1, 2, 3], [4, 5, 6]])
z = np.dot(np.transpose(a), a)
print(z)

#add two arrays
array1 = np.array([1, 2, 3])
array2 = np.array([1, 2, 3])
add_ = array1 * array2
print(add_)

#reshape() we give -1 as argument
test_array = np.array([[1, 2, 3], [2, 3, 4]])
print(test_array)
print(test_array.shape)
yo = test_array.reshape(3, -1)
print(yo)
print(test_array.shape)
print(yo.shape)

#min, max, sum
any_array = np.arange(10).reshape(2, 5)
print(any_array)
print(np.sum(any_array))
print(np.min(any_array))
print(np.max(any_array))

cumulative_array = np.cumsum(any_array)
print(cumulative_array)     #cumulative sum of elements