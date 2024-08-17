#3. Write a Python program that checks if a given number is positive, negative, or zero. 
#    a) Take an integer input from the user.
#  b) Use if-elif-else statements to check the number and print whether it is positive, negative, or zero. 

userInput = input("Enter a integer:")

num = int(userInput)

if num < 0:
    print("The inputted number is negative")
elif num > 0:
    print("The inputted number is positive")
else:
    print("The inputted number is zero")