# 8. Write a Python program to perform the following operations: 
# a) Define a function named reverse_string that takes a string as a parameter and returns the string reversed. 
# b) Call the function with the string "hello" and print the result. 
# c) Call the function with the string "world" and print the result.

def reverse_string(s):
    reverse_s =""
    for letter in s:
        reverse_s = letter + reverse_s
    print("The reversed string is",reverse_s)
reverse_string('Hello')
reverse_string("World")
