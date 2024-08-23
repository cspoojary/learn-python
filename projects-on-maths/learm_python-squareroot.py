import math

def is_perfect_square(x):
    sqrt_value=math.sqrt(x)
    return int(sqrt_value) ** 2== x

number=int(input("Enter a number:  "))
if is_perfect_square(number):
    print("Number is a perfect square")
else:
    print("Number is not a perfect square")