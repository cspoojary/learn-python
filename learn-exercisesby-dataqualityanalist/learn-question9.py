# 9. Write a Python program to perform the following operations on a set: 
# a) Create a set of the first 5 odd numbers. 
# b) Add the next odd number to the set. 
# c) Remove the smallest number from the set. 
# d) Check if the number 7 is in the set.


odd_number={1,3,5,7,9}
print("Initial_set: ",odd_number)
odd_number.add(11)
print("Second_set: ",odd_number)
odd_number.remove(min(odd_number))
print("Third set: ",odd_number)
if 7 in odd_number:
    print("7 is in the set")
else:
    print("& is not in the set")
