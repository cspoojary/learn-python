# 6. Write a Python program to perform the following operations: 
# a) Prompt the user to input their weight (in kg) and height (in meters). 
# b) Calculate the Body Mass Index (BMI) using the formula: 
#  BMI = weight / (height ** 2). 
# c) Classify the BMI according to the following categories: 
# Underweight (BMI < 18.5)
# Normal weight (18.5 <= BMI < 24.9)
# Overweight (25 <= BMI < 29.9)
# Obesity (BMI >= 30)
# d) Print the BMI and its classification.

import math
x= int(input("Enter the weight in Kg: "))
y= float(input("Enter the height in meter: "))
classification= ""
BMI = x/(y ** 2)
if BMI < 18.5:
    classification ="Underweight"
elif  18.5 <= BMI < 24.9:
    classification="Normal weight"
elif 25 <= BMI < 29.9:
    classification="Over weight"
else:
    classification="Obesity"

print("The BMI is", round(BMI, 2),"and","Classification is:",classification)