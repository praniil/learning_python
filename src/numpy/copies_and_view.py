import numpy as np

x = np.arange(10)
print(x)

y = x[1: 3] #creating the view
print(y)

x[1: 3] = [11, 12]  #changing the actual data buffer
print(x)

print(y)    #y gets change as x changes because y is a view

x1 = np.arange(9).reshape(3, 3)
print(x1)

y1 = x1[[1, 2]]
print(y1)

x1[[1, 2]] = [[10, 11, 12], [55, 56, 57]]
print(x1)
print(y1)


x2 = np.array([1, 2, 3, 4, 5])
cpy = x2.copy()
viw = x2.view()

print(cpy.base)     #every NumPy array has the attribute base that returns none if the array owns the data
print(cpy)
print(viw.base)


array = np.array([[1, 2, 3], [2, 3, 4]])
print(array.shape)

reshape_array = array.reshape(3, 2)
print(reshape_array.shape)

transpose_array = array.T
print(transpose_array.shape)

resphape_transpose_array = transpose_array.reshape(2, 3)
print(resphape_transpose_array.shape)

resphape_transpose_array[[0, 1]] = [[1, 1, 1], [1, 1, 1]]   #copy changes will not reflect to the original array
print(resphape_transpose_array.reshape(2, 3))

print("transpose array", transpose_array.reshape(2, 3))

reshape_array[[0, 1, 2]] = [[2, 2], [2, 2], [2, 2]]  #view changes will reflect to the original array
print(reshape_array.reshape(2, 3))

print(array)