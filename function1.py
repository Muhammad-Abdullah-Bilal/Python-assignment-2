import math
def circle_area(r):
    if radius < 0:
        return "Radius cannot be negative"
    else:
        return math.pi * r**2

radius = int(input("Enter radius of a circle:"))    
print("The area of the circle is:", circle_area(radius))
