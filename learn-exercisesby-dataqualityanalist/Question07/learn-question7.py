# 7. Write a Python program to perform the following operations: 
# a) Use a for loop to print numbers from 1 to 10. 
# b) Skip printing the number 5 using loop control statement. 

i=1
for i in range(10):
   if i == 5:
     continue
   print(i)