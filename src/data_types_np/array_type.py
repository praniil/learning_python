import numpy as np

array1 = np.arange(1, 9, 2, dtype=np.float16)
print(array1)

#represent using character code
array2 = np.arange(4, dtype='d')
print(array2)

#converting the type
new2 = array2.astype(np.int16)
print(new2)

#numpy knows that int is numpy.int
new1 = array1.astype(int)
print(new1)