# Abstraction and Encapsulation
class car():
    def __init__(self):
        self.acc = False
        self.clutch = False
        self.brk = False
    def start(self):
        self.acc = True
        self.clutch = True
        print("Car started")

c1 = car()
c1.start()