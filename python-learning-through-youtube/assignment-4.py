# Create an array with 5 values an detect the value at index numbers 2 without using in built function.
array= [4,6,8,7,9]

index = 2
value_of_index = None

for i in  range(5):
    if i == index:
        value_of_index = array[i]
        break
print("Value at index 2 is:",value_of_index)



