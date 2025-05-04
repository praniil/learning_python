import numpy as np
from scipy.signal import convolve

six_by_six = np.random.randint(1, 50, 36)
# print(len(six_by_six))
new_six_by_six = six_by_six.reshape((6, 6))
print(new_six_by_six)

three_by_three = np.array([1, 0, -1, 1, 0, -1, 1, 0, -1])
# print(three_by_three)
new_three_by_three = three_by_three.reshape((3, 3))
print(new_three_by_three)


convolved = convolve(new_six_by_six, new_three_by_three, mode='valid')
print(convolved)
