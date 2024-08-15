# 5. Write a Python program to perform the following operations on a dictionary: 
# a) Create a dictionary with three key-value pairs representing a person's name, age, and city. 
# b) Update the age to 30. 
# c) Add a new key-value pair for the person's profession. 
# d) Remove the city from the dictionary. 

person={
    "name" : "Chethan",
    "age"  : 25,
    "city" : "Mangalore"
}
person["age"]=30
print(person)
person["Proffesion"]="Web developer"
print(person)
person.pop("city")
print(person)