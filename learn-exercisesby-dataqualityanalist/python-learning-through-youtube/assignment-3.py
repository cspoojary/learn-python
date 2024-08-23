#write a code to sort the array in ascending order.
array = [2, 6, 1, 9, 8, 5]
array.sort()
print("The sorted array is:",array)

print("------------------------------")


#Write a code to find a factorial of a given number

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
num = int(input("Enter a element to get factorial:"))
print("The factorial of",num,"is",factorial(num))


