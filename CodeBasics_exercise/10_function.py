# Exercise: https://github.com/codebasics/py/blob/master/Basics/Exercise/10_functions/10_functions_exercise.md
# Q1=>
def Area():
    base = int(input("Enter base: "))
    height = int(input("Enter height: "))
    area = 1/2 * base * height
    print("Area of triangle is: ", area)
Area()

# Q2=> 
x = input("Enter Shape: ")
def Area1():
    base = int(input("Enter base: "))
    height = int(input("Enter height: "))
    area = 1/2 * base * height
    print("Area of triangle is: ", area)

def Area2():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    print("Area of rectangle is: ", area)

if x=="triangle":
    Area1()
elif x=="rectangle":
    Area2()
    
# Q3=> 
n = int(input("Enter value for n: "))
for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()