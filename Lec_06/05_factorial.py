# def function for factorial 

def Calculate_fact():
    x = int(input("Enter a number: "))
    fact = 1
    for i in range(1, x+1):
        fact *= i
    print("Factorial of", x, "is", fact)

Calculate_fact()
