# Polymorpism 
# Operator Overloading
#Create a function to add complex nos
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def showNumber(self):
        print(f"{self.real} i + {self.imag} j")

    def __add__(num1, num2): #use of dunder functions
        newReal = num1.real+num2.real
        newImag = num1.imag+num2.imag
        return ComplexNumber(newReal,newImag)

a = ComplexNumber(1,3)
a.showNumber()
b = ComplexNumber(2,4)
b.showNumber()

c = a + b
c.showNumber()

