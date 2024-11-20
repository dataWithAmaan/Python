# Exercise: https://github.com/codebasics/py/blob/master/Basics/Exercise/18_multiple_inheritance/18_multiple_inheritance.md
class Teacher():
    def teach(self):
        return "Teaching is my profession"
class Youtuber():
    def stream(self):
        return "I stream teaching videos"
class Student(Teacher,Youtuber):
    def study(self):
        return "I am doing Engineering"

student = Student()
print(student.teach())
print(student.stream())
print(student.study())

