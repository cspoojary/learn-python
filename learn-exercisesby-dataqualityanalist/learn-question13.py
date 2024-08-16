# 13. Write a Python program to perform the following operations on a list: 
# a) Create a list of the first 5 prime numbers. 
# b) Append the next prime number to the list. 
# c) Remove the second prime number from the list. 
# d) Sort the list in descending order

prime_numbers=[2,3,5,7,11]
print("Initial list",prime_numbers)
prime_numbers.append(13)
print("Secomd list",prime_numbers)
prime_numbers.remove(prime_numbers[1])
print(prime_numbers)
sorted_number=sorted(prime_numbers, reverse= True)
print(sorted_number)