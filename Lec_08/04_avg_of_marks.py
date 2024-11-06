# create a class that takes the name and marks of 3 subjects. Create the method to print the average 

# class students:
#     def __init__(self, name, marks1, marks2, marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3
#     def average(self):
#         avg = (self.marks1 + self.marks2 + self.marks3) / 3
#         return avg
# s1 = students("Alok",45,43,50)
# print("Name: ", s1.name)    
# print("Average: ", s1.average())


#other method to take marks
class students:

    @staticmethod
    def college():
        print("ABC College")
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def average(self):
        sum = 0  # Initialize sum
        for i in self.marks:  # Use self.marks instead of marks
            sum += i
        avg = sum / len(self.marks)
        return avg  # Move return statement outside the for loop

students.college()
s1 = students("Alok", [45, 43, 50])
print("Name: ", s1.name)
print("Average: ", s1.average())  
