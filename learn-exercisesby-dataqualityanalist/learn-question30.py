# 30. Create a 3x3 NumPy array with values ranging from 1 to 9. Then, find the sum of all elements in the array.

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])
newarr = arr.reshape(3,3)

print("Reshaped array is: ",newarr)
print("The sump of the array:", np.sum(arr))