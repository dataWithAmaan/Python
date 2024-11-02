# impact of class attribute
#Method 1
class Person:
    name = "anonymous"

    def changename(self, name):
        Person.name = name #Changing the value of the variable

    # Method 2
    # def changename(self,name)
    # self.__class__.name = 'John'
p1 = Person()
p1.changename("John")
print(p1.name)
print(Person.name)



# Method 3
class Person:
    name = "anonymous"

    @classmethod
    def changename(cls, name):
        cls.name = name #Changing the value of the variable

p1 = Person()
p1.changename("John")
print(p1.name)
print(Person.name)