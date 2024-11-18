# super() method to call parebt function 
class Car:
    def __init__(self, type):
        self.type = type

class Toyota(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)

car1 = Toyota("Pirus", "electric")
print(car1.name, car1.type)