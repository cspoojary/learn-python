#  26) Write a program to read a collection of integers from the user using List. Display all the 
#      negative numbers followed by all the zeroes and the positive numbers using three lists to
#      store the negative, zero and positive values.
negatives = []
zeroes = []
positives = []

input_string = input("Enter a collection of integers separated by spaces: ")
number_string = input_string.split()

for num_str in number_string:
     try:
          number = int(num_str)

          if number < 0:

            negatives.append(number)
          elif number == 0:
            zeroes.append(number)
          else:
            positives.append(number)
     except ValueError:
        print(f"Warning: '{num_str}' is not a valid integer and will be skipped.")

print("Negative numbers:", negatives)
print("Zeroes:", zeroes)
print("Positive numbers:", positives)