# Error Handling (Extra Study)
# source: https://www.youtube.com/watch?v=V_NXT2-QIlE

try:
    number = int(input("enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Program ended")
