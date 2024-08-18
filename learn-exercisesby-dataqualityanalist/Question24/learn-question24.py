# 24. Write a Python program to test whether a passed letter is a vowel or not.

string1 = input("Enter the string:  ")

vowels = 'aeiouAEIOU'

count = 0
for i in string1:
    if i in vowels:
        count = count+1

print("Total numbers of vowels:",count)