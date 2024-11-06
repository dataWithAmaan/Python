# Q1. Define a circle with rad r using a constructor 
# Calculate area and perimeter with seperate classes
from math import pi
class Circle:
    def __init__(self,r):
        self.r = r

    def area(self):
        area = pi * self.r**2
        return area

    def perimeter(self):
        perimeter = 2 * pi * self.r
        return perimeter

obj = Circle(2)
print("Area:", obj.area())
print("Perimeter:", obj.perimeter())