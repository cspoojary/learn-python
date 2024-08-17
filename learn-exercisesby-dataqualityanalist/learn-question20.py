# 20. Write a Python program to perform the following operations: 
# a) Prompt the user to input the current hour (24-hour format). 
# b) Print a greeting based on the time of day: 
#    Morning (5 AM - 11:59 AM) 
#    Afternoon (12 PM - 4:59 PM) 
#    Evening (5 PM - 8:59 PM) 
#    Night (9 PM - 4:59 AM)

Time = float(input("Enter the Current hour (on 24 hours format): "))

if 5 <= Time < 12:
            greeting = "Good morning!"
elif 12 <= Time < 17:
            greeting = "Good afternoon!"
elif 17 <= Time < 21:
            greeting = "Good evening!"
else:
            greeting = "Good night!"

print ("The time is",Time,"so", greeting)