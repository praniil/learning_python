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