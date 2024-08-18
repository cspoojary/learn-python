# 19. Write a Python function to return a new list with each element squared if it is even, and cubed if it is odd.

def even_odd( elements ):
    new_list= []

    for x in elements:
        if x % 2 == 0:
            new_list.append( x ** 2)

        else:
            new_list.append( x ** 3) 

    return new_list

list = [1,4,7,5,9,8]
result = even_odd(list)
print("The transformed list is:",result)
