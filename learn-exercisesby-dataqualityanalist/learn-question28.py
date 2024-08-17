#  28. Write a function to check if a given string is a palindrome.


def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    string1 = ''.join(c.lower() for c in s if c.isalnum())
    
    # is string1  is equal to reverse string
    return string1 == string1[::-1]

userInput = input("Enter a string to check if it is a palindrome: ")
if is_palindrome( userInput ):
    print(f"'{userInput}' is a palindrome.")
else:
    print(f"'{userInput}' is not a palindrome.")
