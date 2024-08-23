# 14. Write a Python program to perform the following operations: 
# a) Create a list of elements 
# b) Use a for loop to multiply all the items in a list 
# c) Use a while loop to count down from 5 to 1 and print each number 1

element= [2,3,5,4,6]
print("Initail list: ",element)
product=1
for items in element:
    product *= items
print("The product of the item is:",product)

count = 5
while count > 0:
    print(count)
    count -= 1