# the innit method 
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
c1 = Car("black",400)
print(c1.color)
print(c1.mileage)

c2 = Car("Red",300)
print(c2.color)
print(c2.mileage)