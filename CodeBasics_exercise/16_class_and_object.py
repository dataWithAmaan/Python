# Exercise: https://github.com/codebasics/py/blob/master/Basics/Exercise/16_class_and_objects/16_class_and_object_exercise.md
class Employee():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        print("employee name: ",name)
        print("employee id: ",id)

    def __del__(self):
        print("id deleted")
        print("emp object deleted")
emp = Employee(1, "coder") 

del id
del emp