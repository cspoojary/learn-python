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