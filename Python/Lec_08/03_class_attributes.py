# Class attribute 
class student:
    college_name = "ABC College" #common for all the objects 
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print(f"Welcome {self.name} to {student.college_name}")

s1 = student("Amaan",91)
print(s1.name,s1.marks)
print(s1.college_name)
s1.welcome() 