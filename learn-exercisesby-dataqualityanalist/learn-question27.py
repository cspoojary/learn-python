# 27. Create a 2-D array called myarray using arange() having 14 rows and 3 columns with
# start value = -1, step size 1 having. And print the result of the following:
# a. Sum of all elements
# b. Sum of all elements row wise
# c. Sum of all elements column wise
# d. Max of all elements
# e. Min of all elements in each row
# f. Mean of all elements in each row

import numpy as np

start_value = -1
step_size = 1
num_rows = 14
num_columns = 3
num_elements = num_rows * num_columns

array_1d = np.arange(start_value, start_value + num_elements * step_size, step_size)

myarray = array_1d.reshape((num_rows, num_columns))

print("2-D Array (myarray):")
print(myarray)

# a. Sum of all element
sum_all_elements = np.sum(myarray)
print("Sum of all elements:", sum_all_elements)

# b. Sum of all elements row-wise
sum_row_wise = np.sum(myarray, axis=1)
print("Sum of all elements row-wise:", sum_row_wise)

# c. Sum of all elements column-wise
sum_column_wise = np.sum(myarray, axis=0)
print("Sum of all elements column-wise:", sum_column_wise)

# d. Max of all elements
max_all_elements = np.max(myarray)
print("Max of all elements:", max_all_elements)

# e. Min of all elements in each row
min_each_row = np.min(myarray, axis=1)
print("Min of all elements in each row:", min_each_row)

# f. Mean of all elements in each row
mean_each_row = np.mean(myarray, axis=1)
print("Mean of all elements in each row:", mean_each_row)
