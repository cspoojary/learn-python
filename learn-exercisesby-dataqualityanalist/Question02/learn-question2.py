#2. Define two functions max_of_three() and min_of_three() that takes 
#  three numbers as arguments and returns the largest and smallest of them. 

def max_of_three(a,b,c):
    if a>=b and a>=c:
        print("Maximum of a,b,c is:",a)
    elif b>=a and b>=c:
        print("Maximum of a,b,c is:",b)
    else:
       print("Maximum of a,b,c is:",c)
max_of_three(12,13,9)

def max_of_three(a,b,c):
    if a<=b and a<=c:
        print("Manimum of a,b,c is:",a)
    elif b<=a and b<=c:
        print("Minimum of a,b,c is:",b)
    else:
       print("Minimum of a,b,c is:",c)
max_of_three(12,13,9)


    