# 4. Write a Python program to perform the following operations on a set and a dictionary: 
# a) Create a set of even numbers between 1 and 20. 
# b) Add the number 22 to the set. 
# c) Remove the number 8 from the set. 
# d) Create a dictionary with keys as strings and values as their lengths for the words: "apple", "banana", "cherry". 
# e) Update the dictionary by adding a new key-value pair for the word "date".


even_num = {2,4,6,8,10,12,14,16,18,20}
print(even_num)
even_num.add(22)
print(even_num)
even_num.remove(22)
print(even_num)

dict1 = { "banana" : len("banana"),
         "apple": len("apple"),
         "cherry" :len("cherry")}
print(dict1)
dict1["date"]= len("date")
print(dict1)


#Dow program also works.
#Value=["banana", "apple", "cherry"]
#dict1 = {value : len(value) for value in Value}
#print(dict1)
