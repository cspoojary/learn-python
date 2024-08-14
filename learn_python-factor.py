import math

number = int(input("Enter a number:  "))
factors= []

for i in range(1, int(math.sqrt(number)) + 1):
    if number % i == 0:
        factors.append(i)
        factors_pair = number // i   
        if factors_pair != 0:
            factors.append(factors_pair)

factors.sort()
print(factors)