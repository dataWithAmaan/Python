# Exercise: https://github.com/codebasics/py/blob/master/Basics/Exercise/17_inheritance/17_inheritance.md
class Animal():
    def __init__(self,eat):
        self.eat = eat
class Dog(Animal):
    def __init__(self,pet,eat):
        self.pet = pet
        super().__init__(eat)

dog = Dog("dog", "animal eats raw meat")
print(dog.pet, dog.eat)
