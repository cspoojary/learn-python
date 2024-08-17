
# 23. Write a python program to create a array of all the even integers from 30 to 70. And display the 
#     dimension, shape, datatype and print it in the reverse order.


import numpy as np
even_numbers = np.arange(30, 71, 2)

print("The list is:",even_numbers)
print("Dimension:", even_numbers.ndim)
print("Shape:", even_numbers.shape)
print("Datatype:", even_numbers.dtype)


print("Array in reverse order:", even_numbers[::-1])