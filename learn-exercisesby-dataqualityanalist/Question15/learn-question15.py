# 15. Write a Python program to perform the following operation: 
# a) Define a function called average that takes a variable number of arguments and returns their average.


def average(*argument):

    if len(argument) == 0:
        return 0
    total = sum(argument)
    avg = total / len(argument)
    return avg
result = average(30,40)
print(result)
 