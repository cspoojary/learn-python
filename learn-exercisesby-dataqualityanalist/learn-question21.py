# 21. Write a program to find area of Circle, Rectangle ,and a Square using functions.
import math

def area_of_circle(radius):
    return math.pi * radius ** 2

def area_of_rectangle(length, width):
    return length * width

def area_of_square(side):
    return side ** 2

# Circle
radius = float(input("Enter the radius of the circle: "))
print("Area of the circle:" , area_of_circle(radius))

# Rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print("Area of the rectangle:", area_of_rectangle(length, width))

# Square
side = float(input("Enter the side length of the square: "))
print("Area of the square:", area_of_square(side))
print("Thank You")