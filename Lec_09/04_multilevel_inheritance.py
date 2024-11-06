# Multilevel Inheritance
class Grandfather:
    @staticmethod
    def display():
        print("Grandfather")

class Father(Grandfather):
    @staticmethod
    def show():
        print("Father")

class son(Father):
    @staticmethod
    def prt():
        print("Son")

c = son()
c.prt()
c.show()
c.display()
