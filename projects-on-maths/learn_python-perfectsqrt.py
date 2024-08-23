import math
def is_perfect_square(x):
    sqrt_value=math.sqrt(x)
    return int(sqrt_value) ** 2==x

number=int(input("Enter a number:"))
testing_number=1 + 8 * number
if is_perfect_square(testing_number):
    print("It is a triangular number.")
else:
    print("It is not a triangular number.")