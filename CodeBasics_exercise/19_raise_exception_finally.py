# Exercise: https://github.com/codebasics/py/blob/master/Basics/Exercise/19_raise_exception_finally/19_raise_exception_finally.md
class AdultException(Exception):
    pass

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        if age > 18:
            print(f"{self.name} is major")
        else:
            raise AdultException(f"{self.name} is minor")

try:
    person1 = Person("John", 20)
    print(person1.name)
    print(person1.age)
    person2 = Person("Denver", 10) #Exception Thats why code directly jumps to the exception block
    print(person2.name)
    print(person2.age)

except AdultException as e:
    print(e)

finally:
    print("Code Completed!!")