# 11. Write a Python program to perform the following operations: 
#     a) Use a for loop to print first 10 even numbers. 
for i in range(20):
    if i % 2 ==0:
        print(i)
#     b) Use a for loop to calculate the sum of the first 5 positive integers
sum=0
for i in range(5):
    sum += i
print("The sum of the first positive number",sum)
