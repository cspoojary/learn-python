#1.Accept a list of integer values separated by a space and calculate the sum and average of the numbers in the list: 
# a) Using built in function 
# b) Using for loop

integers = input("Enter integers separated by spaces: ")
integers = integers.split()
print("Enterd inputs: ",integers)
n=len(integers)
sum=0
for x in integers:
    sum = sum + int(x)
avg = sum // n
print("sum of integers: ",sum)
print("average of numbers: ",avg)