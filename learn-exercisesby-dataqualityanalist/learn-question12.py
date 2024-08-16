# 12. Write a Python program to perform the following operations: 
# a) Define a recursive function called factorial that takes a number as an argument and returns its factorial. 
# b) Call the factorial function with the number 4 and print the result.

def factorial(n):
    if n== 0 or n== 1:
        return 1
    else:
        return n*factorial(n-1)
print("The factorial is",factorial(5))
