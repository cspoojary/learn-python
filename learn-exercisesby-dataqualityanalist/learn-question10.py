# 10. Write a Python program to perform the following operations: 
# a) Prompt the user to input their age. 
# b) Classify the age into one of the following categories: 
#    Child (0-12 years) 
#    Teenager (13-19 years) 
#    Adult (20-64 years) 
#    Senior (65 years and above) 
# c) Print the category based on the input age.

age=int(input("Enter Your age:  "))

if age <= 12:
    categorie = "Child"
elif 13 <= age <= 19:
    categorie = "Teenager"
elif 20 <= age <= 64:
    categorie = "Adult"
else:
    categorie = "senior"
print("The age of",age,"is under the ",categorie,"category")