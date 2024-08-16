# 7. Write a Python program to perform the following operations: 
# a) Prompt the user to input a grade (between 0 and 100). 
# b) Determine the letter grade based on the following scale: 
#    90 and above: A 
#    80 to 89: B 
#    70 to 79: C 
#    60 to 69: D 
#    Below 60: F 
# c) Print the corresponding letter grade.


userInput = int(input("Enter your Grade:  "))

if userInput >= 90:
    Grade = "A"
elif 80 < userInput <= 89:
    Grade = "B"
elif 70 < userInput <= 79:
    Grade = "C"
elif 60 < userInput <= 69:
    Grade = "D"
else:
    Grade = "F"

print("The corresponding  Grade is",Grade,"to mark of",userInput)