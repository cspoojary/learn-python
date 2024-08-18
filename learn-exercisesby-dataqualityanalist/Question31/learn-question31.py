# 31. Create a 1D NumPy array of 10 random integers between 10 and 50. Replace all odd numbers in the array with -1.

import numpy as np

arr = np.random.randint(10,50,10)
print(arr)
arr[arr % 2 != 0] = -1
print(arr) 