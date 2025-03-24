#sin, cos, exp
#element wise operation
import numpy as np

array = np.arange(start=0, stop=12, step=0.5, dtype=float).reshape(6, 4)
print(array)
#sin
print("element wise sin", np.sin(array))
print("element wise exp", np.exp(array))
print("element wise cos", np.cos(array))

