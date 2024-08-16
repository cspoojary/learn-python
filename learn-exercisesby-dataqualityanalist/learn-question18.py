#  18. Write a Python program to perform the following operations: 
# a) Create a list with 10 numbers 
# b) Use a for loop to calculate the sum of the numbers in the list.

list1=[2,4,65,3,8]
type(list1)
num=1
for element in list1:
    num = sum(list1)
print("The total sum of the elemet is ",num)