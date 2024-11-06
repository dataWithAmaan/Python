# Inheritance Understanding
# Single Inheritance
class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class Toyota(Car):   #Inherited from car class
    def __init__(self,name):
        self.name = name

car1 = Toyota("Fortuner")
car1.start()
car1.stop() 