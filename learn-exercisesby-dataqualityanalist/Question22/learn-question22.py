#  22. Write a program to find the power of a number using recursion.

def power(x,y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x ** y
print(" The power is:",power(4,3))